# Independent audit — 2026-09-30

**Record:** `2026/09/21/stationary-alternating-renewal-markov-pair-law-aliasing--2fe27acb9c54`  
**Repository:** `SCOPE-Science/SCOPE2026` at `253a0fe5d0217455660a277f9adb940030e567ad`  
**Audited tree:** `061715a63b468fdc4b81996017a44479f4436539`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The equilibrium covariance transform rewrites exactly through r_i=phi_i/(1-phi_i) as the displayed dependence on 1+r_0+r_1. Since positive sojourns give phi_i(s)->0 as s->infinity, the high-frequency limit recovers M and then r_0+r_1. Independent symbolic algebra reproduced the explicit Erlang-2 transform r_1=a/s-a/(s+4a), the hyperexponential transform r_0=b/s+a/(s+4a), and their sum (a+b)/s. The proposed phi_0 has positive poles and mixture weights because a+b lies strictly between the denominator roots, and its small-s behavior gives mean 1/b. Matching p and C(t) determines every stationary binary two-time joint table, while the Erlang hazard is age-dependent, so the aliasing and non-Markov conclusion are correct.

## Originality

**PASS (literature-bounded).** Akimoto (2023) supplies the forward equilibrium correlation formula, and older alternating-renewal/telegraph work studies correlations or spectra for specified waiting laws. Searches did not locate the inverse characterization by r_0+r_1 or the all-parameter phase-type construction exactly reproducing every two-state continuous-time Markov pair law. The novelty claim is appropriately limited to this inverse/aliasing statement and explicit construction; older reliability, ion-channel and semi-Markov terminology remains a residual risk.

## Scientific value

**PASS.** The result establishes an exact identifiability boundary: even the full stationary family of lagged two-state transition tables can be perfectly Markov-looking while the process is genuinely semi-Markov. The phase-type counterexample avoids heavy-tail pathologies and clarifies which richer observations are necessary.

## Literature and evidence

- Akimoto, Statistics of the number of renewals, occupation times and correlation in ordinary, equilibrium and aging alternating renewal processes: https://arxiv.org/abs/2306.00359
- Dewanji and Kalbfleisch, Estimation of sojourn time distributions for cyclic semi-Markov processes in equilibrium: https://doi.org/10.1093/biomet/74.2.281
- Lowen and Teich, Fractal renewal processes generate 1/f noise: https://doi.org/10.1103/PhysRevE.47.992

## Limitations

- The model is stationary, binary, alternating-renewal, with independent positive sojourns of finite means.
- Full path, holding-time, higher-order or age-conditioned data can distinguish the aliased processes.
- Equivalent inverse statements in older semi-Markov/reliability literature remain a residual priority risk.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
