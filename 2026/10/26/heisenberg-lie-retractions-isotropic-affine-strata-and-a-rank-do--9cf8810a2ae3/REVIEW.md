# Scientific review

## Correctness

**PASS.** Bracket preservation forces the central block form and the exact equation \(A^TJA=cJ\). Combining it with the three idempotence equations leaves only the identity for \(c=1\), and isotropic-image projections with freely chosen complement and functional for \(c=0\). The isotropic Grassmannian dimension, affine-bundle fiber, finite-field isotropic-frame enumeration and discrete rank maximization are derived explicitly in `RESULT.md`. Direct exhaustive tests of the smallest finite-field cases and the dimension differences passed in `verify.py`. The computations alone do not prove the general theorem.

## Originality

**PASS, with bounded priority risk.** The nearest primary sources concern automorphisms and *normal* decompositional projections [Fisher–Gray–Hydon, arXiv:1303.3376], almost-direct factors [Bergman–Nahlus, arXiv:0910.5181], and unital algebra weak augmentations [Facchini–Heidari Zadeh, arXiv:2210.08230]. These do not state the decomposition of arbitrary Heisenberg Lie retractions by isotropic image and affine complement data, nor the rank-resolved finite-field count and maximal-component transition. Relevant research-record and literature searches found no direct equivalent, but hidden or differently formulated prior classifications remain possible.

## Value

**PASS.** The image of a proper retraction must be abelian, imposing a sharp rank cutoff \(r\leq n\); the exact rank strata form smooth algebraic families rather than an ad hoc finite count. The transition from top-rank to intermediate-rank maximal components at \(n=4,5\) is a structural phenomenon with a corresponding finite-field large-\(q\) distribution. The result does not require an unproved downstream application for this classification to be useful.

## Sources and limits

The general algebraic facts about projections and symplectic isotropic subspaces are pre-existing. There is residual uncertainty about publication priority, especially work indexed under retracts rather than endomorphisms. The theorem is for the standard Heisenberg Lie algebra over fields, not generalized nilpotent Lie algebras or group retractions. No independent validation has been carried out.

Self-review: passed. Independent audit: not yet performed.
