# Independent Audit — 2026/09/20/baumslag-elementary-grading-no-finite-regrading-m9--bf5a40bc90b7

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `71d41d4f60253e181a7eddad21d69e6ba71ba4ef`
- Disposition: **PASSED**

## Correctness

**PASS** — The nine-term construction correctly encodes Baumslag's relator. Using c=b^{-1}ab and a^c=a^2 gives ca^{-2}=a^{-1}c, from which the displayed cycle degrees are a^{-1},a^{-1},b,a,b^{-1},a,b,a^{-1},b^{-1}. Multiplying in the compatible reverse matrix-unit order yields b^{-1}a^{-1}ba b^{-1}ab a^{-2}=1, exactly the defining relator. Any finite regrading therefore sends a,b to elements satisfying the Baumslag relation and hence factors through a finite quotient; Baumslag's theorem makes that image cyclic, forcing the image of a=[a,a^b] to be 1. This is impossible because the original nonzero a-homogeneous component is distinct from the identity component. Transporting a weak equivalence reduces to the same reindexing contradiction. Repeating g_9 for n>9 preserves the obstructing M_9 corner.

## Originality

**PASS** — Gordienko-Schnabel (2018) prove counterexamples only for n>=349 and positivity for n<=3. Gordienko-Pekarsky's current 2026 preprint explicitly improves the counterexample range to every n>=14. Targeted searches for M_9, Baumslag's one-relator group, and finite regrading found no n=9 construction. Baumslag's 1969 finite-quotient theorem is classical; the new content is its compact nine-coordinate encoding in this grading problem, improving the best located upper threshold from 13 to 8.

## Scientific value

**PASS** — The result substantially narrows a concrete open finite-dimensional threshold from 3<=n_0<=13 to 3<=n_0<=8 with a short explicit construction valid over every field. It does not settle n=4,...,8 or reproduce the stronger Hopf/coaction features of the n>=14 construction, but the dimensional improvement is meaningful.

## Sources

- **A non-cyclic one-relator group all of whose finite quotients are cyclic** — Gilbert Baumslag. https://doi.org/10.1017/S1446788700007783 — Classical group-theoretic input; the paper states that every finite quotient of the displayed two-generator one-relator group is cyclic.
- **On weak equivalences of gradings** — Alexey Gordienko; Ofir Schnabel. https://arxiv.org/abs/1704.07170 — 2018 source: counterexamples for n>=349 and positive result for n<=3.
- **On the classification of quantum symmetries** — A. S. Gordienko; A. I. Pekarsky. https://arxiv.org/abs/2511.11923 — Current 2026 version states elementary finite-regrading counterexamples for every n>=14.

## Limitations

- The cases n=4,5,6,7,8 remain unresolved.
- No claim is made that the universal group of the grading is exactly Baumslag’s group.
- The construction does not inherit the additional universal-Hopf/coaction conclusions of Gordienko-Pekarsky.

## Independent checks

```json
{
  "cycle_degrees_reconstructed": true,
  "relator_order_checked": true,
  "finite_quotient_argument_checked": true,
  "n_greater_9_corner_extension_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

GitHub was used only as read-only evidence. The assigned source tree was unchanged between the inventory commit and source-tree-check commit. Open-access/preprint sources were checked before any institutional retrieval attempt. No inaccessible text is claimed as read.
