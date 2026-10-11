# Independent mathematical audit

## correctness

PASS

Affine normalization reduces the problem to the unit ball \(D\subseteq c+TD\). For a unit normal \(u\), let \(s=\|T^{\mathsf T}u\|\). Nesting gives the support inequality \(c\cdot u+s\ge1\). If the unit-ball cap of fraction \(\alpha\le1/2\) has threshold \(t\in[0,1]\), then the same halfspace cuts the outer ellipsoid at normalized threshold \((t-c\cdot u)/s\). For \(c_0=c\cdot u\ge0\), \(c_0+ts-t=t(c_0+s-1)+(1-t)c_0\ge0\), so \((t-c_0)/s\le t\). Monotonicity of the rotationally symmetric cap function gives the desired outer fraction. This argument is uniform in \(t\), hence in all \(\alpha\), and handles thresholds outside the unit interval by the evident full/empty-cap convention. A fresh exact-rational stress check independently verified the scalar implication; the frozen verifier was also read.

## originality

PASS

Fruchard--Magazinov prove the analogous dominance theorem for arbitrary nested planar convex bodies and explicitly leave the nonplanar problem open. Chevallier--Fruchard--Vîlcu develop the planar \(\alpha\)-section framework, while Kincses' arbitrary-dimensional theorem assumes a well-separated family and therefore does not apply to nested bodies. Resultary searches found the assigned ellipsoid theorem but no earlier all-dimensional nested-ellipsoid specialization. The proof is elementary, but it supplies a genuine special-class resolution in the higher-dimensional direction and the stronger simultaneous-in-\(\alpha\) normal family.

## value

PASS

The theorem resolves a natural, explicitly open higher-dimensional section-dominance question on a central geometric class and strengthens it by finding a fixed family of parallel cuts valid for every lower-half volume fraction. Its short proof reflects strong ellipsoidal structure rather than an arbitrary exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
