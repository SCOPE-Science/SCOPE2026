# Independent mathematical audit

## correctness

PASS

Put x=ah/2, y=bh and z=y(1−x). Multiplication gives the lower row (z,1−z) and the upper row ((1−x)(1−x+xy), x(2−x−z)). The factors each preserve the constant column, so applying the endpoint to the two coordinate probability rows tests precisely entrywise nonnegativity. For h>0 the lower-left entry requires x≤1; h=0 gives the identity. With x≤1 the upper-left entry is nonnegative, and z≤1 both is necessary from the lower-right entry and gives x(2−x−z)≥x(1−x)≥0. Maximizing z=bh(1−ah/2) on [0,2/a] gives b/(2a) at h=1/a. For b>2a its two level-one roots are (1±√(1−2a/b))/a, and exactly their intervening open interval fails the test. At b=2a the coincident root does not create a gap; h=2/a gives both rows equal to (0,1). For a=1,b=4, h=1/2 has lower-right entry −1/2, whereas h=19/10 has both rows nonnegative and the middle factor has lower-right entry −33/5. The expansion through h² contains A²/4+(AB+BA)/2 rather than (A+B)²/2; this is first-order forward-Euler splitting, not second-order Strang with exact factors.

## originality

PASS

The compared stronger positivity statements and prior reentrance witnesses concern different maps. No checked source supplies the exact same Euler-factor endpoint criterion or an implication that determines its two-state slice. The assessment concerns the fixed palindromic Euler map only, not priority for reentrant endpoint positivity in general.

## value

PASS

A standard-looking palindromic split of the minimal irreducible Markov generator gives an exact, parameter-open counterexample to downward closure of endpoint admissibility in h. This is stronger than finding a single lucky endpoint or recomputing a stage CFL: it identifies when the second component exists, its full width and its absorbing upper endpoint even though one step late in that component can have a negative intermediate factor. This example separates stage positivity, endpoint positivity and accuracy, within a class not covered by the prior two-state obstruction for RKL2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
