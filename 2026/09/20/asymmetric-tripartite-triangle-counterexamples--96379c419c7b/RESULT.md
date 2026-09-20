# Asymmetric counterexamples for the balanced-tripartite triangle problem

## Statement

For integers \(1\le t\le n\), let
\[
f(n,t)=\min\{\tau(G): G\text{ is tripartite with three parts of size }n,
\ \delta(G)\ge n+t\},
\]
where \(\tau(G)\) is the number of triangles of \(G\).

Define, for an integer \(u\in[t,2t]\),
\[
F_t(u)=u\max\{t^2,(u+t)(2t-u)\}.
\]

**Theorem.** For every pair of integers \(p,q\in[t,2t]\) and every
\[
n\ge 3t+p+q,
\]
there is a balanced tripartite graph with minimum degree at least \(n+t\) and exactly
\[
F_t(p)+F_t(q)
\]
triangles. Consequently,
\[
\boxed{f(n,t)\le F_t(p)+F_t(q).}
\]

This is an asymmetric extension of the symmetric construction of Fang and Xu (2026), which corresponds to \(p=q\).

For \(t\ge2\), put
\[
p_t=\lfloor \sqrt2\,t\rfloor+1.
\]
Then
\[
F_t(t)=2t^3,\qquad F_t(p_t)<2t^3,
\]
and hence
\[
\boxed{f(n,t)<4t^3\quad\text{for every }n\ge 4t+\lfloor\sqrt2\,t\rfloor+1.}
\]
Thus the known counterexample range to the Bollobás--Erdős--Szemerédi proposed lower bound improves from
\[
n\ge 3t+2\lceil\varphi t\rceil=(3+2\varphi)t+O(1)
\]
with \(\varphi=(1+\sqrt5)/2\), to
\[
n\ge (4+\sqrt2)t+O(1).
\]
Numerically the leading threshold coefficient decreases from about \(6.236\) to about \(5.414\), moving substantially closer to the original conjectural range \(n\ge5t\).

Within the two-parameter family in the theorem, this threshold is optimal for merely crossing below \(4t^3\): if \(p+q<t+p_t\), then
\[
F_t(p)+F_t(q)\ge4t^3.
\]
This optimality is only for the displayed construction family and is not a lower bound for arbitrary tripartite graphs.

## Construction

We use the following bipartite gadget, already present in the Fang--Xu construction. For \(u\in[t,2t]\), there is a bipartite graph
\[
H_u=(X_u,Y_u),\qquad |X_u|=u+t,\quad |Y_u|=t,
\]
such that every vertex of \(X_u\) has degree at least \(2t-u\), every vertex of \(Y_u\) has degree at least \(t\), and
\[
|E(H_u)|=\max\{t^2,(u+t)(2t-u)\}.
\]
One explicit construction is to give each vertex of \(Y_u\) \(t\) cyclically consecutive neighbors in \(X_u\), producing \(t^2\) edges with the \(X_u\)-degrees differing by at most one, and then add edges at deficient \(X_u\)-vertices until degree \(2t-u\) is reached. The edge count is exactly the displayed maximum.

Take pairwise disjoint sets
\[
A=A_1\sqcup A_2\sqcup A_3,
\quad B=B_1\sqcup B_2\sqcup B_3,
\quad C=C_1\sqcup C_2\sqcup C_3
\]
with
\[
|A_1|=p,\quad |A_2|=n-p-q,\quad |A_3|=q,
\]
\[
|B_1|=p+t,\quad |B_2|=t,\quad |B_3|=n-p-2t,
\]
\[
|C_1|=q+t,\quad |C_2|=t,\quad |C_3|=n-q-2t.
\]
The assumption \(n\ge p+q+3t\) makes all required sizes nonnegative and leaves the large filler classes available.

Add all edges in the following pairs:

- \(A_1\) to all of \(B\), and \(A_1\) to \(C_2\);
- \(A_2\) to \(B_2\cup B_3\) and to \(C_2\cup C_3\);
- \(A_3\) to all of \(C\), and \(A_3\) to \(B_2\);
- \(B_1\) to \(C_1\cup C_3\), and \(B_3\) to \(C_1\);
- a copy of \(H_p\) between \(B_1\) and \(C_2\);
- a copy of \(H_q\) between \(C_1\) and \(B_2\).

There are no other edges.

## Minimum-degree check

Vertices of \(A_1\) and \(A_3\) have degree exactly \(n+t\). A vertex of \(A_2\) has degree
\[
2n-p-q-2t\ge n+t.
\]

A vertex of \(B_1\) has at least
\[
p+(n-t)+(2t-p)=n+t
\]
neighbors, using its \(H_p\)-degree; symmetrically every vertex of \(C_1\) has degree at least \(n+t\). Every vertex of \(B_2\) is adjacent to all \(n\) vertices of \(A\) and to at least \(t\) vertices of \(C_1\) through \(H_q\), and similarly for \(C_2\). Finally,
\[
d(B_3)=p+(n-p-q)+(q+t)=n+t,
\]
\[
d(C_3)=q+(n-p-q)+(p+t)=n+t.
\]
Thus \(\delta(G)\ge n+t\).

