# Review of Sharp range–valence constant for finite-point Schwarz–Pick matrices

## Correctness

PASS. All maps are holomorphic from \(\mathbb D\) into \(\rho\mathbb D\), have valence at most \(m\), and sampling points may repeat. The exact nonnegative-coefficient expansion yields \(H_{\rho g,Z}\preceq\rho^2H_{g,Z}\). Tian's Theorem 2.1 supplies the \(n\) bound. Independently, the area change-of-variables formula and preimage bound control the derivative-weighted Bergman composition operator by \(\sqrt m\), giving \(H_{g,Z}\preceq mG_Z\) even for nonproper maps. The stated constant follows.

Sharpness is exact, not numerical: for \(d=\min\{n,m\}\), the power map \(\rho z^d\) and a \(d\)-point cyclic fiber give a common Fourier eigenvector of the two Gram matrices, with ratio
\[
d\rho^2\left(\frac{1-r^{2d}}{1-\rho^2r^{2d}}\right)^2\to d\rho^2.
\]
Additional sample points do not change the principal-block lower bound. The \(d=1\) endpoint is checked separately.

## Originality

PASS. The full initiating six-page paper was inspected. Its statements are for arbitrary disk self-maps with constant \(n\), or finite **Blaschke products** with constant \(\min(n,d)\); it does not state a sharp constant depending jointly on target radius and *valence of arbitrary nonproper maps*. Earlier operator-theoretic Schwarz–Pick results use different divided-difference and interpolation formulations. Published searches over Bergman Gram matrices, finite valence, weighted composition, and restricted image radius, together with source/claim overlap checks, did not identify a statement that implies the exact three-parameter theorem.

The proof explicitly separates established ingredients from the new combined sharp result. The residual risk is that a short argument combining known tools could have been observed without being indexed or published under the chosen terminology.

## Value

PASS. Valence controls multiplicity while image radius controls analytic range; neither is encoded by the number of sample points. The theorem gives a complete sharp constant for all three natural parameters rather than a nonsharp perturbation of a known bound. Its nonproper extension is important for image-constrained interpolation and derivative data, and the exact branch-point sharpness mechanism differs qualitatively from the boundary-fiber extremizers in the initiating theorem.

Same-model review: passed. Independent audit: not yet performed.
