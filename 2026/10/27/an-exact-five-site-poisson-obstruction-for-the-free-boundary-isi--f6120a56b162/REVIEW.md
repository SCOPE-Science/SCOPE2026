# Independent mathematical audit

## correctness

PASS

On the free nine-site graph, Poisson avoidance gives log Pr(plus set contained in B) equal to a constant plus the sum of intensities of subsets of B, so the fifth Möbius difference isolates this one nonempty atom. With the corners forced minus, an allowed arm costs three disagreements when the centre is minus and one extra disagreement when the centre is plus (its two corner edges replace its one centre disagreement). The centre-plus baseline costs four disagreements. Thus the two constrained polynomials are (1+t^3)^k and P_k; the log global normalization and the fourth difference of the centre-minus log term both vanish. Independent integer multiplication confirmed the degree-56 factorization; an exact rational Sturm chain for Q gave variations 14 and 13 at 0 and 1. Bisection located t*=0.6276872898128175508386809846705... and beta*=0.2328565913441155004710230108510.... The denominator is positive, the prefactor of Q is negative in (0,1), Q(0)=-1 and Q(1)=32, and t decreases with beta. The same endpoint factors give the stated -2 beta^4 and exp(-16 beta) asymptotics. Frozen replay references: verification/check_cross_intensity.py and verification/check_output.txt, inspected as evidence, not executed. The independent computation checks the algebra and root; the avoidance argument is the proof. A positive cross intensity at higher beta says nothing about all other intensities.

## originality

PASS

The checked sources cover finite avoidance inversion and several Ising or tree nonrepresentability mechanisms, but not the exact five-site intensity and sharp sign interval for this free cyclic graph. The passed claim is the single-atom calculation and its obstruction, not the general framework or an Ising representability phase diagram.

## value

PASS

The symmetric cross is a natural local branching test with its four corners outside the atom, not an arbitrary spin subset. The exact root shows where this particular local witness ceases to certify nonrepresentation; the small free planar box avoids assumptions about ordered phases or boundary fields. It is useful as an exact finite witness and benchmark even without a full atom census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
