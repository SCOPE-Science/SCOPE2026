# Exact endpoint probabilities and a logistic critical window for complete bipartite cover tours

## Finding
Let \(K_{a,b}\) be the complete bipartite graph with parts \(A,B\), where \(a,b\ge1\), and start the simple random walk from a fixed vertex \(u\in A\). Stop on the first visit to every vertex, and write \(P_{a,b}\) for the probability that the last **newly visited** vertex belongs to \(B\). Then
\[
P_{a,b}=\sum_{i=1}^{a}\sum_{j=1}^{b}(-1)^{i+j}\binom ai\binom bj\frac{ib}{ib+ja-ij}.
\]
Every vertex in \(B\) has probability \(P_{a,b}/b\) of being last; for \(a\ge2\), every vertex in \(A\setminus\{u\}\) has probability \((1-P_{a,b})/(a-1)\).

There are two complementary exact and asymptotic classifications. If \(a=b=m\ge2\), let \(T_m,T'_m\) be independent completion times for ordinary uniform \(m\)-coupon collectors, each starting with no coupons, and put \(\rho_m=\Pr(T_m=T'_m)\). Then
\[
P_{m,m}=\frac{1+\rho_m}{2},\qquad
\rho_2=\frac13,\qquad 0<\rho_m<\frac1{2m-1}\quad(m\ge3),
\]
with the asymptotic laws
\[
m\rho_m\longrightarrow\frac14,\qquad
P_{m,m}=\frac12+\frac1{8m}+o(m^{-1}).
\]
Consequently, for \(m\ge3\) any specified other vertex in \(A\) is strictly more likely to be last than any specified vertex in \(B\); their probability difference is
\[
\frac{1-(2m-1)\rho_m}{2m(m-1)}\sim\frac1{4m^2}.
\]
At \(m=2\) all three potential endpoints have equal probability, as required for the four-cycle.

For every fixed real \(c\), let \(a_m=m\) and \(b_m=m+\lfloor cm/\log m\rfloor\), positive for all sufficiently large \(m\). Then
\[
\lim_{m\to\infty}P_{a_m,b_m}=\frac1{1+e^{-c}}.
\]
The imbalance window \(m/\log m\) is sharp: if \(b_m/m\to1\) and \((b_m-m)\log m/m\to+\infty\), the limit is \(1\); if the last ratio tends to \(-\infty\), the limit is \(0\). For the narrow two-vertex starting part, a separate finite closed form holds for every \(b\ge1\):
\[
P_{2,b}=1-\frac2{\binom{2b}b}.
\]

## Assumptions and scope
The graph is finite, undirected, unweighted, simple and complete bipartite; the walk chooses a uniformly random neighbor at each step. An endpoint is the final vertex **first discovered**, not the state after further returns. The starting vertex is a specified member of \(A\). The formula includes stars and the single edge, with the obvious omission of same-part endpoint probabilities when \(a=1\). The window results concern sequences of integers as \(m\to\infty\); finite-sample inequalities are claimed only where explicitly stated.

## Proof
**Independent coupon streams.** At odd walk steps the vertices visited in \(B\) are independent uniform draws from \(B\); at even steps the vertices visited in \(A\) are independent uniform draws from \(A\); and the two sequences are independent. Put \(T_k\) for the number of draws needed to collect all \(k\) coupon types from a fresh independent stream. Since the initial \(A\)-vertex has already been seen, the number of subsequent \(A\)-draws required to see the other \(a-1\) vertices has distribution \(T_a-1\). Thus \(B\) supplies the last new vertex if and only if \(2T_b-1>2(T_a-1)\), or equivalently \(T_b\ge T_a\), with the two coupon times independent. In particular,
\[
P_{a,b}=\Pr(T_b\ge T_a).
\]

**Exact formula.** Inclusion-exclusion gives, for integer \(t\ge0\),
\[
F_k(t):=\Pr(T_k\le t)=\sum_{i=0}^k(-1)^i\binom ki(1-i/k)^t.
\]
For integer \(t\ge1\),
\[
\Pr(T_a=t)=\sum_{i=1}^a(-1)^{i+1}\binom ai\frac ia(1-i/a)^{t-1},
\]
and \(\Pr(T_b\ge t)=\sum_{j=1}^b(-1)^{j+1}\binom bj(1-j/b)^{t-1}\). Multiply and sum over \(t\ge1\). Each inner geometric series has ratio strictly below one, and its denominator simplifies to \((ib+ja-ij)/(ab)\). This gives the stated double sum. The within-part individual endpoint probabilities follow from vertex-exchangeability.

