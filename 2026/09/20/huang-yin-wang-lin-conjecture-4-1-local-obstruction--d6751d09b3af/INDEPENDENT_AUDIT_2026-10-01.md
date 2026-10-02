# Independent mathematical audit — 2026-10-01

## Final claim assessed

A local asymptotic obstruction to Huang–Yin–Wang–Lin Conjecture 4.1

## Correctness — PASS

PASS. Expanding the defining inverse integrals in the local variable \(t=x^p\), reverting the series, and expanding the logarithms gives the stated coefficient of \(x^p\), namely \((3p^2-2p-2)/(2(p+1)^2(2p+1))\). Its sign is negative below \(p_0=(1+\sqrt7)/3\). At \(p=p_0\) the first coefficient vanishes, and an independent symbolic substitution gives the next coefficient \((80\sqrt7-212)/81<0\). Since the ratio tends to \(1/(p+1)\) as \(x\downarrow0\), either negative local term contradicts strict increase. The repository symbolic script agrees with the independent coefficient check but is not itself the proof.

## Originality — PASS

PASS to the best of current knowledge. The complete 2018 Huang–Yin–Wang–Lin article was inspected and ends by posing exactly this monotonicity question as Conjecture 4.1. Published-record searches for the ratio, the polynomial \(3p^2-2p-2\), and the threshold \((1+\sqrt7)/3\) found no earlier counterexample or local expansion. A highly relevant 2020 one-parameter inequalities paper was identified; ordinary full-text retrieval timed out and a lawful institutional attempt found no verified PDF, so it remains an explicit access risk rather than evidence of noncoverage.

### equivalent_formulations

Searches: Huang Yin Wang Lin Conjecture 4.1 generalized sine hyperbolic cosine monotonicity; log(x/sin_p x) over log cosh_p x threshold; Resultary: generalized trigonometric Conjecture 4.1 local obstruction

Evidence: The 2018 primary paper states the ratio and asks whether it is strictly increasing for all \(1<p\le2\); no earlier local-sign obstruction was found.

Reasoning: The Taylor-sign formulation is exactly a local necessary condition for the conjectured monotonicity, so a negative coefficient is a genuine counterexample mechanism.

### broader_coverage

Searches: DOI 10.1186/s13660-018-1644-8 full text; DOI 10.7153/jmi-2020-14-01; DOI 10.1515/dema-2025-0103

Evidence: The 2018 source poses the problem; accessible later indexed material concerns other one-parameter generalized trigonometric inequalities.

Reasoning: No inspected broader theorem implies monotonicity or its failure for the exact logarithmic ratio.

### exact_database_or_table

Searches: Published-record search for coefficient \(3p^2-2p-2\) with generalized sine/cosh; search for threshold \((1+\sqrt7)/3\) in the conjecture context

Evidence: No exact prior theorem or table entry was found.

Reasoning: This is an analytic local expansion rather than a tabulated invariant.

### claim_vs_prior_implication

Searches: 2018 Conjecture 4.1 full HTML; 2020 one-parameter generalized trigonometric inequalities metadata

Evidence: The source leaves the question open; the audited expansion supplies the first located implication that contradicts it on a nontrivial parameter interval.

Reasoning: The counterexample is not a corollary of the printed source results.

## Scientific value — PASS

PASS. A rigorous counterexample interval to an explicit published conjecture is a motivated mathematical correction even though the proof is local. The exact threshold where the first obstruction vanishes, and the second-order endpoint calculation that closes equality there, are necessary to state the counterexample range sharply.

## Source inspections

- **Some Wilker and Cusa type inequalities for generalized trigonometric and hyperbolic functions** — https://doi.org/10.1186/s13660-018-1644-8. Material read: Complete primary HTML, including Theorem 3.9 and Section 4, where Conjecture 4.1 asks whether the audited logarithmic ratio is strictly increasing. Assessment: PRIMARY_SOURCE_EXPLICITLY_LEAVES_CLAIM_OPEN. Evidence: Conjecture 4.1 asks the exact monotonicity question for \(1<p\le2\).
- **Inequalities for generalized trigonometric and hyperbolic functions with one parameter** — https://doi.org/10.7153/jmi-2020-14-01. Material read: Journal metadata and title/issue context; verified full text was not obtained after lawful access attempts. Assessment: INACCESSIBLE_PLAUSIBLE_PRIOR_SOURCE. Evidence: Its scope overlaps the same generalized functions, so hidden overlap is retained as an originality risk; no snippet is used to claim whole-document noncoverage.

## Limitations and residual risks

The result disproves Conjecture 4.1 for \(1<p\le(1+\sqrt7)/3\). It does not determine the global monotonicity range above that local obstruction threshold.

- The 2020 one-parameter inequalities article could not be read in verified full text and remains a plausible originality risk.
- The result is only a local obstruction and leaves \(p>(1+\sqrt7)/3\) unresolved.

## Disposition

**passed**
