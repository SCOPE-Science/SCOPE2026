# Independent mathematical audit

## correctness

PASS

For h>0 the two stages span the plane, since Aq and q are independent by A^2=-kappa^2 I; the correction is along Qy. In energy coordinates the midpoint predictor is a scaled rotation with squared gain D=1+kappa^4 h^4/4. It is invertible and preserves uniform angular law. With r=kappa^2 and s the energy fraction on the second axis, completing the square on the prescribed line gives minimum energy relative to the target D(r-1)^2 s(1-s)/(1+(r^2-1)s). The parabola is strictly convex, so the criterion is inclusive. The phase factor is maximized at s=1/(r+1), giving the stated threshold and four double-root angles there. Independently, writing t=|tan(predictor angle)|, failure is r^2 t^4+(1+r^2-H)t^2+1<0. For H>(r+1)^2 the positive boundary values have product 1/r and difference sqrt(H-(r+1)^2)/r. Thus their angular width gives p_fail=(2/pi) arctan(sqrt(H-(r+1)^2)/(r+1)), equivalent to the stated arcsine law. Expansion at zero and infinity verifies both coefficients (H=D(r-1)^2). Axis directions remain solvable; isotropy makes every correction radial. The exact witness has minimum 9801/1945>2, and the frozen recorded output and script provide bounded corroboration, not proof for the continuum.

## originality

PASS

The original contribution supported here is the sharp one-step explicit-midpoint failure profile for the specified anisotropic oscillator: finite cutoff, partial-phase failure above it, and sharp distribution and limits. The correction method and the classical worst-phase inequality are prior mathematics; no priority is claimed for either. The strongest inspected neighbors do not establish this profile.

## value

PASS

Convexity and even a full stage span may suggest that an energy correction is always available, but the prescribed line can miss the target ellipse. This natural test problem quantifies exactly where a solver needs a fallback or step restriction; it distinguishes universal safety from typical initial-phase failure and measures the onset and remaining successes. It is not just an arbitrary failed input or a recapitulation of local solvability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
