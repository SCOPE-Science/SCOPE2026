# Maximum independent sets in zero-divisor graphs of products of nonbinary finite fields

## Finding

Let
\[
R=\prod_{i=1}^{r}\mathbb F_{q_i},
\qquad r\ge2,
\qquad q_i\ge3\text{ for every }i,
\]
and let \(\Gamma(R)\) be the standard zero-divisor graph: its vertices are the nonzero zero-divisors of \(R\), and distinct vertices are adjacent exactly when their product is zero.

Put
\[
a_i=q_i-1.
\]
For every nonempty proper support \(S\subset[r]\), define
\[
w(S)=\prod_{i\in S}a_i.
\]
Let \(\tau\) be the number of unordered complementary pairs \(\{S,S^c\}\) satisfying
\[
w(S)=w(S^c).
\]

Then
\[
\alpha(\Gamma(R))
=
\sum_{\{S,S^c\}}
\max\{w(S),w(S^c)\},
\]
where the sum runs over unordered complementary pairs of nonempty proper subsets of \([r]\).

Equivalently, if
\[
N=\prod_{i=1}^{r}q_i-\prod_{i=1}^{r}(q_i-1)-1
\]
is the number of vertices, then
\[
\alpha(\Gamma(R))
=
\frac{N}{2}
+
\frac14
\sum_{\varnothing\ne S\subsetneq[r]}
\left|w(S)-w(S^c)\right|.
\]

The maximum independent sets are classified completely. Every such set contains all vertices from every support cell \(S\) with
\[
w(S)>w(S^c),
\]
contains none from every cell with
\[
w(S)<w(S^c),
\]
and, for each tied complementary pair, contains all vertices of exactly one of the two cells. Thus the number of maximum independent sets is
\[
2^\tau.
\]

## Assumptions and scope

The result concerns finite fields of order at least \(3\). The binary case is deliberately excluded: when some \(q_i=2\), the logarithmic weights used below can vanish, and two disjoint tied supports need not be complementary. That boundary requires additional combinatorics and is not claimed here.

For a vertex \(x=(x_1,\ldots,x_r)\), its support is
\[
\operatorname{supp}(x)=\{i:x_i\ne0\}.
\]
A vertex of the zero-divisor graph has a nonempty proper support.

## Proof

For each nonempty proper \(S\subset[r]\), let \(C_S\) be the set of vertices with support exactly \(S\). Then
\[
|C_S|=w(S).
\]
Every \(C_S\) is an independent set, and for distinct supports \(S,T\), every vertex of \(C_S\) is adjacent to every vertex of \(C_T\) exactly when
\[
S\cap T=\varnothing.
\]

If an independent set contains one vertex of \(C_S\), then all remaining vertices of \(C_S\) can be added without creating an edge. Hence every maximum independent set is a union of entire support cells. Therefore maximum independent sets of \(\Gamma(R)\) are equivalent to maximum-weight pairwise-intersecting families of nonempty proper subsets of \([r]\), with weight \(w(S)\).

Pair the supports as
\[
\{S,S^c\}.
\]
An intersecting family contains at most one member of every complementary pair, so
\[
\alpha(\Gamma(R))
\le
\sum_{\{S,S^c\}}\max\{w(S),w(S^c)\}.
\]

It remains to show that the upper bound is attainable and to classify equality.

Because \(q_i\ge3\), every \(a_i>1\). Put
\[
b_i=\log a_i>0,
\qquad
B=\sum_{i=1}^{r}b_i.
\]
Then
\[
w(S)>w(S^c)
\quad\Longleftrightarrow\quad
\sum_{i\in S}b_i>\frac B2.
\]

Two strict-heavy supports cannot be disjoint, because their \(b\)-weights would sum to more than \(B\). A strict-heavy support and a tied support cannot be disjoint for the same reason. If two tied supports \(S,T\) are disjoint, then
\[
\sum_{i\in S}b_i
=
\sum_{i\in T}b_i
=
\frac B2.
\]
Their union therefore has total \(b\)-weight \(B\). Since every \(b_i>0\), this forces
\[
S\cup T=[r],
\]
so \(T=S^c\).

Consequently, the family formed by taking every strict-heavy support and choosing one member arbitrarily from each tied complementary pair is pairwise intersecting. It attains the complementary-pair upper bound.

Equality also gives the classification. Since every support cell has positive size, a maximum-weight intersecting family must select one side of every complementary pair. Whenever the two weights differ, selecting the lighter side would lose positive weight and therefore cannot be maximum. On a tied pair either side is allowed, and the preceding argument shows that these choices are mutually compatible. Hence there are exactly
\[
2^\tau
\]
maximum independent sets.

