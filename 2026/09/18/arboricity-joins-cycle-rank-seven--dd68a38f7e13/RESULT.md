# A cycle-rank criterion for exact arboricity of graph joins

## Statement

For a finite simple graph \(X\), let \(a(X)\) denote its classical arboricity: the minimum number of forests whose edge sets partition \(E(X)\). For a connected graph \(X\), let
\[
\beta(X)=|E(X)|-|V(X)|+1
\]
be its cycle rank (cyclomatic number).

Let \(G,H\) be connected finite simple graphs of orders \(m,n\ge1\), put
\[
\beta=\beta(G)+\beta(H),
\]
and define the full-set arboricity ceiling
\[
K=
\left\lceil
\frac{|E(G)|+|E(H)|+mn}{m+n-1}
\right\rceil
=
\left\lceil
\frac{mn+m+n-2+\beta}{m+n-1}
\right\rceil.
\]

Then
\[
\boxed{a(G*H)=K}
\]
whenever any one of the following holds:

1. \(K\le2\);
2. \(K=3\) and \(\beta\le7\);
3. \(K\ge4\) and
   \[
   \beta\le (K-1)(K-2)+1.
   \]

In particular, the parameter-free consequence
\[
\boxed{
\beta(G)+\beta(H)\le7
\quad\Longrightarrow\quad
a(G*H)=
\left\lceil
\frac{mn+m+n-2+\beta}{m+n-1}
\right\rceil
}
\]
holds for every pair of connected simple factors.

The constant \(7\) in this universal corollary is best possible: there are connected \(G,H\) with total cycle rank \(8\) for which the full-set ceiling is \(3\) but \(a(G*H)=4\).

In the reduced-arboricity convention of Kuanyshov--Yeginbay, \(\operatorname{arb}(X)=a(X)-1\), so each displayed exact formula translates by subtracting one.

## Context

Kuanyshov and Yeginbay (2026) study arboricity under graph wedges and joins. They obtain an exact wedge formula and, for joins, the general bounds
\[
\max\{\operatorname{arb}(G),\operatorname{arb}(H),B\}
\le
\operatorname{arb}(G*H)
\le
\operatorname{arb}(G)+\operatorname{arb}(H)+B+1,
\]
where
\[
B=\left\lceil\frac{mn}{m+n-1}\right\rceil-1
\]
in their reduced convention. They also compute several individual families. The result above supplies an exact join criterion controlled by the total cycle-space dimension of the factors; the admissible cycle rank grows quadratically with the full-set ceiling once \(K\ge4\).

## Proof

Write
\[
J=G*H,\qquad q=K-1.
\]
Since the full vertex set is an admissible Nash--Williams subgraph,
\[
a(J)\ge K.
\]
We prove the reverse inequality.

It is enough to check induced subgraphs: for a fixed vertex set, adding all available edges only increases the Nash--Williams density. Let
\[
A\subseteq V(G),\quad B\subseteq V(H),
\qquad s=|A|,\quad t=|B|.
\]
For a nonempty \(A\), put
\[
c_G(A)=|E(G[A])|-s+1,
\]
and define \(c_H(B)\) analogously. If \(G[A]\) has \(r\) connected components, its cycle-space dimension is
\[
|E(G[A])|-s+r\ge c_G(A),
\]
and cycle-space dimension is monotone under taking subgraphs. Hence
\[
c_G(A)\le\beta(G),\qquad c_H(B)\le\beta(H).
\]
When \(s,t\ge1\), set \(c=c_G(A)+c_H(B)\). Then \(c\le\beta\) and
\[
|E(J[A\cup B])|=st+s+t-2+c.
\]

The desired inequality
\[
|E(J[A\cup B])|\le K(s+t-1)
\]
is equivalent to
\[
c\le R_q(s,t),
\qquad
R_q(s,t):=q(s+t-1)-st+1.
\tag{1}
\]
The useful factorization
\[
R_q(s,t)=q^2-q+1-(q-s)(q-t)
\tag{2}
\]
will control all two-sided subsets.

The definition of \(K=q+1\), applied to the full join, also gives
\[
\beta\le R_q(m,n).
\tag{3}
\]

### Case 1: \(q\ge3\)

Assume
\[
\beta\le q^2-q+1,
\tag{4}
\]
which is exactly hypothesis 3 in terms of \(K\).

If \(s,t\ge q\), then \(q-s,q-t\le0\). Because \(m\ge s\) and \(n\ge t\), (2) implies
\[
R_q(s,t)\ge R_q(m,n)\ge\beta\ge c
\]
by (3).

If, say, \(s<q\le t\), then
\[
(q-s)(q-t)\le0,
\]
and therefore
\[
R_q(s,t)\ge q^2-q+1\ge\beta\ge c
\]
by (4).

It remains to treat \(s,t<q\). Simplicity gives
\[
c_G(A)\le \binom{s}{2}-s+1=\frac{(s-1)(s-2)}2,
\]
and similarly for \(H[B]\). A direct calculation gives
\[
2R_q(s,t)
-\bigl((s-1)(s-2)+(t-1)(t-2)\bigr)
=
(s+t-1)(2q-s-t+2)\ge0,
\]
because \(s,t\le q-1\). Thus (1) holds.

