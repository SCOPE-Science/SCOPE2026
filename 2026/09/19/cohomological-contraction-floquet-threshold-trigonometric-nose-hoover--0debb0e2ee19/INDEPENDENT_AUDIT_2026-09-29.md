# Independent Audit — 2026-09-29

**Record:** `2026/09/19/cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19`  
**Title:** Cohomological contraction and a Floquet edge in the trigonometric Nosé–Hoover flow  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `68a4c924f98008b1ed6a97589771cf59e3ae1ae8`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The exact identities are correct. Eliminating cos(y) from the divergence with ż=b(1−2cos y) gives div v=−(a/2)sin z−(a/(2b))d(cos z)/dt. The stated Liouville gauge for the central-orbit NVE removes the first derivative and gives the displayed two-harmonic Hill equation with a periodic gauge, while Abel’s identity forces transverse determinant one. An independent DOP853 integration reproduced the b=1/2 trace crossing at a≈1.59031680301478, det M≈1, and the reported left/right trace signs.
- **Originality — PASS:** The current source remains the September 17 v1 and its indexed description covers global dynamics, bifurcation diagrams, Lyapunov spectra, integrability limits, and the normal variational equation, but not the source-specific contraction coboundary or a Floquet/Hill stability threshold for the central orbit. Searches for the exact model together with Floquet, Whittaker–Hill, cohomological contraction, and the 1.5903168 threshold found no prior source-specific result. General reversible attractor/repeller theory and periodic-damping Floquet theory are prior art and are not counted as novel.
- **Scientific value — PASS:** The record converts the model’s two-variable contraction observable to an exact one-variable thermostat-phase average and identifies a precise local loss of transverse ellipticity at essentially the same parameter scale as the paper’s observed transition. The distinction between the exact structural identities and the floating-point band-edge computation is scientifically appropriate.

## Independent checks

- Algebraically re-derived the divergence coboundary.
- Re-derived the Liouville substitution including sign and period.
- Integrated the original 2×2 NVE independently and bracketed the trace crossing between 1.58 and 1.60.

## Literature and evidence

- Szumiński and Llibre, Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability — Primary model source; current indexing is v1 from 17 September 2026 and does not advertise the audited contraction/Floquet refinements. (https://arxiv.org/abs/2609.19958)
- Posch and Hoover, Time-reversible dissipative attractors in three and four phase-space dimensions — Generic reversible dissipative attractor/repeller background, excluded from novelty. (https://doi.org/10.1103/PhysRevE.55.6803)
- Sprott, Symmetric Time-Reversible Flows with a Strange Attractor — Generic time-reversible dissipative-flow background, excluded from novelty. (https://doi.org/10.1142/S0218127415500789)

## Limitations

- The cohomological formula assumes b≠0.
- The numerical value a* is high-accuracy floating-point evidence, not an interval-certified theorem.
- The local −1 Floquet collision does not by itself prove the global chaotic transition or a nonlinear period-doubling bifurcation.

**Independent-audit disposition:** passed.

GitHub was read only as evidence; no repository writes were made by this audit run.
