# Cross-height nullity for finite weak-order pseudospheres
## Finding
Let \(h,k\ge 2\) with \(h\ne k\). Let \(P=A_1\oplus\cdots\oplus A_h\) and \(Q=B_1\oplus\cdots\oplus B_k\) be finite weak orders, where every level \(A_i\) and \(B_j\) is an antichain of cardinality at least two and every point of a lower level is below every point of a higher level. Then every continuous map \(f:P\to Q\) is homotopic, as a map of finite spaces, to a constant map. More strongly, for every \(f\) there is a fence in the pointwise-ordered finite mapping space \(Q^P\) from \(f\) to a constant map using at most three comparability edges. Consequently \(Q^P\) is path connected and the unbased finite-space homotopy set \([P,Q]\) is a singleton.

## Assumptions and scope
A finite \(T_0\)-space is identified with its specialization poset. Here \(P=A_1\oplus\cdots\oplus A_h\) means that each \(A_i\) is an antichain and every point of \(A_i\) is below every point of \(A_j\) whenever \(i<j\); \(Q\) is defined similarly. Every level has at least two points. A continuous map is therefore exactly an order-preserving map. The mapping space \(Q^P\) carries the compact-open topology, equivalently the pointwise order: \(f\le g\) when \(f(x)\le g(x)\) for every \(x\in P\).

A fence is a finite zigzag of pointwise comparisons. Barmak--Minian's finite-space formulation of Stong's criterion says that two maps are homotopic exactly when they lie in the same fence component of \(Q^P\). The proof below is entirely inside this finite mapping space.

## Proof
Write \(\lambda(y)=j\) for \(y\in B_j\). For a map \(f:P\to Q\), call \(B_t\) occupied when \(f(P)\cap B_t\ne\varnothing\).

First suppose some occupied level satisfies \(f(P)\cap B_t=\{z}\}\). Define \(g:P\to Q\) by
\[
g(x)=\begin{cases}
z,&\lambda(f(x))\le t,\\
f(x),&\lambda(f(x))>t.
\end{cases}
\]
If \(x\le y\) in \(P\), order preservation of \(f\) shows that either both images lie at levels at most \(t\), or both lie above \(t\), or the first lies at or below \(t\) and the second above it. In the three cases \(g(x)\le g(y)\). Thus \(g\) is a map, and pointwise
\[
f\le g\ge c_z,
\]
where \(c_z\) is the constant map. Hence \(f\) is null-homotopic through a two-edge fence.

Now assume that every occupied target level contains at least two distinct image points. Suppose some source level \(A_i\) is sent to more than one target level, and let \(t\) be the least level met by \(f(A_i)\). Then \(f(A_i)\cap B_t\) contains at least two distinct points. Indeed, if another source level also meets \(B_t\), cross-level order preservation forces its point in \(B_t\) to equal every point of \(f(A_i)\cap B_t\); therefore distinct points in the occupied level \(B_t\) must already occur in \(f(A_i)\cap B_t\).

Choose \(u\in f(A_i)\) with \(\lambda(u)>t\), and choose one value \(z_0\in f(A_i)\cap B_t\). Modify \(f\) only on \(A_i\): every \(x\in A_i\) with \(f(x)\in B_t\) and \(f(x)\ne z_0\) is sent to \(u\), while all other values are unchanged. Call the new map \(g\). Because \(u\) was already an image of the same source level, every image of a lower source level lies below \(u\) and every image of a higher source level lies above \(u\); hence \(g\) is order preserving. Also \(f\le g\). After the modification, \(g(P)\cap B_t=\{z_0}\}\), so the first paragraph gives a two-edge fence from \(g\) to a constant. Therefore \(f\) reaches a constant in at most three comparability edges.

It remains to consider the case in which every source level \(A_i\) is mapped into one target level and every occupied target level contains at least two image points. Write \(f(A_i)\subseteq B_{t_i}\). If \(i<j\), then \(t_i<t_j\): equality would require every point of the nonconstant image \(f(A_i)\) to be below every point of the nonconstant image \(f(A_j)\) inside one antichain, which is impossible. Thus
\[
t_1<t_2<\cdots<t_h.
\]
If \(h>k\), such a strict level injection cannot exist, so one of the preceding two null-homotopy cases must occur.

