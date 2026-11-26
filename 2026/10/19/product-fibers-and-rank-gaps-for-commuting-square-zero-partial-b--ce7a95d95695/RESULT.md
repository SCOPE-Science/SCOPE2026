# Product fibers and rank gaps for commuting square-zero partial bijections

## Finding
Let \(\mathcal I_n\) be the symmetric inverse monoid (the monoid of all partial bijections of a labeled \(n\)-element set), with zero the empty map. Put
\[
 Z_m=\#\{(a,b)\in\mathcal I_m^2:a^2=b^2=ab=ba=0\},\qquad Z_0=1.
\]
Its exponential generating function is
\[
 Z(z)=\sum_{m\ge0}Z_m\frac{z^m}{m!}=\frac{\exp\bigl(z+2z^2/(1-z)\bigr)}{1-z^2}.
\]
For any prescribed partial bijection \(h\in\mathcal I_n\) of rank \(r\), the exact number \(F_n(h)\) of ordered pairs satisfying \(a^2=b^2=0\), \(ab=ba=h\) is
\[
F_n(h)=\begin{cases}
\displaystyle\frac{(n-2r)!}{(n-4r)!}\,Z_{n-4r},&h^2=0,\quad 4r\le n,\\[4pt]
0,&\text{otherwise}.
\end{cases}
\]
Thus, for fixed \(n\), the fiber cardinality depends only on the rank **among admissible targets**, meaning square-zero maps of rank at most \(\lfloor n/4\rfloor\). It does not depend on rank alone across arbitrary prescribed partial bijections: for \(n=4\), the rank-one arrow \(1\mapsto2\) has a fiber of size 2, while the rank-one partial identity on \(\{1\}\) has an empty fiber.

If \(C_{n,r}\) is the number of all such ordered commuting pairs whose product has rank \(r\), then
\[
 \sum_{n\ge0}\sum_{r\ge0}C_{n,r}\,t^r\frac{z^n}{n!}
 =\frac{\exp\bigl(z+2z^2/(1-z)+tz^4\bigr)}{1-z^2}.
\]
The possible product ranks are exactly \(0,1,\ldots,\lfloor n/4\rfloor\). Thus the sharp bound \(\operatorname{rank}(ab)\le\lfloor n/4\rfloor\) holds for all commuting square-zero partial bijections.

## Assumptions and scope
Here \(n\) ranges over all nonnegative integers. Composition has the functional convention \((ab)(x)=a(b(x))\); reversing this convention leaves the assertions unchanged because the pairs commute. A partial map is undefined outside its domain, and equality of partial maps includes equality of domains. Products, squares and zero are calculated in \(\mathcal I_n\), not in its semigroup algebra. Pairs are ordered. The generating functions are formal power series over \(\mathbb Q[t]\).

## Proof
**1. Directed colored graph.** For \(a^2=b^2=0\), depict each arrow of \(a\) in color A and each arrow of \(b\) in color B. Each color separately forms disjoint one-arrow chains: each vertex is incident with at most one arrow of that color, because the map is injective and its domain and image are disjoint. Parallel arrows of distinct colors are allowed.

**2. Forced diamonds.** Suppose \(ab=ba\) and their common product contains \(s\mapsto t\). Write \(u=a(s)\) and \(v=b(s)\), with \(b(u)=a(v)=t\). The vertex \(s\) lies in both domains; \(t\) is in both images; \(u\) is in the image of \(a\) and the domain of \(b\); and \(v\) is in the image of \(b\) and the domain of \(a\). Disjointness of each map's domain and image makes these four vertices pairwise distinct. On these vertices the A-arrows are \(s\to u\) and \(v\to t\), and the B-arrows are \(s\to v\) and \(u\to t\). Every vertex is incident with its unique possible arrow of each color. This diamond therefore has no arrows to any outside vertex and contains exactly one product arrow. Consequently, \(r=\operatorname{rank}(ab)\) requires \(4r\) distinct vertices; disjoint diamonds and isolated vertices attain every allowed rank.

**3. Zero-product pieces.** Remove all the forced diamonds. On the remaining vertices both mixed products vanish. No vertex there can have an incoming arrow of one color and an outgoing arrow of the other: that would define a nonzero mixed product. The square-zero hypotheses exclude incoming and outgoing arrows of the same color. Thus each nonisolated vertex is either a source of all its incident colored arrows or a sink of all of them. Each color has degree at most one, so every nontrivial component of the underlying colored multigraph is an alternating-color path, an alternating even cycle, or a pair of parallel differently-colored edges (viewed as the length-two cycle). The directed edges run from the source bipartition to the sink bipartition. Conversely, every such colored oriented component defines two injective square-zero maps with both mixed products zero.

