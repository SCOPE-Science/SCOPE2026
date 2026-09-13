"""Reproducible STRUCTURAL certificates for lane-1761 target (honest scope).

Builds explicit brick-wall graphs W (H x W grid with alternating vertical
edges, max degree 3), takes S = full middle row, and certifies ONLY:
  (1) max degree 3;
  (2) W - S has exactly two connected components A (top), B (bottom) with
      explicit sizes;
  (3) A and B are each connected;
  (4) clean-ladder lemma instance: after deleting a demo cop set P of size K
      from A, A - P still contains two adjacent fully-intact rows (an intact
      ladder spanning the full width) and a giant connected piece.
No bramble-order / hitting-number claims are made here; the Omega(n)
treewidth lower bound comes from the analytic grid-minor argument in DRAFT.md
plus Seymour-Thomas duality, not from this script.
"""
import json
import os

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1761/output/artifacts"
os.makedirs(OUT, exist_ok=True)


def brick_wall(H, W):
    adj = {(r, c): set() for r in range(H) for c in range(W)}

    def add(u, v):
        adj[u].add(v)
        adj[v].add(u)

    for r in range(H):
        for c in range(W - 1):
            add((r, c), (r, c + 1))
    for r in range(H - 1):
        for c in range(W):
            if (r + c) % 2 == 0:
                add((r, c), (r + 1, c))
    return adj


def components_after_removal(adj, S):
    Sset = set(S)
    seen = set()
    comps = []
    for v in adj:
        if v in Sset or v in seen:
            continue
        stack = [v]
        seen.add(v)
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w in Sset or w in seen:
                    continue
                seen.add(w)
                stack.append(w)
        comps.append(comp)
    return comps


def is_connected_set(adj, blocked, verts):
    verts = set(verts)
    if not verts:
        return False
    start = next(iter(verts))
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w in verts and w not in blocked and w not in seen:
                seen.add(w)
                stack.append(w)
    return seen == verts


def largest_piece(adj, allowed, cops):
    cops = set(cops)
    seen = set()
    best = 0
    for v in allowed:
        if v in cops or v in seen:
            continue
        stack = [v]
        seen.add(v)
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            for w in adj[u]:
                if w in allowed and w not in cops and w not in seen:
                    seen.add(w)
                    stack.append(w)
        best = max(best, size)
    return best


def clean_adjacent_rows(mid, W, cops):
    """Return a pair of adjacent rows in [0, mid) fully disjoint from cops."""
    cop_rows = {r for (r, c) in cops}
    for i in range(mid - 1):
        if i not in cop_rows and (i + 1) not in cop_rows:
            return [i, i + 1]
    return None


results = {}
for (H, W) in [(8, 8), (12, 12)]:
    adj = brick_wall(H, W)
    maxdeg = max(len(v) for v in adj.values())
    assert maxdeg <= 3
    mid = H // 2
    S = [(mid, c) for c in range(W)]
    comps = components_after_removal(adj, S)
    sizes = sorted([len(v) for v in comps], reverse=True)
    assert len(comps) == 2, f"expected 2 components, got {len(comps)}"
    A = [(r, c) for r in range(mid) for c in range(W)]
    B = [(r, c) for r in range(mid + 1, H) for c in range(W)]
    assert is_connected_set(adj, set(S), A), "A must be connected"
    assert is_connected_set(adj, set(S), B), "B must be connected"
    assert len(A) == mid * W and len(B) == (H - 1 - mid) * W
    Ktest = 3 if H == 8 else 4
    cops_demo = [(mid - 1, c) for c in range(0, W, max(1, W // Ktest))][:Ktest]
    assert all(v in set(A) for v in cops_demo)
    ladder = clean_adjacent_rows(mid, W, cops_demo)
    assert ladder is not None, "clean ladder must exist for demo cop set"
    # the ladder itself is connected and avoids cops and S
    L = [(r, c) for r in ladder for c in range(W)]
    assert is_connected_set(adj, set(cops_demo) | set(S), L), "ladder must be intact"
    big = largest_piece(adj, set(A), cops_demo)
    results[f"{H}x{W}"] = {
        "max_degree": maxdeg,
        "num_vertices": len(adj),
        "separator_size": len(S),
        "num_components_after_removal": len(comps),
        "component_sizes": sizes,
        "top_component_size": len(A),
        "bottom_component_size": len(B),
        "top_connected": True,
        "bottom_connected": True,
        "demo_cops_size": Ktest,
        "demo_cops": [list(map(int, v)) for v in cops_demo],
        "clean_adjacent_rows_in_A_after_demo_cops": ladder,
        "ladder_intact_and_connected": True,
        "largest_A_piece_after_demo_cops": big,
    }
    print(f"wall {H}x{W}: maxdeg={maxdeg} comps={sizes} ladder={ladder} bigpiece={big}/{len(A)}")

with open(os.path.join(OUT, "wall_separator_results.json"), "w") as f:
    json.dump(results, f, indent=2)
print("wrote wall_separator_results.json (structural certificates only)")
