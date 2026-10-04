# Almost-chain finite spaces without the fixed point property are exactly minimal sphere models
## Finding
Let \(P\) be a nonempty finite \(T_0\)-space and use the specialization order, so continuous self-maps are exactly order-preserving self-maps. Assume that every point is incomparable with at most one other point. Then \(P\) has a fixed-point-free continuous self-map if and only if there is an integer \(k\ge 1\) for which \(P\) is the ordinal sum of \(k\) copies of the two-point antichain.

When such a map exists it is unique. Writing the \(i\)-th antichain as \(\{a_i,b_i\}\), the map is
\[
 a_i\mapsto b_i,\qquad b_i\mapsto a_i
\]
for every \(1\le i\le k\). Thus, inside this near-chain class, failure of the fixed point property is equivalent to being one of the canonical \(2k\)-point finite sphere models.

The order complex is the join of \(k\) copies of a zero-sphere, hence the boundary of the \(k\)-dimensional cross-polytope. On that sphere the unique fixed-point-free map is induced by central inversion and therefore has degree \((-1)^k\).

## Assumptions and scope
A finite \(T_0\)-space is identified with its specialization poset. Two distinct points are called incomparable when neither is below the other. The hypothesis is that the incomparability degree of every point is at most one. The empty space is excluded. No claim is made for arbitrary width-two posets or for finite spaces with larger incomparability degree.

An ordinal sum of \(k\) two-point antichains means that the underlying set is partitioned into levels \(A_1,\ldots,A_k\), each of size two, points within a level are incomparable, and every point of \(A_i\) is below every point of \(A_j\) whenever \(i<j\).

## Proof
First use a finite-poset iteration lemma. Let \(f:P\to P\) be order-preserving. If \(x\le f(x)\), then
\[
 x\le f(x)\le f^2(x)\le\cdots .
\]
Because \(P\) is finite, this nondecreasing sequence eventually stabilizes, and the stabilization point is a fixed point of \(f\). The same argument with the inequalities reversed shows that if \(f(x)\le x\), then \(f\) has a fixed point. Consequently, if \(f\) is fixed-point-free, then \(x\) and \(f(x)\) are incomparable for every \(x\in P\).

Under the stated incomparability-degree hypothesis, a fixed-point-free \(f\) therefore forces every \(x\) to have exactly one incomparable point. Denote that point by \(\tau(x)\). Necessarily \(f(x)=\tau(x)\) for every \(x\). Symmetry of incomparability gives \(\tau^2=\operatorname{id}\), so the incomparability graph is a perfect matching and \(f=\tau\) is already unique.

It remains to recover the order. Let \(A=\{x,\tau(x)\}\) and \(B=\{y,\tau(y)\}\) be two distinct matching pairs. Every point of \(A\) is comparable with every point of \(B\), because the only point incomparable with a given element is its mate. Suppose \(x<y\). Since \(\tau=f\) is order-preserving, \(\tau(x)<\tau(y)\). We claim all four cross-comparisons point from \(A\) to \(B\). If \(y<\tau(x)\), then \(x<y<\tau(x)\), contradicting that \(x\) and \(\tau(x)\) are incomparable. Hence \(\tau(x)<y\). Likewise, if \(\tau(y)<x\), applying \(\tau\) gives \(y<\tau(x)\), which was just excluded; hence \(x<\tau(y)\). Together with \(x<y\) and \(\tau(x)<\tau(y)\), this shows every element of \(A\) is below every element of \(B\).

Therefore any two matching pairs are uniformly ordered. The set of pairs is consequently a finite total order, and \(P\) is the ordinal sum of its two-point antichain pairs.

Conversely, on any ordinal sum of two-point antichains, swapping the two points in each level preserves all order relations and has no fixed point. The previous argument shows it is the only fixed-point-free self-map.

For the sphere interpretation, Barmak and Minian describe the canonical \(2k\)-point minimal finite model as the iterated non-Hausdorff suspension of a two-point discrete space; its order is exactly the ordinal sum above. Its order complex is the join of \(k\) two-point discrete complexes, hence the cross-polytope boundary. The levelwise swap is induced by \(v\mapsto -v\) on \(\mathbb R^k\), whose determinant is \((-1)^k\), giving the stated degree.

## Verification
The accompanying `verify.py` performs two independent finite checks. First, it enumerates every labeled poset on at most four points, filters to incomparability degree at most one, enumerates every self-map, and verifies that the theorem predicts exactly the fixed-point-free order-preserving maps. The counts of all labeled posets for orders \(1,2,3,4\) are \(1,3,19,219\), matching the standard sequence. Among the filtered posets, exactly one labeled two-point poset and six labeled four-point posets admit a fixed-point-free map, as predicted by the ordinal-sum classification.

Second, it directly checks the canonical ordinal sums with one, two, and three levels. In every case exactly one fixed-point-free order-preserving self-map is found. A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Barmak and Minian's *Minimal Finite Models* identifies the iterated non-Hausdorff suspensions of the two-point discrete space as the unique minimal finite models of spheres and gives the explicit extremal order structure. Their paper does not formulate or prove the fixed-point-free classification above.

Szymik's *Homotopies and the universal fixed point property* reviews the equivalence between finite Kolmogorov spaces with continuous maps and finite posets with monotone maps, and discusses fixed-point properties and selection maps for finite posets. The inspected finite-poset section does not classify fixed-point-free self-maps under a matching incomparability hypothesis, nor does it single out the minimal sphere models by this fixed-point criterion.

Targeted searches for the equivalent formulations “incomparability graph a matching,” “every point incomparable with at most one other,” “ordinal sum of two-element antichains,” and “unique fixed-point-free self-map” did not locate a published statement implying the theorem. This is evidence of noncoverage, not a proof that no prior formulation exists.

## Limitations
The theorem uses the strong local hypothesis that every point has at most one incomparable partner. It does not classify fixed-point-free endomorphisms of general finite posets, even of all width-two posets. The computational verification is finite and is not used as a proof of the all-cardinality statement. The degree conclusion concerns the induced map on the order complex; it does not assert that arbitrary fixed-point-free maps on ordinary spheres are unique.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first submitted 2006-11-06; Journal of Homotopy and Related Structures 2 (2007), 127–140.
2. M. Szymik, *Homotopies and the universal fixed point property*, arXiv:1210.6496, first submitted 2012-10-24; Order 32 (2015), 301–311.
