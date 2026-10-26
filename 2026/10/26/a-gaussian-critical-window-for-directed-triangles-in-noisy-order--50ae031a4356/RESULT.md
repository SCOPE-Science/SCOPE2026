# A Gaussian critical window for directed triangles in noisy ordered tournaments

## Finding
Let \(n\ge3\). On the ordered vertex set \(\{1,\ldots,n\}\), independently orient every edge \(\{i,j\}\), \(i<j\), from \(i\) to \(j\) with probability \(p\in(0,1)\) and in the opposite direction with probability \(1-p\). Let \(C_n\) count unordered vertex triples whose three oriented edges form a directed cycle. Put \(r=p(1-p)\). Then, **exactly for every \(n,p\)**,
\[
\mathbb E C_n=\binom n3 r,\qquad
\operatorname{Var}(C_n)=3\binom n3 r^2+
\frac{n(n-1)^2(n-2)}{12}\,r(1-2p)^2.
\]
For every sequence \(p_n\in(0,1)\) with \(\sqrt n\,(p_n-1/2)\to c\in\mathbb R\),
\[
\frac{C_n-\mathbb EC_n}{n^{3/2}}
\ \Longrightarrow\ \mathcal N\!\left(0,\frac1{32}+\frac{c^2}{12}\right).
\]
For every fixed \(\epsilon\in(0,1/2)\) and every sequence \(p_n\in[\epsilon,1-\epsilon]\) satisfying \(\sqrt n\,|1-2p_n|\to\infty\),
\[
\frac{C_n-\mathbb EC_n}{n^2|1-2p_n|\sqrt{p_n(1-p_n)/12}}
\ \Longrightarrow\ \mathcal N(0,1).
\]
Thus the competition between quadratic and linear random fluctuations has the sharp bias scale \(n^{-1/2}\); its variance coefficient changes continuously across the critical window. The fair-tournament endpoint is included but is not asserted to be a previously unknown individual limit theorem.

## Assumptions and scope
The underlying ranking \(1<\cdots<n\) is deterministic. The \(\binom n2\) edge orientations are mutually independent, with the same rank-directed probability \(p\). A directed triangle is counted once per unordered triple; the two cyclic orientations are not counted separately. The theorem permits bias sequences depending on \(n\), subject to the displayed conditions. For the off-window theorem, the uniform positive lower bound on \(p_n\) and \(1-p_n\) is essential to the stated normalization and proof. No statement is made for sparse near-deterministic orientation regimes.

## Proof
**Exact decomposition.** For \(a<b\), let \(X_{ab}\) be the indicator of the orientation \(a\to b\), and define \(Y_{ab}=X_{ab}-p\). These variables are independent, centered, bounded, and have common variance \(r=p(1-p)\). For \(a<b<c\), the indicator \(I_{abc}\) of a directed cycle is precisely
\[
I_{abc}=X_{ab}X_{bc}(1-X_{ac})+(1-X_{ab})(1-X_{bc})X_{ac}.
\]
The cubic terms cancel on expansion. Substitution of \(X=p+Y\) yields the exact identity
\[
I_{abc}-r=(1-2p)Y_{ac}+
Y_{ab}Y_{bc}-Y_{ab}Y_{ac}-Y_{bc}Y_{ac}.
\]
Consequently
\[
C_n-\mathbb EC_n=L_n+Q_n,
\quad L_n=(1-2p)\sum_{a<c}(c-a-1)Y_{ac},
\]
\[
Q_n=\sum_{a<b<c}\big(Y_{ab}Y_{bc}-Y_{ab}Y_{ac}-Y_{bc}Y_{ac}\big).
\]
All products appearing in \(Q_n\) involve two distinct independent edge variables. Each unordered pair of incident edges of the complete graph appears in exactly one quadratic product, with coefficient \(+1\) or \(-1\). Distinct such products are orthogonal in \(L^2\): in their cross-product some centered edge variable occurs only once. Similarly, \(L_n\) and \(Q_n\) are orthogonal. Therefore
\[
\operatorname{Var}(Q_n)=3\binom n3 r^2,
\quad \operatorname{Var}(L_n)=r(1-2p)^2\sum_{a<c}(c-a-1)^2.
\]
Summing the squares by edge separation gives
\[
\sum_{a<c}(c-a-1)^2
=\sum_{d=0}^{n-2}(n-d-1)d^2
=\frac{n(n-1)^2(n-2)}{12}.
\]
This proves both finite moment formulas, including their boundary cases \(n=3\) and \(p=1/2\).

**Gaussian law inside the critical window.** Suppose \(\sqrt n(p_n-1/2)\to c\), and suppress the triangular-array subscript in the variables. The coefficients of individual terms in \(L_n\) have absolute value \(O(\sqrt n)\), uniformly in the edge, whereas the coefficients of terms in \(Q_n\) are \(\pm1\). All fixed moments of the \(Y_{ab}\) are bounded uniformly. We establish that for each fixed integer \(k\ge3\),
\[
\left|\kappa_k(L_n+Q_n)\right|=O_k(n^{k+1}),
\]
where \(\kappa_k\) is the ordinary cumulant.

