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

For vertices indexed by \(\mathbb Z/n\mathbb Z\), let
\[
\rho(i,j)=\min\{|i-j|,n-|i-j|\}
\]
and
\[
d_q=2R\sin\!\left(\frac{\pi q}{n}\right)
\]
for
\[
0\le q\le\left\lfloor\frac n2\right\rfloor.
\]

For a pair at cyclic separation \(k\), any vertex center \(j\) satisfies
\[
k\le \rho(0,j)+\rho(j,k)\le2\max\{\rho(0,j),\rho(j,k)\},
\]
so the smallest possible maximum index distance is at least \(\lceil k/2\rceil\). A midpoint-nearest vertex on the shorter arc attains this bound. Therefore
\[
\operatorname{hd}(0,k)=2d_{\lceil k/2\rceil}
\]
and
\[
g_k=2d_{\lceil k/2\rceil}-d_k.
\]

For every even \(2m\),
\[
g_{2m-1}-g_{2m}
=
2R\bigl(\sin(2mt)-\sin((2m-1)t)\bigr)>0.
\]
For odd terms, writing \(u=(m+1)t\),
\[
g_{2m+1}=4R\sin u-2R\sin(2u-t),
\]
and
\[
\frac{d}{du}g
=
4R(\cos u-\cos(2u-t))\ge0
\]
because
\[
t\le u\le2u-t\le\pi/2.
\]
Hence the global maximum is the largest admissible odd separation.

The embedded `verify.py` was replayed from its actual package path before packaging. For each \(3\le n\le80\), it independently enumerates every unordered vertex pair and every possible vertex center in Cartesian coordinates, computes hyperdistance directly from the definition, and compares the result to both the compact and residue-class formulas. It also checks the leading asymptotic errors.

The replay output was:

`VERIFY_OK regular-polygon convexity gap n=3..80`

Finite enumeration is not used as an infinite proof. The all-\(n\) theorem follows from the exact center minimization and monotonicity argument above.
