# Maximum pairwise lift-commuting subsets in \(C_{p^a}\times C_{p^a}\)

## Finding

Let \(p\) be a prime and \(a\ge1\), and put
\[
A=C_{p^a}\times C_{p^a}.
\]
Write \(\Delta_D(A)\) for the simple deep commuting graph: its vertices are the elements of \(A\), and two distinct vertices are adjacent when their preimages commute in a Schur cover.

After identifying
\[
A\cong (\mathbb Z/p^a\mathbb Z)^2,
\]
two distinct elements
\[
x=(x_1,x_2),
\qquad
y=(y_1,y_2)
\]
are adjacent exactly when
\[
\boxed{x_1y_2-x_2y_1\equiv0\pmod{p^a}.}
\]

Consequently,
\[
\boxed{\omega(\Delta_D(A))=p^a.}
\]
Even more strongly, the maximum cliques are exactly the subgroups of \(A\) of order \(p^a\).

There are exactly
\[
\boxed{
1+p+\cdots+p^a
=
\frac{p^{a+1}-1}{p-1}
}
\]
maximum cliques.

Their group types are also completely determined. For every integer \(k\) with
\[
0\le k<\frac a2,
\]
there are exactly
\[
\boxed{p^{a-2k-1}(p+1)}
\]
maximum cliques isomorphic to
\[
C_{p^{a-k}}\times C_{p^k},
\]
where \(C_{p^0}\) is understood as the trivial group. If \(a\) is even, there is one further maximum clique,
\[
p^{a/2}A\cong C_{p^{a/2}}\times C_{p^{a/2}}.
\]

Thus the extremal pairwise lift-commuting subsets are not merely bounded in size: they are precisely the half-order subgroups of the homocyclic rank-two group.

## Assumptions and scope

The graph is simple, so loops are removed. The identity is nevertheless a vertex and is adjacent to every other vertex.

The deep commuting graph was introduced by Cameron and Kuzma. For an abelian group, the commutator of preimages in a Schur cover is governed by the exterior-square pairing. A later full-text study of finite abelian \(p\)-groups gives an explicit Schur cover and the commutator formula
\[
[\widetilde x,\widetilde y]
=
\prod_{i<j}a_{ij}^{\,s_it_j-s_jt_i}.
\]
For rank two with equal exponent \(p^a\), this reduces exactly to the determinant congruence above.

The result is stated for the homocyclic rank-two group. No claim is made here for unequal exponents or rank at least three.

## Proof

Let
\[
R=\mathbb Z/p^a\mathbb Z,
\qquad
A=R^2.
\]
The standard Schur-cover presentation for a finite abelian \(p\)-group has, in rank two,
\[
[\widetilde e_1,\widetilde e_2]=z,
\qquad
o(z)=p^a.
\]
Because the cover has nilpotency class two, for
\[
x=x_1e_1+x_2e_2,
\qquad
y=y_1e_1+y_2e_2,
\]
one obtains
\[
[\widetilde x,\widetilde y]
=
z^{\,x_1y_2-x_2y_1}.
\]
Therefore distinct vertices \(x,y\) are adjacent in \(\Delta_D(A)\) exactly when
\[
\det(x,y)=x_1y_2-x_2y_1=0
\]
in \(R\).

Now let \(S\) be a clique and let
\[
L=\langle S\rangle_R\le R^2.
\]
Since the determinant is bilinear, pairwise vanishing on \(S\) implies
\[
\det(u,v)=0
\]
for every \(u,v\in L\). Thus \(L\) is an isotropic \(R\)-submodule for the determinant pairing.

Use Smith normal form over the principal ideal ring \(R\). There are
\[
U\in\operatorname{GL}_2(R)
\]
and integers
\[
0\le i\le j\le a
\]
such that
\[
L
=
U\left(p^iRe_1\oplus p^jRe_2\right).
\]
The two displayed generators have determinant equal to a unit times
\[
p^{i+j}.
\]
Hence isotropy forces
\[
i+j\ge a.
\]
It follows that
\[
|L|
=
p^{(a-i)+(a-j)}
=
p^{2a-i-j}
\le p^a.
\]
Since \(S\subseteq L\),
\[
|S|\le p^a.
\]

Conversely, suppose \(L\le A\) has order \(p^a\). In its Smith form,
\[
p^{2a-i-j}=p^a,
\]
so
\[
i+j=a.
\]
Every determinant of two elements of \(L\) is therefore divisible by \(p^a\), hence vanishes in \(R\). Thus \(L\) is a clique of size \(p^a\).

We have proved both that the clique number is \(p^a\) and that every subgroup of order \(p^a\) is a maximum clique. If \(S\) itself is a maximum clique, then its span \(L\) is isotropic and satisfies
\[
p^a=|S|\le|L|\le p^a.
\]
Therefore \(S=L\), so every maximum clique is one of these subgroups.

It remains to count them.

