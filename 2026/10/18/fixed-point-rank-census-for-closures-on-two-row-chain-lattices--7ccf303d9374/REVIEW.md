# Independent mathematical audit

## correctness

PASS

A fixed set of an extensive monotone idempotent map contains the top and is meet-closed by extensivity and monotonicity. Conversely the meet of its members above each input is its least member above that input and defines the unique such map. Let A and B record occupied lower and upper positions; n−1 must be in B. If A has maximum m, a meet with the lower point at m forces B∩[0,m]⊆A, and that condition suffices for every cross-row meet. For A empty the weight is t(1+t)^(n−1); otherwise columns below m are empty, lower-only or both, while the lower point at m and the top are compulsory, leaving n−1−m optional upper points. The resulting telescoping geometric sum gives (1+t+t²)^n−(1+t)^(n−1). At n=1 this is t+t²; all ranks up to n occur by taking just upper points, and larger ranks by adding an initial segment of lower points to the full upper row. Reversing both coordinates transports Bao et al.'s characteristic interior map to a closure and preserves fixed cardinality. The characteristic minimum is the target itself iff no proper subgroup transfers to it. Finally the normalized law is the difference of 3^n times the law of an iid ternary sum and 2^(n−1) times the fair-binomial law, divided by the difference of these weights. Its distance from the ternary sum is at most 2^(n−1)/(3^n−2^(n−1)); the latter sum has mean n and variance 2n/3, proving the stated CLT. The verification notes and script match their claimed finite scope and were inspected, not executed.

## originality

PASS

The supported result is the all-closure fixed-set-size refinement on this two-row lattice and its consequences, not the unrefined count or the characteristic-map correspondence. The closest rank-graded calculation on exactly the same lattice has a stricter map class and a different polynomial. Earlier general rectangular enumeration establishes the total but not the weighted distribution in the passages checked.

## value

PASS

The formula refines a natural established enumeration by the fixed-set size rather than merely rederiving the total. It answers every cardinality query, gives a transparent structural explanation in terms of the highest selected lower point, and yields a quantitatively accurate normal-law model. Under the transfer correspondence the coefficients count a concrete target statistic (no proper incoming transfer), not an artificial extra parameter of the proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
