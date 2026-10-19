# Collapse of exterior norm domination for Hilbert-valued Fock functions

## Finding
Let \(H\) be a complex Hilbert space. In its Gaussian Fock space of entire \(H\)-valued functions with norm
\[
\|h\|_{\mathcal F^2(H)}^2=\frac1\pi\int_{\mathbb C}\|h(z)\|_H^2e^{-|z|^2}\,dA(z),
\]
consider the exterior domination implication
\[
\|f(z)\|_H\le\|g(z)\|_H\quad(|z|\ge R)
\qquad\Longrightarrow\qquad
\|f\|_{\mathcal F^2(H)}\le\|g\|_{\mathcal F^2(H)}.
\]
There are two sharp failures of scalar extrapolation:

**Finite-dimensional boundary.** For every real \(R\ge1\), this implication fails already for \(H=\mathbb C^2\), even for pairs of vector polynomials of degree at most three. At the scalar-sharp radius \(R=1\), a fully explicit witness is
\[
f(z)=(\sqrt7z^2,3),\qquad g(z)=(z^3,\sqrt{15}z).
\]
For this witness exterior pointwise domination holds, yet \(\|f\|_{\mathcal F^2(\mathbb C^2)}^2-\|g\|_{\mathcal F^2(\mathbb C^2)}^2=2\).

**Infinite-dimensional collapse.** For \(H=\ell^2(\mathbb N_0)\), the implication fails for *every* real \(R>0\). Indeed for each such \(R\), a pair of vector polynomials with values in some finite-dimensional coordinate subspace of \(H\) witnesses failure. Thus no positive exterior radius can deliver the Hilbert-valued Fock norm-domination principle in infinite Hilbert dimension.

## Assumptions and scope
All vector norms are Hilbert norms, all functions are entire and have finite Gaussian Fock norm, and the pointwise assumption is required on the whole closed exterior \(|z|\ge R\); all constructed witnesses also work for the corresponding open exterior. The same construction works in any Hilbert space containing the stated coordinate subspace. The dimension needed when \(R<1\) may depend on \(R\). The result does not determine a sharp radius for fixed finite dimension \(d\ge2\) below one and does not make claims about Banach-valued or general weighted Fock spaces.

## Proof
**Gaussian moments.** By angular orthogonality and polar integration,
\[
\frac1\pi\int_{\mathbb C}|z|^{2k}e^{-|z|^2}\,dA(z)=k!
\]
for every integer \(k\ge0\). Therefore a polynomial \(q(t)=\sum_{k=0}^{K}c_kt^k\) satisfies \(\int_0^\infty q(t)e^{-t}\,dt=\sum_{k=0}^{K}c_kk!\).

**The two-coordinate construction.** Put \(s=R^2\ge1\) and choose \(A>0\). Define
\[
f(z)=(\sqrt{2A+s}\,z^2,A\sqrt{s}),\qquad
  g(z)=(z^3,\sqrt{A^2+2As}\,z).
\]
Writing \(t=|z|^2\), direct expansion gives
\[
\|g(z)\|^2-\|f(z)\|^2
=(t-s)(t-A)^2\ge0\quad(t\ge s).
\]
The difference of the *squared Fock norms* is
\[
\|g\|^2-\|f\|^2
=(1-s)A^2+(2s-4)A+6-2s.
\]
For \(s=1\), this equals \(4-2A<0\) whenever \(A>2\). For \(s>1\), its leading quadratic coefficient is negative, so it is negative for every sufficiently large \(A\). Taking \(s=1,A=3\) yields the explicit witness in the finding, with pointwise squared difference \((t-1)(t-3)^2\) and squared Fock-norm difference \(-2\).

**Weighted polynomial-density lemma.** For every \(s>0\), there is a real polynomial \(p\) with
\[
\int_0^\infty(t-s)p(t)^2e^{-t}\,dt<0.
\]
To prove this, consider \(L^2((0,\infty),(1+t)e^{-t}dt)\). Polynomials are dense here. Indeed, if \(u\) is orthogonal to every polynomial, then
\[
F(w)=\int_0^\infty u(t)(1+t)e^{-t}e^{wt}\,dt
\]
is analytic on \(\operatorname{Re}w<1/2\) by Cauchy--Schwarz, and all derivatives at \(w=0\) vanish. The identity theorem forces \(F\equiv0\) there; uniqueness of the Fourier transform of the integrable function \(u(t)(1+t)e^{-t}\) then gives \(u=0\) almost everywhere. Take a nonzero, real, continuous function \(h\) supported in \((0,s)\), for which the displayed signed integral is negative. Real polynomials \(p_n\) can approximate \(h\) in that weighted \(L^2\) space. Since \(|t-s|\le\max\{1,s\}(1+t)\), Cauchy--Schwarz gives convergence of the signed quadratic integrals, so some \(p_n\) has the required strict negativity.

**Coefficient-sign realization.** Fix such a \(p\), write
\[
q(t)=(t-s)p(t)^2=\sum_{k=0}^{K}c_kt^k,
\qquad c_k^+=\max\{c_k,0\},\quad c_k^-=\max\{-c_k,0\}.
\]
With an orthonormal set \(e_0,\ldots,e_K\) in \(\ell^2\), put
\[
f(z)=\sum_{k=0}^{K}\sqrt{c_k^-}\,z^ke_k,
\qquad g(z)=\sum_{k=0}^{K}\sqrt{c_k^+}\,z^ke_k.
\]
Orthogonality in the target yields exactly
\[
\|g(z)\|^2-\|f(z)\|^2=q(|z|^2)\ge0\quad(|z|\ge R),
\]
while the Gaussian-moment identity gives
\[
\|g\|_{\mathcal F^2}^2-\|f\|_{\mathcal F^2}^2
=\int_0^\infty(t-s)p(t)^2e^{-t}\,dt<0.
\]
The construction is a finite vector polynomial for each \(R>0\). This proves the infinite-dimensional claim.

## Verification
The standalone `verify.py` uses exact rational coefficients and factorial moments to check the boundary witness and several larger radii, and verifies all polynomial coefficient splits in those cases. The universal conclusion does not follow from finite tests: it follows from the density lemma and coefficient-sign realization. The verifier does not certify polynomial density or historical novelty.

## Relationship to prior work
Wikström (2026) proved the sharp *scalar-valued* Gaussian Fock Korenblum radius \(1\), including equality classification; that theorem remains intact. The present question changes the hypothesis from comparison of absolute values of two scalar holomorphic functions to comparison of pointwise Hilbert norms of two holomorphic vector functions. A scalar holomorphic quotient cannot in general encode this vector-norm inequality. The explicit two-coordinate example excludes deduction from the scalar theorem, and the density construction demonstrates loss of *every* exterior radius for an infinite-dimensional target. Earlier work on scalar weighted Bergman and Fock radii also does not imply vector-valued comparison.

## Limitations
No fixed finite-dimensional sharp threshold below \(1\) is asserted. The arbitrary-radius witness may require growing target dimension, and is provided by a polynomial-existence proof rather than by one uniform explicit coefficient formula. A mathematical-priority search is not proof that all older literature has been exhausted. Verification is same-model only; no independent audit was performed.

## References
- F. Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622v1 (first made public 2026-09-30), https://arxiv.org/abs/2609.39622.
- I. Efraimidis, A. Llinares, and D. Vukotić, *Korenblum's Principle for Bergman Spaces with Radial Weights*, Computational Methods and Function Theory 25 (2025), 239--250; online 2024-05-18, https://doi.org/10.1007/s40315-024-00543-6. This treats scalar analytic functions on the disk, a different target and domain.
