# Independent mathematical audit

## correctness

PASS

Fourier decimation contributes q^(−1) at the transform level, and the input alias norm contributes q^(−1) after squaring and integrating; their ratio gives A_q=q^(−1) min σ_min(V)^2. For an oriented gap d, t(z_j−z_(j+d))=t exp(−i(φ+2πj)/q)(1−exp(−2πid/q)), with indices modulo q. Varying the fiber and j together traverses all chord directions (one fixed pair over a single fiber period need not). This yields exactly the listed resonance times, with only finitely many singular fibers at any t>0. For small t, the unitary column DFT gives degree-r columns divisible by t^r with removable unimodular phases; the residual matrix converges uniformly to the polynomial evaluation matrix sqrt(q) k^r/r!. Its last inverse row is the normalized finite-difference row, with squared norm binom(2q−2,q−1)/q. This proves the least-singular-value limit uniformly and the stated sharp frame coefficient. At a positive resonance, three coincident nodes would require three unit-circle points with equal real part, which is impossible. Each possible pair gap is bounded below by a constant times |t−t0| from radial distance to its exponential period, uniformly near that collision. Every inverse interpolation denominator loses at most one factor, even for simultaneous disjoint pairs; a difference of colliding columns supplies the opposite bound. For q=2 the determinant expansion at the collision is 4e^(−2t0)(δ²+t0²u²)+o(δ²+u²) for its squared modulus. Any minimizing phase approaches the collision by compactness, so this uniform relative expansion gives a lower limit matching the fixed collision phase; dividing by the large singular value squared 2(1+e^(−2t0)) and by q=2 yields the claimed constant. The source's reported numerical checks were inspected, not rerun, and are not proof of the global statements.

## originality

PASS

The direct-integral frame criterion and Vandermonde mechanism are established. The closest primary theorem applies to the present channels by Shannon identification, but does not compute the explicit exceptional-time set, the binomial coefficient, or the positive-resonance asymptotics. The closest indexed records have different operators or perturbations. The pass is for the explicit Poisson classification and sharp lower-bound laws, not for generic fiberization.

## value

PASS

A canonical nonselfadjoint shift semigroup at critical spatial/temporal density is a natural sampling model. The exact resonance set separates unique recovery from stable recovery; the sharp constants and order quantify the conditioning close to physically distinct small-time and positive-time degeneracies. In higher dimensions of the fiber the comparison remains valid even when disjoint pairs collide together. These are usable stability estimates rather than a restatement of determinant nonvanishing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
