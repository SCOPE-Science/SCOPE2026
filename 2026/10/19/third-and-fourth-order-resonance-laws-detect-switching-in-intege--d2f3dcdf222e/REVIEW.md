# Review of Third- and fourth-order resonance laws detect switching in integer expanding circle maps

## Correctness — PASS

Every choice of integer slopes at least two and every length \(n\ge1\) is covered by a complete signed-frequency classification. The single-frequency and two-pair baseline terms, the local tripling and consecutive-doubling resonances, and the impossibility of other low-degree collisions are each proved in `RESULT.md`. The run-count argument proves attainability of every inverse-grid point. The actual `checks/verify_moments.py` independently evaluated finite Fourier coefficients using rational arithmetic: 2,297 complete moment comparisons and 66 small-length complete inverse-spectrum checks passed. These diagnostics are finite; they are not presented as a substitute for the all-\(n\) proof.

## Originality — PASS, with priority risk

The most direct prior method, Aistleitner–Berkes–Tichy (arXiv:2301.05561, Section 3), derives moments from signed Diophantine frequencies and explicitly identifies dyadic triple resonance; this method and principle are established prior work. Suzuki (arXiv:2303.17521, primarily 37E05) concerns random beta-map invariant densities. Prochno–Strzelecka (arXiv:2312.09137) prove asymptotic moderate deviations by cumulant estimates. Aimino–Nicol–Vaienti (arXiv:1310.4359, Example 7.3) prove quenched CLTs for random integer multiplication maps. Published published-finding corpus findings c097279b5a2a (annealed asymptotic variance rigidity) and d5c688b954c6 (pair-correlation variance) were checked in full public RESULT text. None of these inspected claims computes both arbitrary-word exact low moments and a sharp complete inverse attainable spectrum. An uncatalogued elementary equivalent enumeration remains a genuine priority risk; unsuccessful searching does not prove global novelty.

## Mathematical value — PASS

The first and second moments are invariant under every integer multiplier sequence, whereas the third/fourth moments identify the exact number and temporal clustering of minimal expansion choices. The sharp no-gap range for all binary schedules and counts is a natural completed invariant: it provides a quantitative finite-time diagnostic between Gaussian-scale universality and arithmetic resonances without requiring broad asymptotic claims. It does not reconstruct entire words or guarantee identifiability from empirical observations.

## Scientific boundaries

All expectations in the deterministic-schedule theorem are over Lebesgue-uniform initial points. The independent-schedule formulas are an explicitly separate annealed corollary; they should not be confused with a quenched central-limit statement. Other observables, noninteger slopes, and noisy finite-sample inference are unproved. Classical Fourier orthogonality and signed-frequency combinatorics are not credited as new. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
