# Zero forcing polynomials recognize nonreduced three-factor co-maximal ideal graphs

## Finding

Let \(R\cong R_1\times R_2\times R_3\) be a finite commutative ring with exactly three local factors, and let \(\lambda_i\ge1\) be the number of proper ideals of \(R_i\). Assume that at least one \(R_i\) is not a field, equivalently at least one \(\lambda_i>1\). Put \[N=\lambda_1+\lambda_2+\lambda_3+\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3.\] For the co-maximal ideal graph \(\mathcal C(R)\), \[\mathcal Z(\mathcal C(R);u)=u^{N-6}\prod_{i=1}^3(u+\lambda_i)\prod_{1\le i<j\le3}(u+\lambda_i\lambda_j).\] Hence \(Z(\mathcal C(R))=M(\mathcal C(R))=N-6\), \(\operatorname{mr}(\mathcal C(R))=6\), and the minimum zero forcing sets are exactly the complements of one vertex from each of the six Boolean blow-up classes, so their number is \((\lambda_1\lambda_2\lambda_3)^3\). Moreover the polynomial recovers the unordered triple \(\{\lambda_1,\lambda_2,\lambda_3\}\), and therefore it determines \(\mathcal C(R)\) up to graph isomorphism within this three-local-factor nonreduced class. For products of three finite chain rings, it consequently recovers the multiset of nilpotency lengths.

The reconstruction is explicit. After removing the zero root, take the absolute values of the six negative roots and sort them as
\[
r_1\le r_2\le\cdots\le r_6.
\]
Then, after sorting
\[
\lambda_1\le\lambda_2\le\lambda_3,
\]
one has
\[
\lambda_1=r_1,\qquad
\lambda_2=r_2,
\]
and
\[
\lambda_3=
\frac{\left(\prod_{j=1}^{6}r_j\right)^{1/3}}{r_1r_2}.
\]

## Assumptions and scope

Let \(R\) be a finite commutative ring with exactly three maximal ideals. Its Artinian decomposition is
\[
R\cong R_1\times R_2\times R_3
\]
with \(R_i\) finite local rings.

Write
\[
\lambda_i=\#\{\text{proper ideals of }R_i\}.
\]
A field has \(\lambda_i=1\). The hypothesis in the finding is that not all three factors are fields.

The co-maximal ideal graph \(\mathcal C(R)\) has as vertices the proper ideals not contained in the Jacobson radical, with two distinct vertices adjacent exactly when their sum is \(R\).

For a graph \(G\),
\[
\mathcal Z(G;u)=\sum_k z(G;k)u^k
\]
is the zero forcing polynomial. The real symmetric maximum nullity and minimum rank are denoted by \(M(G)\) and \(\operatorname{mr}(G)\).

## Proof

Ye, Wu, Liu, and Yu prove that for
\[
R\cong R_1\times\cdots\times R_n
\]
with local factors having \(\lambda_i\) proper ideals, the co-maximal ideal graph is a blow-up of the Boolean graph \(B_n\), and the class indexed by a nonempty proper subset \(S\subset[n]\) has size
\[
\prod_{i\in S}\lambda_i.
\tag{1}
\]

For \(n=3\), label the singleton classes by
\[
C_1,C_2,C_3
\]
and the opposite doubleton classes by
\[
L_1,L_2,L_3,
\]
where \(L_i\) corresponds to the two-element subset \([3]\setminus\{i\}\). Their sizes are
\[
|C_i|=\lambda_i,
\qquad
|L_i|=\lambda_j\lambda_k
\quad
(\{i,j,k\}=\{1,2,3\}).
\tag{2}
\]

The Boolean graph \(B_3\) has a triangle on \(C_1,C_2,C_3\), and \(L_i\) is adjacent only to \(C_i\). Blow-up classes are independent sets, with complete joins exactly along these six quotient edges.

Every class in (2) is a false-twin class. Therefore a zero forcing set may leave at most one white vertex in each class: if two vertices of one class were white, every vertex outside the class would see either both or neither, so neither could be the first one forced.

