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

# Verification

Run `python verify.py` using Python 3.9 or later; it uses only the standard library.

The verifier builds the matrix-unit multiplication table and its induced bitset set-products from the definitions, enumerates all 31 and 1023 nonempty subsets for \(n=2\) and \(n=3\), respectively, and checks central idempotents, zero-adjoining products, and membership sandwiches. It exhaustively checks product preservation for both index permutations on \(n=2\), with reproducibly sampled checks for all six on \(n=3\).

It separately evaluates the Burnside orbit formula for \(2\le n\le6\), and directly enumerates permutation orbits of all nonempty subsets for \(n=2,3\), obtaining \(19\) and \(207\) respectively. Expected marker lines are `VERIFY_OK` and `ORBIT_OK`. Neither the finite tables nor sample tests can prove an all-parameter theorem; the proof of the latter is self-contained in `RESULT.md`.

The origin of the full binary-relation automorphism lemma is Kenneth D. Magill Jr. (1966); the current proof reconstructs it. The historical-coverage comparison against Tamura (1986) is bibliographic rather than full text, a limitation for originality and priority.
