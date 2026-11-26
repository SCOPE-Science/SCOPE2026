# Independent mathematical audit

## correctness

PASS

The positive cube is forward invariant. Equilibrium leaf equations in each represented clique reduce to y_j=(1−τh)/d_j; the hub equation reduces to (1−τH)h=1−H. H has strictly positive derivative, starts at 0 and tends to r>1, and for H>1 the formal root is either nonpositive or exceeds 1/τ (with the singular equation inconsistent). For a positive trajectory, the clique total satisfies the logistic lower inequality S'_j≥(1−τ)S_j−S_j². The same-clique log ratio of extreme coordinates decreases under the stated identity, so the positive lower bound on each S_j protects every leaf; an initially ordered pair cannot cross. The quadratic potential has nonnegative derivative, zero precisely at equilibria in the invariant cube. A connected omega-limit set with leaves bounded away from zero must thus be one of the enumerated equilibria. The hub invasion rate 1−H excludes convergence to E_0 below threshold from positive hub data. At criticality let u=P⁻¹1 be the positive leaf vector, z=y−u, and η=z/h+τu. The exact leaf equation gives η'=[−diag(y)P−(h'/h)I]η+(h'/h)τu. In the P quadratic norm, P positive definite and y bounded away from zero yield uniform strict damping for large t, since h'/h tends to zero; the forcing tends to zero too. Thus η→0 without assuming boundedness of z/h. Then (1/h)'→1−τ using H=1, giving the stated hub and leaf coefficients. The clique-merger difference has the displayed strictly positive numerator for 0<τ<1; the terminal complete graph has threshold 1 and the worked (4,2) root solves 7τ²+2τ−1=0. Inspected RESULT.md, VERIFICATION.md, requirements.txt and verify.py; the supplied finite symbolic/numerical checks were not executed and do not establish the dynamics.

## originality

PASS

General fixed-point inversion, the star and complete extrema and prior full-coexistence stability are established. A catalogue windmill theorem additionally matches the equal-size-two threshold. The distinct contribution supported by the comparison is the arbitrary-partition sharp classification, including the boundary and above-threshold selection from all strictly positive data, exact critical amplitudes and strict monotonicity for degree-changing clique mergers.

## value

PASS

The result interpolates between known extremal ecological graphs using an exact structural parameter, decides the long-time fate even where the positive equilibrium is lost, and quantifies the slow critical extinction and surviving leaf response. The merger comparison is an explicit topology effect with a defined scope, not a claim about generic clustering or degree-preserving rewiring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
