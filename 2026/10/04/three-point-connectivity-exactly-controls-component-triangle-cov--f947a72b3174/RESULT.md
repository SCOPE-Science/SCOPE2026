# Three-point connectivity exactly controls component–triangle covariance

## Finding

Let
\[
G=(V,E)
\]
be a finite simple graph. Form a random spanning subgraph
\[
(V,A)
\]
by retaining every edge independently with probability
\[
0<p<1.
\]

Let
\[
K=K(A)
\]
be the number of connected components,
\[
T=T(A)
\]
the number of open triangles, and
\[
R=|A|-|V|+K
\]
the cycle rank, equivalently the dimension of the cycle space.

Fix a triangle
\[
\tau=\{u,v,w\}
\]
of the base graph. Delete the three edges of \(\tau\), percolate all remaining edges with probability \(p\), and let
\[
C_\tau\in\{1,2,3\}
\]
be the number of distinct connected components of this triangle-deleted random subgraph that contain at least one of
\[
u,v,w.
\]

Then the component–triangle covariance is exactly
\[
\boxed{
\operatorname{Cov}(K,T)
=
-p^3(1-p)^2
\sum_{\tau}
\left[
\Pr(C_\tau=2)
+
(p+2)\Pr(C_\tau=3)
\right].
}
\tag{1}
\]

In particular, if the base graph contains at least one triangle,
\[
\boxed{
\operatorname{Cov}(K,T)<0.
}
\tag{2}
\]

The complementary first-homology statistic has the opposite sign:
\[
\boxed{
\operatorname{Cov}(R,T)
=
p^3(1-p)
\sum_{\tau}
\left[
3
-
(1-p)\Pr(C_\tau=2)
-
(1-p)(p+2)\Pr(C_\tau=3)
\right].
}
\tag{3}
\]

If
\[
t(G)
\]
denotes the number of triangles in the base graph, then
\[
\boxed{
t(G)p^3(1-p)(1+p+p^2)
\le
\operatorname{Cov}(R,T)
\le
3t(G)p^3(1-p).
}
\tag{4}
\]
Hence
\[
\boxed{
\operatorname{Cov}(R,T)>0
}
\tag{5}
\]
whenever \(t(G)>0\).

For the Erdős–Rényi graph
\[
G(n,c/n),
\qquad
0<c<1
\]
fixed, write \(K_n,T_n,R_n\) for its component count, triangle count, and cycle rank. Then
\[
\boxed{
\operatorname{Cov}(K_n,T_n)
\longrightarrow
-\frac{c^3}{3},
}
\tag{6}
\]
while
\[
\boxed{
\operatorname{Cov}(R_n,T_n)
\longrightarrow
\frac{c^3}{6}.
}
\tag{7}
\]

Thus a triangle has two simultaneous topological effects. It is negatively associated with the zeroth Betti number because closing its three edges can merge up to three ambient components, but positively associated with the first Betti number because an open triangle necessarily contributes cycle-space redundancy. The exact finite covariance is controlled only by the three-point connectivity partition visible after the triangle's own edges are removed.

## Assumptions and scope

The finite theorem holds for independent bond percolation on an arbitrary finite simple graph.

The variable \(T\) counts non-induced triangles: a base-graph triangle contributes when all three of its edges are open, regardless of other open edges.

The connectivity variable \(C_\tau\) is measured after removing the three edges of the base triangle before sampling those three edge states. This is essential: it records only alternative ambient connections among the triangle vertices.

The sparse asymptotics (6)--(7) are stated only for fixed
\[
0<c<1.
\]
The supercritical case has non-vanishing ambient three-point connectivity through the giant component and is not claimed here.

## Proof

For a base-graph triangle \(\tau\), let
\[
I_\tau
\]
be its open-triangle indicator. Then
\[
T=\sum_\tau I_\tau.
\]

Fix \(\tau=\{u,v,w\}\) and expose every edge outside \(\tau\). Let
\[
H
\]
be that random triangle-deleted spanning subgraph and let
\[
c=C_\tau.
\]
Write \(K_0\) for the number of components of \(H\).

Now expose the three triangle edges. If their open subset is
\[
S\subseteq E(\tau),
\]
let
\[
\rho_c(S)
\]
be the number by which those edges reduce the component count relative to \(H\). Then
\[
K=K_0-\rho_c(S).
\]

If all three triangle edges are open, the \(c\) ambient components meeting \(u,v,w\) are joined into one, so
\[
\rho_c(E(\tau))=c-1.
\tag{8}
\]

Because
\[
\mathbb E[I_\tau\mid H]=p^3
\]
is constant,
\[
\operatorname{Cov}(K,I_\tau)
=
\mathbb E\!\left[
\operatorname{Cov}(K,I_\tau\mid H)
\right].
\tag{9}
\]
Conditionally on \(H\),
\[
\operatorname{Cov}(K,I_\tau\mid H)
=
p^3
\left(
\mathbb E[\rho_c(S)\mid H]-(c-1)
\right).
\tag{10}
\]

There are three cases.

If
\[
c=1,
\]
all three vertices are already connected in \(H\), so
\[
\rho_1(S)=0
\]
for every \(S\), and the conditional covariance is zero.

If
\[
c=2,
\]
two triangle vertices lie in one ambient component and the third lies in another. One triangle edge is internal to the first component, while the other two are parallel opportunities to join the two ambient components. Hence
\[
\mathbb E\rho_2(S)
=
1-(1-p)^2.
\]
Using (10),
\[
\operatorname{Cov}(K,I_\tau\mid C_\tau=2)
=
-p^3(1-p)^2.
\tag{11}
\]

