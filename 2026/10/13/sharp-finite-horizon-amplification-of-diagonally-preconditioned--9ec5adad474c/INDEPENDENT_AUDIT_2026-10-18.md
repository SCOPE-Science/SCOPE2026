# Independent mathematical audit

## correctness

PASS

The oblique idempotent P=I−k(Dk)^T/(k^TDk) satisfies Pk=0. In the two-plane spanned by k and Dk its matrix is [[0,-tau/mu],[0,1]]; hence ||P||2=||Dk||/(k^TDk). For diagonal entries in [1,kappa], the elementary inequality lambda²≤(1+kappa)lambda−kappa bounds squared norm by ((1+kappa)mu−kappa)/mu²; exact maximum at mu=2kappa/(1+kappa) is C² with C=(kappa+1)/(2sqrt(kappa)). For every integer N≥1, submultiplicativity gives C^N. The explicit d=2 pair P1=C a b^T and P2=C b a^T with orthonormal *unit* a,b (not generally perpendicular) alternating realizes ||P1P2...||=C^N. Zero-target row evolution amplifies exactly C^N while the currently supplied key is annihilated. Independently checked the rank-one identities, projectors, and all powers N≤10 at kappa=2. The proof covers all d≥2 and arbitrary admissible switching; finite tests are corroborative.

## originality

PASS

The motivating OSDN algorithm paper defines the right-preconditioned delta-rule and a token-local erasure/residual result. It does not provide the exact worst-case all-length norm over independently switched admissible keys and diagonal metrics. Szyld and Kantorovich-type inequalities already give classical oblique-projection geometry and a one-step factor; novel content is simultaneous finite-horizon saturation via an alternating transpose pair and the sharp dynamical dichotomy. Related Resultary optimization and projection products address different operators or constrained iterate rules.

## value

PASS

A sharp worst-case finite-horizon growth factor for a normalized memory-erasure update directly measures the gap between local exact erasure and global stability, with an explicit two-key periodic witness and a sharp kappa=1 versus kappa>1 dichotomy. This is a motivated, algorithm-specific matrix-product invariant useful when assessing whether token-wise residual tests imply safe recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
