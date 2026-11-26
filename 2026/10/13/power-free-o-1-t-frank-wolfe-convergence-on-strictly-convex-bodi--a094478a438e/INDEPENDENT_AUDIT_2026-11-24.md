# Independent mathematical audit

## correctness

PASS

Work in the translated affine span and let h_t be objective error. A positive h_t gives positive g_t≥h_t and nonzero projected gradient. Strict convexity excludes any positive-dimensional exposed face for a nonzero direction in this span; compactness and uniqueness give continuity of s(u). On the unit sphere times C restricted to ||z−s(u)||≥ε, the support gap is continuous and strictly positive, hence has a positive minimum ω(ε). For ε<diam(C)/2 the restricted set is nonempty by considering a diameter pair. Along the chosen segment the smoothness bound is f(x_t)−γg_t+Lγ²d_t²/2. The short step minimizes this bound and line search does at least as well, giving decrease at least min(g_t,g_t²/(Ld_t²))/2. With bounded d_t and g_t≥h_t this proves h_t→0; compactness then gives δ_t=dist(x_t,argmin f)→0. Convexity gives h_t≤||Π∇f(x_t)||δ_t, and therefore g_t/h_t≥ω(ε)/δ_t whenever d_t≥ε. For positive errors, the reciprocal error increment is at least the decrease divided by h_t². It is at least 1/(2h_t) in the clipped branch; in the untruncated branch it is at least 1/(2Ld_t²), or at least ω(ε)²/(2LD²δ_t²) when d_t≥ε. Fixing sufficiently small ε for each desired increment and then taking t large proves divergence along all indices, including mixed branches. Cesàro averaging proves t h_t→0. A singleton and a terminated trajectory (extended constantly) are immediate; zero gap is equivalent to constrained optimality by convexity and first-order necessity. The superflat epigraph/hypograph example is strictly convex by h''>0 off zero, continuous strict increase of h' across zero, and strict concavity of the upper curve; at the vertical tip its power-normalized support gap tends to zero. No computational or formal certificate is needed for this analytic result; scope is exact LMO, finite dimension and the two adaptive steps only.

## originality

PASS

Credit Pokutta's reciprocal-error approach, little-o convergence under power-type local dual sharpness (already including zero-gradient objectives), and the superflat obstruction. Credit the earlier nonzero-optimal-gradient overlap indicated by Dunn's reported condition, without assuming completeness of that report. The supported distinct contribution is the all-objectives convergence theorem with purely qualitative strict convexity, including zero projected gradient without power-type local geometry. None of the inspected decisive statements supplies this combination; no originality is credited to the superflat construction itself or to zero gradient with LDS.

## value

PASS

The theorem removes a quantitative geometric hypothesis, not merely an exponent in an already valid estimate. It gives a strict asymptotic improvement over the general 1/t scale for both standard adaptive steps on all compact relatively strictly convex feasible sets, including bodies too flat for every fixed power and objectives with zero projected optimal gradient. The fixed-separation argument explains why that gain is possible without any uniform numerical rate claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
