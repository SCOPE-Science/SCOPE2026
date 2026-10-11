# A bounded monomial composition operator with nonconvergent Aluthge iterates

## Finding

There exists a weighted Hardy space \(H^2(\beta)\) on the unit disk with \(\beta(0)=1\), \(n^{-1}\le\beta(n)\le n\) for every integer \(n\ge1\), and \(\beta(n+1)/\beta(n)\to1\), on which the **unweighted** composition operator
\[
T=C_{z^2},\qquad (Tf)(z)=f(z^2),
\]
is bounded with exact norm \(\|T\|=2\), yet its ordinary Aluthge iterates \(\Delta^N(T)\) do not converge in the weak operator topology. In fact, for explicit unit vectors \(e_1,e_2\),
\[
\lim_{\substack{\ell\to\infty\\\ell\ \mathrm{even}}}
\langle\Delta^{3\cdot2^\ell}(T)e_1,e_2\rangle=2,
\qquad
\lim_{\substack{\ell\to\infty\\\ell\ \mathrm{odd}}}
\langle\Delta^{3\cdot2^\ell}(T)e_1,e_2\rangle=\tfrac12.
\]
Thus the universal strong-convergence question for bounded composition operators on arbitrary weighted Hardy spaces, posed as Question 5.2 in Lahiri--Ojha--Birbonshi (2026), has a negative answer even for the fixed symbol \(z^2\). This statement does not concern their more restricted Question 5.1.

## Assumptions and scope

For every nonnegative integer \(j\), set
\[
 s_j=(-1)^{\lfloor\log_2(j+1)\rfloor}.
\]
Let \(F:[0,\infty)\to\mathbb R\) be the continuous piecewise-affine function with \(F(0)=0\) and slope \(s_j\) on \((j,j+1)\). Hence \(F(j+1)-F(j)=s_j\), and \(F\) is \(1\)-Lipschitz with \(|F(t)|\le t\). Define
\[
 \beta(0)=1,\qquad \beta(n)=2^{F(\log_2 n)}\quad(n=1,2,\ldots).
\]
Write
\[
 H^2(\beta)=\left\{f(z)=\sum_{n\ge0}a_nz^n:\sum_{n\ge0}|a_n|^2\beta(n)^2<\infty\right\},
 \qquad e_n(z)=\frac{z^n}{\beta(n)}.
\]
The vectors \(e_n\) form an orthonormal basis. Because the weights have at most polynomial growth and decay, every element is holomorphic on the unit disk, and polynomial functions are dense. The Aluthge transform uses the polar decomposition \(T=U|T|\) and the convention \(\Delta(T)=|T|^{1/2}U|T|^{1/2}\), with \(\Delta^0(T)=T\).

## Proof

**1. The function space and boundedness.** By \(|F(t)|\le t\),
\[
 n^{-1}\le\beta(n)\le n\quad(n\ge1),\qquad
 \lim_{n\to\infty}\beta(n)^{1/n}=1.
\]
For \(n\ge1\), the Lipschitz estimate gives
\[
 \left|\log_2\frac{\beta(n+1)}{\beta(n)}\right|
 \le\log_2\left(1+\frac1n\right),
\]
so \(n/(n+1)\le\beta(n+1)/\beta(n)\le(n+1)/n\); the multiplication operator \(M_z\) is bounded and the neighboring ratios tend to one. The monomial composition operator acts by
\[
 Te_0=e_0,\qquad Te_n=d_ne_{2n},\qquad d_n=\frac{\beta(2n)}{\beta(n)}\quad(n\ge1).
\]
Again by Lipschitz continuity, \(1/2\le d_n\le2\). The output monomials are distinct, hence \(T\) is bounded and \(\|T\|\le2\). Since \(d_1=\beta(2)/\beta(1)=2\), equality holds. This establishes boundedness of actual analytic composition, not merely an abstract matrix representation.

**2. A reducing weighted-shift orbit.** The subspace
\[
 \mathcal H=\overline{\operatorname{span}}\{e_{2^j}:j\ge0\}
\]
is reducing for \(T\): \(T\) sends \(e_{2^j}\) to a multiple of \(e_{2^{j+1}}\), while \(T^*e_{2^j}\) is a multiple of \(e_{2^{j-1}}\) when \(j\ge1\), and zero at \(j=0\). No basis vector off the orbit maps onto one on the orbit. Under the identification \(e_{2^j}\leftrightarrow\delta_j\), the restriction is the unilateral positive weighted shift
\[
 W\delta_j=w_j\delta_{j+1},\qquad
 w_j=\frac{\beta(2^{j+1})}{\beta(2^j)}=2^{F(j+1)-F(j)}=2^{s_j}\in\{1/2,2\}.
\]
Each Aluthge transform respects orthogonal reducing direct sums because polar decomposition and positive functional calculus do.

