# Self-review

## Correctness
PASS. The Plücker degree was reconstructed directly from Borel--Weil and the type-\(C\) Weyl dimension formula, not imported from a finite table. The contributing positive coroots give a root product that simplifies exactly to
\[
2^{\binom{k}{2}}d!
\frac{\prod_{i=0}^{k-1}i!}
{\prod_{i=1}^{k}(2n-2i+1)!}.
\]
The Bruhat decomposition gives
\[
\chi_{\mathrm{top}}(\operatorname{IG}(k,2n))
=
2^k\binom nk.
\]

For fixed \(k\ge2\), the normalized ratio of degree to Euler characteristic is strictly increasing in \(n\). The proof compares the exact adjacent quotients and reduces the key inequality to an explicit positive polynomial. On the boundary \(n=k\), the exact Lagrangian recurrence shows the normalized degree is already greater than one for every \(k\ge3\). The remaining \(k=1,2\) cases are explicit.

The bundled checker independently evaluates the root product, factorial product, Weyl-cell count, adjacent-\(n\) identity, and Lagrangian recurrence. Finite computation is regression evidence only.

## Originality
PASS. The inspected primary archival source treats the same type-\(C\) isotropic Grassmannians and their Schubert calculus, but targeted full-text searches found no Euler-characteristic or degree-versus-Euler theorem. Searches using geometric, Weyl-cell, two-plane, and Lagrangian formulations did not locate the complete dichotomy.

Nearby results on degree arithmetic, Lagrangian degree identities, and ordinary Grassmannians do not imply the accepted type-\(C\) comparison. Residual risk remains because the final inequalities are elementary once both classical formulas are reconstructed.

## Value
PASS. Plücker degree and Bruhat-cell count are two canonical measures of complexity for a foundational family of homogeneous varieties. The result completely orders them, proves there are no equality cases, and isolates the unique non-projective exception.

Self-review: passed. Independent audit: not yet performed.
