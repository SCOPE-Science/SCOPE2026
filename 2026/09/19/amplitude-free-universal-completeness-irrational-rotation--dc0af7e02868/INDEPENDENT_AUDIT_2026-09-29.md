# Independent Audit — 2026/09/19/amplitude-free-universal-completeness-irrational-rotation--dc0af7e02868

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `3e828529c017c317385e18a3cc53fb88a5efcacb`
- Disposition: **PASSED**

## Correctness

**PASS** — The removal of the amplitude bound is supported by a complete replacement for each place where small amplitude is used. For d>0, every difference lambda_{m+d}-lambda_m is one of d+beta{d alpha} and d-beta(1-{d alpha}); either can vanish only if alpha+beta^{-1} is rational. The lower bound |difference|>=d-|beta| leaves only finitely many small d to inspect, proving uniform discreteness for every fixed nonresonant beta. Bounded displacement from Z then gives density one. In the meromorphic stage, reindexing q=l-floor(beta j) keeps every pole within 1+|beta| of q, so weighted pole summability and the density count survive with beta-dependent constants. Pole collisions imply d(alpha+beta^{-1}) in Z and hence are excluded. The irrational-rotation ergodic average gives pole upper density at most |S|<1, while the integer zeros have lower density one; Jensen's formula forces the meromorphic function to vanish identically. The final Hahn-Banach step is valid for every 1<=p<infinity because dual annihilators on finite-measure S lie in L1. No hidden order-preservation assumption is needed.

## Originality

**PASS** — Bertolini-Florit-Simon-Liehr-Taylor's September 2026 paper is the directly relevant source and establishes universal completeness for an explicit density-one irrational-rotation construction, while the audited record identifies and removes the one-dimensional small-amplitude restriction by replacing its bounded-displacement estimates with finite-beta bounds. Earlier quasicrystal and universal-sampling work establishes related universality phenomena but not this amplitude-free theorem for the same explicit family on arbitrary measurable spectra. Targeted searches for the exact formula, nonresonance condition, and an arbitrary-amplitude follow-up found no covering statement. The novelty claim is limited to this source-specific 1D extension; the surrounding sampling theory is prior art.

## Scientific value

**PASS** — The extension changes the admissible parameter set qualitatively: arbitrarily large perturbation amplitudes are allowed even though the indexing need no longer preserve order. It clarifies that arithmetic nonresonance, rather than small geometric displacement, is the essential obstruction in dimension one. This materially strengthens a very recent explicit universal completeness construction without changing its density threshold.

## Sources

- Universal completeness of exponentials (Susanna Bertolini; Enric Florit-Simon; Lukas Liehr; Mitchell A. Taylor): https://arxiv.org/abs/2609.20805 — Primary 2026 source for the density-one universal-completeness construction and its higher-dimensional extensions.
- Universal sampling and interpolation of band-limited signals (Alexander Olevskii; Alexander Ulanovskii): https://doi.org/10.1007/s00039-008-0674-7 — Earlier universal sampling/interpolation background; uses different constructions and does not supply the audited amplitude-free irrational-rotation theorem.
- Quasicrystals are sets of stable sampling (Basile Matei; Yves Meyer): https://doi.org/10.1016/j.crma.2008.10.006 — Classical simple-quasicrystal sampling background.

## Limitations

- The theorem is one-dimensional and does not remove smallness assumptions from the higher-dimensional construction.
- The resonant set alpha+beta^{-1} in Q and the critical spectral measure |S|=1 are not covered.
- The separation constant may deteriorate badly with beta; no parameter-uniform quantitative frame or stability bound is claimed.
- The source preprint is extremely recent, so contemporaneous unindexed observations remain a residual originality risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "uniform_discreteness_checked_for_both_signs_of_beta": true,
  "meromorphic_reindexing_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before considering institutional retrieval.
