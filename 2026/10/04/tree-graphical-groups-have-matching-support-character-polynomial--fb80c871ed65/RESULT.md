# Tree graphical groups have matching-support character polynomials

## Finding

Let \(T\) be a tree on \(n\) vertices and let \(q\) be an odd prime power. For each edge subset
\[
S\subseteq E(T),
\]
write
\[
\nu(S)
\]
for the matching number of the spanning forest
\[
(V(T),S).
\]
Define
\[
\mathcal R_T(q,z)
=
\sum_{S\subseteq E(T)}
(q-1)^{|S|}z^{\nu(S)}.
\]

Then the irreducible-character degree distribution of the graphical group
\[
\mathbf G_T(\mathbf F_q)
\]
is given exactly by
\[
\boxed{
\operatorname{ch}(T,i;q)
=
q^{n-2i}[z^i]\mathcal R_T(q,z).
}
\]
Thus Rossmann's character-enumeration question has a polynomial answer for every tree, extending the previously recorded path family to all tree shapes.

The polynomial \(\mathcal R_T\) has a direct rooted-tree recursion. Root \(T\) at a vertex \(r\). For a rooted subtree \(T_v\) and a support \(S\subseteq E(T_v)\), let
\[
\mu_v(S)
\]
be its matching number and let
\[
\mu_v^{0}(S)
\]
be the maximum size of a matching using no edge incident with the root \(v\). Then
\[
\mu_v(S)-\mu_v^{0}(S)\in\{0,1\}.
\]
Define
\[
P_v^{(\delta)}(q,z)
=
\sum_{\substack{S\subseteq E(T_v)\\
\mu_v(S)-\mu_v^{0}(S)=\delta}}
(q-1)^{|S|}z^{\mu_v(S)},
\qquad
\delta\in\{0,1\}.
\]
For a leaf,
\[
P_v^{(0)}=1,
\qquad
P_v^{(1)}=0.
\]
If \(v\) has children
\[
c_1,\ldots,c_k,
\]
then
\[
\boxed{
P_v^{(0)}
=
\prod_{j=1}^{k}
\left(
P_{c_j}^{(0)}+qP_{c_j}^{(1)}
\right)
}
\]
and
\[
\boxed{
P_v^{(1)}
=
z\left(
q^k
\prod_{j=1}^{k}
\left(
P_{c_j}^{(0)}+P_{c_j}^{(1)}
\right)
-
P_v^{(0)}
\right).
}
\]
At the root,
\[
\boxed{
\mathcal R_T(q,z)
=
P_r^{(0)}+P_r^{(1)}.
}
\]

The linear-algebraic mechanism is field-independent: if \(F\) is any forest and every edge of \(F\) receives a nonzero weight in any field, then the associated alternating weighted adjacency matrix has rank
\[
\boxed{2\nu(F).}
\]

As a simple non-path example, for the star
\[
K_{1,m}
\]
one obtains
\[
\mathcal R_{K_{1,m}}(q,z)
=
1+(q^m-1)z,
\]
and hence
\[
\operatorname{ch}(K_{1,m},0;q)=q^{m+1},
\]
\[
\operatorname{ch}(K_{1,m},1;q)=q^{m-1}(q^m-1),
\]
with no other character degrees.

## Assumptions and scope

The graphical group is the class-two group scheme attached to a graph in the sense used by Rossmann and by Rossmann--Voll.

The character formula is stated for odd \(q\), exactly the range in which the O'Brien--Voll Kirillov-orbit formula applies to these class-two graphical groups.

The rank identity for weighted forests itself is valid over arbitrary fields, including characteristic \(2\).

The statistic
\[
\nu(S)
\]
is the maximum matching size of the support forest, not the number of matchings of a prescribed size.

## Proof

Let
\[
B_T(y)
\]
be the alternating commutator matrix of the graphical group, with one coordinate
\[
y_e\in\mathbf F_q
\]
for each edge \(e\) of \(T\). Its support graph is the forest
\[
F_y=(V(T),\{e:y_e\ne0\}).
\]

We first prove the weighted-forest rank identity. Let \(F\) be a forest whose present edges have nonzero weights. If \(F\) has no edges, both its matching number and the matrix rank are zero.

Otherwise choose a leaf \(v\) with neighbour \(u\), and let the nonzero weight on \(uv\) be \(a\). In a basis beginning with \(u,v\), the only nonzero entry in the \(v\)-row outside the \(u\)-column is absent. For every other vertex \(w\), replace its basis vector by
\[
e_w-\frac{B(u,w)}{a}e_v.
\]
This congruence eliminates every matrix entry between \(u\) and vertices other than \(v\), without changing the matrix on the remaining vertices. Hence the matrix is congruent to the direct sum of
\[
\begin{pmatrix}
0&a\\
-a&0
\end{pmatrix}
\]
and the weighted alternating matrix of
\[
F-\{u,v\}.
\]
Therefore
\[
\operatorname{rank}B_F
=
2+\operatorname{rank}B_{F-\{u,v\}}.
\]

A maximum matching of a forest may always be chosen to contain the edge from a leaf to its neighbour: if the neighbour is already matched elsewhere, replace that edge by the leaf edge. Consequently
\[
\nu(F)
=
1+\nu(F-\{u,v\}).
\]
Induction proves
\[
\operatorname{rank}B_F=2\nu(F).
\]

