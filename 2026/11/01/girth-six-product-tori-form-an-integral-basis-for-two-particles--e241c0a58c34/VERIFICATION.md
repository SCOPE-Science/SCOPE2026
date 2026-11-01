---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification details

The scripts `verify.py` and `symmetry.py` reconstruct the graph and check this specific finite theorem from first principles. `verify.py` computes cubical boundary matrices over the integers; its Smith form is derived with exact integer arithmetic, while its rank bound is certified independently by elimination in the field with three elements and by a displayed integral unimodular minor. The program checks all sixty torus chains are actual two-cycles and exhaustively enumerates simple graph cycles shorter than seven edges. `symmetry.py` enumerates all graph isomorphisms to itself and checks the two orbits, rather than assuming an incomplete generating subgroup. The recorded outputs are `verify.out` and `symmetry.out`.

**Key facts verified:** cell counts \((120,336,228)\), boundary ranks \((119,208)\) over characteristic zero, mod-two degree-two rank \(207\), Smith diagonal \((1^{\times207},2)\), exactly \(24\) shortest hexagons and \(60\) disjoint pairs, signed minor \(-1\), automorphism count \(96\) and pair-orbit sizes \((12,48)\). Standard homological algebra and the known graph-configuration deformation retraction identify the calculated cubical homology with the continuous configuration-space homology. These are exact finite verifications, not claims of independent external certification.

**Limits:** `sympy` and `networkx` are external computational dependencies. The verification establishes only the stated graph, particle count, and actions; it does not establish novelty in every inaccessible publication.
