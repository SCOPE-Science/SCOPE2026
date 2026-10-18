# Sharp radial mean-body envelopes of Cartesian products of simplices

## Finding
Let \(k\ge2\) and let \(K=\Delta_1\times\cdots\times\Delta_k\), where \(\Delta_i\) is any nondegenerate \(d_i\)-simplex in a Euclidean space of dimension \(d_i\ge1\). Set \(D=\sum_i d_i\), \(\delta=\min_i d_i\), and \(L=K-K\). Define the Gardner–Zhang radial mean body \(R_pK\) for each finite real \(p>-1\), including the logarithmic limit at \(p=0\). For every positive integer \(m\), let
\[
 c_{m,p}=\begin{cases}
 \displaystyle\left(\prod_{j=1}^{m}\frac{j}{j+p}\right)^{1/p},&p\ne0,\\[4pt]
 \exp(-H_m),&p=0,
 \end{cases}\qquad H_m=\sum_{j=1}^{m}\frac1j.
\]
Then the following **sharp radial inclusions** hold for every \(p>-1\):
\[
 \boxed{\quad c_{D,p}L\ \subset\ R_pK\ \subset\ c_{\delta,p}L.\quad}
\]
For any nonzero direction \(x=(x_i)_i\), put \(a_i=\|x_i\|_{\Delta_i-\Delta_i}\) and \(a=\max_i a_i\). Equality at the lower radial bound occurs **exactly** when every \(a_i=a\); equality at the upper bound occurs **exactly** when one and only one \(a_i\) is nonzero, and that block has dimension \(\delta\). Thus both constants are optimal for the *fixed* product \(K\), not merely over all products.

The exact directional law is also available. If \(T_x\) denotes the exit distance along \(x\) from a point chosen uniformly in \(K\), then
\[
 \Pr(T_x>t)=\prod_{i=1}^k(1-ta_i)_+^{d_i}\quad(t\ge0),
\]
and \(T_x\) is distributed as the minimum of independent scaled \(\operatorname{Beta}(1,d_i)\) random variables (omit zero blocks). Consequently the entire radial profile, not only the sharp bounds, is an explicit finite beta-polynomial integral.

The sharp distortion between the outer and inner multiples of \(L\) is
\[
 A_{D,\delta}(p)=\frac{c_{\delta,p}}{c_{D,p}}
 =\begin{cases}
 \displaystyle\exp\!\left(\frac1p\sum_{j=\delta+1}^{D}\log(1+p/j)\right),&p\ne0,\\
 \exp(H_D-H_\delta),&p=0.
 \end{cases}
\]
It decreases **strictly** in \(p\in(-1,\infty)\), from the unattained limiting value \(D/\delta\) as \(p\downarrow-1\) to \(1\) as \(p\to+\infty\).

A nontrivial dimension–parameter crossover occurs for \(K_N=\Delta_N\times\Delta_N\) with \(N\ge2\). If \(p_N/N\to\lambda>0\), then
\[
 \lim_{N\to\infty}\log A_{2N,N}(p_N)
 =F(\lambda)
 :=\frac{(2+\lambda)\log(2+\lambda)-(1+\lambda)\log(1+\lambda)-2\log 2}{\lambda}.
\]
If instead \(p_N/N\to0\) with \(p_N>-1\), then \(A_{2N,N}(p_N)\to2\); if \(p_N/N\to+\infty\), then \(A_{2N,N}(p_N)\to1\). Thus the two limits in dimension and exponent do not commute, and \(p\) of order \(N\) is the exact transition scale.

## Assumptions and scope
Products are taken in the direct sum of factor vector spaces. The factors may be translated, arbitrarily shaped and arbitrarily scaled simplices; all formulas are affine invariant. Here \(B-B\) is the difference body of \(B\), \(\|\cdot\|_B\) is the Minkowski gauge for a body containing the origin, and \(z_+=\max\{z,0\}\). The mean body is defined, for a unit vector \(u\), using the one-sided exit distance \(T_u(X)=\sup\{t\ge0:X+tu\in K\}\) from a uniformly sampled \(X\in K\):
\[
 \rho_{R_pK}(u)=\begin{cases}(\mathbb E T_u^p)^{1/p},&p\ne0,\\ \exp(\mathbb E\log T_u),&p=0.\end{cases}
\]
For \(-1<p<0\) these are finite negative moments, not reciprocal positive moments. This normalization is the Gardner–Zhang convention; convexity in the negative range is supplied by Langharst's theorem [1]. The sharp constants refer to **radial containments** in the intrinsic gauge of \(K-K\), not Euclidean inradii or Banach–Mazur distances. The new non-parallelotope regime requires at least one \(d_i\ge2\), although the identities also specialize to cubes.

