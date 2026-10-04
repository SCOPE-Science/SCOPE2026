# Extraspecial commuting graphs are perfect exactly in rank one

## Finding

Let \(G\) be an extraspecial \(p\)-group of order
\[
p^{2r+1},
\qquad
r\ge1,
\]
where \(p\) is any prime. Then the commuting graph of \(G\) is perfect if and only if
\[
\boxed{r=1.}
\]

For \(r=1\), deleting the center gives
\[
\boxed{
\Gamma^\circ(G)
\cong
(p+1)K_{p(p-1)}.
}
\]
Consequently the commuting graph on all elements is
\[
\boxed{
\Gamma(G)
\cong
K_p\vee\bigl((p+1)K_{p(p-1)}\bigr),
}
\]
and is perfect.

For every \(r\ge2\), the noncentral commuting graph contains an explicit induced \(5\)-cycle. If
\[
e_1,f_1,e_2,f_2,\ldots
\]
is a symplectic basis of \(G/Z(G)\), take
\[
v_1=e_1,
\qquad
v_2=e_2,
\qquad
v_3=f_1,
\qquad
v_4=f_1+f_2,
\qquad
v_5=e_1-e_2+f_2.
\]
Then
\[
\langle v_i,v_{i+1}\rangle=0
\]
for cyclic indices modulo \(5\), while every nonconsecutive pairing is nonzero. Thus any representatives of these five quotient vectors induce
\[
C_5
\]
in the commuting graph. Hence the graph is not perfect.

The construction works in characteristic \(2\) as well: there the minus sign equals a plus sign, and all five nonconsecutive pairings remain equal to the nonzero field element.

## Assumptions and scope

The commuting graph \(\Gamma(G)\) has vertex set \(G\), with distinct elements adjacent when they commute. Write
\[
\Gamma^\circ(G)=\Gamma(G)[G\setminus Z(G)]
\]
for the induced noncentral commuting graph.

A graph is perfect if every induced subgraph has clique number equal to chromatic number. Adding universal vertices preserves perfectness, so
\[
\Gamma(G)
\]
is perfect if and only if
\[
\Gamma^\circ(G)
\]
is perfect.

For an extraspecial \(p\)-group,
\[
Z(G)=G'=\Phi(G)
\]
has order \(p\), and
\[
V=G/Z(G)
\]
is an elementary abelian group of dimension \(2r\) over \(\mathbf F_p\). The commutator map defines a nondegenerate alternating bilinear form
\[
\langle xZ(G),yZ(G)\rangle=[x,y]\in Z(G)\cong\mathbf F_p.
\]
Thus two group elements commute exactly when their quotient vectors are orthogonal.

The theorem covers both extraspecial isomorphism types for each order and includes \(p=2\).

## Proof

Let
\[
V=G/Z(G)
\]
with its nondegenerate alternating commutator form.

First suppose
\[
r=1.
\]
Then \(V\) is two-dimensional. For every nonzero vector \(v\),
\[
v^\perp
\]
has dimension one and contains \(v\), hence
\[
v^\perp=\langle v\rangle.
\]
Therefore two nonzero quotient vectors are orthogonal exactly when they lie on the same one-dimensional subspace.

There are
\[
\frac{p^2-1}{p-1}=p+1
\]
one-dimensional subspaces of \(V\). For each such line there are \(p-1\) nonzero quotient vectors, and every quotient vector represents a coset of \(Z(G)\) containing \(p\) group elements. Hence each line yields a clique of size
\[
p(p-1),
\]
with no edges between distinct line-cliques. Thus
\[
\Gamma^\circ(G)\cong(p+1)K_{p(p-1)}.
\]
A disjoint union of cliques is perfect. The \(p\) central elements are universal and form a clique, so adjoining them preserves perfectness.

Now suppose
\[
r\ge2.
\]
Choose a symplectic basis
\[
e_1,f_1,e_2,f_2,\ldots,e_r,f_r
\]
with
\[
\langle e_i,f_i\rangle=1
\]
and all cross-pairings between distinct hyperbolic pairs equal to zero.

Define
\[
v_1=e_1,
\quad
v_2=e_2,
\quad
v_3=f_1,
\quad
v_4=f_1+f_2,
\quad
v_5=e_1-e_2+f_2.
\]
The consecutive pairings are
\[
\langle v_1,v_2\rangle=0,
\]
\[
\langle v_2,v_3\rangle=0,
\]
\[
\langle v_3,v_4\rangle=0,
\]
\[
\langle v_4,v_5\rangle
=
\langle f_1,e_1\rangle
+
\langle f_2,-e_2\rangle
=
-1+1=0,
\]
and
\[
\langle v_5,v_1\rangle=0.
\]

