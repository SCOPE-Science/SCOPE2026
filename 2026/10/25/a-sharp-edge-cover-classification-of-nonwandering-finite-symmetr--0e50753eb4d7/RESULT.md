# A sharp edge-cover classification of nonwandering finite symmetric products

## Finding
Let \(Y\) be the compact binary-shift quotient introduced by Đorić (2026): the underlying subshift consists of configurations containing at most one \(01\) and at most one \(10\); its two constant configurations are identified to a point \(p\). Write \(g\) for the descended left shift. The other points are the rising fronts \(x_i\), falling fronts \(y_i\), and the finite islands \(z_{r,l},w_{r,l}\) (finite nonzero runs of, respectively, ones or zeros), where \(i,r\in\mathbb Z\) and \(l\ge1\).

For each finite nonempty \(A\subseteq Y\), define a directed graph \(G_A\) whose allowable arcs, when both endpoints lie in \(A\), are:

* \(p\to v\) for every \(v\in A\);
* \(x_i\to p\) and \(x_i\to y_j\) for every \(j\in\mathbb Z\);
* \(y_i\to p\) and \(y_i\to x_j\) for every \(j\in\mathbb Z\);
* \(z_{r,l}\to p\) and \(w_{r,l}\to p\).

Let \(\mu_A\) be the maximum matching size of the bipartite graph whose left and right vertex sets are copies of \(A\) and whose edges correspond to the arcs above. If some point of \(A\) has no incoming or no outgoing allowable arc, set \(\tau(A)=\infty\); otherwise let
\[
\tau(A)=2|A|-\mu_A.
\]
For every integer \(n\ge |A|\),
\[
\boxed{A\in\Omega(F_n(g))\quad\Longleftrightarrow\quad \tau(A)\le n.}
\]
In particular \(\tau(A)\) is the **least** symmetric-product level at which \(A\) is nonwandering. This sharp threshold is not solely the size of \(A\): if \(a,b\) are two distinct finite islands, then \(\tau(\{p,a,b\})=4\), although the set has three elements.

## Assumptions and scope
Here \(F_n(Y)\) is the compact space of nonempty subsets of \(Y\) with at most \(n\) points, with its Hausdorff topology, and \(F_n(g)(B)=g(B)\). A point is nonwandering if every neighborhood returns to itself under at least one positive iterate. Every island is an isolated point of \(Y\). Distinct fronts \(x_i,y_j\) remain distinct after taking the quotient.

## Proof
**Step 1: all possible large-time single-point transitions.** Suppose \(u_k\to u\) and \(g^{m_k}u_k\to v\) with \(m_k\to\infty\). The pair \((u,v)\) must be one of the arcs listed in \(G_A\), with \(A\) replaced by \(Y\). To see this directly before quotienting, use the fact that each binary configuration has at most one rising and one falling transition. A finite island of fixed length is isolated, so its forward translates converge to one of the two constant configurations and hence to \(p\). A sequence approaching a fixed rising front has a rising boundary at its fixed index for all sufficiently large \(k\); under an unbounded left shift, that boundary escapes to the left. Its only possible nonconstant limiting boundary is the opposite, falling boundary of a growing island. Thus a rising front can lead only to \(p\) or a falling front; the reversed statement holds for a falling front. When \(u=p\), every target is possible. These statements remain valid in the quotient because only the two constants are identified.

**Step 2: every allowable arc can be realized simultaneously at arbitrarily large common times.** We describe realizations at time \(m\) and let \(m\to\infty\), writing each point by its pre-quotient representative. For \(p\to v\) use \(g^{-m}v\), which converges to \(p\); for \(u\to p\), use the fixed point \(u\), whose forward translates converge to \(p\). For \(p\to p\) use \(p\). To realize \(x_i\to y_j\), take a block of ones supported on \([i,i+m+j-i)=[i,m+j)\). Its initial limit is \(x_i\), while its image after \(m\) shifts tends to \(y_j\). For \(y_i\to x_j\) use instead a finite block of zeros with those endpoints. For any *finite set of distinct arcs*, their realizing configurations are pairwise distinct for sufficiently large \(m\): if the starting vertices differ they have separated starting limits; if starting vertices agree but endpoints differ they have separated endpoint limits. Hence any finite collection of allowable arcs produces simultaneous finite sets of cardinality equal to the number of arcs.

