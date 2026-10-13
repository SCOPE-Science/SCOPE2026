# Symmetry breaking in ideal-intersection graphs of fully nonreduced finite principal ideal rings

## Finding

Let \(R\cong\prod_{i=1}^r R_i\), where each \(R_i\) is a finite commutative local principal ideal ring whose maximal ideal has nilpotency length \(\ell_i\ge2\), and let \(G(R)\) be the intersection graph on the nonzero proper ideals. Put \(P=\prod_{i=1}^r\ell_i\), \(N=\prod_{i=1}^r(\ell_i+1)-2\), and for nonempty \(S\subseteq[r]\) put \(w_S=\prod_{i\in S}\ell_i\) when \(S\ne[r]\) and \(w_{[r]}=P-1\). If \(H=\{\pi\in S_r:\ell_{\pi(i)}=\ell_i\text{ for every }i\}\), then \[\operatorname{Aut}(G(R))\cong\left(\prod_{\varnothing\ne S\subseteq[r]} S_{w_S}\right)\rtimes H.\] Moreover, \(\operatorname{Det}(G(R))=N-(2^r-1)\) and the distinguishing number is \(D(G(R))=P-1\).

In particular, the distinguishing number recovers the product of the local nilpotency lengths:
\[
D(G(R))+1=\prod_{i=1}^r\ell_i.
\]

## Assumptions and scope

Let
\[
R\cong R_1\times\cdots\times R_r,
\qquad r\ge1,
\]
where each \(R_i\) is a finite commutative local principal ideal ring that is not a field. If \(\mathfrak m_i\) is its maximal ideal, write
\[
\mathfrak m_i^{\ell_i}=0,
\qquad
\mathfrak m_i^{\ell_i-1}\ne0,
\qquad
\ell_i\ge2.
\]
Every ideal of \(R_i\) is
\[
R_i=\mathfrak m_i^0,
\mathfrak m_i,
\ldots,
\mathfrak m_i^{\ell_i}=0.
\]

The graph \(G(R)\) has the nonzero proper ideals as vertices, with distinct ideals adjacent exactly when their intersection is nonzero. The assumption \(\ell_i\ge2\) for every local factor is the natural fully nonreduced regime: it makes every one-coordinate support cell have at least two vertices. Field factors create singleton cells and a different symmetry-breaking boundary, which is not asserted here.

## Proof

Write an ideal as
\[
I_a=\prod_{i=1}^r\mathfrak m_i^{a_i},
\qquad
0\le a_i\le\ell_i.
\]
Define its active support by
\[
\sigma(a)=\{i:a_i<\ell_i\}.
\]
Since intersections in a chain ring satisfy
\[
\mathfrak m_i^{a_i}\cap\mathfrak m_i^{b_i}
=
\mathfrak m_i^{\max(a_i,b_i)},
\]
one has
\[
I_a\cap I_b\ne0
\quad\Longleftrightarrow\quad
\sigma(a)\cap\sigma(b)\ne\varnothing.
\tag{1}
\]

For each nonempty support \(S\subseteq[r]\), let \(V_S\) be the set of graph vertices with support \(S\). If \(S\ne[r]\), then
\[
|V_S|=w_S=\prod_{i\in S}\ell_i.
\]
For \(S=[r]\), the same count includes the whole ring, which is not a vertex, so
\[
|V_{[r]}|=w_{[r]}=P-1,
\qquad
P=\prod_{i=1}^r\ell_i.
\tag{2}
\]
Summing the cells gives
\[
N=|V(G(R))|=
\prod_{i=1}^r(\ell_i+1)-2.
\tag{3}
\]

By (1), each \(V_S\) is a clique of true twins. These are exactly the maximal true-twin classes. Indeed, if \(S\ne T\), choose \(i\in S\setminus T\) after interchanging the two sets if needed. Because \(\ell_i\ge2\), the singleton-support cell \(V_{\{i\}}\) contains at least two vertices; a suitable vertex in that cell is adjacent to a chosen vertex of \(V_S\) but not to a chosen vertex of \(V_T\). Thus vertices from different support cells do not have the same closed neighborhood.

Collapse every \(V_S\) to one vertex. The quotient graph \(Q_r\) has all nonempty subsets of \([r]\) as vertices, with adjacency given by nonempty intersection. A support \(S\) has quotient degree
\[
2^r-2^{r-|S|}-1,
\]
so an automorphism preserves support cardinality. It therefore permutes the singleton supports. For every support of size at least two, its singleton neighbors are exactly the singleton subsets it contains, so the singleton permutation determines its image. Consequently
\[
\operatorname{Aut}(Q_r)\cong S_r.
\tag{4}
\]

An automorphism of \(G(R)\) can induce only a coordinate permutation preserving the cell sizes. Since
\[
|V_{\{i\}}|=\ell_i,
\]
this means precisely
\[
H=\{\pi\in S_r:\ell_{\pi(i)}=\ell_i\text{ for every }i\}.
\]
Conversely, every such coordinate permutation preserves all cell sizes and lifts to a graph automorphism, while every cell admits an arbitrary internal permutation. Hence
\[
\operatorname{Aut}(G(R))
\cong
\left(\prod_{\varnothing\ne S\subseteq[r]}S_{w_S}\right)\rtimes H.
\tag{5}
\]