Suppose \(h<k\). Choose a target level \(B_t\) omitted by \(t_1,\ldots,t_h\), and choose \(z\in B_t\). If \(t<t_1\), replace all values on \(A_1\) by \(z\); the resulting map \(g\) satisfies \(g\le f\). If \(t>t_h\), replace all values on \(A_h\) by \(z\); then \(f\le g\). Finally, if \(t_i<t<t_{i+1}\), replace all values on \(A_i\) by \(z\); again \(f\le g\). In every case the replacement is order preserving and the new image meets \(B_t\) in the singleton \(\{z}\}\). The first paragraph therefore contracts \(g\), giving a fence of at most three edges from \(f\) to a constant.

Thus every map \(P\to Q\) is null-homotopic when \(h\ne k\). All constant maps lie in one component because the comparability graph of the nontrivial weak order \(Q\) is connected. Hence \(Q^P\) is path connected and \([P,Q]\) has one element.

## Verification
The symbolic argument above is the proof for all allowed heights and level sizes. The accompanying program `artifacts/verify.py` independently reconstructs weak orders from their level sizes, exhaustively enumerates every order-preserving map in seven unequal-height test pairs, constructs the same singleton/spanning/gap fence prescribed by the proof, and checks every comparison and every intermediate map. The cases include both directions of height mismatch, nonuniform level sizes, a four-level target, a four-level source, and the spanning-level branch with source sizes \((4,2)\) and target sizes \((2,2,2)\).

Across the seven cases the program checks \(11{,}435\) order-preserving maps and prints `VERIFY_OK`. The finite enumeration is only a stress test; it is not used to infer the all-heights theorem.

## Relationship to prior work
Barmak--Minian identify finite \(T_0\)-spaces with posets and, in their treatment of strong homotopy, state that the finite function space \(Y^X\) is the pointwise poset of order-preserving maps and that two maps are homotopic exactly when they are joined by a fence. Their earlier work gives the canonical finite sphere models and places the problem in MSC 55P10/55P15. Speed studies the poset \(\operatorname{Hom}(P,Q)\) for arbitrary finite posets, but the inspected paper computes its Möbius function and related enumerative quantities, not its fence components. Later pseudosphere literature identifies these ordered joins of discrete levels and records that their order complexes are wedges of spheres, but does not give the cross-height finite mapping-space classification proved here.

The two-point-source-level special case is contained in the present theorem. The new structural step is the spanning-level perturbation: when a source level has more than two points and crosses target levels, all but one value in its lowest occupied target level can be pushed to an already used higher value, forcing a singleton target level and hence a short contraction. This removes the binary source-level restriction and yields the uniform three-edge fence bound.

## Limitations
Equal source and target heights are excluded; in that regime level-preserving maps with nonconstant restrictions can form non-null isolated mapping-space points. The theorem also assumes every level has at least two points; allowing singleton levels changes the pseudosphere structure and can change the mapping-space behavior. The statement concerns direct homotopy of maps between the finite spaces themselves and does not classify maps after subdivision, replacement by weakly equivalent spaces, or passage to arbitrary classical representatives.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first submitted 2006-11-06.
2. J. A. Barmak and E. G. Minian, *Strong homotopy types, nerves and collapses*, arXiv:0907.2954v1; see Proposition 4.1 for the pointwise mapping-space fence criterion.
3. T. P. Speed, *On the Möbius function of \\(\\operatorname{Hom}(P,Q)\\)*, Bulletin of the Australian Mathematical Society 29 (1984), 39--46, DOI 10.1017/S0004972700021250.
4. *Pseudospheres: combinatorics, topology and distributed systems*, Journal of Applied and Computational Topology, DOI 10.1007/s41468-023-00162-5; see the characterization of pseudospheres as ordinal sums of trivial posets and the wedge-of-spheres discussion.
