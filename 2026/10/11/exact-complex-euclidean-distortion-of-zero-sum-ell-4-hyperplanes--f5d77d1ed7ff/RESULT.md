# Exact complex Euclidean distortion of zero-sum \(\ell_4\) hyperplanes

## Finding
For every integer \(n\ge2\), consider the complex hyperplane
\[
H_n=\left\{z=(z_1,\ldots,z_n)\in\mathbb C^n:\sum_{j=1}^n z_j=0\right\}
\]
with the norm \(\|z\|_4=(\sum_j|z_j|^4)^{1/4}\). Let \(d_{\mathrm{BM}}\) denote **multiplicative** Banach--Mazur distance, with infimum only over **complex-linear** isomorphisms. Then
\[
\boxed{d_{\mathrm{BM}}\bigl(H_n,\ell_2^{n-1}(\mathbb C)\bigr)^4=\frac{n^2-3n+3}{n-1}.}
\]
The identity is proved simultaneously with the sharp, all-complex-coefficient moment bounds
\[
\boxed{\frac1n\le\frac{\sum_{j=1}^n |z_j|^4}{\bigl(\sum_{j=1}^n|z_j|^2\bigr)^2}
\le\frac{n^2-3n+3}{n(n-1)}}\qquad(0\ne z\in H_n).
\]
A full set of unit-modulus \(n\)-th roots of unity attains the lower bound. The real vector \((n-1,-1,\ldots,-1)\) attains the upper bound. The ambient Euclidean quadratic form restricted to \(H_n\) is already optimal; no nonstandard complex ellipsoid can reduce the Banach--Mazur distance. In dimension \(n=3\) the distance has fourth power \(3/2\), unlike the real zero-sum plane, whose inherited fourth-power norm is Euclidean up to scale.

## Assumptions and scope
All dimensions are finite integers \(n\ge2\). Scalars, coordinates, linear maps, and inner products are complex, except in the intermediate real lemma. The fourth-power norm is a sum, not an average. Write \(B(z)=\sum_j|z_j|^2\) and \(Q(z)=\sum_j|z_j|^4\). Distances use the convention
\[
d_{\mathrm{BM}}(X,Y)=\inf_{T:X\to Y\ \mathrm{complex\ linear\ invertible}}\|T\|\,\|T^{-1}\|,
\]
not its logarithm. Neither a universal statement for other exponents nor a formula for arbitrary codimension-one subspaces is claimed.

## Proof
**1. The exact real zero-sum fourth-moment bound.** For every real \(x\ne0\) with \(\sum_j x_j=0\), we first show
\[
\sum_jx_j^4\le M_n\left(\sum_j x_j^2\right)^2,
\qquad M_n=\frac{n^2-3n+3}{n(n-1)}.\tag{1}
\]
The cases \(n=2\) and \(n=3\) follow from direct expansion: on the respective zero-sum subspaces, \(\sum_jx_j^4=\tfrac12(\sum_jx_j^2)^2\).

For \(n\ge4\), normalize \(\sum_jx_j^2=1\) and maximize \(\sum_jx_j^4\) on the compact intersection with \(\sum_jx_j=0\). The two constraint gradients are independent because no nonzero constant vector is zero-sum. The multiplier equations give a cubic \(4t^3-2\lambda t-\mu\) vanishing at every distinct coordinate value \(t\). Thus there are at most three distinct coordinate values.

Suppose there are three, denoted \(a<b<c\). Comparing coefficients with \(4(t-a)(t-b)(t-c)\) gives \(a+b+c=0\). The constrained Lagrangian has diagonal second derivative \(12t^2-2\lambda\), which is the derivative in \(t\) of \(4(t-a)(t-b)(t-c)\). At \(t=a\) it equals \(4(a-b)(a-c)\), and at \(t=c\) it equals \(4(c-a)(c-b)\); both are strictly positive. Were either extremal root repeated, a vector adding \(1\) and \(-1\) to two occurrences of that root would be tangent to both constraints and would have strictly positive Lagrangian second variation, contradicting maximality. Hence \(a\) and \(c\) each occur exactly once and \(b\) occurs \(n-2\) times. The zero-sum constraint together with \(a+b+c=0\) forces \((n-3)b=0\); therefore \(b=0\) and \(a=-c\), giving moment ratio \(1/2\). This is strictly below the two-level candidate \(M_n>1/2\) when \(n\ge4\). Consequently a maximizer must have exactly two distinct coordinate values.

If one level occurs \(k\) times and the other \(n-k\) times, the zero-sum relation gives, by direct substitution,
\[
\frac{\sum_jx_j^4}{(\sum_jx_j^2)^2}
=\frac{n}{k(n-k)}-\frac3n.\tag{2}
\]
For \(1\le k\le n-1\), this is largest exactly when \(k=1\) or \(k=n-1\). This yields \((1)\), with equality for \((n-1,-1,\ldots,-1)\).

