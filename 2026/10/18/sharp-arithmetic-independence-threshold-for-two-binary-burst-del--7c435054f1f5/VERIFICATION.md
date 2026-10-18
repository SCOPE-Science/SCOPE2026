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

# Reproduction

Execute `python3 verify.py` with Python 3. The program constructs all contiguous-burst outputs as distinct strings, compares their cardinalities with the shifted-mismatch count, independently reconstructs the exact joint tables of the two burst widths, checks binomial marginals and every joint independence decision, and checks the explicit critical-length polynomial coefficient by coefficient. It checks every \(1\le b<c<n\) for \(3\le n\le11\), totaling \(165\) triples. The expected terminal message begins `VERIFIED 165`.

This is exhaustive **only for the stated finite range**. For arbitrary \(n\), the mathematical proof uses the exact graph-spin generating function, a finite group permutation decomposition into \(\gcd(b,c)\) cycles, and strict positivity of the cycle correction. The experiment is not an independent infinite proof.

The marginal identity is known in earlier literature; novelty is claimed only for the two-width threshold and the explicit first-dependence joint law. Independent external verification has not been performed.
