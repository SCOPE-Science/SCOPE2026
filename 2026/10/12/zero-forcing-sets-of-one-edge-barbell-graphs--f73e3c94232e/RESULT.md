# Zero forcing sets of one-edge barbell graphs

## Finding
For integers \(p,q\ge3\), form \(B_{p,q}\) from two disjoint cliques
\[
A=\{a\}\cup X\cong K_p,\qquad B=\{b\}\cup Y\cong K_q,
\]
by adding the single edge \(ab\), and no other edge between the two cliques. For an initial blue set \(S\), write \(W=V(B_{p,q})\setminus S\) for the initially white vertices.

Then \(S\) is a zero forcing set if and only if
\[
|W|\le3,\qquad |W\cap X|\le1,\qquad |W\cap Y|\le1.
\]
Therefore the full zero forcing polynomial is
\[
\mathcal Z(B_{p,q};z)
=(2pq-p-q)z^{p+q-3}
+(pq+p+q-2)z^{p+q-2}
+(p+q)z^{p+q-1}
+z^{p+q}.
\]
In particular,
\[
Z(B_{p,q})=p+q-3,
\]
and the number of minimum zero forcing sets is \(2pq-p-q\). Equivalently, a minimum set is the complement of one of the following four kinds of white triples:
\[
\{a,b,x\},\quad \{a,b,y\},\quad \{a,x,y\},\quad \{b,x,y\},
\]
where \(x\in X\) and \(y\in Y\) whenever they occur.

## Assumptions and scope
Graphs are finite, simple, and undirected. Zero forcing uses the standard color-change rule: a blue vertex with exactly one white neighbor forces that neighbor blue. The theorem assumes \(p,q\ge3\). It concerns the one-edge barbell defined above; it does not assert the same formula for variants in which the two cliques are joined by a longer path. It also does not address positive-semidefinite, skew, signed, or other forcing variants.

## Proof
First suppose two distinct vertices \(x_1,x_2\in X\) are white. Every vertex adjacent to either lies in the clique \(A\). While both remain white, every blue vertex of \(A\) adjacent to one is adjacent to both, so no blue vertex can force either one. Vertices outside \(A\) cannot force them because they are not adjacent to them. Hence no zero forcing set can leave two vertices of \(X\) white. Thus \(|W\cap X|\le1\). By symmetry, \(|W\cap Y|\le1\).

Under these two restrictions, four white vertices are possible only in the form \(W=\{a,b,x,y\}\) with \(x\in X\) and \(y\in Y\). This configuration has no legal first force: every blue vertex of \(X\) sees the two white neighbors \(a,x\), and every blue vertex of \(Y\) sees the two white neighbors \(b,y\). Hence a zero forcing set must also satisfy \(|W|\le3\).

Conversely, assume \(|W|\le3\), \(|W\cap X|\le1\), and \(|W\cap Y|\le1\). The cases \(|W|\le1\) are immediate. For \(|W|=2\), the possible location types are
\[
\{a,b\},\ \{a,x\},\ \{a,y\},\ \{b,x\},\ \{b,y\},\ \{x,y\}.
\]
For \(\{a,b\}\), a blue vertex of \(X\) forces \(a\), after which \(a\) forces \(b\). For \(\{a,x\}\), \(b\) forces \(a\) and then a blue vertex of \(X\) forces \(x\). The cases \(\{b,y\}\), \(\{a,y\}\), and \(\{b,x\}\) are symmetric variants, while for \(\{x,y\}\) a blue vertex in each clique can force its white internal vertex. The hypotheses \(p,q\ge3\) ensure that the needed blue internal vertices exist.