For a determining set, at most one vertex may be omitted from each true-twin cell: if two vertices of one cell were omitted, their transposition would fix the proposed determining set pointwise. Therefore
\[
\operatorname{Det}(G(R))
\ge
\sum_{\varnothing\ne S\subseteq[r]}(w_S-1)
=N-(2^r-1).
\tag{6}
\]
Choose all but one vertex from every support cell. Except for the one-vertex boundary \(r=1,\ell_1=2\), each cell then contains a fixed vertex, so no support cell can move under an automorphism fixing the chosen set pointwise; the remaining internal permutation is also forced to be trivial. In the boundary case the graph is \(K_1\) and the same formula gives zero. Thus equality holds in (6).

For the distinguishing number, the full-support cell is the unique largest true-twin class. By (2) its size is
\[
W=P-1.
\]
Every distinguishing coloring must be injective on a true-twin class, so
\[
D(G(R))\ge W.
\tag{7}
\]

To attain the bound, color \(V_{[r]}\) injectively with all \(W\) colors. If \(r\ge2\), every proper support cell has size strictly less than \(W\), while
\[
W=P-1\ge2^r-1.
\]
For every size \(1\le k<W\), there are at least \(W\) distinct \(k\)-subsets of the color set, because
\[
\binom{W}{k}\ge W.
\]
There are fewer than \(W\) proper support cells. Assign every proper cell a different color subset of the required cardinality and use those colors injectively inside that cell. A color-preserving automorphism must preserve every support cell because its color set is unique, and injectivity then fixes each vertex. For \(r=1\), the graph is a clique and the conclusion is immediate. Hence
\[
D(G(R))=P-1.
\tag{8}
\]

## Verification

The accompanying `verify.py` was read from its actual packaged path before replay.

It constructs the exponent-vector graph directly for nilpotency-length tuples
\[
(2),\quad(3),\quad(2,2),\quad(2,3).
\]
For the seven-vertex \((2,2)\) case it exhausts every vertex permutation and confirms that the full automorphism group has order \(48\), exactly as (5) predicts. For all four cases it independently generates the structural automorphisms, brute-forces the determining number from those automorphisms, builds a distinguishing coloring using exactly \(P-1\) colors, and verifies that its color stabilizer is trivial.

It also reconstructs the ideal-intersection graphs of
\[
\mathbb Z/36\mathbb Z
\quad\text{and}\quad
\mathbb Z/108\mathbb Z
\]
directly from divisor ideals, checking every adjacency against the exponent-support model.

Exact replay output:

```text
ells=(2,): N=1, |Aut|=1, Det=0, distinguishing witness uses 1 colors
ells=(3,): N=2, |Aut|=2, Det=1, distinguishing witness uses 2 colors
ells=(2, 2): N=7, |Aut|=48, Det=4, distinguishing witness uses 3 colors
ells=(2, 3): N=10, |Aut|=1440, Det=7, distinguishing witness uses 5 colors
Z/36Z and Z/108Z direct ideal-intersection reconstructions OK
VERIFY_OK
```

The finite computations corroborate the proof; the arbitrary-ring theorem follows from the chain-ideal decomposition, the exact true-twin classification, and the quotient-graph automorphism argument.

## Relationship to prior work

Jafari and Jafari Rad study the same intersection graph of ideals and place that work first in the algebra classification \(16\mathrm{B}\); their 2011 paper determines domination parameters rather than automorphism or symmetry-breaking invariants. Its first public journal date is 19 July 2011.

Abu Osba, Al-Addasi, and Abughneim develop the exact finite commutative principal-ideal-ring setting used here. Their full article describes the decomposition into local principal ideal rings and the chain of powers of each maximal ideal, then studies radius, eccentricity, domination, independence, geodetic and hull numbers, chordality, and the complement. Full-text searches found no occurrence of “automorphism,” “determining,” “distinguishing,” or “symmetry.”

Boutin introduced determining sets as a way to identify graph automorphisms, while Albertson and Collins introduced distinguishing labelings. Those general definitions do not provide the ring-specific true-twin decomposition, automorphism group (5), or the exact formulas (6)--(8).

A later paper determines automorphisms for intersection graphs of left ideals of full matrix rings over finite fields. That is a different noncommutative family whose vertices are subspace-like left ideals; it does not cover finite commutative products of chain rings.

## Limitations

Every local factor is assumed nonfield, equivalently \(\ell_i\ge2\). This is a structural boundary, not a claim about mixed products containing field factors: singleton support cells in mixed products alter the pointwise-base and color-set arguments.

The automorphism group is the graph automorphism group, not the image of the ring automorphism group.

The theorem depends on the nilpotency lengths but not on the residue-field orders. Consequently these symmetry invariants need not determine the underlying finite principal ideal ring up to isomorphism.

## References

1. S. H. Jafari and N. Jafari Rad, “Domination in the intersection graphs of rings and modules,” *Italian Journal of Pure and Applied Mathematics* 28 (2011), 17–20. First public journal date: 19 July 2011. Classification listed first: \(16\mathrm{BXX}\).
2. E. Abu Osba, S. Al-Addasi, and O. Abughneim, “Some Properties of the Intersection Graph for Finite Commutative Principal Ideal Rings,” *International Journal of Combinatorics* (2014), Article 952371. DOI: 10.1155/2014/952371.
3. D. L. Boutin, “Identifying Graph Automorphisms Using Determining Sets,” *Electronic Journal of Combinatorics* 13 (2006), R78. DOI: 10.37236/1104.
4. M. O. Albertson and K. L. Collins, “Symmetry Breaking in Graphs,” *Electronic Journal of Combinatorics* 3 (1996), R18. DOI: 10.37236/1242.
5. F. Xu, D. Wong, and F. Tian, “Automorphism group of the intersection graph of ideals over a matrix ring,” *Linear and Multilinear Algebra* 70 (2022), 322–330. DOI: 10.1080/03081087.2020.1723473.
