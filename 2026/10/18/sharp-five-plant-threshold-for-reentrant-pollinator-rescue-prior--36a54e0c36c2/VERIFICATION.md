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

# Reproducibility and verification

`verify.py` is a self-contained Python 3 program with no external modules, data downloads or random seeds. Run `python3 verify.py`. The program defines precisely the five plant neighborhoods in the theorem, constructs the normalized gain polynomials by counting adjacent plants of each degree, and independently enumerates all joint pollinator-survival states to compute expected persistent plant richness, with and without a selected guaranteed pollinator.

For each of the seven targets and for failure probabilities \(q=1/4\), \(q=3/4\), and \(q=9/10\), the exact state enumeration agrees with \(G_j(q)=qH_j(q)\). The checks also reproduce \(H_A(q)=1+2q^5\), \(H_B(q)=2q\), the five auxiliary score forms, and \(H_A(3/4)-H_B(3/4)=-13/512\). Rational arithmetic is used throughout; no Monte Carlo approximations or numerical comparisons are needed for these checks.

The general no-reentry theorem for networks with at most four plant species depends on the signed-monomial classification and Descartes' rule detailed in `RESULT.md`. Finite enumeration of one example is not an exhaustive proof of that universal statement. Likewise, numerical approximations of the two switching probabilities are not certificates of the exact root count; strict monotonicity of \(f'\) together with exact signs proves the count.

The scientific result has undergone an internal self-review only. No external independent validation or audit has been undertaken. Model limitations and literature-access risks are documented separately.
