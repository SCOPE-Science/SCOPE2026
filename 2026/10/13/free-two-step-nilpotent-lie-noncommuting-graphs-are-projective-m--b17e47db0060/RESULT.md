# Free two-step nilpotent Lie noncommuting graphs are projective multipartite graphs

## Finding

Let
\[
N_r(q)=V\oplus\Lambda^2V
\]
be the free two-step nilpotent Lie algebra on an \(r\)-dimensional vector space \(V\) over \(\mathbf F_q\), where
\[
r\ge2.
\]
Its bracket is
\[
[v,w]=v\wedge w,
\qquad
[V,\Lambda^2V]=0.
\]
Put
\[
c=\binom r2,
\qquad
s=q^c(q-1),
\qquad
k=\frac{q^r-1}{q-1}.
\]

Then
\[
Z(N_r(q))=\Lambda^2V,
\]
and the element-level noncommuting graph is
\[
\boxed{
\mathcal N(N_r(q))
\cong
K_{\underbrace{s,\ldots,s}_{k\text{ parts}}}.
}
\]

The \(k\) independent parts are indexed by projective points
\[
\ell\in\mathbf P(V).
\]
For a one-dimensional subspace \(\ell\le V\), the corresponding part is
\[
P_\ell=(\ell\oplus\Lambda^2V)\setminus\Lambda^2V.
\]
Every such part has cardinality
\[
|P_\ell|=(q-1)q^c=s.
\]

Consequently,
\[
\boxed{\alpha(\mathcal N(N_r(q)))=s}
\]
and
\[
\boxed{
\omega(\mathcal N(N_r(q)))
=
\chi(\mathcal N(N_r(q)))
=
k.
}
\]

The extremizers are exact. Every maximum independent set is one \(P_\ell\), equivalently the noncentral part of the maximal abelian subalgebra
\[
\ell\oplus\Lambda^2V.
\]
Every optimal \(k\)-coloring is, up to permutation of the colors, the projective-point partition
\[
\{P_\ell:\ell\in\mathbf P(V)\}.
\]

The graph is regular of degree
\[
\boxed{s(k-1)}
\]
and has adjacency spectrum
\[
\boxed{
\left\{
(s(k-1))^1,
(-s)^{k-1},
0^{k(s-1)}
\right\}.
}
\]
Its full graph automorphism group is
\[
\boxed{
\operatorname{Aut}(\mathcal N(N_r(q)))
\cong
S_s\wr S_k,
}
\]
with the usual imprimitive action on the \(k\) equal parts.

Thus the noncommuting graph of the universal free class-two Lie algebra collapses completely to projective incidence at the level of one-dimensional quotient directions.

## Assumptions and scope

The element-level noncommuting graph has vertex set
\[
N_r(q)\setminus Z(N_r(q))
\]
and joins two vertices exactly when their Lie bracket is nonzero.

The theorem holds for every prime power \(q\) and every generator rank \(r\ge2\), including characteristic \(2\).

The claim is about the free two-step nilpotent Lie algebra itself. Quotients can identify independent wedge coordinates and therefore can have additional commuting pairs.

## Proof

Write
\[
L=N_r(q)=V\oplus W,
\qquad
W=\Lambda^2V.
\]
By construction,
\[
W\le Z(L).
\]
Conversely, take
\[
x=v+z,
\qquad
v\in V,
\quad
z\in W.
\]
If \(v\ne0\), choose \(w\in V\) not contained in the one-dimensional space \(\mathbf F_qv\). Then
\[
[x,w]=v\wedge w\ne0.
\]
Hence no element with nonzero \(V\)-component is central, so
\[
Z(L)=W.
\]

Now let
\[
x=v+z,
\qquad
y=w+z',
\]
be noncentral vertices, so \(v,w\ne0\). Their bracket is
\[
[x,y]=v\wedge w.
\]
In an exterior square,
\[
v\wedge w=0
\]
if and only if \(v,w\) are linearly dependent. Therefore
\[
[x,y]=0
\iff
\mathbf F_qv=\mathbf F_qw.
\]

For each projective point \(\ell\in\mathbf P(V)\), define
\[
P_\ell=(\ell\oplus W)\setminus W.
\]
Two vertices commute exactly when they lie in the same \(P_\ell\). Hence each \(P_\ell\) is an independent part and every two vertices in different parts are adjacent.

The number of projective points is
\[
k=\frac{q^r-1}{q-1}.
\]
For fixed \(\ell\), there are \(q-1\) nonzero choices of the quotient vector in \(\ell\) and \(q^c\) independent choices of the central component, so
\[
|P_\ell|=q^c(q-1)=s.
\]
This proves the complete multipartite formula.

For an equal-part complete multipartite graph with \(k\) parts of size \(s\), the maximum independent sets are exactly the parts, while a clique contains at most one vertex from each part and can choose one from every part. Therefore
\[
\alpha=s,
\qquad
\omega=k.
\]
The same partition is a \(k\)-coloring, so
\[
\chi=k.
\]
Any proper coloring with only \(k\) colors must assign different colors to different parts because every cross-part pair is adjacent; hence every optimal coloring is the part partition up to color permutation.