If
\[
c=3,
\]
the three vertices lie in three distinct ambient components. The reduction is zero with no open triangle edge, one with exactly one open edge, and two with at least two open edges. Therefore
\[
\begin{aligned}
\mathbb E\rho_3(S)
&=
3p(1-p)^2
+
2\left(
3p^2(1-p)+p^3
\right)\\
&=
3p-p^3.
\end{aligned}
\]
Since the fully open triangle reduces the component count by two,
\[
2-(3p-p^3)
=
(1-p)^2(p+2),
\]
and hence
\[
\operatorname{Cov}(K,I_\tau\mid C_\tau=3)
=
-p^3(1-p)^2(p+2).
\tag{12}
\]

Averaging (11)--(12) and summing over \(\tau\) proves (1).

Strict negativity in (2) follows because, for every base triangle, the event that every edge outside the triangle is closed has positive probability. On that event,
\[
C_\tau=3.
\]

For the cycle rank,
\[
R=|A|-|V|+K.
\]
Only the three edges of \(\tau\) covary with \(I_\tau\), and each contributes
\[
\operatorname{Cov}(\mathbf 1_{\{e\in A\}},I_\tau)
=
p^3(1-p).
\]
Thus
\[
\operatorname{Cov}(|A|,I_\tau)
=
3p^3(1-p).
\tag{13}
\]
Adding (13) to the component covariance gives (3).

Since
\[
\Pr(C_\tau=2)+\Pr(C_\tau=3)\le1
\]
and
\[
(1-p)(p+2)\ge1-p,
\]
the largest possible subtraction in the bracket of (3) occurs when
\[
\Pr(C_\tau=3)=1.
\]
Therefore
\[
3-(1-p)(p+2)
=
1+p+p^2,
\]
which proves the lower bound in (4); the upper bound is immediate by dropping the nonnegative subtraction. This proves (4)--(5).

For the sparse complete-graph specialization, take
\[
p=\frac cn,
\qquad
0<c<1.
\]
After deleting the three internal edges of a fixed triangle, any connection between two of its vertices must use a path of length at least two. A union bound over simple paths gives
\[
\Pr(u\leftrightarrow v)
\le
\sum_{\ell\ge2}
n^{\ell-1}
\left(\frac cn\right)^\ell
\le
\frac{c^2}{n(1-c)}.
\tag{14}
\]
Hence, uniformly over base triangles,
\[
\Pr(C_\tau=3)=1+O(n^{-1}),
\qquad
\Pr(C_\tau=2)=O(n^{-1}).
\tag{15}
\]

There are
\[
\binom n3
\]
base triangles. Substitution of (15) into (1), with
\[
p=\frac cn,
\]
gives
\[
\operatorname{Cov}(K_n,T_n)
=
-\binom n3
\left(\frac cn\right)^3
\left(1-\frac cn\right)^2
\left(2+o(1)\right),
\]
which proves (6).

Likewise, (3) gives
\[
\operatorname{Cov}(R_n,T_n)
=
\binom n3
\left(\frac cn\right)^3
\left(1-\frac cn\right)
\left(1+o(1)\right),
\]
proving (7).

## Verification

The accompanying checker exhaustively enumerates every percolation configuration for several finite base graphs, including complete graphs and graphs with overlapping triangles.

For several rational values of \(p\), it computes \(K\), \(T\), \(R\), and every triangle-deleted three-point connectivity law exactly. It then verifies (1) and (3) with rational arithmetic and checks the universal bounds (4).

The finite replay is supplementary. The theorem for arbitrary finite graphs is proved by conditioning on all edges outside one triangle and classifying the three possible ambient connectivity partitions.

## Relationship to prior work

Elçi, Weigel, and Fytas study bridges and non-bridges in the random-cluster model and derive exact finite-graph relations from the Russo–Margulis formula. In the independent-percolation specialization they use the response of the component count to a single edge to relate component behavior to bridge probabilities. Their inspected full text treats edge classes, bridge density, and bridge fluctuations, but does not formulate a triangle-count covariance or a three-vertex connectivity correction.

Janson's classical functional-limit paper develops asymptotic theory for fixed subgraph counts in Erdős–Rényi graphs, including triangle counts as a standard example of the general framework. The accessible publisher record describes subgraph-count fluctuations but does not resolve covariance with the total number of connected components. Full text was not available in the inspected source, so an older implicit treatment remains a residual originality risk.

The present identity sits exactly between these two strands: it replaces the single-edge bridge/candidate-bridge dichotomy by the three-state connectivity partition seen by a triangle and converts it into an exact component covariance and an opposite-sign cycle-rank covariance.

## Limitations

The result is specific to independent bond percolation. In a random-cluster model with cluster weight different from one, the three triangle edges are not independent of the exposed exterior configuration.

The triangle formula does not immediately reduce to pairwise connection probabilities; distinguishing \(C_\tau=2\) from \(C_\tau=3\) is essential.

The subcritical asymptotic uses only a simple path union bound and therefore deliberately stops at fixed \(c<1\). Critical and supercritical limits require more detailed three-point connectivity information.

More general fixed motifs admit analogous rank-increment formulas, but no general motif theorem is claimed here.

## References

1. E. M. Elçi, M. Weigel, and N. G. Fytas, “Bridges in the random-cluster model,” arXiv:1509.00668, first submitted 2015-09-02; later *Nuclear Physics B* 903 (2016), 19–50, DOI 10.1016/j.nuclphysb.2015.12.001.
2. S. Janson, “A functional limit theorem for random graphs with applications to subgraph count statistics,” *Random Structures & Algorithms* 1 (1990), 15–37, DOI 10.1002/rsa.3240010103.
