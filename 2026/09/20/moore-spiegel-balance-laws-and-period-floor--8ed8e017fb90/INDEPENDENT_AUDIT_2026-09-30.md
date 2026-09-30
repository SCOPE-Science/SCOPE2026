# Independent audit — Exact recurrence balances and a strict period floor for the Moore--Spiegel oscillator

## Scope
Independent review of `2026/09/20/moore-spiegel-balance-laws-and-period-floor--8ed8e017fb90` for task `d78192f91c71d25955327c261d13fec3`. The assigned source tree `2723b3fb4777ade18e4bcbc42f94ffaf0111fb61` matches the tree on repository `main` at commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`. Audit date: 2026-09-30 UTC.

## Correctness
**PASS.**

- Direct differentiation gives Fdot=y^2-Tx^2 and Gdot=z^2+(R-T)y^2-Rx^2y^2; the committed symbolic checker independently reports zero residuals, including the T=0 first integral.
- For compact invariant measures, integration of Lie derivatives gives the two balances and the mean identities. For T<0 the first balance forces support at the origin; for T=0 it forces y=0 and invariance then z=0.
- For bounded forward T<0 trajectories, monotonicity plus boundedness makes x,y square-integrable and uniform-continuity/Barbalat arguments give x,y,z->0. At T=0, the second balance gives z in L2 after controlling its signed y^2 term, and the exact first integral forces convergence of bounded x to one equilibrium level.
- For R>T>0 the second balance gives a strict y^2-weighted mean-square excursion because a nontrivial invariant measure cannot have z=0 almost everywhere. For a nonconstant periodic orbit, the first balance forces T>0, averaging the jerk equation gives mean x=0, sharp Wirtinger gives P>=2pi/sqrt(T), and equality substitution leaves R(x^2-1)x'=0, excluding equality when R!=0.

## Originality
**PASS_NARROW.**

- Targeted searches across classic and modern Moore–Spiegel literature did not locate the exact invariant-measure balances, the complete compact-recurrence obstruction for T<=0, the damping-threshold support statement, or the global strict period floor.
- Baker–Moore–Spiegel (1971) is the principal historical coverage risk because it studies periodic solutions. Open-access searches did not yield verified full text; an authorized Oxford retrieval attempt returned no verified PDF, so this audit does not claim to have read that paper.
- Later accessible literature emphasizes strange attractors, bifurcations, topology/generalizations, and control rather than this package of exact global integral constraints.

## Scientific value
**PASS.**

- The result supplies exact constraints that apply simultaneously to periodic, quasiperiodic, and chaotic compact recurrence, together with a sharp parameter-only period floor and global bounded-recurrence exclusion in the nonpositive-T regime.

## Literature checked
- [A thermally excited non-linear oscillator](https://doi.org/10.1086/148562)
- [Aperiodic behaviour of a nonlinear oscillator](https://academic.oup.com/qjmam/article/24/4/391/1846426)
- [Ordinary Differential Equations with Strange Attractors](https://doi.org/10.1137/0138034)
- [Synchronizing Moore and Spiegel](https://doi.org/10.1063/1.166271)
- [Universalities in the chaotic generalized Moore & Spiegel equations](https://doi.org/10.1016/j.chaos.2014.09.002)
- [Removable dynamics in the Nose-Hoover and Moore-Spiegel Oscillators](https://arxiv.org/abs/2409.16624)

## Limitations
- Invariant-measure claims require compact support; convergence for T<=0 is conditional on forward boundedness; the period theorem does not prove cycle existence.
- Baker–Moore–Spiegel (1971) full text remained inaccessible after lawful open-access attempts and authorized institutional retrieval; no claim is made to have read it.

## Conclusion
The record **passes** the independent three-axis audit on the stated, literature-bounded claim. No substantive research-file correction is required. This audit does not convert a targeted literature search into an exhaustive priority guarantee.
