# Independent mathematical audit

## correctness

PASS

Both the frozen formula and the retained result are correct. After conditioning on, and rotating by, the angle of a labelled sample, independent uniform residual points become ordered uniform arguments and their differences have constant simplex density (n-1)!. The chord is 2 sin(pi x), even for a gap over a semicircle. The diagonal comes from the Beta(1,n-1) marginal and sin^2=(1-cos(2·))/2. At fixed two-gap sum z, integrating sin(pi x) sin(pi(z-x)) over x from 0 to z gives [sin(pi z)/pi-z cos(pi z)]/2; the two-gap density supplies (n-1)(n-2)(1-z)^(n-3). Replacing z(1-z)^(n-3) by the difference of successive powers gives exactly (s_n-r_n)/2. Counting ordered terms gives the asserted variance. The J expression follows from the integral exponential Taylor remainder with factor (ia)^(k+1)/k!. An independent symbolic replay, python3 /workspace/review_work/reproduce_4.py, verified the two small exact cases by direct simplex integration and the expansions of the power-sum covariances. The original higher-order variance is also correct: the cubic variance has coefficients (360,-6048,60552) at orders 5–7, the cubic–quintic covariance leads at 28800 n^-7, the quintic variance is O(n^-9), and the seventh-power remainder is O in L2 of n^-6, giving covariance with the centered cubic term O(n^-17/2). The revised files retain these coefficients only as a credited consequence, not as a separate finding. The frozen checker was inspected, not run.

## originality

PASS

PASS applies to the repaired finite-n formula only. The frozen originality claim cannot be accepted in full: the indexed earlier n=4 result is exact, and a distinct earlier record gives the actual perimeter Taylor polynomial, the exact mixed covariance for every two spacing powers, and the needed L2 bound. Inserting the cubic and quintic indices and expanding the earlier rising-factorial expressions directly gives both correction terms, even though they were not printed as two coefficients. The repair explicitly credits this coverage and removes the asymptotics and special cases from the contribution. The retained all-n evaluated nonpolynomial variance is not supplied by the compared finite-four formulas or the earlier truncated expansion.

## value

PASS

The surviving finite formula gives the exact sampling uncertainty of the standard chord-sum estimator of circle length, at sample sizes where a leading asymptotic is only approximate. It captures dependence between different chords and replaces a simplex double integral or a power-series resummation by a number of elementary finite sums independent of the number of gap pairs. The value is the arbitrary-n variance evaluation, not the covered asymptotic correction or rederiving one already known small case. No numerical conditioning guarantee is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
