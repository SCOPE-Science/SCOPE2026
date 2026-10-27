# Scientific review

**Correctness — PASS.** The real dimension-four spherical-harmonic addition formula produces the exact Gram normalization. All 24 base characteristic polynomials have independent exact-integer power-sum checks (24 moments each) in `verify_f4_spectra.py`; the finite check is exhaustive for the 24 possible residues. A proof of the 24-periodic diagonal shift completes the infinite-degree result, including the tightness characterization.

**Originality — PASS under bounded search.** The nearest literature provides Gegenbauer-design methods and D4/F4 group geometry, not the coupled normalized short/long F4 line spectra. Related separate-orbit sampling and a generic rational-angle periodicity result do not imply the 24 finite cross-orbit eigenvalue tables. Literature searches did not identify the same table; unindexed equivalent work remains possible.

**Mathematical value — PASS.** The explicit finite association of two dual 24-cells produces a complete spectral classification, a sharp early tight-interpolation degree, and repeated degree-by-degree loss/recovery of interpolation. This is a natural harmonic interpolation problem for an exceptional root arrangement, not an arbitrary data subset.

**Closest primary literature:** Bannai–Okuda–Tagami (2013), arXiv:1308.5101; Hirao–Nozaki–Tasaka (2023), arXiv:2303.09000. **Scope:** exactly degree-resolved sampling on normalized root lines, not general spherical designs.

Self-review: passed. Independent audit: not yet performed.
