# Independent mathematical audit — 2026-10-01

## Final finding

The record passes correctness, originality, and scientific value.

## Correctness

Starting from the exact Kac–Murdock–Szegő phase equation, scaling the first eigenfrequency by block length yields the unique Robin-limit equation under the local-to-unity parameter. The centered cosine eigenvector formula and Riemann-sum normalization give the stated overlap and angle limits; compactness of the scaled parameter gives the iff criterion for convergence to the DCT DC vector. The limiting eigenvalue follows from the exact covariance eigenvalue formula. The guarded verifier was inspected and agrees with these analytic limits; it is corroboration rather than the proof.

## Originality

### Equivalent formulations

Searches covered synonymous statements, equivalent parameterizations, and natural reductions. The final claim was compared at the level of implication rather than title similarity.

### Broader coverage

The closest published repository result from 18 September gives an all-order fixed-DCT rank-one factorization but only a fixed-size DCT endpoint. A near-duplicate boundary-layer record on 19 September was inspected from its actual Git blob, but repository chronology places the assigned result at 03:29:33 UTC and that duplicate result at 15:32:08 UTC, so it is later, not prior coverage. Reznik's primary abstract likewise states only that the corrections become identities as correlation tends to one at fixed order. No inspected prior source implies the sharp joint scale, Robin profile, or first-row iff criterion.

### Exact database or table

No finite table or database was used to infer an infinite theorem or to establish novelty. Repository computations, where present, were treated only as checks of arithmetic or finite instances.

### Claim versus prior implication

Known ingredients and covered consequences were separated from the surviving claim. A prior theorem counts as coverage whenever it logically implies the final statement under the same hypotheses; no such implication was found for the surviving final claim.

## Scientific value

The theorem identifies the exact scale on which the standard high-correlation DCT approximation ceases to be uniform, supplies an explicit limiting profile and nonzero angle, and directly constrains a recent fast-factorization claim. This is a natural asymptotic boundary question rather than an arbitrary parameter slice.

## Source inspections

- **Exact fast factorizations of the AR(1) Karhunen–Loève transform** (arXiv:2609.20221): primary arXiv abstract; direct PDF fetch was blocked Assessment: NOT_COVERING. The abstract states identity corrections as correlation tends to one for fixed order, but gives no joint block-length/high-correlation boundary law.
- **All-order fixed-DCT rank-one factorization of the AR(1) Karhunen–Loève transform** (published repository record dated 2026-09-18): complete RESULT.md from the guarded Git tree Assessment: NOT_COVERING. It proves the rank-one DCT-basis factorization for every order but does not state the local-to-unity Robin limit or the sharp first-row iff criterion.
- **The AR(1) KLT-to-DCT endpoint is nonuniform in block length** (published repository record dated 2026-09-19): complete RESULT.md plus Git commit chronology Assessment: LATER_NOT_PRIOR. Its first result commit is 2026-09-19T15:32:08Z, whereas the assigned result first entered at 2026-09-19T03:29:33Z.

## Residual risks

- The motivating arXiv PDF could not be fetched; only its primary abstract was inspected directly.
- Several older transform references were not available in full, so an older asymptotic statement in different notation remains a residual risk.
