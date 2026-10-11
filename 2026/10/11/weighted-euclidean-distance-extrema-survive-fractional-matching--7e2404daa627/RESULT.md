# Weighted Euclidean distance extrema survive fractional matching relaxation

## Finding

Let \(G=(V,E)\) be any finite loopless simple graph with at least one edge. Denote by \(\mathcal M(G)\) the convex hull of its matching-incidence vectors, and by
\[
\mathcal F(G)=\left\{x\in\mathbb R_{\ge0}^{E}:\sum_{e\ni v}x_e\le1\ \text{for every }v\in V\right\}
\]
the fractional matching polytope. Fix strictly positive diagonal weights \(w_e>0\), and write \(\|z\|_w^2=\sum_{e\in E}w_ez_e^2\).

**Theorem.** For every nonnegative center \(c\in\mathbb R_{\ge0}^{E}\),
\[
\boxed{\max_{x\in\mathcal F(G)}\|x-c\|_w^2
=\max_{M\text{ matching}}\|\mathbf1_M-c\|_w^2.}
\]
Every nonintegral vertex of \(\mathcal F(G)\) has **strictly smaller** squared distance than the maximum. In fact, write the nonintegral vertex as isolated unit-weight matching edges together with vertex-disjoint odd cycles \(C_1,\ldots,C_s\) carrying weight \(1/2\). If \(\ell_j=|E(C_j)|\), then there exists an ordinary matching \(M\) such that
\[
\|\mathbf1_M-c\|_w^2-\|x-c\|_w^2\ge
\sum_{j=1}^{s}\sum_{e\in E(C_j)}w_e
\left(\frac{\ell_j-2}{4\ell_j}+\frac{c_e}{\ell_j}\right)>0.
\]

Consequently, **the minimum enclosing weighted Euclidean balls of \(\mathcal M(G)\) and \(\mathcal F(G)\) have exactly the same unique center and radius**. Every nonintegral point of \(\mathcal F(G)\) lies strictly inside this common ball. Their weighted Euclidean diameters likewise agree:
\[
\boxed{\operatorname{diam}_w^2\mathcal F(G)
=\operatorname{diam}_w^2\mathcal M(G)
=\max_{M,N\text{ matchings}}\sum_{e\in M\triangle N}w_e.}
\]
Every diametral endpoint is an integral matching vertex. Equivalently, the last maximum is the largest total edge weight of a subgraph whose nontrivial components are paths or even cycles.

## Assumptions and scope

All graphs are finite, loopless and simple; isolated vertices are permitted, but the edge set is nonempty. The metric is diagonal with \(w_e>0\). Only the *pointwise farthest-point* identity requires \(c_e\ge0\): a minimum enclosing ball, whose center is unknown in advance, automatically has nonnegative center. The diameter concerns Euclidean distances in edge-coordinate space, **not** shortest-path distance along the polytope's one-skeleton. No integrality of the maximizing fractional objective \(\sum_ex_e\) is asserted.

## Proof

**1. Extreme-point structure.** Every vertex of \(\mathcal F(G)\) has coordinates in \(\{0,1/2,1\}\). Its coordinates equal to one form a matching whose endpoints support no other positive coordinates. Consider the subgraph \(H\) of remaining edges carrying strictly fractional coordinates \(0<x_e<1\). For extremality, the active vertex-degree equalities must uniquely determine those fractional coordinates. A vertex of degree one in \(H\) cannot have its degree inequality tight, because that would force its single positive incident coordinate to equal one. A connected component of \(H\) that is not a cycle has strictly more fractional edges than vertices with potentially tight degree equalities: writing \(t\) for the number of vertices of degree at least two within that component, the handshaking identity gives
\[
|E(H)|-t=\frac{n_1+\sum_{v:\deg_H(v)\ge2}(\deg_H(v)-2)}2>0,
\]
where \(n_1\) counts degree-one vertices in the component. Thus such a component has a nonzero feasible two-sided perturbation and cannot occur in an extreme point. A cycle has as many edges as degree constraints; all must be tight, giving \(x_{e^-}+x_{e^+}=1\) around the cycle. An even cycle has a nontrivial alternating perturbation; an odd cycle forces every coordinate to \(1/2\). Conversely, odd half-cycles together with isolated unit edges are determined by active constraints and are vertices. This is also the standard fractional-matching vertex classification in the literature.

**2. Strict distance improvement.** Fix a nonintegral vertex \(x\), and replace each half-cycle \(C_j\) independently by a uniformly random near-perfect matching of that odd cycle. Keep all the unit-weight edges of \(x\). Each cycle edge occurs with probability \(p_j=(\ell_j-1)/(2\ell_j)\). The random union is always a genuine matching. On a half-cycle edge \(e\), the difference between the expected rounded squared distance and its original contribution is exactly
\[
 w_e\left[p_j(1-c_e)^2+(1-p_j)c_e^2-(1/2-c_e)^2\right]
 =w_e\left(\frac{\ell_j-2}{4\ell_j}+\frac{c_e}{\ell_j}\right).
\]
All other edge contributions are unchanged. Summation proves the stated positive mean gain; at least one matching attains at least this mean. This excludes every nonintegral vertex from maximizing distance to any nonnegative center. Since a convex quadratic achieves its maximum on vertices of a compact polytope, the pointwise identity follows.

