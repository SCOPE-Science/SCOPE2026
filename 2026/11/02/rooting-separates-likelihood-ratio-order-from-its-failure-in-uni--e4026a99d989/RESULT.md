# Rooting separates likelihood-ratio order from its failure in uniform Cayley forests

## Finding
Fix \(n\ge2\). For each \(1\le k\le n\), choose a set \(R\) of \(k\) distinct vertices of the complete graph on \([n]\), specify \(r\in R\), and sample uniformly from the undirected spanning forests with precisely one root from \(R\) in each component. Let \(S_{n,k}\) be the number of vertices in the component of \(r\). Its law does not depend on the particular choice of \(R,r\).

**Rooted likelihood-ratio theorem.** For every \(1\le k<\ell\le n\),
\[
 S_{n,\ell}\le_{\mathrm{lr}}S_{n,k}.
\]
For \(2\le k\le n-2\), the adjacent likelihood ratio is strictly increasing over the common support \(1\le s\le n-k\), with
\[
 \frac{\Pr(S_{n,k}=s)}{\Pr(S_{n,k+1}=s)}
 =\frac{(k^2-1)(n-k)}{k^2 n}\,\frac{n-s}{n-k-s+1}.
\]
The two endpoint comparisons are strict by support containment. Thus for \(1\le k<\ell\le n\), every integer threshold \(2\le t\le n-k+1\) has
\[
 \Pr(S_{n,k}\ge t)>\Pr(S_{n,\ell}\ge t),
 \qquad W_1(S_{n,k},S_{n,\ell})=n\left(\frac1k-\frac1\ell\right).
\]
Here \(W_1\) is the ordinary cost-\(|a-b|\) Wasserstein distance between distributions on the integers. If the roots themselves are sampled uniformly and one independently marks a uniformly random vertex, its component-size law also decreases in likelihood-ratio order with \(k\).

**Sharp removal-of-roots boundary.** In contrast, sample uniformly from *unrooted* spanning forests with exactly \(k\) components, and let \(U_{n,k}\) be the size of the component containing a fixed vertex. For every integer \(n\ge5\), the expected likelihood-ratio order \(U_{n,3}\le_{\mathrm{lr}}U_{n,2}\) fails already between sizes one and two. Indeed, if \(u_k(s)=\Pr(U_{n,k}=s)\), then
\[
 \frac{u_2(1)/u_3(1)}{u_2(2)/u_3(2)}
 =1+\frac{(n-4)(5n-7)}{(n-2)^3(n+5)}>1.
\]
For \(n\le4\), every adjacent unrooted comparison satisfies the non-strict likelihood-ratio order. Thus five vertices are the first failure. This statement does not claim that first-order stochastic order fails in the unrooted model.

## Assumptions and scope
A spanning forest uses all labeled vertices, has no cycles, and has exactly \(k\) tree components. The fixed-root model gives equal weight to each forest whose \(k\) components each contain exactly one vertex of \(R\); orientation away from these roots is unique. It differs from the uniform distribution on *unrooted* \(k\)-component forests, which gives equal weight to each forest regardless of component sizes. The likelihood-ratio order \(X\le_{\mathrm{lr}}Y\) means \(\Pr(X=a)\Pr(Y=b)\ge\Pr(X=b)\Pr(Y=a)\) for all integers \(a<b\); disjoint or nested endpoint supports are allowed. The result is for all integers \(n\ge2\) and all admissible \(k,\ell\), with no asymptotic assumption.

For \(2\le k\le n-1\) and \(1\le s\le n-k+1\), define \(\tau(1)=1\) and \(\tau(s)=s^{s-2}\) for \(s\ge2\). The fixed-root point masses (a specialization of classical forest enumeration) are
\[
 p_{n,k}(s)=\frac{\binom{n-k}{s-1}\tau(s)(k-1)(n-s)^{n-s-k}}{k n^{n-k-1}}.
\]
At the upper endpoint \(s=n-k+1\), the exponent \(n-s-k=-1\) is interpreted literally, and the factor \((k-1)(n-s)^{-1}=1\). The boundary laws are \(S_{n,1}=n\) and \(S_{n,n}=1\) almost surely.

## Proof
**1. Fixed-root enumeration.** Cayley's tree count on \(s\) specified labeled vertices is \(\tau(s)\). Choose the other \(s-1\) nonroots in the marked-root component in \(\binom{n-k}{s-1}\) ways, choose its tree in \(\tau(s)\) ways, and choose a forest on the remaining \(n-s\) vertices with the other \(k-1\) specified roots. The fixed-root Cayley forest formula gives exactly \((k-1)(n-s)^{n-s-k}\) such remaining forests. Division by the total \(k n^{n-k-1}\) yields \(p_{n,k}(s)\). For \(k=1,n\) the laws are degenerate as stated.

**2. Likelihood-ratio ordering.** For \(2\le k\le n-2\) and \(1\le s\le n-k\), cancel the adjacent masses:
\[
 \frac{p_{n,k}(s)}{p_{n,k+1}(s)}
 =\frac{(k^2-1)(n-k)}{k^2 n}\,\frac{n-s}{n-k-s+1}.
\]
Because \(\frac{n-s}{n-k-s+1}=1+\frac{k-1}{n-k-s+1}\), this quotient is strictly increasing in \(s\). Moreover \(p_{n,k}\) has the additional positive endpoint \(s=n-k+1\) absent from \(p_{n,k+1}\). This proves the cross-product inequality for all support pairs. Cases \(k=1\) and \(k=n-1\) follow directly from the degenerate endpoint laws. Composition of likelihood-ratio inequalities gives every pair \(k<\ell\).

