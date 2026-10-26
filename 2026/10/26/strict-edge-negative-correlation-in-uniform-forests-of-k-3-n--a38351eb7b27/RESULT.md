# Strict edge-negative correlation in uniform forests of \(K_{3,n}\)

## Finding
Let \(n\ge3\) be an integer, and choose uniformly among **all** acyclic spanning edge subsets (including disconnected forests and isolated vertices) of the complete bipartite graph \(K_{3,n}\). For a host edge \(e\), let \(I_e\) indicate its inclusion. Put
\[
V_n=3n^2+13n+16,\qquad U_n=3n^2+23n+38.
\]
For every host edge, \(\Pr(I_e=1)=U_n/(4V_n)\). For any two **distinct** host edges \(e,f\), the covariance is strictly negative, with the following exact three-orbit classification:
\[
\operatorname{Cov}(I_e,I_f)=
\begin{cases}
-\dfrac{(n-1)(9n^3+51n^2+104n+92)}{16V_n^2},& \text{a common vertex in the size-}\!n\text{ part},\\[4pt]
-\dfrac{41n^2+181n+194}{8V_n^2},& \text{a common vertex in the size-}\!3\text{ part},\\[4pt]
-\dfrac{17n^2+77n+66}{8V_n^2},& \text{vertex-disjoint edges}.
\end{cases}
\]
In particular, the first covariance tends to \(-1/16\); the other two are asymptotic to \(-41/(72n^2)\) and \(-17/(72n^2)\), respectively. This supplies an all-size strict pairwise edge-negative-correlation theorem for a three-connected family outside the series-parallel class.

## Assumptions and scope
The vertex sets of \(K_{3,n}\) are \(\{a,b,c\}\) and \(\{1,\ldots,n\}\). Forests are labeled, chosen equiprobably without conditioning on their number of components or edges. No edge fugacity or individual edge weights are varied. Every unordered pair of distinct edges falls into exactly one of the three types above. The assertion concerns pairwise covariance, not full negative association or the positive-weight I-Rayleigh property.

## Proof
**1. Exhaustive structural decomposition.** A leaf-side vertex is called *high* when it has two or three chosen neighbors among \(a,b,c\). The other vertices have degree zero or one and independently admit four choices: no neighbor or one of the three hubs. Acyclicity is equivalent to exactly one of these mutually exclusive configurations among the high vertices:

* no high vertices;
* exactly one high vertex, whose neighbor set is one of three pairs or the full triple;
* exactly two high vertices, with distinct two-hub neighbor sets.

To prove necessity, two identical pair-neighbor sets create a four-cycle, all three different pair-neighbor sets together create a six-cycle, and any further high vertex alongside a triple-neighbor set creates a cycle. Conversely, in the three listed configurations the compression of high vertices onto the three hubs is a forest, and attaching any number of degree-one leaf-side vertices cannot create a cycle. This proves sufficiency and exhaustiveness.

The number of eligible spanning forests is therefore
\[
Z_n=4^n+4n4^{n-1}+6\binom n2 4^{n-2}=4^{n-2}V_n.
\]
This unweighted forest-count formula was already known; it is included here as a normalization identity, not claimed as a new result.

**2. One-edge incidence.** Fix an edge \(e\) joining one hub to one leaf-side vertex. Partition its containing forests by the structural cases: (a) no high vertex, (b) one high vertex which is the marked leaf, (c) one high vertex different from the marked leaf, (d) two high vertices including the marked leaf, or (e) two high vertices distinct from it. These respectively contribute
\[
4^{n-1},\quad 3\cdot4^{n-1},\quad
4(n-1)4^{n-2},\quad4(n-1)4^{n-2},\quad
6\binom{n-1}{2}4^{n-3}.
\]
The term with a high marked leaf of degree two has two admissible neighbor pairs; degree three has one. Hence the single-edge containing count is
\[
A_n=4^n+8(n-1)4^{n-2}+6\binom{n-1}{2}4^{n-3}=4^{n-3}U_n.
\]
Dividing by \(Z_n\) gives the asserted marginal probability.

