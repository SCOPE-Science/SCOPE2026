# Exact rainbow path covers of \(K_{2,m}\) from two matchings

## Result

Let \(c\) be an arbitrary proper edge-colouring of \(K_{2,m}\).

**Theorem.** If \(m\ge 12\), then
\[
\operatorname{rpc}(K_{2,m},c)=\left\lceil \frac m2\right\rceil.
\]
In fact the edges can be **partitioned**, rather than merely covered, by
\(\lceil m/2\rceil\) rainbow paths.

For \(m=2t\ge12\), the statement has the following prescribed-role strengthening.
Write the two-vertex side as \(\{x,y\}\), the \(2t\)-vertex side as \(R\), and
prescribe any partition \(R=M\sqcup S\) with \(|M|=|S|=t\). Then \(E(K_{2,2t})\)
has a decomposition into \(t\) rainbow copies of \(P_5\) such that every
\(u\in M\) is the unique vertex of \(R\) internal to one of the \(P_5\)'s.
Consequently
\[
\operatorname{rpc}(K_{2,m})=\left\lceil \frac m2\right\rceil
\qquad (m\ge12).
\]

Here \(\operatorname{rpc}(G,c)\) is the minimum number of rainbow simple paths
whose union contains \(E(G)\), and \(\operatorname{rpc}(G)\) is the maximum of
this quantity over proper edge-colourings \(c\).

## Context

Liu, Xu and Yang introduced this extremal viewpoint for rainbow path covers and
proved, uniformly for complete multipartite graphs, an asymptotic formula in
terms of matching number and maximum degree.  For \(K_{2,m}\) their theorem
specializes to
\[
\operatorname{rpc}(K_{2,m})=(1+o(1))\,\frac m2.
\]
The result above removes the asymptotic error completely for \(m\ge12\), and
does so for every proper colouring separately.  It also gives an edge
decomposition and permits the middle vertices on the large side to be
prescribed in advance.

## Proof

Let
\[
R=\{v_1,\dots,v_m\},\qquad
a_i=c(xv_i),\qquad b_i=c(yv_i).
\]
Properness says that the \(a_i\)'s are pairwise distinct, the \(b_i\)'s are
pairwise distinct, and \(a_i\ne b_i\) for every \(i\).

Define a partial map \(\phi:R\rightharpoonup R\) by
\[
\phi(v_i)=v_j\quad\Longleftrightarrow\quad b_i=a_j.
\]
Because both colour lists are injective, \(\phi\) is a partial injection; and
because \(a_i\ne b_i\), it has no fixed point.

### Even case

Let \(m=2t\) with \(t\ge6\), and fix an arbitrary partition
\[
R=M\sqcup S,\qquad |M|=|S|=t.
\]

We first choose a bijection \(\sigma:M\to S\) such that
\[
\sigma(u)\ne \phi(u)
\]
whenever \(\phi(u)\in S\).  The allowed pairs form \(K_{t,t}\) with at most a
matching deleted, so such a perfect matching \(\sigma\) exists.

Next construct a bipartite graph \(H\) with parts \(M,S\).  For \(u\in M\) and
\(w\in S\), declare \(uw\) allowed unless one of the following holds:
\[
w=\sigma(u),\qquad \phi(w)=u,\qquad \phi(w)=\sigma(u).
\]
Each of the three forbidden relations is a matching (possibly partial).  The
first is the graph of the bijection \(\sigma\); the second is a restriction of
the inverse of the partial injection \(\phi\); and the third is a restriction
of that inverse composed with \(\sigma\).  Hence every vertex of \(H\) has
degree at least
\[
t-3\ge t/2.
\]

A balanced bipartite graph with both part sizes \(t\) and minimum degree at
least \(t/2\) has a perfect matching.  Indeed, for \(X\) in one part, if
\(|X|\le t/2\), then \(N(X)\) has size at least \(t/2\ge|X|\).  If
\(|X|>t/2\) and \(|N(X)|<|X|\), a vertex outside \(N(X)\) would have all its
neighbours in a set of size \(t-|X|<t/2\), contradicting the minimum-degree
condition.  By Hall's theorem, \(H\) therefore has a perfect matching; let the
corresponding bijection be \(\tau:M\to S\).

For each \(u\in M\), take the path
\[
P_u=\sigma(u)-x-u-y-\tau(u).
\]
The condition \(\tau(u)\ne\sigma(u)\) makes this a simple \(P_5\).  Its four
edge colours are
\[
a_{\sigma(u)},\ a_u,\ b_u,\ b_{\tau(u)}.
\]
The first two are distinct because the \(a\)-colours are injective; the last
two are distinct because the \(b\)-colours are injective; and \(a_u\ne b_u\)
by properness.  The remaining three possible repetitions are excluded exactly
by
\[
\sigma(u)\ne\phi(u),\qquad
\phi(\tau(u))\ne u,\qquad
\phi(\tau(u))\ne\sigma(u).
\]
Thus every \(P_u\) is rainbow.

Finally, because both \(\sigma\) and \(\tau\) are bijections, the family
\(\{P_u:u\in M\}\) uses every edge \(xv\) and every edge \(yv\) exactly once.
It is therefore a rainbow \(P_5\)-decomposition of \(K_{2,2t}\).

### Odd case

Let \(m=2t+1\ge13\).  Choose any \(z\in R\).  The two-edge path
\[
x-z-y
\]
is rainbow by properness.  Delete \(z\); the remaining graph is
\(K_{2,2t}\) with \(t\ge6\), so the even case decomposes its edges into
\(t\) rainbow \(P_5\)'s.  Together these give \(t+1=\lceil m/2\rceil\)
edge-disjoint rainbow paths covering all edges.

### Optimality

The vertex \(x\) has degree \(m\), while any simple path contains at most two
edges incident with \(x\).  Hence every path cover, rainbow or not, contains at
least
\[
\left\lceil\frac m2\right\rceil
\]
paths.  This matches the construction above.

\(\square\)

## Constructive corollary

The proof is algorithmic.  For even \(m\ge12\), after any prescribed balanced
split \(R=M\sqcup S\), one finds \(\sigma\) and \(\tau\) by two ordinary
bipartite perfect-matching computations.  Thus the optimal rainbow
edge-decomposition can be constructed in polynomial time.

## Originality boundary and limitations

To the best of our knowledge, the exact formula and the prescribed-middle
rainbow \(P_5\)-decomposition above are not present in the literature.  The
closest direct source is the 2026 preprint of Liu, Xu and Yang, which proves an
asymptotic formula for all complete multipartite graphs and therefore gives
\((1+o(1))m/2\) for \(K_{2,m}\).  Searches for exact and synonymous formulations
involving rainbow path covers/decompositions of \(K_{2,m}\) and complete
bipartite graphs did not locate an equivalent result.

The threshold \(m\ge12\) comes from the elementary minimum-degree criterion
used for the second perfect matching and is not claimed to be sharp.  This
record does not classify the remaining finite values \(m<12\), nor does it
give exact formulas for \(K_{r,m}\) with \(r\ge3\).  The motivating preprint is
very recent, so unindexed parallel work remains a residual originality risk.

## References

1. Xiao-Chuan Liu, Boyan Xu, Xu Yang, *Sharp Rainbow Path Covers in Dense and
   Complete Multipartite Graphs*, arXiv:2609.18740 (2026).
   https://arxiv.org/abs/2609.18740
2. GAPCOMB problem booklet, section on rainbow path covers (background problem
   and terminology).
   https://requile.github.io/open_problems_booklet.pdf
