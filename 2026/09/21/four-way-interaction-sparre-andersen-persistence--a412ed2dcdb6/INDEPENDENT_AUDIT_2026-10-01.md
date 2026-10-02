# Independent audit — 2026-10-01

## Final claim

For four fair 3-wise independent signs coupled to iid non-atomic positive amplitudes in \([a,b]\) with \(b<2a\), the sole fourth-order sign coefficient \(\theta\) determines strong four-step persistence exactly as \((35-5\theta)/128\); in particular the two parity-conditioned exchangeable continuous models have every proper subset iid but persistence \(15/64\) and \(5/16\).

## Correctness — PASS

Fair 3-wise independence annihilates every nonconstant Walsh coefficient of degree at most three, leaving exactly the degree-four coefficient \(\theta\), so the sign mass function is \(2^{-4}(1+\theta\prod_i e_i)\). Under positive- and negative-parity conditioning, \(b<2a\) fixes the sign of every two-positive/one-negative three-step sum; the only remaining comparisons are between iid continuous quantities and therefore have probabilities \(1/2\) or \(3/8\). Summing the four positive-first patterns gives \(15/64\) and \(5/16\), hence the affine formula. The exact verifier confirms every proper sign marginal is uniform and independently reproduces these rational values; the analytic pattern argument establishes the theorem.

Checked sources:
- Sparre Andersen, On the fluctuations of sums of random variables (1953) and On sums of symmetrically dependent random variables (1953).
- Benjamini, Kozma and Romik, Random walks with k-wise independent increments, ECP 11 (2006).
- Narayanan, Three-wise independent random walks can be slightly unbounded, RSA 61 (2022), accessible full article page inspected.
- Berger and Béthencourt, An application of Sparre Andersen’s fluctuation theorem for exchangeable and sign-invariant random variables, arXiv:2304.09031.
- Iľkovič and Yan, Extremal persistence probabilities of exchangeable sign-invariant random variables, arXiv:2609.05586.
- Published finding dated 2026-09-20 on pure n-way dependence and Student t size, inspected through Resultary.
- Assigned exact verifier and independent rational replay.

Residual risks:
- None.

## Originality — PASS

Best-of-knowledge originality passes for the exact persistence response and proper-marginal indistinguishability statement. Limited-independence parity constructions and anomalous path statistics are known, and a 2026-09-20 published finding uses the same pure n-way dependence mechanism for Student t size, but that different statistic does not imply the four-step persistence coefficients. Berger--Béthencourt require global sign invariance, precisely the property the parity-tilted models violate.

### Equivalent formulations

Searches:
- Resultary query: four-step Sparre Andersen persistence 3-wise independent signs fourth-order interaction parity conditioning proper-subset marginals
- Searches of limited-independence random walks and exchangeable sign-invariant persistence

Evidence:
- The assigned record was the only exact persistence hit.
- A 2026-09-20 finding applies pure n-way dependence to Student t size, showing the dependence gadget is prior but not this path probability.

Reasoning: Equivalent formulations are the projection of the persistence indicator onto the sole degree-four Walsh character and failure of proper-subset laws to determine persistence.

### Broader coverage

Searches:
- Berger--Béthencourt arXiv:2304.09031
- Narayanan 2022
- Benjamini--Kozma--Romik 2006

Evidence:
- Berger--Béthencourt prove Sparre-Andersen persistence under exchangeability plus global sign invariance.
- Narayanan and Benjamini--Kozma--Romik show limited independence can change maxima or long-run behavior, not this exact four-step persistence law.

Reasoning: The prior results are broader in horizon or model but do not dominate the audited finite response because the crucial global symmetry hypothesis is absent.

### Exact database or table

Searches:
- Resultary exact-topic query
- Exact verifier for the two parity classes

Evidence:
- No prior exact table of \(15/64\), \(5/16\), or the coefficient \(-5/128\) was located.
- The verifier is used only for correctness, not as proof of novelty.

Reasoning: This finite invariant is motivated by the universality boundary; no known table mechanically supplies it.

### Claim versus prior implication

Searches:
- Berger--Béthencourt theorem versus parity-tilted model
- 2026-09-20 Student-t pure-interaction finding

Evidence:
- The sign-invariant theorem is inapplicable because a nonzero degree-four parity tilt is not invariant under arbitrary coordinate sign flips.
- The Student-t calculation concerns a different statistic even though it uses the same dependence family.

Reasoning: Neither result implies the stated persistence formula; the current calculation identifies the exact missing fourth-order information for this event.

### Source inspections

- **An application of Sparre Andersen’s fluctuation theorem for exchangeable and sign-invariant random variables** — Not covering: the audited models are exchangeable but intentionally fail global sign invariance. Material read: Primary arXiv abstract/theorem description concerning exchangeable sign-invariant vectors and persistence Method: Primary-source inspection Evidence: The source makes sign invariance an explicit hypothesis for its persistence conclusion.
- **Three-wise independent random walks can be slightly unbounded** — Shows anomalous maximal displacement under 3-wise independence, not the exact four-step persistence response. Material read: Accessible article page including abstract and references to the full result Method: Primary full-text page inspection Evidence: Its main statistic is expected maximum distance and related moment bounds.

Checked sources:
- Sparre Andersen, On the fluctuations of sums of random variables (1953) and On sums of symmetrically dependent random variables (1953).
- Benjamini, Kozma and Romik, Random walks with k-wise independent increments, ECP 11 (2006).
- Narayanan, Three-wise independent random walks can be slightly unbounded, RSA 61 (2022), accessible full article page inspected.
- Berger and Béthencourt, An application of Sparre Andersen’s fluctuation theorem for exchangeable and sign-invariant random variables, arXiv:2304.09031.
- Iľkovič and Yan, Extremal persistence probabilities of exchangeable sign-invariant random variables, arXiv:2609.05586.
- Published finding dated 2026-09-20 on pure n-way dependence and Student t size, inspected through Resultary.
- Assigned exact verifier and independent rational replay.

Residual risks:
- Older dependent-fluctuation literature is broad, and an equivalent four-step calculation under different terminology remains a best-of-knowledge risk.
- The theorem is finite-horizon and assumes the independent sign-amplitude representation with \(b<2a\).

## Scientific value — PASS

The theorem gives a sharp finite-horizon information boundary for a classical persistence law: every proper subset can be exactly iid while a single invisible fourth-order coefficient moves the path probability by a fixed amount. This is a motivated counterexample/boundary result, not merely an arbitrary four-variable computation.

Checked sources:
- Sparre Andersen, On the fluctuations of sums of random variables (1953) and On sums of symmetrically dependent random variables (1953).
- Benjamini, Kozma and Romik, Random walks with k-wise independent increments, ECP 11 (2006).
- Narayanan, Three-wise independent random walks can be slightly unbounded, RSA 61 (2022), accessible full article page inspected.
- Berger and Béthencourt, An application of Sparre Andersen’s fluctuation theorem for exchangeable and sign-invariant random variables, arXiv:2304.09031.
- Iľkovič and Yan, Extremal persistence probabilities of exchangeable sign-invariant random variables, arXiv:2609.05586.
- Published finding dated 2026-09-20 on pure n-way dependence and Student t size, inspected through Resultary.
- Assigned exact verifier and independent rational replay.

Residual risks:
- Older dependent-fluctuation literature is broad, and an equivalent four-step calculation under different terminology remains a best-of-knowledge risk.
- The theorem is finite-horizon and assumes the independent sign-amplitude representation with \(b<2a\).

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
