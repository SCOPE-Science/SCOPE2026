# Review

## Correctness

PASS. The proof reconstructs every symmetric unimodal integer law as a convex
mixture of centered discrete uniforms. Their variance and mean absolute
deviation are exactly
\[
v_m=\frac{m(m+1)}3,
\qquad
d_m=\frac{m(m+1)}{2m+1},
\]
and the grid points lie on the strictly concave curve
\[
d=\frac{3v}{\sqrt{12v+1}}.
\]
The piecewise-linear interpolation through consecutive grid points is therefore
concave, so Jensen gives the exact upper envelope. Strict slope decrease gives
the equality classification. A point-mass/large-uniform mixture gives a
same-variance sequence with mean absolute deviation tending to zero, and convex
mixing fills the complete open-closed interval.

The phase correction is derived from an exact finite formula before expansion;
it is not inferred from numerical fits.

## Originality

PASS, with a residual older-literature risk. Segers' full 2014 preprint treats
mean absolute deviation as a dispersion functional and develops sample
asymptotics, but does not solve any unimodal fixed-variance extremal problem.
The full Navard--Seaman--Young paper characterizes discrete unimodality and
proves variance upper bounds, but no fixed-variance mean-absolute-deviation
formula appears in the inspected text.

Klaassen's full Gauß-inequality preprint uses Khintchine's representation to
obtain sharp continuous tail inequalities under first- and second-moment
constraints. It supplies the relevant continuous uniform-mixture comparison,
but it does not contain an integer-lattice adjacent-uniform interpolation or
the phase correction derived here.

Targeted semantic and web searches for discrete symmetric unimodal mean
absolute deviation, variance-normalized first absolute moments, and uniform
extremizers did not return the displayed finite-variance envelope.

## Value

PASS. Mean absolute deviation is a standard dispersion functional whose
population meaning is particularly transparent and robust to heavy tails. The
theorem gives a complete exact range at fixed variance inside an important
shape-constrained lattice class, identifies all upper extremizers, proves that
no positive lower bound exists without a support constraint, and quantifies the
first lattice correction to the classical continuous uniform constant.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK moment_checks=2002 slope_checks=999 equality_checks=21000 random_mix_checks=30000 low_sequence_checks=20 phase_checks=20`.
