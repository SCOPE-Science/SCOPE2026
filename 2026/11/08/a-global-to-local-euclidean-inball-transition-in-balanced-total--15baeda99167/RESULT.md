# A global-to-local Euclidean inball transition in balanced total-matching polytopes

## Finding

For every integer \(n\ge2\), let \(G_n=K_{n,n}\) be the simple unweighted complete bipartite graph with two vertex classes of size \(n\). Let \(P_n\) be the convex hull, in its standard vertex-and-edge incidence-coordinate Euclidean space, of the indicator vectors of all total matchings of \(G_n\). Then \(P_n\) has dimension \(N=n^2+2n\), and its intrinsic Euclidean inradius is

\[
\boxed{\rho_n=\left[\max\left\{n+2+\sqrt{1+\frac2n},\;n+1+\sqrt{n+1}\right\}\right]^{-1}.}
\]

There is exactly one center of a largest contained Euclidean ball, namely \(c_n=\rho_n\mathbf1_N\). The inball contacts undergo a strict global-to-local transition: if \(n=2\) or \(n=3\), precisely the \(N\) nonnegativity facets and the single full-graph balanced-biclique facet contact the inball, totaling \(N+1\) facets. For all \(n\ge4\), precisely the \(N\) nonnegativity facets and the \(2n\) vertex-degree facets contact it, totaling \(N+2n\) facets. No other facets touch the unique maximal ball.

In particular, the tangent-facet counts are \(9\), \(16\), and \(32\) at \(n=2,3,4\), respectively, and \(\lim_{n\to\infty}n\rho_n=1\).

## Assumptions and scope

A *total matching* is a subset of graph vertices and edges whose elements are pairwise compatible: no two selected vertices are adjacent, no two selected edges are incident, and no selected edge is incident to a selected vertex. Coordinates are indexed by all \(2n\) vertices and all \(n^2\) edges. We use the unscaled standard Euclidean metric on \(\mathbb R^N\) with these coordinates orthonormal. The empty total matching and every singleton total matching exist; thus the origin and all coordinate unit vectors belong to \(P_n\), making it full-dimensional in \(\mathbb R^N\). All assertions quantify over every integer \(n\ge2\).

For a halfspace \(\langle a,z\rangle\le b\) with nonzero outer normal, a ball of center \(c\) and radius \(r\) lies in that halfspace if and only if \(\langle a,c\rangle+r\|a\|_2\le b\). The *tangent facets* are facets whose supporting hyperplanes have distance exactly \(r\) from the incenter.

## Proof

**1. Complete inequalities.** We use the complete irredundant original-coordinate facet description of the total-matching polytope of a complete bipartite graph in Faenza--Ferrarini [2, Theorem 2]. It consists of nonnegativity, vertex-degree, edge, balanced-biclique, and nonbalanced lifted-biclique inequalities. Below we check the metric effect of *all* families, especially the last one; omitting the lifted family would not prove the theorem.

The first three types are

\[
 z_d\ge0;\qquad x_v+\sum_{e\ni v}y_e\le1;\qquad
 x_a+x_b+y_{ab}\le1\quad(ab\in E(G_n)).
\]

The balanced-biclique inequality for any \(K_{t,t}\) subgraph, \(1\le t\le n\), is the sum of its \(t^2+2t\) vertex and edge coordinates at most \(t\). The case \(t=1\) repeats the edge inequality.

For the remaining lifted inequalities take a sub-biclique \(K_{u,v}\) with \(2\le u<v\le n\), with subsets of the two vertex sides of sizes \(a,b\), where \(1\le a<u\), \(0\le b<a\), and \(b=0\) requires \(a=1\). Put

\[
 \tau=\frac{v-u}{a-b}>0,\quad m=a+b+ab,\quad H_0=u+v+uv,
 \quad B=u+a\tau.
\]

The lifted normal has coefficient \(1+\tau\) on the \(m\) positions belonging to the chosen vertices and their induced edges, coefficient \(1\) on the other \(H_0-m\) positions of that sub-biclique, and coefficient \(0\) elsewhere. Its right-hand side is \(B\). These are precisely the coefficient rules of [2, equation (7)], including interchange of the two color classes.

**2. Coordinatewise lower obstruction.** Suppose a Euclidean ball of radius \(r\) is contained in \(P_n\), with arbitrary center \(c\). Every coordinate inequality \(z_d\ge0\) implies \(c_d\ge r\). For any *positive-coefficient* facet \(\langle a,z\rangle\le b\), this yields the general upper bound

\[
 r\le \frac{b}{\|a\|_1+\|a\|_2}.
\]

Conversely, for the special center \(c=r\mathbf1_N\), all such facet inequalities hold if and only if their displayed bounds hold. Thus the exact inradius equals the minimum of those reciprocals over the known positive-coefficient facets, and \(r\mathbf1_N\) is an incenter at that minimum. In particular no assumption that an optimal center is symmetric is needed.

For a degree inequality the reciprocal is \(1/[n+1+\sqrt{n+1}]\), since its normal has \(n+1\) unit entries. For a balanced \(K_{t,t}\) it is

\[
 \frac{t}{t^2+2t+\sqrt{t^2+2t}}
 =\frac1{t+2+\sqrt{1+2/t}}.
\]

The denominator \(f(t)=t+2+\sqrt{1+2/t}\) is strictly increasing for real \(t\ge1\): its derivative is \(1-1/(t^2\sqrt{1+2/t})>0\). Consequently, the strongest balanced inequality is the *unique* whole-graph \(K_{n,n}\) inequality, with inverse bound \(f(n)=n+2+\sqrt{1+2/n}\). Edge inequalities are already the \(t=1\) balanced case.

