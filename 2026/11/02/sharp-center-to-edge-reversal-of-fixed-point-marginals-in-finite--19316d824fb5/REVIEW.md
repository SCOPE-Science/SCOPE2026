# Independent mathematical audit

## correctness

PASS

Put a=i-1, b=n-i. Inserting a forced fixed point into a permutation of a+b labels introduces one inversion for each of the J large values on the left and the J small values on the right, so it tilts the reference Mallows weight by q^(2J); the normalization ratio is 1/[n]_q. (The actual deletion pushforward conditional on a fixed point is tilted, not plain Mallows; Step 1's reference weight must be read before the tilt, as in Step 2.) For cut count j, choosing the small and large labels on the left gives two Gaussian binomials for within-type inversions across the cut, j^2 large-left/small-right cross inversions, and two factorial weights for the internal orders. The sum of these weights over j is the total permutation weight, establishing normalization and the diagonal formula. For b>=a+2, the new/old mass ratio on j=0,...,a is a positive constant times [b-j]_q/[a+1-j]_q = 1+[b-a-1]_q q^t/[t]_q, t=a+1-j. Because [t+1]_q=1+q[t]_q, q^t/[t]_q strictly decreases in t. The ratio is increasing, with new positive mass at a+1, so the difference of the masses has a single negative-to-positive crossing and gives stochastic dominance with a strict upper tail, including when a=0. Applying q^(2j) reverses the comparison below q=1 and gives strict increase above it. At q=1 the function is constant and all marginals are 1/n. Double reversal preserves inversion count and exchanges mirrored positions, including the even central tie. At n=2 the strict comparison has empty range. The frozen exact finite verification is supportive; its source was inspected, not executed.

## originality

PASS

The Gaussian cut-crossing distribution is covered by earlier exact finite height/rectangle formulas. They also give access to individual point probabilities and are antecedents to the diagonal representation. The credited result is the strict balancing comparison of the cut laws combined with the finite-n reversal of the fixed-point profile, for every real q>0, not priority for the cut law or generic one-site enumeration. The closest available finite formulas do not state the balancing inequality or another inequality implying this reversal by direct specialization.

## value

PASS

The finite diagonal of the mean permutation matrix is a natural location-sensitive observable. The exact strict reversal distinguishes edge and center effects that a mean fixed-point count, a stationary approximation, or symmetry cannot reveal. The ordered cut law is a structural explanation valid at all sizes and for every positive q, even when the fixed-point signal itself is flat at q=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
