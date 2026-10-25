# Sharp finite-base type spectrum for unordered generic multiorders

## Finding
Fix an integer \(d\ge1\). Let \(\mathcal M_d\) be the Fraïssé limit of all finite sets equipped with \(d\) unrelated named strict linear orders \(<_1,\ldots,<_d\). Let \(G_d\) be the closed permutation group consisting of the permutations of its domain that permute these orders, independently allowing each order to be reversed. Thus \(G_d/\operatorname{Aut}(\mathcal M_d)\) is the signed permutation group \(C_2\wr S_d\).

Fix an ordered tuple \(A=(a_1,\ldots,a_m)\) of distinct individually named points. For \(m\ge2\), let \(\pi_j\in S_m\) list the parameter labels in increasing \(<_j\)-order. Identify a permutation with its reversed list, and let \(r_1,\ldots,r_h\) be the positive multiplicities of the resulting unoriented ranking patterns among the \(d\) coordinates. Then the number \(t(A)\) of complete nonalgebraic one-types over \(A\) for the reduct determined by \(G_d\) is exactly
\[
 t(A)=\prod_{i=1}^{h}\binom{m+r_i}{r_i}.
\]
The residual coordinate-symmetry quotient of the pointwise stabilizer has order \(\prod_{i=1}^{h}r_i!\). For \(m=0\) or \(1\), there is exactly one nonalgebraic one-type (and for \(m=1\) the full signed-coordinate quotient remains).

Set \(K=m!/2\), an integer when \(m\ge2\), and divide \(d=qK+s\) with \(0\le s<K\). Among **all** individually named \(m\)-point bases in \(\mathcal M_d\), the sharp extremal type counts are
\[
 \boxed{\binom{m+d}{d}\le t(A)\le
 \binom{m+q}{q}^{K-s}\binom{m+q+1}{q+1}^{s}.}
\]
The lower bound is attained exactly when all \(d\) coordinate rankings agree up to reversal. The upper bound is attained exactly when the multiplicities of the \(K\) possible unoriented rankings differ by at most one (including zeros). Every stated equality configuration exists.

The least number of individually named parameters for which **some** base destroys every nonidentity signed-coordinate symmetry is
\[
 \boxed{m_d=\min\{m\ge2:m!/2\ge d\}.}
\]
In particular, this is a strict, all-dimensional threshold, not merely an asymptotic estimate.

## Assumptions and scope
The statements concern \(d\ge1\), finite tuples of **distinct**, **pointwise fixed** parameters, and **nonalgebraic** one-types. The group \(G_d\) is precisely the signed-coordinate overgroup defined above, not the group of all reduct automorphisms and not a claim about classification of all reducts. For \(m\ge2\), the parameter labels are kept fixed; an unoriented ranking is the two-element set \(\{\pi,\operatorname{rev}(\pi)\}\), and so there are exactly \(m!/2\) such classes. The powers with exponent zero in the extremal formula equal one.

## Proof
**1. Existence and the group quotient.** The class of all finite \(d\)-multiorders has the strong amalgamation property: amalgamate each linear order independently, inserting the new elements in any prescribed relative slots. Its countable Fraïssé limit is ultrahomogeneous. Reindexing the \(d\) orders and independently reversing them preserves the age, so every signed coordinate permutation is realized by a permutation of the countable domain, by uniqueness of the Fraïssé limit. Its kernel is exactly the order-preserving automorphism group. Conversely every element of \(G_d\) induces such a signed permutation. Hence the asserted quotient \(C_2\wr S_d\) is exact; \(G_d\) is a finite union of closed cosets of \(\operatorname{Aut}(\mathcal M_d)\).

**2. Which quotient elements fix the base?** Write \(\pi_j\) for the order of the \(m\) fixed parameter labels along coordinate \(j\). A signed coordinate permutation can lift to an element fixing \(A\) pointwise precisely when, for every output coordinate \(i\), its input ranking is \(\pi_i\) or the reversed list \(\operatorname{rev}(\pi_i)\), according to that coordinate's sign. Sufficiency follows from homogeneity: the transformed parameter tuple has the same complete order diagram, so an ordinary automorphism carries it back to \(A\). Necessity follows by restricting the transformed orders to \(A\). For \(m\ge2\), no ranking equals its reversal, and so signs are forced by the permutation of coordinates. Exactly the coordinate permutations preserving each unoriented ranking class survive; the quotient is \(\prod_i S_{r_i}\). For \(m=1\), both orientations agree on the single point, leaving all signs and all coordinate permutations.

