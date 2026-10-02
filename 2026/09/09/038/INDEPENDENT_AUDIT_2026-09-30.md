# Independent audit — SCOPE-20260909-038

Audited at: 2026-09-30T22:49:30Z

Final disposition: **repaired**.

## Correctness

**PASS** — Fresh enumeration of all 65,536 skew-symmetric length-33 sequences reproduced E_min=88 at exactly indices 10112,15366,26963,29397, 281 distinct energies, total energy 32,505,856, and vanishing odd-lag correlations. Independent grid evaluation reproduced the stated flatness values for all six frontier members. A separate all-member FFT grid scan, combined with the rigorous Bernstein enclosure factor 1.0000047062172828, certified that every one of the other 65,530 members is dominated by a frontier member. The three reversal-pair frontier, rectangle exclusion F>=6 and M<=1.25, and all quoted endpoint intervals follow.

## Originality

**PASS** — The merit optimum at N=33 is not new by itself: Packebusch-Mertens computed all optimal skew-symmetric sequences through N<=119. What survives as the final claim is the joint merit-flatness Pareto census and certified flatness tradeoff; no checked source supplies or implies that joint table.

### Equivalent formulations

Searches checked: published-record search: length 33 skew symmetric Littlewood merit flatness Pareto; web: N=33 skew Littlewood sup norm merit factor Pareto.

Evidence: The only exact joint match was the present record. Prior LABS sources optimize autocorrelation energy/merit, not the unit-circle sup-norm jointly.

Reasoning: No equivalent joint Pareto statement was located.

### Broader coverage

Searches checked: Packebusch Mertens Low Autocorrelation Binary Sequences 2016; De Groot Wurtz Hoffmann exact enumeration skew sequences; Balister et al Flat Littlewood Polynomials Exist.

Evidence: Packebusch-Mertens covers merit-optimal skew sequences through N<=119; Balister et al. is asymptotic flatness existence. Neither gives the N=33 joint merit-flatness frontier.

Reasoning: A known merit optimum plus a general flatness theorem does not imply the six-member finite Pareto frontier or its certified intervals.

### Exact database or table

Searches checked: LABS skew N=33 optimal sequence tables; length 33 Littlewood flatness table.

Evidence: Merit-factor tables cover the energy optimum; no checked table contains the all-65,536 flatness/energy joint dominance data.

Reasoning: The exact merit marginal is covered, but the joint database is not.

### Claim versus prior implication

Searches checked: arXiv:1512.02475 skew optimal sequences; arXiv:1907.09464 flat Littlewood.

Evidence: Autocorrelation optimality does not determine sup norm, and asymptotic existence of flat polynomials does not identify this finite skew frontier.

Reasoning: The joint claim requires the independent finite flatness enclosure/census.

### Source inspections

- **Low Autocorrelation Binary Sequences** (https://arxiv.org/abs/1512.02475): PARTIAL_COVERAGE. Material read: abstract stating all optimal sequences N<=66 and all optimal skew-symmetric sequences N<=119. Covers the N=33 merit optimum in principle, but not the joint flatness/Pareto census.
- **Low autocorrelation binary sequences: exact enumeration and optimization by evolutionary strategies** (https://doi.org/10.1080/02331939208843771): PARTIAL_COVERAGE. Material read: publisher abstract describing skew chains through N=71 and merit-factor tables. Merit/autocorrelation enumeration only; no joint Littlewood sup-norm frontier.

Checked sources: published SCOPE findings search; Packebusch-Mertens 2016; de Groot-Wurtz-Hoffmann 1992; Balister et al. 2019.

Residual risks: Flatness-specific finite tables may exist under sequence-design terminology; no such N=33 joint table was found.

## Scientific value

**PASS** — The exact Pareto tradeoff between two independently motivated sequence-quality criteria (aperiodic merit and Littlewood sup-norm flatness) is a natural finite classification for the classical skew-symmetric N=33 LABS space. The full frontier and dominance certificate are more informative than the already-known merit optimum or the stipulated rectangle alone.

## Repair

The old sentence treating size-22 existence as open is removed. Kadoo (2010) is cited as prior global Rédei-type existence. The final theorem is explicitly limited to the three verified witnesses and the low-complexity graph-function exclusion. The repaired claim was reassessed on all three axes above.
