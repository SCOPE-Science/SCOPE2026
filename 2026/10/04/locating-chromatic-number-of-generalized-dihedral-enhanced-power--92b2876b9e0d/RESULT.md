# Locating chromatic number of generalized-dihedral enhanced power graphs

## Finding

Let \(A\) be a nontrivial finite abelian group of order \(m\), and let
\[
G=\operatorname{Dih}(A)=A\rtimes\langle t\rangle,
\qquad
 t^2=1,
\qquad
 tat=a^{-1}
\]
for every \(a\in A\).

Let \(\mathcal P_e(G)\) be the enhanced power graph: two distinct group elements are adjacent when they lie in a common cyclic subgroup. Define
\[
T(A)=\{u\in A:o(u)=2\text{ and }u\text{ lies in no cyclic subgroup of }A\text{ of order greater than }2\}.
\]
Then the locating chromatic number is
\[
\boxed{\chi_L(\mathcal P_e(G))=m+|T(A)|+1.}
\]

The correction term \(|T(A)|\) has a closed group-theoretic form. If \(A\) is not a \(2\)-group, then
\[
T(A)=\varnothing.
\]
If
\[
A\cong C_{2^{a_1}}\times\cdots\times C_{2^{a_r}},
\qquad a_i\ge1,
\]
and
\[
s=|\{i:a_i\ge2\}|,
\]
then
\[
|T(A)|=2^r-2^s
\]
and therefore
\[
\boxed{
\chi_L(\mathcal P_e(\operatorname{Dih}(A)))
=|A|+2^r-2^s+1.
}
\]

For the ordinary dihedral group \(D_{2n}=\operatorname{Dih}(C_n)\), \(n\ge2\), this specializes to
\[
\chi_L(\mathcal P_e(D_{2n}))=
\begin{cases}
4,&n=2,\\
n+1,&n\ne2.
\end{cases}
\]

## Assumptions and scope

A proper coloring of a connected graph with color classes \(C_1,\ldots,C_k\) is locating if the color code
\[
(d(v,C_1),\ldots,d(v,C_k))
\]
is different for every pair of vertices. The locating chromatic number \(\chi_L\) is the minimum possible \(k\).

The theorem concerns generalized dihedral groups with finite abelian kernel. The inversion action is allowed to be trivial on some or all of the kernel; in particular, elementary abelian \(2\)-groups are included.

The literature motivation is Problem 15 in the 2022 survey of enhanced power graphs, which asks for the locating chromatic number of enhanced power graphs of finite groups. A 2021 study computes metric-dimension and spectral data for several nonabelian families, including ordinary dihedral groups, but not locating chromatic numbers.

## Proof

Write elements of the nontrivial coset as \(at\), with \(a\in A\). Since
\[
(at)^2=atat=aa^{-1}=1,
\]
every element of \(At\) is an involution.

We first determine the leaves of \(\mathcal P_e(G)\). Every \(at\in At\) is adjacent only to the identity. Indeed, two distinct elements of \(At\) cannot lie in one cyclic subgroup because a cyclic group has at most one involution. If \(at\) and \(x\in A\setminus\{1\}\) lay in a common cyclic subgroup, they would commute. But
\[
(at)x=ax^{-1}t,
\qquad
x(at)=axt,
\]
so commutation forces \(x=x^{-1}\). Then \(x\) is an involution distinct from \(at\), again impossible inside a cyclic subgroup. Thus
\[
N(at)=\{1\}.
\]

Now let \(u\in A\setminus\{1\}\). Its neighbors inside \(A\) in the enhanced power graph are exactly the nonidentity elements that share a cyclic subgroup with \(u\). Hence \(u\) has no nonidentity neighbor precisely when \(u\) has order \(2\) and is contained in no cyclic subgroup of \(A\) of order greater than \(2\). These are exactly the elements of \(T(A)\). Therefore
\[
F=At\cup T(A)
\]
is a false-twin class of cardinality
\[
|F|=m+|T(A)|,
\]
and every vertex of \(F\) has open neighborhood \(\{1\}\).

In any locating coloring, distinct false twins must have distinct colors: if two false twins had the same color, their distances to every color class would coincide. Moreover, the identity is adjacent to every vertex of the enhanced power graph, so it cannot share a color with any other vertex. Consequently
\[
\chi_L(\mathcal P_e(G))\ge m+|T(A)|+1.
\]

We now construct a locating coloring with exactly this many colors. Give all vertices of \(F\) distinct colors and give the identity one new color. Put
\[
R=A\setminus(\{1\}\cup T(A)).
\]
Since
\[
|R|=m-1-|T(A)|<m+|T(A)|=|F|,
\]
pair every vertex of \(R\) injectively with a distinct vertex of \(F\), and let each paired vertex reuse its partner's color. The coloring is proper because vertices of \(F\) are adjacent only to the identity, while all vertices of \(R\) receive distinct colors.