**3. Pair incidence.** If two fixed edges have the same leaf-side endpoint, that vertex must be high. It either has exactly the specified two neighbors, has all three, or has those two plus a distinct two-hub neighbor set at one other high vertex. The count is
\[
B_{0,n}=2\cdot4^{n-1}+2(n-1)4^{n-2}=4^{n-2}(2n+6).
\]
For edges with **different** leaf-side endpoints, first force their two incidences. Define
\[
W_0=4^{n-2}+4(n-2)4^{n-3}+6\binom{n-2}{2}4^{n-4},
\qquad
W_1=4^{n-2}+2(n-2)4^{n-3}.
\]
When neither marked leaf is high, there are \(W_0\) completions; when exactly one is a degree-two high vertex and the other has degree one, there are \(4W_1\); when exactly one is degree three and the other degree one, there are \(2\cdot4^{n-2}\). If both marked leaves have degree two, distinct neighbor pairs are required: there are \(2\) choices when the forced edges share a hub, and \(3\) choices when their hubs differ. Therefore
\[
B_{1,n}=W_0+4W_1+4\cdot4^{n-2}
=4^{n-4}(3n^2+33n+66),
\]
\[
B_{2,n}=W_0+4W_1+5\cdot4^{n-2}
=4^{n-4}(3n^2+33n+82).
\]
These formulas can be checked directly at \(n=3\) and are derived from disjoint exhaustive cases, not from numerical interpolation.

**4. Exact covariance and signs.** Since a pair probability equals \(B_{j,n}/Z_n\) and the squared marginal equals \(A_n^2/Z_n^2\), the three joint probabilities are
\[
\frac{2n+6}{V_n},\qquad
\frac{3n^2+33n+66}{16V_n},\qquad
\frac{3n^2+33n+82}{16V_n}.
\]
Straight polynomial multiplication yields the identities
\[
U_n^2-16(2n+6)V_n
=(n-1)(9n^3+51n^2+104n+92),
\]
\[
U_n^2-(3n^2+33n+66)V_n=2(41n^2+181n+194),
\]
\[
U_n^2-(3n^2+33n+82)V_n=2(17n^2+77n+66).
\]
Substitution gives the three displayed covariance formulas. Each numerator factor is positive for every integer \(n\ge3\), while \(V_n>0\); thus every covariance is **strictly** negative. Comparing leading coefficients establishes the three stated asymptotics. \(\square\)

## Verification
The standalone `verify.py` program independently enumerates all \(2^{3n}\) edge subsets of \(K_{3,n}\) for \(1\le n\le6\), deciding acyclicity by union-find and comparing every one-edge and every unordered two-edge incidence with the exact formulas using `fractions.Fraction`. It additionally checks the polynomial factorization identities coefficientwise, and verifies the resulting strict signs for \(1\le n\le1000\) wherever admissible. The extracted program passed **4,825 exact assertions**. The argument for all \(n\ge3\) is the combinatorial decomposition and polynomial identities above, not the finite checks.

## Relationship to prior work
Huang's November 2023 paper on negative correlation of arboreal gas motivates the open pairwise edge-correlation question. At edge fugacity one, that model equals the uniform measure on unrooted forests here. Huang proves large-fugacity adjacent-edge results and results on complete graphs under parameter restrictions, not the exact uniform-forest three-orbit classification for \(K_{3,n}\). Erickson proves I-Rayleigh for series-parallel graphs; \(K_{3,n}\), for \(n\ge3\), contains a \(K_4\) minor and is not in that class. Stark treats uniform bipartite forests but its adjacent-edge negative-correlation asymptotics require **both** part sizes to diverge, and the paper explicitly leaves the nonadjacent-edge comparison open in that regime. Fixing the smaller side at three is outside its hypotheses. Speyer's 2019 counting argument already gives the exact \(Z_n\) normalization above, but it does not address joint edge incidences, their sign, or sharp pair types. Grimmett and Winkler's finite-graph computations cover some small instances, not every \(n\). These comparisons identify the scope of the contribution; they cannot certify absolute historical priority.

## Limitations
The theorem proves strict pairwise edge-negative correlation only for unweighted forests of the stated complete-bipartite family. It does not establish full negative association, arbitrary edge weights, all edge fugacities, or the general graph conjecture. Existing unpublished or differently formulated conclusions may affect historical priority. Finite enumeration is merely corroboration; no independent audit has been performed.

## References
1. X. Huang, *On Negative Correlation of Arboreal Gas on Some Graphs*, arXiv:2311.00965v1, first posted 2023-11-02. https://arxiv.org/html/2311.00965v1
2. A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, arXiv:1008.3660v3. https://arxiv.org/html/1008.3660v3
3. D. Stark, *The asymptotic number of spanning forests of complete bipartite labelled graphs*, Discrete Mathematics 313 (2013), 697–708. https://doi.org/10.1016/j.disc.2012.10.026
4. D. E. Speyer, answer to *Spanning forests of bipartite graphs and distinct row/column sums of binary matrices*, Mathematics Stack Exchange, June 2, 2019. https://math.stackexchange.com/questions/3235160/3248773
5. G. Grimmett and P. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185. https://arxiv.org/abs/math/0302185