Indeed, expand the cumulant multilinearly into ordered selections of \(k\) monomials. Suppose \(s\) selected monomials are linear and \(k-s\) are quadratic. A joint cumulant is zero if a centered base variable appears in only one occurrence among all factors: every moment involving the term containing that unique variable vanishes. It is also zero if the selected monomials split into two nonempty collections using disjoint sets of base variables, by independence. In a surviving selection, there are therefore at most \(v\le(2k-s)/2=k-s/2\) distinct base variables, and their corresponding edges in \(K_n\) form a connected graph (each quadratic monomial joins two incident edges). A connected graph with \(v\) edges uses at most \(v+1\) of the original \(n\) vertices. For fixed \(k\), the number of choices of those edges and their monomial incidence pattern is \(O_k(n^{v+1})\). The product of the \(s\) linear coefficients is \(O_k(n^{s/2})\). Thus all selections with at least one quadratic term contribute \(O_k(n^{k+1})\). When all \(k\) terms are linear, connectedness forces them all to use the same base variable: the contribution is at most \(O_k(n^{2+k/2})=O_k(n^{k+1})\). Joint cumulants of each fixed order are bounded because their arguments are bounded products of centered Bernoulli variables. This proves the bound.

For \(k\ge3\), dividing the cumulant by \(n^{3k/2}\) gives \(O_k(n^{1-k/2})\to0\). The exact variance yields
\[
\frac{\operatorname{Var}(L_n+Q_n)}{n^3}\longrightarrow
\frac{c^2}{12}+\frac1{32}>0.
\]
The first cumulant is zero. The moment–cumulant identities therefore imply convergence of all moments to those of the indicated centered Gaussian law; the Gaussian moment problem is determinate, giving convergence in distribution.

**Gaussian law outside the critical window.** Assume \(p_n\in[\epsilon,1-\epsilon]\) and \(\sqrt n\,|1-2p_n|\to\infty\). The exact variance formulas give
\[
\frac{\operatorname{Var}(Q_n)}{\operatorname{Var}(L_n)}
=O\!\left(\frac1{n(1-2p_n)^2}\right)\longrightarrow0.
\]
The linear term is a weighted sum of independent centered Bernoulli indicators. Its largest summand is bounded by \(n|1-2p_n|\), while its standard deviation is asymptotic to \(n^2|1-2p_n|\sqrt{r_n/12}\). Their ratio is \(O(1/n)\) uniformly under the stated \(\epsilon\) bound. Hence the Lindeberg condition holds, and the triangular-array Lindeberg–Feller theorem gives asymptotic normality for the normalized linear term. The quadratic remainder vanishes in \(L^2\) under this normalization; Slutsky's theorem finishes the proof.

## Verification
The standalone Python checker `tournament_cyclic_checker.py` independently enumerates every orientation of the tournament for \(n=3,4,5,6\) and for \(p\in\{1/4,1/3,1/2,2/3\}\), with exact rational probabilities. It checks the decomposition for each of the \(135{,}456\) weighted orientation states, computes the exact distribution and first two moments, and compares these moments to the formulas above. All 16 complete state-space cases passed. This computation verifies the finite formulas in the enumerated cases, **not** the unbounded Gaussian limits; those follow from the cumulant argument and the triangular-array CLT in the proof.

Reproduce with `python3 tournament_cyclic_checker.py` from the directory containing the checker. The program uses only the standard library. The proof does not require any external numerical certificate.

## Relationship to prior work
The ordered independent-edge model is the classical Condorcet random tournament model discussed by Saile and Suksompong (arXiv:1804.02743, first public 2018-04-08), whose full-text discussion concerns tournament choice sets and connectivity rather than a cyclic-triangle count CLT. Malinovsky and Rinott (arXiv:2206.08461, first public 2022-06-16) prove negative-association results for tournament score vectors, not the present moving-parameter cyclic-count limit. Malinovsky and Moon (arXiv:2104.01450, first public 2021-04-03) treat dependence inequalities and maximal scores. These models and established dependence tools are acknowledged.

Andersson's 1998 study addresses subgraph-count asymptotics in **fair** random tournaments; the fair case \(p=1/2\) here is therefore not presented as independently novel. The new claimed contribution is the **exact finite biased variance decomposition together with the Gaussian transition with the coefficient \(1/32+c^2/12\) at the varying-bias scale \(n^{-1/2}\)** and its matching off-window normalization. General orthogonal-decomposition and degenerate-statistics limit theorems are related background; applying a general theorem without calculating the degeneracy crossover would not supply the displayed explicit critical coefficient.

## Limitations
Only independent, identically biased orientations relative to a fixed total vertex order are covered. The Gaussian law is a weak limit, not a local limit theorem, moderate-deviation theorem, uniform Berry–Esseen estimate, or statement about joint counts of distinct motifs. For bias tending to \(0\) or \(1\), the off-window theorem does not apply as stated. Historical priority of the varying-bias crossover remains uncertain, especially relative to general U-statistic limit theory. The full 1998 fair-tournament article was not available for material comparison; its published abstract explicitly specifies independent fair orientations.

## References
1. C. Saile and W. Suksompong, *Robust Bounds on Choosing from Large Tournaments*, arXiv:1804.02743, first posted 2018-04-08. https://arxiv.org/abs/1804.02743
2. Y. Malinovsky and Y. Rinott, *On Tournaments and Negative Dependence*, arXiv:2206.08461, first posted 2022-06-16. https://arxiv.org/abs/2206.08461
3. Y. Malinovsky and J. W. Moon, *On negative dependence inequalities and maximal scores in round-robin tournaments*, arXiv:2104.01450, first posted 2021-04-03. https://arxiv.org/abs/2104.01450
4. P. Andersson, *On the asymptotic distributions of subgraph counts in a random tournament*, Random Structures & Algorithms 13 (1998), 249–260, DOI:10.1002/(SICI)1098-2418(199810/12)13:3/4<249::AID-RSA4>3.0.CO;2-V.
