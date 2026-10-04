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

Define \(q=\mu^*-\mu\), \(K=b/\delta\), total population \(T\), and total noncompliant population \(X\). Direct summation of the six source equations gives
\[
T'=b-\delta T,
\qquad
X'=\bigl(q(T-X)-(\nu+\delta)\bigr)X.
\]
On \(qK=\nu+\delta\), the substitution \(Y=T-K\) gives \(Y'=-\delta Y\) and \(X'=q(Y-X)X\). The reciprocal \(U=1/X\) then obeys the linear equation used in `RESULT.md`, from which \(tX(t)\to1/q\) follows exactly.

For the exact rational check in `verifier.py`, take \(b=\delta=\beta=\gamma=\nu=1\), \(q=2\), \(\alpha=1/2\), \(\eta=0\), \(T(0)=K=1\), and \(X(0)=1/4\). Then the behavioral ratio is exactly one, the disease ratio is \(1/8\), and
\[
X(t)=\frac1{4+2t}
\]
solves \(X'=-2X^2\) exactly. The script checks the derivative identity at rational test times only as a replay of this closed-form identity; the general theorem is established by the analytic derivation, not by finite sampling.

The infection comparison matrix tends to an upper-triangular Hurwitz matrix when \(\mathcal R_D<1\), while the recovered comparison matrix tends to another Hurwitz matrix. The proof in `RESULT.md` records the explicit dominating matrices and the resulting exponential decay limits.
