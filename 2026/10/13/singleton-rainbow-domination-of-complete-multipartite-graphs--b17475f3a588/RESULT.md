# Singleton rainbow domination of complete multipartite graphs

## Finding

Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a connected complete multipartite graph, with partite classes
\[
V_1,\ldots,V_r,
\]
and let
\[
k\ge1.
\]

A singleton \(k\)-rainbow dominating function is a map
\[
f:V(G)\to\{0,1,\ldots,k\},
\]
where \(0\) means “uncolored”, and every vertex labeled \(0\) must see every color
\[
1,\ldots,k
\]
in its open neighborhood.

For
\[
a_{i,c}
=
\bigl|\{v\in V_i:f(v)=c\}\bigr|,
\qquad
A_c=\sum_{i=1}^r a_{i,c},
\]
the function \(f\) is singleton \(k\)-rainbow dominating if and only if
\[
\boxed{
a_{i,0}>0
\Longrightarrow
A_c-a_{i,c}\ge1
\quad
\text{for every }c\in[k].
}
\]

Equivalently: every part containing an uncolored vertex must have every color represented in some different part.

This immediately gives the complete weight enumerator
\[
\boxed{
\widetilde R_{k,G}(x)=
\sum_{\mathbf a}
\left(
\prod_{i=1}^r
\binom{n_i}{a_{i,0},a_{i,1},\ldots,a_{i,k}}
\right)
x^{\sum_i\sum_{c=1}^k a_{i,c}},
}
\]
where the sum ranges over all arrays of nonnegative integers with
\[
\sum_{c=0}^k a_{i,c}=n_i
\]
for every \(i\), subject to the displayed feasibility implication.

There is also a closed finite optimization formula for the minimum weight. For a proper subset
\[
F\subsetneq[r],
\]
put
\[
W_F=\sum_{i\in F}n_i.
\]
If
\[
W_F\ge k,
\]
define
\[
\Phi(F)=W_F.
\]
If
\[
W_F<k,
\]
put
\[
q_F=k-W_F,
\]
and define
\[
\kappa_F(q_F)
=
\sum_{i\notin F}\min\{n_i-1,q_F\}.
\]
When
\[
\kappa_F(q_F)\ge2q_F,
\]
define
\[
\Phi(F)=2k-W_F;
\]
otherwise set
\[
\Phi(F)=+\infty.
\]

Then
\[
\boxed{
\widetilde\gamma_{rk}(G)
=
\min\left\{
|V(G)|,\,
\min_{F\subsetneq[r]}\Phi(F)
\right\}.
}
\]

Thus singleton rainbow domination on complete multipartite graphs is controlled by a sharp dichotomy: colors placed in fully colored parts need only one occurrence, whereas every color absent from all fully colored parts must be duplicated in two distinct partially colored parts.

## Assumptions and scope

All graphs are finite, simple, undirected, and connected. The graph is complete multipartite with at least two nonempty parts.

A singleton \(k\)-rainbow dominating function assigns either no color or exactly one color to each vertex. Every uncolored vertex must have all \(k\) colors represented in its open neighborhood. Its weight is the number of colored vertices. The minimum weight is denoted by
\[
\widetilde\gamma_{rk}(G).
\]

The theorem treats arbitrary
\[
k\ge1.
\]
If every vertex is colored, the singleton-rainbow condition is vacuous, which explains the universal candidate
\[
|V(G)|.
\]

## Proof

For a vertex
\[
v\in V_i,
\]
its open neighborhood is exactly
\[
V(G)\setminus V_i.
\]
Therefore, if \(f(v)=0\), color \(c\) appears in \(N(v)\) exactly when at least one vertex of color \(c\) lies outside \(V_i\). In the count notation this is
\[
A_c-a_{i,c}\ge1.
\]
All zero-labeled vertices in the same part have the same neighborhood, so one implication per part is both necessary and sufficient. This proves the structural classification.

For fixed count data \(\mathbf a\), the number of labeled functions realizing those counts is independently multinomial in each part:
\[
\prod_{i=1}^r
\binom{n_i}{a_{i,0},a_{i,1},\ldots,a_{i,k}}.
\]
The weight is
\[
\sum_i\sum_{c=1}^k a_{i,c}.
\]
Summing over the feasible count arrays proves the enumerator.

It remains to prove the minimum formula.

Take a singleton \(k\)-rainbow dominating function having at least one zero. Let
\[
F
\]
be the set of parts containing no zero-labeled vertex. These parts are fully colored, and their total weight contribution is exactly
\[
W_F.
\]

Consider a color that does not occur in any part of \(F\). Such a color cannot occur in only one part outside \(F\): every part outside \(F\) contains a zero, so a zero in that unique supporting part would fail to see the color outside its own part. Hence every color absent from \(F\) must occur in at least two distinct parts outside \(F\).

