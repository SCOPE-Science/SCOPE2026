# Mathematical review

## Correctness — PASS

The hypotheses are uniform in arbitrary integers \(p,d\ge2\) and radii \(r,s\in(0,1)\). Independent Fourier transforms of the two regular orbits yield exactly \(d\) positive two-by-two Gram blocks; determinant normalization contributes \((1-r^2)^{pd}(1-s^2)^{pd}\). The numerator recurrence follows by differentiation of the coefficient-generating series. The signed-root induction establishes simple negative roots, including degree-zero and degree-change boundaries. As the relative phase runs through a half period, root-factor squared moduli strictly increase and the denominator squared modulus strictly decreases. The Gram blocks remain positive for distinct nodes and the collision endpoint is handled separately. This proves global strict ordering, not merely a local second variation. The exact optimum is the product of the block determinants at half-step rotation. The accompanying self-contained checker passes 7,598 supplementary assertions.

## Originality — PASS relative to inspected evidence

The root-location theorem in Step 2 is a known Veronese phenomenon (Jochemko, 2016); novelty is not asserted for that input. The concrete new conclusion is a universal *strict global angle ordering* and exact optimal determinant across all integer power Bergman kernels and every equal-sized concentric pair. General approximate-Fekete literature (Karvonen–Särkkä–Tanaka, 2019) does not state this all-parameter phase theorem. A related Hardy/Szegő power-one two-orbit determinant formula is not a higher-power consequence, because the Cauchy determinant identity is specific to exponent one. Contemporary weight-parameter work of Marinescu–Xing (2026) concerns kernel regularity and its abstract does not establish a discrete Gram optimization theorem; its full text was inaccessible. Remaining risk is stronger unindexed literature or unseen full-text material.

## Value — PASS

The relative orientation of two concentric regular interpolation layers is a natural deterministic kernel design problem: its Gram determinant controls aggregate interpolation volume and a product of spectral stability factors. The theorem removes the phase variable *globally* for infinitely many kernels, sizes and radii; establishes strict uniqueness except natural angular periodicity; and supplies exact positive sharp constants. It is not a numerical spot check or a reformulation of a single-radius Hardy case. The result does not claim unrestricted optimal node placement.

Self-review: passed. Independent audit: not yet performed.
