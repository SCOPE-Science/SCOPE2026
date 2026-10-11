# Review of A logarithmic-moment calculus for radial Lelong averages

## Correctness

PASS. The proof reduces every radial average to a probability average of the spherical mean on logarithmic radii. The spherical mean
\[
\phi(x)=S(u,e^x)
\]
is increasing and convex, with asymptotic slope
\[
\nu(u,0)
\]
at \(-\infty\). Hence every fixed backward increment converges to the slope times its length.

Convexity also supplies the uniform majorant
\[
0\le\phi(x)-\phi(x-s)\le Cs.
\]
The finite logarithmic moment is exactly the integrability condition for this majorant. Dominated convergence therefore proves the formula for arbitrary radial probability laws, and the mollifier and uniform-ball cases follow by exact pushforward identities.

## Originality

PASS. The September 2026 primary paper proves an exact spherical-solid formula and uses radial regularizations only to characterize the zero-Lelong case. It explicitly writes the mollified value as a weighted average of spherical means but does not retain the nonzero slope to compute the limiting coefficient.

Claim-specific searches for exact mollifier gaps, logarithmic radius moments, pairwise radial averaging formulas, and the source identifier found no covering statement. The closest earlier VMO paper gives the classical slope characterization and the zero-Lelong equivalence but contains no mollifier, regularization, convolution, or spherical-mean formula matching the claim.

The result is therefore a genuine extension of the source's main additive identity from one distinguished averaging law to the full radial probability class with finite logarithmic moment.

## Value

PASS. The coefficient
\[
1/(2n)
\]
in the fresh source is presented as an exact new invariant of the sphere-versus-ball comparison. The accepted result explains that coefficient structurally as a logarithmic radius moment and shows that every radial smoothing operator has its own exact coefficient.

This yields a kernel-independent calculus for comparing radial regularizations and an exact recovery of the Lelong number from any smooth radial mollifier. The extension is natural for pluripotential regularization and is broader than a routine substitution into the sphere-solid formula.

Same-model review: passed. Independent audit: not yet performed.
