# Independent mathematical audit

## correctness

PASS

On labelled bidirected cycles stable sets are independent dominating sets. The cyclic membership language excludes 11 and 000 in each coordinate, so the trace counts each labelled ordered pair once with target-symbol XOR weight. Independently used a 9-state pair automaton (age of the last occupied site in each coordinate); exact determinant, length-one and length-two corrections, and two dominant-root derivatives all agree. Replay: python3 /workspace/audit-04-reproduce.py (SymPy); no frozen script was executed. At t=1 the one-coordinate recurrent shift has cycles of lengths 2 and 3 and is irreducible, hence primitive, as is its tensor square. Analytic isolation of its simple Perron root gives a uniform exponentially small trace error near t=1; differentiating and substituting the centered characteristic-function argument proves the stated moments and Gaussian limit, with strictly positive exact variance. For odd n the sole agreement vertex cannot be in both sets (its neighbors would also have to agree), so an alternating path with that one uncovered vertex gives precisely 2n possibilities; even n has the two proper alternating assignments. These arguments include n=3 and use ordered, not rotation-quotiented, pairs.

## originality

PASS

The cycle pair formula, including the antisymmetric-sector contribution, and the odd-cycle extremal count are distinct from the closest inspected results. The path result has the very same symmetric-sector denominator and leading mean, so these should not be presented as uniquely cycle-specific discoveries. No inspected source gives the full cyclic trace enumerator with its two factors and cycle pair limit law. This is a bounded finding about coverage, not a priority certificate.

## value

PASS

A natural cyclic benchmark for extension diversity: exact ordered-pair coefficients answer distance-tail counts at every size, parity determines the maximum multiplicity, and the explicit variance gives the fluctuation scale. The cyclic trace detects a sector absent from the path scalar series. This is a reusable exact invariant of a motivated graph family, not a numerical sequence check or a claim of a new general transfer method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
