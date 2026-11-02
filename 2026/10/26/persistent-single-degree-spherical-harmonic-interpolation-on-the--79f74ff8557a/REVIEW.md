# Independent mathematical audit

## correctness

PASS

PASS. The 24 truncated-octahedral vertices are all permutations of (0,±1,±2)/√5, grouped into 12 antipodal pairs. For fixed degree ℓ, the spherical addition theorem makes evaluation rank equal to rank of the 12×12 real symmetric Gram matrix G_ℓ=(P_ℓ(v_i·v_j)) on parity-compatible representatives; positive scalar factors do not alter rank. Legendre arguments are rational j/5, −4≤j≤5, so the three-term recurrence supplies exact rational certificates. Independent exact Gaussian elimination freshly computed all 129 ranks ℓ=0..128 and reproduced [1,3,5,6,9,9,10,12,11] for ℓ=0..8, followed by rank 12 through 128; it also verified that the degree-six harmonic H=(x²−y²)(y²−z²)(z²−x²) evaluated on representatives spans a nonzero annihilator for G_8. For all ℓ≥129, distinct nonantipodal reps satisfy |dot|≤4/5, and Bernstein |P_ℓ(t)|≤sqrt(2/(πℓ sqrt(1−t²))) bounds each off-diagonal by sqrt(10/(3πℓ)), giving Gershgorin row sum ≤11 sqrt(10/(3πℓ))<1; the last inequality is rigorously established at 129 using π>223/71 and 85910/86301<1. Therefore no extrapolation from ℓ≤128 is required. Full rank at ℓ=7 then dip ℓ=8 makes the permanent threshold ℓ≥9 sharp; parity-compatible data, not arbitrary inconsistent antipodal values, is interpolated.

## originality

PASS

PASS best-of-knowledge for the explicit all-degree RANK PROFILE of exact-degree harmonics on the 24-point truncated-octahedral orbit, including a nonmonotone ℓ=8 defect and permanent threshold ℓ=9. The addition theorem, interpolation criteria and general spherical designs are known and not presented as novel. The inspected An–Chen–Sloan–Womersley 2010 and Khalid–Kennedy–McEwen 2014 primary full texts concern low-pass spherical-design or bandlimited sampling schemes (with varying node sets), not this fixed single-degree 24-vertex rank classification. Related finite-group and lattice-orbit harmonic decompositions might already encode the same profile, and inaccessible/unindexed tables remain genuine risk. No inspected stronger theorem was found to imply all listed ranks and tail.

## value

PASS

PASS. The Archimedean truncated octahedron is a canonical symmetric 24-point sampling orbit. Fixed-frequency spherical-harmonic interpolation differs from band-limited interpolation, and an exact exceptional loss at degree 8 after full rank at degree 7 is a meaningful representation-theoretic obstruction. Identifying the persistent degree-nine threshold and explicit blind mode, with a complete rational/analytic certificate, is a natural complete classification rather than an arbitrary computed slice. No claim of good numerical conditioning is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