For \(|W|=3\), the restrictions leave exactly four location types:
\[
\{a,b,x\},\quad \{a,b,y\},\quad \{a,x,y\},\quad \{b,x,y\}.
\]
If \(W=\{a,b,x\}\), any blue vertex of \(Y\) forces \(b\), then \(b\) forces \(a\), then a blue vertex of \(X\) forces \(x\). If \(W=\{a,x,y\}\), a blue vertex of \(Y\setminus\{y\}\) forces \(y\), then \(b\) forces \(a\), then a blue vertex of \(X\setminus\{x\}\) forces \(x\). The other two cases are symmetric. Thus every set satisfying the three displayed restrictions is zero forcing.

It remains to count. Admissible white triples have the four types above, giving
\[
(p-1)+(q-1)+2(p-1)(q-1)=2pq-p-q.
\]
Admissible white pairs are all pairs except two internal vertices of \(X\) or two internal vertices of \(Y\), so their number is
\[
\binom{p+q}{2}-\binom{p-1}{2}-\binom{q-1}{2}=pq+p+q-2.
\]
There are \(p+q\) admissible one-vertex complements and one empty complement. These counts give the stated polynomial and show that its least exponent is \(p+q-3\).

## Verification
The proof above is uniform in \(p,q\). As a finite corroboration, `verify_barbell_zero_forcing.py` exhaustively checks every subset for all \(3\le p,q\le6\), compares direct zero forcing closure with the theorem's complement criterion, and checks every polynomial coefficient and every minimum set. Its deterministic output is:

`VERIFY_OK parameter_pairs=16 subset_checks=14400 minimum_checks=504 max_order=12`

The exhaustive computation is not used as a proof for arbitrary \(p,q\); the analytic obstruction and force sequences establish the theorem.

## Relationship to prior work
The standard zero forcing parameter and color-change rule originate in the AIM Minimum Rank--Special Graphs Work Group paper, which was publicly available online on 26 November 2007 and is classified under AMS 05C50. Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart later introduced the zero forcing polynomial and proved generic formulas for its top coefficients. Their Theorem 1 already explains the coefficients at degrees \(p+q\), \(p+q-1\), and, after evaluating the neighborhood condition, \(p+q-2\). The barbell-specific contribution here is the exact all-set complement criterion, including the first nonzero coefficient at degree \(p+q-3\), the complete minimum-set classification, and its count \(2pq-p-q\).

Row developed a general cut-vertex technique for computing zero forcing numbers. That source is directly relevant because \(B_{p,q}\) has cut vertices, and it may subsume the scalar value \(Z(B_{p,q})\). The accessible bibliographic material does not state an all-minimum-set classification or counting polynomial. Accordingly, no originality is asserted for the scalar value in isolation; the retained statement is the structural classification and resulting enumeration.

Searches using the aliases “barbell”, “dumbbell”, and “two cliques joined by one edge”, together with searches for the exact minimum-set count and zero forcing polynomial, did not locate a prior statement equivalent to the complement criterion above. The full searchable arXiv text of the zero forcing polynomial paper was inspected in its extremal-coefficient and graph-family sections and contains no occurrence of “barbell” or “dumbbell”.

## Limitations
The theorem is limited to \(p,q\ge3\) and a single bridge edge. The cases with a clique of order below three can have different helper-vertex behavior and are not included. A longer path between the cliques is a different family. The 2012 cut-vertex paper was identifiable and its abstract/bibliographic record was checked, but its full text was not openly available in the inspected sources; this leaves a residual coverage risk for the scalar zero forcing number, not for any specific all-minimum-set classification found in accessible material. No claim is made about minimum rank or equality with maximum nullity.

## References
1. AIM Minimum Rank--Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628--1648. DOI: 10.1016/j.laa.2007.10.009. Publicly available online 26 November 2007; AMS 05C50, 15A18, 15A03.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910; Discrete Applied Mathematics 258 (2019), 35--48.
3. D. D. Row, *A technique for computing the zero forcing number of a graph with a cut-vertex*, Linear Algebra and its Applications 436 (2012), 4423--4432. DOI: 10.1016/j.laa.2011.05.012.
