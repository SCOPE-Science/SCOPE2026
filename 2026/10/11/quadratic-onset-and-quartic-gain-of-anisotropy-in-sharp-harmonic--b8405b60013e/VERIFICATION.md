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

Let
\[
\Psi_n(s,r)
=
n\log L_{n,r}(e^s)-s.
\]
The source proves that this is strictly convex in
\[
s
\]
and has a unique minimizer
\[
s_n(r)=\log q_n(r).
\]

At
\[
r=0,
\]
\[
L_{n,0}(e^s)
=
n\,\mathbb E
\sqrt{1+(e^{2s}-1)t^2},
\]
where
\[
t
\]
is one coordinate of a uniform point on
\[
S^{n-1}.
\]
Using
\[
\mathbb E(t^2)=1/n
\]
and
\[
\mathbb E(t^4)=3/[n(n+2)]
\]
gives
\[
H_n
=
\partial_s^2\Psi_n(0,0)
=
\frac{2(n-1)(n+1)}{n(n+2)}.
\]

The exact source formulas for the radial and tangential Poisson-gradient components give, after a second-order Taylor expansion,
\[
nL_{n,r}'(1)-L_{n,r}(1)
=
\frac{(n-2)(n-1)(3n+2)}
{n^2(n+2)}
r^2
+
O(r^4).
\]
Since
\[
L_{n,0}(1)=n,
\]
\[
\partial_s\Psi_n(0,r)
=
A_n r^2+O(r^4),
\qquad
A_n
=
\frac{(n-2)(n-1)(3n+2)}
{n^3(n+2)}.
\]

The implicit-function theorem yields
\[
\log q_n(r)
=
-\frac{A_n}{H_n}r^2+O(r^4),
\]
hence
\[
q_n(r)
=
1-
\frac{(n-2)(3n+2)}
{2n^2(n+1)}
r^2
+
O(r^4).
\]

Strict convexity and Taylor expansion around
\[
s=0
\]
then give
\[
\Psi_n(0,r)-\Psi_n(s_n(r),r)
=
\frac{A_n^2}{2H_n}r^4+O(r^6).
\]
This is exactly
\[
\log
\frac{\mathcal J_n^{\mathrm{iso}}(r)}
{\mathcal J_n(r)}.
\]
The coefficient simplifies to
\[
\delta_n
=
\frac{(n-2)^2(n-1)(3n+2)^2}
{4n^5(n+1)(n+2)}.
\]

The symmetry
\[
L_{n,-r}(q)=L_{n,r}(q)
\]
justifies the even remainders. The proof is analytic; numerical minimization was used only as a secondary sanity check.
