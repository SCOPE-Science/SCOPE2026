# Independent mathematical audit

## correctness

PASS

The polytope is the unit cube with a single positive normal halfspace cap in any d≥2 and T>0, so it is full dimensional and has exactly two possible vertex types: retained Boolean vertices S with a(S)≤T, and cut-edge vertices along edges from feasible S (a(S)<T) to infeasible S∪{i} (a(S)+a_i>T). Every retained Boolean vertex has an exclusive strict sign orthant of inward directions; for each absent singleton a_i>T, the new cut vertex on its edge from the all-negative corner requires another disjoint cone with u_j>0 (j≠i) and a·u<0, which forces u_i<0 and is incompatible with all kept orthants and other such cut vertices. This supplies |V|+|J| independent fractional weight lower bounds. Explicit directions u^S use one coordinate −2A/a_r and appropriate remaining signs (and u^∅ all plus), while absent singleton directions w^i have a large negative i-th coordinate; each strictly enters all active facets of every vertex. Thus the ordinary upper bound matches the fractional lower bound. Ties are covered by weak retained-vertex and strict edge crossing inequalities; cancellation of singleton thresholds gives d+1+#{|S|≥2,a(S)≤T}. Reconstructed rational cut-edge lists and independent strict active-normal checks for six examples including tied thresholds verified coverage; the proof, not these bounded checks, covers arbitrary real weights and all d.

## originality

PASS

The exact weighted threshold staircase for a single halfspace-capped cube is not implied by general cube local-maximality, shallow independent-corner truncations, product-of-simplices illumination or universal fractional upper bounds. Checked the equivalent Boolean weighted knapsack count and the correction from cut edges, with the one-corner known special case explicitly acknowledged. Best-of-knowledge, with residual risk of older clipped-box identities.

## value

PASS

This theorem gives a dimension-uniform, complete, exact law for both ordinary and fractional illumination of a geometrically natural anisotropic single-facet perturbation of the cube, with all tied thresholds. The extra cut-edge witness shows retained cube vertex counting can be false (weights (3,1,1), T=5/2 give I=5, not 4), and singleton cancellation yields a sharp subset-sum staircase. It supplies many exact real convex-body illumination cases beyond upper-bound-only results and has a clear role in understanding fractional integrality and hypercube perturbations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
