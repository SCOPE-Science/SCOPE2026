# Edge-regular primitive-idempotent graphs of finite full matrix rings

## Finding

For a prime power \(q\) and an integer \(n\ge3\), let
\[
R=M_n(\mathbb F_q).
\]
Let \(P_{n,q}\) denote the subgraph of the indecomposability graph of \(R\) induced by the primitive idempotents. Write
\[
[m]_q=\frac{q^m-1}{q-1}.
\]

Then \(P_{n,q}\) is edge-regular. More precisely,
\[
|V(P_{n,q})|=q^{n-1}[n]_q,
\]
every vertex has degree
\[
k=q^{n-2}[n-1]_q,
\]
and every adjacent pair has exactly
\[
\lambda=q^{n-3}[n-2]_q
\]
common neighbors.

It follows that
\[
|E(P_{n,q})|
=
\frac{q^{2n-3}[n]_q[n-1]_q}{2}
\]
and
\[
T(P_{n,q})
=
\frac{q^{3n-6}[n]_q[n-1]_q[n-2]_q}{6},
\]
where \(T(P_{n,q})\) is the number of triangles.

Equivalently, the graph induced by the neighborhood of every vertex is \(\lambda\)-regular on \(k\) vertices.

When \(n=3\), one has \(\lambda=1\). Hence every vertex neighborhood is a perfect matching and every edge lies in a unique triangle. In this dimension the triangles are in bijection with the unordered noncollinear triples of points of \(\operatorname{PG}(2,q)\).

## Assumptions and scope

The field \(\mathbb F_q\) is arbitrary finite, so \(q\) is any prime power. The matrix size satisfies \(n\ge3\).

The indecomposability graph is the graph introduced for rings with the descending chain condition on idempotents: its nontrivial idempotents are adjacent when they are orthogonal and at least one cross-corner is nonzero. For the simple ring \(M_n(\mathbb F_q)\), two primitive idempotents are adjacent exactly when they are orthogonal.

Only the subgraph induced by primitive idempotents is considered here. No claim is made about common-neighbor counts among higher-rank idempotents in the full indecomposability graph.

## Proof

A primitive idempotent of \(M_n(\mathbb F_q)\) has rank one. Such an idempotent \(e\) is uniquely determined by its image \(P=\operatorname{im}(e)\), a projective point, and its kernel \(H=\ker(e)\), a projective hyperplane with
\[
P\not\subset H.
\]
Conversely, every nonincident point-hyperplane pair \((P,H)\) determines the projection onto \(P\) along \(H\). Thus the primitive idempotents are exactly the antiflags
\[
(P,H),\qquad P\not\subset H,
\]
of \(\operatorname{PG}(n-1,q)\).

For nonzero idempotents \(e,f\) in a full matrix ring one has \(eRf\ne0\): choose a nonzero vector in \(\operatorname{im}(f)\), send it by a suitable matrix to a vector not killed by \(e\), and compose. Hence for primitive idempotents the indecomposability adjacency condition reduces to
\[
ef=fe=0.
\]

If \(e\leftrightarrow(P,H)\) and \(f\leftrightarrow(Q,M)\), then
\[
ef=0\iff Q\subset H,
\qquad
fe=0\iff P\subset M.
\]
Therefore
\[
(P,H)\sim(Q,M)
\iff
Q\subset H\ \text{and}\ P\subset M.
\]

There are \([n]_q\) projective points. For a fixed point \(P\), the number of hyperplanes not containing \(P\) is
\[
[n]_q-[n-1]_q=q^{n-1}.
\]
Consequently
\[
|V(P_{n,q})|=q^{n-1}[n]_q.
\]

Fix \((P,H)\). To choose a neighbor \((Q,M)\), first choose a point \(Q\subset H\), giving \([n-1]_q\) choices. Then choose a hyperplane \(M\) through \(P\) but not through \(Q\). The number of hyperplanes through \(P\) is \([n-1]_q\), while the number through the projective line \(\langle P,Q\rangle\) is \([n-2]_q\). Hence there are
\[
[n-1]_q-[n-2]_q=q^{n-2}
\]
choices for \(M\). Thus
\[
k=q^{n-2}[n-1]_q.
\]

Now let \((P,H)\) and \((Q,M)\) be adjacent. Then \(P\ne Q\), \(H\ne M\),
\[
Q\subset H,\qquad P\subset M,
\]
and no point of \(H\cap M\) lies on the projective line \(\langle P,Q\rangle\). Indeed,
\[
H\cap\langle P,Q\rangle=\{Q\},
\qquad
M\cap\langle P,Q\rangle=\{P\}.
\]

