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

The standalone `verify.py` requires only Python 3 standard-library modules. Execute `python verify.py` in the directory containing that script, and compare its output byte for byte with `verification_output.txt`.

The verifier reconstructs the simplicial face collection by forbidding induced disjointness-graph triples with a vertex of degree two, rather than assuming the claimed cover decomposition. It checks this independent enumeration against the star/four-subset cover, computes reduced mod-two Betti ranks for the finite values \(n=5,6,7,8\), and computes signed Lefschetz traces for four permutation samples in each case. Those traces match the fourth exterior power of the standard permutation-augmentation representation.

An integral boundary check enumerates the eight facets of the octahedral intersection for each four-subset and verifies that its stated signed two-chain is a cycle whose triangle-facet projection is the tetrahedron boundary up to sign. This is the critical local signed-attaching calculation. The infinite family is proved in `RESULT.md`; no finite computation is presented as proof for all \(n\).

These checks do not constitute independent scientific audit, formal proof certification, or a complete bibliographic search.
