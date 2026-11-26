# Independent mathematical audit

## correctness

PASS

KKT gives 0 for a ball containing 0 and otherwise the unique active step y=(I+sH)⁻¹x at distance h. For a dyadic eigenspace the maximal fractional decrement is less than twice the minimal one, so the projected step is bounded by twice the projected radial decrement; telescoping gives 2 times the sum of initial projected norms. Cauchy–Schwarz counts only occupied bands m, hence proves the stated bound with m≤p=1+floor(log₂κ), which counts the entire grid including empty bands. Coordinatewise signed monotonicity proves the independent ℓ₁ and √d bounds, also for summable radii. All nonterminal constant-radius steps have length h, so finite length forces termination with the stated bound. For the geometric family, each disjoint-interior time window [2⁻ʲ⁻¹,2⁻ʲ] contributes at least (e⁻¹ᐟ²−e⁻¹)/√p in coordinate j. On a fixed compact nonzero subarc the normalized flow is smooth in a tube and the implicit-step residual is O(h²). The local implicit solution in that tube is the exact ball minimizer by KKT; a tube-exit induction with Lipschitz stability gives O(h) error through floor(a₀/h) active steps for all sufficiently small h. Taking a₀ up to the arclength at t=1 proves the lower bound. The lower limit is at fixed H and fixed radius within each run, not an arbitrary-radii count. Independently solved scalar multipliers with Brent's method for p=2,4,8 and three fixed radii, plus separate flow quadrature; the h=.001 call lengths were 1.046, 1.166 and 1.413. Replay: OPENBLAS_NUM_THREADS=1 python /workspace/independent_checks.py (NumPy and SciPy). The finite diagnostics do not establish the limit.

## originality

PASS

The supported distinction is the explicit arbitrary-radius bound for the exact variable-resolvent orbit, refined by the number of occupied bands, and the use of that discrete geometry to establish sharp order for fixed-radius oracle counts. The ball algorithm, general finite-length and fixed-dimensional call laws, and the spectral √logκ order and geometric lower-bound mechanism for ordinary quadratic flow are credited prior work. The new scope is the exact implicit iteration, not discovery of the continuous spectral phenomenon.

## value

PASS

Spectral occupancy is a natural instance measure for exact quadratic minimization. A dimension-independent length estimate also for nonterminating and adaptive-radius runs answers a trajectory question that finite-call estimates alone do not. The all-band example certifies a sharp obstruction in the small-radius oracle count; it measures actual motion rather than just objective decrease. The value is the explicit discrete guarantee and the transfer in both directions, not the already known continuous-flow order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
