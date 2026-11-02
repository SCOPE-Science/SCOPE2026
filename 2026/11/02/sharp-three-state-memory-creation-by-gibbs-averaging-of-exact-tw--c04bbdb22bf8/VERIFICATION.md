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

# Reproducibility and limits

The supplied `verify.py` is standalone Python 3 code using SymPy; run it with `python verify.py` in an environment where SymPy is available. The exact recorded standard output is in `VERIFIER_OUTPUT.txt`.

Successful checks include the full symbolic stochastic parameterization, determinant polynomial identity, exact Gibbs compression, endpoint formulae, rank-one projection identities and norms, the parameterized family satisfying the two-step-mixing equation, eight endpoint/interior algebraic witnesses, exact compressed powers for six time steps, 48 strictly positive rational exact mixers, and two-state rigidity. The recorded run passed 3,714 assertions. Mathematical claims valid for all dimensions of the parameter interval are established by the proof's analytic inequalities and Cayley--Hamilton argument; finitely many evaluated examples are not a proof of an inequality on a continuum.

Verification is self-review and computational. No independent review, publication priority assessment, or external certification has been performed. Scientific scope and historical-priority risks are stated in the main result and review.
