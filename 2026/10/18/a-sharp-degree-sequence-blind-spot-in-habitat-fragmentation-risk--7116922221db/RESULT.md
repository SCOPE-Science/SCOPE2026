# A sharp degree-sequence blind spot in habitat-fragmentation risk on trees

## Finding

In a tree-shaped habitat network, remove habitat patches either by retaining exactly \(k\) uniformly selected vertices or by retaining each vertex independently with probability \(p\). Let \(C\) be the number of connected components induced by the surviving patches (\(C=0\) for the empty set). The following three statements hold.

1. **Moment universality and extremizers.** The mean of \(C\) depends only on population of patches \(n\), and its variance depends on the network only through the degree statistic \(W(T)=\sum_{v\in V(T)}\binom{\deg_T(v)}{2}\). For each \(n\ge4\), every \(3\le k\le n-1\), and every \(0<p<1\), the \(n\)-vertex path is the unique minimum-variance tree and the \(n\)-vertex star the unique maximum-variance tree, up to isomorphism. The exact maximum-minus-minimum variances are
   \[
   (n-2)(n-3)(a_3-a_4)\quad\text{and}\quad(n-2)(n-3)p^3(1-p),
   \]
   respectively, where \(a_r=(k)_r/(n)_r\) for \(0\le r\le4\), with \(a_r=0\) when \(k<r\).

2. **First distributional escape from degree information.** Every two trees on at most five vertices with the same degree multiset are isomorphic. On six vertices, exactly one pair of nonisomorphic trees has the same degree multiset, \((1,1,1,2,2,3)\). Label the vertices \(0,1,2,3,4,5\). Write \(A\) for edges \(\{01,03,04,12,25\}\) and \(B\) for edges \(\{01,02,03,14,25\}\). Under uniform selection of four vertices, the laws are
   \[
   \begin{array}{c|rrrr}
    c&1&2&3&4\\\hline
    15\Pr(C_A=c)&4&8&2&1\\
    15\Pr(C_B=c)&5&5&5&0
   \end{array}
   \]
   Their common mean is \(2\) and variance is \(2/3\), but their **third central moments** are \(2/5\) and \(0\), respectively.

3. **An exact all-probabilities skewness separation.** For the same two trees, under independent retention, their first and second moments agree for every \(0\le p\le1\), while their third central moments differ by
   \[
   \mathbb E[(C_A-\mathbb E C_A)^3]-\mathbb E[(C_B-\mathbb E C_B)^3]
   =6p^4(1-p)^2.
   \]
   The difference is strictly positive for every \(0<p<1\). This is the smallest number of habitat patches for which equal-degree tree networks can have different fragment-count third central moments.

## Assumptions and scope

\(T=(V,E)\) is any finite simple undirected **tree** with \(n=|V|\) vertices; loops, cycles, extra habitat connections, and heterogeneous survival probabilities are excluded. A connected component means a component of the **vertex-induced subgraph** on surviving vertices, not the number of retained edges or a bond-percolation cluster count. The empty survivor set has zero components. Uniform \(k\)-retention assigns probability \(1/\binom nk\) to each set of size \(k\), for every integer \(0\le k\le n\). Independent retention is Bernoulli with the same probability \(p\) for each vertex, independently. Degree sequences are multisets (sorted degrees), not vertex-labelled lists. Uniqueness of extremizers is always up to graph isomorphism.

For uniform \(k\)-retention and \(n\ge4\), define \(a_r=(k)_r/(n)_r\) for \(r\in\{2,3,4\}\), where \((t)_r=t(t-1)\cdots(t-r+1)\) and \(a_r=0\) if \(k<r\). Explicitly,
\[
\mathbb E C=k-\frac{k(k-1)}n,
\]
\[
\operatorname{Var}(C)=(n-1)a_2+2W(T)a_3
 +2\left(\binom{n-1}{2}-W(T)\right)a_4-(n-1)^2a_2^2.
\]
For \(k=0,1,2,n\), this variance is independent of the tree; at \(k=2\), in particular, any selected pair is adjacent with the same probability \(2/n\). The positive path–star separation is asserted only for \(3\le k\le n-1\) and \(n\ge4\).

For independent retention and arbitrary \(n\ge1\),
\[
\mathbb E C=np-(n-1)p^2,
\]
\[
\operatorname{Var}(C)=np(1-p)+(n-1)p^2(1-p^2)
 -4(n-1)p^2(1-p)+2W(T)p^3(1-p).
\]
No statement is made that two trees having the same degree sequence must have the same complete fragment-count distribution; the six-vertex witness disproves that assertion.

