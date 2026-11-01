# Scientific review of exact low-bandwidth sensor migration

## Correctness

**PASS.** The statement fixes the normalized path operator, orthonormal eigenvectors, the number of low Fourier modes, the temporal Vandermonde design, and the determinant criterion. The exact determinant ratio follows from the normalized cosine eigenvectors with all endpoint factors canceled. Piecewise-cubic calculus gives the four-mode global classification, including ties at path orders \(4,7,9\). The general inward-neighbor theorem uses an explicit quantitative cosine-product estimate. The extracted standalone checker reports `CHECK_OK assertions=5641`; this is supporting evidence and not a substitute for the universal proof.

## Originality

**PASS relative to inspected accessible sources; priority remains provisional.** Marques et al. give the general Vandermonde sensor framework and a determinant-noise criterion, but do not classify low-pass optimal sensors on normalized paths. Bulai et al. (2026-09-21) analyze graph Paley-Wiener dynamical sampling and numerical path examples; the inspected abstract does not state exact \(m=2,3,4\) thresholds, exceptional ties, or the arbitrary-bandwidth large-path rule. A published full-spectrum normalized-path determinant optimum instead chooses endpoints. This full-spectrum claim cannot imply the present strict low-pass classification by parameter substitution: for large \(n\) the current optimizers are the immediate neighbors, not the endpoints. The source's inaccessible full text and unindexed earlier work remain risks. A search failure by itself is not a proof of novelty.

## Value

**PASS.** The exact \(D\)-optimal sensor location is relevant to graph-diffusion reconstruction under isotropic sensor noise. The result identifies a genuine low-bandwidth/full-bandwidth reversal, completely enumerates exceptional ties for the first four modes, and proves a uniform localization theorem at arbitrary finite bandwidth. These claims are stronger than verifying a particular path numerically; they provide a complete natural small-band design classification and a general structural sufficient condition.

## Limits

The bounds concern determinant design for one sensor, not all notions of stability. The sufficient general bandwidth threshold is not known to be sharp. A full-text comparison against the 2026 motivating article was unavailable; the closest accessible primary manuscript concerns the broader sampling framework.

Self-review: passed. Independent audit: not yet performed.
