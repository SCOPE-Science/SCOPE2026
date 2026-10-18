# Independent mathematical audit

## correctness

PASS

Dihedral symmetry reduces difference vector to d(t)=(1-t)v0+t*v1, 0<=t<=1/2. Chord endpoints are in P10∩(P10-d). With n=(-d2,d1), maximize n·x/h_P(n). On [0,τ] the active pair is original u3 and shifted u1; on [τ,1/2] it is original u3 and shifted u2, τ=(3-sqrt5)/2. Explicit nonnegative normal decompositions certify optimality. Independently reconstructed both intersections in SymPy and verified all 40 endpoint half-space residuals are EXACT nonnegative algebraic numbers per branch; because residuals are affine in t, this verifies continuum feasibility. Numeric LP checks at 6 independent t values agree with stated quadratics to <5e-16. The first ratio is convex with equal maxima at 0,τ; second decreases on [τ,1/2], yielding m=(7-3sqrt5)/2 and exactly those dihedral equality directions.

## originality

PASS

Best-of-knowledge exact benchmark for the decagon singled out by original conjecture. Later stronger SCOPE all-family record is explicitly compared and chronologically later, not prior.

## value

PASS

The decagon is the explicit candidate extremal body in Dalla–Larman–Mani-Levitska–Zong; exact M-curvature and equality-direction classification provide a natural analytic benchmark for the unresolved maximum problem, not an arbitrary invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