## Proof

**1. Forest identity and first moments.** For every retained vertex set \(S\subseteq V\), the induced subgraph \(T[S]\) is a forest. Hence
\[
C(S)=|S|-|\{uv\in E:u,v\in S\}|.
\]
In fixed-size sampling, write \(I_e=\mathbf1_{\{e\subseteq S\}}\) and \(X=\sum_{e\in E}I_e\). Since \(C=k-X\), its variance equals that of \(X\). Every fixed set of \(r\) distinct vertices survives jointly with probability \(a_r\). Therefore \(\mathbb E X=(n-1)a_2\). There are \(W(T)\) unordered pairs of incident distinct edges (three distinct endpoints) and \(\binom{n-1}2-W(T)\) unordered pairs of disjoint edges (four endpoints). Expanding \(X^2\) gives the exact displayed fixed-size variance formula, with no independence assumption between the edge indicators.

For Bernoulli survival write \(Y_v=\mathbf1_{\{v\text{ survives}\}}\). Then \(C=\sum_vY_v-\sum_{uv\in E}Y_uY_v\). The vertex sum has variance \(np(1-p)\), and the edge sum has variance \((n-1)p^2(1-p^2)+2W(T)p^3(1-p)\); disjoint edge indicators are independent. Each edge contributes two equal vertex-edge covariances \(p^2(1-p)\), so the covariance between the two sums is \(2(n-1)p^2(1-p)\). The Bernoulli formulas follow by expansion.

**2. Sharp extremizers and strictness.** Put \(b_v=\deg_T(v)-1\ge0\). By the handshake lemma \(\sum_vb_v=n-2\), and
\[
W(T)=\sum_v\binom{b_v+1}{2}=(n-2)+\sum_v\binom{b_v}{2}.
\]
The minimum is \(n-2\), achieved exactly when \(b_v\le1\) at every vertex, equivalently when the tree is a path. For the maximum, \(\sum_v\binom{b_v}{2}\le\binom{n-2}{2}\), since it counts pairs in the disjoint groups of \(b_v\) objects, and equality holds exactly when all \(n-2\) objects occupy one group. This is exactly the star, with \(W=(n-1)(n-2)/2\). Thus the difference in \(W\) is \((n-2)(n-3)/2\). The coefficient of \(W\) in the fixed-size variance is \(2(a_3-a_4)\), positive for \(3\le k\le n-1\) because \(a_4=a_3(k-3)/(n-3)<a_3\). In the Bernoulli variance the coefficient is \(2p^3(1-p)>0\) for \(0<p<1\). Multiplication yields both sharp gaps and the asserted uniqueness.

**3. Minimal degree twins.** The degree-sum and positivity restrictions enumerate all degree multisets of trees on at most six vertices. Through five vertices the possible multisets each admit a unique tree. At six vertices the six nonisomorphic tree types are: one path, one star, one tree of degree multiset \((1,1,1,1,2,4)\), one double-star with multiset \((1,1,1,1,3,3)\), and the two arrangements of \((1,1,1,2,2,3)\). In the latter, the degree-three vertex has pendant arm lengths \((3,1,1)\) or \((2,2,1)\), respectively; these are \(A\) and \(B\) above. Prüfer-sequence enumeration followed by canonical-tree isomorphism reduction independently verifies this complete six-type count (see verification program).

For \(k\le3\) the component-count distribution for any tree is determined by \(n\) and \(W(T)\): on a three-vertex set, exactly two retained edges occur precisely for a length-two path, counted by \(W(T)\); the number with one retained edge follows from the expected edge count, and the remaining count follows by subtraction. For \(k=2\) only adjacency matters. For \(k=n-1\), deleting a single vertex leaves a number of components equal to its original degree (and choosing the deleted vertex uniformly samples the degree multiset). Consequently, all conditional fragment-count distributions of degree-twin six-vertex trees agree except possibly at \(k=4\). Direct enumeration of the \(\binom64=15\) retained quadruples in the two explicit edge lists gives the distribution table. Both means equal \(2\) and both variances equal \(2/3\). Their centered cubic moments are \((-4+2+8)/15=2/5\) and \((-5+5)/15=0\).

