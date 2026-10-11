# Scientific review: split finite-field extension Hessian

## Correctness — PASS

For every odd prime power, the proof converts the quartic extension moment to an ordered-pair convolution with the exact factor \(q^{-5}\). It counts the \(xy=w\) fibers, computes the Fourier transform of each character-weighted fiber sum, and evaluates the axis-support character sum. These identities give four explicit real quadratic coefficients with strictly positive nonconstant spectrum. They also establish the stated multiplicities and the sharp local Rayleigh bound. Direct comparison of the two independent quadratic computations in `hessian_check.py` passes 88 tests, including the nonprime field \(\mathbb F_9\). Finite tests alone are not treated as an infinite-field proof.

## Originality — PASS, subject to indexed-source limitations

The closest primary source, arXiv:2405.16647, Theorem 1.4 and Section 7, provides the best \(L^2\to L^4\) constant, the global extremizers and convolution sizes, not the second-variation spectrum or sharp local coercivity. The new result requires a separate two-frequency Fourier calculation and identifies unequal real/imaginary axes-versus-mixed curvature bands, which do not follow as quantified statements from uniqueness of extremizers. Related indexed finite-field moment-curve stability results concern a different object and exponent, and later cone results concern different quadrics. Residual risk: an equivalent local Hessian computation may exist in unindexed literature.

## Value — PASS

The exact local stability constant answers how sensitively sharp extension deteriorates under infinitesimal perturbations, distinguishing amplitude and phase as well as isotropic and rulings-aligned frequencies. The result identifies the unique least-curved geometric family and extends without alteration to nonprime odd finite fields. This is a meaningful quantitative refinement of a natural sharp endpoint inequality, rather than a numerical illustration or restatement of extremizer uniqueness.

## Limits

Only local stability is proved, with a field-size-dependent neighborhood; no global distance-to-extremizer modulus is asserted. The full unrestricted proof depends on finite-field character orthogonality and the previously established sharp inequality. No independent external validation is claimed.

Same-model review: passed. Independent audit: not yet performed.
