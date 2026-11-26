# Independent mathematical audit

## correctness

PASS

Taking absolute values cannot increase the input edge variation; if the absolute values are constant the output variation is zero. For nonnegative data subtraction of the minimum, rotation, and scaling give f₀=0 and variation at most one. The signed edge expression has vertex coefficients σᵢ₋₁−σᵢ. At its positive vertices expand the radius choice, and at its negative vertices use a majorant of every average, which attains the optimum at the maximum. This gives the exact LP decomposition; weak duality requires both nonnegative multipliers and one inequality for each nonnegative variable. I wrote and ran a separate checker using shortest-arc graph distances and direct t, z, and f coordinate inequalities rather than the frozen matrix builder. It exhausted branches 730, 2186, 12032, 38912 and respectively checked 9494, 33514, 213760, 782464 dual coordinates, in addition to each dual objective and each witness. The least radius containing the point mass gives 1/min(2k+1,n) at distance k, so the values telescope around both arcs, attaining the upper bound. Exact replay: python3 /tmp/opencode/scope_independent_cycle_audit.py; it reads the frozen JSON data, not the supplied executable checker.

## originality

PASS

Best-of-knowledge pass for the four upper bounds on arbitrary real centered cycle data, not for the point-mass lower bound or the formula in general. The strongest indexed overlap gives the identical formula after equal-weight specialization, but only for cycles of length three through five; the strongest literature graph census also stops at five. Neither these nor the other inspected statements justify the four upper bounds by specialization. The same-day relationship is not a priority determination.

## value

PASS

Cycles are the natural periodic analogue of paths for one-dimensional maximal variation, and the optimal contraction rather than any bound is a meaningful benchmark. These are the two full next diameter levels beyond the five-vertex census, including both even and odd saturation of graph balls. The result tests the same point-mass conjectural mechanism across those next levels and certifies the precise arbitrary-data invariant rather than repeating a numerical or witness-only computation. No general-cycle theorem is needed to make those exact benchmarks useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
