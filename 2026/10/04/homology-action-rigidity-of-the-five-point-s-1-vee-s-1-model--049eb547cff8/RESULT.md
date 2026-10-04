# Homology-action rigidity of the five-point \(S^1\vee S^1\) model
## Finding
Let \(P\) be the five-point \(T_0\)-space with minima \(a,b\), maxima \(x,y,z\), and all six relations \(a,b<x,y,z\). With the cycle basis \(c_1=[a,x]-[b,x]+[b,y]-[a,y]\), \(c_2=[a,x]-[b,x]+[b,z]-[a,z]\) of \(H_1(P;\mathbb Z)\cong\mathbb Z^2\), its \(197\) continuous self-maps induce exactly \(31\) endomorphisms: the zero matrix; the \(18\) rank-one matrices \(\pm u v^{\mathsf T}\) with \(u\in\{(1,0)^{\mathsf T},(0,1)^{\mathsf T},(1,-1)^{\mathsf T}\}\) and \(v\in\{(1,0)^{\mathsf T},(0,1)^{\mathsf T},(1,1)^{\mathsf T}\}\); and the \(12\) integral isometries of \(q(s,t)=s^2+st+t^2\). Exactly \(12\) self-maps induce an isomorphism on \(H_1\), and these are precisely the \(12\) homeomorphisms.

Equivalently, the image of the direct self-map monoid on first homology is
\[
\{0\}\cup
\{\pm u v^{\mathsf T}\}\cup
O(q;\mathbb Z),
\]
where the middle set uses
\[
u\in\{(1,0)^{\mathsf T},(0,1)^{\mathsf T},(1,-1)^{\mathsf T}\},
\qquad
v\in\{(1,0)^{\mathsf T},(0,1)^{\mathsf T},(1,1)^{\mathsf T}\},
\]
and
\[
q(s,t)=s^2+st+t^2.
\]
The three pieces have respectively \(1\), \(18\), and \(12\) matrices.

## Assumptions and scope
Finite \(T_0\)-spaces are identified with their specialization posets, so continuous maps are exactly order-preserving maps. The poset \(P\) has two minimal points \(a,b\), three maximal points \(x,y,z\), and every minimal point lies below every maximal point. Its order complex is the graph \(K_{2,3}\), hence it is a five-point minimal finite model of \(S^1\vee S^1\).

Orient every edge of the order complex from a minimal point to a maximal point. We use
\[
c_1=[a,x]-[b,x]+[b,y]-[a,y],
\qquad
c_2=[a,x]-[b,x]+[b,z]-[a,z].
\]
These form a basis of \(H_1(P;\mathbb Z)\cong\mathbb Z^2\).

The statement concerns direct self-maps of this fixed five-point finite space. It does not assert that larger finite models, subdivisions, or arbitrary CW representatives of \(S^1\vee S^1\) have the same realization restriction.

## Proof
The order complex is \(K_{2,3}\), with five vertices and six edges, so its first Betti number is \(6-5+1=2\). The displayed cycles are independent and span the cycle lattice.

A continuous self-map is an order-preserving function \(f:P\to P\). There are only \(5^5=3125\) set maps. The exact count \(197\) can also be checked without enumeration. If \(U(p)\) denotes the principal upper set of \(p\), then after choosing the two images \(f(a),f(b)\), each of \(f(x),f(y),f(z)\) can be chosen independently in \(U(f(a))\cap U(f(b))\). The ordered pairs of images of \(a,b\) contribute
\[
2\cdot4^3+2\cdot3^3+12\cdot1^3+3\cdot1^3
=128+54+12+3
=197.
\]

For any order-preserving \(f\), the induced simplicial chain map sends an oriented edge \([u,v]\) to \([f(u),f(v)]\) when the two images are distinct and to zero when they coincide. Since the order complex is one-dimensional, the image of each \(c_i\) is again a cycle. In the chosen basis, the coefficients of \([b,y]\) and \([b,z]\) recover its coordinates, so every induced \(H_1\)-matrix is computed directly over the integers.

