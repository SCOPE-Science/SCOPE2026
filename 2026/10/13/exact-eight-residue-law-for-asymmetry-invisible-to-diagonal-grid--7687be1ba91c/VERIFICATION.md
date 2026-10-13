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

The exact-integer script `verify.py` checks row/column normalization, all diagonal-grid prefixes, and attained asymmetry of explicit feasible arrays at \(n=3\) and \(n=8\), as well as a brute-force grid-pair calculation of the closed eight-residue formula for every \(2\le n\le95\). Further distinct large dimensions verify the centered-spacing optimization. Its finite range is not an exhaustive test of all \(n\). The infinite mathematical proof uses the published sharp upper-envelope and diagonal-splice theorems, plus an algebraic reduction to the two adjacent candidate grid spacings. No independent audit has been performed.
