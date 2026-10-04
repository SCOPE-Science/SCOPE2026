# Height mismatch nullifies maps from binary-level finite pseudospheres
## Finding
Let \(h,k\ge 2\) with \(h\ne k\). Let \(P=A_1\oplus\cdots\oplus A_h\) be a finite weak order with \(|A_i|=2\) for every \(i\), and let \(Q=B_1\oplus\cdots\oplus B_k\) be a finite weak order with \(|B_j|\ge2\) for every \(j\). Then every continuous map \(f:P\to Q\) is homotopic, as a map of finite spaces, to a constant map. Equivalently, the finite function space \(Q^P\) is path connected. In particular, for the canonical minimal finite sphere models \(X_n=(S^0)^{\circledast(n+1)}\) and \(X_m=(S^0)^{\circledast(m+1)}\) with \(n,m\ge1\) and \(n\ne m\), the finite-space homotopy set \([X_n,X_m]\) is a singleton.

For maps between canonical minimal finite sphere models, this is stronger than saying that the induced map between order-complex spheres is classically null-homotopic: the map itself contracts inside the finite target through a zigzag of pointwise-comparable finite-space maps.

## Assumptions and scope
Write \(P=A_1\oplus\cdots\oplus A_h\), where every source level \(A_i\) is a two-point antichain, and \(Q=B_1\oplus\cdots\oplus B_k\), where every target level \(B_j\) is an antichain of size at least two. The ordinal sum order means every point of an earlier level is below every point of a later level. Continuity is therefore the same as order preservation.

The restriction \(k\ge2\) keeps the target connected. The theorem concerns unbased finite-space homotopy. It does not assert that arbitrary weak-order sources with larger source levels have the same property.

## Proof
Let \(f:P\to Q\) be order preserving, and let \(R=f(P)\subseteq Q\) with the induced order.

First suppose some occupied target level meets \(R\) in exactly one point \(c\). Then \(R\) is contractible as a finite space. Indeed, define \(u:R\to R\) by sending every point in an occupied level below the level of \(c\) to \(c\), while fixing \(c\) and every point above it. This map is order preserving, the identity satisfies \(1_R\le u\) pointwise, and the constant map \(c_R\) satisfies \(c_R\le u\). Stong's pointwise-comparability criterion therefore gives \(1_R\simeq u\simeq c_R\). Since \(f\) factors through \(R\), the original map is null-homotopic.

It remains to consider the case in which every occupied target level contains at least two image points. Fix a source level \(A_i=\{{a_i,a_i'}\}\). Its two images cannot lie in two different target levels. If \(f(a_i)\) lies in \(B_r\) and \(f(a_i')\) lies in \(B_s\) with \(r<s\), then no other source level can contribute a second point to \(B_r\): an earlier source level would have to map a point below the distinct point \(f(a_i)\) in the same antichain \(B_r\), while a later source level would have to receive the image \(f(a_i')\in B_s\) below a point of \(B_r\). Both are impossible. Thus \(B_r\cap R\) would be a singleton, contrary to assumption. Hence the two points of every \(A_i\) map to one common target level, and because that occupied level is not a singleton, their images are distinct.

If \(i<i'\), the target levels receiving \(A_i\) and \(A_{i'}\) must be strictly ordered. Equality is impossible because two distinct image points in one target antichain cannot both be below two distinct image points in that same antichain. Consequently the no-singleton case uses exactly \(h\) distinct target levels, one for each source level.

If \(h>k\), this is impossible, so the singleton-level case already proves null-homotopy.

If \(h<k\), choose an unoccupied target level \(B_t\) and a point \(b\in B_t\). Let \(i_R:R\hookrightarrow Q\) be inclusion and define \(v:R\to Q\) by sending every point of \(R\) below level \(t\) to \(b\), while fixing every point of \(R\) above level \(t\). Then \(i_R\le v\) pointwise and the constant map \(b_R\) satisfies \(b_R\le v\). Hence \(i_R\simeq b_R\). Since \(f=i_R\circ f_R\), the map \(f\) is null-homotopic.

This proves the claim for every unequal pair of heights.

## Verification
The proof is symbolic. The accompanying checker independently enumerates all order-preserving maps in six representative unequal-height cases, including nonuniform target levels, verifies the singleton-level versus omitted-level dichotomy for every enumerated map, and computes the comparability graph of the finite function space. In every case the graph has one connected component.

The tested source/target level-size pairs are \((2,2)\to(2,3,2)\), \((2,2)\to(3,2,3)\), \((2,2,2)\to(3,2)\), \((2,2,2)\to(2,3)\), \((2,2)\to(2,2,2,2)\), and \((2,2,2,2)\to(2,3)\). These finite checks are sanity tests only; they are not used to extrapolate the theorem.

## Relationship to prior work
Stong proved that homotopy classes of maps between finite spaces are the path components of the finite function space and, in particular, that pointwise-comparable maps are homotopic. Barmak and Minian identified \((S^0)^{\circledast(n+1)}\) as the unique \(2n+2\)-point minimal finite model of \(S^n\), and the ordinal-sum/order-complex correspondence is standard in finite-space topology.

A previously established direct-map rigidity result for the same minimal sphere models showed only that the induced simplicial map between the order-complex spheres is classically null-homotopic when the dimensions differ. That statement does not imply finite-space null-homotopy, because finite-space homotopy is strictly finer than homotopy after passage to order complexes in general. The present claim proves the stronger finite-space contraction and extends it to every weak-order target with at least two points per level.

Targeted searches for formulations using finite mapping spaces, ordinal sums, weak orders, pseudospheres, unequal heights, and minimal finite sphere models located no theorem giving this cross-height finite-space nullity. The closest published-finding corpus record concerns interval-endomorphism algebra dimensions of weak orders, not homotopy classes of maps.

## Limitations
The two-point hypothesis on every source level is essential to the proof: a larger source antichain can place multiple image points in more than one target level without creating a singleton occupied level. No claim is made for arbitrary source weak orders. Equal-height maps are also excluded; non-null isolated classes do occur there. The result concerns direct maps of finite models and does not preclude nontrivial classical sphere maps after subdivision or enlargement.

## References
1. R. E. Stong, “Finite topological spaces,” Transactions of the American Mathematical Society 123 (1966), 325–340, DOI 10.1090/S0002-9947-1966-0195042-2.
2. J. A. Barmak and E. G. Minian, “Minimal Finite Models,” arXiv:math/0611156, first submitted 2006-11-06; Journal of Homotopy and Related Structures 2 (2007), 127–140.