For
\[
0\le k<\frac a2,
\]
a subgroup of type
\[
C_{p^{a-k}}\times C_{p^k}
\]
lies in the single \(\operatorname{GL}_2(R)\)-orbit of
\[
L_k=p^kRe_1\oplus p^{a-k}Re_2.
\]
An invertible matrix stabilizes \(L_k\) exactly when its lower-left entry is divisible by
\[
p^{a-2k}.
\]
Modulo \(p\), the stabilizer consists of invertible upper-triangular matrices, an index-\(p+1\) subgroup of \(\operatorname{GL}_2(\mathbb F_p)\). Each additional required \(p\)-adic zero digit contributes a factor \(p\) to the index. Therefore the orbit size is
\[
p^{a-2k-1}(p+1).
\]

If \(a\) is even and
\[
k=\frac a2,
\]
the subgroup is
\[
p^{a/2}A,
\]
which is characteristic and hence unique.

Summing the orbit sizes gives
\[
\sum_{0\le k<a/2}p^{a-2k-1}(p+1)
\]
plus the central term \(1\) when \(a\) is even. In either parity this telescopes to
\[
1+p+\cdots+p^a
=
\frac{p^{a+1}-1}{p-1}.
\]

## Verification

The included replay builds the determinant-adjacency graph directly and enumerates every maximal clique by a bit-set Bron--Kerbosch algorithm.

It checks the cases
\[
(p,a)=(2,1),(2,2),(2,3),(3,1),(3,2).
\]
For every case it verifies:

- the maximum clique size is \(p^a\);
- every maximum clique is closed under addition and inverses, hence is a subgroup;
- every subgroup returned this way has order \(p^a\);
- the number of maximum cliques is
  \[
  \frac{p^{a+1}-1}{p-1};
  \]
- the distribution by invariant-factor type agrees with
  \[
  p^{a-2k-1}(p+1)
  \]
  and the unique middle subgroup when \(a\) is even.

For example,
\[
C_4\times C_4
\]
has seven maximum cliques of order \(4\): six cyclic ones and the unique subgroup
\[
2A\cong C_2\times C_2.
\]
Likewise,
\[
C_8\times C_8
\]
has fifteen maximum cliques of order \(8\): twelve cyclic ones and three of type
\[
C_4\times C_2.
\]

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Cameron and Kuzma introduced the deep commuting graph and explicitly left graph-theoretic properties such as chromatic number untreated. Their paper gives the \(C_3\times C_3\) example but does not determine maximum cliques in homocyclic groups.

Hatui, Mukherjee, and Patra later developed a broad study of deep commuting graphs. Their full preprint gives the Schur-cover commutator formula for arbitrary finite abelian \(p\)-groups and proves several structural results. It explicitly describes
\[
\Delta_D(C_p\times C_p)
\]
as \(p+1\) cliques of order \(p\) meeting at the identity, and notes that the order-\(p\) subgroup of
\[
C_{p^2}\times C_{p^2}
\]
induces a complete graph of order \(p^2\). The paper defines clique number as background terminology but does not state a clique-number theorem, classify maximum cliques of
\[
C_{p^a}\times C_{p^a},
\]
or enumerate them.

A 2026 article by Arvin, Edalatzadeh, and Salemkar studies direct products and graph isomorphism for deep commuting graphs. Its accessible abstract states that finite abelian groups are determined by their deep commuting graphs, but does not state the maximum-clique classification proved here. The full article was not available in the inspected text interface, so it remains a bibliographic residual risk rather than evidence of noncoverage.

The theorem above uses the published rank-two commutator relation as its starting point and adds the extremal isotropic-submodule classification and exact orbit count.

## Limitations

The proof uses the special rank-two homocyclic module
\[
(\mathbb Z/p^a\mathbb Z)^2.
\]
For unequal exponents, the commutator modulus and subgroup geometry are asymmetric. For rank at least three, maximal isotropic submodules for the full exterior-square condition require a different analysis.

The theorem determines clique number and every maximum clique, but it does not determine the chromatic number.

The 2026 direct-product paper was inspectable only through its abstract and bibliographic record. An equivalent maximum-clique statement could also exist in literature phrased in terms of isotropic submodules over finite chain rings rather than deep commuting graphs.

## References

1. P. J. Cameron and B. Kuzma, “Between the enhanced power graph and the commuting graph,” arXiv:2012.03789v1, first public version 7 December 2020; *Journal of Graph Theory* 102 (2023), 295–303, DOI 10.1002/jgt.22871.
2. S. Hatui, S. Mukherjee, and K. L. Patra, “On the deep commuting graph of a finite group,” arXiv:2511.13303v1, 17 November 2025.
3. B. Arvin, B. Edalatzadeh, and A. R. Salemkar, “On Deep-Commuting Graph of Groups,” *Journal of Graph Theory* 113 (2026), 195–207, DOI 10.1002/jgt.70059.