The embedded verifier examines all \(3125\) set maps, keeps exactly the \(197\) order-preserving ones, computes their two-by-two integral homology matrices, and checks equality with the following explicit set:
\[
\{0\}
\cup
\{\pm u v^{\mathsf T}:
u\in\{(1,0)^{\mathsf T},(0,1)^{\mathsf T},(1,-1)^{\mathsf T}\},
v\in\{(1,0)^{\mathsf T},(0,1)^{\mathsf T},(1,1)^{\mathsf T}\}\}
\cup
O(q;\mathbb Z).
\]
The first part has one matrix. The outer-product part has \(18\) distinct rank-one matrices. For the positive definite form \(q(s,t)=s^2+st+t^2\), the verifier enumerates its six primitive vectors of value \(1\) and obtains exactly \(12\) integral isometries. Thus there are exactly \(31\) matrices.

The multiplicities by homological rank are exact:
\[
149\text{ maps have zero action},\qquad
36\text{ maps have rank-one action},\qquad
12\text{ maps have rank-two action}.
\]
Each rank-one matrix occurs twice; each integral \(q\)-isometry occurs once.

A homeomorphism of \(P\) independently permutes the two minima and the three maxima, so
\[
\operatorname{Aut}(P)\cong S_2\times S_3
\]
and there are \(12\) homeomorphisms. The verifier checks directly that their \(12\) induced matrices are exactly \(O(q;\mathbb Z)\), and that no other order-preserving map has determinant \(\pm1\). Therefore a self-map induces an isomorphism on \(H_1(P;\mathbb Z)\) if and only if it is a homeomorphism.

## Verification
The embedded `verify.py` is a dependency-free exhaustive certificate. It reconstructs the poset and cycle basis, enumerates every set map, filters order-preserving maps, computes the induced integral chain maps, checks the exact \(31\)-matrix structural description, and independently compares homology invertibility with the homeomorphism condition.

A successful replay prints:
`VERIFY_OK`
`continuous_self_maps=197`
`distinct_H1_matrices=31`
`matrix_types=1_zero+18_rank_one+12_q_isometries`
`map_rank_distribution=149_zero_action+36_rank_one_action+12_isomorphism_action`
`homeomorphisms=12`
`H1_isomorphism_iff_homeomorphism=yes`

## Relationship to prior work
Barmak--Minian characterize minimal finite models of finite graphs and explicitly identify a five-point model of \(S^1\vee S^1\). Their full text gives the minimal-model classification but does not state a self-map census or an induced-homology realization semigroup. McCord's classical correspondence identifies the weak homotopy information carried by order complexes, but it likewise does not imply the direct-map realization classification above.

For the ordinary CW bouquet \(S^1\vee S^1\), arbitrary integral two-by-two matrices occur on \(H_1\): map each circle generator to a loop word with the desired abelianized exponent vector. The five-point finite model therefore has the same weak homotopy type but a sharply smaller direct self-map image on homology, consisting of only \(31\) matrices.

Targeted searches using the five-point model, \(K_{2,3}\), bouquet/wedge aliases, exact counts, self-map monoids, homology actions, and the hexagonal form found no source stating this exact \(197\)-map/\(31\)-matrix classification. Search failure is supporting evidence only, not a proof of novelty.

## Limitations
The result is exact for the specified five-point poset and its direct continuous self-maps. It does not classify homotopy classes of maps between arbitrary finite models, nor does it constrain direct maps on larger models. The novelty assessment is based on targeted database and literature comparison and cannot exclude every obscure or unindexed source.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first submitted 2006-11-06; later *Journal of Homotopy and Related Structures* 2 (2007), 127--140.
2. M. C. McCord, *Singular homology groups and homotopy groups of finite topological spaces*, *Duke Mathematical Journal* 33 (1966), 465--474, DOI 10.1215/S0012-7094-66-03352-7.
3. R. E. Stong, *Finite topological spaces*, *Transactions of the American Mathematical Society* 123 (1966), 325--340, DOI 10.1090/S0002-9947-1966-0195042-2.
