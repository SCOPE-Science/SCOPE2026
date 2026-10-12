# Exact labeled census and face enumerator for six-vertex point hypergraphs
## Finding
Let \(K\) be an algebraically closed field of characteristic \(0\). A six-variable skew polynomial algebra determines a 3-uniform point hypergraph on the labeled vertex set \([6]\), with a face for each coordinate 2-plane contained in its point scheme. There are exactly \(50{,}214\) labeled point hypergraphs.

Define the face enumerator
\[
P(t)=\sum_{\mathcal H} t^{|\mathcal H|},
\]
where the sum runs over all labeled point hypergraphs on \([6]\). Then
\[
P(t)=1+20t+190t^2+1080t^3+3885t^4+8844t^5+12510t^6+10800t^7+6870t^8+3540t^9+1568t^{10}+440t^{11}+330t^{12}+60t^{13}+60t^{14}+15t^{16}+t^{20}.
\]
In particular, there are no such hypergraphs with exactly \(15\), \(17\), \(18\), or \(19\) faces.

Under the natural relabeling action of \(S_6\), the \(50{,}214\) hypergraphs form exactly \(174\) orbits. If \(N_s\) denotes the number of orbits of size \(s\), the nonzero values are
\[
\begin{aligned}
&(N_1,N_6,N_{10},N_{12},N_{15},N_{20},N_{30},N_{45})=(2,1,1,1,6,3,2,4),\\
&(N_{60},N_{72},N_{90},N_{120},N_{180},N_{240},N_{360},N_{720})=(13,2,15,7,28,1,61,27).
\end{aligned}
\]

## Assumptions and scope
The field hypothesis is exactly the characteristic-zero algebraically closed setting of arXiv:2610.05311v1. Vertices are labeled by \([6]\), and faces are the triples corresponding to coordinate 2-planes contained in the point scheme. The count is therefore a labeled refinement of the published six-vertex classification, not a count of algebra isomorphism classes or of parameter points in the realizing moduli spaces.

## Proof
Theorem 5.16 of arXiv:2610.05311v1 states that a 3-uniform hypergraph on six vertices is a point hypergraph if and only if it satisfies the tetrahedron condition and is not an octahedral obstruction. For a labeled hypergraph on \([6]\), encode its face set by a \(20\)-bit mask, one bit for each element of \(\binom{[6]}{3}\). The tetrahedron condition is equivalent to requiring that, for each of the \(15\) four-element subsets of \([6]\), the induced mask contains a number of faces different from \(3\).

Exhausting all \(2^{20}=1{,}048{,}576\) masks gives exactly \(50{,}334\) masks satisfying the tetrahedron condition. The explicit obstruction in Remark 5.17 has face set
\[
\{124,135,145,236,246,356,456\}.
\]
Its orbit under \(S_6\) has exactly \(120\) distinct labeled members, all with seven faces and all satisfying the tetrahedron condition. Theorem 5.16 therefore gives
\[
50{,}334-120=50{,}214
\]
labeled point hypergraphs.

Counting the surviving masks by Hamming weight gives the displayed polynomial \(P(t)\). As a separate quotient check, repeatedly take one surviving mask and remove its full \(S_6\)-orbit. This yields the displayed orbit-size profile; its orbit count is \(174\), and its weighted sum is
\[
\sum_s sN_s=50{,}214.
\]
The orbit count \(174\) independently matches Remark 5.17 of arXiv:2610.05311v1.

## Verification
The accompanying `verify.py` performs the complete \(2^{20}\)-mask scan, constructs the full \(S_6\)-orbit of the published obstruction directly from all \(720\) permutations, computes the face distribution, and then quotients the surviving set into \(S_6\)-orbits without external canonical-labeling software. It checks \(50{,}334\) tetrahedron-condition masks, an obstruction orbit of size \(120\), \(50{,}214\) point hypergraphs, the full face enumerator, \(174\) relabeling orbits, and the orbit-size profile before printing `VERIFY_OK`.

The computation is exhaustive over a finite set. It is not being used to prove Theorem 5.16; that theorem is the mathematical classification input. The computation only derives the exact finite census from that theorem.

## Relationship to prior work
Higashitani and Ueyama prove the six-vertex criterion and state that there are exactly \(174\) point hypergraphs up to isomorphism. They do not state the labeled total, the face-number enumerator, or the orbit-size profile. Belmans, De Laet, and Le Bruyn previously reported \(175\) \(S_6\)-equivalence classes of adequate collections in dimension five and suggested all could be realized; the 2026 theorem identifies the single octahedral obstruction that removes one class. The present census uses that corrected criterion and refines the isomorphism-class count into exact labeled multiplicities and face statistics.

## Limitations
The statement is restricted to six vertices and to the characteristic-zero algebraically closed setting of the classification theorem. It does not enumerate realization parameters inside the moduli varieties attached to each point hypergraph. The exact census is conditional only on the published Theorem 5.16 as its structural classification input; the finite enumeration itself is independently reproducible from the supplied code.

## References
1. A. Higashitani and K. Ueyama, *Hypergraphs associated to skew polynomial algebras and surface triangulations*, arXiv:2610.05311v1, especially Definitions 1.2--1.3, Theorem 5.16, and Remark 5.17.
2. P. Belmans, K. De Laet, and L. Le Bruyn, *The point variety of quantum polynomial rings*, arXiv:1509.07312v1, especially Section 3 and the discussion of the \(175\) \(S_6\)-equivalence classes.
