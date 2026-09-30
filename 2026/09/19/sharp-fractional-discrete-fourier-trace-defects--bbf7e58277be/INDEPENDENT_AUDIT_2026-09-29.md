# Independent Audit — Sharpness of all fractional trace-defect regimes for discrete Fourier concentration

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `b907ab5d3105c4b2c9da38d200d84c3aaf571c6f`  
**Audited current source tree:** `b907ab5d3105c4b2c9da38d200d84c3aaf571c6f`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The alternating-gap self-similar construction has boundary neighborhood size O(h^theta) and a matching translation lower law. Parseval converts the two-sided translation law into Fourier mass of order L^{-theta} on every sufficiently large multiplicative annulus after excluding low and high frequencies. The grid-cell approximation differs from E_theta only near its boundary, and taking |k| above a fixed K_0 makes the continuous lower translation term dominate the O(N^{-theta}) discretization error. In the trace identity, all summands are nonnegative: log-many disjoint annuli give N^{d-theta} log N on the critical line, one macroscopic annulus gives N^{d-eta} when gamma>eta, and a fixed nonzero Fourier coefficient gives N^{d-gamma} when gamma<eta. The product constructions satisfy the required Minkowski and spectral-translation hypotheses.

## Originality — PASS

PASS, with the claim deliberately narrowed by archive chronology. Mayeli's Remark 9.4 explicitly leaves the fractional critical logarithm and both off-critical powers open. However, the same SCOPE archive contains an earlier September 19 record, `sharp-off-critical-discrete-fourier-trace-defect--dc7870b56a90`, committed at 02:26 UTC, that already proves the two off-critical power lower bounds along lacunary scales. The present record was first committed at 20:20 UTC. Thus no originality credit is assigned here for merely resolving the off-critical powers. What remains independently new and substantial is the full fractional critical-line logarithmic sharpness, the exact two-sided translation construction for every exponent, the every-annulus Fourier-energy lemma, and the stronger all-large-N realization that simultaneously yields all three regimes.

## Scientific value — PASS

PASS. After removing the already-archived off-critical priority, the fractional critical result still closes the most delicate part of Mayeli's open sharpness question for every 0<theta<1 and supplies a reusable translation-modulus-to-annular-energy mechanism. The all-scale construction is also a genuine strengthening of the earlier lacunary off-critical record.

## Independent checks

- Read Mayeli arXiv:2609.12226v1 from lawful indexed HTML. Remark 9.4 states that fractional critical logarithmic sharpness and both off-critical power sharpness were open; Section 10 labels the fractional experiments numerical evidence rather than proof.
- Re-derived the Cantor-coloring boundary-neighborhood and translation-modulus estimates, including the role of alternating gap generations.
- Re-derived the low/high frequency exclusions in Parseval and the conclusion that a fixed proportion of Fourier L2 mass lies on every macroscopic annulus.
- Checked the grid discretization error and why choosing K_0 sufficiently large preserves the lower lattice translation law.
- Checked all three lower regimes term-by-term in the nonnegative trace identity.
- Verified GitHub chronology: the off-critical SCOPE record entered at commit 3d82b5ae508946c477a9570c4b3d37c716f6b411 (02:26 UTC), while this all-fractional record entered at c4e506e136edb5feff09130550fbc30f22031fa9 (20:20 UTC) on 2026-09-19.
- Verified the current main record tree equals the assigned source-tree SHA and the 2026-09-30 audit markers are absent.

## Limitations

- The examples are deliberately disconnected self-similar sets; no connected-domain sharpness theorem is claimed.
- No novelty credit is assigned to the off-critical power theorem already present earlier in the SCOPE archive.
- The theorem establishes growth-rate sharpness, not exact leading constants or detailed plunge-region eigenvalue asymptotics.
- The direct source and both SCOPE records are very recent, leaving residual simultaneous-work risk outside indexed literature.

## Evidence and references

- https://arxiv.org/abs/2609.12226
- https://arxiv.org/html/2609.12226v1
- https://doi.org/10.1007/s00205-024-01979-9
- https://github.com/SCOPE-Science/SCOPE2026/commit/3d82b5ae508946c477a9570c4b3d37c716f6b411
- https://github.com/SCOPE-Science/SCOPE2026/commit/c4e506e136edb5feff09130550fbc30f22031fa9
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/sharp-fractional-discrete-fourier-trace-defects--bbf7e58277be

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
