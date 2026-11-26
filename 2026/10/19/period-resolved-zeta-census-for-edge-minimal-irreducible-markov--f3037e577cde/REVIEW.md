# Independent mathematical audit

## correctness

PASS

For the repaired result, the unique branching vertex generates two first-return cycles covering all vertices, with a common deterministic suffix. Their lengths realize the stated inequalities, and making the two disjoint forward branches and common return path produces every pair; precisely the double Hamiltonian equal case would require parallel edges. Their intersection leaves only the two single-cycle determinant terms. The gcd is the period, and at z=1 the determinant −1 gives trivial Bowen–Franks group and unit, matching the full two-shift under the irreducible non-permutation classification. Writing a=du,b=dv reduces the sum condition to u+v≥floor(N/d)+1 for coprime u<v; subtracting φ(s)/2 per excluded sum gives T, with the diagonal contributing only for d<N<2d. The mixing profiles genuinely arriving are the φ(N) pairs (a,N); the losses are the φ(N)/2 unordered coprime pairs of sum N. Net change is therefore precisely φ(N)/2. No endpoint exception occurs for N≥3; d≥N gives no admissible profiles. Inspected the frozen verification notes and VERIFY_SPARSE.py; not executed. The program's small graph tests are primitive comparisons and its larger arithmetic test uses the parameter set, not exhaustive graph generation or a turnover certificate. The repaired turnover follows symbolically.

## originality

PASS

Bounded pass for the corrected period-stratified distinct-zeta census within the exact N+1 edge family, with its exact mixing turnover. The butterfly form, two-return polynomial, and continuous-orbit-equivalence criterion are prior; this is a modest arithmetic refinement, not a new graph or orbit-equivalence classification.

## value

PASS

The parameter slice is the smallest edge budget beyond directed cycles, not a discretionary cutoff. Period-by-period counts quantify the number of zeta-distinguished shifts within a single COE class and recover the sharp mixing census. The turnover correction also distinguishes actual profile change from the growth of the count. This is a useful exact invariant of a natural family, not a claim about classification of equal-zeta shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