A common neighbor \((S,N)\) must satisfy
\[
S\subset H\cap M
\]
and
\[
P,Q\subset N,
\qquad
S\not\subset N.
\]
There are \([n-2]_q\) choices for \(S\subset H\cap M\). For each such \(S\), the hyperplanes containing \(\langle P,Q\rangle\) number \([n-2]_q\), while those also containing \(S\) number \([n-3]_q\). Therefore the number avoiding \(S\) is
\[
[n-2]_q-[n-3]_q=q^{n-3}.
\]
Hence every adjacent pair has exactly
\[
\lambda=q^{n-3}[n-2]_q
\]
common neighbors.

Regularity gives
\[
|E(P_{n,q})|
=
\frac{|V|k}{2}
=
\frac{q^{2n-3}[n]_q[n-1]_q}{2}.
\]
Each edge belongs to exactly \(\lambda\) triangles, and each triangle contributes three edges, so
\[
T(P_{n,q})
=
\frac{|E|\lambda}{3}
=
\frac{q^{3n-6}[n]_q[n-1]_q[n-2]_q}{6}.
\]

For a fixed vertex \(v\), a neighbor \(w\) has exactly \(\lambda\) common neighbors with \(v\), all of which lie in the graph induced by \(N(v)\). Thus every local graph is \(\lambda\)-regular.

If \(n=3\), then
\[
\lambda=q^0[1]_q=1.
\]
So every local graph is a perfect matching and every edge is contained in exactly one triangle.

Finally, in \(\operatorname{PG}(2,q)\), a triangle with vertices
\[
(P,H_P),\quad(Q,H_Q),\quad(S,H_S)
\]
forces
\[
H_P=QS,\qquad H_Q=PS,\qquad H_S=PQ.
\]
The antiflag condition says exactly that \(P,Q,S\) are noncollinear. Conversely every unordered noncollinear triple \(\{P,Q,S\}\) yields precisely this triangle. This proves the stated bijection.

## Verification

The standalone `verify.py` artifact constructs projective points and hyperplanes directly over prime fields, forms the antiflag graph using the cross-incidence criterion, and checks vertex count, degree, adjacent common-neighbor count, edge count, triangle count, and every local degree.

It was replayed from its packaged path on
\[
(n,q)\in\{(3,2),(3,3),(3,5),(4,2),(5,2)\}.
\]

Exact replay output:

```text
n=3 q=2 N=28 k=6 lambda=1 E=84 T=28
n=3 q=3 N=117 k=12 lambda=1 E=702 T=234
n=3 q=5 N=775 k=30 lambda=1 E=11625 T=3875
n=4 q=2 N=120 k=28 lambda=6 E=1680 T=3360
n=5 q=2 N=496 k=120 lambda=28 E=29760 T=277760
VERIFY_OK
```

The finite checks corroborate the formulas. The theorem for arbitrary prime powers is established by the projective counting proof, not by enumeration.

## Relationship to prior work

Cvetko-Vah and Dolžan introduced indecomposability graphs of rings and proved, for full matrix rings, that primitive-idempotent adjacency is exactly orthogonality. Their matrix-ring analysis establishes connectivity and diameter behavior but does not state the finite-field degree, common-neighbor, local-graph, edge, or triangle formulas above.

The rank-one idempotent graph here has a projective reformulation on nonincident point-hyperplane pairs. Searches under primitive-idempotent, orthogonality, antiflag, cross-incidence, common-neighbor, and edge-regular terminology did not locate a statement equivalent to the formulas above.

Later work on idempotent/nilpotent graphs of \(2\times2\) matrix rings uses a different vertex set and a different zero-product-with-transpose adjacency. It does not imply the present \(n\ge3\) primitive-idempotent result.

## Limitations

The result concerns primitive idempotents only. The full indecomposability graph also contains higher-rank nontrivial idempotents, whose local intersection numbers are not addressed.

The proof is specific to full matrix rings over finite fields. Matrix rings over finite local rings require additional kernel/image data and are not covered.

A residual literature risk is that the same antiflag cross-incidence orbital graph may occur in finite-geometry or permutation-group literature under a terminology not exposed by the searches performed. No such equivalent statement was located, and the ring-theoretic source itself does not state these parameters.

## References

1. K. Cvetko-Vah and D. Dolžan, “Indecomposability Graphs of Rings,” *Bulletin of the Australian Mathematical Society* 77 (2008), 151–159. DOI: 10.1017/S0004972708000154. Published online 1 February 2008.
2. A. Lande, A. Khairnar, and I. Gutman, “The zero-divisor graph of \(2\times2\) matrix ring and its energies,” *Filomat* 39 (2025), 7559–7570. DOI: 10.2298/FIL2522559L.