**4. Labeled connected counts.** An isolated vertex contributes \(z\) to the connected exponential generating series. For a path on \(k\ge2\) labeled vertices choose a linear ordering, a color for the first edge and a source/sink status for the first vertex, then identify the two parametrizations by reversal. This gives \(2k!\) labeled structures and contributes \(2z^k\). For each even cycle on \(2j\ge4\) labeled vertices, there are \((2j-1)!/2\) undirected cycles, with two alternating colorings and two source/sink choices each; they contribute \(z^{2j}/j\). The parallel-edge two-cycle has two orientations on its two vertices and contributes \(z^2\). The connected series is therefore
\[
 z+\sum_{k\ge2}2z^k+\sum_{j\ge1}\frac{z^{2j}}j
 =z+\frac{2z^2}{1-z}-\log(1-z^2).
\]
The labeled exponential formula yields \(Z(z)\).

**5. Prescribed product fibers.** If \(h=ab=ba\), then \(h^2=a^2b^2=0\). For a square-zero target of rank \(r\), its arrows have disjoint source and target sets, leaving \(n-2r\) unused vertices. Each arrow \(s\to t\) forces a diamond, whose ordered intermediate vertices can be chosen freely subject to all \(2r\) intermediate vertices being distinct. For \(4r\le n\) this gives \((n-2r)!/(n-4r)!\) choices. The remaining \(n-4r\) vertices carry any of the \(Z_{n-4r}\) zero-product pairs, independently. This number is positive because the zero-product pair of empty maps is always available. If \(4r>n\) no diamond assignment is possible.

**6. Rank refinement.** The number of square-zero partial maps of rank \(r\) is \(n!/[r!(n-2r)!]\): choose disjoint source and target sets and a bijection. Multiplying by the fiber cardinality gives \(C_{n,r}=n! Z_{n-4r}/[r!(n-4r)!]\) for \(4r\le n\), and zero otherwise. Summation gives \(Z(z)\exp(tz^4)\).

## Verification
The accompanying standalone `verify.py` enumerates square-zero partial bijections directly from disjoint source and target sets. For \(0\le n\le7\), it tests every ordered pair for commutation, tabulates every prescribed square-zero product, and compares those fibers and product-rank counts with an integer recurrence from the connected components. Run `python3 verify.py` with standard Python 3. The expected totals for \(n=0,\ldots,7\) are \(1,1,7,31,277,2101,22891,245827\); the rank-one counts for \(n=4,5,6,7\) are \(24,120,2520,26040\). Targets that do not square to zero are excluded by the proof, not by the finite square-zero target census. The same-rank contrast in the Finding follows from the two choices of ordered intermediate vertices versus the impossibility of a non-square-zero target.

## Relationship to prior work
Ganyushkin and Mazorchuk [1] develop chain/cycle enumeration for individual partial injections and study unrestricted random products in Section 6. Their fixed-outcome product probabilities do not condition on commuting square-zero factors. Araújo, Bentz and Konieczny [2] give the general chain-based commutation criterion in Proposition 2.2. Its specialization to one-arrow chains gives the local structural background; the enumerative claims here concern the zero-product component counts and the labeled fibers and rank series built from them. There is also a finite-field matrix analogue [3] with a four-times-rank feasibility condition and a residual zero-product factor. It counts all linear endomorphisms, rather than the partial-bijection submonoid with its injective colored-arrow constraints; its fibers do not directly give the restricted labeled counts here.

## Limitations
No claim concerns noninjective partial maps, nilpotency index greater than two, arbitrary linear endomorphisms, or unordered pairs. Exhaustive finite checks corroborate but do not establish the general enumerative theorem. An equivalent specialized enumeration not identified in the inspected literature may exist.

## References
1. O. Ganyushkin and V. Mazorchuk, *Combinatorics and distributions of partial injections*, arXiv:math/0511431v1 (17 November 2005), https://arxiv.org/abs/math/0511431.
2. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664v1 (8 May 2012), https://arxiv.org/abs/1205.1664.
3. *Complete finite-field product fibers for pairs of commuting square-zero matrices*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-complete-finite-field-product-fibers-for-pairs-of-commuting-squa--c8a4349a84d7.