**Balanced exact inequality and correction.** When \(a=b=m\), exchangeability of the independent coupon times gives \(\Pr(T'_m>T_m)=(1-\rho_m)/2\), so \(\Pr(T'_m\ge T_m)=(1+\rho_m)/2\). Represent a coupon time as a sum of independent geometric waiting times:
\[
T_m\stackrel d=\sum_{j=1}^m H_j,\qquad
\Pr(H_j=t)=\frac jm\bigl(1-\frac jm\bigr)^{t-1},\quad t\ge1.
\]
Here \(H_1\) has success probability \(1/m\), while \(S=H_2+\cdots+H_m\) is independent of \(H_1\). For independent copies \(S,S'\), the \(\ell^2\) convolution inequality gives
\[
\rho_m=\|p_S*p_{H_1}\|_2^2\le\|p_{H_1}\|_2^2=\frac1{2m-1}.
\]
The inequality is strict if \(S\) is non-degenerate (\(m\ge3\)); it is equality for \(m=2\) when \(S\equiv1\). This proves the comparison of individual endpoint probabilities, including its sharp equality boundary.

For the coefficient, standard inclusion-exclusion and Bonferroni truncation yield the Gumbel limit \((T_m-m\log m)/m\Rightarrow G\) with density \(g(x)=e^{-x-e^{-x}}\). Fourier inversion on the integer lattice gives
\[
m\rho_m=\frac1{2\pi}\int_{-\pi m}^{\pi m}\left|\mathbb E e^{itT_m/m}\right|^2\,dt.
\]
For \(|t|\le\pi m\) and \(m\ge2\), the single \(H_1\) factor bounds the integrand by \((1+2t^2/\pi^2)^{-1}\), using \(1-\cos x\ge2x^2/\pi^2\) for \(|x|\le\pi\). The bound is integrable; weak convergence supplies pointwise convergence of the moduli to the Gumbel characteristic modulus. Dominated convergence followed by Plancherel yields
\[
\lim_{m\to\infty}m\rho_m=\int_{\mathbb R}g(x)^2\,dx
=\int_0^\infty y e^{-2y}\,dy=\frac14.
\]
Substitution into the finite exact endpoint identities proves both asymptotic constants.

**Logistic imbalance window.** Write \(b_m=m+\delta_m\). The independent classical coupon limits imply
\[
\frac{T_{b_m}-b_m\log b_m}{b_m}\Rightarrow G_1,
\qquad\frac{T_m-m\log m}{m}\Rightarrow G_2,
\]
with independent standard Gumbel variables \(G_1,G_2\). For \(\delta_m=\lfloor cm/\log m\rfloor\), both coupon scales are asymptotic to \(m\), while \((b_m\log b_m-m\log m)/m\to c\). Therefore \((T_{b_m}-T_m)/m\Rightarrow c+G_1-G_2\). The difference has a continuous logistic law, so there is no limiting tie ambiguity and
\[
\Pr(c+G_1-G_2\ge0)=\frac1{1+e^{-c}}.
\]
If \(\delta_m=o(m)\) but \(\delta_m\log m/m\to\pm\infty\), the deterministic difference in coupon centering dominates the tight Gumbel fluctuations, proving the two off-window limits.

**A two-vertex part.** For \(a=2\), the second \(A\)-vertex first appears after a geometric number of \(A\)-draws with success probability \(1/2\). Conditioning on \(T_b\) gives \(P_{2,b}=1-\mathbb E[2^{-(T_b-1)}]\). The independent-geometric representation of \(T_b\) gives
\[
\mathbb E[2^{-(T_b-1)}]=2\prod_{j=1}^b\frac j{b+j}
=\frac{2}{\binom{2b}b},
\]
as claimed.

## Verification
Run `python3 verify.py` from the extracted directory. The standalone program uses only standard-library exact rational arithmetic. It checks the double inclusion-exclusion sum independently against a state-count Markov recurrence for all \(1\le a,b\le8\), verifies the two-vertex formula through \(b=17\), and checks the balanced collision identity, exact inequalities and special values through \(m=11\). The run completed with **190 exact assertions passed**. Infinite-sample and asymptotic conclusions use the arguments above, not the finite computations.

## Relationship to prior work
The 1993 Lovász–Winkler and 2022 Buchanan–Horn–Rombach results classify graphs whose cover-tour endpoints are uniform; their assertions do not furnish the all-parameter endpoint probabilities or the near-balanced logistic window stated here. The 2003 Myers–Wilf paper **already evaluates exactly** the probability that two equal-size independent coupon collectors finish simultaneously; the finite balanced tie values are therefore not presented as new. The classical coupon-collector Gumbel theorem is also preexisting, and supplies a needed limiting ingredient. The present claim combines a graph-specific, all-parameter endpoint reduction, the finite two-vertex central-binomial law, and an explicit uniformity-crossover calculation with its balanced \(m^{-1}\) correction; no novelty is asserted for the standalone coupon-collector tie formula or Gumbel limit.

## Limitations
No complete finite-sample sign classification for unequal part sizes is asserted. The logistic statement concerns proportions of last endpoints **by side**, not a limiting distribution on named vertices. Stronger or equivalent results might be implicit in other complete-bipartite cover-time analyses or in older two-population occupancy work; historical priority is not independently certified. Finite exact checks do not certify the infinite asymptotics. This note provides a mathematical argument rather than an independently validated publication.

## References
1. C. Buchanan, P. Horn, P. Rombach, *On the Last New Vertex Visited by a Random Walk in a Directed Graph*, arXiv:2209.08079v1 (first public 2022-09-16), https://arxiv.org/abs/2209.08079.
2. L. Lovász, P. Winkler, *A Note on the Last New Vertex Visited by a Random Walk*, Journal of Graph Theory 17 (1993), 593–596, https://doi.org/10.1002/jgt.3190170505.
3. A. N. Myers, H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1 (2003), §2.1, https://arxiv.org/html/math/0304229v1.
4. A. Pósfai, *Approximation Theorems Related to the Coupon Collector's Problem*, arXiv:1006.3531 (2010), https://arxiv.org/abs/1006.3531.