Vertices in different color classes are automatically distinguished by the coordinate corresponding to either one's own color class. It remains only to distinguish a same-color pair \((r,f)\) with \(r\in R\) and \(f\in F\). By the definition of \(R\), the vertex \(r\) has a nonidentity neighbor \(z\in A\). Such a \(z\) cannot lie in \(T(A)\), because vertices of \(T(A)\) are leaves, so \(z\in R\). Let \(C_z\) be the color class containing \(z\). Then
\[
d(r,C_z)=1,
\qquad
d(f,C_z)=2,
\]
because every path from the leaf \(f\) to a nonidentity vertex passes through the identity. Thus the coloring is locating, proving
\[
\chi_L(\mathcal P_e(G))=m+|T(A)|+1.
\]

It remains to compute \(|T(A)|\). If \(A\) has odd order, it has no involutions. If \(A\) has both an involution \(u\) and a nontrivial odd-order element \(b\), then \(u\) and \(b\) commute and \(ub\) has order \(2o(b)\); moreover
\[
(ub)^{o(b)}=u.
\]
Thus every involution lies in a cyclic subgroup of order greater than \(2\). Hence \(T(A)=\varnothing\) whenever \(A\) is not a \(2\)-group.

Suppose now that \(A\) is a finite abelian \(2\)-group. In additive notation, an involution \(u\) lies in a cyclic subgroup of order greater than \(2\) if and only if
\[
u\in 2A.
\]
Indeed, if \(u=2v\) then \(v\) has order \(4\); conversely, the unique involution in any cyclic \(2\)-group of order at least \(4\) is twice an element of order \(4\). Therefore
\[
T(A)=A[2]\setminus 2A.
\]
For
\[
A\cong C_{2^{a_1}}\times\cdots\times C_{2^{a_r}},
\]
we have \(|A[2]|=2^r\). In the intersection \(A[2]\cap2A\), a factor with \(a_i=1\) contributes only zero, while a factor with \(a_i\ge2\) contributes two choices. Hence
\[
|A[2]\cap2A|=2^s,
\]
where \(s=|\{i:a_i\ge2\}|\). It follows that
\[
|T(A)|=2^r-2^s.
\]
The ordinary dihedral formula follows by taking \(A=C_n\).

## Verification

The included replay constructs generalized dihedral groups directly for a collection of cyclic and noncyclic abelian kernels. It enumerates all cyclic subgroups, builds the enhanced power graph from the defining adjacency relation, identifies the false-twin leaf class, constructs the locating coloring used in the proof, and checks all color codes.

The tested kernels include
\[
C_2,\ C_3,\ C_4,\ C_5,\ C_6,\ C_8,\ C_2^2,\ C_2\times C_4,\ C_4^2,\ C_2\times C_6,\ C_3^2,\ C_2^3.
\]
For every test, the replay verifies both the structural formula for \(|T(A)|\) and the claimed number of colors. It returns `VERIFY_OK`.

The finite replay is not used to prove the universal statement.

## Relationship to prior work

The 2022 survey on enhanced power graphs explicitly proposes the general problem of describing the locating chromatic number of the enhanced power graph of a finite group. The theorem above gives an exact answer for every generalized dihedral group with finite abelian kernel, including kernels of arbitrary rank and mixed primary structure.

A 2021 paper on enhanced power graphs of several nonabelian groups studies metric dimension, resolving polynomials, distance properties, and Laplacian spectra. Its full text describes ordinary dihedral enhanced power graphs among its spectral families but does not discuss locating chromatic number. The present result instead exploits the complete false-twin structure of the generalized dihedral coset and identifies the exact additional obstruction contributed by isolated involutions in the abelian kernel.

The formula is not merely an ordinary-dihedral specialization. For example, if \(A\cong C_2^r\), then every nonidentity kernel element is an isolated involution in \(\mathcal P_e(A)\), and the theorem gives
\[
\chi_L(\mathcal P_e(\operatorname{Dih}(A)))=2|A|.
\]
At the opposite extreme, if \(A\) is not a \(2\)-group, the correction vanishes and the value is simply \(|A|+1\).

## Limitations

The theorem uses the inversion semidirect-product structure. It does not determine locating chromatic numbers for arbitrary semidirect products or for all finite groups.

The exact correction term depends on which involutions of the kernel are isolated in its enhanced power graph. For nonabelian kernels, this description need not reduce to the invariant-factor count proved here.

Targeted searches under locating-coloring, enhanced-power, cyclic-graph, dihedral, and generalized-dihedral terminology did not locate an equivalent theorem. An equivalent result could nevertheless exist under different terminology or in unindexed literature.

## References

1. X. Ma, A. Kelarev, Y. Lin, and K. Wang, “A survey on enhanced power graphs of finite groups,” *Electronic Journal of Graph Theory and Applications* 10(1) (2022), 89–111, DOI 10.5614/ejgta.2022.10.1.6.
2. Parveen, S. Dalal, and J. Kumar, “Enhanced Power Graph of Certain Non-abelian Groups,” arXiv:2108.13006v1 (2021); later published with DOI 10.1142/S1793830923500635.
3. G. Chartrand, D. Erwin, M. A. Henning, P. J. Slater, and P. Zhang, “The locating-chromatic number of a graph,” *Bulletin of the Institute of Combinatorics and its Applications* 36 (2002), 89–101.
