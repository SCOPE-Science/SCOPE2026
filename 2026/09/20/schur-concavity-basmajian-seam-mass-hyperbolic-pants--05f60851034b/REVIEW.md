# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof reduces the three seam lengths to the standard right-angled-hexagon cosine law. Applying the half-angle identity and elementary hyperbolic sum-to-product identities gives the first closed formula. A three-factor product-to-sum identity gives the second formula.

At fixed total boundary length, the only variable term in the denominator of the second formula is a symmetric sum of translates of \(\cosh\), hence a strictly Schur-convex function. The negative logarithmic dependence makes the seam mass strictly Schur-concave. The equal-cuff maximum and the degenerate infimum follow from majorization; continuity gives the complete range. The sharp \(L/2\) global bound follows from the explicit equal-cuff maximum.

The verification script `artifacts/verify_seam_mass.py` reproduces the direct seam computation from the hexagon law and agrees with the closed formula on deterministic samples.

## Originality

PASS, to the best of our knowledge.

The classical inputs themselves are not claimed as new: hyperbolic pants/hexagon trigonometry, the existence and uniqueness of seams, and Basmajian's orthospectrum identity are established literature.

Searches were made using exact and synonymous combinations involving hyperbolic pairs of pants, seams, orthogeodesics/orthospectra, Basmajian identity, fixed total boundary length, equal cuffs, majorization/Schur concavity, and products of \(\tanh(d_i/2)\). No located source states the closed three-seam mass formula together with the fixed-total strict Schur-concavity, exact range, or sharp universal one-half bound.

A close neighboring paper, Doan--Parlier--Tan (2023), proves monotonicity and convexity properties for pants terms in the Luo--Tan identity. Its object is a different dilogarithmic pants measure, not the three inter-cuff Basmajian contribution. Basmajian--Parlier--Tan (2025) studies families of prime-orthogeodesic identities; no matching fixed-total majorization theorem was located from the accessible records and targeted searches.

Residual risk is material because the proof is elementary once the classical hexagon law is written down. An equivalent formula may occur in older hyperbolic-trigonometry or orthospectrum literature under different notation. The original Basmajian article was bibliographically located, but its complete text was not directly inspected here; the two-dimensional summand was cross-checked in later survey literature. The recent prime-orthogeodesic article was checked through bibliographic/abstract-level material and targeted searches rather than a complete line-by-line full-text comparison.

## Value

PASS.

The result gives a global order theorem, not merely a symmetric-point inequality: any majorization step that balances the cuffs increases the three-seam Basmajian mass. It also gives the exact fixed-total range and a sharp universal statement that these three simplest inter-cuff orthogeodesics account for strictly less than half of the boundary in Basmajian's identity, with one half approached by long equal-cuff pants.

## Limitations

- Compact hyperbolic pairs of pants with positive geodesic cuffs only; cusps are limiting cases.
- The theorem concerns the three inter-cuff seams, not the complete orthospectrum.
- No Schur monotonicity is asserted for the individual seam lengths.
- Equivalent older folklore remains possible.
