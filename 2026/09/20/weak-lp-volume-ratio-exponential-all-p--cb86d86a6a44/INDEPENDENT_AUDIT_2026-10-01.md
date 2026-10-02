# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-cb86d86a6a44`

## Correctness — PASS

After scaling, membership in the positive weak-\(\ell_p\) ball is exactly the empirical-tail family \(N_y(t)<nt^{-p}\). The positive \(p\)-Gaussian has the same entropy rate as the scaled \(\ell_p\) ball and satisfies every tail constraint strictly. Moving sufficiently small mass from an interval below one to a higher compact interval preserves the strict tail constraints while increasing differential entropy; compactifying the remaining tail only decreases the constrained survival function. A finite partition with uniform slack produces type classes entirely inside the weak ball, and Stirling plus binwise relative entropy gives an exponential volume rate strictly above the classical \(\ell_p\) rate. This yields a positive exponential gap for every finite \(p\).

### Correctness sources

- assigned RESULT.md
- Doležalová–Vybíral 2020 full accessible article text
- Kabluchko–Prochno–Sonnleitner 2023

### Correctness risks

- The proof is existential and gives no optimal exponential base or exact nth-root limit.

## Originality — PASS

Doležalová and Vybíral's primary article was inspected at its ratio-of-volumes section. It proves exponential growth for \(0<p\le2\) and explicitly states the same conclusion for all finite \(p\) as an open problem. Current Resultary searches found no later theorem closing the \(p>2\) range except the audited record. The later probabilistic Lorentz-ball work concerns different second parameters and does not imply this weak-\(\ell_p\) ratio statement.

### equivalent_formulations

Searches:
- Resultary: weak Lp volume ratio exponential all p Dolezalova Vybiral open p>2
- Doležalová–Vybíral DOI 10.1016/j.jat.2020.105407
- Kabluchko–Prochno–Sonnleitner arXiv:2303.04728

Evidence:
- The 2020 paper explicitly proves the ratio theorem only for \(0<p\le2\) and states all finite \(p\) as an open problem.
- No current semantic hit supplies the missing \(p>2\) theorem.

Reasoning:
The exact weak-Lorentz ratio, general Lorentz-ball asymptotics, and entropy-number embeddings were compared separately.

### broader_coverage

Searches:
- Doležalová–Vybíral 2020
- probabilistic Lorentz balls 2023
- entropy numbers of Lorentz embeddings 2025

Evidence:
- The broader later works do not state a weak-\(\ell_p\) to classical-\(\ell_p\) volume ratio with positive exponential gap for all finite \(p\).

Reasoning:
Coarse nth-root volume estimates for each ball separately do not imply that their ratio has a strict exponential factor.

### exact_database_or_table

Searches:
- current Resultary Lorentz/weak-Lp findings
- volume-ratio searches

Evidence:
- No exact database/table or stronger covering theorem was located.

Reasoning:
The claim is an asymptotic analytic theorem, not a table value.

### claim_vs_prior_implication

Searches:
- claim-versus-2020 theorem

Evidence:
- The source's Theorem 8 stops at \(p\le2\) and explicitly leaves the remaining range open.

Reasoning:
The audited entropy perturbation is a new mechanism that crosses the previous parameter barrier rather than a substitution into the older construction.

### source_inspections

- **On the volume of unit balls of finite-dimensional Lorentz spaces** — https://doi.org/10.1016/j.jat.2020.105407. Trigger: Primary source posing the exact open range. Material read: Accessible full article text through the weak-Lebesgue volume formulas and Section 3.2 ratio-of-volumes theorem/open problem. Method: Primary full-text statement comparison. Assessment: NOT COVERING \(p>2\); explicitly leaves it open. Evidence: Theorem 8 proves exponential growth for \(0<p\le2\), followed by the statement that the all-finite-\(p\) extension is left open.
- **A probabilistic approach to Lorentz balls** — https://arxiv.org/abs/2303.04728. Trigger: Closest later probabilistic/maximum-entropy framework. Material read: Accessible bibliographic and theorem-scope material. Method: Scope comparison. Assessment: Not covering the weak-\(\ell_p\) ratio theorem. Evidence: Its parameter regime and probabilistic representation differ from the audited weak-ball ratio problem.

### checked_sources

- https://doi.org/10.1016/j.jat.2020.105407
- https://arxiv.org/abs/2303.04728
- https://doi.org/10.4064/sm240409-15-2
- current Resultary exact search
- assigned RESULT.md

### residual_risks

- A non-indexed solution to the 2020 open problem could exist, but no plausible specific covering source was found.

## Scientific value — PASS

The theorem closes an explicit open parameter range in high-dimensional Lorentz-ball geometry. The entropy-improving tail-slack argument is also reusable: it converts strict empirical-tail feasibility into a strict volume-rate gain without relying on the older low-\(p\) subset construction.

### Value sources

- Doležalová–Vybíral open problem
- assigned entropy/type proof

### Value risks

- The exact asymptotic rate and optimal exponential base remain open.

## Limitations

- Finite \(p\) only.
- Existential positive rate; no exact limit or optimal base.
- No large-deviation principle or limiting empirical law is proved.

## Disposition

**PASSED**
