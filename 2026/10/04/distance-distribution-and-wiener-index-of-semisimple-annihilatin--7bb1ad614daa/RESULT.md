# Distance distribution and Wiener index of semisimple annihilating-ideal graphs

## Finding

Let
\[
R=F_1\times\cdots\times F_n
\]
be a direct product of \(n\ge 2\) fields, and let \(G=\mathbb{AG}(R)\) be its annihilating-ideal graph. Then \(G\) has \(2^n-2\) vertices. If \(d_k\) denotes the number of unordered pairs of distinct vertices at graph distance \(k\), then
\[
d_1=\frac{3^n-2^{n+1}+1}2,
\qquad
d_2=2^{2n-1}+1-3^n,
\qquad
d_3=\frac{3^n-3\cdot2^n+3}2.
\]
Thus, with the convention that the coefficient of \(x^0\) is the number of vertices, the Hosoya polynomial is
\[
H(G;x)=
(2^n-2)
+\frac{3^n-2^{n+1}+1}2x
+(2^{2n-1}+1-3^n)x^2
+\frac{3^n-3\cdot2^n+3}2x^3,
\]
and
\[
W(G)=H'(G;1)=4^n-11\cdot2^{n-1}+7.
\]
For \(n=2\), the distance-two and distance-three coefficients vanish and \(G\cong K_2\); for \(n\ge3\), the diameter is \(3\).

## Assumptions and scope

The fields \(F_i\) are arbitrary; only the finite number \(n\) of direct factors matters. The annihilating-ideal graph has as vertices the nonzero ideals with nonzero annihilator, with distinct ideals adjacent exactly when their product is zero.

No assertion is made here for products having nonfield factors or for nonreduced rings.

## Proof

Every ideal of \(R\) is uniquely
\[
I_S=\prod_{i=1}^n J_i,
\qquad
J_i=
\begin{cases}
F_i,&i\in S,\\
0,&i\notin S,
\end{cases}
\]
for a subset \(S\subseteq[n]\). The nonzero annihilating ideals are exactly those with
\[
\varnothing\ne S\ne[n],
\]
so there are \(2^n-2\) vertices. Moreover
\[
I_S I_T=0
\quad\Longleftrightarrow\quad
S\cap T=\varnothing.
\]
Hence the graph depends only on \(n\): it is the strong Boolean graph on the nonempty proper subsets of \([n]\).

For distinct nonempty proper \(S,T\), there are three cases.

If \(S\cap T=\varnothing\), then \(d(S,T)=1\).

If \(S\cap T\ne\varnothing\) and \(S\cup T\ne[n]\), then the nonempty set
\[
U=[n]\setminus(S\cup T)
\]
is disjoint from both \(S\) and \(T\). Thus \(S-U-T\) is a path of length two, and the pair is nonadjacent, so \(d(S,T)=2\).

Finally, suppose \(S\cap T\ne\varnothing\) and \(S\cup T=[n]\). There is no nonempty subset disjoint from both, so the pair has no common neighbor and its distance is at least three. Since \(S,T\) are proper, both complements are nonempty, and
\[
S-S^c-T^c-T
\]
is a path of length three because
\[
S\cap S^c=S^c\cap T^c=T^c\cap T=\varnothing.
\]
Therefore \(d(S,T)=3\).

It remains to count the three cases. For distance one, count ordered disjoint nonempty pairs \((S,T)\). Each coordinate has three choices: in \(S\), in \(T\), or in neither. Inclusion-exclusion for \(S\ne\varnothing\) and \(T\ne\varnothing\) gives
\[
3^n-2\cdot2^n+1.
\]
Dividing by two for unordered pairs yields
\[
d_1=\frac{3^n-2^{n+1}+1}2.
\]

For distance three, under \(S\cup T=[n]\), each coordinate is of type \(S\setminus T\), \(T\setminus S\), or \(S\cap T\). Properness of both sets and nonempty intersection require all three types to occur. The number of ordered pairs is therefore the number of surjections from \([n]\) onto three labeled classes:
\[
3^n-3\cdot2^n+3.
\]
Hence
\[
d_3=\frac{3^n-3\cdot2^n+3}2.
\]

The total number of unordered distinct pairs is
\[
\binom{2^n-2}2.
\]
Subtracting \(d_1+d_3\) gives
\[
d_2=\binom{2^n-2}2-d_1-d_3
=2^{2n-1}+1-3^n.
\]
The displayed Hosoya polynomial follows, and differentiating at \(x=1\) gives
\[
W(G)=d_1+2d_2+3d_3
=4^n-11\cdot2^{n-1}+7.
\]

## Verification

The proof is purely symbolic. The included replay independently constructs the subset-disjointness graph for each \(2\le n\le8\), computes all-pairs shortest-path distances by breadth-first search, and checks every coefficient and the Wiener formula. It returns `VERIFY_OK`.

## Relationship to prior work

Mohammad and Younus computed Hosoya polynomials and Wiener indices for annihilating-ideal graphs of several families of \(\mathbb Z_n\), including prime-power and mixed-prime cases. Their paper does not treat arbitrary products of fields.

Guo, Wu, and Yu proved that when
\[
R=\prod_{i=1}^n F_i,
\]
the annihilating-ideal graph is precisely the finite Boolean graph whose vertices are the nonempty proper subsets of \([n]\) and whose adjacency is disjointness. Their paper studies structural, clique, and coloring properties, not the Hosoya polynomial or Wiener index.

The 2022 survey on Wiener indices of graphs over rings explicitly identifies annihilating-ideal graphs among the natural ring graphs whose Wiener indices remain to be developed. The formula above resolves that direction for the full semisimple commutative family of finite direct products of fields.

## Limitations

The theorem is restricted to finite direct products of fields. Although targeted literature and database searches did not locate the same distance distribution or Wiener formula, an equivalent formula could exist under the terminology “strong Boolean graph” or in an unindexed source.

## References

1. T. Asir, V. Rabikka, A. M. Anto, and N. Shunmugapriya, “Wiener index of graphs over rings: a survey,” *AKCE International Journal of Graphs and Combinatorics* (2022), DOI 10.1080/09728600.2022.2140088.
2. H. Q. Mohammad and S. A. Younus, “On Annihilating-Ideal Graph of \(\mathbb Z_n\),” *Al-Rafidain Journal of Computer Sciences and Mathematics* 12(2) (2018), DOI 10.33899/csmj.2018.163570.
3. J. Guo, T. Wu, and H. Yu, “On rings whose annihilating-ideal graphs are blow-ups of a class of Boolean graphs,” *Journal of the Korean Mathematical Society* 54(3) (2017), 847–865, DOI 10.4134/JKMS.j160283.
