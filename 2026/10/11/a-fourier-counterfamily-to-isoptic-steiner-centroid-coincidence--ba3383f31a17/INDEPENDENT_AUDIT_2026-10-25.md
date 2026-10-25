# Independent mathematical audit

## correctness

PASS

For |eps|<1/11 the support radius is 1-3eps cos(2t)-8eps cos(3t)>0, giving a smooth strictly convex oval. Since there is no first Fourier harmonic, ∫(p e_t+p′ n_t)dt/(2π)=(0,0). The orthoptic is the intersection of support lines at t and t+π/2, z=p e_t+q n_t with g=-cos2t+sin3t. Differentiating gives B=-1+eps(f′-g), C=1+eps(f+g′), and exact curvature measure 1+(B C′-C B′)/(B²+C²). An independently written Laurent/Fourier coefficient convolution (not executing the source verifier) yields zeroth and first centroid coefficients 0 and exact quadratic coefficient (2,0). Uniform smooth remainder follows from positive B²+C² near eps=0. The orthoptic is a smooth embedded, positive-curvature perturbation of radius-sqrt2 circle, hence turning 2π and the same curvature-centroid normalization. Therefore its centroid is (2eps²+O(eps³),0) and differs from the original for every sufficiently small nonzero real eps; the theorem asserts no explicit maximal eps0. Independent numerical quadrature of the UNEXPANDED centroid at +/-0.005, +/-0.01 and turning integral corroborates the coefficient but is not the universal proof.

## originality

PASS

The 2014 Mozgawa paper explicitly asks whether the Steiner centroids of an oval and any of its isoptics coincide; it establishes coincidence only for circular isoptics. The 2021/2022 Cieslak–Mozgawa direct follow-up classifies circular isoptics rather than noncircular orthoptic Steiner centroids. The 1996 primary geometric isoptic treatment covers annular areas, tangent angles, constant-width special cases and differential equations, not the asserted quadratic centroid drift. Resultary and targeted primary-literature searches found no distinct theorem with the same negative implication. This is a best-of-knowledge priority assessment, not a proof of novelty; inaccessible original 1991 chapter remains an explicit residual risk.

## value

PASS

The primary 2014 paper poses precisely a universal isoptic–Steiner-centroid coincidence question. Producing an explicit smooth strictly convex counterfamily with a rigorously nonzero second-order orthoptic displacement resolves that well-motivated problem negatively. Two simple support harmonics reveal the mechanism and can guide further study of which angles or symmetry constraints preserve the curvature centroid. This is not a routine restatement of standard support parametrization or a numerical anomaly; the exact perturbative sign for all small nonzero eps is its substantive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
