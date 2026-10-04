# Review of A logarithmic gap between full and restricted weak square-function bounds

## Correctness

PASS. Osękowski's theorem supplies, for arbitrarily large dyadic \(A_2\) characteristic, a full weak-\(L^2\) lower bound
\[
C_{\mathrm{full}}(w)
>
\frac{e^{-2}}{48}
\sqrt{[w]_{A_2^d}\log(1+[w]_{A_2^d})}.
\]
The 2018 theorem supplies the universal characteristic-input restricted estimate
\[
C_{\mathrm{res}}(w)
\le
C_0\sqrt{[w]_{A_2^d}}.
\]
The normalization is compatible because \(S_{w^{-1}}=SM_{w^{-1}}\) and multiplication by \(w^{-1}\) is an isometry from \(L^2(w^{-1})\) to \(L^2(w)\). Division gives the claimed square-root logarithmic ratio. Selecting source weights at thresholds tending to infinity forces the ratio to diverge.

No converse estimate for \(C_{\mathrm{res}}\) on the same source weights is used, and the claim is limited accordingly.

## Originality

PASS. The full 2026 primary text was inspected through its introduction, exact definition of the dyadic square function and weight characteristic, and Theorem 1.2. It proves sharpness of the full weak norm but does not discuss restricted weak type.

The full 2018 primary text was inspected through its introduction and Section 4. It proves the sharp characteristic-input restricted estimate and emphasizes the absence of a logarithmic correction, while the full weak estimate then available was only an upper bound. Consequently that paper could not establish an unbounded full-versus-restricted separation.

Searches for the source identifier, “restricted weak”, “full weak”, “logarithmic gap”, and weighted dyadic square-function testing found no primary publication stating the ratio theorem. The closest recent published refinement calibrates the full-weak sharpness example but does not compare it with restricted testing.

Residual risk is limited to a short corollary of the two papers having been noted informally or in material not indexed by the searches.

## Value

PASS. Restricted weak testing is a natural testing surrogate in weighted harmonic analysis, and the 2018 paper specifically highlighted its lack of the logarithmic correction present in the full weak upper estimate. The 2026 sharpness theorem makes it possible to decide whether that contrast is merely an artifact of upper bounds.

The result shows it is structural: characteristic-input testing can underestimate the full weak norm by an unbounded factor, with a quantitative square-root logarithmic lower separation. This identifies a precise obstruction to any constant-loss testing characterization at the critical exponent.

Same-model review: passed. Independent audit: not yet performed.
