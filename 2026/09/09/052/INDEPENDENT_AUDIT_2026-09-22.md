# Independent audit — 2026-09-26

Record: `2026/09/09/052`. Verdict: **correctness PASS; originality PASS (two explicit values only); scientific value PASS (limited divisorial data).** Disposition: retain accepted.

## Correctness
I read Belousov–Loginov arXiv:2403.03700v3 §§3,5–6, including the effective cone, intersection table, F1 Zariski decomposition, F2 beta computation and D-flag lemma. Their data hold for the smooth degree-14 family without the special-fibre condition in these steps. Independently expanding (cD+aF1+bF2)^3 from the intersection numbers gives 2c³−6c²a−3c²b+12cab and volume 14 at (1,1,2). Exact rational polynomial integration yields for F1 the pieces 19/4 and 7/8, hence S=45/112 and beta=67/112; for D the integral 17/2, hence S=17/28 and beta=11/28. The D threshold u=1 follows from the cited simplicial effective cone; the line tests make the path nef through 1. BL themselves calculate S(F2)=45/56 in Proposition 5.2 and both D-flag quantities=45/56 with δ_P≥56/45 in Lemma 6.1, exactly as reproduced here.

## Prior work and originality
The geometry, intersection numbers, effective cone, F1 piecewise positive part, F2 value, and D-flag/local delta inequality are already in Belousov–Loginov. I did not find the explicit fractions S(F1)=45/112 and S(D)=17/28 printed there; they follow by elementary integration of that paper's formulas. Originality is credited only to those two numeric divisorial evaluations and their uniform statement, not a new K-stability result or geometric construction.

## Scientific value and limits
The two positive beta values are precise checks for divisors on the special stratum as well as general members. They do not control valuations over worse multiple fibres or prove special-stratum K-stability, and positivity for these divisors is far weaker than the needed global delta bound. The proof depends on the published Mori/effective cone and Zariski decomposition inputs.

Sources: RESULT.md and artifacts/verify_beta.py; https://arxiv.org/html/2403.03700v3, especially §§3,5–6.
