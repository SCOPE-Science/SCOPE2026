# Contractible Components of Finite-Ray-Graph Hyperspaces

## Finding

Let \(X\) be a finite connected ray-graph with compact finite core \(K\) and \(k\) attached rays \(R_1,\ldots,R_k\), each parametrized by \([0,\infty)\). For an integer \(n\ge 1\), let \(C_n(X)\) be the space of nonempty closed subsets of \(X\) having at most \(n\) connected components, equipped with the extended Hausdorff metric induced by arc length.

For each \(S\subseteq\{1,\ldots,k\}\), let \(\mathcal C_n^S(X)\) consist of those sets that are unbounded exactly along the rays indexed by \(S\), and put
\[
Y_S=K\cup\bigcup_{i\in S}R_i.
\]
Every \(\mathcal C_n^S(X)\) is contractible to the single hyperspace point \(Y_S\). Consequently,
\[
C_n(X)\simeq \coprod_{S\subseteq\{1,\ldots,k\}}\{*\},
\]
a discrete space of \(2^k\) points.

## Assumptions and scope

A finite connected ray-graph consists of a finite connected graph \(K\) and finitely many copies of \([0,\infty)\), each attached at one vertex of \(K\). Core edges have their usual arc-length metric. The Hausdorff metric is allowed to take the value \(+\infty\), as is necessary for subsets with different unbounded direction sets. The theorem applies to every finite \(k\) and every integer \(n\ge1\). It makes no assertion for infinitely many rays, non-graph cores, or the Vietoris topology.

## Proof

Fix a direction set \(S\). Write \(d_0\) for the original path metric. For \(0\le t<1\), define
\[
c(t)=\rho(t)=\frac{t}{1-t},\qquad w(t)=\frac{1}{(1-t)^2}.
\]
Let \(g_t\) fix \(K\) and send a point with coordinate \(x\) on any ray to the point with coordinate \(\max\{0,x-c(t)\}\). Let \(d_t\) be the path metric that leaves lengths on \(K\) and on rays in \(S\) unchanged, and multiplies lengths on rays outside \(S\) by \(w(t)\). Define
\[
H_t(A)=\{x\in X:d_t(x,g_t(A))\le \rho(t)\}\quad(0\le t<1),
\qquad H_1(A)=Y_S.
\]

At \(t=0\), the shift is zero and the neighborhood radius is zero, so \(H_0(A)=A\). For \(t<1\), the map \(g_t\) is continuous and proper. Its image has at most \(n\) connected components. In a length space, the finite-radius neighborhood of a connected set is connected; therefore taking this neighborhood cannot increase the number of connected components beyond \(n\). A finite shift preserves which rays are unbounded, and a finite-radius neighborhood in \(d_t\) cannot make a bounded portion of a ray unbounded. Thus \(H_t(A)\in\mathcal C_n^S(X)\) for every \(t<1\).

For continuity below \(t=1\), restrict \(t\) to any compact subinterval of \([0,1)\). The functions \(c,\rho,w\) are then bounded and continuous. Within a fixed direction class, the bounded portions on rays outside \(S\) and the starting points of the unbounded tails on rays in \(S\) are locally uniformly bounded in the Hausdorff topology. Hence only a finite part of the graph and finite initial ray segments determine the boundaries of the neighborhoods. On this finite collection of edge intervals, the shifts, weights, and neighborhood endpoints vary continuously. For fixed \(t\), the neighborhood operator is \(1\)-Lipschitz in its own Hausdorff metric. These facts give joint continuity of \(H_t(A)\) for \(t<1\).

It remains to check \(t=1\). For each fixed \(A\), all bounded ray portions and all starting points of its unbounded tails have a finite common bound. Once \(c(t)\) exceeds that bound, \(g_t(A)\) contains every complete ray in \(S\), intersects \(K\), and has no non-vertex points on rays outside \(S\). If \(\rho(t)\ge\operatorname{diam}(K)\), its \(d_t\)-neighborhood contains \(Y_S\). On a ray outside \(S\), a point at original coordinate \(x\) can belong to that neighborhood only if
\[
w(t)x\le \rho(t),\qquad\text{so}\qquad x\le \frac{\rho(t)}{w(t)}=t(1-t).
\]
Consequently,
\[
d_H^{\,0}\bigl(H_t(A),Y_S\bigr)\le t(1-t)\longrightarrow 0.
\]
The same finite bounds can be chosen uniformly for \(A'\) in a sufficiently small Hausdorff neighborhood of \(A\) inside \(\mathcal C_n^S(X)\); this proves joint continuity at \(t=1\). Thus \(H\) is a contraction of \(\mathcal C_n^S(X)\) to \(Y_S\).

Finally, if two sets have different unbounded direction sets, their extended Hausdorff distance is infinite. Each direction class is therefore clopen. The classes form a finite disjoint union, and the contractions above give a homotopy equivalence of the whole hyperspace with a discrete set of \(2^k\) points.

## Verification

The proof explicitly tracks the unbounded direction set, the component bound, the endpoint \(t=0\), joint continuity for \(t<1\), and the uniform limit at \(t=1\). The result is stronger than a count of path components: it determines the homotopy type of each component. No numerical experiment is used or needed for this constructive argument.

## Relationship to prior work

The closest primary source is Esty's preprint *The Hyperspaces \(C_n(X)\) of finite ray-graphs* (arXiv:1012.1578, first public on 2010-12-07). Its Theorem 5.3 proves that the extended-Hausdorff hyperspace has exactly \(2^k\) path-connected components. Its Section 6 treats the Vietoris topology, where it states contractibility for \(CL(X)\) and path-connectedness for \(C_n(X)\). Those results do not state contractibility of each component in the extended-Hausdorff topology. The construction here supplies that additional componentwise homotopy classification. The related 2008 contractibility paper is available in this run only by its abstract, which concerns the Vietoris topology; it is recorded as a scope-limited comparison rather than evidence of noncoverage of its full text.

## Limitations

The theorem depends on the finite connected ray-graph structure, finitely many rays, finitely many allowed connected components, and the extended Hausdorff metric. The argument uses a time-dependent weighted path metric to make the contraction compatible with the unbounded directions. An independent audit has not been performed, and the literature search cannot rule out every unindexed equivalent theorem.

## References

1. Norah Esty, *The Hyperspaces \(C_n(X)\) of finite ray-graphs*, arXiv:1012.1578, first public date 2010-12-07. Sections 1, 5, and 6; especially Theorem 5.3 and Theorems 6.1–6.2.
2. Norah Esty, *The hyperspaces \(C_n(X)\) for finite ray-graphs*, *Applied General Topology* 14(1) (2013), 73–84. DOI: 10.4995/agt.2013.1619.
3. Norah Esty, *On the contractibility of certain hyperspaces*, *Topology Proceedings* 32 (2008), 291–300. Abstract inspected; full text unavailable in this run.
4. R. Duda, *On the hyperspace of subcontinua of a finite graph, II*, *Fundamenta Mathematicae* 63 (1968), 225–255. Bibliographic record and cited scope inspected; full text not used to infer noncoverage.
