---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At n>=6 the first and last three bits are disjoint positions. If P and S are the prefix and suffix projections of a code, P and S are disjoint and the initial pairs of P avoid the terminal pairs of S, including for self-overlap. Conversely all compatible boundaries in P×S can be filled independently in the middle. For b distinct initial binary pairs in P, a=|P|<=2b and |S|<=2(4-b)-t, where t counts P-arcs exiting those b pair states. Singletons and two-state subsets of the displayed de Bruijn graph contain at most one and two arcs, respectively, bounding the products by 10 and 9. For b=3 there are at most two suffixes, so a<=5 suffices; at a=6 every outgoing arc is used, including one entering the missing state from another state, so at most one suffix survives. Empty P or b=4 gives zero. The displayed prefix and suffix sets give 2×5=10, including at n=6 with empty middle. Independent enumeration of all 256 prefix sets gives the same maximum and direct ordered-pair construction checks passed at n=6,7,8. Replay by running python3 /workspace/branches/34e9da9b-0bba-4797-8e9f-ce7d1f7568bc/boundary_exhaust.py. Enumeration covers the whole boundary kernel, not all lengths directly; the projection and lifting arguments cover those.

## originality

PASS

The supported distinct contribution is the exact unrestricted six-bit maximum 10 under only lengths 2 and 3, with a matching symbolic upper bound. The all-length multiplier after that base case is known and is not credited as a novel lifting theorem. No inspected prior statement or straightforward implication establishes the sharp base case.

## value

PASS

Lengths two and three form the shortest nontrivial consecutive interval starting at two. Length six is forced by the nonintersecting boundary reduction, not an arbitrary finite slice. The exact base value determines the optimal rate coefficient for every longer binary code with that restricted-overlap interval; the sharp bound answers an extremal question that neither lifting nor a construction size alone resolves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
