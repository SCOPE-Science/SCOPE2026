# Strict-order degree pairs reconstruct width-two series–parallel posets, with a sharp five-point orbit boundary

## Finding
Let \(P=(X,<)\) be a nonempty finite series–parallel partial order of width at most two. For each \(x\in X\), put
\[
 d_-(x)=|\{y\in X:y<x\}|,\qquad d_+(x)=|\{y\in X:x<y\}|.
\]
The **unordered multiset** \(\mathcal D(P)=\{\!\{(d_-(x),d_+(x)):x\in X\}\!\}\) determines \(P\) up to order isomorphism. Moreover, two vertices of \(P\) have identical degree pairs if and only if an order automorphism takes one to the other. Thus the very first nontrivial round of ordinary directed counting colour refinement, started uniformly on the strict-order relation, already yields the automorphism-orbit partition, and its cross-structure colour histogram distinguishes nonisomorphic posets **within this class**. In particular, the class is identifiable internally by two-variable first-order logic with counting.

The canonical series-factor normal form is a finite sequence whose entries are singletons and parallel unions of two nonempty chains \(C_a\parallel C_b\), with \(1\le a\le b\). The corresponding ordinary generating function for isomorphism classes, including the empty poset, is
\[
 F(z)=\frac{1}{1-z-\frac{z^2}{(1-z)(1-z^2)}}.
\]
Its positive-order coefficients for orders one through twelve are \(1,2,4,9,19,41,87,186,396,845,1801,3841\).

The width bound is sharp for the **orbit-recovery-by-degree-pairs** assertion: the disjoint parallel union of a three-vertex \(V\)-shaped poset and a two-element chain has width three and five vertices. It has two maximal points with the same pair \((1,0)\) lying in distinct automorphism orbits (indeed the two maximal vertices of the \(V\) share that pair with the maximum of the two-element chain). Its order dual is the other five-point obstruction. There is no orbit-recovery failure for any series–parallel poset on at most four vertices; at five vertices exactly these two dual isomorphism types fail.

## Assumptions and scope
A finite series–parallel poset is obtained from singleton posets by repeated **series composition** \(A\oplus B\), which places every element of \(A\) below every element of \(B\), and **parallel composition** \(A\parallel B\), which introduces no comparisons between factors. Equivalently these are finite \(N\)-free posets. Width is the maximum size of an antichain. A chain \(C_a\) has \(a\ge1\) elements. All degrees count the full **strict transitive order relation**, not cover edges of a Hasse diagram. The empty poset occurs solely as the unit in the generating function and is excluded from the main claim. The signature contains the named strict binary order predicate, so counting refinement counts predecessors and successors separately.

No claim is made for arbitrary width-three posets or for non-series–parallel posets. The isomorphism assertion is restricted to comparing two posets both in the stated class; it is not a claim of identification against arbitrary relational structures.

## Proof
**Canonical normal form.** Flatten consecutive series and consecutive parallel operations. The series-indecomposable factors of any nontrivial finite series–parallel poset are exactly the connected components of its *incomparability graph*, ordered by the direction of the intercomponent comparisons. To see this, the series composition makes its factors pairwise comparable across factors, hence disconnected in the incomparability graph; an indecomposable parallel node has its incomparability graph connected because every vertex of one nonempty parallel child is incomparable with every vertex of the others. This establishes uniqueness of the maximal ordered series decomposition. In a poset of width at most two, each such factor is either a singleton or a parallel union of exactly two chains: a parallel node has width equal to the sum of the widths of its children, so two or more nonempty children and a total width bound of two force exactly two width-one children, hence chains. The two chain lengths are unordered, and their normal form is \(C_a\parallel C_b\), \(a\le b\).

**Degree formulas.** Let \(n=|X|\). Fix a series factor \(B\), write \(p\) for the total size of earlier factors and \(s=n-p-|B|\) for the total size of later factors. If \(B\) is a singleton, its unique point has degree pair \((p,s)=(p,n-p-1)\). If \(B=C_a\parallel C_b\), then a point in the first chain at zero-based position \(t\in\{0,\dots,a-1\}\) has degree pair
\[
 (p+t,s+a-1-t)=(p+t,n-p-b-1-t),
\]
and a point in the second chain at position \(r\in\{0,\dots,b-1\}\) has pair
\[
 (p+r,s+b-1-r)=(p+r,n-p-a-1-r).
\]
Every degree-pair predecessor count in \(B\) belongs to the integer interval \([p,p+|B|-1]\), and those of later series factors begin at least at \(p+|B|\). Consequently the predecessor-count intervals of different series factors are disjoint.

**Reconstruction.** A multiset of the \(n\) degree pairs permits an explicit left-to-right decoder. Initially \(p=0\). At each stage exactly the first elements of the next series factor have predecessor count \(p\). If there is only one, the next factor is a singleton of size one, with successor count \(n-p-1\). If there are two, with successor counts \(u,v\), the next factor is a two-chain parallel sum with unordered chain lengths
\[
 \{a,b\}=\{n-p-1-u,n-p-1-v\}.
\]
Both lengths are positive and their sum is the factor size \(m=a+b\). Remove the multiset entries whose predecessor counts lie in \([p,p+m-1]\), increase \(p\) by \(m\), and repeat. Because of the disjointness just proved, this consumes exactly that factor and never a later factor. The unique canonical list is recovered without knowing any labels, proving the isomorphism assertion.