## Triangle count

The only triangles are of the two forms
\[
A_1-B_1-C_2
\quad\text{and}\quad
A_3-B_2-C_1.
\]
Indeed, the listed complete pairs and the absence of all other pairs rule out every other triple of one vertex from each main part. Therefore
\[
\tau(G)
=|A_1|\,|E(H_p)|+|A_3|\,|E(H_q)|
=F_t(p)+F_t(q),
\]
proving the theorem.

## The \((4+\sqrt2)t\) threshold

For \(x=u/t\) with \(1\le x\le\sqrt2\), one is on the branch
\[
F_t(u)=u(u+t)(2t-u),
\]
and
\[
\frac{F_t(u)}{t^3}-2
=x(x+1)(2-x)-2
=(x-1)(2-x^2)\ge0.
\]
Hence \(F_t(u)\ge2t^3\) for every integer
\[
t\le u\le\lfloor\sqrt2\,t\rfloor.
\]

For \(p_t=\lfloor\sqrt2\,t\rfloor+1\), we have \(p_t>\sqrt2\,t\). If \(p_t\le\varphi t\), the same factorization gives \(F_t(p_t)<2t^3\). If \(p_t>\varphi t\), then the maximum in \(F_t\) equals \(t^2\), so
\[
F_t(p_t)=p_t t^2<2t^3
\]
for \(t\ge2\). Taking \((p,q)=(p_t,t)\) proves the strict counterexample for every \(n\ge4t+p_t\).

For the family-optimality statement, if \(p+q<t+p_t\) and \(p,q\ge t\), then both \(p,q<p_t\), so both terms are at least \(2t^3\). Hence the sum is at least \(4t^3\).

## Context and originality boundary

Bollobás, Erdős and Szemerédi (1975) proved the universal lower bound \(f(n,t)\ge t^3\), constructed examples with \(4t^3\) triangles for \(n\ge5t\), and suggested that \(4t^3\) should be the true minimum in that range.

Fang and Xu (2026) disproved that proposal by a symmetric construction with a single parameter \(p\): for \(n\ge2p+3t\) it has
\[
2F_t(p)
\]
triangles. Optimizing near \(p=\varphi t\) gives their threshold
\(n\ge3t+2\lceil\varphi t\rceil\) and asymptotic triangle count \((1+\sqrt5)t^3\).

The present contribution is the independent choice of the two parameters \(p,q\), together with the observation that minimizing the *order needed to cross below* \(4t^3\) is a different optimization problem from minimizing the triangle count itself. The asymmetric choice \((t,p_t)\) gives the sharper counterexample threshold \((4+\sqrt2)t+O(1)\).

To the best of our knowledge, the two-parameter formula and the \((4+\sqrt2)t\) counterexample range have not appeared previously. Searches covered the exact problem, balanced-tripartite minimum-degree triangle counts, the constants \(4t^3\), \(\sqrt2\), asymmetric/unequal parameter variants, and the citation chain around the 1975 and 2026 papers. The 1975 construction and the 2026 Fang--Xu construction were inspected directly. No specific inaccessible paper was identified as especially likely to contain the same result. Because the Fang--Xu preprint is very recent, an unindexed parallel observation or later revision remains a material residual originality risk.

## Verification

`artifacts/verify.py` constructs the graph directly from the definition, checks the three part sizes and minimum degree, counts triangles from adjacency sets, and compares against \(F_t(p)+F_t(q)\). It exhaustively checks all \((p,q)\) for \(1\le t\le12\) at two admissible orders and verifies the threshold arithmetic for \(2\le t\le5000\). The recorded output is in `artifacts/verification.txt`.

Finite computation is supporting evidence only; the theorem is proved symbolically above.

## Limitations

- The result is an upper-bound construction; it does not determine \(f(n,t)\).
- The family-optimality statement is only about this two-parameter construction and does not preclude different counterexamples for smaller \(n\), including in the remaining strip from \(5t\) to about \((4+\sqrt2)t\).
- The bipartite gadget itself is inherited from Fang--Xu; the new step is asymmetrizing the two copies and optimizing for the earliest strict violation of \(4t^3\).
- Originality is assessed only to the best of our knowledge; the recency of the source preprint raises the risk of parallel or subsequently revised coverage.
- Finite verification does not replace the proof.

## References

1. B. Bollobás, P. Erdős, E. Szemerédi, *On complete subgraphs of r-chromatic graphs*, Discrete Mathematics 13 (1975), 97--107. https://users.renyi.hu/~p_erdos/1975-19.pdf
2. C. Fang, R. Xu, *On the minimum number of triangles in balanced tripartite graphs with large minimum degree*, arXiv:2609.20590 (2026), v1. https://arxiv.org/abs/2609.20590
3. UCSD Erdős Problems, *Number of triangles in a multi-partite graph with large minimum degree*. https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/TrianglesInMultipartiteGraph.html
