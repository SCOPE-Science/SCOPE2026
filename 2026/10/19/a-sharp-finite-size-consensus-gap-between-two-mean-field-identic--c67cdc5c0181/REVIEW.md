# Independent mathematical audit

## correctness

PASS

With replacement from the other N−1 vertices, the two interior jump rates are positive, and a finite path to either endpoint gives almost-sure absorption. Dividing the generator drift by N and taking N large gives the stated common drift, because x+(1−x)=1 and x²−(1−x)²=2x−1. The harmonic equation gives consecutive increments in ratio ((N−j)/j)^(q−1); multiplying telescopes to binomial powers. The binomial theorem and Vandermonde normalize the q=2 and q=3 laws exactly. For m=N−1≥2 the squared-binomial-to-binomial mass ratio is strictly increasing up to the central set and then strictly decreasing, except for the possible central tie. There are negative tails and a positive central part. For m odd the left half has zero total difference, and for m even the left half without the central atom has difference minus half that atom's positive difference; this proves strict negativity for all prefixes strictly below the midpoint and reflection proves the other sign. On the upper half the successive difference crosses zero when binom(m,k) decreases through binom(2m,m)/2^m; equality yields the adjacent tie and the stated index test. Compact-uniform Stirling expansions and Chebyshev truncation using variances m/4 and m²/[4(2m−1)] give the two moving-threshold Gaussian limits. The local ratio tends to √2 exp(−2s²), and the monotone discrete crossing is bracketed by any two positive offsets straddling √log(2)/2. Substituting in the limiting distribution difference yields the stated 0.08303203749… limit. Nonvanishing in the window means separation at nonzero fixed scaled offsets and a positive limiting maximum, not a uniform positive lower bound all the way down to the midpoint. Independent safe-integer recurrence comparisons covered all 204 counts for N=3,…,19, including the stated N=5 example; verify_exit.py was inspected, not executed, and its frozen reported finite checks are not the proof.

## originality

PASS

Credit established coverage of the common drift and of the two exact fixation CDFs under specialization of the later general catalogue formula. The supported distinct contribution is the strict same-drift finite-N comparison, exact maximizing-index characterization and sharp limiting maximal separation for these two panels. The checked earlier diffusion treatments and the later binary fixation formula do not supply that comparison. Chronology is not used as a substitute for comparing the statements.

## value

PASS

The result answers an identifiable modeling question: two rules indistinguishable at the deterministic drift level can yield a sizeable, precisely quantified difference in consensus predictions. The effect does not disappear in the maximal critical window, even though the fixed-density predictions agree. The strict finite comparison, exact optimizer test and limiting location and size make the example usable as a benchmark; displaying two standard CDFs alone would not establish that value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