We prove the converse under the non-field hypothesis. Relabel so that
\[
\lambda_3>1.
\]
Then the classes
\[
C_3,\quad L_1,\quad L_2
\]
all have size at least two and hence contain a blue vertex even when one representative is left white.

Start with any coloring having at most one white vertex in each of the six classes. The blue representatives in \(L_1\) and \(L_2\) first force any white representatives in \(C_1\) and \(C_2\).

If \(L_3\) contains a blue vertex, it similarly forces any white representative in \(C_3\). The only case where \(L_3\) may have no blue representative is
\[
\lambda_1=\lambda_2=1
\]
with its unique vertex white. After \(C_1\) and \(C_2\) are blue, a blue vertex of \(C_3\) has that \(L_3\)-vertex as its unique white neighbor, so it forces \(L_3\); then \(L_3\) forces a possible white representative of \(C_3\).

At this point every core class \(C_i\) is fully blue. A blue vertex in \(C_i\) then forces the possible remaining white representative in \(L_i\). Thus every coloring with at most one white vertex per class is zero forcing.

Consequently, a zero forcing set is obtained independently in each class by either taking the entire class or omitting exactly one vertex. A class of size \(w\) contributes
\[
u^w+w u^{w-1}
=
u^{w-1}(u+w)
\]
to the polynomial. Multiplying the six factors in (2) gives
\[
\mathcal Z(\mathcal C(R);u)
=
u^{N-6}
\prod_{i=1}^{3}(u+\lambda_i)
\prod_{1\le i<j\le3}(u+\lambda_i\lambda_j).
\tag{3}
\]

The least exponent is
\[
Z(\mathcal C(R))=N-6,
\]
and its coefficient is the product of the six class sizes,
\[
(\lambda_1\lambda_2\lambda_3)^3.
\]

For minimum rank, let \(H\) be the adjacency matrix of the six-vertex Boolean graph \(B_3\), ordered as
\[
C_1,C_2,C_3,L_1,L_2,L_3.
\]
Explicitly,
\[
H=
\begin{pmatrix}
0&1&1&1&0&0\\
1&0&1&0&1&0\\
1&1&0&0&0&1\\
1&0&0&0&0&0\\
0&1&0&0&0&0\\
0&0&1&0&0&0
\end{pmatrix},
\]
and
\[
\det H=-1.
\]
Replacing each entry of \(H\) by the corresponding constant block produces the adjacency matrix of \(\mathcal C(R)\). Since every blow-up class is nonempty, this block matrix has rank \(6\). Hence
\[
\operatorname{mr}(\mathcal C(R))\le6.
\]
The standard inequality
\[
M(G)\le Z(G)
\]
gives
\[
\operatorname{mr}(\mathcal C(R))
=
N-M(\mathcal C(R))
\ge N-Z(\mathcal C(R))
=6.
\]
Therefore
\[
\operatorname{mr}(\mathcal C(R))=6
\]
and
\[
M(\mathcal C(R))=Z(\mathcal C(R))=N-6.
\]

Finally, (3) determines the local ideal counts. Sort
\[
\lambda_1\le\lambda_2\le\lambda_3.
\]
The six nonzero root magnitudes form the multiset
\[
\{\lambda_1,\lambda_2,\lambda_3,
\lambda_1\lambda_2,\lambda_1\lambda_3,\lambda_2\lambda_3\}.
\tag{4}
\]
Because every \(\lambda_i\ge1\), the two smallest entries of (4), with multiplicity, are
\[
\lambda_1,\lambda_2.
\]
Also the product of all six entries is
\[
(\lambda_1\lambda_2\lambda_3)^3.
\]
Thus the displayed recovery formula gives \(\lambda_3\).

The blow-up description (1) depends only on the unordered triple of local proper-ideal counts, so equal zero forcing polynomials imply isomorphic co-maximal ideal graphs in this class. The converse is automatic.

If \(R_i\) is a finite chain ring of nilpotency length \(\ell_i\), then it has exactly \(\ell_i\) proper ideals. Hence the polynomial recovers
\[
\{\ell_1,\ell_2,\ell_3\}.
\]

## Verification

