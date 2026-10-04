# Zero forcing recovers the local-factor count of nonreduced finite principal ideal rings

## Finding

Let \(R\cong\prod_{i=1}^{r}R_i\) be a finite commutative principal ideal ring, where each \(R_i\) is a finite local chain ring of maximal-ideal nilpotency length \(\ell_i\ge1\), and assume at least one \(\ell_i\ge2\), so \(R\) is nonreduced. Let \(G(R)\) be the intersection graph on the nonzero proper ideals of \(R\), and put \(N=\prod_{i=1}^{r}(\ell_i+1)-2\). If \((r,\ell_1)=(1,2)\), then \(G(R)=K_1\), so \(Z(G(R))=M(G(R))=1\) and \(\operatorname{mr}(G(R))=0\). In every other nonreduced case, over the real symmetric minimum-rank model, \[Z(G(R))=M(G(R))=N-r\qquad\text{and}\qquad\operatorname{mr}(G(R))=r.\] Thus, away from the one-vertex boundary, the real symmetric minimum rank of the ideal-intersection graph is exactly the number of local factors in the principal-ideal decomposition.

For \(r\ge2\), this equality is witnessed simultaneously by a support-incidence Gram matrix and by an explicit zero forcing set that leaves exactly \(r\) ideals white. The result is insensitive to the individual nilpotency lengths except through the graph order \(N\).

## Assumptions and scope

Let
\[
R\cong\prod_{i=1}^{r}R_i
\]
be a finite commutative principal ideal ring. Each local factor \(R_i\) is a finite chain ring with maximal ideal \(\mathfrak m_i\) and nilpotency length
\[
\ell_i\ge1,
\qquad
\mathfrak m_i^{\ell_i}=0,
\qquad
\mathfrak m_i^{\ell_i-1}\ne0.
\]
A field factor has \(\ell_i=1\). Assume that at least one \(\ell_i\ge2\).

Every ideal has the form
\[
I=\prod_{i=1}^{r}I_i,
\]
with \(I_i\) an ideal of \(R_i\). Define its active support by
\[
\sigma(I)=\{i:I_i\ne0\}.
\]
Because the ideals of a chain ring are linearly ordered,
\[
I_i\cap J_i\ne0
\quad\Longleftrightarrow\quad
I_i\ne0\text{ and }J_i\ne0.
\]
Hence, for distinct nonzero proper ideals,
\[
I\sim J
\quad\Longleftrightarrow\quad
\sigma(I)\cap\sigma(J)\ne\varnothing.
\tag{1}
\]

The number of graph vertices is
\[
N=\prod_{i=1}^{r}(\ell_i+1)-2.
\]

For a graph \(G\), \(\operatorname{mr}(G)\) denotes the minimum rank over real symmetric matrices having exactly the graph's off-diagonal zero-nonzero pattern, and
\[
M(G)=|V(G)|-\operatorname{mr}(G)
\]
is maximum nullity. The standard zero forcing inequality is
\[
M(G)\le Z(G).
\]

## Proof

First suppose \(r\ge2\). Form the \(r\times N\) support-incidence matrix \(B\) whose column indexed by \(I\) is the \(0\)-\(1\) incidence vector of \(\sigma(I)\). Set
\[
A=B^\mathsf{T}B.
\]
For two distinct vertices \(I,J\),
\[
A_{I,J}=|\sigma(I)\cap\sigma(J)|.
\]
By (1),
\[
A_{I,J}\ne0
\quad\Longleftrightarrow\quad
I\sim J.
\]
Thus
\[
A\in\mathcal S(G(R)).
\]

For every \(i\), the ideal
\[
E_i=0\times\cdots\times0\times R_i\times0\times\cdots\times0
\]
is a proper nonzero ideal, and its column in \(B\) is the \(i\)-th standard basis vector. Therefore
\[
\operatorname{rank}B=r,
\qquad
\operatorname{rank}A=r.
\]
Consequently
\[
\operatorname{mr}(G(R))\le r,
\qquad
M(G(R))\ge N-r.
\tag{2}
\]

Reorder the local factors so that \(\ell_1\ge2\), and let \(\mathfrak m_1\ne0\) be the maximal ideal of \(R_1\). Leave white the following \(r\) vertices:
\[
W_1=\mathfrak m_1\times R_2\times\cdots\times R_r,
\]
and, for \(2\le j\le r\),
\[
W_j=
0\times\cdots\times0\times R_j\times R_{j+1}\times\cdots\times R_r.
\]
Color every other vertex blue.

The blue ideal
\[
X_1=R_1\times0\times\cdots\times0
\]
meets \(W_1\) nontrivially and is disjoint from every \(W_j\) with \(j\ge2\). Hence
\[
X_1\longrightarrow W_1.
\]

