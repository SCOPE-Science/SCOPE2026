# Review of Sharp transverse derivative and optimality of the harmonic Landau shear

## Correctness

PASS. For bounded real harmonic \(u\) with zero value and zero gradient at the origin, the first three Fourier constraints remove the constant and first harmonics. The transverse derivative at \((r,0)\) is therefore a linear functional against the odd kernel
\[
K_r(t)
=
\frac{(1-r^2)\sin t}{(1-2r\cos t+r^2)^2}.
\]
After odd symmetrization, the only remaining constraint is the zero first sine moment. Subtracting the median kernel level \(H_r(0)\) gives an \(L^\infty\) extremal problem whose sign changes exactly at \(t=\pi/2\). The resulting integral is exactly
\[
\frac{8r}{\pi(1-r^4)}.
\]
The source perturbation has the extremal boundary trace and saturates the bound.

For a vertical shear, the Jacobian is
\[
1+(M-1)u_y.
\]
Thus the sharp derivative inequality gives an exact lower bound on every positive-real-axis fold radius, attained by the source map. The comparison with the holomorphic Landau radius reduces to one strictly increasing cubic, proving the exact threshold.

## Originality

PASS. The fresh primary source contains the same extremal-looking harmonic function but uses it only as one counterexample and compares its exact fold radius to a crude rational upper bound. It neither proves derivative extremality among all zero-first-jet perturbations nor computes the optimal threshold of the full shear mechanism.

A full-text comparison with modern harmonic Schwarz-lemma literature found sharp general gradient bounds but no refinement using the vanishing first jet. A full-text comparison with higher-order harmonic Schwarz lemmas found different hypotheses: sense-preserving disk self-maps with a zero of multiplicity \(p\), rather than scalar bounded harmonic perturbations into an interval.

Candidate-specific published-finding searches over the source identifier, the exact threshold, the derivative constant, zero-first-jet terminology, and vertical-shear optimality returned no implication-equivalent result.

## Value

PASS. The source paper's threshold improvement alone would be numerically small, but the accepted claim is structural: it proves that the source perturbation is the sharp extremal for the entire natural vertical-shear counterexample architecture. This identifies exactly what the construction can and cannot achieve.

The theorem therefore converts one explicit counterexample into an optimality principle, supplies the exact parameter boundary for that mechanism, and creates a benchmark for any future attempt to disprove the harmonic Landau conjecture at smaller \(M\): such an improvement must leave this real-axis bounded-shear framework or exploit a different critical geometry.

Same-model review: passed. Independent audit: not yet performed.
