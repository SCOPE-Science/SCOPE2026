# A sharp inverse-population welfare gap for odd professional networks

## Finding

For every odd integer \(n\ge 3\), with frictionless network formation \(\gamma=0\) and admissible fixed probabilities \(0<p\le q\), \(p+q\le1\), the average-welfare gap between the social optimum and a maximal matching \(M_n\) satisfies \[\frac{q(p-\frac34p^2)}{n}\le \bar U_n^*-\bar U(M_n)\le \frac{1-q(1-p)}{n}.\] Thus, for fixed \(p,q>0\), the gap is \(\Theta(n^{-1})\); the lower bound is witnessed by replacing one isolated vertex and one edge of \(M_n\) with a triangle, which raises total welfare by exactly \(q(p-\frac34p^2)\).

## Assumptions and scope

Consider the frictionless Professional Networking Game on a simple undirected graph with an odd number \(n\ge3\) of vertices. Each vertex receives zero exogenous opportunities with probability \(q\), two with probability \(p\), and one otherwise, independently across vertices. Each vertex can use one opportunity; if a vertex receives two, it passes one to a uniformly random neighbor. We assume \(0<p\le q\), \(p+q\le1\), and \(\gamma=0\). The admissible range implies \(0<p\le1/2\).

For a graph \(G\), let \(d_j\) be the degree of vertex \(j\), let an empty product equal one, and write the expected utility as

\[
 u_i(G)=1-q\prod_{j\in N(i)}\left(1-\frac{p}{d_j}\right).
\]

Let \(\bar U(G)=n^{-1}\sum_i u_i(G)\), and let \(\bar U_n^*\) be its maximum over all graphs on \(n\) vertices. The maximal matching \(M_n\) consists of \((n-1)/2\) disjoint edges and one isolated vertex. The comparison graph \(T_n\) consists of one triangle and \((n-3)/2\) disjoint edges. The claim bounds the gap to the optimum; it does not assert that \(T_n\) is globally optimal.

## Proof

A vertex in a disjoint edge has a degree-one neighbor, so its expected utility is

\[
 u_2=1-q(1-p).
\]

An isolated vertex has utility \(u_0=1-q\). In a triangle, each of the two neighbors of a deficient vertex has degree two and passes to that vertex with probability \(p/2\). Independence of the neighbors' exogenous draws gives

\[
 u_3=1-q\left(1-\frac p2\right)^2.
\]

There are two edge-vertices and one isolated vertex in the affected three-vertex component of \(M_n\), whereas \(T_n\) uses a triangle on those three vertices. All other edge components cancel in the welfare difference. Hence

\[
\begin{aligned}
 W(T_n)-W(M_n)
 &=3u_3-2u_2-u_0\\
 &=q\left[3-2p-3\left(1-\frac p2\right)^2\right]\\
 &=q\left(p-\frac34p^2\right)>0.
\end{aligned}
\]

Since \(\bar U_n^*\ge\bar U(T_n)\), division by \(n\) proves the lower bound.

For the upper bound, the primary source proves via AM--GM that every graph has average utility at most \(u_2=1-q(1-p)\). Also,

\[
 \bar U(M_n)=\frac{(n-1)u_2+u_0}{n}\ge\frac{n-1}{n}u_2,
\]

because \(u_0=1-q\ge0\). Therefore \(\bar U_n^*-\bar U(M_n)\le u_2/n\). Combining the two bounds gives the displayed interval. For fixed admissible \(p,q>0\), both constants are positive, so the gap is \(\Theta(n^{-1})\). No characterization of the globally optimal odd-order graph is needed for this conclusion.

## Verification

The three component utilities follow directly from the published expected-utility formula with \(\gamma=0\). The substitution and simplification of \(W(T_n)-W(M_n)\) are exact. The upper bound is the published AM--GM bound from Proposition 4.2's deferred proof. The argument uses no finite enumeration, numerical approximation, or unproved asymptotic interchange.

## Relationship to prior work

Dwork, Hays, Kleinberg, and Raghavan state that a perfect matching is efficient when it exists and that, for odd \(n\), maximal matchings achieve average utility within \(o(1)\) of the optimum. Their Appendix C gives the explicit upper bound \([1-q(1-p)]/n\). The calculation here supplies a positive lower bound \(q(p-3p^2/4)/n\) by an explicit triangle substitution. Together, the bounds show that the finite-size gap has the sharp order \(\Theta(1/n)\) for fixed admissible parameters. The result does not claim exact optimality of the triangle-plus-matching graph.

## Limitations

The result applies only to the frictionless model, odd \(n\ge3\), independent exogenous opportunity draws, and fixed parameters satisfying \(0<p\le q\) and \(p+q\le1\). The constants are not uniform if \(p\) or \(q\) varies with \(n\). The globally optimal graph for odd \(n\) remains unclassified by this result. Independent audit has not been performed.

## References

1. C. Dwork, C. Hays, J. Kleinberg, and M. Raghavan, “Equilibria, Efficiency, and Inequality in Network Formation for Hiring and Opportunity,” arXiv:2402.13841v1, first submitted 21 February 2024, Sections 3 and 4.1, Proposition 4.2, Appendix C. https://arxiv.org/abs/2402.13841
2. Mathematics Subject Classification 2020, code 91A43, “Games involving graphs.” American Mathematical Society, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=91A43
