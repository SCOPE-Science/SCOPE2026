#!/usr/bin/env python3
import json
import pathlib
import subprocess
import tempfile

root = pathlib.Path(__file__).resolve().parent
cert = json.loads((root / "certificate.json").read_text(encoding="utf-8"))
with tempfile.TemporaryDirectory() as td:
    exe = pathlib.Path(td) / "verify"
    subprocess.run(
        ["g++", "-O3", "-std=c++17", str(root / "verify.cpp"), "-o", str(exe)],
        check=True,
    )
    p = subprocess.run([str(exe)], check=True, text=True, capture_output=True)
out = p.stdout.strip()
required = [
    "VERIFY_OK",
    "states=5",
    "alphabet=2",
    "proper=1",
    f"one_cluster_maps={cert['number_of_total_one_cluster_maps']}",
    f"candidates={cert['candidate_ordered_labeled_automata']}",
    f"synchronizing={cert['carefully_synchronizing_candidates']}",
    f"max_threshold={cert['maximum_shortest_careful_reset_length']}",
    f"boundary_labeled={cert['labeled_extremizers']}",
    f"isomorphism_classes={cert['number_of_isomorphism_classes']}",
    "engines=2",
]
for token in required:
    assert token in out, token
print(out)
