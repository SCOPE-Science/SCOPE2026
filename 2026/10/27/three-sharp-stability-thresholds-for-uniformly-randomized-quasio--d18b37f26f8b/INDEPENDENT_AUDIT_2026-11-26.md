# Independent mathematical audit

## correctness

PASS

Pythagoras gives |y−cx|≤sr|x| on the target line. Uniform arclength is therefore multiplication by c+sU with U uniform on [−r,r], for either sign of x; independence across half-steps gives two independent factors per sweep. The largest magnitude c+sr is attained and can be chosen at every step, giving sharp adversarial robustness and a constant nonzero sweep at its boundary. Taking the p-th absolute moment factors exactly, and the stated antiderivative integrates over intervals crossing zero as well. For p=2 the one-step factor is c²+s²r²/3, hence r=√3 is critical and does not give decay in mean square. For r>0 an exact zero has probability zero; the logs have finite second moment and positive variance. Apply the SLLN and, at zero mean, the LIL to the iid sums of two log increments per sweep: the critical limsup and liminf are +∞ and −∞ in log magnitude. When c>0 the mean is negative through r=c/s by Jensen and integration, and beyond that point its derivative has sign 1−t artanh(t) for t=c/(sr), changing from negative to positive once. The mean diverges to +∞, so the positive zero is unique. When c=0 the mean is log r−1 and the cutoff is e; deterministic r=0 contracts, with immediate absorption for perpendicular lines. Strict Jensen at r=√3 makes the pathwise cutoff larger, and r_rob=s/(1+c)≤1. The frozen checker was inspected, not run; its finite rational and numerical tests do not prove the infinite-time thresholds. The log gain can have unbounded support below, despite the verifier prose: the proof correctly uses finite variance, not boundedness.

## originality

PASS

Credit the deterministic admissibility and robust contraction to the prior QAP theory rather than counting them as a new result. The supported distinct claim is the stability classification for independent uniform sampling over the full feasible interval: exact angle-independent second-moment boundary, unique angle-dependent almost-sure boundary with the critical case classified, and their strict separation from one another and from worst-case selection. Standard scalar random-product results supply moment factorization and the log-drift criterion, not the particular projection law, uniqueness or separation of its cutoffs. No inspected applicable prior statement supplies the combined random classification.

## value

PASS

A standard admissibility tolerance is often interpreted as a single notion of numerical safety. On the same simple geometry, the exact thresholds show that all-selection contraction, moment stability and almost-sure decay are sharply different: a tolerance can yield almost-sure decay while the second moment grows. The comparison is useful precisely because the sampling rule is specified and the critical equalities are settled, without making claims for other random solvers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
