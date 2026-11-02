# Independent mathematical audit

## correctness

PASS

For the exact source-type rational update with positive tau, zero reaction and coordinatewise mirrored Neumann ghosts, a fixed state satisfies the reflected five-point harmonic equation Delta_ref w=0 for w=u|G_hu|^{p−2}. Finite maximum principle on the connected reflected grid forces w constant; at a mirrored corner G_hu=0, hence w=0. With u>0 and p>2 this forces all centered differences to vanish, giving exactly four independent values on index-parity classes in 2D and two in 1D; every such state conversely has G_hu=0 and is fixed. Checkerboard edge energy counts 2N(N+1) opposite edges and equals 2(1+1/N)N^p|a−b|^p. For p>3 the map x→|x|^{p−2} has zero derivative at x=0, so DT_tau=identity at every parity-class state. An independent rational implementation verified 12 patterns and exact energy640 at N=p=4; the proof is unrestricted in grid/step/p and does not assume stability beyond Jacobian.

## originality

PASS

The primary 2026 source develops exactly the update and proves constant-equilibrium preservation (Theorem2) and positive solutions (Theorem1), but does not classify every strictly positive fixed point of its mirror-ghost specialization. Reiss 2014 explains generic centered-derivative odd-even decoupling; it is not claimed new. Here a source-specific product w=u|G_hu|^{p−2}, reflecting harmonicity and corner zero prove the entire positive stationary manifold, high edge-energy checkerboard family and identity-Jacobian regime. The full source and Reiss introduction were read; alternative boundary completions and broader centered-gradient literature remain historical risks.

## value

PASS

A positivity-preserving and constant-equilibrium-preserving diffusion scheme could still harbor high-gradient stationary artifacts. The exact classification shows every positive four-parity array is fixed at every step, and its worst checkerboard gradient energy diverges as h^(-p) while the continuum Neumann p-heat equilibrium is spatially constant. The p>3 identity Jacobian explains linear neutrality. This is a substantive discretization-fidelity and numerical-model-interpretation result for a natural scheme rather than a cheap isolated parity example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