**4. Bernoulli third-moment identity.** In six-vertex Bernoulli retention, a particular \(k\)-set has probability \(p^k(1-p)^{6-k}\). The two trees have identical conditional first and second raw moments at each \(k\), so their unconditional first and second moments agree and their third *central* moment difference equals the raw third moment difference. For \(k\ne4\) the conditional distributions coincide. For \(k=4\), the difference of unnormalized third raw moments over all 15 subsets is
\[
4\cdot1^3+8\cdot2^3+2\cdot3^3+1\cdot4^3
 -\bigl(5\cdot1^3+5\cdot2^3+5\cdot3^3\bigr)=6.
\]
Multiplying by \(p^4(1-p)^2\) proves the exact all-\(p\) identity. Since no degree twins exist at lower orders, six is the sharp onset of this degree-sequence blindness.

## Verification

The standalone file `verify_fragmentation.py` uses only the Python standard library and exact rational arithmetic. It exhausts Prüfer codes for each \(1\le n\le6\), canonically deduplicates unrooted tree isomorphism types, enumerates every retained subset, computes components via **two independent routes** (retained-edge count and disjoint-set union), and verifies the fixed-size mean and variance identities. It finds respectively \(1,1,1,2,3,6\) tree types, exactly one degree-twin pair on six vertices, and distinct conditional distributions only at \(k=4\). It verifies moment differences of orders one, two, and three. It separately sums the Bernoulli subset probabilities at three exact rational \(p\) values for every tree up to six vertices and checks both Bernoulli moment identities; it also verifies the path-star variance gap at each \(0\le k\le n\) for \(4\le n\le9\). All tests reported `ALL_CHECKS_PASSED`.

The unrestricted \(n\)-vertex extremal conclusions and all-\(p\) six-vertex identity follow from the preceding symbolic proofs; the finite checks are not extrapolated to establish them. The finite enumeration is used only to corroborate the complete degree-twin classification at orders at most six.

## Relationship to prior work

Tittmann, Averbouch, and Makowsky introduced the general induced-subgraph component polynomial \(Q(G;x,y)\). It already **encodes the entire fragment-count distribution** for fixed-size and independent vertex retention on *any* finite graph. Therefore neither that encoding nor the forest identity or the ability to calculate the six-vertex distributions from \(Q\) is claimed as new. Their Proposition 2 establishes that full \(Q\) distinguishes nonisomorphic trees through nine vertices, a different comparison from degree-sequence or low-moment indistinguishability. The present finding specializes to habitat trees and establishes explicit universal first- and second-moment laws, exact sharp path/star variance gaps, and the first degree-twin split at the *third* central moment with a positive formula for every intermediate survival probability.

Hackl, Panholzer, and Wagner derive uncover-process laws for **uniform random labelled trees**; the present extremal result concerns every fixed tree of a given order. Janson studies the visible-edge/forest-component process for large **sequences** of deterministic or random trees, giving limiting Gaussian-process covariance formulas under degree assumptions (Theorem 8.1). This strongly anticipates dependence on degree moments but is not an all-finite-order variance extremal theorem nor a six-vertex third-moment classification. Urban and colleagues supply the ecological framework in which patches and dispersal links form a habitat graph, rather than an exact random-failure moment theorem.

## Limitations

The two protocols select patches **uniformly** or independently with **homogeneous** survival probability. This is a mathematical model of habitat fragmentation, not a calibrated conservation prediction. Heterogeneous risk, correlated failures, cycles, patch weights, restoration decisions, and fragment-size distributions are outside the claim. The precise six-vertex witness quantifies a difference in third *central moments*, not a complete ordering of ecological harm, and the extremal variance theorem does not assert convex stochastic order. The generic component-count polynomial of Tittmann et al. provides stronger distributional computability, and independent literature review remains necessary to rule out equivalent previously published moment-extremal or skewness results.

## References

- P. Tittmann, I. Averbouch, J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147, first posted 22 December 2008; *European Journal of Combinatorics* 32 (2011), 954–974, doi:10.1016/j.ejc.2011.03.017.
- D. L. Urban, E. S. Minor, E. A. Treml, R. S. Schick, *Graph models of habitat mosaics*, *Ecology Letters* 12 (2009), 260–273, doi:10.1111/j.1461-0248.2008.01271.x.
- B. Hackl, A. Panholzer, S. Wagner, *The Uncover Process for Random Labeled Trees*, *La Matematica* 2 (2023), 861–892, doi:10.1007/s44007-023-00060-3.
- S. Janson, *Uncovering a graph*, *Probability Theory and Related Fields* 195 (2026), 689–740, first published 1 September 2025, doi:10.1007/s00440-025-01401-9.
