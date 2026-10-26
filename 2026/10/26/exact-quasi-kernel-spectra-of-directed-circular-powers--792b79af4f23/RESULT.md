# Exact quasi-kernel spectra of directed circular powers

## Finding
Let \(n\ge3\) and \(1\le k<n\). Let \(D_{n,k}\) have vertex set \(\mathbb Z/n\mathbb Z\) and arcs \(i\to i+d\) for every \(1\le d\le k\), modulo \(n\). A quasi-kernel is an independent set \(Q\) from which every vertex is reachable along at most two directed arcs. Write \(a_{n,k}(s)\) for the number of quasi-kernels with \(s\) vertices. Then

\[
a_{n,k}(s)=\frac ns [x^{n-s(k+1)}](1+x+\cdots+x^k)^s
\]
for positive \(s\), with a negative-degree coefficient understood to be zero. Equivalently, putting \(t=n-s(k+1)\),
\[
a_{n,k}(s)=\frac ns\sum_{0\le j\le s,\;t-j(k+1)\ge0}(-1)^j\binom sj\binom{t-j(k+1)+s-1}{s-1}.
\]
In particular, the attainable quasi-kernel cardinalities form the exact consecutive integer interval
\[
\left\{s\in\mathbb Z:\left\lceil\frac{n}{2k+1}\right\rceil\le s\le\left\lfloor\frac{n}{k+1}\right\rfloor\right\}.
\]
The minimum quasi-kernel size is \(\lceil n/(2k+1)\rceil\), the maximum is \(\lfloor n/(k+1)\rfloor\), and the displayed coefficient formula counts every optimum on both ends. For example, \(D_{9,2}\) has nine quasi-kernels of size two and three of size three, and none of other sizes.

## Assumptions and scope
All digraphs are finite and loopless, with both opposing arcs allowed. Modular increments are interpreted in \(\{1,\ldots,k\}\), so \(k<n\) prevents loops. Independence forbids an arc in either direction between distinct selected vertices. Directed two-step reachability includes paths of lengths zero, one and two. Quasi-kernels are subsets of distinct vertices, not cyclic sequences or orbits under rotation. The convention that a quasi-kernel reaches every vertex, rather than being reached by every vertex, agrees with the motivating 2026 paper; reversal of all arcs preserves these counts by reflection.

## Proof
Order the \(s\ge1\) selected vertices cyclically as \(q_1,\ldots,q_s\), and write \(g_i\) for the positive clockwise distance from \(q_i\) to \(q_{i+1}\), with indices taken cyclically. Then \(\sum_i g_i=n\). Independence is equivalent to \(g_i\ge k+1\) for every \(i\): an adjacent pair of selected vertices at clockwise distance at most \(k\) gives an arc; conversely any such arc between selected vertices would force an adjacent selected pair on its clockwise interval to have gap at most \(k\).

A path of at most two arcs from a selected vertex can travel forward by at most \(2k\) successive positions. Conversely every clockwise displacement \(1\le d\le2k\) is realizable by at most two arcs: use one arc if \(d\le k\), and steps \(k\) and \(d-k\) otherwise. Consider one cyclic gap between successive selected vertices \(q_i\) and \(q_{i+1}\). The vertices strictly inside that gap are all reachable from \(q_i\) within two steps exactly when \(g_i-1\le2k\). If \(g_i\ge2k+2\), the vertex at clockwise displacement \(2k+1\) from \(q_i\) is not reachable from \(q_i\), nor from any earlier selected vertex, because all predecessors lie farther clockwise from it. Nor can an alternative two-arc walk cover it by wrapping around: the existence of this gap implies \(n>2k+1\), so the total forward distance of at most \(2k\) cannot wrap around the whole cycle. Thus the quasi-kernel condition is exactly \(k+1\le g_i\le2k+1\) for every gap.

For fixed \(s\), the number of ordered gap vectors is \([x^n](x^{k+1}+\cdots+x^{2k+1})^s\). Decorate a quasi-kernel by one of its \(s\) selected vertices, and use that vertex as the starting point for its ordered clockwise gap vector. This gives \(s\,a_{n,k}(s)\) decorated objects. Conversely there are \(n\) choices for the starting vertex and one choice of ordered gap vector, giving the displayed \(n/s\) formula. Setting \(g_i=k+1+y_i\), the \(y_i\) range independently over \(\{0,\ldots,k\}\). Inclusion-exclusion for bounded weak compositions gives the binomial expression above. Such a sum of \(s\) bounded integers can attain every integer between its endpoints, so a quasi-kernel of size \(s\) exists exactly when \(s(k+1)\le n\le s(2k+1)\). This proves the entire cardinality spectrum and both extrema.

## Verification
The accompanying standalone Python program independently constructs arcs, all directed walks of length at most two, and every vertex subset for each of 90 pairs \((n,k)\) with \(3\le n\le14\) and \(1\le k<n\). It compares the direct subset census with an independently evaluated coefficient formula and returns `VERIFY_OK exhaustive_circulant_cases=90`. Run `python3 verify_quasi.py` with Python 3 and its standard library. These finite tests are checks of the specification and implementation; the preceding gap argument proves the infinite parameter family.

## Relationship to prior work
Ai, Gutin, Liu, and Meng (arXiv:2610.23487v1, first posted 2026-10-16) establish a weighted quasi-kernel transfer theorem and sharp universal bounds; they do not give a cardinality enumerator for powers of directed cycles. Gutin, Koh, Tay, and Yeo (2004) classify digraphs having one or two quasi-kernels and prove a lower bound of three for most strong digraphs. The present statement determines all cardinalities and the exact number of quasi-kernels of each size on the entire two-parameter directed circulant family. It is consistent with both prior general results and is not implied by their numerical bounds. Direct searches for oriented cycle powers, circular-arc domination, cyclic bounded compositions, and independent distance-two dominating sets did not identify an equivalent published statement. General bounded-composition tools underlie the enumerator, and a formulation elsewhere under periodic dominating codes remains a priority risk.

## Limitations
The result concerns consecutive-step circular powers, not arbitrary circulant step sets, mixed orientations, or arbitrary digraphs. It enumerates labeled vertex subsets, not inequivalent subsets up to dihedral symmetry. Its gap characterization uses the two-step reachability radius and does not assert results for higher reachability radii. The finite verifier is not an independent proof or external review; historical-priority and naming conventions may expose earlier equivalent formulations.

## References
1. J. Ai, G. Gutin, X. Liu, X. Meng, *Small and large quasi-kernels: a weighted transfer theorem*, arXiv:2610.23487v1 (2026-10-16), https://arxiv.org/abs/2610.23487v1.
2. G. Gutin, K. M. Koh, E. G. Tay, A. Yeo, *On the number of quasi-kernels in digraphs*, Journal of Graph Theory 46 (2004), 48–56, https://www.cs.rhul.ac.uk/home/gutin/paperstsp/quasik130903.pdf.
3. T. Nguyen, A. Scott, P. Seymour, *Distant digraph domination*, Electronic Journal of Combinatorics 33 (2026), P1.32, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p32/pdf/.
4. B. Jartoux, *Counting kernels in directed graphs with arbitrary orientations*, arXiv:2202.04476 (2022), https://arxiv.org/abs/2202.04476.
