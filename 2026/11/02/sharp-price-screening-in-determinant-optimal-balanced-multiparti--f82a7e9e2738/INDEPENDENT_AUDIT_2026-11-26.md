# Independent mathematical audit

## correctness

PASS

For r≥3, m≥2 and positive prices and budget, connected feasible points have a positive grounded determinant and disconnected points cannot maximize it. The grounded Laplacian is injective in the weights of this simple graph, so strict log-det concavity gives uniqueness, and orbit averaging/invariance reduces the optimizer to two weights without constraining the original optimization. The four nonzero eigenvalue blocks are (r−1)mx, m[x+(r−2)y], m[x+(r−1)y], and rmx with multiplicities m−1, (r−1)(m−1), r−2, and 1; their product divided by rm gives the claimed tree polynomial. With u=r−2, v=r−1 and N=rm−1, the derivative divided by u is v(m−1)/(1+ut)+v/(1+vt)−NQ/(2P+uQt). Clearing its positive denominator gives C+Lt−At² as stated. If C>0 there is one positive root. If C≤0 the linear term is strictly negative (already negative at equality and decreasing in Q), so t=0 is the unique optimizer. Independently, on the bipartite support the active resistance is (rm−1)/(m²(r−1)x) and the inactive-endpoint resistance is 2/(mx); their ratio gives the same KKT cutoff including equality. Near the critical price, a positive root satisfies t=C/(−L+At); using L=−2Pm(r−1)(r−2)/r+O(1) and C/P=2(r−1)/r−rγ+γ/m gives the positive-part limit, including t=O(m⁻²) at equality of the limiting prices. Independent exact spanning-tree enumeration on K_{2,2,2} gives determinants 32 and 4608 and equal marginal gain per price across individual edges at (x,y,Q/P)=(1,0,8/5) and (2,1,28/23).

## originality

PASS

The supported contribution is the full all-r price allocation (quadratic interior conductances and exact critical-window profile, together with the screening regime), not tree enumeration, log-det optimization, or the generic resistance test for edge deletion. No equivalent coverage of that full claim was found in the inspected comparisons.

## value

PASS

In a standard determinant criterion on a natural network family, the result tells a designer exactly when an entire price class can be removed without losing optimality, proves that no asymmetric individual allocation improves the design, and quantifies how much conductance is retained through the transition. The critical profile and closed interior solution give actionable information beyond existence or a tree-count formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
