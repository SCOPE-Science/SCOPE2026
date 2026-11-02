#!/usr/bin/env python3
"""Reproduce exact Platonic two-leak forcing and minimal-fort polynomials."""
import json
import pathlib
import re
import shutil
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
GRAPHS = ("tetrahedral", "cubical", "octahedral", "dodecahedral", "icosahedral")
EXPECTED = json.loads((ROOT / "baseline_counts.json").read_text(encoding="utf-8"))


def parse_count_map(value):
    return {key: int(number) for key, number in re.findall(r"(\d+):(\d+)", value)}


def graph_data(name):
    data = (ROOT / "graphs" / (name + "_graph.txt")).read_text(encoding="utf-8")
    rows = [tuple(map(int, row.split())) for row in data.splitlines()]
    n, m = rows[0]
    assert n <= 20 and len(rows) == m + 1
    edges = [tuple(sorted(pair)) for pair in rows[1:]]
    assert len(set(edges)) == m and all(0 <= u < v < n for u, v in edges)
    degrees = [0] * n
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    assert len(set(degrees)) == 1
    assert (n, m, degrees[0]) == {
        "tetrahedral": (4, 6, 3),
        "cubical": (8, 12, 3),
        "octahedral": (6, 12, 4),
        "dodecahedral": (20, 30, 3),
        "icosahedral": (12, 30, 5),
    }[name]
    # Explicit graph-isomorphism certificates against combinatorial standard models.
    if name == "cubical":
        phi = (0, 1, 3, 2, 4, 6, 7, 5)
        canonical = {tuple(sorted((u, v))) for u in range(8) for v in range(u+1, 8)
                     if ((u ^ v).bit_count() == 1)}
    elif name == "dodecahedral":
        phi = (0, 1, 2, 12, 14, 4, 3, 13, 11, 19, 9, 8, 7, 17, 15, 5, 6, 16, 18, 10)
        canonical = set()
        for i in range(10):
            canonical.update(tuple(sorted(pair)) for pair in
                             ((i, (i+1) % 10), (i, 10+i), (10+i, 10+(i+2) % 10)))
    elif name == "icosahedral":
        phi = (0, 1, 10, 11, 7, 2, 6, 4, 5, 9, 8, 3)
        canonical = set()
        for i in range(5):
            canonical.update(tuple(sorted(pair)) for pair in
                             ((0, 1+i), (11, 6+i), (1+i, 1+(i+1) % 5),
                              (6+i, 6+(i+1) % 5), (1+i, 6+i), (1+i, 6+(i-1) % 5)))
    elif name == "tetrahedral":
        phi = tuple(range(4))
        canonical = {(u, v) for u in range(4) for v in range(u+1,4)}
    else:
        phi = tuple(range(6))
        # The octahedral graph is the complement of a perfect matching.
        nonedges = {(u, v) for u in range(6) for v in range(u+1,6)} - set(edges)
        assert len(nonedges) == 3 and {u for e in nonedges for u in e} == set(range(6))
        canonical = set(edges)
    assert len(set(phi)) == n
    transformed = {tuple(sorted((phi[u], phi[v]))) for u, v in edges}
    assert transformed == canonical, (name, "noncanonical graph")
    return data


def check_output(stdout, name):
    matches = []
    for row in stdout.splitlines():
        hit = re.fullmatch(
            r"leaks=(\d+) Z=(\d+) optimal=(\d+) witness=(\d+) minimal_bad_size:(.*?) goodSizes:(.*)",
            row.strip(),
        )
        assert hit is not None, (name, row)
        ell = hit.group(1)
        data = {
            "Z": int(hit.group(2)),
            "optimal": int(hit.group(3)),
            "witness_mask": int(hit.group(4)),
            "minimal_fort_sizes": parse_count_map(hit.group(5)),
            "forcing_sizes": parse_count_map(hit.group(6)),
        }
        assert data == EXPECTED[name][ell], (name, ell, data)
        assert data["optimal"] == data["forcing_sizes"][str(data["Z"])], name
        matches.append(ell)
    assert matches == ["0", "1", "2"], (name, matches)


def main():
    assert shutil.which("g++"), "C++17 g++ compiler required"
    with tempfile.TemporaryDirectory(prefix="platonic_verification_") as td:
        binaries = []
        for src in ("enumerate.cpp", "direct_check.cpp"):
            binary = pathlib.Path(td) / src.replace(".cpp", "")
            subprocess.run(["g++", "-std=c++17", "-O2", str(ROOT / src), "-o", str(binary)], check=True)
            binaries.append(binary)
        for graph in GRAPHS:
            text = graph_data(graph)
            output = subprocess.run(binaries[:1], input=text, text=True, capture_output=True, check=True)
            check_output(output.stdout, graph)
            direct = subprocess.run(binaries[1:], input=text, text=True, capture_output=True, check=True)
            assert direct.stdout.startswith("DIRECT_CHECK_OK n="), (graph, direct.stdout, direct.stderr)
            print(graph, "ALL_CHECKS_OK", direct.stdout.strip())
    print("ALL_EXACT_CHECKS_OK")


if __name__ == "__main__":
    main()