Strict first-order stochastic domination at every nonconstant threshold follows from the strict adjacent cross-product inequality (or the additional endpoint), then by transitivity. Symmetry over the \(k\) roots and \(n-k\) nonroots gives \(\mathbb E S_{n,k}=n/k\): each nonroot belongs to the marked component with probability \(1/k\), and there is one marked root. On the line, \(W_1\) between stochastically ordered integrable laws equals the difference of their means. This establishes the distance formula.

When \(R\) is chosen uniformly and a uniformly random vertex is marked, the probability of its being in a component of size \(s\) is the size bias of a uniformly chosen root's component size:
\[
 q_{n,k}(s)=\frac{k s}{n}p_{n,k}(s).
\]
Since \(\sum_s s p_{n,k}(s)=n/k\), this is normalized. Its adjacent ratios are \(q_{n,k}(s)/q_{n,k+1}(s)=\frac{k}{k+1}\,p_{n,k}(s)/p_{n,k+1}(s)\), so the likelihood-ratio order survives.

**3. Unrooted obstruction for every \(n\ge5\).** Let \(F(n,k)\) denote the number of unrooted forests of \(k\) trees on \([n]\). Conditioning on the component of vertex one gives
\[
 u_k(s)=\frac{\binom{n-1}{s-1}\tau(s)F(n-s,k-1)}{F(n,k)},
 \qquad F(n,1)=n^{n-2}.
\]
The classical exact two-component count is
\[
 F(m,2)=\frac{(m-1)(m+6)m^{m-4}}2\qquad(m\ge2).
\]
For completeness, write \(T(z)=\sum_{m\ge1}m^{m-2}z^m/m!\) and let \(R=ze^R\). Then \(T=R-R^2/2\), and by the labeled exponential formula followed by Lagrange inversion,
\[
 F(m,2)=\frac{m!}{2}[z^m]T(z)^2
 =\frac{(m-1)!}{2}[v^{m-1}](2v-3v^2+v^3)e^{mv},
\]
which simplifies to the displayed count for \(m\ge4\); the cases \(m=2,3\) follow from the definition by direct enumeration. Consequently, for \(n\ge5\),
\[
 \frac{u_2(1)/u_3(1)}{u_2(2)/u_3(2)}
 =\frac{F(n-1,1)F(n-2,2)}{F(n-1,2)F(n-2,1)}
 =\frac{(n-1)^2(n-3)(n+4)}{(n-2)^3(n+5)}
 =1+\frac{(n-4)(5n-7)}{(n-2)^3(n+5)}>1.
\]
An increasing \(u_2(s)/u_3(s)\) is necessary for \(U_{n,3}\le_{\mathrm{lr}}U_{n,2}\), so this reverses the order. For \(n=4\), the same expression is exactly one on the only nontrivial common adjacent support; all other pairs at \(n\le4\) involve a point mass or single common support value. Thus \(n=5\) is the sharp first failure.

## Verification
The standalone Python 3 file `verify.py` uses exact rational arithmetic throughout. It checks normalization, means, the rooted and random-vertex likelihood-ratio cross-products, strict stochastic-tail comparisons, and Wasserstein mean differences for \(2\le n\le50\). It also directly enumerates valid parent functions for every fixed-root model through seven vertices, independently enumerates all acyclic edge subsets in unrooted forests through six vertices, and compares these to the forest-count recurrence. It identifies \((n,k)=(5,2)\) as the first unrooted violation and verifies the infinite-family formula against exact counts over finite test ranges. These experiments check implementation and boundaries; the preceding arguments prove the statements for all admissible integers.

## Relationship to prior work
Pitman's *Coalescent Random Forests* (1996 preprint; published 1999) gives the classical forest counts and a coalescent coupling implying weaker stochastic monotonicity for unrestricted randomly rooted forests. Pitman's 2001 *Random mappings, forests, and subsets associated with Abel-Cayley-Hurwitz multinomial expansions*, especially Proposition 15, already contains a general component-subset distribution encompassing the fixed-root mass formula above. Neither the enumeration, the conditional component distribution nor the expectation \(n/k\) is claimed new. The comparisons established here are the all-parameter strict likelihood-ratio comparison, its invariant size-biased version, and the every-order, sharp unrooted obstruction. Sokal's total-positivity results concern matrices of forest enumerators indexed by order and component count, not the distribution of the component of a tagged root. The unrooted two-component count is classical; the cross-model inequality is distinct from that count.

## Limitations
The complete conditional distribution in the rooted case was previously known, so the order theorem is a new comparison *derived from*, not independent of, classical formulas; historical priority for this particular comparison is not fully established. No general dominance classification for all unrooted \(k\) is asserted, and failure of likelihood-ratio ordering must not be mistaken for failure of stochastic ordering. The result is specific to complete graphs with equal forest weights and to the stated root-selection conventions.

## References
- J. Pitman, *Coalescent Random Forests*, University of California Berkeley Technical Report 457 (1996); later *Journal of Combinatorial Theory A* 85 (1999), 165–193. https://statistics.berkeley.edu/tech-reports/457
- J. Pitman, *Random mappings, forests, and subsets associated with Abel-Cayley-Hurwitz multinomial expansions*, *Séminaire Lotharingien de Combinatoire* 46 (2001), B46h, Proposition 15. https://www.mat.univie.ac.at/~slc/wpapers/s46pitman.pdf
- A. D. Sokal, *Total positivity of some polynomial matrices that enumerate labeled trees and forests I*, arXiv:2105.05583 (2021). https://arxiv.org/abs/2105.05583
- T. Łuczak and B. Pittel, *Components of random forests*, *Combinatorics, Probability and Computing* 1 (1992), 35–52. https://doi.org/10.1017/S0963548300000067
