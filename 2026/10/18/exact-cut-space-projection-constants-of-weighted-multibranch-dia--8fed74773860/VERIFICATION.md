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

# Verification and reproducibility

The result has an analytic proof by norm-preserving finite-group averaging, exact weighted-column computation, and a scalar reciprocal-sum minimax inequality. Its generality is \(m\ge3\), every positive real branch length, and all real linear projections onto the cut space. The proof is self-contained and does not use experiment-based extrapolation.

Run `python3 verify_exact.py`. This standalone standard-library checker builds the exact rational matrix of the claimed projection from 120 cases, verifies \(P^2=P\), verifies the cut-space range and fixes a full basis, and calculates the full weighted \(\ell_1\) matrix operator norm by all columns. It also verifies the equality conditions for the norm lower bound. The observed output is `PASS: 120 exact cases, idempotence, full weighted column norms, range/fixing, sharp lower bounds`.

Run `python3 verify_lp.py` with SciPy and NumPy. This independently minimizes the norm of an **unrestricted** projection matrix, by linear constraints on its kernel and its action on the quotient. Its fixed-seed 50 cases for \(2\le m\le6\) (40 with \(m\ge3\)) matched the formula within \(10^{-8}\); observed final line is `PASS`.

Limits: the exact checker validates each listed finite instance, not the theorem's infinite quantifier. The floating-point LP cross-check cannot establish exact minimality or exclude near-degenerate pathology; this is established by the analytic lower bound. The scripts depend only on the accompanying files and, for the optional LP experiment, the documented packages. No independent scientific audit has been performed.
