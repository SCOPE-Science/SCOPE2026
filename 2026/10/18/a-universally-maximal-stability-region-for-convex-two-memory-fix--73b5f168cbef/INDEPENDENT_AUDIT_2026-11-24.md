# Independent mathematical audit

## correctness

PASS

For the scalar characteristic p(z)=z²−a((1−q)z+q), write R=|a|² and x=Re a. The monic quadratic Schur–Cohn inequalities become q²R<1 and F=(1−q²R)²−(1−q)²|a+qR|²>0. For R<1 a putative |z|≥1 contradicts |z|²≤|a||z|; at R=1, a=1 has root 1 for every weight, while F(1/3)=8(1−x)/27>0 at the other points. At R>1 a stable q gives positive F somewhere on [0,1/sqrt(R)], whose endpoints are nonpositive. The derivative is 2R(3q−1)[x−1+q(R−x)]. At the other candidate q_0, the relation q_0 R=1−(1−q_0)x yields 1−q_0²R=(1−q_0)(1+q_0x) and Re(a+q_0R)=1+q_0x, hence F(q_0)=−(1−q_0)²(R−x²)≤0, including real a. Therefore a positive interior maximum is at 1/3 and satisfies the strict product constraint. At that q, 27F=27−18R−8Rx−R², bounded above at fixed t=sqrt(R) by −(t−3)^3(t+1), so F>0 forces R<9. For a=−t the real quadratic test gives tq<1 and t(1−2q)<1; the smaller effective upper bound equals 3 only at q=1/3, furnishing a strict inclusion witness for every other q. For real a≥1, p(1)≤0 gives a real root ≥1; the imaginary boundary gives R=6sqrt(3)−9 and the endpoint a=−3 has a double root −1. Triangularizing A gives the quadratic factors of the block companion even for defective matrices; spectral radius below one is exactly exponential stability for all initial pairs. The frozen check.py was inspected, not executed; recorded grid and rational checks are diagnostics, not the universal complex proof.

## originality

PASS

The strongest actual comparators give the real negative frontier or equal-weight regions, not full complex containment by a single fixed unequal weight. The assessment credits the older real result and classical Schur machinery; the distinct content is the universal complex set-inclusion optimum with an exact boundary. The comparison is bounded, not a general priority claim.

## value

PASS

A uniform dominance theorem is stronger than an improved real margin or a per-matrix tuning rule: one constant convex rule preserves every stability guarantee attainable by any constant two-lag weight, including nonreal eigenvalues of nonnormal finite matrices. The exact strict Schur boundary gives a direct admissibility test with no claim about transient amplification, nonlinear maps, or fastest contraction. This is a natural complete classification and a useful parameter choice, not simply a restatement of a quadratic root test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
