# A four-period obstruction for limited domination on Möbius ladders

## Finding
For each integer \(n\ge3\), let \(M_{2n}\) be the graph with vertex set \(\mathbb Z/(2n)\mathbb Z\) and an edge from each vertex \(i\) to \(i-1\), \(i+1\), and \(i+n\), with subscripts understood modulo \(2n\). Every vertex has degree three.

A set \(D\subseteq V(G)\) is *1-limited dominating* if every vertex outside \(D\) has a neighbor in \(D\), and every vertex in \(D\) has at most one neighbor outside \(D\). Write \(\gamma_1^{\mathrm L}(G)\) for its minimum cardinality.

**Theorem.** For all integers \(n\ge3\),
\[
\gamma_1^{\mathrm L}(M_{2n})=\begin{cases}n,&4\mid n,\\ n+1,&4\nmid n.\end{cases}
\]
If \(4\mid n\), the graph has **exactly four** minimum 1-limited dominating vertex sets: the two complementary choices for each of the two cyclic phases of the repeating binary pattern \(0011\). Equivalently, it has exactly **two** perfect matching cuts, both formed entirely by alternating perimeter edges.

## Assumptions and scope
Graphs are finite, simple, undirected, and have no loops. The Möbius ladder convention here uses \(2n\) vertices and requires \(n\ge3\), avoiding coincident edges. "Perfect matching cut" means an edge cut whose crossing edges meet every vertex exactly once; two complementary vertex sides define the same unordered cut. The lower bound and constructive upper bound concern 1-limited dominating sets, not ordinary domination, efficient domination, or edge-open packing.

## Proof
**1. Degree counting.** Let \(D\) be a 1-limited dominating set and put \(U=V\setminus D\). Every vertex of \(U\) has a neighbor in \(D\), so \(|E(D,U)|\ge|U|\). Every vertex of \(D\) has at most one neighbor in \(U\), so \(|E(D,U)|\le|D|\). Because \(|D|+|U|=2n\), necessarily \(|D|\ge n\).

If equality holds, then \(|D|=|U|=n\), and both inequalities must be equalities. Thus *each* vertex, whether in \(D\) or \(U\), has exactly one neighbor across the cut. Conversely, a vertex bipartition having exactly one crossing edge per vertex gives a 1-limited dominating set of size \(n\) on either side. We classify all such bipartitions.

**2. Crossing indicators.** Assign binary colors \(c_i\in\{0,1\}\) according as \(i\notin D\) or \(i\in D\). Define integers (not values in a field)
\[
a_i=c_i\oplus c_{i+1},\qquad b_i=c_i\oplus c_{i+n}\quad (i\bmod 2n),
\]
where \(\oplus\) is binary exclusive-or. At vertex \(i\), exactly one edge crosses if and only if
\[
 a_{i-1}+a_i+b_i=1.\tag{1}
\]
The antipodal edge implies \(b_{i+n}=b_i\). Subtract equation (1) for vertices \(i\) and \(i+n\). Setting \(d_i=a_{i+n}-a_i\in\{-1,0,1\}\), we obtain
\[
 d_{i-1}+d_i=0,\qquad d_i=(-1)^i d_0,\qquad d_{i+n}=-d_i.\tag{2}
\]
Also, because the chord goes across \(n\) perimeter edges,
\[
 b_i=\left(\sum_{j=i}^{i+n-1}a_j\right)\bmod 2.\tag{3}
\]

**3. Even \(n\).** When \(n\) is even, equation (2) gives \(d_i=0\) for every \(i\), so the perimeter crossing sequence has period \(n\). Equation (3) then shows that all \(b_i\) have the same value \(b\), equal to the parity of the \(n\)-term sum of \(a\). If \(b=1\), equation (1) forces every \(a_i=0\), contradicting equation (3). Hence \(b=0\), and equation (1) becomes \(a_{i-1}+a_i=1\), which forces the binary sequence \(a\) to alternate \(0,1,0,1,\ldots\). Its \(n\)-term sum has parity \((n/2)\bmod2\). Since \(b=0\), \(n/2\) must be even, or \(4\mid n\).

Conversely, when \(4\mid n\), choose either alternating sequence for \(a\). The total parity around the \(2n\)-cycle is even, so it determines a consistent sequence \(c_i\) uniquely after choosing \(c_0\). The opposite vertices have the same color because any \(n\) consecutive increments include \(n/2\) ones, an even number; thus every chord is monochromatic. At every vertex exactly one of the two perimeter edges crosses, so equation (1) holds. Two choices of alternating phase times two choices for \(c_0\) produce four binary colorings, hence four labeled minimum sets; complementary colors produce the same cut and there are two cuts. The necessity argument shows that no further minimum sets exist.

