# Independent mathematical audit

## correctness

PASS

The local reset clock kills each backward voter lineage at rate r; a union bound on survival back to the start gives convergence for any finite spin set and uniqueness conditional on the template. For the mixed and two-spin functions the stationary generators give (r−Δ/2)H=rC and (2r−Δ)G=2rH off the origin, with G_0=1. I independently solved the mixed recurrence for c≠q in the basis c^n,q^n and applied the odd-reflection Green kernel on the positive half-line: G_1=q+(1−q)^2 sum_{n≥1} q^(n−1)H_n. The convergent limit extends to c=q. Symbolic reduction of this independent expression (/workspace/audit_replay_5.py) gives exactly the asserted rational function, both derivatives and all three specializations c=−1,0,1. For c<0 the q-derivative is positive by the displayed positive-coefficient grouping and 7q²−3q+1>0, and the endpoints are c and 1. The c-derivative is positive on the physical domain by bounding its numerator bracket separately for 3q²≥1 and 3q²<1. Since r decreases with q, this proves a single crossing and the asserted ordering. For c≥0 coalescence before either reset has positive probability and every template pair moment is nonnegative. The cubic root gives r*=1.446156936667017074…; the implicit equation near (q,c)=(0,0) gives q=−c/2+O(c²) and the claimed asymptotic. Uniqueness of the negative c boundary refers to admissible correlations in [−1,0), not to roots of the polynomial over all real c.

## originality

PASS

Grange's prior work uses the same local frozen-memory protocol and supplies the kinetic framework and the independent-template stationary result. The inspected exact pair solution assumes independent spins, not the full exponential covariance family, and neither its solution nor the related global resetting models imply the strict sign-crossing theorem. The original content supported here is the evaluated correlated-template law and its unique ordered thresholds, not the resetting protocol or Green-kernel machinery.

## value

PASS

The sign reversal quantifies when local resetting overcomes voter alignment for a natural family of spatially anticorrelated memories. The strict ordered boundaries, their sharp lower envelope and its exact checkerboard witness provide a quantitative benchmark more informative than the known i.i.d. correlation. It is a local annealed effect, not a thermodynamic phase transition or a quenched sign theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
