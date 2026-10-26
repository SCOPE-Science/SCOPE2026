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

# Verification notes

The all-size result follows from the five analytic proof steps in `RESULT.md`, not from finite enumeration. The algebraic derivative identity \(q\mu_n'(q)=\operatorname{Cov}_q(C,I)\) comes from differentiation of a strictly positive finite partition function. The uniform-point calculation uses completion of two forced directed arcs to a uniform permutation of residual paths. The two endpoint coefficients are obtained by classifying the unique extremal permutation and all its nearest inversion neighbors.

The standalone `verify.py` uses standard-library exact integer and rational arithmetic. Running `python verify.py` produced `checker_output.txt` and verified the endpoint coefficient identities and \(q=1\) covariance for all \(2\le n\le8\), plus the exact derivative polynomial for \(n=3\). The \(n=3\) root uniqueness uses Descartes' rule in addition to these coefficients. No computation is presented as proof for unbounded \(n\).

Not checked: uniqueness of covariance sign crossing for arbitrary \(n\), joint parameter–size limits, or independent assessment of originality. Full historical priority beyond the inspected scientific sources remains uncertain.
