# Scientific review: the first-Hermite annular concentration counterexample

## Correctness

**PASS.** The spectral identity is reconstructed from the complete Hermite basis and the first true-polyanalytic Bargmann transform. Its angular frequencies are distinct, so the centered-disk localization form is diagonal, not merely bounded by a truncated computation. The factorization
\[
\lambda_m(T)-\lambda_{m+1}(T)=e^{-T}\frac{T^m}{m!}\frac{(m-T)(m+1-T)}{m+1}
\]
proves the disk's exact infinite-dimensional maximum at unit area, including all boundary equalities. Time-frequency covariance handles off-center disks. Annular area is exactly one; an elementary strict logarithmic inequality proves the lower bound exceeds the disk norm. The supplied stand-alone checker independently reproduces the finite integral identities and numerical inequality. No finite calculation is used to justify the infinite-dimensional supremum.

## Originality

**PASS, subject to remaining bibliographic risk.** The motivating historical Hermite-window transformation (Abreu–Gröchenig, arXiv:1012.4283, §2) concerns transforms and sampling, not optimal concentration regions. Maximenko–Tellería-Romero (arXiv:1905.00978, Proposition 6.3) provides general radial Toeplitz spectral integrals but neither the unit-area disk's threefold top eigenvalue nor the optimized, strictly superior equal-area annular construction. Obtaining the counterexample requires comparing the full infinite disk spectrum with a separate area-constrained variational calculation. Nicola–Tilli's Gaussian-window Faber–Krahn theorem (arXiv:2106.03423) concerns a different window and hence cannot imply the same disk-optimality statement for the first Hermite window. Targeted searches for annular counterexamples and equivalent formulations did not identify a prior statement of this precise strict comparison. A broader unpublished or unlocated shape-optimization theorem, or an overlooked explicit deduction of the 2019 radial formula, could affect novelty; absence from searches is not a proof of uniqueness.

## Value

**PASS.** Gaussian-window disk optimality is a fundamental benchmark for spectrogram energy concentration. Changing only the analysis window to the first excited Hermite state changes the optimal *shape*: an explicitly optimized unit-area ring improves captured energy by approximately \(33.675\%\) over every disk. The theorem is an exact motivated counterexample to an otherwise tempting extension of an isoperimetric principle. It delimits a concrete measurement-design limitation without asserting an unproved global annular optimizer.

## Remaining limitations

The optimized annulus is optimal only among concentric unit-area annuli for the fixed Gaussian test signal. Global optimizers among arbitrary measurable regions or other input states are not characterized. Bibliographic comparison includes full relevant sections of the primary sources, but cannot rule out every more-general theorem. Computational checks are corroborative, not external certification.

Self-review: passed. Independent audit: not yet performed.