If \(t\) different colors occur in \(F\), then
\[
t\le\min\{k,W_F\}.
\]
The remaining
\[
k-t
\]
colors each need at least two vertices outside \(F\). Consequently the total weight is at least
\[
W_F+2(k-t).
\]
If \(W_F\ge k\), this gives the lower bound
\[
W_F.
\]
If \(W_F<k\), it gives
\[
2k-W_F.
\]

There is one additional feasibility restriction in the second case. A part outside \(F\) must retain at least one zero, so it can contain at most
\[
n_i-1
\]
selected vertices. For
\[
q=k-W_F,
\]
each of the \(q\) colors not represented in the fully colored parts must be placed in two distinct outside parts.

This is a capacitated bipartite placement problem: there are \(q\) color nodes, each requiring degree \(2\), and one part node for every
\[
i\notin F,
\]
of capacity
\[
n_i-1,
\]
with at most one copy of a given color in any one part. Such a placement exists if and only if
\[
\sum_{i\notin F}\min\{n_i-1,q\}\ge2q.
\]

For completeness, the sufficiency follows from the capacitated Hall criterion. For any \(1\le t\le q\), the available capacity for \(t\) chosen colors is
\[
\sum_{i\notin F}\min\{n_i-1,t\}.
\]
For each fixed capacity \(c\), the ratio
\[
\frac{\min\{c,t\}}{t}
\]
is nonincreasing in \(t\). Hence the inequality at \(t=q\) implies
\[
\sum_{i\notin F}\min\{n_i-1,t\}\ge2t
\]
for every \(t\le q\), which is exactly the Hall condition for giving every color two distinct part incidences.

Now construct an extremal function.

If
\[
W_F\ge k,
\]
use all vertices in the parts of \(F\), assign every color at least once among them, and label every vertex outside \(F\) by \(0\). Every zero sees all colors outside its own part because all colors occur in the fully colored parts.

If
\[
W_F<k
\]
and the capacity inequality holds, assign \(W_F\) distinct colors to the vertices of the full parts. Place each of the remaining
\[
q=k-W_F
\]
colors once in each of two distinct outside parts using the Hall placement above, leaving at least one zero in every outside part. A zero in any such part sees each remaining color in its other supporting part and sees every full-part color in \(F\). The resulting weight is
\[
W_F+2q
=
2k-W_F.
\]

Finally, the all-colored function has weight
\[
|V(G)|
\]
and is always feasible. Taking the minimum over these mutually exhaustive possibilities proves the formula.

## Verification

The accompanying script `artifacts/verify.py` independently reconstructs the singleton-rainbow definition on every nondecreasing complete-multipartite part profile of total order \(2\) through \(7\), for every
\[
1\le k\le4.
\]

It exhaustively enumerates all vertex labels
\[
0,1,\ldots,k,
\]
checks the neighborhood condition directly, compares it with the part-count criterion, groups the functions by their partwise count matrices, verifies the multinomial enumerator coefficient by coefficient, and compares the brute-force minimum with the closed optimization formula.

Replay output:

`ALL CHECKS PASSED; profiles=37; enumerators=148; labelings_checked=1591634; orders=2..7; colors=1..4`

The computation is corroborative only. The arbitrary-order and arbitrary-\(k\) theorem is analytic.

## Relationship to prior work

Žerovnik's 2026 paper on singleton three-rainbow domination of cylindrical graphs provides the fresh motivation. It studies
\[
k=3
\]
on
\[
P_m\square C_n,
\]
developing lower and upper bounds and exact subfamilies. Its preliminaries define singleton \(k\)-rainbow domination for general \(k\).

The inspected paper is product-graph focused and does not state a complete-multipartite classification. Exact searches for singleton rainbow domination together with complete multipartite and complete bipartite terminology did not locate such a theorem.

A close but non-covering result in the published-result database classifies ordinary \(2\)-rainbow dominating functions on complete multipartite graphs. Ordinary rainbow domination permits a vertex to receive a set containing multiple colors, whereas singleton rainbow domination permits at most one color per vertex. The minimum and feasible-function spaces therefore differ, especially when several colors must be duplicated across parts. The present theorem also applies simultaneously to arbitrary \(k\).

## Limitations

The graph class is restricted to complete multipartite graphs. The proof uses the fact that every vertex in one part has exactly the complement of that part as its open neighborhood.

The minimum formula is a finite subset optimization over the fully colored parts. It is exact, but no claim is made that the optimal subset \(F\) can always be chosen from a smaller predetermined family such as the smallest or largest parts.

The originality assessment is literature-based. Singleton rainbow domination has appeared under related rainbow-domination terminology since before 2026, and an equivalent special case could be difficult to retrieve under different notation. The current exact searches and the closest published-result comparisons did not reveal a covering complete-multipartite theorem.

## References

1. J. Žerovnik, “On Singleton 3-Rainbow Domination of Cylindrical Graphs,” Mathematics 14 (2026), 2917, DOI 10.3390/math14162917, published August 12, 2026.
2. B. Brešar, M. A. Henning, and D. F. Rall, “Rainbow domination in graphs,” Taiwanese Journal of Mathematics 12 (2008), 213–225.
