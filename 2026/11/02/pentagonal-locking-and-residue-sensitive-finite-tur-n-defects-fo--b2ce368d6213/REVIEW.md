# Independent mathematical audit

## correctness

PASS

For N>=9 the five residue support points are distinct, and positive definiteness on Z/N is exactly discrete nonnegativity of 1+2a cos(theta_j)+2b cos(4theta_j) after real-even symmetrization. The explicit continuous feasible witness at a0=2(sqrt5−1)/5,b0=(sqrt5−1)/10 has polynomial factor (cos(theta)+cos(pi/5))^2 times a strictly positive quadratic, and therefore has only double zeros at ±4pi/5. When 5 divides N these nodes are sampled, yielding the bound 1+2(a+b)<=sqrt5; otherwise all sampled values are strictly positive and small scaling raises the objective above sqrt5. For fixed r=N mod5 nonzero and large N, consecutive grid nodes around 4pi/5 determine a unique (a_N,b_N); nonzero determinant, strictly positive curvature near double zero, and positivity away from zeros prove feasibility. Positive dual multipliers on these two active constraints prove global optimality and uniqueness among real-even optimizers. Expansion in h=2pi/N, u={2N/5}, gives excess 8pi²u(1−u)/(cos(pi/5)N²)+O(N^-3), hence the 48/25 and 32/25 residue coefficients. Source gives no unproved explicit onset for this asymptotic. Independently enumerated finite 2D LP Fourier-constraint vertex intersections for sixteen moduli N=9..31 including multiples and nonmultiples of five; direct all-grid checks matched the nearest-contact candidate and exact lock/excess cases.

## originality

PASS

The continuous integer-group five-point support optimum sqrt5 is ALREADY explicitly derived by Kolountzakis–Révész (2003 Example 3, support {0,±1,±4}); it is merely a premise, not the novelty. Their earlier discrete Carathéodory–Fejér framework optimizes a single harmonic coefficient, not the total supported mass a+b. The assessed new finite-cyclic contribution is exact divisibility locking, eventual two-contact real-even uniqueness and two residue-dependent 1/N² corrections.

## value

PASS

Discrete-versus-continuous positive-definite extremal problems are explicitly motivated in classical Turán/Carathéodory–Fejér work. The theorem determines precisely when a finite cyclic sample locks the known pentagonal optimum, shows strict excess otherwise, and quantifies two different arithmetic mesh-error constants with an optimizer uniqueness mechanism. These sharp all-residue statements are not a trivial restatement of the classical continuous value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