**2. Phase averaging transfers the sharp real bound to all complex vectors.** Fix complex \(z\in H_n\). For \(0\le\theta<2\pi\), put \(x_j(\theta)=\operatorname{Re}(e^{i\theta}z_j)\). Then \(x(\theta)\) is real zero-sum, so \((1)\) holds for every angle. Define \(T(z)=\sum_jz_j^2\). Direct integration of trigonometric monomials gives
\[
\frac1{2\pi}\int_0^{2\pi}\sum_jx_j(\theta)^4\,d\theta=\frac38Q(z),
\]
\[
\frac1{2\pi}\int_0^{2\pi}\left(\sum_jx_j(\theta)^2\right)^2d\theta
=\frac14B(z)^2+\frac18|T(z)|^2.
\]
Integrating \((1)\) and multiplying by \(8/3\),
\[
Q(z)\le M_n\left(\frac23B(z)^2+\frac13|T(z)|^2\right)
\le M_n B(z)^2,
\]
where the last inequality is \(|\sum_jz_j^2|\le\sum_j|z_j|^2\). The real outlier attains equality. Thus the complex upper constant equals the exact real upper constant.

**3. The complex lower constant.** Cauchy--Schwarz yields \(B(z)^2\le nQ(z)\). Equality requires all moduli to agree. Such an equal-modulus zero-sum vector exists for every \(n\ge2\): take \(z_j=e^{2\pi i(j-1)/n}\). Therefore \(\min_{z\ne0}Q(z)/B(z)^2=1/n\), with no parity restriction.

**4. Optimality among all complex Euclidean positions.** Let \(q\) be any positive-definite Hermitian quadratic form on \(H_n\). Write the best pointwise constants as \(\alpha\|z\|_4^2\le q(z)\le\beta\|z\|_4^2\). Average \(q\) over the coordinate permutation group. The same inequalities survive averaging, so the distortion factor \(\sqrt{\beta/\alpha}\) cannot increase. Any permutation-invariant Hermitian form on the standard zero-sum representation is a positive scalar multiple of \(B\): extend its matrix by zero on the constant line, where permutation invariance forces the ambient matrix to have one common diagonal entry and one common off-diagonal entry. Hence \(q\) can be taken as \(cB\). For this choice the fourth power of the ratio of maximal to minimal radial norms is
\[
\frac{\max_{0\ne z\in H_n}Q(z)/B(z)^2}{\min_{0\ne z\in H_n}Q(z)/B(z)^2}
=\frac{M_n}{1/n}=\frac{n^2-3n+3}{n-1}.
\]
The lower inequality for arbitrary Hermitian forms and attainment for \(B\) prove the stated complex Banach--Mazur distance.

## Verification
The self-contained mathematical proof above applies to every integer dimension. A separate exact-arithmetic diagnostic program `verify.py` checks the two-level equality in dimensions \(2\) through \(20\), symbolically verifies phase-average coefficient identities, and tests all nonzero complex vectors on a small integral lattice in dimensions \(2\) through \(5\). Its finite grid is a diagnostic, **not** the proof of the universal inequality. The global argument rests on the constrained stationary-point classification, exact angular integration, and averaging of Hermitian quadratic forms.

## Relationship to prior work
Classical bounds for standardized finite-sample moments are related to step 1, which is not asserted to be a newly discovered real inequality. Dalén's paper explicitly advertises best possible finite-sample moment bounds, but the available abstract does not resolve whether its full text includes this particular normalization. Riener's symmetric-polynomial half-degree principle concerns real symmetric polynomial inequalities and helps contextualize the two-level real extremization; this proof does not require that principle. Kobos and Varivoda address complex Banach--Mazur distances between **full** complex sequence spaces and complex discrepancy, not the zero-sum subspaces examined here. The new assertion is the exact **complex hyperplane** Euclidean distance across every dimension, including its phase-sensitive lower radial bound and optimality among all complex Hermitian positions.

## Limitations
The result is restricted to complex scalars, the coordinate-sum-zero hyperplane, exponent four, and complex-linear Banach--Mazur distance. No classification of every complex extremizer is claimed; explicit attaining families suffice. The real first ingredient may already be known through sample-moment theory. An obscure equivalent formula for the complex hyperplane may remain in older unindexed work. Independent external mathematical validation has not been performed.

## References
1. C. Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464v1 (first publicly submitted 2010-01-25), https://arxiv.org/abs/1001.4464. Full open text inspected, including the main principles and proofs.
2. T. Kobos and M. Varivoda, *A Complex Analogue of Spencer's Six Standard Deviations Theorem and the Complex Banach--Mazur Distance*, arXiv:2602.12868v1 (2026-02-13), https://arxiv.org/abs/2602.12868. Full open text inspected, including Theorem 1.5 and Sections 2--4.
3. J. Dalén, *Algebraic bounds on standardized sample moments*, Statistics & Probability Letters 5 (1987), 329--331, RePEc:eee:stapro:v:5:y:1987:i:5:p:329-331, https://ideas.repec.org/a/eee/stapro/v5y1987i5p329-331.html. Abstract and bibliographic record consulted; full text not available in this review.
