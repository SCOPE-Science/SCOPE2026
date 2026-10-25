# A universal parity-sensitive spherical width gap between type-B and type-D signed orbit polytopes

## Finding

For every integer \(n\ge4\) and strictly increasing positive weight list \(a=(a_1,\ldots,a_n)\), compare two natural signed-permutation orbit polytopes:
\[
B_n(a)=\operatorname{conv}\{(\varepsilon_i a_{\sigma(i)})_{i=1}^n:\varepsilon_i\in\{-1,1\},\ \sigma\in S_n\},
\]
\[
D_n(a)=\operatorname{conv}\{(\varepsilon_i a_{\sigma(i)})_{i=1}^n:\prod_i\varepsilon_i=1,\ \sigma\in S_n\}.
\]
Every orbit point is a vertex: all have squared Euclidean norm \(\sum_i a_i^2\), and a point of that norm cannot be a nontrivial convex combination of other points on that sphere. Therefore the second polytope has exactly half as many vertices as the first.

Let \(h_K(u)=\max_{x\in K}\langle x,u\rangle\) and \(W_K(u)=h_K(u)+h_K(-u)\) for \(\|u\|_2=1\). Let \(m(u)=\min_i|u_i|\), and let \(p(u)\in\{0,1\}\) be the parity of the number of negative coordinates for vectors with no zero coordinates. The exact one-sided support difference is
\[
h_{B_n(a)}(u)-h_{D_n(a)}(u)=2a_1m(u)p(u).
\]
When a coordinate is zero, this difference equals zero. Consequently,
\[
d_H(B_n(a),D_n(a))=\frac{2a_1}{\sqrt n}.
\]
The full directional-width defect \(\Delta_n(u)=W_{B_n(a)}(u)-W_{D_n(a)}(u)\) equals
\[
\Delta_n(u)=\begin{cases}2a_1m(u),& n\ \text{odd},\\4a_1m(u)p(u),&n\ \text{even}.\end{cases}
\]
Thus the angular fraction of directions with unchanged width is zero for odd \(n\) and exactly one half for even \(n\).

For a Haar-uniform unit direction \(U_n\), let \(\lambda=\sqrt{2/\pi}\), let \(E\) be exponential with rate \(\lambda\), and let \(J\) be an independent Bernoulli random variable with success probability one half. Along either parity subsequence, and for *any* sequence of strictly positive increasing weights,
\[
\frac{n^{3/2}}{a_1}\Delta_n(U_n)\ \Longrightarrow\ \begin{cases}2E,&n\ \text{odd},\\4JE,&n\ \text{even}.\end{cases}
\]
All fixed positive moments converge. In particular the normalized expected width loss tends to \(2/\lambda=\sqrt{2\pi}\) for both parities, whereas its limiting variance is \(4/\lambda^2=2\pi\) for odd dimensions and \(12/\lambda^2=6\pi\) for even dimensions. These limits concern the difference between the same two orbit polytopes in the same random direction, not the width law of either polytope separately.

## Assumptions and scope

The weights satisfy \(0<a_1<\cdots<a_n\), the coordinate metric is standard Euclidean, and the random direction is uniform on the whole sphere \(S^{n-1}\). The weights may depend arbitrarily on \(n\). The case \(a_i=i\) gives the canonical pair of strictly positive signed-permutation orbit models. These are the full signed-permutation and even-sign-change orbit polytopes of the *same* vector; they are not defined using the two different Weyl vectors of the root systems, one of which has a zero coordinate.

## Proof

**Exact support optimization.** Write \(b_i=|u_i|\) and arrange them nondecreasingly as \(b_{(1)}\le\cdots\le b_{(n)}\). Rearrangement and independent sign optimization yield
\[
h_{B_n(a)}(u)=\sum_{i=1}^n a_i b_{(i)}.
\]
If the number of negative coordinates of \(u\) is even, a maximizing signed permutation already has even sign parity, and the two support functions agree. Otherwise, every feasible even-sign orbit point mismatches at least one sign with \(u\). For any permutation \(\sigma\) the resulting objective is at most
\[
\sum_i a_{\sigma(i)}b_i-2\min_i a_{\sigma(i)}b_i
\ \le\ \sum_i a_i b_{(i)}-2a_1b_{(1)}.
\]
Equality is attained by the rearrangement-optimal assignment and reversing the sign on the smallest-absolute-value coordinate. This proves the support formula. With a zero coordinate, parity can be corrected at no cost, giving zero support difference; all sphere statements use directions with nonzero coordinates almost surely.

