# Review of Sharp log-Lipschitz endpoint for real and imaginary parts of harmonic quasiregular maps

## Correctness

PASS. The proof begins with the exact integral inequality for \(F'=h'+g'\) in the primary source. With a Lipschitz real boundary trace, the endpoint integral is exactly logarithmic in \((1-r)^{-1}\). The source's inequalities
\[
|h'|\le(1-k)^{-1}|F'|,
\qquad
|g'|\le k(1-k)^{-1}|F'|
\]
give
\[
|h'|+|g'|\le K|F'|.
\]
The logarithmic radial growth is integrable, so \(h\) and \(g\) extend continuously to the boundary. A radial--angular--radial path at depth equal to the boundary separation converts the derivative bound into the stated \(\delta\log(e/\delta)\) modulus. The analytic sharpness example is reconstructed exactly: the Fourier series of \(|\theta|\) gives the odd-harmonic conjugate series and the identity
\[
\sum_{m\ {\rm odd}}\frac{\cos(m\theta)}m
=
\frac12\log\cot\frac\theta2,
\]
which yields the coefficient \(2/\pi\). The theorem's quantifiers and boundary range are explicit, and no finite experiment is used for the infinite claim.

## Originality

PASS. The closest source, arXiv:2506.04618v1, proves the real-to-imaginary Hölder transfer only for \(0<\alpha<1\), explicitly states that the Lipschitz conclusion fails at \(\alpha=1\), and gives the \(|\theta|\) example. It does not state the endpoint log-Lipschitz upper bound or the exact \(2/\pi\) leading coefficient.

The related 2025 paper titled “Zygmund's theorem for harmonic quasiregular mappings” was inspected and concerns the classical conjugate-function integrability theorem involving \(\mathbf h\log^+\mathbf h\) and \(h^1\), not the boundary Zygmund or log-Lipschitz class. The 2014 quasiregular Lipschitz-type paper was also inspected: its endpoint theorems transfer regularity from the modulus \(|f|\) to the full map, a stronger and different hypothesis than knowing only the real part. The 2013 modulus-of-continuity theorem transfers a prescribed full boundary modulus to its harmonic extension, again not a real-to-imaginary theorem.

Candidate-specific published-finding corpus searches for harmonic quasiregular Lipschitz endpoints, log-Lipschitz conjugates, Hilbert-transform aliases, and \(\theta\log\theta\) behavior found no statement covering the claim. Residual risk remains that an equivalent endpoint observation could occur under classical conjugate-function terminology not surfaced by the searches.

## Value

PASS. The motivating paper ends its smoothness theorem precisely at \(0<\alpha<1\) and uses a logarithmic counterexample to show why a literal Lipschitz endpoint cannot hold. The accepted claim supplies the natural optimal replacement at that boundary: the real and imaginary parts remain quantitatively coupled, but with exactly one logarithmic loss. This both closes the endpoint regularity picture for the source theorem and identifies the exact leading singular modulus in its canonical counterexample.

Same-model review: passed. Independent audit: not yet performed.
