# The quarter-circumference law for commuting retractions of finite metric cycles

## Finding
Let \(n\ge 3\) be an integer, and let \(C_n\) be the set \(\{0,1,\ldots,n-1\}\) with the shortest-path metric of the unit-edge cycle. For an ordering \((v_1,\ldots,v_n)\) of its vertices with \(v_1=0\), consider retractions \(r_k:C_n\to\{v_1,\ldots,v_k\}\), one for each \(1\le k\le n\), such that \(r_jr_k=r_kr_j=r_{\min(j,k)}\). Define \(\kappa(C_n)\) to be the minimum, over all these choices, of \(\max_{1\le k\le n}\operatorname{Lip}(r_k)\). Then
\[
\boxed{\kappa(C_n)=\left\lceil\frac n4\right\rceil}\qquad(n\ge3).
\]
An optimal family is explicitly given below. The optimal lower bound follows from an integer winding invariant: a one-vertex collapse cannot alter winding if every map moves adjacent vertices through distances strictly less than one quarter of the circumference.

## Assumptions and scope
Every edge in \(C_n\) has length \(1\), and \(d(i,j)=\min\{|i-j|,n-|i-j|\}\). All retractions are defined on the full vertex set and use this **ambient** metric; their images are arbitrary vertex prefixes, not necessarily induced connected subgraphs. A retraction onto \(S\) fixes each point of \(S\). Commutativity and the single-new-vertex condition are essential. No assertion concerns arbitrary linear bases of the associated Lipschitz-free space, weighted cycles, or continuous circles.

For every map \(f:C_n\to C_n\), its Lipschitz norm equals the maximum of \(d(f(i),f(i+1))\) over the \(n\) unit edges (indices modulo \(n\)). Indeed, shortest cycle paths give the inequality from edge bounds to all pairs. Thus each such Lipschitz norm is a nonnegative integer, and each retraction onto the whole cycle has norm \(1\).

## Proof
**Lower bound.** Suppose a commuting prefix family satisfies \(K:=\max_k\operatorname{Lip}(r_k)<n/4\). Each successive map sends adjacent domain vertices to target vertices at graph distance at most \(K<n/2\). For an oriented edge \(i\to i+1\), define \(\Delta_f(i)\) to be the unique integer in \((-n/2,n/2)\) congruent to \(f(i+1)-f(i)\pmod n\), where \(f=r_k\). Uniqueness holds because \(|\Delta_f(i)|\le K<n/4\). The number
\[
\deg(f):=\frac1n\sum_{i=0}^{n-1}\Delta_f(i)
\]
is an integer, since the telescoping sum is \(0\pmod n\). The identity \(r_n\) has degree \(1\), while the constant \(r_1\) has degree \(0\).

Fix \(k<n\), set \(f=r_{k+1}\), \(g=r_k\), and write \(v=v_{k+1}\) and \(a=g(v)\), with \(a\) in the earlier prefix. Commutativity gives \(g=g\circ f\), so \(g(x)=f(x)\) unless \(f(x)=v\); in the latter case \(g(x)=a\). If \(k\ge1\), the set \(E=f^{-1}(v)\) is a nonempty proper subset of the cycle, because \(f\) fixes at least one earlier vertex. Decompose \(E\) into maximal cyclic consecutive intervals. In each interval, all internal edges have equal endpoint images under both maps, contributing zero to the degree difference. Let \(b,c\) be the common images of the exterior neighbors immediately before and after that interval. The two boundary-edge contributions to \(n(\deg f-\deg g)\) are
\[
\Delta(b,v)+\Delta(v,c)-\Delta(b,a)-\Delta(a,c),
\]
where \(\Delta(u,w)\) denotes the uniquely chosen short signed arc from \(u\) to \(w\). Each of the four oriented arcs has length at most \(K\), because it is the image of a unit domain edge under \(f\) or \(g\). The displayed integer is divisible by \(n\) (it is the signed length of a closed loop) and has absolute value at most \(4K<n\). It is therefore zero. Summing over all intervals proves \(\deg f=\deg g\). Induction from \(k=1\) to \(k=n-1\) gives \(0=1\), a contradiction. Hence \(K\ge n/4\). As \(K\) is an integer, \(K\ge\lceil n/4\rceil\).

