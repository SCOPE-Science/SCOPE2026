# Self-review

## Correctness: PASS
The support-function decomposition is exhaustive under ordinary constant width and Fourier cutoff five. Curvature nonnegativity bounds a two-frequency sup norm. Sampling at six extrema of the third harmonic yields a phase-independent bound, supplemented by a reverse-triangle bound; the two algebraic regimes imply the exact spectral quadratic inequality. The independent Fourier-area integral then yields the claimed sharp base minimum plus a positive sixth-amplitude gap. The equality support has nonnegative curvature everywhere and is convex. The included deterministic checker passed 1,682 finite diagnostics, which supplement but do not replace the continuous proof.

## Originality: PASS, with historical-priority risk
The strongest prior, Bayen and Henrion (2010 manuscript; 2012 journal), Sec. 3.1.4, **numerically observes** the same minimizing shape for a fifth-degree real-cosine subfamily. The shape and numerical observation are expressly prior, not independently claimed here. The new proof treats every independent third/fifth sine-cosine phase, gives a globally exact inequality and a quantitative fifth-amplitude gap, and completely classifies equality. The 2026 symmetry-minimizer theorem and the published dihedrally invariant harmonics at frequencies \(n\) and \(3n\) do not imply this claim. The full 2010 manuscript remained inaccessible; equivalent earlier analytic inequalities are an unresolved historical-priority risk.

## Mathematical value: PASS
A sharp complete finite-Fourier classification solves a canonical constrained version of constant-width area minimization and answers whether adding the first higher odd harmonic after degree three improves the optimum. The quantitative fifth-amplitude term is meaningful control of shape perturbations and is not a routine substitution of known constants. Its coefficient is not asserted optimal. The differing behavior of resonant higher harmonics gives substantive mathematical motivation.

## Evidence and limitations
Detailed comparison searches, accessible source material, and bounded historical-priority uncertainty are recorded in AUDIT.json. The package includes a complete all-phase elementary proof and a standalone standard-library verifier; finite computations do not prove the continuum statement. No result beyond Fourier degree five or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