**Two-sided width and Hausdorff distance.** Under \(u\mapsto-u\), the number of negative coordinates changes parity exactly when \(n\) is odd. Adding the support losses at \(u\) and \(-u\) gives the displayed width formula. Since \(D_n(a)\subset B_n(a)\), the support-function characterization of Euclidean Hausdorff distance gives
\[
d_H(B_n(a),D_n(a))=\max_{\|u\|_2=1}\bigl(h_{B_n(a)}(u)-h_{D_n(a)}(u)\bigr).
\]
Here \(m(u)\le1/\sqrt n\); equality is obtained by choosing all coordinates to have equal absolute value and an odd number of negative signs. Thus the formula for \(d_H\) is sharp.

**Gaussian angular limit.** Let \(G_1,\ldots,G_n\) be independent standard Gaussians and set \(R_n=(\sum_iG_i^2)^{1/2}\), \(M_n=\min_i|G_i|\), \(U_n=G/R_n\). Then \(U_n\) is uniform on the sphere and
\[
n^{3/2}m(U_n)=(nM_n)\frac{\sqrt n}{R_n}.
\]
The half-normal distribution satisfies \(\Pr(|G_i|\le z)=\lambda z+O(z^3)\) as \(z\downarrow0\). Hence for fixed \(t\ge0\),
\[
\Pr(nM_n>t)=\bigl(1-\lambda t/n+O(n^{-3})\bigr)^n\to e^{-\lambda t}.
\]
Also \(R_n/\sqrt n\to1\) in probability. Slutsky's theorem gives \(n^{3/2}m(U_n)\Rightarrow E\). Gaussian signs are independent of Gaussian absolute values, so the sign-parity variable is independent of \(M_n\) and \(R_n\) and is exactly Bernoulli one half. The two parity limits follow.

**Moments.** There is an absolute \(c>0\) such that \(\Pr(|G|>z)\le e^{-cz}\) for all \(z\ge0\), which gives \(\Pr(nM_n>t)\le e^{-ct}\), uniformly in \(n,t\). Thus the moments of \(nM_n\) are uniformly bounded at every fixed order. For fixed \(q>0\), inverse chi-square moments show \(\sup_{n\ge n_q}\mathbb E[(\sqrt n/R_n)^q]<\infty\). Hölder's inequality proves uniform integrability of every fixed power of \(n^{3/2}m(U_n)\), hence moment convergence. Since \(\mathbb E E=1/\lambda\) and \(\mathbb E E^2=2/\lambda^2\), the stated means and variances follow.

## Verification

The standalone `verify.py` directly enumerates all signed-permutation vertices for ranks \(2,3,4,5\), compares unconstrained and even-sign support maxima against the exact formula in 27 deterministic pseudorandom cases, and checks both directional widths. Its separate sampling diagnostic reports the expected asymptotic scale of \(n^{3/2}\min_i|U_i|\) at three larger dimensions. Only the analytical proof establishes statements for arbitrary rank and weight lists; sampling does not establish the limiting distribution.

## Relationship to prior work

Ardila, Castillo, Eur and Postnikov study Coxeter permutahedra, type-B and type-D submodular descriptions, and deformations, providing the natural reflection-group geometric setting. Godland and Kabluchko give detailed type-B orbit-polytope formulas for projected face counts and conic angle sums. Neither of these inspected treatments states the *coupled* type-B/type-D support loss, its exact Hausdorff modulus, or its parity-dependent random-width distribution. General Coxeter orbit-support principles recover each individual support maximum abstractly, but an implication to the two-scale spherical parity law additionally requires the explicit cross-type sign-optimization identity and the minimum-order-statistic limit. The finite rearrangement argument itself is elementary and is not represented as a novel general optimization principle.

## Limitations

This result compares full and even signed permutation orbits of the *same* generic strictly positive weight vector. It does not compare the standard type-B and type-D root-sum zonotopes under their distinct Weyl-vector choices. The original-result assessment is bibliographic, not an independence certificate: equivalent formulas could exist in less-indexed literature on signed orbit polytopes. No claim is made about stochastic widths of unrelated Coxeter families or independent mathematical validation.

## References

1. F. Ardila, F. Castillo, C. Eur, A. Postnikov, *Coxeter submodular functions and deformations of Coxeter permutahedra*, first publicly posted 24 April 2019, arXiv:1904.11029; *Advances in Mathematics* 365 (2020), 107039.
2. T. Godland, Z. Kabluchko, *Projections and Angle Sums of Belt Polytopes and Permutohedra*, first publicly posted 9 September 2020, arXiv:2009.04186; *Results in Mathematics* 78 (2023), 140, DOI:10.1007/s00025-023-01918-2.