For the five nonconsecutive pairs one obtains
\[
\langle v_1,v_3\rangle=1,
\qquad
\langle v_1,v_4\rangle=1,
\]
\[
\langle v_2,v_4\rangle=1,
\qquad
\langle v_2,v_5\rangle=1,
\]
and
\[
\langle v_3,v_5\rangle=-1.
\]
All are nonzero in every characteristic. In characteristic \(2\), of course,
\[
-1=1.
\]

Choose arbitrary representatives
\[
x_i\in G
\]
of the five cosets \(v_i\). Commutation depends only on the quotient vectors, so the induced graph on
\[
\{x_1,x_2,x_3,x_4,x_5\}
\]
is exactly a \(5\)-cycle.

By the Strong Perfect Graph Theorem, a graph containing an induced odd cycle of length at least five is not perfect. Hence
\[
\Gamma^\circ(G)
\]
and therefore
\[
\Gamma(G)
\]
are not perfect for every
\[
r\ge2.
\]

## Verification

The included checker independently constructs the standard symplectic form on
\[
\mathbf F_p^{2r}
\]
for
\[
p=2,3,5,7.
\]

For rank one it builds the noncentral element-level blow-up: vertices are pairs
\[
(v,z),
\]
where
\[
v\in\mathbf F_p^2\setminus\{0\},
\qquad
z\in\mathbf F_p,
\]
and adjacency is orthogonality of the quotient vectors. It verifies exactly
\[
p+1
\]
connected components, each a complete graph of order
\[
p(p-1).
\]

For rank two it evaluates all ten pairings among the five displayed vectors and verifies that the zero pairings are exactly the five edges of a cycle.

The checker returns `VERIFY_OK`.

The computation is illustrative only. The theorem is proved symbolically for every prime and every rank.

## Relationship to prior work

Cameron's survey *Graphs defined on groups* formulates the broad problem of determining which finite groups have perfect commuting graph. Its first public arXiv version appeared in 2021 and is classified under MSC \(20D60\).

Arvind and Cameron's 2022 paper gives the structural input used here for extraspecial groups: the quotient by the center is a symplectic vector space and the commuting relation is orthogonality. It also describes the order-\(p^3\) commuting graph as \(p+1\) cliques meeting in the center.

Britnell and Gill classify quasisimple groups with perfect commuting graph and give general structural restrictions. Extraspecial groups have no quasisimple components, so their classification theorem does not settle this family.

Ma, Cameron, and Maslova later study cograph, chordal, split, and threshold commuting graphs. Their full text restates the perfect-graph question, notes the quasisimple work, and gives the standard forbidden-subgraph characterization, but does not state an extraspecial perfectness classification.

The rank-one positive case is compatible with established results on CA-groups and with the known order-\(p^3\) clique decomposition. The new content claimed here is the sharp all-rank extraspecial boundary and the uniform explicit induced \(C_5\) for every rank at least two, including characteristic two.

Targeted searches for “extraspecial p-group commuting graph perfect”, “induced C5”, “odd hole”, “symplectic orthogonality graph”, and cograph/chordal variants did not locate this classification.

## Limitations

The theorem concerns extraspecial groups only. It does not classify perfect commuting graphs for arbitrary special, semi-extraspecial, or class-two \(p\)-groups.

The proof uses the standard symplectic description of extraspecial groups; it does not distinguish the two extraspecial isomorphism types because their commuting relations have the same symplectic quotient geometry.

The rank-one positive case is not asserted to be new independently of prior CA-group and order-\(p^3\) results.

Failed literature searches do not prove novelty. An equivalent statement could appear in finite-geometry language for symplectic orthogonality graphs without being phrased as a commuting-graph theorem.

## References

1. P. J. Cameron, “Graphs defined on groups,” arXiv:2102.11177v1, first public version 22 February 2021; *International Journal of Group Theory* 11 (2022), 53–107. MSC 20D60.
2. V. Arvind and P. J. Cameron, “Recognizing the Commuting Graph of a Finite Group,” arXiv:2206.01059v1, first public version 2 June 2022.
3. X. Ma, P. J. Cameron, and N. V. Maslova, “Forbidden subgraphs in commuting graphs of finite groups,” arXiv:2305.07301v1, first public version 12 May 2023.
4. J. R. Britnell and N. Gill, “Perfect commuting graphs,” arXiv:1309.2237v1, *Journal of Group Theory* 20 (2017), 71–102.
