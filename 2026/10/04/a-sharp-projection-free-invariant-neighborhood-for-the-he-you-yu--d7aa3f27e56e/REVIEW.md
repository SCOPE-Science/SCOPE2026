# Independent mathematical audit

## correctness

PASS

Centering at the saddle gives the projection-free matrix \(M=\begin{pmatrix}1&\tau\\-\sigma&1-\tau\sigma\end{pmatrix}\). Direct multiplication verifies \(M^{\mathsf T}QM=Q\) for \(Q=\begin{pmatrix}\sigma&\tau\sigma/2\\\tau\sigma/2&\tau\end{pmatrix}\), whose determinant is \(\tau\sigma(1-\tau\sigma/4)>0\) exactly when \(\tau\sigma<4\). Completing squares on \(u=-1\) and \(v=-1\) gives boundary minima \(\sigma(1-\tau\sigma/4)\) and \(\tau(1-\tau\sigma/4)\), so the stated \(c_*\) is exactly the largest strict invariant-energy sublevel contained in the positive orthant. Since the linear candidate preserves energy, induction proves projections never activate. At \(\tau\sigma=4\sin^2(\pi/m)\), the characteristic roots are the primitive pair \(e^{\pm2\pi i/m}\), so every nonzero orbit in the sublevel has exact period \(m\). The inspected checker independently reproduces these identities; finite resonant samples are corroboration only.

## originality

PASS

The 2014 primary source was read through its full counterexample section: it gives the same projected recurrence, the exact six-cycle for \(r=s=1\), and finite 1000-iteration tiny-step tests, but not the sharp invariant-energy sublevel or the all-period resonance family. Bailey–Gidel–Piliouras was read through its exact conserved-energy theorem: it covers the unconstrained alternating bilinear dynamics and its one-dimensional ellipses, so the invariant itself is prior art. The surviving contribution is the exact largest ellipse sublevel guaranteed never to hit either nonnegativity projection, plus the resulting exact constrained \(m\)-cycles for arbitrarily small steps. Resultary search found no earlier finding implying those constrained statements.

## value

PASS

The result resolves the mechanism behind a canonical published tiny-step nonconvergence example: it gives the exact largest local neighborhood on which projection effects disappear and upgrades finite numerical warnings to explicit exact cycles with arbitrarily small steps. This is a motivated sharp boundary statement, not merely a restatement of the known unconstrained invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
