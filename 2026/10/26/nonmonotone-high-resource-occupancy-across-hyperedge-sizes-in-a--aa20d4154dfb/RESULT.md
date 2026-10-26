# Nonmonotone high-resource occupancy across hyperedge sizes in a state-dependent public-goods transition

## Finding

Consider the high/low resource-state transition prescribed by Wei et al. (2026) for a fixed population of cooperators, with sensitivity exponents \(\alpha_1=1\) and \(\alpha_2=2\). For \(n\geq3\) labeled vertices, exactly \(m\in\{0,\ldots,n\}\) cooperators and a uniformly sampled \(g\)-vertex hyperedge, let \(H_{n,m}(g)\) denote the hyperedge's stationary probability of being in the high-value resource state, averaged over the choice of edge.

For every \(2\leq g\leq n\), the exact value is
\[
H_{n,m}(g)=\frac{1}{\binom ng}\sum_{k=0}^g\binom mk\binom{n-m}{g-k}\frac{k^2}{g^2-gk+k^2},
\]
where impossible binomial coefficients are zero. In particular,
\[
H_{n,m}(2)=\frac{m(m+2n-3)}{3n(n-1)},\qquad
H_{n,m}(3)=\frac{m(3n^2+6nm-15n-2m^2-6m+14)}{7n(n-1)(n-2)},
\]
with exact difference
\[
H_{n,m}(3)-H_{n,m}(2)
=\frac{m(n-m)(6m-5n+4)}{21n(n-1)(n-2)}.
\]
For \(0<m<n\) this difference is negative exactly when \(6m<5n-4\). Nevertheless the full-population edge has \(H_{n,m}(n)=h(m/n)\) with \(h(x)=x^2/(1-x+x^2)\). The **smallest** population exhibiting the strict three-scale reversal \(H_{n,m}(3)<H_{n,m}(2)<H_{n,m}(n)\) is \(n=7\), with \(m=5\):
\[
H_{7,5}(3)=\frac{31}{49}<H_{7,5}(2)=\frac{40}{63}<H_{7,5}(7)=\frac{25}{39}.
\]
No population of size \(3\le n\le6\), for any nontrivial cooperator count, exhibits this exact three-scale strict reversal.

For a sequence of populations with \(n\to\infty\), \(m/n\to x\in(0,1)\), and each fixed edge size \(g\), the hypergeometric expression converges to
\[
H_g(x)=\sum_{k=0}^g\binom gk x^k(1-x)^{g-k}h(k/g).
\]
Write \(H_\infty(x)=\lim_{g\to\infty}H_g(x)=h(x)\). The **complete strict order diagram** for the benchmark group sizes two, three and unbounded is
\[
\begin{array}{ll}
0<x<1/\sqrt2: & H_\infty(x)<H_3(x)<H_2(x),\\
1/\sqrt2<x<\sqrt3-1: & H_3(x)<H_\infty(x)<H_2(x),\\
\sqrt3-1<x<5/6: & H_3(x)<H_2(x)<H_\infty(x),\\
5/6<x<1: & H_2(x)<H_3(x)<H_\infty(x).
\end{array}
\]
At the three internal endpoints the corresponding adjacent quantities are equal. In particular, for every \(x\in(1/\sqrt2,5/6)\), increasing group size from two to three **reduces** high-resource occupancy, while sufficiently large groups have **higher** occupancy than three-player groups. This is an exact conditional-environment phenomenon, not a conclusion about strategic cooperation frequency.

## Assumptions and scope

There are \(n\) fixed labeled agents, exactly \(m\) permanent cooperators, and binary resource states (high/low) attached to hyperedges of cardinality \(g\). Each edge has high-state transition probability \(q\) from high and \(q^2\) from low, with \(q=k/g\) its proportion of cooperators. All edges receive updates at positive rates independent of their resource states; the actual update-rate scale does not alter the stationary marginal. The edge is selected uniformly from all \(g\)-subsets, or an equivalently exchangeable random hypergraph supplies a uniformly marginal edge. No claim is made for the realized average of a fixed, nonequitable hypergraph or for strategy/environment coevolution. The model uses the original high/low transition probabilities with the indicated exponents; it does not assume independence of stationary edge states.

## Proof

**1. The frozen-edge invariant law.** The two-state transition matrix (rows: current high, low; columns: next high, low) is
\[
P(q)=\begin{pmatrix}q&1-q\\q^2&1-q^2\end{pmatrix}.
\]
A stationary high-state probability \(p\) obeys \(p=pq+(1-p)q^2\), whence \(p(1-q+q^2)=q^2\). Since \(1-q+q^2>0\) for every \(q\in[0,1]\), there is exactly one stationary distribution with \(p=h(q)\). For \(0<q<1\) the chain is irreducible and aperiodic; at \(q=0,1\) it has a unique absorbing class. Thus the stationary formula applies at both boundaries. State-independent random thinning of update times does not change this invariant probability.

**2. Hypergeometric averaging.** For an exchangeably drawn size-\(g\) hyperedge, the number \(K\) of cooperators has mass \(\Pr(K=k)=\binom mk\binom{n-m}{g-k}/\binom ng\). Taking the expectation of \(h(K/g)\) gives the first formula, without requiring independence between distinct edges. The values \(h(0)=0\), \(h(1/2)=1/3\), \(h(1)=1\), \(h(1/3)=1/7\) and \(h(2/3)=4/7\) yield the displayed two- and three-vertex closed forms by substitution and binomial simplification. Subtraction yields the exact factorization. When \(g=n\) the hyperedge is the whole vertex set, so \(K=m\) deterministically and \(H_{n,m}(n)=h(m/n)\).

