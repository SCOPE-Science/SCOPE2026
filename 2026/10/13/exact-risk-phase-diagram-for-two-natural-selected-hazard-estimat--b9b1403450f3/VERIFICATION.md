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

For \(n\ge2\) and \(r>0\), the proved reciprocal expectation is
\[
E\!\left[(\sigma_JY_J)^{-1}\right]
=
\frac1{n-1}
-
\frac{\left(r/(1+r)^2\right)^{n-1}}
{(n-1)^2B(n,n-1)}.
\]
The MLE-minus-BSEE-analogue risk difference is this expression minus
\[
\log\!\frac n{n-1}.
\]

The threshold calculation sets this difference to zero and solves the resulting quadratic relation between
\[
q_n
\quad\text{and}\quad
\rho_n/(1+\rho_n)^2.
\]

The standalone `verify.py` performs four independent checks:

1. numerical beta integration agrees with the closed reciprocal-expectation formula on deterministic \((n,r)\) cases;
2. the risk difference is negative at equal hazards and positive for sufficiently extreme hazard ratios through a broad finite range of \(n\);
3. the displayed \(\rho_n\) zeros the risk difference numerically;
4. the threshold values printed for \(n=2,5,8\) match direct bisection of the risk difference.

Expected final line:
`VERIFY_OK rho2=4.284376516357 rho5=2.679141980534 rho8=2.287831457726`.

These finite computations are reproducibility checks only; uniqueness for every \(n\ge2\) is proved analytically.
