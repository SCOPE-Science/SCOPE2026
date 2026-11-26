# Independent mathematical audit

## correctness

PASS

For any delta in (0,1/6] choose r>=1 so that a=1/(3*2^r)<4 delta, then choose a<c<min(2a,4 delta). This guarantees c<1/3 and c/2<a<c<2a. The external branches required by the cited model agree because the lower breakpoint is at least 1/3 and the upper breakpoint at most 2/3. On [c,1-c/2) the right branch of f0 starts at 2 delta>c/2 and ends below 1-c, while its left branch is between c/2 and 1/3; on [c/2,1-c) the left branch of f1 starts at c and is below 1-2 delta<1-c/2, while the right branch starts at least at 2/3 and ends below 1-c/2. Thus the half-open core is admissible. The atoms a,2a,...,1/3 and their reflections 2/3,...,1-a put precisely the endpoints in opposite strips. At all interior atoms the two maps go to the preceding and following atom. In particular f1(1/3)=2/3 and f0(2/3)=1/3 even at delta=1/6, where the equality branches give the same values; the first and last sites deterministically reflect inward. Detailed balance holds with weights proportional to the path degrees (1 at the endpoints, 2 inside, total 2(2r+1)). Both gate masses are equal and positive. For positive-measure sets choose support atoms and a nearest-neighbor path of positive probability, proving annealed metric transitivity; aperiodicity is not required. Theorem 1.2 and Remarks 1.3 and 1.5 of Nakamura–Nakano–Toyokawa–Yano now give the ordinary arcsine law for each support point, whose point mass is absolutely continuous with respect to this discrete measure. The original-time and accelerated maps are not identified. The supplied rational checker was inspected, not executed; the strict inequalities prove the continuum statement.

## originality

PASS

The supported contribution is an explicit thirds-based stationary finite-core witness charging both gates for every nonzero generalized Hata–Yano parameter, notably all previously uncovered 0<delta<1/8 in the problem-posing paper. The prior conditional limit theorem is not itself new. The closest distinct indexed finding has a meaningful overlap in the same reflected-path mechanism and has all-parameter arcsine examples on a different dyadic lattice; it is indexed a week later and does not give the specific non-dyadic witness. No first-publication claim is made.

## value

PASS

This explicitly fills an existence gap asked in the original core-law paper, including the whole small positive interval not covered by its deterministic construction. The concrete finite measure gives checkable witnesses and identifiable initial points rather than asserting a new limit theorem or relying on sampling parameters. The separate Gharaei–Homburg question and all-initial-point behavior are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
