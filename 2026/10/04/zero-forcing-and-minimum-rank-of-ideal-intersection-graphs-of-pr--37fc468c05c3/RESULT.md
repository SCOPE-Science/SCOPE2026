# Zero forcing and minimum rank of ideal-intersection graphs of products of fields

## Finding

Let \(R=F_1\times\cdots\times F_r\) be a direct product of \(r\ge3\) fields, and let \(G(R)\) be the simple intersection graph whose vertices are the nonzero proper ideals of \(R\), with distinct ideals adjacent exactly when their intersection is nonzero. Then, over the real symmetric minimum-rank model, \(G(R)\) has zero forcing number and maximum nullity \(Z(G(R))=M(G(R))=2^r-r-2\), and minimum rank \(\operatorname{mr}(G(R))=r\). A minimum zero forcing set is obtained by initially leaving white the \(r\) ideals corresponding to the supports \(\{1,2\},\{2,3,\ldots,r\},\{3,4,\ldots,r\},\ldots,\{r\}\) and coloring every other vertex blue.

Thus the number of field factors is recovered exactly as the real symmetric minimum rank of the ideal-intersection graph:
\[
r=\operatorname{mr}(G(R)).
\]
Since the graph has \(2^r-2\) vertices, its zero forcing number and maximum nullity are the complementary quantity
\[
2^r-r-2.
\]

## Assumptions and scope

Let
\[
R=F_1\times\cdots\times F_r,
\qquad r\ge3,
\]
where the \(F_i\) are fields. Every ideal is obtained by choosing, independently in each coordinate, either \(0\) or \(F_i\). Hence the nonzero proper ideals are indexed by the nonempty proper subsets
\[
S\subsetneq [r].
\]
Write \(I_S\) for the corresponding ideal. Then
\[
I_S\cap I_T=I_{S\cap T},
\]
so two distinct vertices are adjacent exactly when
\[
S\cap T\ne\varnothing.
\]

For a finite simple graph \(G\), let \(\mathcal S(G)\) be the set of real symmetric matrices whose off-diagonal nonzero pattern is exactly \(G\). The minimum rank is
\[
\operatorname{mr}(G)=\min_{A\in\mathcal S(G)}\operatorname{rank}A,
\]
and the maximum nullity is
\[
M(G)=|V(G)|-\operatorname{mr}(G).
\]
The standard zero forcing number \(Z(G)\) satisfies
\[
M(G)\le Z(G).
\]

## Proof

There are
\[
n=2^r-2
\]
vertices.

Let \(B\) be the \(r\times n\) real matrix whose column indexed by a vertex \(S\) is the incidence vector \(\mathbf 1_S\). Consider
\[
A=B^\mathsf{T}B.
\]
For distinct vertices \(S,T\),
\[
A_{S,T}=|S\cap T|.
\]
Therefore
\[
A_{S,T}\ne0
\quad\Longleftrightarrow\quad
S\cap T\ne\varnothing,
\]
so \(A\in\mathcal S(G(R))\). The singleton vertices give the standard basis columns of \(B\), hence
\[
\operatorname{rank}B=r.
\]
Consequently
\[
\operatorname{rank}A=r,
\]
and therefore
\[
\operatorname{mr}(G(R))\le r,
\qquad
M(G(R))\ge n-r.
\tag{1}
\]

It remains to construct a zero forcing set of size \(n-r\). Initially leave white precisely the following \(r\) vertices:
\[
W_1=\{1,2\},
\qquad
W_j=\{j,j+1,\ldots,r\}
\quad(2\le j\le r).
\]
Color every other vertex blue.

The singleton \(\{1\}\) is blue and, among the white vertices, it is adjacent only to \(W_1\). Hence it forces \(W_1\).

After \(W_1,\ldots,W_{j-1}\) have been forced, for every
\[
2\le j\le r-1
\]
the singleton \(\{j\}\) is blue and meets exactly one remaining white vertex, namely \(W_j\). Thus
\[
\{j\}\longrightarrow W_j.
\]
After \(W_{r-1}\) is forced, only \(W_r=\{r\}\) remains white, and the now-blue vertex \(W_{r-1}=\{r-1,r\}\) forces it. Hence
\[
Z(G(R))\le n-r.
\tag{2}
\]