**3. Exact one-type count.** Over \(A\), a new point of \(\mathcal M_d\) is determined, up to \(\operatorname{Aut}(\mathcal M_d)_A\), by one of the \(m+1\) open insertion slots in each coordinate. Every slot vector is realized, and each has infinitely many realizations, by the free extension property. Choose for each unoriented ranking class a canonical ranking list. If a coordinate has the reverse ranking, replace its slot index \(j\) by \(m-j\). After this normalization, the surviving signed-coordinate permutations simply permute the \(r_i\) slot indices inside each class. Therefore a one-type is exactly one multiset of size \(r_i\) from \(m+1\) slots for each class, giving \(\binom{m+r_i}{r_i}\) choices, independently. For \(m=1\), independent sign flips act transitively on the \(2^d\) slot vectors, leaving one type. For \(m=0\), the transitivity of the underlying homogeneous structure gives one type.

**4. Minima, maxima and all equality cases.** For fixed \(m\ge2\), let \(f(r)=\binom{m+r}{r}\), \(f(0)=1\). The ratio \(f(r)/f(r-1)=(m+r)/r\) is strictly decreasing for positive \(r\). Therefore replacing occupied multiplicities \(a>b+1\) by \(a-1,b+1\) strictly increases the product, and splitting a positive block into two positive blocks also strictly increases it: \(f(a)f(b)>f(a+b)\) for \(a,b\ge1\). (For the last inequality compare the products of ratios \(f(j)/f(j-1)\) for \(j=1,\ldots,a\) and \(j=b+1,\ldots,a+b\).) Thus the unique minimizing occupancy pattern has one block of size \(d\), while the maximizing occupancy over at most \(K=m!/2\) classes uses the most balanced possible sizes, namely \(K-s\) blocks of size \(q\) and \(s\) of size \(q+1\). The values are the displayed formulas; all occupancy patterns occur because the \(d\) linear orders are freely and independently prescribed on an \(m\)-element set.

**5. Sharp parameter threshold.** By Step 2, the residual signed-coordinate quotient is trivial exactly when all positive occupancy sizes equal one. This can occur precisely when the number \(K=m!/2\) of available unoriented rankings is at least \(d\). The one-point base leaves all signed symmetries, so taking the least \(m\ge2\) proves the threshold.

## Verification
A standalone Python 3 checker, `verify_multiorder.py`, constructs the actual admissible signed-coordinate group actions on finite slot vectors, enumerates their orbit sets, and compares the resulting counts and group orders with the closed formulas. It checks orientation-flipped representatives separately. The reported run tested \(987\) independent parameter-pattern/action instances and \(14\) minimum/maximum configurations for \(1\le m\le4\) and listed dimensions up to \(4\), ending with `ALL_CHECKS_PASS`. This tests examples; the all-parameter result rests on the proof above.

## Relationship to prior work
Cameron (2002) introduces the two-order representation of a permutation, the universal homogeneous case, and the open higher-multiorder classification question. Linman and Pinsker (2014/2018) analyze the reducts and signed order operations for the **two-order** random permutation. Braunfeld and Simon (arXiv:1807.07110, 2018; revised 2020) classify homogeneous structures with finitely many linear orders and describe the primitive generic multiorder situation. None of those inspected primary statements supplies the arbitrary-dimensional finite-base multinomial-multiset type formula, its sharp global extremizers, or its factorial parameter threshold. The present result concerns one specified natural intermediate symmetry group; it neither refines nor challenges the full classification theorems.

## Limitations
All counts are for nonalgebraic **one-types**, not higher tuple types or full reduct lattices. The extremal theorem identifies occupancy patterns, not the number of labeled realizations of each pattern. The novelty comparison does not eliminate implicit or unindexed earlier derivations of the multiset orbit argument. No independent mathematical audit has been performed.

## References
1. P. J. Cameron, *Homogeneous Permutations*, Electronic Journal of Combinatorics 9(2), R2 (2002), DOI: 10.37236/1674; first public date recorded as 2002-10-31. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i2r2/pdf/
2. J. Linman and M. Pinsker, *Permutations on the Random Permutation*, arXiv:1405.4297, https://arxiv.org/pdf/1405.4297
3. S. Braunfeld and P. Simon, *The classification of homogeneous finite-dimensional permutation structures*, arXiv:1807.07110, https://arxiv.org/pdf/1807.07110