Now fix a tree \(T\). For an edge assignment \(y\), the rank of \(B_T(y)\) depends only on its support:
\[
\operatorname{rank}B_T(y)
=
2\nu(F_y).
\]
For a fixed support \(S\), exactly
\[
(q-1)^{|S|}
\]
edge assignments have support \(S\). Therefore the number of specialisations of rank \(2i\) is
\[
\rho_i(T;q)
=
\sum_{\substack{S\subseteq E(T)\\
\nu(S)=i}}
(q-1)^{|S|}
=
[z^i]\mathcal R_T(q,z).
\]

For graphical groups,
\[
|\mathbf G_T(\mathbf F_q)/\mathbf G_T(\mathbf F_q)'|
=
q^n.
\]
The O'Brien--Voll character-rank formula therefore gives, for odd \(q\),
\[
\operatorname{ch}(T,i;q)
=
q^{n-2i}\rho_i(T;q),
\]
which is the displayed character formula.

It remains to prove the rooted recursion. For a rooted support forest in \(T_v\), forcing \(v\) to remain unmatched makes the child subtrees independent, so
\[
\mu_v^0
=
\sum_j\mu_{c_j}.
\]
For every child,
\[
\mu_{c_j}-\mu_{c_j}^0\in\{0,1\}.
\]
Allowing \(v\) to be matched improves the optimum by one exactly when at least one child edge \(vc_j\) is present and the child is in state \(0\).

To remain in state \(0\), a child in state \(0\) must have the edge \(vc_j\) absent, while a child in state \(1\) may have that edge absent or present. The latter two edge choices have total weight
\[
1+(q-1)=q.
\]
This yields
\[
P_v^{(0)}
=
\prod_j
(P_{c_j}^{(0)}+qP_{c_j}^{(1)}).
\]

If edge choices are unrestricted, every parent-child edge contributes total weight \(q\), so the generating polynomial with exponent
\[
\sum_j\mu_{c_j}
\]
is
\[
q^k\prod_j(P_{c_j}^{(0)}+P_{c_j}^{(1)}).
\]
Subtracting the state-\(0\) cases leaves exactly the supports for which the root gains one matching edge; multiplying by \(z\) records that increment. Hence
\[
P_v^{(1)}
=
z\left(
q^k\prod_j(P_{c_j}^{(0)}+P_{c_j}^{(1)})
-
P_v^{(0)}
\right).
\]
At the root, both states are allowed, so
\[
\mathcal R_T=P_r^{(0)}+P_r^{(1)}.
\]

## Verification

The included checker independently verifies the theorem in two ways.

For several nonisomorphic trees, including a path, a star, a branched six-vertex tree, and a seven-vertex binary tree, and for
\[
q=3,5,
\]
it enumerates every edge assignment, forms the corresponding alternating matrix, computes its rank by finite-field Gaussian elimination, and checks that the rank is exactly twice the matching number of the support.

Independently, it enumerates all support edge sets and evaluates
\[
\sum_S(q-1)^{|S|}z^{\nu(S)},
\]
then compares this polynomial coefficient-by-coefficient with the rooted recursion.

Finally, it checks that the resulting character counts
\[
q^{n-2i}[z^i]\mathcal R_T(q,z)
\]
satisfy the degree-squared identity
\[
\sum_i
\operatorname{ch}(T,i;q)q^{2i}
=
|\mathbf G_T(\mathbf F_q)|
=
q^{n+|E(T)|}.
\]

The checker returns `VERIFY_OK`.

The finite computations verify representative instances; the infinite family is proved symbolically above.

## Relationship to prior work

Rossmann explicitly asks how the numbers of irreducible characters of each degree of graphical groups depend on the finite-field order. In the same discussion, he records polynomial answers only for edgeless graphs, paths, and complete graphs, and notes that the general rank-count approach may be difficult.

The theorem here gives a uniform answer for every tree. The key simplification is that after an edge-weight specialisation, the support remains a forest, and the alternating-matrix rank collapses exactly to twice the support matching number. The rooted recursion then computes the entire rank distribution.

O'Brien and Voll provide the general Kirillov-orbit formula converting commutator-matrix rank counts into irreducible-character counts. Their theorem is the representation-theoretic bridge used here; it does not enumerate the tree support ranks.

Skew-rank literature relates ranks of oriented-graph matrices to matching numbers and proves general bounds involving the cycle rank. Those results support the relevance of matching number to acyclic skew matrices, but they concern fixed real oriented adjacency matrices rather than all finite-field edge-weight specialisations and do not derive graphical-group character multiplicities.

Targeted searches using graphical groups, trees, character degrees, skew-adjacency ranks, weighted forests, matching numbers, and the rooted recurrence did not locate the displayed all-tree character formula.

## Limitations

The character formula is stated only for odd finite fields because the representation-theoretic conversion uses the O'Brien--Voll class-two Kirillov framework in that range.

The rooted recursion is an exact algorithmic formula rather than a single closed product for arbitrary tree shapes.

The matching-support polynomial is not the ordinary matching polynomial: it weights each edge support by the maximum matching size of the resulting forest.

For graphs containing cycles, alternating-matrix rank may depend on cancellations among different matching monomials; the forest argument no longer applies directly.

Failed searches do not prove novelty.

## References

1. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1, first public version 12 July 2021; *Bulletin of the London Mathematical Society* 54 (2022), 1923–1943, DOI 10.1112/blms.12665. Primary MSC 20D15.
2. E. A. O'Brien and C. Voll, “Enumerating classes and characters of \(p\)-groups,” *Transactions of the American Mathematical Society* 367 (2015), 7775–7796, DOI 10.1090/tran/6276.
3. X. Ma, D. Wong, and F. Tian, “Skew-rank of an oriented graph in terms of matching number,” *Linear Algebra and its Applications* 495 (2016), 242–255, DOI 10.1016/j.laa.2016.01.036.