**3. Exact iteration coefficients.** For any positive unilateral weighted shift \(V\delta_j=v_j\delta_{j+1}\), its polar decomposition is the unilateral shift times \(\operatorname{diag}(v_j)\); hence \(\Delta(V)\) has weights \((v_jv_{j+1})^{1/2}\). Inductively, the first weight of \(\Delta^N(W)\) is
\[
 b_N=\prod_{j=0}^{N}w_j^{2^{-N}\binom Nj}
 =2^{\,2^{-N}\sum_{j=0}^N\binom Nj s_j}
 =2^{\mathbb E[s_{B_N}]},
\]
where \(B_N\) has the binomial distribution \(\operatorname{Bin}(N,1/2)\). Because \(\mathcal H\) is reducing,
\[
 b_N=\langle\Delta^N(T)e_1,e_2\rangle.
\]
These equalities hold for every integer \(N\ge0\), not only at sampled indices.

**4. Two genuine subsequential limits.** Fix an integer \(\ell\ge4\) and put \(N_\ell=3\cdot2^\ell\). The mean of \(B_{N_\ell}\) is \(3\cdot2^{\ell-1}\). Whenever
\[
 |B_{N_\ell}-3\cdot2^{\ell-1}|<2^{\ell-2},
\]
its integer value lies in the block \(2^\ell-1\le j\le2^{\ell+1}-2\), on which \(s_j=(-1)^\ell\). Hoeffding's binomial tail inequality gives
\[
 \mathbb P\left(|B_{N_\ell}-N_\ell/2|\ge 2^{\ell-2}\right)
 \le2\exp(-2^\ell/24).
\]
Since \(|s_j|=1\), it follows that
\[
 \left|\mathbb E[s_{B_{N_\ell}}]-(-1)^\ell\right|
 \le4\exp(-2^\ell/24)\longrightarrow0.
\]
Therefore \(b_{N_\ell}\to2\) for even \(\ell\) and \(b_{N_\ell}\to1/2\) for odd \(\ell\). The fixed matrix coefficient has two distinct subsequential limits, so \(\Delta^N(T)\) cannot converge in weak operator topology and hence cannot converge strongly to a quasinormal or any other operator. This proves the claim.

## Verification

The standalone script `verification/check_aluthge.py` checks the integer slope identity and its endpoint bounds, the first three binomial-exponent identities, and exact rational binomial averages at \(N=3\cdot2^\ell\) for \(4\le\ell\le9\). It also numerically checks the stated Hoeffding upper bound at those finite indices. Its expected output is `MONOMIAL_COMPOSITION_ALUTHGE_BINOMIAL_IDENTITIES_OK`. These checks are supporting reproducibility tests; the universal nonconvergence result follows from the four-step analytic argument above.

## Relationship to prior work

Lahiri, Ojha and Birbonshi, arXiv:2604.27762v1 (first public posting April 30, 2026), prove strong convergence for particular linear-fractional composition operators and explicitly ask in their Question 5.2 whether **every** bounded composition operator on **some** weighted Hardy space has strongly convergent Aluthge iterates. The present counterexample answers precisely that broader question; their narrower Question 5.1 for two specified linear-fractional symbols is unaffected.

Chō, Jung and Lee (2005, preprint accessible online) already construct unilateral weighted shifts whose Aluthge iterates do not converge even weakly and give the binomial-weight formula. We do not claim those general weighted-shift facts as new. The added ingredient is a concrete, regular analytic weighted Hardy norm whose unweighted monomial composition operator contains an explicit divergent weighted shift as a reducing orbit. Jung, Kim and Ko (2015) study strong convergence for two linear-fractional symbols on the classical Hardy space; those special symbols do not cover this example. Benhida, Budzyński and Trepkowski (2018) study Aluthge transforms of weighted composition operators on general \(L^2\)-spaces, principally their domain and hyponormality behavior; they do not state this analytic composition counterexample in the inspected portions.

## Limitations

This disproves a universal convergence assertion on the full class of weighted Hardy coefficient spaces; it does not disprove convergence on classical Hardy or weighted Bergman spaces, nor for all possible weight sequences or for the linear-fractional families in Question 5.1. The binomial nonconvergence mechanism for abstract unilateral weighted shifts is prior work. No independent external proof audit has been performed.

## References

1. S. Lahiri, S. Ojha, R. Birbonshi, *Iterated Aluthge transforms of some composition operators on weighted Bergman spaces*, arXiv:2604.27762v1, April 30, 2026; especially Section 4 (definition of weighted Hardy spaces) and Section 5, Question 5.2. https://arxiv.org/pdf/2604.27762
2. M. Chō, I. B. Jung, W. Y. Lee, *On Aluthge transforms of \(p\)-hyponormal operators*, Integral Equations and Operator Theory **53** (2005), 321--329; Section 3, Proposition 3.2. Author-hosted manuscript: https://www.math.snu.ac.kr/~wylee/03CJL.pdf
3. S. Jung, Y. Kim, E. Ko, *Iterated Aluthge transforms of composition operators on \(H^2\)*, International Journal of Mathematics **26** (2015), 1550079. DOI: 10.1142/S0129167X15500792.
4. C. Benhida, P. Budzyński, J. Trepkowski, *Aluthge transforms of unbounded weighted composition operators in \(L^2\)-spaces*, arXiv:1809.01205v1 (2018). https://arxiv.org/pdf/1809.01205