For \(2\le j\le r-1\), after \(W_1,\ldots,W_{j-1}\) have become blue, let
\[
X_j=
0\times\cdots\times0\times R_j\times0\times\cdots\times0.
\]
Among the remaining white vertices, \(X_j\) is adjacent only to \(W_j\), so
\[
X_j\longrightarrow W_j.
\]
Finally, after \(W_{r-1}\) becomes blue, the only white vertex is \(W_r\), and \(W_{r-1}\) forces it. Thus
\[
Z(G(R))\le N-r.
\tag{3}
\]

Combining (2), (3), and \(M(G)\le Z(G)\),
\[
N-r\le M(G(R))\le Z(G(R))\le N-r.
\]
Therefore
\[
Z(G(R))=M(G(R))=N-r
\]
and
\[
\operatorname{mr}(G(R))=r.
\]

Now let \(r=1\). If \(\ell_1\ge3\), then the nonzero proper ideals form the clique
\[
K_{\ell_1-1}.
\]
Therefore
\[
Z=\ell_1-2=N-1=N-r,
\qquad
\operatorname{mr}=1=r.
\]
If \(\ell_1=2\), the graph is \(K_1\). Its unique vertex must initially be blue, while the zero \(1\times1\) matrix is allowed in the real symmetric graph-pattern model. Hence
\[
Z=M=1,
\qquad
\operatorname{mr}=0.
\]

## Verification

The accompanying `verify.py` constructs the graph directly from exponent vectors for representative nilpotency-length tuples, including local rings, one nonfield factor with field factors, and several genuinely nonlocal nonreduced cases.

For every test case it verifies the exact off-diagonal pattern of the support Gram matrix and computes its rank over rational arithmetic. It also replays the stated forcing construction. In every case with at most \(16\) vertices, it additionally checks directly that no set one smaller than the claimed minimum can zero-force the graph.

Exact replay output:

```text
lengths=(2,): N=1, boundary K1, Z=1, mr=0
lengths=(3,): N=2, r=1, constructed_Z=1, forces=1, Gram_rank=1
lengths=(4,): N=3, r=1, constructed_Z=2, forces=1, Gram_rank=1
lengths=(2, 1): N=4, r=2, constructed_Z=2, forces=2, Gram_rank=2
lengths=(3, 1): N=6, r=2, constructed_Z=4, forces=2, Gram_rank=2
lengths=(2, 2): N=7, r=2, constructed_Z=5, forces=2, Gram_rank=2
lengths=(3, 2): N=10, r=2, constructed_Z=8, forces=2, Gram_rank=2
lengths=(2, 1, 1): N=10, r=3, constructed_Z=7, forces=3, Gram_rank=3
lengths=(2, 2, 1): N=16, r=3, constructed_Z=13, forces=3, Gram_rank=3
lengths=(2, 1, 1, 1): N=22, r=4, constructed_Z=18, forces=4, Gram_rank=4
VERIFY_OK
```

The finite checks are corroborative only. The arbitrary-ring theorem follows from the support-intersection equivalence, the rank-\(r\) Gram witness, the explicit forcing chain, and the general inequality \(M(G)\le Z(G)\).

## Relationship to prior work

Jafari and Jafari Rad study the same intersection graph of proper nontrivial ideals of a commutative ring. Their paper lists primary 2000 Mathematics Subject Classification \(16BXX\) and determines ordinary domination. It does not discuss zero forcing, maximum nullity, or minimum rank.

Abu Osba, Al-Addasi, and Abughneim treat finite commutative principal ideal rings specifically. Their open full text records the decomposition into local principal ideal rings, the chain of ideals in each local factor, and formulas for classical graph invariants such as domination, independence, radius, geodetic number, hull number, and chordality. Full-text searches found no occurrence of “zero forcing,” “minimum rank,” or “maximum nullity.”

The general zero forcing/minimum-rank inequality comes from the AIM Minimum Rank — Special Graphs Work Group. The present theorem supplies the ring-specific support Gram representation and a matching forcing construction in the nonreduced principal-ideal regime.

## Limitations

The theorem is stated only for nonreduced finite commutative principal ideal rings. Products of fields form a separate reduced regime.

The one-vertex local ring boundary \(\ell_1=2\) is exceptional because an isolated vertex has zero minimum rank but zero forcing number one.

The minimum-rank statement is over real symmetric matrices. Other coefficient fields can behave differently because support-intersection counts may vanish in positive characteristic.

The proof determines the minimum size but does not classify every minimum zero forcing set.

## References

1. S. H. Jafari and N. Jafari Rad, “Domination in the intersection graphs of rings and modules,” *Italian Journal of Pure and Applied Mathematics* 28 (2011), 17–20. Published 19 July 2011.
2. E. Abu Osba, S. Al-Addasi, and O. Abughneim, “Some Properties of the Intersection Graph for Finite Commutative Principal Ideal Rings,” *International Journal of Combinatorics* (2014), Article 952371. DOI: 10.1155/2014/952371.
3. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
