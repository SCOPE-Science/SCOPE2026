# Minimum order for consecutive distributed degree sets in bipartite graphs

**Same-model review: passed. Independent audit: not yet performed.**

## Statement

For a bipartite graph `B=(X,Y)`, define its distributed degree sets by
\[
D_X=\{d_B(x):x\in X\},\qquad D_Y=\{d_B(y):y\in Y\}.
\]
Write `[t]={1,2,\ldots,t}` and assume `1<=a<=b`.

### Theorem
Among all finite simple bipartite graphs satisfying
\[
D_X=[a],\qquad D_Y=[b],
\]
the minimum possible order is
\[
\boxed{
N(a,b)=a+b+
\left\lceil\frac{b(b+1)-a(a+1)}{2a}\right\rceil .
}
\]

The same number is the minimum order among **connected** realizations whenever `a>=2`. For `a=b=1`, the unique minimum realization is `K_2`. If `a=1<b`, no connected realization exists at any order.

Thus the consecutive unequal-cardinality family `[a],[b]` has an exact minimum-order formula, and except for the unavoidable family `[1],[b]` with `b>1`, minimum order can be attained without sacrificing connectedness.

## Proof

Let
\[
S_t=1+2+\cdots+t=\frac{t(t+1)}2,
\qquad
H=S_b-S_a.
\]

### 1. Lower bound

Put `x=|X|`, `y=|Y|`, and `e=|E(B)|`. Since `D_Y=[b]`, every degree `1,2,...,b` must occur at least once in `Y`, so `y>=b`. For fixed `y`, the smallest possible degree sum on `Y` is obtained by taking one copy of each degree `1,...,b` and giving every additional vertex degree `1`. Hence
\[
e=\sum_{y\in Y}d(y)
\ge S_b+(y-b)
=y+\frac{b(b-1)}2.
\]

Likewise `x>=a`. For fixed `x`, the largest possible degree sum on `X` subject to `D_X=[a]` is obtained by taking one copy of each degree `1,...,a-1` and giving every remaining vertex degree `a`. Therefore
\[
e=\sum_{x\in X}d(x)
\le ax-\frac{a(a-1)}2.
\]
Combining the two inequalities gives
\[
x\ge
\left\lceil
\frac{y+\frac{b(b-1)}2+\frac{a(a-1)}2}{a}
\right\rceil.
\]
Consequently
\[
x+y\ge
y+
\left\lceil
\frac{y+\frac{b(b-1)}2+\frac{a(a-1)}2}{a}
\right\rceil.
\]
The right-hand side is strictly increasing in the integer `y`, so it is minimized at `y=b`. Substitution yields
\[
x+y\ge b+
\left\lceil\frac{S_b+\frac{a(a-1)}2}{a}\right\rceil
=a+b+\left\lceil\frac{H}{a}\right\rceil=N(a,b).
\]

### 2. Sharp degree sequences

Let
\[
m=\left\lceil\frac{H}{a}\right\rceil.
\]
If `H=0`, use the same sequence `(a,a-1,...,1)` on both sides.

Suppose `H>0`, and write
\[
H=a(m-1)+r,\qquad 1\le r\le a.
\]
On `Y`, prescribe the degree sequence
\[
C=(b,b-1,\ldots,1).
\]
On `X`, prescribe
\[
R=(a,a-1,\ldots,1)\cup
(\underbrace{a,\ldots,a}_{m-1\text{ copies}},r),
\]
sorted in nonincreasing order. Then `R` has length `a+m`, `C` has length `b`, both have sum `S_b`, and their sets of distinct entries are exactly `[a]` and `[b]`.

It remains to prove that `R,C` are bigraphic. Let
\[
L=(a,a-1,\ldots,1),
\quad
P=(b,b-1,\ldots,a+1),
\quad
Q=(\underbrace{a,\ldots,a}_{m-1},r).
\]
Then `C=P\cup L`, `R=Q\cup L`, and `P,Q` have the same total `H`.

The partition `P` majorizes `Q`: for each prefix not exceeding the length of `P`, every part of `P` is at least `a+1`, whereas every part of `Q` is at most `a`; after `P` is exhausted its prefix sum is already the full common total `H`. Majorization is preserved when the same partition is adjoined to both sides, because the sum of the `k` largest parts of a union `A\cup L` is
\[
\max_{i+j=k}\bigl(A_i^*+L_j^*\bigr),
\]
where `A_i^*` and `L_j^*` denote prefix sums. Hence
\[
C=P\cup L\succeq Q\cup L=R.
\]
The staircase partition `C=(b,b-1,...,1)` is self-conjugate. The Gale-Ryser theorem therefore implies that `R,C` are the degree sequences of a simple bipartite graph. Its order is
\[
(a+m)+b=N(a,b),
\]
so the lower bound is sharp.

### 3. Connected realization lemma

We use the following elementary fact.

**Lemma.** Let two positive integer sequences be bigraphic, with total number of vertices `n` and common degree sum `e`. If `e>=n-1`, then they have a connected simple bipartite realization.

