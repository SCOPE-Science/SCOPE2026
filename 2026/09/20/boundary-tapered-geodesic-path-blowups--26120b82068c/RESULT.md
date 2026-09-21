# Boundary-tapered path blow-ups improve the geodesic-subpath lower bound

## Statement

For positive integers \(a_1,\ldots,a_s\) with \(s\ge 2\), let
\[
B(a_1,\ldots,a_s)
\]
be the path blow-up obtained from a path on \(s\) vertices by replacing its \(i\)-th
vertex with an independent set \(A_i\) of size \(a_i\), joining every vertex of
\(A_i\) to every vertex of \(A_{i+1}\), and adding no other edges.

Write \(\operatorname{gpn}(G)\) for the geodesic subpath number: the number of all
shortest paths in \(G\), including the \(|V(G)|\) zero-length paths.

The following exact formula holds:
\[
\boxed{
\operatorname{gpn}(B(a_1,\ldots,a_s))
=
n+
\sum_{1\le i<j\le s}\prod_{r=i}^{j}a_r
+
\sum_{i=1}^{s}\binom{a_i}{2}(a_{i-1}+a_{i+1}),
}
\tag{1}
\]
where \(n=\sum_i a_i\) and \(a_0=a_{s+1}=0\).

Now let \(q\ge3\), \(n=3q\), and define
\[
H_q=B(1,2,\underbrace{3,\ldots,3}_{q-2\text{ copies}},2,1).
\]
Then
\[
\boxed{
\operatorname{gpn}(H_q)
=
\frac{121}{36}\,3^q+\frac{33}{2}q-\frac{141}{4}.
}
\tag{2}
\]

Knor, Sedlar, Škrekovski and Zhang defined
\[
G_{3,q}=B(\underbrace{3,\ldots,3}_{q\text{ copies}})
\]
and proved
\[
\operatorname{gpn}(G_{3,q})
=
\frac94\,3^q+\frac{33}{2}q-\frac{81}{4}.
\tag{3}
\]
Consequently,
\[
\boxed{
\operatorname{gpn}(H_q)-\operatorname{gpn}(G_{3,q})
=
10\cdot 3^{q-2}-15>0
\qquad(q\ge3).
}
\tag{4}
\]

Thus the equal-layer construction \(G_{3,n/3}\) from the 2026 paper is not the
largest known construction even within path blow-ups.  In particular, if
\[
M_n=\max\{\operatorname{gpn}(G):G\text{ is a connected }n\text{-vertex graph}\},
\]
then for \(n=3q\), \(q\ge3\),
\[
M_{3q}\ge
\frac{121}{36}\,3^q+\frac{33}{2}q-\frac{141}{4}
\sim \frac{121}{36}\,3^{n/3}.
\tag{5}
\]
The leading constant improves the previous \(9/4\) construction by the factor
\[
\frac{121/36}{9/4}=\frac{121}{81}\approx1.493827.
\]

This supplies the construction side of Problem 14 in Knor et al., which asks for
a graph with geodesic subpath number larger than their \(G_{3,n/3}\) benchmark
and/or an improved general upper bound.

## Proof of the path-blow-up formula

Take \(u\in A_i\) and \(v\in A_j\) with \(i<j\).  Every \(u\)-\(v\) geodesic must
move through the layers in order and choose exactly one vertex from each
intermediate layer.  Hence
\[
\operatorname{gpn}_{B}(u,v)=\prod_{r=i+1}^{j-1}a_r.
\]
There are \(a_i a_j\) choices of the endpoint pair, so all pairs from distinct
layers \(A_i,A_j\) contribute
\[
\prod_{r=i}^{j}a_r.
\]

For two distinct vertices \(u,v\in A_i\), the layer is independent and their
common neighbors are exactly the vertices of \(A_{i-1}\cup A_{i+1}\).  Their
distance is two and every common neighbor gives one geodesic, so
\[
\operatorname{gpn}_{B}(u,v)=a_{i-1}+a_{i+1}.
\]
Summing this over the \(\binom{a_i}{2}\) unordered pairs inside \(A_i\), and then
adding the \(n\) zero-length geodesics, gives (1).

## Evaluation of the tapered family

