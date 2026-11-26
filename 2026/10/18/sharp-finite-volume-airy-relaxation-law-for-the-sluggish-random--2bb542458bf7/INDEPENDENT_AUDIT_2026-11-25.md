# Independent mathematical audit

## correctness

PASS

Detailed balance gives unit edge conductances against the masses |k|+2 and normalization L²+5L+2. The first excited Jacobi mode has one sign change; reflection and simplicity rule out an even mode. Its odd restriction gives the stated half-chain quotient, including the single incident edge at L. With h=1/L the scaled gap is the stiffness divided by the right-endpoint mass sum. On each linear cell the L¹ norm of (xf²)'' is bounded in aggregate by a constant times the stiffness, so trapezoidal quadrature has a uniform O(h²) mass remainder relative to stiffness. The order-h mass consists of the endpoint trace f(1)²/2 and the bulk 2∫f², with both signs positive. Differentiation of the simple continuum eigenvalue gives −μ b₁(u)/b₀(u); interpolation and the eigenfunction weak identity bound the discrete eigenvalue error by O(h²) at the scaled level, giving O(L⁻⁵) after rescaling. The stationary limit follows by a Riemann sum; the relaxation parameter is the smallest positive eigenvalue of I−P, equivalently the Poissonized rate. Independent replay: python -B /workspace/review_replay.py 3, using a power-series solution rather than Airy evaluation and half-chain eigenvalues at L=16,64,256,1024. The numerical checks corroborate, not prove, the asymptotic.

## originality

PASS

Best-of-knowledge pass for the two-term rejected-boundary box gap, specifically the lattice-sensitive L⁻⁴ term. The walk and its unconfined Airy behavior are known; neither is credited as new. The methods and source comparisons do not establish exhaustive priority.

## value

PASS

The finite-box relaxation time is a natural measurable invariant of an existing subdiffusive walk. Its exact first correction distinguishes rejected endpoints and the microscopic waiting law from continuum models with the same spreading exponent and leading scale. The coefficient is useful as a finite-size benchmark, not merely another finite numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
