# Independent mathematical audit

## correctness

PASS

For all 0<t<1 in the full-line integer-grid continuous piecewise-affine L2 spline space, inserting t adds precisely one tent direction h_t. Orthogonalizing gives nonzero g_t=h_t−Ph_t and the exact rank-one difference Q_t f=<f,g_t>g_t/||g_t||_2^2. The integer-hat Gram matrix has diagonal 2/3 and off-diagonals 1/6; its inverse sqrt(3)(−q)^|j−k| with q=2−sqrt(3) satisfies both diagonal normalization and the off-diagonal recurrence and is bounded on ell2. Thus the coefficients c0,c1 and their two alternating geometric tails follow. The new nodal value d=1/2+(sqrt(3)−1)t(1−t) is strictly larger than |c_j| at old knots, so ||g_t||_infinity=d. By orthogonality E=||g_t||_2^2=[sqrt(3)+2(sqrt(3)−1)t(1−t)]/12>0. Integrating all infinite alternating tails as a geometric series plus the two sign-changing cell segments yields B=||g_t||_1, exactly equation (8). Symmetry of the kernel and an L∞ sign witness give both endpoint operator norms dB/E; L1 equality follows by duality/approximating a concentration at its maximum. Fresh independent exact SymPy algebra verifies reduction to the stated rational R(u), with u=t(1−t), and the identity R'(u)=3J(u)/H(u)^2; every coefficient of H,J is positive at sqrt(3), so R strictly increases over [0,1/4], with endpoint 2 and unique t=1/2 maximum 27/26+45sqrt(3)/52=2.537351660396... . A separately written SciPy 101-hat finite-section Gram system with independent piecewise absolute integrals agrees with exact formulas to <1e−12 for t=.001,.137,.5,.731,.999. These experiments validate computed identities, not replace the proof for the infinite line.

## originality

PASS

Best-of-knowledge original narrow result: the stated continuous-position rank-one refinement-increment norm R(t(1-t)) and strict unique midpoint maximum differ from published whole-projector Lebesgue constants, periodic projection norms, and inverse-Gram decay inequalities. The key equivalence to an individual normalized Franklin/Strömberg wavelet projection was explicitly checked, not treated as a different object. In the relevant accessible primary mathematical sections no dominating theorem or explicit formula giving this exact one-step norm and monotonicity was found. Historical priority is not certified; the most plausible 2003 Strömberg-wavelet article remained inaccessible in full, and was not represented as NOT_COVERING.

## value

PASS

The operator Q_t isolates the new L2 spline component released by a single interior knot; its norm is a direct worst-case amplification measure relevant to stability of adaptive piecewise-linear least-squares refinement. Optimizing knot location over an entire continuum is intrinsic to the object, not an arbitrary finite slice. The exact closed R(t(1−t)), strict midpoint extremizer, and precise t→0/1 limit provide sharp structural information unavailable from bounds for either whole projection alone. The result is a mathematically complete narrow stability classification; no broad adaptive algorithm, all-mesh or high-degree extension is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