Finally,
\[
\sum_{\varnothing\ne S\subsetneq[r]}w(S)
=
\prod_i(1+a_i)-1-\prod_i a_i
=
N.
\]
For each complementary pair,
\[
\max\{u,v\}=\frac{u+v+|u-v|}{2}.
\]
Summing over pairs gives
\[
\alpha(\Gamma(R))
=
\frac N2
+
\frac14
\sum_{\varnothing\ne S\subsetneq[r]}
|w(S)-w(S^c)|.
\]

## Verification

The standalone `verify.py` artifact was read from its packaged path and replayed.

For several tuples with two through five factors, the program enumerates every choice of one support from each complementary pair, rejects the nonintersecting choices, and checks that the maximum weight and the number of maximizers agree with the theorem. Tested tuples include
\[
(3,3),\ (3,5),\ (3,3,3),\ (7,5,5),\ (3,4,7),
\]
\[
(3,3,3,3),\ (3,3,4,4),\ (3,4,5,7),
\]
and two five-factor examples.

It also checks the equivalent absolute-difference formula and verifies that the three-factor specialization agrees with the previously published exact formula. Larger six- and seven-factor tuples are checked against the two closed forms without exhaustive family enumeration.

Exact replay output:

```text
q= (3, 3) alpha= 2 ties= 1 max_families= 2
q= (3, 5) alpha= 4 ties= 0 max_families= 1
q= (3, 3, 3) alpha= 12 ties= 0 max_families= 1
q= (7, 5, 5) alpha= 64 ties= 0 max_families= 1
q= (3, 4, 7) alpha= 36 ties= 1 max_families= 2
q= (3, 3, 3, 3) alpha= 44 ties= 3 max_families= 8
q= (3, 3, 4, 4) alpha= 81 ties= 2 max_families= 4
q= (3, 4, 5, 7) alpha= 234 ties= 1 max_families= 2
q= (3, 3, 3, 3, 3) alpha= 160 ties= 0 max_families= 1
q= (3, 3, 3, 4, 5) alpha= 368 ties= 0 max_families= 1
large q= (3, 3, 3, 3, 3, 3) alpha= 512 ties= 10 max_families= 1024
large q= (3, 4, 5, 7, 8, 9) alpha= 21226 ties= 0 max_families= 1
large q= (5, 5, 5, 5, 5, 5, 5) alpha= 59136 ties= 0 max_families= 1
VERIFY_OK
```

The finite checks corroborate the proof; the arbitrary-\(r\) theorem rests on the complement-pair and positive-logarithm argument, not on enumeration.

## Relationship to prior work

LaGrange gave an algorithm and classification framework for zero-divisor graphs of direct products of integral domains and finite reduced rings. That structural background explains why support cells are natural.

Alikhani and Mirvakili studied independent sets in zero-divisor graphs. Their arbitrary-factor theorem gives a general lower bound, while their subsequent exact results treat products of three, four, and five integral domains by separate case analyses. The result here replaces those bounded-rank case splits, under the natural nonbinary hypothesis, by one exact formula for every number of finite-field factors and also classifies all maximum independent sets.

Birch, Thibodeaux, and Tucci studied finite direct products and derived edge-count formulas. Their work is another algebra-primary source for the same direct-product zero-divisor setting, but it does not give the independence result above.

## Limitations

No assertion is made when at least one factor is \(\mathbb F_2\). The proof pinpoints the obstruction: zero logarithmic coordinate weight permits disjoint tied supports that are not complementary.

The theorem concerns the standard zero-divisor graph, not annihilating-ideal, compressed, cozero-divisor, or ideal-intersection graphs.

The originality comparison includes direct searches for arbitrary-factor exact independence formulas and broader weighted-intersecting formulations. A residual literature risk remains that an abstract weighted-intersection theorem, stated far from ring graphs, could imply the support optimization as a corollary; no such implication-equivalent source was located in the inspected literature.

## References

1. J. D. LaGrange, “On Realizing Zero-Divisor Graphs,” *Communications in Algebra* 36 (2008), 4509–4520. DOI: 10.1080/00927870802182499.
2. S. Alikhani and S. Mirvakili, “Independent sets of some graphs associated to commutative rings,” arXiv:1301.1452, first submitted 8 January 2013.
3. L. M. Birch, J. J. Thibodeaux, and R. P. Tucci, “Zero Divisor Graphs of Finite Direct Products of Finite Rings,” *Communications in Algebra* 42 (2014), 3852–3860. DOI: 10.1080/00927872.2013.796556.
