# Universal resolving threshold and extremal bisectors of Johnson graphs

## Finding

Let \(n,k\) be integers with \(n\ge 2k\ge6\). In the Johnson graph \(J(n,k)\), the vertices are the \(k\)-subsets of \([n]\), and two are adjacent if they differ by one element. Define the resolving number \(\operatorname{res}(G)\) as the least integer \(t\) such that **every** set of \(t\) vertices distinguishes every pair of graph vertices by their distance vectors. Then

\[
\operatorname{res}(J(n,k))=\begin{cases}
37,&(n,k)=(8,4),\\
\binom{n-2}{k}+\binom{n-2}{k-2}+1,&\text{otherwise}.
\end{cases}
\]

Every maximum-cardinality nonresolving landmark set is exactly a distance bisector \(\mathcal B(X,Y)=\{W:d(W,X)=d(W,Y)\}\). Its witness pairs have separation one, except that (i) in \(J(6,3)\) both separations one and two occur and (ii) in \(J(8,4)\) only separation four occurs. The exact numbers of distinct labeled maximum nonresolving sets are

\[
N_{\max}(n,k)=\begin{cases}30,&(n,k)=(6,3),\\35,&(n,k)=(8,4),\\\binom n2,&\text{otherwise}.\end{cases}
\]

## Assumptions and scope

All graphs are finite, simple, undirected; vertex distances are ordinary shortest-path lengths. Binomial coefficients with an inadmissible lower index are zero. The theorem is asserted for all integers \(n\ge2k\ge6\), with no upper bound on the parameters. A nonresolving landmark set is a set \(S\) for which two distinct vertices \(X,Y\) satisfy \(d(W,X)=d(W,Y)\) for every \(W\in S\). This is the *universal* threshold, distinct from the usual minimum metric dimension or equidistant dimension.

## Proof

**1. Bisector reduction and formula.** Since \(d(W,X)=k-|W\cap X|\), a set is nonresolving exactly when it is contained in a bisector. For \(r=d(X,Y)\), let \(A=X\setminus Y\), \(B=Y\setminus X\), each of size \(r\); the remaining ground set has size \(n-2r\). Bisector membership is \(|W\cap A|=|W\cap B|\). Therefore its size depends only on \(r\), and is

\[
b_r(n,k)=\sum_{j=0}^r\binom rj^2\binom{n-2r}{k-2j}.
\]

The previously known general bisector identity for resolving number gives \(\operatorname{res}=1+\max_{1\le r\le k}b_r(n,k)\); it follows directly because the largest nonresolving set is a full bisector. In particular \(b_1(n,k)=\binom{n-2}{k}+\binom{n-2}{k-2}\). The remainder proves the nontrivial comparison of all \(r\).

**2. Short separations.** For each \(r\), the coefficient of \(z^k\) in

\[
(1+z)^{n-2r}\left((1+z)^{2r-2}(1+z^2)-\sum_{j=0}^r\binom rj^2z^{2j}\right)
\]

is \(b_1(n,k)-b_r(n,k)\). For \(r=2,3,4,5\), its coefficient lists at \(n=2r+1\), beginning in degree zero, are respectively

\[
(0,2,0,0,2,0),\quad(0,4,2,6,6,2,4,0),
\]
\[
(0,6,6,26,20,20,26,6,6,0),\quad
(0,8,12,68,62,110,110,62,68,12,8,0).
\]

Multiplication by \(1+z\) preserves coefficientwise nonnegativity and propagates strict positivity in all relevant interior degrees. The only allowable short-distance equality at \(n\ge2k\ge6\) is \(b_2(6,3)=b_1(6,3)=8\). To handle the base \(n=2r\) separately (necessarily \(k=r\)): \(b_3(6,3)=0\), \(b_4(8,4)=36>30=b_1(8,4)\), and \(b_5(10,5)=0\). Hence only the stated exception remains for separations two through five.

**3. All longer separations.** Let \(r\ge6\) and first \(n=2r\). At every odd \(k\), \(b_r(2r,k)=0<b_1(2r,k)\). By complement symmetry, it suffices at even \(k=2j\) to consider \(1\le j\le r/2\). Write

\[
R_{r,j}=\frac{\binom rj^2}{\binom{2r-2}{2j}+\binom{2r-2}{2j-2}},\quad
H_{r,j}=(2r-2j)(2r-2j-1)+(2j)(2j-1).
\]

Direct cancellation gives

\[
\frac{R_{r+1,j}}{R_{r,j}}=
\frac{(r+1)^2(2r+1-2j)H_{r,j}}{r(r+1-j)(2r-1)H_{r+1,j}}<1.
\]

To verify the strict inequality with no asymptotics, put \(t=r-2j\ge0\). The denominator product minus the numerator product is exactly

\[
2j(8j^3+28j^2t+12j^2+32jt^2+36jt+10j+10t^3+17t^2+7t)>0.
\]

For \(j=1,2,3\), the starting checks at \(r=6\) give \(R_{6,1}=18/23\), \(R_{6,2}=15/17\), and \(R_{6,3}=20/21\). For \(j\ge4\), the starting parameter is \(r=2j\). Vandermonde's identity implies

