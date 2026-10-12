# Review of Sharp diagonal-purity frontier for depolarization-resistant qudit entanglement

## Correctness — PASS

The global-depolarization partial transpose splits into independent pair blocks with eigenvalues q/d²±(1−q)√(x_ix_j), so NPT survival depends monotonically on m=max√(x_ix_j). For s≥1/2, identity s+2m²=t²+Σremaining x_j²≤t²+(1−t)²≤1 is sharp precisely for two-level input. For s≤1/2, AM–GM on top two and Cauchy on remaining d−2 give s≥2m²+(1−2m)²/(d−2) whenever m≥1/d, and solving the increasing function yields the claimed sharp branch; m<1/d is automatically bounded. Equality cases are explicitly realized and normalized. Checks of 8,016 equality/population cases completed. The proof, not finite tests, covers all real s and all integer d≥3.

## Originality — PASS

Ali et al. 2606.16695 explicitly derives the pairwise global-noise NPT criterion and equal-population threshold, which is credited. The new claim is the *all diagonal-purity strata* sharp optimization and complete equality cases, including a nonmonotone robustness frontier peaking at s=1/2, not a derivation of the already known pairwise spectrum. Independent local-noise flat-support optimization addresses a different channel and restricted input class, so it does not imply this global-noise all-spectrum problem. Targeted public-record and literature queries for collision purity, extremal largest pairs, and two-level optimality found no covering statement; search failure is not proof of novelty. Primary whole-text access limited; priority risk remains.

The strongest source is Ali, Rostom, Al-Kuwari, Kuniyil, Rahim and Haddadi, High-dimensional coherence to entanglement transduction under canonical noise, arXiv:2606.16695v1 (15 June 2026). Its full text was accessed only in indexed extracts, not as a continuous downloaded document. This is an explicit priority uncertainty rather than a claim of full-paper exclusion. Independent local noise is scientifically distinct from the present global-depolarization channel. The classical possibility of an earlier moment-inequality equivalent remains.

## Value — PASS

Diagonal purity Σ|c_j|⁴ is the experimentally meaningful collision probability/inverse participation ratio of input basis measurements. A device choosing coherent populations under a fixed participation budget needs a sharp NPT survival noise guarantee. This theorem supplies the complete exact frontier, all extremizers, a dimension-independent support-changing threshold s=1/2, and the counterintuitive fact that equal occupation of only two levels outlasts an equal-population d-level input under global depolarization. This is a natural full-parameter optimization rather than an arbitrary numerical slice or a claimed improvement in unrelated channel models.

## Limits

The scope is ideal converted pure states, global depolarization, fixed computational-basis collision purity and NPT survival; not all forms of quantum entanglement or alternative local noise models. The verification program tests finite instances and does not substitute for the proof.

Self-review: passed. Independent audit: not yet performed.
