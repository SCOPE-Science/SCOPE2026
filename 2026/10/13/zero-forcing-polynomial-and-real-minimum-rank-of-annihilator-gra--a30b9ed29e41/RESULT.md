# Zero forcing polynomial and real minimum rank of annihilator graphs of three equal finite fields

## Finding

Let \(q\) be a prime power and \(R=\mathbb F_q\times\mathbb F_q\times\mathbb F_q\). For Badawi's annihilator graph \(AG(R)\) on the nonzero zero-divisors, put \(a=(q-1)^2\), \(b=q-1\), and \(N=3q(q-1)\). If \(q\ge3\), define \(e_2=3a^2+9ab+3b^2\) and \(e_3=a^3+9a^2b+9ab^2+b^3\). Then \[\mathcal Z(AG(R);u)=3ab(a+b)^2u^{N-4}+e_3u^{N-3}+e_2u^{N-2}+Nu^{N-1}+u^N,\] and, over real symmetric graph-pattern matrices, \[Z(AG(R))=M(AG(R))=N-4,\qquad \operatorname{mr}(AG(R))=4.\] Every minimum zero forcing set is obtained by leaving one white vertex in four of the six annihilator-support classes, where the four selected classes are one of exactly twelve forcing four-class profiles; hence there are \(3ab(a+b)^2=3q^2(q-1)^5\) minimum sets. For \(q=2\), \(AG(R)\) is the triangular prism and \(\mathcal Z(AG(R);u)=14u^3+15u^4+6u^5+u^6\), with \(Z=M=3\) and \(\operatorname{mr}=3\).

For \\(q\\ge3\\), the real minimum rank remains exactly \\(4\\) while the graph order \\(3q(q-1)\\) grows without bound. The polynomial records the complete count of forcing sets at every possible size, not only the minimum.

## Assumptions and scope

Let
\\[
R=\\mathbb F_q^3.
\\]
Badawi's annihilator graph \\(AG(R)\\) has as vertices the nonzero zero-divisors of \\(R\\), with distinct vertices \\(x,y\\) adjacent when
\\[
\\operatorname{ann}(xy)\\ne\\operatorname{ann}(x)\\cup\\operatorname{ann}(y).
\\]

Afkhami, Khashyarmanesh, and Rajabi give the exact six-class decomposition for a product of three fields. Specializing to equal fields, write
\\[
A_1,A_2,A_3
\\]
for the zero-divisors having exactly one zero coordinate and
\\[
A_4,A_5,A_6
\\]
for those having exactly two zero coordinates. Then
\\[
|A_1|=|A_2|=|A_3|=a=(q-1)^2,
\\qquad
|A_4|=|A_5|=|A_6|=b=q-1.
\\]
Every \\(A_i\\) is independent, and the class adjacency is
\\[
\begin{aligned}
N(A_1)&=\\{A_2,A_3,A_6\\},&N(A_2)&=\\{A_1,A_3,A_5\\},\\\\
N(A_3)&=\\{A_1,A_2,A_4\\},&N(A_4)&=\\{A_3,A_5,A_6\\},\\\\
N(A_5)&=\\{A_2,A_4,A_6\\},&N(A_6)&=\\{A_1,A_4,A_5\\}.
\end{aligned}
\\tag{1}
\\]
Thus the six-class quotient is the triangular prism, and
\\[
N=|V(AG(R))|=3a+3b=3q(q-1).
\\]

## Proof

Assume first that \\(q\\ge3\\), so each of the six false-twin classes has at least two vertices. A zero forcing set cannot leave two white vertices in one class: those two false twins form a fort, because every vertex outside the pair sees either both or neither. Hence any forcing coloring leaves at most one white representative in each \\(A_i\\).

Conversely, if at most one white vertex is left per class, every class has a blue representative. Therefore forcing depends only on the set \\(W\\) of white class labels. A blue representative of class \\(A_i\\) can force exactly when its class has precisely one neighbor in \\(W\\). After that force, the corresponding label is deleted from \\(W\\). Thus the problem is the finite peeling process on the six-vertex quotient in (1).

A direct class-level analysis gives:

- every label subset of size at most \\(3\\) peels completely;
- among the \\(15\\) four-label subsets, exactly \\(12\\) peel completely;
- no five- or six-label subset peels.

For the twelve forcing four-label profiles, exactly three contain one of \\(A_1,A_2,A_3\\), six contain two, and three contain all three. Therefore the maximum number of initially white vertices is \\(4\\), and
\\[
Z(AG(R))=N-4.
\\tag{2}
\\]
The number of minimum forcing sets is
\\[
3ab^3+6a^2b^2+3a^3b
=3ab(a+b)^2
=3q^2(q-1)^5.
\\tag{3}
\\]

All two-label and three-label profiles peel, so weighting each white profile by the number of choices of its representatives gives
\\[
e_2=3a^2+9ab+3b^2
\\]
and
\\[
e_3=a^3+9a^2b+9ab^2+b^3.
\\]
Together with the unique all-blue set and the \\(N\\) ways to leave one vertex white, (2)--(3) give
\\[
\\mathcal Z(AG(R);u)
=3ab(a+b)^2u^{N-4}
+e_3u^{N-3}
+e_2u^{N-2}
+Nu^{N-1}
+u^N.
\\tag{4}
\\]

