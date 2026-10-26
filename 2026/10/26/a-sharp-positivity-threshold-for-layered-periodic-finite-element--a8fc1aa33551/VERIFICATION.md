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

# Verification of the finite-element threshold
The analytic proof uses an explicitly scaled consistent mass matrix and a two-periodic block factorization. Its critical checks are: the Schur resolvent identity, the strict inequalities for the low-step regime, the signed cyclic Green kernel bound in the mixed-sign regime, and the Stieltjes inverse for steps beyond the cutoff.

Running `python verify.py` with Python 3 standard library produces `VERIFY_OK 116 six-or-more-node exact rational cases; four-node boundary witness`. The script tests exact rational entries of \((M+\tau K)^{-1}M\), exact stochastic row sums, negativity witnesses on both subcritical branches, and the four-node positive exception. It is not an exhaustive or infinite computational certification. The text proof, not the finite tests, establishes all sizes and real positive coefficients.

The theorem does not assert positivity for nonuniform meshes, arbitrary nonalternating diffusion patterns or values not in its hypotheses. No independent audit or independent validation has been performed.
