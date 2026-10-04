# Homotopy versus weak homotopy classification of finite weak orders
## Finding
Let \(W(r_1,\ldots,r_h)=A_1\oplus\cdots\oplus A_h\) be the ordinal sum of nonempty antichains, with \(|A_i|=r_i\). Then \(W\) is contractible exactly when some level is a singleton. If every \(r_i\ge2\), its order complex satisfies
\[
|\mathcal K(W)|\simeq \bigvee^{\prod_i(r_i-1)} S^{h-1}.
\]
For two such weak orders \(W(r_1,\ldots,r_h)\) and \(W(s_1,\ldots,s_k)\), ordinary homotopy equivalence of the finite spaces is completely classified by the following alternatives: either both spaces have a singleton level, in which case both are contractible, or neither has a singleton level and \(h=k\) together with \(r_i=s_i\) for every \(i\). Their weak homotopy types are equal exactly when either both are contractible, or neither has a singleton level and
\[
h=k,\qquad \prod_i(r_i-1)=\prod_j(s_j-1).
\]
Thus weak homotopy collapses the full ordered level data to height plus one product, whereas ordinary finite-space homotopy retains the entire ordered level-size vector.

A concrete smallest-style witness of this information loss is
\[
W(2,4,2)\quad\text{and}\quad W(2,2,4).
\]
Both are eight-point cores and both order complexes are homotopy equivalent to \(\bigvee^3 S^2\), but the finite spaces are not homotopy equivalent because their ordered level-size vectors differ.

## Assumptions and scope
A finite weak order here means a finite \(T_0\)-space whose specialization poset is a lexicographic, equivalently ordinal, sum of nonempty antichains indexed by a finite chain. The level decomposition is intrinsic: two elements lie in the same level exactly when they are equal or incomparable, and the levels inherit a total order. Weak homotopy type is used in the standard finite-space sense, equivalently the homotopy type of the order complex through McCord's weak equivalence.

The classification covers every finite weak order. The wedge formula is stated in the noncontractible case \(r_i\ge2\); if a singleton level occurs, the finite space itself is contractible, not merely weakly contractible.

## Proof
First suppose \(A_j=\{c\}\) is a singleton level. Define \(u:W\to W\) by \(u(x)=c\) for points in levels at or below \(A_j\), and \(u(x)=x\) for points above \(A_j\). This map is order preserving. Pointwise, \(\operatorname{id}_W\le u\), because every point below \(c\) is sent upward to \(c\), and \(\operatorname{const}_c\le u\), because every point fixed above \(c\) lies above \(c\). Comparable continuous maps between finite spaces are homotopic, so
\[
\operatorname{id}_W\simeq u\simeq \operatorname{const}_c.
\]
Hence \(W\) is contractible.

Now assume every \(r_i\ge2\). A point in a non-top level has at least the two incomparable points of the next level as minimal strict upper bounds, so its strict upper set has no minimum. Dually, a point in a non-bottom level has at least two incomparable maximal strict lower bounds. At the top and bottom the corresponding strict sets are empty. Therefore no point is up beat or down beat, so \(W\) is a Stong core. In particular it is not contractible.

A nonempty chain in \(W\) contains at most one point from each level, and every choice of at most one point from each of several distinct levels is a chain. Hence
\[
\mathcal K(W)=D_{r_1}*\cdots*D_{r_h},
\]
where \(D_r\) is the discrete simplicial complex on \(r\) vertices. For any nonempty finite complex \(X\) and \(r\ge2\), choosing one vertex \(v_0\in D_r\) writes \(D_r*X\) as \(r\) cones on \(X\) with common base. Collapsing the contractible cone \(v_0*X\) identifies the common base to a point and gives
\[
D_r*X\simeq \bigvee^{r-1}\Sigma X.
\]
Iterating this identity gives
\[
|\mathcal K(W)|\simeq \bigvee^{\prod_i(r_i-1)}S^{h-1}.
\]

If two noncontractible weak orders are homotopy equivalent as finite spaces, both are cores, so Stong's theorem forces the homotopy equivalence to be a homeomorphism. A poset isomorphism preserves the intrinsic totally ordered incomparability classes, hence preserves each level size in order. Thus \(h=k\) and \(r_i=s_i\) for all \(i\); the converse is immediate from an isomorphism level by level.

For weak homotopy type, McCord's theorem reduces the question to the homotopy types of the two order complexes. In the noncontractible case these are wedges of a positive number of spheres. Two such wedges are homotopy equivalent only if the sphere dimensions agree and the top reduced homology ranks agree. Those invariants are respectively \(h-1\) and \(\prod_i(r_i-1)\). Equality of them is also sufficient because both complexes are then homotopy equivalent to the same wedge of spheres. This proves the weak classification. The contractible alternative was handled in the first paragraph.

## Verification
The proof is structural and does not depend on finite enumeration. A separate standard-library checker, `verify.py`, was nevertheless used as a stress test. It enumerates order-complex simplices and computes mod-two boundary ranks for the level vectors \( (2,2)\), \( (3,3)\), \( (2,2,2)\), \( (2,4,2)\), \( (2,2,4)\), and \( (3,2,3,2)\); it also checks directly that these spaces have no beat points. The computed top Betti ranks are respectively \(1,4,1,3,3,4\), exactly \(\prod_i(r_i-1)\), with no intermediate reduced homology. The checker separately verifies the explicit comparator contraction for singleton examples, including an interior singleton level, and verifies the pair \(W(2,4,2)\), \(W(2,2,4)\) has the same weak signature but different ordered level vectors. The replay output ends with `VERIFY_OK`.

These computations are finite consistency checks only; they are not used as proof of the quantified theorem.

## Relationship to prior work
Barmak and Minian's finite-space framework records the two ingredients used here: deletion of beat points gives strong deformation retracts and finite spaces without beat points are cores rigid under homotopy equivalence; McCord's order-complex construction represents weak homotopy type. Their 2006 work also supplies minimal finite sphere models built from two-point antichain levels.

Mosquera-Lois studies the current Whitehead problem for minimal finite models and constructs weakly equivalent, non-homotopy-equivalent cores. In the inspected full text, the ordinal-sum antichain family appears in the special two-point sphere model, but no classification was found for arbitrary level sizes. The present statement instead gives an exact family-wide comparison: ordinary homotopy type is the ordered level vector, while weak homotopy type is only the pair consisting of height and the product \(\prod_i(r_i-1)\).

Pouzet and Zaguia describe finite weak orders as lexicographic sums of antichains indexed by a linear order. Their work concerns perpendicular orders and does not address finite-space homotopy or weak homotopy classification.

## Limitations
The result concerns finite weak orders, equivalently ordinal sums of antichains. It does not claim a classification for arbitrary finite posets, arbitrary complete multipartite graphs viewed without orientation, or Coxeter-theoretic weak orders. It classifies weak homotopy type in the zigzag sense standard for finite spaces; it does not assert that every pair with the same weak type admits a weak homotopy equivalence map in each direction. The literature comparison cannot exclude an equivalent older statement under terminology not found by the searches; this is the principal residual originality risk.

## References
1. J. A. Barmak and E. G. Minian, *Simple Homotopy Types and Finite Spaces*, arXiv:math/0611158, first public version 2006-11-06.
2. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first public version 2006-11-06.
3. D. Mosquera-Lois, *Whitehead's theorem for minimal finite models*, arXiv:2608.06176, first public version 2026-08-06.
4. M. Pouzet and I. Zaguia, *Weak orders admitting a perpendicular linear order*, Discrete Mathematics 307 (2007), 97-107, DOI 10.1016/j.disc.2006.05.038.
