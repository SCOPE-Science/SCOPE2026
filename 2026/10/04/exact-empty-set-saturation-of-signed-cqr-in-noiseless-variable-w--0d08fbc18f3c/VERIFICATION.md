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

The checker `verify.py` reconstructs the claimed finite-sample identity without importing any research package. For several \((m,\alpha)\) pairs, it enumerates each possible rank of one test width among \(m+1\) distinct widths. For each rank it removes the test point, forms the calibration scores \(-W_i\), selects the empirical order statistic prescribed by the CQR finite-sample quantile, constructs the two output endpoints, and verifies both of the following equivalences:
\[
C(X)=\varnothing\quad\Longleftrightarrow\quad \operatorname{rank}(W)\le \lfloor\alpha(m+1)\rfloor,
\]
\[
Y\in C(X)\quad\Longleftrightarrow\quad \operatorname{rank}(W)>\lfloor\alpha(m+1)\rfloor.
\]
It also checks that the empirical rank frequencies equal the closed forms, verifies the \(m=99\), \(\alpha=0.1\) value exactly, and evaluates the three reported conditional binomial-tail probabilities.

The proof covers all finite \(m\) and \(\alpha\in[1/(m+1),1)\) under the stated continuity and noiseless symmetric-band assumptions. The asymptotic conditional statement is limited to fixed \(u\ne\alpha\). Tied widths, the boundary \(u=\alpha\), and non-additive or localized conformal variants are not certified by this checker or claimed by the theorem.