For real minimum rank, let \\(B\\) be the \\(6\\times6\\) adjacency matrix of the triangular-prism class graph in (1). Exact row reduction gives
\\[
\\operatorname{rank}_{\\mathbb R}B=4.
\\]
Blow up the \\(i\\)-th row and column of \\(B\\) according to \\(|A_i|\\). The resulting symmetric matrix has zero off-diagonal entries exactly at nonedges of \\(AG(R)\\), nonzero entries exactly at edges, and still has rank \\(4\\). Hence
\\[
\\operatorname{mr}(AG(R))\\le4.
\\]
The standard inequality \\(M(G)\\le Z(G)\\), together with (2), implies
\\[
N-\\operatorname{mr}(AG(R))\\le N-4,
\\]
so \\(\\operatorname{mr}(AG(R))\\ge4\\). Therefore
\\[
\\operatorname{mr}(AG(R))=4,
\\qquad
M(AG(R))=Z(AG(R))=N-4.
\\]

Now let \\(q=2\\). Each class in (1) is a singleton, so \\(AG(R)\\) is the triangular prism itself. Every two-white set is forcing because the prism has no twin pair. For three white vertices, exactly six of the twenty triples are forts; the other fourteen have an outside vertex with a unique white neighbor and then reduce to the two-white case. Thus
\\[
\\mathcal Z(AG(R);u)=14u^3+15u^4+6u^5+u^6.
\\]
In particular, \\(Z=3\\). A rank-three real Gram witness is obtained from the vectors
\\[
(1,0,0),(0,1,0),(1,0,1),(1,1,-1),(1,2,3),(0,3,-2),
\\]
ordered so that the six zero pairings are exactly a six-cycle, the complement of the triangular prism. Hence \\(\\operatorname{mr}\\le3\\); the inequality \\(M\\le Z\\) gives the reverse bound, so \\(\\operatorname{mr}=3\\) and \\(M=Z=3\\).

## Verification

The accompanying `verify.py` first checks the six-class peeling census exactly: all \\(20\\) three-class profiles peel, precisely \\(12\\) of the \\(15\\) four-class profiles peel, and none of the larger profiles does.

For \\(q=2\\) and \\(q=3\\), it then constructs \\(\\mathbb F_q^3\\) element by element, computes every annihilator directly, applies Badawi's defining adjacency test, verifies the published six-class quotient, and exhaustively enumerates every zero forcing set. The resulting complete polynomials agree with (4) and with the triangular-prism boundary.

For \\(q=4,5,7\\), it checks the weighted class formulas and the real symmetric rank witnesses. All ranks are computed by exact rational row reduction.

Exact replay output:

```text
type_profile_counts= {0: 1, 1: 6, 2: 15, 3: 20, 4: 12, 5: 0, 6: 0} size4_Aclass_distribution= (3, 6, 3)
q=2: N=6, class_sizes=[1, 1, 1, 1, 1, 1], polynomial={3: 14, 4: 15, 5: 6, 6: 1}, witness_rank=3
q=3: N=18, class_sizes=[4, 4, 4, 2, 2, 2], polynomial={14: 864, 15: 504, 16: 132, 17: 18, 18: 1}, witness_rank=4
q=4: N=36, class_sizes=[9, 9, 9, 3, 3, 3], predicted_polynomial={32: 11664, 33: 3672, 34: 513, 35: 36, 36: 1}, witness_rank=4
q=5: N=60, class_sizes=[16, 16, 16, 4, 4, 4], predicted_polynomial={56: 76800, 57: 15680, 58: 1392, 59: 60, 60: 1}, witness_rank=4
q=7: N=126, class_sizes=[36, 36, 36, 6, 6, 6], predicted_polynomial={122: 1143072, 123: 128520, 124: 5940, 125: 126, 126: 1}, witness_rank=4
VERIFY_OK
```

The finite calculations corroborate the proof. The arbitrary-prime-power theorem follows from the published six-class structure, the complete finite quotient peeling analysis, and the rank witness.

## Relationship to prior work

Badawi introduced the annihilator graph and established its basic structural theory. The original article has primary Mathematics Subject Classification \\(13A15\\), and it contains no zero-forcing or minimum-rank result.

Afkhami, Khashyarmanesh, and Rajabi explicitly decompose the annihilator graph of a product of three fields into the six independent classes used in (1), and prove that its clique and chromatic numbers are both \\(3\\). Their decomposition is prior structural coverage and is not claimed here.

Boyer and collaborators introduced the zero forcing polynomial and give general formulas for several graph families. Their full text contains no triangular-prism or blow-up specialization. Targeted searches under annihilator-graph, product-of-three-fields, triangular-prism blow-up, false-twin blow-up, minimum-rank, maximum-nullity, and zero-forcing-polynomial formulations did not locate (4) or the constant-rank conclusion.

The general inequality \\(M(G)\\le Z(G)\\) comes from the AIM Minimum Rank -- Special Graphs Work Group. The ring-specific content here is the complete weighted forcing census on the six annihilator classes and the resulting exact rank-four realization for every \\(q\\ge3\\).

## Limitations

The theorem treats three equal finite field factors. Products of three unequal fields have the same six-class quotient but unequal class sizes of a more general form; no formula for that larger parameter family is claimed here.

The minimum rank is over real symmetric graph-pattern matrices. Other coefficient fields are not covered.

The published six-class graph decomposition is prior work. The new claim is the complete zero forcing polynomial, all minimum forcing sets, and the exact real minimum rank/maximum nullity consequences.

The \\(q=2\\) triangular-prism boundary is separated because the false-twin classes become singletons.

## References

1. A. Badawi, “On the Annihilator Graph of a Commutative Ring,” *Communications in Algebra* 42 (2014), 108–121. DOI: 10.1080/00927872.2012.707262. Published online 18 October 2013.
2. M. Afkhami, K. Khashyarmanesh, and Z. Rajabi, “Some results on the annihilator graph of a commutative ring,” *Czechoslovak Mathematical Journal* 67 (2017), 151–169. DOI: 10.21136/CMJ.2017.0436-15. First published 24 February 2017.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033; arXiv:1801.08910.
4. AIM Minimum Rank -- Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
