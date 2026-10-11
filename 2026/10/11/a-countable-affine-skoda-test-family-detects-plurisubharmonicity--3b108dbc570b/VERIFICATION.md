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
K=\mathbb Q(i).
\]
Assume the Skoda estimate only for
\[
g_{q,A,M}(z)
=
\bigl(A(z-q),M\bigr),
\]
where
\[
q\in D\cap K^n,
\qquad
A\in\operatorname{GL}(n,K),
\qquad
M,\ell\in\mathbb N,
\]
and the Skoda exponent is
\[
\varepsilon=\ell.
\]

If the Levi matrix is not positive semidefinite, choose a positive definite Hermitian
\[
P
\]
with
\[
\operatorname{tr}(H_\varphi P)<0.
\]
The source affine calculation represents
\[
P
=
\overline{A^{-1}}
(A^{-1})^{\mathsf T}.
\]
Strict negativity is open, so density of Gaussian-rational points and matrices allows the center and matrix to be chosen from the displayed countable sets. The center can simultaneously be chosen with
\[
f(q)\ne0
\]
because a nonzero holomorphic function has zero set with empty interior.

Under
\[
w=A(z-q),
\]
the assumed tuple becomes
\[
(w_1,\ldots,w_n,M).
\]
The affine Jacobian multiplies both sides of the Skoda estimate by the same positive constant.

For fixed
\[
M,
\]
the inspected proof of Proposition 3.8 uses the special tuple above and takes
\[
\varepsilon\to\infty.
\]
Its ordinary limits remain valid along
\[
\varepsilon=1,2,3,\ldots.
\]
Therefore, for every positive integer
\[
M,
\]
the same proof gives
\[
\operatorname{tr}
i\partial\bar\partial\widetilde\varphi(0)
\ge
-\frac{n^2}{M^2}.
\]
Letting positive integer
\[
M
\]
tend to infinity forces a nonnegative transformed trace, contradicting the selected strict negative test.

On a pseudoconvex domain, classical Skoda division gives the estimate for all zero-free holomorphic tuples and all positive real exponents, and therefore for this countable subfamily.

No finite computation is used as a substitute for the limiting or density arguments.
