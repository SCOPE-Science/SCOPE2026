# Metric-dimension threshold of semisimple annihilating-ideal graphs

## Finding

Let
\[
R=F_1\times\cdots\times F_n
\]
be a direct product of \(n\ge2\) fields, and let \(G=\mathbb{AG}(R)\) be its annihilating-ideal graph. Then
\[
\dim_{\mathrm{th}}(G)=
\begin{cases}
1,&n=2,\\
3,&n=3,\\
2^n-2^{\lfloor(n-1)/2\rfloor}-2^{\lceil(n-1)/2\rceil}-2,&n\ge4.
\end{cases}
\]

For \(n\ge4\), the pairs of vertices having the fewest distinguishing vertices are exactly the nested support pairs \(A\subset B\) satisfying
\[
|B\setminus A|=1
\]
and
\[
\bigl||A|-|[n]\setminus B|\bigr|\le1.
\]
Equivalently, the obstruction to making every large landmark set resolving is sharpest at a one-coordinate inclusion whose lower support and upper complement are as balanced as possible.

## Assumptions and scope

The metric-dimension threshold \(\dim_{\mathrm{th}}(H)\) of a finite connected graph \(H\) is the least integer \(t\) such that every \(t\)-vertex subset of \(V(H)\) is a resolving set.

The theorem concerns the annihilating-ideal graph of a finite direct product of fields. The field cardinalities do not enter the answer: the graph is determined only by the number \(n\) of simple factors.

For a finite connected graph \(H\) and distinct vertices \(u,v\), define
\[
D_H(u,v)=\{w\in V(H):d(w,u)\ne d(w,v)\}.
\]
A landmark set fails to resolve \(u,v\) exactly when it is disjoint from \(D_H(u,v)\). Therefore
\[
\dim_{\mathrm{th}}(H)
=
|V(H)|-\min_{u\ne v}|D_H(u,v)|+1.
\]

## Proof

Every ideal of
\[
R=F_1\times\cdots\times F_n
\]
is determined by its support \(A\subseteq[n]\). The nonzero annihilating ideals are exactly the nonempty proper supports. Two such ideals multiply to zero exactly when their supports are disjoint. Hence \(G\) is the strong Boolean graph
\[
B_n
\]
on
\[
2^{[n]}\setminus\{\varnothing,[n]\},
\]
with adjacency given by disjointness.

For distinct vertices \(A,B\), partition \([n]\) into four regions and write
\[
a=|A\cap B|,
\qquad
b=|A\setminus B|,
\qquad
c=|B\setminus A|,
\qquad
d=|[n]\setminus(A\cup B)|.
\]
Thus
\[
a+b+c+d=n.
\]

For a third support \(X\), its distance to \(A\) is:
\[
1
\quad\Longleftrightarrow\quad
X\cap A=\varnothing,
\]
\[
3
\quad\Longleftrightarrow\quad
X\cap A\ne\varnothing
\ \text{ and }\
X\cup A=[n],
\]
and otherwise its distance is \(2\), except for the self-distance at \(X=A\). Counting the subsets in the three distance states for \(A\) and \(B\), and then correcting the two self-distances when \(d(A,B)=2\), gives the following exact formulas for
\[
|D(A,B)|=|D_{B_n}(A,B)|.
\]

If \(A\subset B\), so \(b=0\), \(c>0\), and necessarily \(a,d\ge1\), then
\[
|D(A,B)|
=
(2^c-1)(2^a+2^d-1)+2.
\]
The symmetric formula holds when \(B\subset A\).

If \(A\cap B=\varnothing\), then
\[
|D(A,B)|
=
(2^d+1)(2^b+2^c-2)-2.
\]

If \(A\cap B\ne\varnothing\), neither set contains the other, and \(A\cup B=[n]\), then
\[
|D(A,B)|
=
(2^a+1)(2^b+2^c-2)-2.
\]

If all four regions are nonempty, then
\[
|D(A,B)|
=
(2^a+2^d)(2^b+2^c-2).
\]

Put
\[
F(m)=2^{\lfloor m/2\rfloor}+2^{\lceil m/2\rceil}.
\]
Among positive integers with fixed sum \(m\), the quantity \(2^r+2^{m-r}\) is minimized at the balanced choices, and its minimum is \(F(m)\).

Consider first the nested case. Since \(a+d=n-c\),
\[
|D(A,B)|
\ge
(2^c-1)(F(n-c)-1)+2.
\]
When \(c=1\), this becomes
\[
|D(A,B)|\ge F(n-1)+1,
\]
with equality exactly when
\[
|a-d|\le1.
\]
For \(c\ge2\), use
\[
2^c-1\ge3\cdot2^{c-2}
\]
and
\[
F(n-c)-1\ge2^{(n-c)/2}.
\]
This gives
\[
|D(A,B)|
\ge
3\cdot2^{n/2+c/2-2}+2
>
F(n-1)+1.
\]