**3. Identical smallest enclosing balls.** For each \(x\ge0\), replacing a negative coordinate \(c_e<0\) of a proposed center by zero strictly decreases \(\|x-c\|_w^2\); the decrease is at least \(w_ec_e^2>0\). Hence every minimax center of either polytope lies in the nonnegative orthant. By Step 2, the two minimax radius functions agree there, proving equality of optimal radii and centers. Uniqueness follows from the strict-convexity identity
\[
\left\|x-\frac{a+b}{2}\right\|_w^2
=\frac{\|x-a\|_w^2+\|x-b\|_w^2}{2}-\frac{\|a-b\|_w^2}{4},
\]
valid for every \(x\), and positive weights. No nonintegral point can lie on the boundary: nonintegral vertices have the strict Step 2 gap; a nonvertex on a strictly convex Euclidean sphere cannot be a nontrivial convex combination of distinct points inside its ball.

**4. Identical diameters.** Fix \(y\in\mathcal F(G)\), necessarily nonnegative. Step 2 replaces any farthest \(x\in\mathcal F(G)\) by a matching \(M\) without decreasing distance. Now apply Step 2 again with center \(\mathbf1_M\) to replace \(y\) by another matching \(N\). Maximizing both variables proves diameter equality. The strict part and strict convexity show all diametral endpoints are matching vertices. For incidence vectors, the squared weighted difference is exactly \(\sum_{e\in M\triangle N}w_e\). Their symmetric-difference graph has components alternating between the two matchings: paths and even cycles. Conversely, any disjoint union of paths and even cycles has a proper two-edge-coloring, giving the two matching classes. This proves the graph-theoretic formula.

## Verification

The self-contained Python 3 standard-library script `verify.py` checks the vertex decomposition and distance comparisons with exact rational arithmetic. Its deterministic run covers all 1,024 labeled five-vertex graphs, 160 further six-vertex graph instances, 2,368 nonnegative center cases, 7,300 fractional-vertex distance comparisons, 4,836 odd-cycle gain identities, and 1,184 diameter comparisons. All checks passed. The finite checks do not establish the unrestricted quantifiers; these follow from the proofs in Steps 1–4.

For a sharp hypothesis boundary, on a triangle with unit weights and center \(c=(-10,-10,-10)\), the half-integral vertex is at squared distance \(330.75\), whereas the farthest matching vertex has squared distance \(321\). Thus nonnegativity cannot be omitted from the *pointwise* statement. For a triangle with \(c=0\), the strict improvement over the half-cycle is exactly \(1/4\).

## Relationship to prior work

The classical description of the fractional matching polytope and its half-integral vertices underlies the argument. Blanchard–De Loera–Louveaux study monotone simplex-path length for these matching polytopes, while Sanità investigates their **combinatorial one-skeleton diameter**; neither inspected result states this weighted Euclidean farthest-point identity or the two metric invariance conclusions. Behrend analyzes fractional perfect matching structures and incidence ranks, which inform the vertex analysis but do not settle these metric extremal claims. The result should not be confused with a John (maximum inscribed-volume) ellipsoid: that is a different, dual-type optimization. Earlier equivalent results under diagonal convex-quadratic optimization terminology remain possible.

## Limitations

The pointwise theorem needs nonnegative centers and strictly positive diagonal weights; non-diagonal quadratic forms and signed centers are outside its scope. The proof does not give a polynomial-time algorithm for maximizing the graph-theoretic diameter formula. Literature priority remains subject to wider expert checking, including alternative nomenclature for separable convex quadratic optimization. No independent scientific audit has been performed.

## References

1. M. Blanchard, J. A. De Loera, Q. Louveaux, *On the Length of Monotone Paths in Polyhedra*, arXiv:2001.09575 (first publicly posted 2020-01-27), §§1, 3 and results on matching/fractional-matching polytopes; SIAM Journal on Discrete Mathematics 35 (2021), 1746–1768, DOI 10.1137/20M1315646. Primary MSC 52B12.
2. L. Sanità, *The diameter of the fractional matching polytope and its hardness implications*, arXiv:1806.03397 (2018), §§1–2 and appendix, on one-skeleton path distances and half-integral extreme points.
3. R. E. Behrend, *Fractional Perfect b-Matching Polytopes I: General Theory*, arXiv:1301.7356 (2013), including incidence-matrix rank characterization and vertex structures.
4. J. Edmonds, *Maximum matching and a polyhedron with 0,1-vertices*, Journal of Research of the National Bureau of Standards B 69 (1965), 125–130 (as cited in [1]).
