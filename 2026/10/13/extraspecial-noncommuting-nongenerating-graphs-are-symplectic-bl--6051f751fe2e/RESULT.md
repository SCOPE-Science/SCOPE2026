# Extraspecial noncommuting–nongenerating graphs are symplectic blow-ups

## Finding

Let \(G\) be an extraspecial \(p\)-group of order
\[
p^{1+2n}.
\]
Write
\[
Z=Z(G)=G'=\Phi(G),
\qquad
|Z|=p,
\]
and
\[
V=G/Z\cong \mathbf F_p^{\,2n}.
\]

If
\[
n=1,
\]
then
\[
\boxed{\Xi(G)\text{ is edgeless}.}
\]

If
\[
n\ge2,
\]
then
\[
d(G)=2n>2,
\]
so no pair generates \(G\). Hence
\[
\Xi(G)
\]
is exactly the noncommuting graph on \(G\setminus Z\).

The commutator induces a nondegenerate alternating form
\[
B:V\times V\to\mathbf F_p.
\]
Let
\[
\Sigma_{2n}(p)
\]
be the graph whose vertices are the one-dimensional subspaces of \(V\), with distinct projective points adjacent exactly when they are nonorthogonal under \(B\).

Then
\[
\boxed{
\Xi(G)\cong
\Sigma_{2n}(p)
\bigl[\overline{K}_{p(p-1)}\bigr].
}
\]

Thus each projective point is blown up to an independent set of size
\[
p(p-1).
\]
The two extraspecial isomorphism types of the same order have the same graph.

Put
\[
v=\frac{p^{2n}-1}{p-1}.
\]
The projective base graph is strongly regular with parameters
\[
\boxed{
\left(
v,\,
p^{2n-1},\,
p^{2n-2}(p-1),\,
p^{2n-2}(p-1)
\right).
}
\]

Consequently, for \(n\ge2\), the graph \(\Xi(G)\) has
\[
\boxed{p(p^{2n}-1)}
\]
vertices, is regular of degree
\[
\boxed{p^{2n}(p-1)},
\]
and has diameter \(2\).

Its adjacency spectrum is
\[
\boxed{
\left\{
p^{2n}(p-1)^1,\,
\bigl(p^n(p-1)\bigr)^{(v-1-p^n)/2},\,
\bigl(-p^n(p-1)\bigr)^{(v-1+p^n)/2},\,
0^{\,v(p(p-1)-1)}
\right\}.
}
\]

In particular, the graph is blind to the extraspecial plus/minus type, but its spectrum determines the prime and the symplectic rank. Indeed, if
\[
D=p^{2n}(p-1)
\]
is the valency and
\[
R=p^n(p-1)
\]
is the positive nontrivial eigenvalue, then
\[
\frac{D}{R}=p^n
\]
and
\[
p=1+\frac{D}{(D/R)^2}.
\]
Therefore the spectrum recovers
\[
p,\qquad n,\qquad |G|=p^{1+2n}.
\]

## Assumptions and scope

The graph \(\Xi(G)\) has vertex set
\[
G\setminus Z(G),
\]
and two distinct vertices are adjacent exactly when they do not commute and do not generate \(G\).

The theorem covers every extraspecial finite \(p\)-group, including both isomorphism types and the prime \(2\).

The rank-one case is exceptional because extraspecial groups of order \(p^3\) are two-generated. The symplectic blow-up formula is asserted only for
\[
n\ge2.
\]

## Proof

For an extraspecial group,
\[
\Phi(G)=Z(G)
\]
and
\[
G/\Phi(G)\cong\mathbf F_p^{\,2n}.
\]
Burnside's basis theorem therefore gives
\[
d(G)=2n.
\]

Suppose first that
\[
n=1.
\]
Two noncentral elements \(x,y\) fail to commute exactly when their images
\[
\bar x,\bar y\in V
\]
have nonzero commutator pairing. In a two-dimensional alternating space this means that \(\bar x,\bar y\) are linearly independent. They therefore span
\[
G/\Phi(G),
\]
so Burnside's basis theorem gives
\[
\langle x,y\rangle=G.
\]
Thus every noncommuting pair is generating, and \(\Xi(G)\) has no edges.

Now assume
\[
n\ge2.
\]
Then
\[
d(G)=2n\ge4,
\]
so no two elements generate \(G\). Hence adjacency in \(\Xi(G)\) is simply noncommutation.

Choose a generator \(z\) of \(Z\). Since \(G\) has class \(2\), there is a unique alternating bilinear form
\[
B:V\times V\to\mathbf F_p
\]
such that
\[
[x,y]=z^{B(\bar x,\bar y)}.
\]
Its radical is zero: if
\[
B(\bar x,\bar y)=0
\]
for every \(\bar y\in V\), then \(x\) commutes with all of \(G\), so \(x\in Z\) and \(\bar x=0\).

Therefore
\[
x\sim y
\quad\Longleftrightarrow\quad
B(\bar x,\bar y)\ne0.
\]

All \(p\) elements in one nonzero coset of \(Z\) have the same neighborhood. Moreover, scalar-multiple nonzero vectors are mutually orthogonal, and each projective line contains
\[
p-1
\]
nonzero vectors. Hence one projective point corresponds to
\[
p(p-1)
\]
group vertices, with no edges among them. This proves
\[
\Xi(G)\cong
\Sigma_{2n}(p)
\bigl[\overline{K}_{p(p-1)}\bigr].
\]