The general maximum-nullity inequality gives
\[
M(G(R))\le Z(G(R)).
\tag{3}
\]
Combining (1), (2), and (3),
\[
n-r\le M(G(R))\le Z(G(R))\le n-r.
\]
Therefore
\[
Z(G(R))=M(G(R))=n-r=2^r-r-2,
\]
and
\[
\operatorname{mr}(G(R))=n-M(G(R))=r.
\]

## Verification

The accompanying `verify.py` constructs the subset-intersection graph directly. For every
\[
3\le r\le10,
\]
it checks the stated \(r\)-vertex white family, replays the entire zero forcing sequence, and verifies that the Gram matrix \(B^\mathsf{T}B\) has exactly the required off-diagonal graph pattern. For
\[
3\le r\le6,
\]
it also computes the Gram rank exactly over the rationals. Finally, for \(r=3\) and \(r=4\), it exhaustively enumerates all vertex subsets to verify the minimum zero forcing number independently of the rank bound.

Exact replay output:

```text
r=3: n=6, constructed ZFS size=3, forces=3, Gram pattern OK
r=4: n=14, constructed ZFS size=10, forces=4, Gram pattern OK
r=5: n=30, constructed ZFS size=25, forces=5, Gram pattern OK
r=6: n=62, constructed ZFS size=56, forces=6, Gram pattern OK
r=7: n=126, constructed ZFS size=119, forces=7, Gram pattern OK
r=8: n=254, constructed ZFS size=246, forces=8, Gram pattern OK
r=9: n=510, constructed ZFS size=501, forces=9, Gram pattern OK
r=10: n=1022, constructed ZFS size=1012, forces=10, Gram pattern OK
r=3: exhaustive Z=3, minimum ZFS count=15
r=4: exhaustive Z=10, minimum ZFS count=442
VERIFY_OK
```

The exhaustive checks are finite corroboration only. The arbitrary-rank theorem follows from the incidence Gram matrix, the explicit forcing sequence, and the general inequality \(M(G)\le Z(G)\).

## Relationship to prior work

Pucanović, Radovanović, and Erić study the same ideal-intersection graph for commutative rings, with primary classification \(13A15\), concentrating on graph embeddings and genus. Their full text develops the Artinian product decomposition needed to analyze nonlocal rings. Full-text searches of the inspected source found no occurrence of “zero forcing” or “minimum rank.”

Abu Osba, Al-Addasi, and Abughneim study this graph for finite commutative principal ideal rings. Their open full text explicitly treats the product-of-fields case and determines ordinary parameters including domination, radius, independence, geodetic and hull numbers, chordality, and properties of the complement. Full-text searches found no occurrence of “zero forcing” or “minimum rank.”

The general inequality \(M(G)\le Z(G)\) and the use of zero forcing for graph minimum-rank problems come from the AIM Minimum Rank — Special Graphs Work Group. The present result is the exact evaluation of both quantities for this algebraically defined Boolean-intersection family.

## Limitations

The theorem concerns products of at least three fields. For a product of two fields the intersection graph consists of two isolated vertices, so the displayed formula does not extend to that boundary case.

The minimum rank is over real symmetric matrices with the standard graph-pattern convention. Minimum rank over other fields can behave differently because the Gram entry \(|S\cap T|\) can vanish modulo the characteristic.

Searches found no prior statement of the exact zero forcing, maximum nullity, or real minimum-rank formulas for this ideal-intersection family, but terminology for subset-intersection graphs varies and creates a residual indexing risk.

## References

1. Z. S. Pucanović, M. Radovanović, and A. Lj. Erić, “On the genus of the intersection graph of ideals of a commutative ring,” *Journal of Algebra and Its Applications* 13 (2014), 1350155. DOI: 10.1142/S0219498813501557. Published online 13 December 2013.
2. E. Abu Osba, S. Al-Addasi, and O. Abughneim, “Some Properties of the Intersection Graph for Finite Commutative Principal Ideal Rings,” *International Journal of Combinatorics* (2014), Article 952371. DOI: 10.1155/2014/952371.
3. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