**Step 3: the edge-cover condition is sufficient.** A directed arc set \(E\subseteq E(G_A)\) is an edge cover when every vertex has at least one incoming and one outgoing arc. For \(|E|\le n\), apply Step 2 to the arcs in \(E\), producing finite sets \(B_m\in F_n(Y)\). The two endpoint-cover conditions give \(B_m\to A\) and \(g^m(B_m)\to A\). This proves \(A\in\Omega(F_n(g))\).

**Step 4: the edge-cover condition is necessary.** For \(A\ne\{p\}\), no finite set \(A\) is periodic under \(F_n(g)\), since \(p\) is the only periodic point of \(g\). Thus from nonwandering one can choose neighborhoods of diameter tending to zero, return times \(m_k\to\infty\), and \(B_k\in F_n(Y)\) for which both \(B_k\to A\) and \(g^{m_k}(B_k)\to A\). Passing to a subsequence fixes the cardinality \(|B_k|\le n\) and the assignment of each point of \(B_k\) to its limiting starting and endpoint vertices of \(A\). By Step 1 all assigned pairs are allowable arcs. Every vertex is covered on both sides, and after discarding duplicate pairs at most \(n\) arcs remain. The singleton \(A=\{p\}\) has its self-loop and also satisfies the conclusion.

**Step 5: sharp minimum.** The directed edge-cover problem is the ordinary edge-cover problem on a bipartite graph with left/right copies of \(A\). If it has no isolated vertex, the classical matching/edge-cover identity gives its minimum number of edges \(2|A|-\mu_A\). If it has an isolated vertex no cover exists. Steps 3–4 prove the boxed equivalence. For \(A=\{p,a,b\}\) with \(a,b\) distinct finite islands, the only relevant arcs are \(p\to p,p\to a,p\to b,a\to p,b\to p\). Any cover needs all four nonloop arcs; they attain the bound, so \(\tau(A)=4\).

## Verification
The accompanying standalone Python file checks the edge-cover identity by brute-force enumeration on small induced graphs, the complete source-paper \(F_2\) classification for representative point types, and the strict level-three/level-four transition for two islands. These checks are finite illustrations; Steps 1–5 establish the theorem for all finite subsets and all levels.

## Relationship to prior work
Đorić (2026), Proposition 3 and Theorem 4, introduces the construction and proves the existence of extra nonwandering points in the second symmetric product. Proposition 7 gives the **exact** nonwandering set at level two. The present result classifies the full hierarchy \(F_n(g)\) for **every** \(n\) and every finite configuration, with a sharp minimum level computable by bipartite matching. The minimum-edge-cover formula is standard combinatorics, not claimed as original; the contribution is its exact realization as a dynamical nonwandering threshold with necessary and sufficient dynamical transition arcs.

## Limitations
The theorem concerns this particular countable compact quotient system, not arbitrary hyperspace dynamics or arbitrary subshifts. Its classification uses the possibility that neighborhoods of a finite set contain *more* points than the set itself; simply matching one-to-one trajectories of its members would be incorrect when \(n>|A|\). Priority under different hyperspace terminology cannot be ruled out without exhaustive independent bibliographic review.

## References
1. M. Đorić, *A note on the non-wandering dynamics in the \(n\)-fold symmetric products*, arXiv:2610.23058v1, first posted 2026-10-16, especially Proposition 3, Theorem 4, Proposition 7 and Remark 8; https://arxiv.org/html/2610.23058v1 .
2. Classical bipartite matching–edge-cover identity (no novelty claimed).
