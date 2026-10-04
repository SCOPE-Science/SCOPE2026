# Domination of the underlying zero-divisor graph of \(M_2(\mathbb F_q)\)

## Finding

Let \(q\) be a prime power and let \(\overline{\Gamma}(M_2(\mathbb F_q))\) be the simple undirected zero-divisor graph whose vertices are the nonzero singular matrices and whose distinct vertices \(A,B\) are adjacent exactly when \(AB=0\) or \(BA=0\). Then \[\gamma\!\left(\overline{\Gamma}(M_2(\mathbb F_q))\right)=\begin{cases}2,&q=2,\\ q+1,&q>2.\end{cases}\] Thus forgetting the directions in the standard directed matrix zero-divisor graph strictly lowers the domination number only in the binary \(2\times2\) case.

The proof also gives a structural model of the graph as a scalar blow-up of a graph on ordered pairs of projective lines.

## Assumptions and scope

Let \(F=\mathbb F_q\), let \(V=F^2\), and let \(\mathcal P=\mathbb P^1(F)\), so
\[
|\mathcal P|=q+1.
\]
The graph \(\overline{\Gamma}(M_2(F))\) has as vertices the nonzero singular matrices. Two distinct matrices \(A\) and \(B\) are adjacent when
\[
AB=0\quad\text{or}\quad BA=0.
\]

Every vertex has rank one. For \(L,K\in\mathcal P\), define
\[
\mathcal F_{L,K}
=
\{A:\operatorname{im}A=L,\ \ker A=K\}.
\]
Since a rank-one map with fixed image and kernel is a nonzero scalar multiple of any one such map,
\[
|\mathcal F_{L,K}|=q-1.
\]

## Proof

Take
\[
A\in\mathcal F_{L,K},
\qquad
B\in\mathcal F_{L',K'}.
\]
Because both maps have rank one,
\[
AB=0
\iff
\operatorname{im}B\subseteq\ker A
\iff
L'=K,
\]
and similarly
\[
BA=0
\iff
L=K'.
\]
Hence, for distinct matrices,
\[
A\sim B
\iff
L'=K\ \text{or}\ L=K'.
\tag{1}
\]

In particular, a diagonal fiber \(\mathcal F_{L,L}\) is a clique, while an off-diagonal fiber \(\mathcal F_{L,K}\) with \(L\ne K\) is independent.

For the upper bound, choose one representative \(D_L\in\mathcal F_{L,L}\) for every \(L\in\mathcal P\). There are \(q+1\) representatives. Every vertex in a diagonal fiber is dominated inside that fiber, and every vertex of an off-diagonal fiber \(\mathcal F_{L,K}\) is adjacent to both \(D_L\) and \(D_K\). Therefore
\[
\gamma\!\left(\overline{\Gamma}(M_2(F))\right)\le q+1.
\tag{2}
\]

Now assume \(q>2\), and suppose that a dominating set \(D\) has size at most
\[
m-1,
\qquad m=q+1.
\]
Let \(S\subseteq\mathcal P\times\mathcal P\) be the set of projective types represented by \(D\), and put
\[
k=|S|\le |D|\le m-1.
\]
Let \(\mathcal A\) be the set of first coordinates occurring in \(S\), and let \(\mathcal B\) be the set of second coordinates occurring in \(S\). Define
\[
X=\mathcal P\setminus\mathcal B,
\qquad
Y=\mathcal P\setminus\mathcal A.
\]
Both \(X\) and \(Y\) are nonempty because \(|\mathcal A|,|\mathcal B|\le k<m\).

If a type \((x,y)\in X\times Y\) were absent from \(S\), then by (1) no vertex of its fiber would be adjacent to any vertex of \(D\). Thus
\[
X\times Y\subseteq S.
\tag{3}
\]
Since \(X\) and \(Y\) are nonempty, (3) also forces
\[
X\cap Y=\varnothing.
\]
Write
\[
a=|X|,
\qquad
b=|Y|,
\qquad
c=m-a-b.
\]
The complement \(C=\mathcal P\setminus(X\cup Y)\) equals \(\mathcal A\cap\mathcal B\). The rectangle \(X\times Y\) accounts for \(ab\) represented types. Every line of \(C\) must still occur as a first coordinate and as a second coordinate among the remaining represented types, so at least \(c\) further types are needed. Consequently
\[
k\ge ab+c
=
m-1+(a-1)(b-1)
\ge m-1.
\tag{4}
\]
Together with \(k\le |D|\le m-1\), equality holds everywhere. Hence
\[
k=|D|=m-1,
\]
and either \(a=1\) or \(b=1\). Equality also means that exactly one vertex of \(D\) lies in each represented fiber, and the \(c\) represented types outside \(X\times Y\) have both coordinates in \(C\).

