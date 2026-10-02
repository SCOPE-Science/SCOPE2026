# Independent mathematical audit — SCOPE-20260918-d45af12fa2b8

Final disposition: **REPAIRED AND ACCEPTED**.

## Correctness
**PASS** — After removing the already-covered strip component, the surviving ellipse theorem is exact. For an affine disk \(E=x_0+AD\), Plancherel and the radial density \(|\widehat{\chi_D}|^2\) reduce the double-Hilbert defect to the angular measure of the signs of the two row functionals of \(A^{-T}\). If their angle is \(\alpha\), the opposite-sign wedges have total angle \(2\alpha\), so the normalized squared defects are \(4(1-\alpha/\pi)\) and \(4\alpha/\pi\). For the diagonal ellipse the row angle is \(\pi-2\arctan\varepsilon\), giving \(\sqrt{(8/\pi)\arctan\varepsilon}\). No finite experiment is used.

## Originality
**PASS** — The original package bundled two contributions. A separately published September 18 SCOPE finding already gives the sharp truncated-strip asymptotic with the same leading constant, so that component is covered and is removed in the repaired claim. Fresh Resultary searches found no published SCOPE record covering the all-ellipse angular identity, and the accessible primary abstract of Abakumov–Domelevo–Petermichl–Poltoratski states approximate invariant open sets but not an ellipse formula. Full source text was not available in this run, so originality of the ellipse theorem remains best-of-knowledge.

### Equivalent formulations
The surviving final claim is only the all-ellipse defect identity and its diagonal-ellipse corollary; the strip asymptotic is not retained as new content.

### Broader coverage
Those broader results do not mechanically imply the affine-ellipse angular formula in the material inspected.

### Exact database or table
This negative search is not itself novelty proof; the conclusion relies on the source comparison and explicit coverage boundary.

### Claim versus prior implication
After repair, the surviving ellipse theorem is not implied by the inspected prior statement.

## Value
**PASS** — The repaired theorem gives a smooth strictly convex, bounded family with an exact log-free defect and identifies the controlling affine angle for every ellipse. This is a motivated structural counterpoint to the hard-strip construction rather than an arbitrary example.

## Source inspections
- **Invariant sets of the double Hilbert transform** (arXiv:2609.15155): primary arXiv abstract; full text was unavailable through the accessible route in this run Assessment: ABSTRACT_ONLY; does not decide hidden full-text overlap. Evidence: The abstract states existence of finite-measure open-set approximate eigenvectors and exact invariant bent strips, but no ellipse identity.
- **Sharp logarithmic defect for a truncated double-Hilbert strip** (Resultary 2026/9/18 SCOPE-sharp-logarithmic-defect-truncated-double-hilbert-strip--867a0fef0943): complete RESULT.md Assessment: COVERS_OLD_STRIP_COMPONENT. Evidence: It proves the same \(\frac{2}{\pi}\sqrt{\varepsilon\log(1/\varepsilon)}\) leading asymptotic and a stronger convergent expansion.

## Residual risks
- The highly relevant source preprint could not be read in full during this run, so an unindexed ellipse observation remains possible.
- The repaired claim intentionally drops the covered strip asymptotic; no originality is claimed for that component.

## Repair boundary
The final accepted claim is the corrected ellipse theorem in `RESULT.md`; the previously bundled sharp truncated-strip asymptotic is omitted because it is already covered by a separately published result.