\[
\binom{4j}{2j}\ge\binom{2j}{j}^2\left(1+\frac{2j^2}{(j+1)^2}\right).
\]

The factor on the right is larger than \((4j-1)/(2j-1)\), since their difference is \(2j(j^2-3j-1)/((j+1)^2(2j-1))>0\). As \(2\binom{4j-2}{2j}=(2j-1)\binom{4j}{2j}/(4j-1)\), this proves \(R_{2j,j}<1\), and monotonicity proves \(R_{r,j}<1\) for all later \(r\). Thus \(b_r(2r,k)<b_1(2r,k)\) for every interior degree. Multiplication of their coefficientwise difference by \((1+z)^{n-2r}\) preserves strict positivity in all admissible degrees for every \(n\ge2r\). This completes the maximum-bisector comparison.

**4. Equality families and counts.** If \(r=1\), the bisector depends only on the exchanged ground pair \(\{a,b\}\) and consists exactly of the \(k\)-subsets containing both or neither of \(a,b\). Distinct ground pairs give distinct bisectors: the pair is recovered as the unique pair of coordinate-indicators always equal throughout the bisector. Thus there are \(\binom n2\) of them.

For \(J(6,3)\), a distance-two witness pair partitions the six ground elements into three unordered pairs \(A,B,C\). Its bisector consists of all eight transversals taking exactly one point from each pair. Distinct perfect matchings yield distinct transversal families, and there are 15 perfect matchings; no such family coincides with a distance-one bisector. Together with the 15 distance-one bisectors, this gives 30.

For \(J(8,4)\), distance-four witnesses are complementary 4-sets, giving an unordered 4+4 bipartition. The bisector consists of all 36 4-sets selecting exactly two from each block. The unordered bipartition is recoverable by counting, for each ground pair, the number of bisector members containing it: the count is 6 for a same-block pair and 9 for a cross-block pair. Therefore distinct bipartitions yield distinct bisectors, totaling \(\frac12\binom84=35\). Every maximum nonresolving set must equal one of these largest bisectors. \(\square\)

## Verification

The standalone file `johnson_threshold_verify.py` uses only the Python standard library. Run `python3 johnson_threshold_verify.py`. It independently constructs every vertex of each Johnson graph, calculates original Johnson graph distances from intersections, and enumerates *all* unordered witness pairs and their equidistant sets for every \(6\le n\le10\) and \(3\le k\le\lfloor n/2\rfloor\). It checks the predicted maximum sizes, allowed witness distances, and distinct optimizer-family counts, including both exceptions. It also checks the coefficient formula for 1,444 parameter pairs with \(n\le80\) and the relevant rational inequalities on finite ranges; its terminal output is `VERIFY_OK`. These finite tests corroborate, but do not replace, the preceding all-parameter proof.

## Relationship to prior work

Garijo, González, and Márquez established the *general* resolving-number/distance-bisector identity in 2013; it is explicitly used as the starting point, not claimed anew. Korivand, Khashyarmanesh, and Tavakoli's 2022 metric-dimension-threshold article develops the invariant and evaluates other graph families; it does not provide this Johnson-family maximization and equality classification. Earlier Johnson/Kneser metric-dimension papers study the **minimum** size of a resolving set, not the all-sets guarantee. The Johnson-graph equidistant-dimension literature (2021 and 2024) asks for the existence of equidistant landmarks for each vertex pair and cannot be substituted for a maximum-bisector calculation. The 2022 distinguishing-threshold paper studies automorphism-breaking colorings of Johnson graphs, not metric landmark resolution. A previously reported triangular-graph \(J(n,2)\) formula concerns \(k=2\), outside the present domain \(k\ge3\).

## Limitations

The result is confined to ordinary Johnson graphs with \(n\ge2k\ge6\); complementary-set isomorphisms give the symmetric parameter regime but are not used to assert additional graph classes. No claim is made about ordinary *minimum* metric dimension, equidistant dimension, or automorphism-distinguishing thresholds. The literature search does not establish definitive worldwide publication priority; a hitherto unindexed equivalent classification may exist. Independent mathematical audit has not been performed.

## References

1. D. Garijo, A. González, A. Márquez, *The resolving number of a graph*, Discrete Mathematics & Theoretical Computer Science 15 (2013), full text: https://dmtcs.episciences.org/615/pdf . General bisector identity.
2. M. Korivand, B. Khashyarmanesh, M. Tavakoli, *Metric Dimension Threshold of Graphs* (first public 2022-09-14), https://doi.org/10.1155/2022/1838719 .
3. F. González, C. Hernando, M. Mora, *The Equidistant Dimension of Graphs* (2021), https://arxiv.org/abs/2107.10805 .
4. J. Kratica, M. Čangalović, V. Kovačević-Vujčić, *Equidistant dimension of Johnson and Kneser graphs* (2024), https://arxiv.org/abs/2406.17870 .
5. S. Shekarriz and collaborators, *Distinguishing threshold of graphs* (2022), https://doi.org/10.1002/jgt.22923 .