Choose any \((x,y)\in X\times Y\). It is off-diagonal because \(X\cap Y=\varnothing\). By (1), it is adjacent to no other type in the rectangle and to no represented type with both coordinates in \(C\). Therefore the selected vertex of \(\mathcal F_{x,y}\) has no selected type-neighbor. Since \(q>2\),
\[
|\mathcal F_{x,y}|=q-1\ge2,
\]
so there is an unselected vertex in the same independent fiber. That vertex is adjacent to no member of \(D\), contradicting domination. Thus
\[
\gamma\!\left(\overline{\Gamma}(M_2(F))\right)\ge q+1
\]
for \(q>2\). With (2),
\[
\gamma\!\left(\overline{\Gamma}(M_2(\mathbb F_q))\right)=q+1
\qquad(q>2).
\]

It remains to handle \(q=2\). Then every fiber has one vertex and \(|\mathcal P|=3\). Write
\[
\mathcal P=\{c,x,y\}.
\]
The two vertices of types
\[
(c,c)
\quad\text{and}\quad
(x,y)
\]
dominate all nine projective types: the first dominates every type having first or second coordinate \(c\), and the second dominates every remaining type. Hence
\[
\gamma\!\left(\overline{\Gamma}(M_2(\mathbb F_2))\right)\le2.
\]
No vertex is universal: given a type \((L,K)\), choose a projective line \(M\) distinct from both \(L\) and \(K\) when they differ, or merely distinct from \(L=K\) otherwise; then the diagonal type \((M,M)\) is nonadjacent to \((L,K)\). Thus the domination number is exactly \(2\).

## Verification

The accompanying `verify.py` performs two independent finite checks.

First, it constructs the actual matrix graph arithmetically over \(\mathbb F_2\) and \(\mathbb F_3\), tests every candidate dominating set up to the proved optimum, and obtains
\[
|V(\overline{\Gamma}(M_2(\mathbb F_2)))|=9,\qquad \gamma=2,
\]
and
\[
|V(\overline{\Gamma}(M_2(\mathbb F_3)))|=32,\qquad \gamma=4.
\]

Second, it exhaustively checks the projective-type lower-bound mechanism for \(q\in\{2,3,4,5\}\). The exact output is:

```text
VERIFY_OK
actual_q2_vertices=9 gamma=2
actual_q3_vertices=32 gamma=4
projective_support_checks=q2,q3,q4,q5
theorem_values=q2:2,q3:4,q4:5,q5:6
```

These computations are corroborative. The theorem for arbitrary prime powers is proved by the projective-line argument above.

## Relationship to prior work

Božić and Petrović studied directed zero-divisor graphs of matrix rings and their diameter. The matrix-ring topic is classified under MSC \(16S50\).

Jafari and Jafari Rad later studied domination for the directed graph. For a finite field of order \(q\) and dimension \(n\), their Theorem 2.7 and Corollary 2.9 give directed out- and in-domination number
\[
\frac{q^n-1}{q-1}.
\]
For \(n=2\), this equals \(q+1\).

That directed result does not imply the present undirected lower bound: passing to the underlying undirected graph adds every reverse arc as an edge and can reduce domination. The binary case proves that the reduction can be strict:
\[
q+1=3
\quad\text{directed, but}\quad
\gamma=2
\quad\text{underlying undirected}.
\]
For \(q>2\), the present projective-fiber argument proves that no reduction occurs.

A later survey explicitly records the noncommutative undirected convention used here—two vertices are adjacent when either product vanishes—and surveys the directed matrix zero-divisor literature. Targeted searches for domination of this underlying undirected matrix graph did not locate the formula above.

## Limitations

The theorem treats \(2\times2\) full matrix rings over finite fields. It does not give the domination number for \(M_n(\mathbb F_q)\) when \(n\ge3\), for matrix rings over nonfields, or for other undirected symmetrizations.

The originality comparison is strongest against the directed matrix-domination literature and the surveyed matrix-graph literature. An unindexed paper using the older undirected noncommutative convention could still contain the same \(2\times2\) formula.

## References

1. I. Božić and Z. Petrović, “Zero-Divisor Graphs of Matrices Over Commutative Rings,” *Communications in Algebra* 37 (2009), 1186–1192. DOI: 10.1080/00927870802465951.
2. S. H. Jafari and N. Jafari Rad, “On Domination of Zero-divisor Graphs of Matrix Rings,” *Canadian Mathematical Bulletin* 58 (2015), 271–275. DOI: 10.4153/CMB-2015-017-6.
3. “Graphs from matrices — a survey,” *AKCE International Journal of Graphs and Combinatorics* (2024). DOI: 10.1080/09728600.2024.2332780.
