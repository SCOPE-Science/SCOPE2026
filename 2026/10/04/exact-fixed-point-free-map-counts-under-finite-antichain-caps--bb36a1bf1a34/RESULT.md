# Exact fixed-point-free map counts under finite antichain caps
## Finding
Let \(X\) be a nonempty finite \(T_0\)-space and identify it with its specialization poset. For an integer \(r\ge 2\), let \(A_r\) be an \(r\)-point antichain disjoint from \(X\), and let \(X\oplus A_r\) be the ordinal sum in which every point of \(X\) lies below every point of \(A_r\).

Write \(\operatorname{Fpf}(X)\) for the fixed-point-free order-preserving self-maps \(g:X\to X\). For \(g\in\operatorname{Fpf}(X)\), define
\[
u(g)=\left|\left\{z\in X: g(x)\le z\text{ for every }x\in X\right\}\right|.
\]
Then the number \(N_{\mathrm{fpf}}\) of fixed-point-free continuous self-maps satisfies
\[
N_{\mathrm{fpf}}(X\oplus A_r)=\sum_{g\in\operatorname{Fpf}(X)}(u(g)+r-1)^r.
\]
For \(r=2\), \(X\oplus A_2\) is the non-Hausdorff suspension \(SX\), so
\[
N_{\mathrm{fpf}}(SX)=\sum_{g\in\operatorname{Fpf}(X)}(u(g)+1)^2.
\]
As a qualitative corollary for every \(r\ge2\), \(X\oplus A_r\) has the fixed point property exactly when \(X\) does. That existence-level consequence is consistent with the classical lexicographic-sum fixed-point theory; the result above is the exact enumeration refinement.

## Assumptions and scope
All spaces are finite and \(T_0\). Continuity is therefore equivalent to order preservation. The construction is the ordinal sum with a discrete set of new maximal points. The theorem counts all fixed-point-free self-maps exactly; it does not count maps with prescribed numbers of fixed points, nor does it claim a formula for arbitrary lexicographic sums.

The statistic \(u(g)\) counts common upper bounds in \(X\) of the entire image \(g(X)\). It depends on the actual endomorphism, not only on the homotopy class or the induced action on homology.

## Proof
Put \(Y=X\oplus A_r\) and write \(A_r=\{a_1,\ldots,a_r\}\). Let \(F:Y\to Y\) be order preserving and fixed-point-free.

First, \(F(X)\subseteq X\). Indeed, suppose that \(F(x)=a_j\) for some \(x\in X\). Since \(x<a_i\) for every \(i\), monotonicity gives \(a_j=F(x)\le F(a_i)\). The point \(a_j\) is maximal in \(Y\), so this forces \(F(a_i)=a_j\) for every \(i\). Taking \(i=j\) gives \(F(a_j)=a_j\), contradicting fixed-point-freeness.

Hence \(g=F|_X\) is a fixed-point-free order-preserving self-map of \(X\). Fix such a map \(g\). For each new maximal point \(a_i\), monotonicity of an extension \(F\) is equivalent to
\[
g(x)\le F(a_i)\qquad\text{for every }x\in X.
\]
If \(F(a_i)\in X\), there are exactly \(u(g)\) possibilities, namely the common upper bounds of \(g(X)\). If \(F(a_i)\in A_r\), every new maximal point satisfies the required inequalities, but fixed-point-freeness excludes \(a_i\) itself, leaving exactly \(r-1\) possibilities. Distinct points of \(A_r\) are incomparable, so there are no further relations coupling these choices. Thus \(g\) has exactly \((u(g)+r-1)^r\) fixed-point-free extensions to \(Y\).

Conversely, choosing independently for each \(a_i\) one of those \(u(g)+r-1\) allowed images produces an order-preserving map: all relations internal to \(X\) are respected by \(g\), every relation \(x<a_i\) is respected by construction, and there are no relations between distinct members of \(A_r\). The map is fixed-point-free because \(g\) is fixed-point-free and \(a_i\) was excluded as the image of itself. Summing over \(g\in\operatorname{Fpf}(X)\) proves the formula.

## Verification
The proof above is symbolic and is the evidence for all finite \(X\) and all \(r\ge2\). The accompanying standard-library program `verify.py` independently enumerates every labeled poset on at most four points, every order-preserving self-map involved, and compares the direct fixed-point-free count on \(X\oplus A_r\) with the formula. It checks all \(r=2\) cases through four points and all \(r=3\) cases through three points, for \(265\) theorem instances. Running

`python3 verify.py`

prints the deterministic summary recorded in `verification_output.txt` and ends with `VERIFY_OK`.

These finite computations are regression checks only. They are not used to infer the theorem for untested sizes.

## Relationship to prior work
Barmak and Minian identify finite \(T_0\)-spaces with finite posets and explicitly define the non-Hausdorff suspension \(SX\) by adjoining two new points; their paper does not enumerate fixed-point-free self-maps of that construction. Höft and Höft study fixed-point-free components in lexicographic sums and prove qualitative criteria for when such a sum has the fixed point property. Their main characterization, and their two-element-antichain example, concern existence of fixed points rather than an exact count of fixed-point-free endomorphisms. Baclawski and Björner provide foundational fixed-point theory for posets, again at the level of fixed-point existence and topology of fixed-point sets.

The formula here is strictly finer than the qualitative fixed-point-property statement for this two-level lexicographic sum: it resolves every fixed-point-free map of \(X\) by the common-upper-bound statistic \(u(g)\) and counts all extensions exactly.

## Limitations
The theorem is special to an antichain of new maximal points. For a general ordinal or lexicographic summand, relations inside the added part couple the images and the independent-choice factor \((u(g)+r-1)^r\) no longer applies. The result also does not classify the distribution of \(u(g)\) for a given \(X\); computing that distribution can itself be difficult.

The literature comparison included the most directly relevant accessible full texts on non-Hausdorff suspension and lexicographic-sum fixed-point theory. An older or obscure source could in principle contain an equivalent enumeration formula; no such formula was found in the targeted searches or inspected sources.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, 6 November 2006.
2. H. Höft and M. Höft, *Fixed point free components in lexicographic sums with the fixed point property*, Demonstratio Mathematica 24 (1991), DOI: 10.1515/dema-1991-1-227.
3. K. Baclawski and A. Björner, *Fixed Points in Partially Ordered Sets*, Advances in Mathematics 31 (1979), 263–287, DOI: 10.1016/0001-8708(79)90045-8.
4. B. S. W. Schröder, *The fixed point property for ordered sets*, Arabian Journal of Mathematics 1 (2012), 529–547, DOI: 10.1007/s40065-012-0049-7.