**Proof.** Choose a realization with the minimum possible number of connected components. If it is disconnected and `e>=n-1`, then not every component can be a tree, because a forest with at least two components has at most `n-2` edges. Hence one component `C` contains a cycle. Choose an edge `uv` on a cycle in `C` and any edge `xy` in another component `D`, with `u,x` in the same bipartition class. Replace `uv,xy` by `uy,xv`. The new edges did not previously exist because they join different components; degrees and simplicity are preserved. Since `uv` lies on a cycle, `C-uv` remains connected. If `xy` is a bridge, its two resulting pieces are joined separately to `C`; if it is not a bridge, all of `D` remains connected and is joined to `C`. Thus two components merge, contradicting minimality. ∎

For the sharp sequences above, `e=S_b` and `n=N(a,b)`. If `a>=2`, then `e>=n-1`. To see this, put `h=b-a`. When `h=0` this is immediate. When `h>=1`,
\[
H=\sum_{j=a+1}^{b}j\ge h(a+1).
\]
Since `a>=2`, this implies
\[
\left\lceil\frac Ha\right\rceil\le H-h.
\]
Therefore
\[
\begin{aligned}
e-(n-1)
&=S_b-a-b-m+1\\
&=\frac{(a-1)(a-2)}2+H-h-m\\
&\ge0.
\end{aligned}
\]
The lemma gives a connected realization of the same minimum order.

### 4. The exceptional family `a=1`

If `a=b=1`, `K_2` realizes both degree sets and has order `2=N(1,1)`.

If `a=1<b`, every vertex in `X` has degree `1`. A path joining two distinct vertices of `Y` would contain an internal vertex of `X` with degree at least `2`, impossible. Since `D_Y=[b]` with `b>1` forces at least two vertices in `Y`, no connected realization exists.

This completes the proof.

## Context and prior literature

Manoussakis and Patil studied minimum orders for bipartite graphs with prescribed distributed degree sets of equal cardinality. Their 2014 paper explicitly left the different-cardinality case open in the sense of determining a bipartite graph with the corresponding minimum-order property.

Iványi, Pirzada, and Dar subsequently proved existence for arbitrary prescribed distributed degree sets, without requiring equal cardinalities. Their 2015 paper also notes that their general construction usually produces a larger solution than the earlier minimum-order construction, and gives `{1}` versus `{1,2}` as an example where positive prescribed degree sets nevertheless admit no connected realization.

The present theorem determines the exact minimum order for the two-parameter unequal-cardinality family of consecutive positive sets `[a]` and `[b]`, and determines exactly when that minimum can be realized connectedly. The equal case `a=b` is included for completeness and is consistent with the older equal-cardinality theory; the new content concerns unequal cardinalities and the connected-realization boundary.

Later work on degree sets in `k`-partite graphs has primarily treated global degree sets and existence rather than this distributed minimum-order problem. Targeted searches for the formula above, its equivalent degree-sum form, and consecutive distributed-degree-set formulations did not locate an equivalent theorem.

## Verification

The standalone script `artifacts/verify_interval_degree_sets.py` checks the constructive degree sequences with the Gale-Ryser inequalities for all `1<=a<=20` and `a<=b<=40` (610 parameter pairs). It also exhaustively enumerates degree multiplicities for small parameters to compare the exact ordinary and connected minima against the theorem. The recorded output is in `artifacts/expected_output.txt`.

The finite checks support the proof but are not used as a substitute for it.

## Limitations

Originality is to the best of our knowledge. Equivalent results could exist in unindexed literature, theses, or under alternate terminology such as distributed score sets or prescribed partite degree sets. The result treats the structured family of consecutive positive sets `[a]` and `[b]`; it does not solve the minimum-order problem for arbitrary unequal-cardinality sets. The equal-cardinality case was already treated in earlier work and is not claimed as new here.

## References

1. Y. Manoussakis and H. P. Patil, *Bipartite Graphs and their Degree Sets*, Electronic Notes in Discrete Mathematics 15 (2003), 125. https://doi.org/10.1016/S1571-0653(04)00554-2
2. Y. Manoussakis and H. P. Patil, *On degree sets and the minimum orders in bipartite graphs*, Discussiones Mathematicae Graph Theory 34 (2014), 383-390. https://doi.org/10.7151/dmgt.1742
3. A. Iványi, S. Pirzada, and F. A. Dar, *Tripartite graphs with given degree set*, Acta Universitatis Sapientiae, Informatica 7 (2015), 72-106. https://doi.org/10.1515/ausi-2015-0013
4. U. Samee, T. A. Naikoo, S. Pirzada, and B. A. Rather, *On degree sets in k-partite graphs*, Acta Universitatis Sapientiae, Informatica 12 (2020), 251-259. https://doi.org/10.2478/ausi-2020-0015
5. D. Gale, *A theorem on flows in networks*, Pacific Journal of Mathematics 7 (1957), 1073-1082. https://doi.org/10.2140/pjm.1957.7.1073
6. H. J. Ryser, *Combinatorial properties of matrices of zeros and ones*, Canadian Journal of Mathematics 9 (1957), 371-377. https://doi.org/10.4153/CJM-1957-044-3
