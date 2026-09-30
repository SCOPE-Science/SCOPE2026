# Independent Audit — 2026/09/18/accelerated-filtrations-break-growth-entropy-dichotomy--3c11c354c506

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `fc5bf5d487356c9814d24d4ccfb78cf08c1a707c`
- Disposition: **PASSED**

## Correctness

**PASS** — The accelerated-filtration counterexample is correct under the source paper's own filtration convention 0=V_0⊂V_1⊂... . If U is a finite-dimensional generating subspace containing 1 and A is infinite dimensional, the chain U^r is strictly increasing: equality U^r=U^{r+1} would force all later powers to stabilize and hence A=U^r finite dimensional. Therefore dim(U^{b^n}/U^{b^{n-1}})≥b^n-b^{n-1}; and b^n+b^m≤b^{n+m} for b≥2, so V_n=U^{b^n} is indeed an exhaustive multiplicative finite-dimensional filtration with entropy at least log b. For k[x] the quotient dimensions are exactly b^n-b^{n-1}, giving entropy log b while GKdim=1. This directly contradicts the arbitrary-filtration positive-entropy⇒exponential-growth/GK-dimension implications stated in arXiv:2609.18144v1. The one-sided comparison and the linear-control repair are also sound: exhaustivity gives U⊂V_s and hence U^n⊂V_{sn}, while V_n⊂U^{an+c} supplies the reverse coarse comparison. For the final entropy implication, d(r)=dim U^r is submultiplicative, so log d(r)/r has a limit by Fekete; a positive exponential subsequence forced by the filtered entropy therefore makes that limit positive.

## Originality

**PASS** — Filtration dependence of algebraic entropy is not new: Bock et al. already show that linear reindexing multiplies entropy and explicitly warn that nonzero entropy can be made arbitrarily large. But their zero-entropy discussion covers restricted changes such as linear reindexing and standard filtrations. The record's exponential reindexing U^{b^n} is qualitatively different: it creates positive entropy from a standard zero-entropy filtration and gives a self-contained universal obstruction to a very recent arbitrary-filtration theorem. Targeted searches did not locate this explicit universal acceleration or the k[x] contradiction before the record.

## Scientific value

**PASS** — Although elementary, the construction identifies a genuine hypothesis failure in a current growth/entropy theorem, gives the smallest possible counterexample k[x], and supplies a precise repair by linear comparability with a standard filtration. That is scientifically useful because it separates intrinsic algebra growth from arbitrary index acceleration and prevents downstream use of the false dichotomy.

## Sources

- Growth functions of algebras and an application to Leavitt path algebras (João Schwarz; Alfilgen Sebandal): https://arxiv.org/abs/2609.18144 — Current v1 defines arbitrary finite-dimensional filtrations and states that positive filtered algebraic entropy implies exponential growth.
- Algebraic Entropy of Path Algebras and Leavitt Path Algebras of Finite Graphs (Wolfgang Bock; Cristóbal Gil Canto; Dolores Martín Barquero; Cándido Martín González; Iván Ruiz Campos; Alfilgen Sebandal): https://doi.org/10.1007/s00025-024-02198-0 — Prior filtration-dependence result: linear reindexing multiplies entropy; zero entropy is preserved only for the restricted filtration changes treated there.

## Limitations

- The novelty is the explicit exponential-reindexing obstruction and repair, not the general observation that entropy depends on a filtration.
- A later revision of arXiv:2609.18144 could repair the source theorem; the audit concerns the version and claims available at the assigned snapshot.

## Independent checks

```json
{
  "method": "direct proof reconstruction",
  "checks": [
    "strict growth of U^r in every infinite-dimensional affine algebra with 1∈U",
    "multiplicativity b^n+b^m≤b^(n+m)",
    "exact entropy log b for k[x]",
    "coarse two-sided comparison under V_n⊂U^(an+c)",
    "Fekete argument for exponential intrinsic growth"
  ],
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; Oxford Download was not needed in this record.