Each part \(P_\ell\) is
\[
(\ell\oplus W)\setminus W.
\]
The subalgebra \(\ell\oplus W\) is abelian. It is maximal abelian because adding any element whose quotient direction is not \(\ell\) creates a nonzero wedge bracket. Thus maximum independent sets are exactly the noncentral parts of maximal abelian subalgebras containing the center.

Every vertex is adjacent to all vertices outside its own part, giving degree
\[
s(k-1).
\]

For the spectrum, order vertices part by part. The adjacency matrix is
\[
(J_k-I_k)\otimes J_s.
\]
The matrix \(J_k-I_k\) has eigenvalues
\[
k-1
\]
once and
\[
-1
\]
with multiplicity \(k-1\), while \(J_s\) has eigenvalues \(s\) once and \(0\) with multiplicity \(s-1\). Tensoring gives
\[
(s(k-1))^1,
\qquad
(-s)^{k-1},
\qquad
0^{k(s-1)}.
\]

Finally, every graph automorphism may independently permute vertices within each part and may arbitrarily permute the equal-sized parts. Therefore
\[
\operatorname{Aut}(\mathcal N(L))\cong S_s\wr S_k.
\]

## Verification

The included checker constructs the free two-step algebra directly for
\[
(q,r)=(2,2),(2,3),(3,2),(3,3),(5,2).
\]
It represents central coordinates in the standard wedge basis and computes every bracket explicitly.

For every unordered pair of noncentral elements, it checks that the bracket vanishes exactly when their quotient vectors define the same projective point. It then verifies the predicted number and size of parts, regular degree, independence number, clique/chromatic count from the multipartite decomposition, and the spectral multiplicity identities.

For example,
\[
N_3(2)
\]
has \(56\) graph vertices and decomposes as
\[
K_{8,8,8,8,8,8,8}.
\]
The predicted spectrum is
\[
\{48^1,(-8)^6,0^{49}\}.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the all-\(q\), all-\(r\) theorem.

## Relationship to prior work

Cagliero, Gutiérrez Frez, and Szechtman use the standard model
\[
L(V)=V\oplus\Lambda^2V
\]
for the free two-step nilpotent Lie algebra and record the defining bracket explicitly. Their work is representation-theoretic and does not study finite noncommuting graphs.

Ruan, Sheng, and Zhang later give the same free two-step model over an arbitrary field in their study of Hall Lie algebras arising from one-cyclic perfect complexes. This confirms that the exterior-square model used here is valid uniformly over finite fields.

Chareh Khah Moghaddam, Erfanian, and Shamsaki introduced the element-level noncommuting graph for finite-dimensional Lie algebras and study general graph properties and reconstruction questions. Their full searchable preprint contains no occurrence of “free” or “multipartite” and does not identify the free two-step family.

The new statement combines these two strands: freeness makes
\[
[v,w]=0
\]
exactly the projective dependence relation, so the whole graph, all extremal independent sets, every optimal coloring, the spectrum, and the automorphism group become explicit.

Targeted semantic and literature searches under free-two-step, exterior-square, projective, commuting/noncommuting, multipartite, and spectrum formulations did not locate this exact theorem.

## Limitations

The complete multipartite structure depends on the freeness of the class-two bracket. In a proper quotient of \(\Lambda^2V\), distinct quotient directions can acquire zero bracket and merge the clean projective pattern.

The theorem determines the graph exactly but does not claim that this graph characterizes the free two-step Lie algebra among all finite Lie algebras.

The graph formula is short once the exterior-square model is written down, so an equivalent observation may exist in finite-geometry or graph-Lie-algebra literature under different terminology.

Failed searches do not prove novelty.

## References

1. L. Cagliero, L. Gutiérrez Frez, and F. Szechtman, “Free 2-step nilpotent Lie algebras and indecomposable modules,” arXiv:1703.06214v1, first public version 17 March 2017; published as “Free 2-step nilpotent Lie algebras and indecomposable representations,” *Communications in Algebra* 46 (2018), 2990–3005, DOI 10.1080/00927872.2017.1404086. MSC 17B10, 17B30.
2. S. Ruan, J. Sheng, and H. Zhang, “Lie algebras arising from 1-cyclic perfect complexes,” arXiv:1705.07307v1, first public version 20 May 2017; *Journal of Algebra* 580 (2021), DOI 10.1016/j.jalgebra.2021.06.030.
3. A. Chareh Khah Moghaddam, A. Erfanian, and A. Shamsaki, “On the non-commuting graph associated to a finite-dimensional Lie algebra,” arXiv:2406.15902v1, first public version 22 June 2024; later published in *Journal of the Indonesian Mathematical Society* 32 (2026), DOI 10.22342/jims.v32i1.1643.
