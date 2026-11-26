# Independent mathematical audit

## correctness

PASS

For unit edge weights the constant eigenvalue is 0 and all orthogonal modes have Laplacian eigenvalue n. Thus the extrapolate is J/n+R(nh)(I−J/n), with R(x)=8/(x+2)²−1/(x+1). It fixes constants, and 1−R(x)=x(x²+6x+4)/[(x+2)²(x+1)] is strictly positive for x>0. Clearing the positive denominator of its common diagonal gives the asserted cubic H_n. Where R≥0 this diagonal is strictly positive; where R<0 the numerator 1+(n−1)R is decreasing in n. At n=28 the identity H_28=x(x−11)²−5x+112 proves strict positivity on [0,22] and on [22,∞) separately. For all n≥29, H_n(0)>0, H_n(12)=2640−92n<0 and H_n tends to +∞. Descartes' count of at most two positive roots with multiplicity gives exactly one simple root on each side of 12, and no other positive zeros. This proves the entire interval statement, including its endpoints and the identity at h=0; outside the interval the nonnegative row-sum-one matrix is stochastic, and a negative diagonal inside makes a coordinate impulse fail. Independent replay `python3 /workspace/independent_reproduction.py 1` produced exact diagonals 4/4459 at (n,x)=(28,12), −1/2639 at (29,12), and 47/10527 at (29,20), with the predicted off-diagonal signs, and recovered the two n=29 roots 10.4352065911559987… and 13.3946905220461563…. These finite checks supplement the complete algebraic proof.

## originality

PASS

The supported contribution is the complete-graph full-matrix cutoff and reentry for the given rational stepper, not Richardson extrapolation or its scalar sign change. There is actual material overlap with a later public weighted-graph diagonal theorem: it covers the full diagonal portion, even the same cubic on K_n. This is credited but does not establish earlier coverage or furnish a statement about all entries. Earlier directly compared results concern the scalar mode, a pure-birth chain, or the method without the graph conclusion.

## value

PASS

Complete graphs are a canonical test of diffusion time steppers with one common nonconstant decay scale. Exact state positivity, unlike scalar stability, matters for stochastic averaging and nonnegative data. The sharp dimension obstruction and bounded negative window tell users precisely when sign is lost and when it recovers; neither feature is explained by the familiar scalar sign change alone. The classification covers every step and graph order within its chosen family, not an arbitrarily selected example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
