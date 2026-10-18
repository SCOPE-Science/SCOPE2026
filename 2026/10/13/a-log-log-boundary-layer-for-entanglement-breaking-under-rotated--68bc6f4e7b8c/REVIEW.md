# Independent mathematical audit

## correctness

PASS

The stated 3x3 Bloch map decomposes into A (2x2, determinant lambda, trace t=(1+lambda)cos theta) and scalar lambda. Cayley–Hamilton yields the r_n,v_n recurrences. For det A^n>0, its trace norm squared equals tr(A^n)^2 + [(A^n)12−(A^n)21]^2; adding lambda^n and applying the established unital-qubit nuclear-norm ≤1 criterion proves the exact iff. Schur stability follows from 1±t+lambda>0 for interior theta; at endpoints the norm is 1+2lambda^n>1. Perturbing the two A eigenvalues as 1−a_lambda theta² and lambda(1+a_lambda theta²) with n=O(log 1/theta), and controlling the theta² and n²theta⁴ error terms, yields defect 2lambda^n−a_lambda n theta²+o(theta² log(1/theta)); monotonicity from ||M||op≤1 converts this to the index O(1) bracket. Independently coded direct 3x3 SVD and scalar recurrences agreed to 1e−8 in 1659 distinct (lambda,theta,n) cases, including endpoint and near-alignment cases.

## originality

PASS

The universal qubit EB nuclear-norm condition and qualitative eventual-breaking classification are old; the direct recurrence and sharp log-log boundary layer are the proposed new contribution. Lami–Giovannetti establishes the test, Cuevas et al use rotated phase damping with two use/filter questions, and Bhat–Dey–Saha arXiv:2609.24168 gives general qualitative eventually-EB characterization but not the fixed-family singular-angle asymptotic in examined full PDF. Mathematically equivalent two-by-two spectral asymptotics could appear in unindexed physical literature.

## value

PASS

A tiny misalignment changes a dephasing-preserved qubit channel from never finite-time EB to eventually EB. The logarithmically divergent index, its negative loglog correction and nontrivial signed transition profile quantify an operationally meaningful nonuniform limit beyond merely checking one quantum-channel iterate; limited to direct unfiltered one-qubit channels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