**3. Sharp finite order.** At \((n,m)=(7,5)\), direct substitution gives the three stated fractions, with positive differences \(H(2)-H(3)=1/441\) and \(H(7)-H(2)=5/819\). For \(n=3,4,5,6\), the inequality \(h(m/n)>H_{n,m}(2)\) holds among \(1\le m<n\) only at \(m=n-1\), as follows from the sign of the polynomial
\[
m^2+(2n-3)m-2n^2+3n
\]
in the exact factorization
\[
h(m/n)-H_{n,m}(2)=\frac{m(n-m)[m^2+(2n-3)m-2n^2+3n]}{3n(n-1)(m^2-mn+n^2)}.
\]
For \(m=n-1\), the factor \(6m-5n+4=n-2>0\), so \(H_{n,m}(3)>H_{n,m}(2)\). Thus no smaller \(n\) satisfies both strict inequalities. Each of the finitely many cases can also be checked directly using exact rational arithmetic in the included program.

**4. Fixed-density group-size phases.** The hypergeometric sampling law tends to \(\operatorname{Binomial}(g,x)\) at every fixed \(g\), giving \(H_g(x)\). Since \(K/g\to x\) in probability as \(g\to\infty\) and \(h\) is bounded and continuous, \(H_g(x)\to h(x)\). Evaluating the first two binomial polynomials gives
\[
H_2(x)=\frac{2x+x^2}{3},\qquad H_3(x)=\frac{3x+6x^2-2x^3}{7}.
\]
Their complete comparisons factor exactly as
\[
H_3-H_2=\frac{x(1-x)(6x-5)}{21},
\]
\[
h-H_2=\frac{x(1-x)(x^2+2x-2)}{3(x^2-x+1)},
\]
\[
h-H_3=\frac{x(1-x)(3-x)(2x^2-1)}{7(x^2-x+1)}.
\]
All omitted factors in these formulas are positive on \((0,1)\). Their internal roots are respectively \(5/6\), \(\sqrt3-1\) and \(1/\sqrt2\), in ascending order \(1/\sqrt2<\sqrt3-1<5/6\). Sorting all three quantities between these thresholds proves the four-region classification. For \(x\in(1/\sqrt2,5/6)\), the strict inequalities \(H_3<H_2\) and \(H_3<h\), combined with convergence \(H_g\to h\), force some sufficiently large integer \(g>3\) with \(H_g>H_3\).

## Verification

The included standalone `verify.py` uses only Python's standard library and rational arithmetic. It directly reconstructs every edge expectation for \(3\le n\le37\), \(0\le m\le n\), and edge sizes two, three, and full population, compares the closed formulas and factorization, exhausts the smaller-population sharpness cases, checks the seven-agent witness, and cross-checks the three binomial difference identities at rational densities. It reports 4,155 successful assertions. The proof of all sizes and continuous-density intervals is analytic; these computations are consistency checks, not exhaustive infinite certification.

## Relationship to prior work

Wei, Xiong, Li, Feng and Szolnoki (2026) introduce the two-state resource-transition hypergraph public-goods model and its sensitivity exponents (their equations (6) and (7)), then report coevolving cooperation behavior mainly by simulation. The present result **conditions on frozen strategies** and computes an exact stationary resource marginal, revealing a size-order reversal that is not a conclusion from their cooperation-frequency plots. Su, McAvoy, Wang and Nowak (2019) already analyze stochastic game transitions and stationary transition matrices; basic two-state stationarity is not claimed as novel here. Feng, Pi, Deng and Kurths (2025 preprint; earlier journal publication) analyze Markovian individual game-state changes; that model differs from composition-dependent uniform-hyperedge averaging. Binomial limits and continuity are classical; the claimed contribution is the explicit environmentally motivated three-size phase diagram and smallest finite-population reversal under the specific 2026 transition kernel.

## Limitations

This result concerns the frozen-strategy conditional resource subsystem, not the stationary law of the coupled imitation process. It does not imply that larger groups increase or decrease the eventual **number of cooperators**, or that an arbitrary fixed hypergraph has the average shown. The full group-size ordering for all intermediate group sizes is not classified. The two- and three-size comparison exploits the special parameter choice \(\alpha_1=1\), \(\alpha_2=2\). Historical novelty is not guaranteed; the older related literature includes some uninspected full texts that are not known to cover the exact hypergeometric crossover.

## References

1. N. Wei, X. Xiong, Q. Li, M. Feng, and A. Szolnoki, *Cooperation in Public Goods Games over Uniform Random Hypergraphs with Game Transitions* (2026), arXiv:2603.22967v1, first submitted 24 March 2026, DOI:10.1098/rsif.2025.1319. https://arxiv.org/html/2603.22967v1
2. Q. Su, A. McAvoy, L. Wang, and M. A. Nowak, *Evolutionary dynamics with game transitions*, PNAS 116 (2019), 25398–25404, DOI:10.1073/pnas.1908936116, arXiv:1905.10269. https://arxiv.org/abs/1905.10269
3. M. Feng, B. Pi, L.-J. Deng, and J. Kurths, *An Evolutionary Game With the Game Transitions Based on the Markov Process*, IEEE Transactions on Systems, Man, and Cybernetics: Systems (published online 2023), DOI:10.1109/TSMC.2023.3315963, preprint arXiv:2502.05742. https://arxiv.org/abs/2502.05742