**Upper bound.** For \(n=3\), every two distinct cycle vertices have distance \(1\); choose any ordering from \(0\) and map each not-yet-fixed vertex to \(0\). All maps are \(1\)-Lipschitz.

For \(n\ge4\), write \(K=\lceil n/4\rceil\) and take the quarter-point anchors
\[
 a=\lceil n/4\rceil,\qquad b=\lceil n/2\rceil,\qquad c=\lceil3n/4\rceil.
\]
These satisfy \(0<a<b<c<n\), and all four forward cyclic gap lengths \(a,b-a,c-b,n-c\) are at most \(K\). Enumerate the vertices in the order \(0,a,b,c\), followed by all remaining vertices in increasing numerical order. Assign each nonroot vertex a parent of smaller enumeration rank: \(a\mapsto0\), \(b\mapsto a\), \(c\mapsto a\), and for a nonanchor vertex in one of the four open arcs \((0,a),(a,b),(b,c),(c,n)\), assign parent \(0,a,b,c\), respectively. Set \(r_k(x)\) equal to the first ancestor of \(x\) whose enumeration rank is at most \(k\). These maps fix exactly the first \(k\) vertices and commute, since taking successive rank truncations is associative.

For the initial three nontrivial prefixes, all map values are among \(\{0\}\), \(\{0,a\}\), or \(\{0,a,b\}\). The two-label map has Lipschitz constant at most \(d(0,a)\le K\). The three-label map, read clockwise around the original cycle, has successive constant-label regions \(0,a,b,a\) and hence only transitions between \(0,a\) or \(a,b\), whose distances are at most \(K\). Once all four anchors are fixed, every edge lies within a closed forward arc between consecutive anchors, of length at most \(K\). Throughout the subsequent insertions the image of either endpoint is either itself or the starting anchor of this arc. Thus both images lie in the same closed arc and have ambient distance at most its length, which is at most \(K\). Every map in the family is therefore \(K\)-Lipschitz, proving equality.

## Verification
A standalone Python 3 script, `check_cycle.py`, constructs the parent rule and directly checks vertex ranks, retraction ranges, edgewise Lipschitz bounds, and commutation for every \(3\le n\le128\). Running `python3 check_cycle.py` produced:

`PASS: 126 cycle sizes (n=3,...,128), every prefix, all cycle edges, and commutation`

This finite test supports the upper-bound construction but does not establish the formula for arbitrarily large \(n\); both bounds are proved above without relying on a finite search. The lower-bound argument uses an exact integer-degree obstruction rather than numerical extrapolation.

## Relationship to prior work
Novotný [1, Theorem 5] proves a growing lower bound for commuting retractions on a **different pointed metric**, namely a cycle with an extra central basepoint at distance equal to the radius from every rim vertex. His bound of order \(\sqrt n\) does not imply an exact value for an ordinary cycle rooted **at a rim vertex**, nor does the quarter-circle construction apply to the added center. Hájek–Medina [2, Definition 1.2 and Theorem 2.6] develop commuting retractional bases for nets in finite-dimensional Banach spaces; their dimension-independent net bound neither determines nor bounds sharply the present finite-cycle extremum. The exact \(\lceil n/4\rceil\) formula supplies a finite cycle benchmark for the norm cost of retraction-derived linear projection chains.

## Limitations
Only unit-edge simple cycles are treated. The claim does not say that every ordering attains the optimum; the four-anchor ordering is essential to the supplied upper bound. It does not optimize arbitrary nonretractional projection sequences on Lipschitz-free spaces. The earlier centered-cycle result and possible unindexed equivalent treatments remain relevant bibliographic comparisons. Independent external mathematical evaluation has not been carried out.

## References
1. M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188, first public 2019-05-30. Especially Definition 3 and Theorem 5 (centered-cycle metric), and Corollary 2 (commuting retractions).
2. P. Hájek and R. Medina, *Schauder Bases in Lipschitz Free Spaces over Nets in Banach Spaces*, arXiv:2112.03095, first public 2021-12-07. Especially Definition 1.2 and Theorem 2.6.
