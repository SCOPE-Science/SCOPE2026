# Review of Directional analytic-shadow refinement of harmonic Bergman Riesz–Fejér

## Correctness

PASS. For a harmonic expansion
\[
f(z)=c+\sum_{n\ge1}a_nz^n+\sum_{n\ge1}b_n\overline z^{\,n},
\]
the directional shadow
\[
F_\zeta(w)=c+\sum_{n\ge1}(a_n\zeta^n+b_n\overline\zeta^{\,n})w^n
\]
is analytic and satisfies \(F_\zeta(r)=f(r\zeta)\) exactly. Radial orthogonality gives both its exact weighted Bergman norm and the harmonic norm of \(f\). The elementary coefficient inequality then gives
\[
\|F_\zeta\|_{A^2_\alpha}^2
\le2\|f\|_{a^2_\alpha}^2-|f(0)|^2.
\]
Applying the verified analytic Riesz–Fejér theorem to \(F_\zeta\) proves the claim. The opposite ray is encoded by \(F_\zeta(-r)\), so the diameter estimate follows without an additional structural assumption.

The center normalization is correct because the normalized weighted measure has \(\beta_0=1\). The analytic special case loses no factor, and the test \(f(z)=z-\overline z\) correctly gives zero shadow on the real ray.

## Originality

PASS. The full 2026 primary text was inspected through Theorems 1.2 and 1.3 and the complete proof of Theorem 1.3. Its Hilbert-space refinement explicitly assumes \(f(0)=0\), removes the constant coefficient, splits the function into two real harmonic parts, and obtains a uniform factor-two estimate. It does not state the one-shadow formula, the center-energy correction, or the normalization-free diameter improvement.

Kasuga's full 2025 open-access paper was inspected through its statement of Andreev's \(p=2\) analytic theorem and its all-positive-exponent analytic extension. Those results concern analytic Bergman functions, so they supply the analytic input but not the harmonic directional shadow.

Candidate-specific searches for the source identifier, removal of \(f(0)=0\), center-value corrections, analytic lifts, and weighted harmonic Bergman radial traces found no published statement implying the accepted claim. The accessible abstract of the 2022 harmonic Riesz–Fejér paper concerns harmonic Hardy-space circle/diameter comparisons, not weighted harmonic Bergman traces.

## Value

PASS. The recent paper's strongest \(p=2\) improvement is presented only under an origin normalization, even though its general \(p=2\) theorem has no such restriction. The finding removes that gap and simultaneously exposes the direction-dependent coefficient interference that the real/imaginary splitting discards. For \(\alpha\ge0\), it extends the paper's improved full-diameter constant from normalized functions to all weighted harmonic Bergman functions and retains a strictly favorable center-energy term.

This is a structural strengthening of the new theorem rather than a formal subtraction of a constant: the exact analytic shadow can be much smaller than the uniform estimate because the analytic and coanalytic modes may cancel along the selected ray.

Same-model review: passed. Independent audit: not yet performed.