**4. Odd \(n\).** From equation (2), either \(d_0=0\), or \(d_0=1\), or \(d_0=-1\). If \(d_0=0\), then \(a\) has period \(n\), equation (3) gives constant \(b\), and, as in the even case, \(b=1\) is impossible. With \(b=0\), equation (1) forces alternation, impossible for a binary sequence with odd period \(n\).

If \(d_0=1\), the equality \(a_{i+n}-a_i=(-1)^i\), together with \(a_i\in\{0,1\}\), implies \(a_i=0\) for even \(i\) and \(a_i=1\) for odd \(i\). If \(d_0=-1\), the opposite alternating phase follows. In either case equation (1) forces \(b_i=0\) for every \(i\). But for odd \(n\), the parities of the \(n\)-term sums of an alternating binary sequence beginning at an even or an odd index are different. Equation (3) therefore gives \(b_i=1\) for at least one vertex, a contradiction. Thus no bipartition with exactly one crossing neighbor per vertex exists for odd \(n\).

Taken together, steps 3 and 4 show that a 1-limited dominating set of size \(n\) exists *exactly* when \(4\mid n\).

**5. A matching upper bound otherwise.** For every \(n\ge3\), choose the consecutive arc
\[
D=\{0,1,\ldots,n\}.
\]
Both endpoint vertices \(0,n\) have one outside neighbor along the perimeter and an inside antipodal neighbor. Each internal vertex \(1,\ldots,n-1\) has its two perimeter neighbors inside \(D\) and its antipode outside \(D\), so every vertex of \(D\) has exactly one neighbor outside. Every outside vertex \(n+1,\ldots,2n-1\) has its antipode among \(1,\ldots,n-1\) inside \(D\), hence is dominated. Therefore \(D\) is 1-limited dominating with \(n+1\) vertices. Combining this construction with the proved lower bound and equality classification gives the claimed formula and rigidity. \(\square\)

## Verification
The supplied `verify_mobius.py` has two logically distinct finite implementations of the definition: (i) exhaustive enumeration of every vertex subset, and (ii) exact min-plus dynamic programming on a two-row strip with a twisted boundary that represents the antipodal chords. The implementations agree for all \(3\le n\le8\), and the dynamic program agrees with the formula for all \(3\le n\le200\), including the prediction of exactly four minima when \(4\mid n\). Reproducing `verification_output.txt` from `verify_mobius.py` requires Python 3 only. These finite checks are corroboration, not a proof for arbitrary \(n\): the infinite claim follows from steps 1–5.

## Relationship to prior work
The 1-limited domination invariant and its general graph bounds were developed by Božović and collaborators in 2026 (arXiv:2606.22422), and Tepeh studied Cartesian products and complexity (arXiv:2606.22428). Radić and Tepeh (arXiv:2610.01796, initially public 2026-10-01) investigate 1-limited and \((1,2)\)-domination in cubic graphs, including Goldberg-family results. Those works motivate the cubic setting but the inspected statements do not determine the full Möbius-ladder parameter or the equality-coloring count. Fakharan et al. (2021) already state the \(M_6=K_{3,3}\) minimum value of four in the language of \((1,2)\)-domination: that instance is **prior work, not a newly claimed special case**. General half-order bounds also precede this note. The novelty assessment concerns the *uniform four-period classification, sharp minimum for all orders, and exactly two equality cuts*.

Perfect matching-cut theory is directly relevant because equality translates into a perfect matching cut. The known efficient-domination classification of cubic vertex-transitive graphs instead imposes disjoint closed neighborhoods, which is a different constraint and has a different congruence for Möbius ladders. Searches for matching-cut formulations and cyclic-graph variants identified no precise covering statement, but mathematical priority is not conclusively established by nonappearance in searches.

## Limitations
No claim is made about counting the minimum sets when \(4\nmid n\), about arbitrary cubic graphs, or about independence from all unindexed research. This is a mathematical proof checked within the same research process; **independent mathematical audit has not been performed**. A previously known perfect matching-cut classification of this family, if found, could limit the originality of the equality characterization. The theorem itself is explicit for all \(n\ge3\), but neither the finite verification nor bibliographic searches certify an independently established result.

## References
1. E. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796v1 (2026), https://arxiv.org/html/2610.01796v1 .
2. *On k-limited domination in graphs*, arXiv:2606.22422v1 (2026), https://arxiv.org/abs/2606.22422 .
3. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428v1 (2026), https://arxiv.org/abs/2606.22428 .
4. S. Fakharan et al., *On (1,2)-domination in cubic graphs*, Discrete Mathematics 344 (2021), article 112546, https://www.researchgate.net/publication/353283962_On_12-domination_in_cubic_graphs .
5. *Efficient domination in cubic vertex-transitive graphs* (2012), European Journal of Combinatorics, https://doi.org/10.1016/j.ejc.2012.04.007 .
6. Bouquet and Picouleau, *The complexity of the perfect matching-cut problem*, Journal of Graph Theory (2025), https://onlinelibrary.wiley.com/doi/full/10.1002/jgt.23167 .