The accompanying `verify.py` constructs the six-class blow-up directly and also independently constructs the co-maximal ideal graph at the ideal level for products of three prime-power chain rings.

It exhaustively reproduces the complete zero forcing polynomial in the representative regimes
\[
(\lambda_1,\lambda_2,\lambda_3)
=
(1,1,2),\quad
(1,2,2),\quad
(2,2,2).
\]
These include the sharp boundary with two field factors.

For each case it checks the six class sizes, every adjacency, the least coefficient, and the exact rank \(6\) of the adjacency witness by rational row reduction.

The recovery formula is checked for every ordered triple
\[
1\le\lambda_1\le\lambda_2\le\lambda_3\le8
\]
except the all-field triple. The least-redundant boundary
\[
(1,1,3)
\]
is also checked profile-by-profile: all \(64\) ways of leaving at most one white representative in each of the six classes force successfully.

Exact replay output:

```text
l=(1, 1, 2): weights=[1, 1, 2, 2, 2, 1], N=9, Z=3, min_sets=8, adjacency_rank=6
l=(1, 2, 2): weights=[1, 2, 2, 4, 2, 2], N=13, Z=7, min_sets=64, adjacency_rank=6
l=(2, 2, 2): weights=[2, 2, 2, 4, 4, 4], N=18, Z=12, min_sets=512, adjacency_rank=6
RECOVERY_CENSUS_OK
ALL_64_PROFILES_FORCE_OK
VERIFY_OK
```

The finite checks corroborate the symbolic proof. The reconstruction theorem and arbitrary-ring statement do not rely on finite enumeration.

## Relationship to prior work

Ye and Wu introduced the co-maximal ideal graph and established its basic graph-theoretic properties. Their article has primary classification \(13A15\).

Ye, Wu, Liu, and Yu subsequently proved the decisive structural statement used here: a co-maximal ideal graph with finitely many maximal ideals is a blow-up of a Boolean graph, and for a product of local rings the blow-up class indexed by \(S\) has size \(\prod_{i\in S}\lambda_i\). Their full text does not discuss zero forcing or minimum rank.

A recent general modular-compression theorem for zero forcing polynomials shows that forcing polynomials of bounded-neighborhood-diversity graphs can be reduced exactly to their type graphs. That theorem subsumes the generic false-twin compression underlying (3), so the existence of a type-profile formula alone is not claimed as new here. The present strengthened statement identifies the complete factorization for the three-local co-maximal family, proves the sharp rank equality, and, crucially, proves that the polynomial itself recovers the local ideal-count triple and therefore the graph.

Boyer and collaborators introduced the zero forcing polynomial and developed its general structural theory. Their work supplies the polynomial framework but does not specialize to co-maximal ideal graphs or recover local ideal counts.

## Limitations

The theorem assumes exactly three local factors and excludes the product-of-three-fields case. When all
\[
\lambda_i=1,
\]
the graph is the unblown Boolean graph \(B_3\), and the factorization (3) does not hold.

The polynomial recovers the numbers of proper ideals in the local factors, not the local rings themselves. Different finite local rings can have the same number of proper ideals.

For finite chain rings the proper-ideal count equals the nilpotency length, so the stronger chain-length recovery conclusion applies.

The minimum rank is over real symmetric graph-pattern matrices.

The modular-compression component of the polynomial calculation has broader recent coverage; the originality claim is the co-maximal specialization together with exact algebraic parameter recovery and the rank conclusion.

## References

1. M. Ye and T. Wu, “Co-Maximal Ideal Graphs of Commutative Rings,” *Journal of Algebra and Its Applications* 11 (2012), 1250114. DOI: 10.1142/S0219498812501149. Published 9 November 2012.
2. M. Ye, T. Wu, Q. Liu, and H. Yu, “Implements of Graph Blow-Up in Co-Maximal Ideal Graphs,” *Communications in Algebra* 42 (2014), 2476–2483. DOI: 10.1080/00927872.2012.762924.
3. X. Wang, “Modular Compression of Leaky Forts and Leaky Forcing Polynomials,” preprint, 26 May 2026. DOI: 10.5281/zenodo.20388397.
4. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033.
5. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