**3. Nonbalanced facets are strictly farther from the proposed center.** For one lifted inequality as in step 1, put

\[
 S=H_0+\tau m=\|a_{\mathrm{lift}}\|_1,\qquad
 H=H_0+(2\tau+\tau^2)m=\|a_{\mathrm{lift}}\|_2^2.
\]

The ratio controlling its inball obstruction is \((S+\sqrt H)/B\). A direct expansion, using \(v=u+\tau(a-b)\), gives

\[
 (u+2)B-S=\tau b(u-a)\ge0.
\]

Moreover,

\[
\begin{aligned}
 (u+2)B^2-H={}&u(u+2)(u-1)\\
 &+\tau\bigl[2ua(u+2)-(a-b)(u+1)-2m\bigr]\\
 &+\tau^2\bigl[(u+2)a^2-m\bigr].
\end{aligned}
\]

Every coefficient is strictly positive: \(u\ge2\), \(1\le a<u\), \(0\le b<a\) imply \(m\le a(u+1)\) and \(a-b\le a\), so the linear coefficient is at least \(a[2u(u+2)-3(u+1)]>0\); the quadratic coefficient is at least \(a[(u+2)a-(u+1)]>0\). Hence \(\sqrt H/B<\sqrt{u+2}\), and

\[
 \frac{S+\sqrt H}{B}
 <u+2+\sqrt{u+2}
 \le n+1+\sqrt{n+1}.
\]

The final inequality uses \(u\le n-1\). Thus *every* nonbalanced lifted facet is strictly weaker for the Euclidean inball than a vertex-degree facet, even though it is necessary in the full facet description.

**4. The exact radius and the integer transition.** Steps 1--3 yield

\[
 \rho_n^{-1}=\max\left\{f(n),\;n+1+\sqrt{n+1}\right\}.
\]

The difference of the degree denominator from the balanced denominator is

\[
 g(n)=\sqrt{n+1}-1-\sqrt{1+2/n}.
\]

Direct substitution gives \(g(2)<0\), \(g(3)<0\), \(g(4)>0\), while \(g(x)\) is strictly increasing for all real \(x\ge3\) because

\[
 g'(x)=\frac1{2\sqrt{x+1}}+\frac1{x^2\sqrt{1+2/x}}>0.
\]

This proves the stated strict cases without an integer equality case.

**5. Uniqueness and every contact.** All \(N\) coordinate facets touch the ball centered at \(\rho_n\mathbf1_N\). When \(n=2,3\), the unique full-graph balanced inequality is also tight. At *any* center of a maximum ball, all coordinates are at least \(\rho_n\), while their sum is at most \(N\rho_n\) by that tight balanced inequality. Therefore all coordinates equal \(\rho_n\).

When \(n\ge4\), every one of the \(2n\) node inequalities is tight at the uniform center. At any maximum-ball center, each node inequality gives \(x_v+\sum_{e\ni v}y_e\le(n+1)\rho_n\); each of its \(n+1\) coordinates is at least \(\rho_n\). Therefore each equals \(\rho_n\), and the node supports cover all \(N\) coordinates. Thus this incenter is unique as well. Strict inequalities in steps 2--4 eliminate all other facet contacts; the irredundant facet list ensures the stated counts. Finally, for large \(n\), the degree denominator is dominant and equals \(n+1+\sqrt{n+1}\), giving \(n\rho_n\to1\).

## Verification

A reproducible checker is included as `scripts/check_total_matching.py` with dependencies recorded in `requirements.txt`. It constructs all facet inequalities, including every parameterized nonbalanced lifted facet, for \(n=2,3,4\) and optimizes the Euclidean inball by linear programming. It also independently maximizes and minimizes individual center coordinates at the predicted radius, verifies tangent-facet types, and checks every size-parameter orbit of lifted inequalities for \(2\le n\le30\). Its successful final marker is `BALANCED_TOTAL_MATCHING_INBALL_VERIFIED`. The proof above, not the finite checker, covers all integers \(n\ge2\).

## Relationship to prior work

Ferrarini [1] introduced balanced and lifted nonbalanced biclique facets of total-matching polytopes. Faenza and Ferrarini [2, Theorem 2] supplied the complete, nonredundant inequality description for complete bipartite graphs. Those known results establish the necessary facets, not the Euclidean largest-ball and contact-classification statement obtained here. In a separate language, \(P_n\) is the stable-set polytope of the *total graph* of \(K_{n,n}\), not the matching polytope of \(K_{n,n}\). The latter distinction matters because its geometry and coordinates differ. A perfect-graph stable-set inradius formula does not cover this family: the total graph already has an induced five-cycle when \(n=2\), and larger total graphs inherit it.

## Limitations

This result concerns simple unweighted balanced complete bipartite graphs in the natural full vertex-and-edge Euclidean embedding. It does not give the inball of unbalanced bicliques, general bipartite graphs, arbitrary weighted or affine realizations, or the John ellipsoid. The supplied computational tests are finite corroboration rather than an independent infinite verification. Historical priority under equivalent Chebyshev-center or stable-set-polytope formulations remains open to further literature checking; the result has not undergone independent mathematical audit.

## References

[1] Luca Ferrarini, *Facets of the Total Matching Polytope for bipartite graphs*, arXiv:2111.15528 (first publicly posted 2021-11-30). https://arxiv.org/abs/2111.15528

[2] Yuri Faenza and Luca Ferrarini, *The Total Matching Polytope of Complete Bipartite Graphs*, arXiv:2303.00328 (first publicly posted 2023-03-01), especially Theorem 2 and equation (7). https://arxiv.org/abs/2303.00328