We must also control one-sided subsets. Let \(U\) be an \(r\)-vertex induced subgraph of either factor. From cycle rank and simplicity,
\[
|E(U)|
\le
\min\left\{\binom r2,\ r-1+\beta\right\}.
\tag{5}
\]
If \(2\le r\le2q+2\), then
\[
\binom r2\le(q+1)(r-1).
\]
If \(r\ge2q+3\), then (4) and \(q\ge3\) give
\[
\beta\le q^2-q+1\le q(r-1),
\]
so (5) again yields
\[
|E(U)|\le(q+1)(r-1)=K(r-1).
\]
Thus every one-sided subgraph also satisfies Nash--Williams with \(K\) forests.

### Case 2: \(q=2\)

Here \(K=3\), and assume \(\beta\le7\).

Every one-sided induced subgraph has at most
\[
\min\left\{\binom r2,\ r-1+7\right\}\le3(r-1)
\]
edges on \(r\ge2\) vertices, so it has arboricity at most \(3\).

For a two-sided set with \(s,t\ge2=q\), the same argument using (2) and (3) gives
\[
R_2(s,t)\ge R_2(m,n)\ge\beta\ge c.
\]
If \(t=1\), then \(c_H(B)=0\) and
\[
c
\le
\min\left\{7,\frac{(s-1)(s-2)}2\right\}
\le s+1
=
R_2(s,1).
\]
The case \(s=1\) is symmetric. Hence (1) holds for every two-sided subset.

### Case 3: \(q=1\)

Here \(K=2\). Equation (3) becomes
\[
0\le\beta\le R_1(m,n)=m+n-mn.
\]
If \(m,n\ge2\), this forces \(m=n=2\) and \(\beta=0\). Thus \(G=H=K_2\), so \(J=K_4\) and \(a(J)=2\).

If, say, \(n=1\), then \(\beta(H)=0\) and \(\beta(G)\le1\). For a two-sided set, \(t=1\), so
\[
c=c_G(A)\le1=R_1(s,1).
\]
A one-sided \(r\)-vertex subgraph has at most \(r\le2(r-1)\) edges for \(r\ge2\). The symmetric case is identical. Therefore \(a(J)=2\).

### Case 4: \(q=0\)

Here \(K=1\). Equation (3) gives
\[
0\le\beta\le1-mn.
\]
Hence \(m=n=1\) and \(\beta=0\), so \(J=K_2\) and \(a(J)=1\).

All cases prove the criterion.

## Universal cycle-rank-seven corollary

If \(\beta\le7\), then Cases 3 and 4 need no extra hypothesis; Case 2 is exactly covered; and in Case 1,
\[
q^2-q+1\ge7
\qquad(q\ge3).
\]
Hence the exact full-set formula holds for every connected pair with total cycle rank at most seven.

## Sharpness of the universal constant

Let \(Q\) be obtained from \(K_6\) by deleting two edges, so \(|E(Q)|=13\). Form \(G\) by adjoining one new leaf to any vertex of \(Q\), and let \(H=K_1\). Then
\[
|V(G)|=7,\qquad |E(G)|=14,\qquad \beta(G)=8,
\]
while \(\beta(H)=0\).

The join \(J=G*K_1\) has \(8\) vertices and
\[
|E(J)|=14+7=21,
\]
so the full-set ceiling is
\[
\left\lceil\frac{21}{7}\right\rceil=3.
\]
However, the induced subgraph on the six vertices of \(Q\) together with the cone vertex has \(7\) vertices and \(13+6=19\) edges. Nash--Williams therefore gives
\[
a(J)\ge\left\lceil\frac{19}{6}\right\rceil=4.
\]
Since \(J\subseteq K_8\) and \(a(K_8)=4\), in fact \(a(J)=4\). Thus total cycle rank \(8\) already admits a counterexample, and the uniform constant \(7\) cannot be increased.

## Consequences

- The exact formula holds for the join of any two trees.
- It holds for every join whose connected factors together have at most seven independent cycles.
- For larger cycle rank it still holds whenever the predicted full-set arboricity \(K\ge4\) is large enough that
  \[
  \beta\le(K-1)(K-2)+1.
  \]
- Via \(\operatorname{gscat}(X)=\operatorname{arb}(X)=a(X)-1\) for connected graphs in the convention used by Kuanyshov--Yeginbay, the same criterion gives exact simplicial geometric category values for these joins.

## Limitations

The criterion is sufficient, not necessary. Many joins outside the stated cycle-rank range also attain the full-set ceiling. The quadratic threshold in hypothesis 3 is not claimed sharp for each fixed \(K\). No claim is made that the full vertex set maximizes the *fractional* Nash--Williams density; only its ceiling is shown to equal the arboricity.

Originality is to the best of our knowledge. The principal directly relevant source is very recent, so unindexed parallel work remains a residual risk.

## References

1. N. Kuanyshov and I. Yeginbay, *Arboricity and Simplicial Geometric Category of Wedges and Joins of Graphs*, arXiv:2609.20606 (2026), especially Theorem 23 and Section 3.2.
2. C. St. J. A. Nash-Williams, *Decomposition of Finite Graphs Into Forests*, Journal of the London Mathematical Society 39 (1964), 12. DOI: 10.1112/jlms/s1-39.1.12.