It remains to count the base graph.

The number of projective points is
\[
v=\frac{p^{2n}-1}{p-1}.
\]
For a fixed nonzero vector \(x\), its orthogonal hyperplane contains
\[
\frac{p^{2n-1}-1}{p-1}
\]
projective points, including \(\langle x\rangle\). Hence the number of nonorthogonal projective points is
\[
k
=
\frac{p^{2n}-1}{p-1}
-
\frac{p^{2n-1}-1}{p-1}
=
p^{2n-1}.
\]

For two distinct projective points represented by independent vectors \(x,y\), the two linear functionals
\[
B(x,-),\qquad B(y,-)
\]
are independent. The number of vectors nonorthogonal to both is therefore
\[
p^{2n}
-
2p^{2n-1}
+
p^{2n-2}
=
p^{2n-2}(p-1)^2.
\]
Dividing by \(p-1\) gives
\[
p^{2n-2}(p-1)
\]
common projective neighbors. This count is the same whether
\[
B(x,y)
\]
vanishes or not, so
\[
\lambda=\mu=p^{2n-2}(p-1).
\]

The strongly regular identity is therefore
\[
A^2
=
p^{2n-2}I
+
p^{2n-2}(p-1)J
\]
on the orthogonal complement of the all-ones decomposition in the usual way. The two nonprincipal eigenvalues are
\[
p^{n-1}
\quad\text{and}\quad
-p^{n-1}.
\]
Their multiplicities \(f_+\) and \(f_-\) satisfy
\[
f_++f_-=v-1
\]
and, from the zero trace,
\[
p^{2n-1}
+
p^{n-1}(f_+-f_-)=0.
\]
Thus
\[
f_+=\frac{v-1-p^n}{2},
\qquad
f_-=\frac{v-1+p^n}{2}.
\]

Blowing up every vertex to an independent set of size
\[
s=p(p-1)
\]
replaces the base adjacency matrix \(A\) by
\[
A\otimes J_s.
\]
Every base eigenvalue is multiplied by \(s\), and zero acquires the additional multiplicity
\[
v(s-1).
\]
This yields the displayed spectrum.

Finally, the two extraspecial groups of a given order have isometric commutator alternating spaces, so the graph depends only on \(p\) and \(n\), not on the quadratic or exponent data distinguishing the two types.

## Verification

The included checker verifies three independent features.

For the order-\(p^3\) boundary, it constructs the standard extraspecial groups
\[
\operatorname{UT}_3(\mathbf F_2)
\quad\text{and}\quad
\operatorname{UT}_3(\mathbf F_3),
\]
enumerates all noncentral pairs, and checks directly that every noncommuting pair generates the whole group. Thus \(\Xi(G)\) is edgeless in rank one.

For
\[
(p,n)=(2,2)
\quad\text{and}\quad
(3,2),
\]
it constructs the projective symplectic base graph and verifies
\[
k=p^{2n-1},
\qquad
\lambda=\mu=p^{2n-2}(p-1).
\]
It also verifies the matrix identity that forces the two nonprincipal base eigenvalues
\[
\pm p^{n-1}.
\]

Finally, for the order-\(32\) standard extraspecial group, it constructs the full graph directly from group commutators and confirms that it equals the predicted independent blow-up. The observed graph has \(30\) vertices and degree \(16\), matching the formulas.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the infinite family.

## Relationship to prior work

Freedman's work on the noncommuting–nongenerating graph proves general connectivity and diameter results and records that a nonabelian group which is not two-generated has \(\Xi(G)\) connected of diameter \(2\). The inspected full text contains no occurrence of “extraspecial” and does not identify the exact graph or its spectrum in this family.

Earlier work of Chin studies maximum pairwise noncommuting sets in extraspecial groups. The accessible abstract states upper and lower bounds for such sets, not a graph decomposition or spectral formula. Full text was not available through the inspected public source, so overlap with an unindexed internal statement remains a bibliographic risk.

The theorem here adds the rank-one empty boundary, the exact projective symplectic blow-up for every higher rank, the full spectrum, and the observation that the graph determines the prime and rank but cannot distinguish the two extraspecial types.

Searches using noncommuting–nongenerating, extraspecial, symplectic, spectrum, and plus/minus-type terminology did not locate this combined statement.

## Limitations

For
\[
n\ge2,
\]
the equality of \(\Xi(G)\) with the noncommuting graph is immediate from the fact that \(G\) is not two-generated. The substantive content is the exact projective blow-up, spectral calculation, and type-blind rigidity statement.

The theorem concerns extraspecial groups. Special groups with larger center or derived subgroup can produce higher-dimensional commutator targets, so a single symplectic form no longer controls the graph.

The inaccessible full text of the 2005 extraspecial noncommuting-set paper is a residual novelty risk.

Failed searches do not prove novelty.

## References

1. S. D. Freedman, “The non-commuting, non-generating graph of a non-simple group,” arXiv:2211.08869v1, first public version 16 November 2022; *Algebraic Combinatorics* 6 (2023), 1395–1418, DOI 10.5802/alco.305. Classification begins with MSC 20D60.
2. A. Y. M. Chin, “On non-commuting sets in an extraspecial \(p\)-group,” *Journal of Group Theory* 8 (2005), 189–194, DOI 10.1515/jgth.2005.8.2.189.
