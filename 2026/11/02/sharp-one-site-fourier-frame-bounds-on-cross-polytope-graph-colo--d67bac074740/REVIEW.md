# Mathematical review: sharp colouring-frame spectrum

## Correctness

**PASS.** The complete proof in RESULT.md derives the chromatic count by partition-colour injections, extracts the same-part coincidence probability, and uses colour-label permutation symmetry to isolate the one-site Fourier blocks. Within each spatial block, antipodal differences, zero-sum pair means, and the all-ones vector are an orthogonal, exhaustive eigenbasis. The rank boundary is proved by strict positivity, not by finite samples; the first-extra-palette calculation is an exact factorial identity. The asymptotic follows by bounding the available colours conditional on all other pairs. The accompanying standalone checker confirmed the algebra using exact fractions, eight direct exhaustive small-instance enumerations, and 3756 direct full-character Gram entries. No nonstandard external lemma is assumed.

## Originality

**PASS under bounded primary-source comparison.** Shrock--Xu (arXiv:0911.4218v1) treats weighted proper-colouring partition functions, whereas the new theorem is a labelled-site Fourier Gram eigenvalue result. Crew--Spirkl (arXiv:2009.14141) investigates chromatic symmetric-function bases for complete multipartite graphs; its inspected theorems do not state this spectral reconstruction law. Delorme (DOI 10.1016/j.disc.2011.07.018) computes graph adjacency spectra, which are different operators. General frame-construction theory (Cahill et al., arXiv:1106.0921v1) motivates the norm ratio but does not compute this sample family. A two-part complete-bipartite spectral result intersects the present graph family at the excluded case of two parts only. Targeted published-result searches yielded no covering all-palette formula; absence from searches is not proof of historical priority.

## Mathematical value

**PASS.** This is a natural infinite family of constrained Fourier samplers on graphs of geometric interest (cross-polytope graphs). The first nondegenerate palette has a sharp condition ratio growing linearly with the dimension, while the large-palette ratio tends to one. Full eigenvalues and multiplicities identify the precise directions responsible for ill-conditioning, rather than merely verifying linear independence or recomputing a chromatic polynomial.

## Boundaries and residual risks

The theorem concerns uniform proper colourings and only the constant plus single-vertex additive characters. It asserts an exact minimum of two explicit levels but does not assert a uniform branch ordering for all palettes. An equivalent Potts correlation or association-scheme specialization might exist in less directly indexed literature. No independent mathematical audit or validation has been performed.

Self-review: passed. Independent audit: not yet performed.
