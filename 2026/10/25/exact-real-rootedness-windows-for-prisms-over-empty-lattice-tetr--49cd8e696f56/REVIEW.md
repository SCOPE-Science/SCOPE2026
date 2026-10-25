# Scientific assessment: empty-tetrahedron prism root windows

## Correctness
PASS. For any empty lattice tetrahedron, the standard Ehrhart coefficient identities force the numerator \(1+(m-1)z^2\), without using a potentially restrictive Reeve normal form. The product with a length-\(k\) segment multiplies each dilation count by \(kn+1\), giving the stated differential transform. The explicit cubic discriminant factors into two terms with ordered roots in the volume parameter. The rational-root argument excludes additional integral equality boundaries. The finite integer classification follows from the strict monotonicity and limit eight of the remaining threshold. Exact symbolic verification and direct lattice-point tests corroborate these computations. See `RESULT.md` and `check.py`.

## Originality
PASS relative to accessible literature and indexed findings. The relevant inspected May 2026 paper uses Reeve tetrahedra for Ehrhart coefficient sign patterns, not a classification of numerator roots of their segment products. The October 2026 product theorem requires real-rootedness of both factors, while every nonunimodular empty tetrahedron has nonreal numerator roots. The August 2026 large-width theorem is a sufficient result unrelated to fixed width-one realizations. A closely related published result about segment products preserves log-concavity under a log-concave input assumption, which fails for the tetrahedral input with an internal zero. Searches for equivalent roots, discriminants, height thresholds, and parameter tables yielded no decisive prior coverage. Risk: an equivalent result could be expressed using Hadamard-product or real-rootedness-preserver terminology outside indexed sources. Historical novelty is not independently certified.

## Mathematical value
PASS. The natural inverse question is exactly when multiplying an archetypal non-real-rooted lattice simplex by an integer segment produces a real-rooted Ehrhart numerator. The answer applies to *all* empty tetrahedra, is exact for all normalized volumes and segment heights, and reveals nonmonotone transient windows for volumes four through eight but permanent stabilization beyond volume eight. This includes arbitrarily large normalized volumes at lattice width one. It is a motivated sharp phase classification rather than a single arbitrary example or a generic positivity calculation.

## Closest literature and limits
F. Liu, S. Tao, G. Xin (arXiv:2605.23544); F. Liu (arXiv:2610.06338), Section 2; B. Nill (arXiv:2608.03635), Sections 1–3; and the published indexed claim *Lattice-segment factors preserve Ehrhart \(h^*\)-log-concavity* (2026). The method does not classify segment products over tetrahedra with extra lattice points or over higher-dimensional empty simplices. The argument proves a mathematical statement but does not certify worldwide historical priority.

Self-review: passed. Independent audit: not yet performed.