## Proof
**1. The simplex covariogram is a power of its difference-body gauge.** Fix a \(d\)-simplex \(\Delta=\operatorname{conv}(v_0,\ldots,v_d)\). Every translation vector \(y\) has unique barycentric increments \(b_j\) with \(\sum_jb_j=0\) and \(y=\sum_jb_jv_j\). In barycentric coordinates the overlap \(\Delta\cap(\Delta+y)\) is described by \(z_j\ge\max\{0,b_j\}\), \(\sum_jz_j=1\). It is empty if \(s:=\sum_j(b_j)_+>1\), otherwise a translated homothetic simplex with scale \(1-s\). As \(y\in t(\Delta-\Delta)\) holds exactly when \(\sum_j(b_j)_+\le t\), one has \(s=\|y\|_{\Delta-\Delta}\). Therefore
\[
 \frac{|\Delta\cap(\Delta+y)|}{|\Delta|}=(1-\|y\|_{\Delta-\Delta})_+^d.
\]
This elementary overlap formula is also the usual simplex-case computation underlying earlier radial-body work; it is not asserted new for a single simplex.

**2. Independent beta exit laws.** Because Cartesian-product intersections and volumes factor, for any ray \(tx\),
\[
 \frac{|K\cap(K+tx)|}{|K|}=\prod_i(1-ta_i)_+^{d_i}.
\]
The left side is \(\Pr(T_x>t)\), since a uniformly chosen point remains inside after translation by \(tx\) precisely on this intersection. The factors are survival functions of \(U_i/a_i\) with independent \(U_i\sim\operatorname{Beta}(1,d_i)\); for \(a_i=0\) ignore the corresponding block. This proves the complete exit law. In particular the limiting support is \(0\le t\le1/a\) and \(\rho_L(x)=1/a\) in the degree-minus-one radial extension.

**3. Stochastic sandwich and equality.** Scale \(x\) to make \(a=1\), so \(0\le a_i\le1\) and at least one \(a_i=1\). For every \(0<t<1\),
\[
 (1-t)^D\ \le\ \prod_i(1-ta_i)^{d_i}\ \le\ (1-t)^\delta.
\]
The left inequality is strict on the entire interval unless **all** \(a_i=1\). For the right inequality, choose a block with \(a_i=1\), whose dimension is at least \(\delta\). Equality throughout the interval is possible precisely if it has dimension \(\delta\) and every other \(a_j=0\). For \(t\ge1\) the survival functions are all zero. These are exactly the stochastic bounds
\[
 U_D\preceq_{\mathrm{st}}\ aT_x\preceq_{\mathrm{st}}U_\delta,
 \qquad U_m\sim\operatorname{Beta}(1,m).
\]
The ordinary generalized mean \((\mathbb E Z^p)^{1/p}\) is strictly increasing under strict stochastic domination for every finite \(p>-1\), \(p\ne0\); for negative \(p\) the moment inequality reverses but the negative reciprocal power reverses it back. The logarithmic mean is strictly increasing as well. Direct beta integration gives
\[
 \mathbb E U_m^p= mB(p+1,m)
 =\frac{m!\,\Gamma(p+1)}{\Gamma(p+m+1)}
 =\prod_{j=1}^m\frac{j}{j+p},
 \qquad\mathbb E\log U_m=-H_m.
\]
Thus multiplication by \(\rho_L(x)\) yields the inclusions and all equality conditions for \(R_pK\). Their sharpness is realized by choosing vectors \(x_i\) with equal positive \(\Delta_i-\Delta_i\) gauges, or a single nonzero minimal-dimensional block, respectively.

**4. Strict parameter monotonicity.** Taking logarithms of the exact ratio gives
\[
 \log A_{D,\delta}(p)=\sum_{j=\delta+1}^D\frac{\log(1+p/j)}p.
\]
Each summand decreases strictly on \((-1,\infty)\). Indeed, for \(p\ne0\), its derivative is \(\big(p/(j+p)-\log(1+p/j)\big)/p^2<0\), by \(\log z>1-1/z\) whenever \(z>0\), \(z\ne1\). At zero the continuous derivative is \(-1/(2j^2)<0\). As \(p\downarrow-1\), the factors indexed by \(j\ge2\) give \(\sum_{j=\delta+1}^D\log(j/(j-1))=\log(D/\delta)\); as \(p\to\infty\), every fixed summand tends to zero. This proves monotonicity and both limits.