**Orbits and the first refinement.** Order automorphisms preserve each position in the ordered series list. They fix a singleton and, in a parallel two-chain factor, preserve each chain unless \(a=b\), in which case the two chains may be swapped. Each chain itself has only the identity order automorphism. Within a factor the displayed degree pairs are equal precisely for equal zero-based positions on equal-length chains; different factors have disjoint predecessor-count intervals. Therefore degree-pair equality and automorphism-orbit equivalence coincide. One directed counting-refinement round from the uniform colouring assigns the signature consisting of old colour and predecessor/successor counts, which is exactly this degree pair. For two structures in the class, the common colour histogram determines the degree-pair multiset and hence isomorphism. Explicit \(C^2\) formulas for the number of vertices of a given pair are obtainable by counting \(x\) satisfying both \(\exists^{=a}y\,(y<x)\) and \(\exists^{=b}y\,(x<y)\), which use only \(x,y\).

**Generating function.** A singleton contributes \(z\). An unordered pair of positive chain lengths contributes
\[
 \sum_{1\le a\le b}z^{a+b}=\frac{z^2}{(1-z)(1-z^2)}.
\]
The normal form is an arbitrary ordered sequence of these atomic factors, yielding the displayed reciprocal series.

**Sharp finite boundary.** For \(Q=(C_1\oplus(C_1\parallel C_1))\parallel C_2\), the two maximal elements in the \(V\) component have strict degree pair \((1,0)\), as does the maximal point of the separate chain. These vertices are not in one automorphism orbit: their comparability components have different cardinalities. The dual gives the second example. For the no-smaller and exactly-two-at-size-five statements, the executable exhaustive certificate `verify_boundary.py` recursively generates all canonical series/parallel trees at orders one through six, normalizing associativity and commutativity, and explicitly tests **every permutation** for preservation of the strict order relation. It finds \(1,2,5,15,48,167\) isomorphism types at orders one through six, with zero degree/orbit failures through order four and precisely the two dual failures at order five. The generator's completeness follows inductively from the defining series/parallel construction and the canonical decomposition above; its explicit permutation test is exhaustive, not a random graph sample.

## Verification
`verify_normal_form.py` independently generates every width-at-most-two normal form through twelve vertices, constructs its full strict order, tests the unlabeled multiset decoder, checks the absence of cross-structure degree-multiset collisions and confirms degree-pair/orbit equality for every vertex pair. It checks 7,232 normal forms and outputs `NORMAL_FORM_VERIFY_PASS`.

`verify_boundary.py` uses a different recursive constructor for all series–parallel posets through six points and determines each automorphism orbit by enumerating all vertex permutations. It verifies the width bound for every example and the precise first-failure statement, outputting `BOUNDARY_VERIFY_PASS`. The actual invocation and observed output are embedded in the accompanying records. These finite checks corroborate the all-order proof; the proof does not infer an infinite theorem from a finite enumeration.

## Relationship to prior work
Valdes, Tarjan and Lawler give foundational recognition and decomposition theory for series–parallel digraphs; Habib, Kelly, Lebhar and Paul use the canonical composition tree of series–parallel posets for sandwich recognition. Those results supply the structural setting, not the specific reconstruction of a width-two poset from the multiset of strict predecessor/successor counts or its sharp orbit boundary. Arvind, Köbler, Rattan and Verbitsky study colour-refinement identification and orbit refinement for *undirected* graphs; their general equivalence and hierarchy motivate the question but do not imply this result for the directed transitive comparability relation. Dukes, Kitaev, Remmel and Steingrímsson study *\((2+2)\)-free* posets via indistinguishability of complete upper/lower sets, a different forbidden pattern and a different invariant. No full-range equivalent to the asserted reconstruction was identified in the inspected sources and recorded research searches. Earlier specialized coverage remains a residual publication-priority risk.

## Limitations
The reconstruction is for width at most two **and** series–parallel posets; removal of either hypothesis is not covered. Its positive assertion applies to the first refinement round on the **strict order** representation, not necessarily to cover graphs. The five-point boundary addresses orbit recovery by **degree pairs**, not the stabilized colouring or cross-structure identification of width-three posets. Exhaustive verification is finite and limited to the recorded ranges. No independent scientific validation or publication-priority certification is claimed here.

## References
1. J. Valdes, R. E. Tarjan and E. L. Lawler, *The Recognition of Series Parallel Digraphs*, STOC 1979, 1–12, DOI 10.1145/800135.804393 (first listed publication 1979-04-30).
2. M. Habib, D. Kelly, E. Lebhar and C. Paul, *Can transitive orientation make sandwich problems easier?*, Discrete Mathematics 307 (2007), 2030–2041, DOI 10.1016/j.disc.2005.12.048.
3. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, initially public 2015-02-04.
4. M. Dukes, S. Kitaev, J. Remmel and E. Steingrímsson, *Enumerating (2+2)-free posets by indistinguishable elements*, arXiv:1006.2696, initially public 2010-06-14.