Put \(t=q-2\).  For a layer sequence \(a_1,\ldots,a_s\), define
\[
E_j=\sum_{i=1}^{j}\prod_{r=i}^{j}a_r.
\]
Then
\[
E_j=a_j(1+E_{j-1}).
\tag{6}
\]
For
\[
(1,2,\underbrace{3,\ldots,3}_{t},2,1)
\]
the successive values start with
\[
E_1=1,\qquad E_2=4,
\]
and after the \(r\)-th central 3-layer,
\[
E=\frac{11\cdot3^r-3}{2}.
\]
The final two layers then give
\[
11\cdot3^t-1,\qquad 11\cdot3^t.
\]
Since \(\sum_j E_j\) is precisely the contribution of the zero-length paths and
all endpoint pairs in distinct layers, summing the recurrence yields
\[
\sum_jE_j=\frac{121\cdot3^t-6t-17}{4}.
\tag{7}
\]

The same-layer term in (1) equals
\[
4+4+\bigl(18t-6\bigr)=18t+2,
\tag{8}
\]
where the middle expression also gives the correct value when \(t=1\).
Combining (7) and (8),
\[
\operatorname{gpn}(H_q)
=
\frac{121}{4}3^t+\frac{33}{2}t-\frac94.
\]
Substituting \(t=q-2\) gives (2).

Equation (3) is Proposition 3 of Knor et al. specialized to \(k=3\).
Subtracting (3) from (2) gives
\[
\frac{10}{9}3^q-15=10\cdot3^{q-2}-15,
\]
which is positive for every \(q\ge3\).  This proves (4).

## Why the boundary modification helps

The equal 3-layers are asymptotically efficient in the interior, but an endpoint
layer has only one neighboring layer.  Replacing each endpoint 3-layer by two
successive independent layers of sizes \(1,2\) keeps the order unchanged while
creating additional layer intervals and additional shortest-path endpoint pairs.
The gain at the two boundaries survives at the leading exponential scale, which
is why the asymptotic constant changes from \(9/4\) to \(121/36\).

## Verification

The script `artifacts/verify_path_blowups.py` performs two checks using only the
Python standard library.

1. For \(3\le q\le8\), it constructs both \(H_q\) and \(G_{3,q}\), counts shortest
   paths independently by breadth-first search, and verifies (1)--(4).
2. It enumerates every positive-integer path-blow-up composition for
   \(n=9,12,15,18\).  In these finite ranges, \(H_{n/3}\) is the unique maximizing
   layer composition.

The second check is finite evidence only; no claim is made here that \(H_q\) is
optimal among all path blow-ups for every \(q\), much less among all connected
graphs.

## Literature context and originality

Knor, Sedlar, Škrekovski and Zhang introduced the geodesic subpath number in 2026.
Their Proposition 3 gives the exact value for the equal-layer sequential joins
\(G_{k,t}\), and their comparison identifies \(G_{3,n/3}\) as the strongest
construction among the graph families treated there.  Their Problem 14 explicitly
asks for a smaller general upper bound and/or a graph with geodesic subpath number
larger than the \(G_{3,n/3}\) benchmark.

The full open-access version of that paper, including Proposition 3 and Problem 14,
was inspected.  Searches for the exact invariant name, Problem 14, sequential
joins, unequal layer sizes, path blow-ups, and equivalent shortest-path-count
language did not locate a later research article giving (1), the family \(H_q\),
or the improvement (4).  Because the invariant and open problem are recent,
indexing delay and differently phrased follow-up work remain residual originality
risks.  Originality is claimed only to the best of our knowledge.

## Limitations

- The construction improves the lower bound but does not determine the true
  maximum \(M_n\).
- The 2026 general upper bound remains larger by a factor linear in \(n\) at the
  exponential scale; no improved universal upper bound is proved here.
- Formula (5) is stated for orders divisible by three.  Analogous tapered
  constructions exist at other residues, but they are not claimed or optimized
  here.
- The finite composition enumeration through order 18 does not establish
  path-blow-up optimality in general.
- Originality is to the best of our knowledge.

## Reference

M. Knor, J. Sedlar, R. Škrekovski and X.-D. Zhang,
*Counting Geodesic Paths in Graphs*, Mediterranean Journal of Mathematics 23,
Article 171 (2026).
https://doi.org/10.1007/s00009-026-03159-3
Preprint: https://arxiv.org/abs/2604.04907