It remains to show that every nonnested pair has strictly more distinguishers. If all four regions are nonempty, then
\[
2^a+2^d\ge2^{(a+d)/2+1},
\]
while
\[
2^b+2^c-2\ge2^{(b+c)/2}.
\]
Hence
\[
|D(A,B)|\ge2^{n/2+1}>F(n-1)+1
\]
for every \(n\ge4\).

If \(A\cup B=[n]\) and the pair is nonnested, then
\[
|D(A,B)|=(2^a+1)(2^b+2^c-2)-2.
\]
For \(a=1\),
\[
|D(A,B)|
\ge
3(F(n-1)-2)-2
>
F(n-1)+1.
\]
For \(a\ge2\), the same exponential bounds give
\[
|D(A,B)|
\ge
2^{n/2+1}-2,
\]
which is strictly larger than \(F(n-1)+1\) for \(n\ge5\); the only remaining case \(n=4\) gives \(8>7\) directly.

If \(A\cap B=\varnothing\), then
\[
|D(A,B)|=(2^d+1)(2^b+2^c-2)-2.
\]
For \(d=0\),
\[
|D(A,B)|
\ge
2F(n)-6
>
F(n-1)+1.
\]
For \(d=1\),
\[
|D(A,B)|
\ge
3(F(n-1)-2)-2
>
F(n-1)+1.
\]
For \(d\ge2\), the same exponential estimate gives
\[
|D(A,B)|
\ge
2^{n/2+1}-2,
\]
again strictly larger for \(n\ge5\), while \(n=4\) is checked directly.

Therefore, for \(n\ge4\),
\[
\min_{A\ne B}|D(A,B)|
=
F(n-1)+1,
\]
and equality occurs precisely for the balanced one-coordinate nested pairs described above. Since
\[
|V(B_n)|=2^n-2,
\]
the threshold identity yields
\[
\dim_{\mathrm{th}}(B_n)
=
(2^n-2)-(F(n-1)+1)+1
=
2^n-F(n-1)-2.
\]
This is
\[
2^n-2^{\lfloor(n-1)/2\rfloor}
-2^{\lceil(n-1)/2\rceil}-2.
\]

For \(n=2\), \(B_2\cong K_2\), so every one-vertex set resolves and the threshold is \(1\). For \(n=3\), direct inspection gives
\[
\min_{A\ne B}|D(A,B)|=4
\]
on the six-vertex graph \(B_3\), hence
\[
\dim_{\mathrm{th}}(B_3)=6-4+1=3.
\]

## Verification

The included replay constructs \(B_n\) exactly for every \(2\le n\le9\), computes all-pairs graph distances by breadth-first search, determines every set \(D(A,B)\), and checks the stated threshold formula.

For every \(4\le n\le9\), it also verifies that every minimizing pair is nested, differs by one coordinate, and has balanced lower support and upper complement. The replay returns `VERIFY_OK`.

The finite replay is not used as the proof of the universal statement.

## Relationship to prior work

Guo, Wu, and Yu proved that a direct product of \(n\ge3\) fields has annihilating-ideal graph exactly equal to the strong Boolean graph \(B_n\), and their paper develops structural, clique, chromatic, and complemented-graph properties of these graphs.

Korivand, Khashyarmanesh, and Tavakoli introduced the metric-dimension threshold in 2022, motivated by resolving sets that remain useful when landmark choices are constrained or vulnerable. They determined the invariant for paths, cycles, the Petersen graph, and several extremal threshold classes.

A 2021 survey of Boolean graphs records their standard structural invariants and applications but does not discuss metric dimension or metric-dimension threshold. Targeted searches in the strong-Boolean, annihilating-ideal, and metric-threshold terminology did not locate the formula above.

## Limitations

The theorem is for annihilating-ideal graphs that are exactly strong Boolean graphs, in particular finite direct products of fields. It does not give the metric threshold of arbitrary blow-ups of \(B_n\), nor of annihilating-ideal graphs of nonreduced rings.

The principal residual risk is bibliographic: an equivalent threshold calculation could exist under different terminology for disjointness graphs on the full Boolean lattice.

## References

1. J. Guo, T. Wu, and H. Yu, “On rings whose annihilating-ideal graphs are blow-ups of a class of Boolean graphs,” *Journal of the Korean Mathematical Society* 54(3) (2017), 847–865, DOI 10.4134/JKMS.j160283.
2. M. Korivand, K. Khashyarmanesh, and M. Tavakoli, “Metric Dimension Threshold of Graphs,” *Journal of Mathematics* (2022), Article 1838719, DOI 10.1155/2022/1838719.
3. T. Wu, “Boolean graphs — A survey,” in *Ring Theory 2019*, DOI 10.1142/9789811230295_0008.
