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

For a centered \(m\)-dimensional body,
\[
L_K^{2m}
=
\frac{\det A(K)}{\operatorname{vol}(K)^2}.
\]
The proof uses the exact recursions
\[
S(P\times Q)=S(P)S(Q)
\]
and
\[
S(P\oplus_1Q)=C_{p,q}S(P)S(Q),
\]
where
\[
S(K)=L_K^{2\dim K}.
\]

The checker uses exact rational arithmetic for
\[
C_{p,q}
=
\binom{p+q}{p}^{2}
\left(\frac{(p+1)(p+2)}{(p+q+1)(p+q+2)}\right)^p
\left(\frac{(q+1)(q+2)}{(p+q+1)(p+q+2)}\right)^q.
\]
It verifies the strict-loss pattern through dimension \(40\), recursively enumerates all exact Hanner values through dimension \(9\), and checks the cube and cross-polytope endpoint formulas.

These finite checks do not prove the quantified theorem. The all-dimensional proof is the beta-integral covariance computation plus the analytic inequality \(C_{p,q}\le1\).