**5. The dimension–exponent crossover.** For two equal factors of dimension \(N\),
\[
 \log A_{2N,N}(p)=\frac1p\sum_{j=N+1}^{2N}\log(1+p/j).
\]
When \(p/N\to\lambda\in(0,\infty)\), this is a Riemann sum tending to \(\lambda^{-1}\int_1^2\log(1+\lambda/t)\,dt\), whose antiderivative gives the displayed \(F\). If \(p/N\to0\), the expansion \(\log(1+p/j)/p=1/j+O(|p|/j^2)\) is uniform for \(j>N\), since \(p>-1\); summation gives \(\log A\to\log2\). If \(p/N\to\infty\), the upper bound \(0\le\log A\le(N/p)\log(1+p/N)\to0\) completes the proof.

## Verification
The standalone `verify.py` checks the beta moment identities by exact rational polynomial integration in dimensions including \((2,3)\), \((2,4,1)\), and \((3,3)\), at exponents both positive and negative; it checks the exact stochastic moment inequalities and the logarithmic endpoint, and compares numerical values against the rigorous crossover and monotonicity formulas. Execute `python3 verify.py` (standard library only). Finite checks do not prove the theorem: the complete proof is the barycentric intersection identity, stochastic ordering, strict equality analysis, and Riemann-sum argument above.

## Relationship to prior work
Gardner and Zhang [3] introduced radial mean bodies. Langharst's 2026 result [1] establishes convexity for the negative exponent range, and supplies the standard covariogram moment representation. Ni, Xiong and Cheung [4] consider individual simplices; the simplex overlap formula is acknowledged rather than claimed original. Langharst, Manui and Zvavitch [2], Proposition 34, develop a cube integral formula. Existing published square contact classifications and cube differentiability classifications [5,6] concern the **all-one-dimensional factor** case and thus do not establish the present sharp \(D\)-versus-\(\delta\) bounds, blockwise equality classification, or balanced high-dimensional simplex-product crossover. The new geometric content is the simultaneous, globally sharp direction classification across products with genuine simplex factors, with a nontrivial dimension–parameter limit. A general stochastic distance-between-two-uniform-points inequality [7] concerns a different random variable, not one-point directional exit distances.

## Limitations
The result does not establish a universal optimal inclusion for arbitrary convex bodies; its exact constants depend on the product-of-simplices structure. The all-segment (cube) specialization is already represented in the earlier cube literature and is not claimed new. The 2007 simplex paper [4] could be compared by abstract but its full text was unavailable through attempted lawful retrieval; possible unindexed previous tensor-product computations remain a genuine historical priority risk. The crossover statement is asymptotic and does not assert a finite-\(N\) uniform error bound. Independent audit and independent validation have not been performed.

## References
1. D. Langharst, *Radial Mean Bodies Are Convex* (initial preprint title; later revised as *Convexity of Radial Mean Bodies via an Extension of Ball's Bodies*), arXiv:2603.14134v1, first public March 14, 2026; https://arxiv.org/abs/2603.14134 .
2. D. Langharst, A. Manui, A. Zvavitch, *On The Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117v1, first public January 27, 2026; https://arxiv.org/abs/2601.20117 .
3. R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, Amer. J. Math. 120 (1998), 505–528, DOI 10.1353/ajm.1998.0021.
4. G. Ni, G. Xiong, K. Cheung, *Radial mean bodies of simplices* (2007), DOI 10.1007/s11741-007-0108-z; full text not inspected.
5. *A four-to-four contact transition in radial mean bodies of the square*, published mathematical research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-four-to-four-contact-transition-in-radial-mean-bodies-of-the-s--9b3146060ea1 .
6. *Sharp differentiability strata of radial mean bodies of parallelotopes*, published mathematical research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-differentiability-strata-of-radial-mean-bodies-of-parallel--fc444dfaf505 .
7. *A sharp beta stochastic bound for difference-body distances*, published mathematical research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-beta-stochastic-bound-for-difference-body-distances--4609b4d88176 .
