# Independent audit — 2026-10-01

## Final claim

For \(u_\tau(x)=\log\Gamma(x)/\log((x^2+\tau)/(x+\tau))\) with the continuous value at \(x=1\), strict increase holds for every \(0<\tau\le212.435\), while the explicit \(x=9\) derivative obstruction occurs at a unique \(\tau_9\in(212.508612771,212.508612772)\), so the critical parameter lies in the stated interval.

## Correctness — PASS

Binet bounds give a strict explicit lower comparison for the derivative numerator on the new range. A fresh independent execution of the exact interval algorithm checked every width-\(10^{-3}\) subinterval of \([2.23,15]\) at \(\tau=212.435\); the smallest certified lower endpoint was about \(2.293\times10^{-7}\). The tail polynomial and its first derivative are negative at 15 while its second derivative stays negative, forcing the required concavity sign thereafter and hence positivity of the comparison function. The published parameter comparison propagates positivity to smaller \(\tau\). At \(x=9\), fresh directed interval evaluation gave opposite derivative signs at the two quoted endpoints, and parameter monotonicity makes the zero unique. The finite interval computation verifies exactly the compact piece it is claimed to certify; the rest is analytic.

Checked sources:
- Kupán, Márton and Szász, A result regarding monotonicity of the Gamma function, Acta Univ. Sapientiae Math. 9 (2017), complete accessible article text inspected.
- Zhao, Guo and Qi, A refinement of a double inequality for the gamma function, Publ. Math. Debrecen 80 (2012).
- NIST DLMF section 5.9 on Binet formulas.
- Resultary semantic search for the same gamma quotient and critical parameter.
- Assigned interval verifier and fresh full replay of its 0.001-width certificate.

Residual risks:
- The interval certificate is computer-assisted rather than formally proof-assistant checked.

## Originality — PASS

Best-of-knowledge originality passes. The complete 2017 primary article states numerical evidence for a transition \(\tau_0\in(212,213)\), proves only \(0<\tau\le25\), and gives the parameter-monotonicity tools used here. Resultary and targeted searches found no prior rigorous extension near 212 or a narrow certified transition bracket.

### Equivalent formulations

Searches:
- Resultary query: Gamma monotonicity critical parameter tau log Gamma quotient D_tau 212 213
- Exact quotient and 2017 DOI/title searches

Evidence:
- The assigned record was the only exact Resultary hit.
- The 2017 primary article explicitly says numerical results suggest a value in \((212,213)\) and then states Theorem 1 only for \(\tau\le25\).

Reasoning: Equivalent formulations include positivity of the quotient derivative or a critical parameter for the logarithmic gamma ratio; no prior rigorous near-212 bracket was located.

### Broader coverage

Searches:
- Kupán--Márton--Szász 2017 full text
- Zhao--Guo--Qi 2012

Evidence:
- The 2017 source covers all \(\tau\le25\) and a large-\(\tau\) counterexample, not the new certified endpoint.
- The 2012 work motivates the quotient/conjecture but predates the counterexample and transition analysis.

Reasoning: No inspected broader theorem mechanically yields the 212.435 lower certificate or the \(x=9\) upper bracket.

### Exact database or table

Searches:
- 2017 numerical transition report
- Fresh interval replay

Evidence:
- The prior \((212,213)\) location is explicitly numerical, not a rigorous interval theorem.
- The current certificate rigorously validates the lower endpoint and the explicit derivative obstruction.

Reasoning: A reported numerical interval does not cover a proof of a rigorous narrower bracket.

### Claim versus prior implication

Searches:
- 2017 Theorem 1 and Theorem 2 versus audited Binet certificate

Evidence:
- The parameter comparison theorem transfers a single new certified \(\tau\) downward but does not produce that certification.
- The audited Binet/Stirling lower bound plus interval arithmetic supplies the missing uniform positivity.

Reasoning: The new result is not a corollary of the 2017 theorem without the additional certificate and tail proof.

### Source inspections

- **A result regarding monotonicity of the Gamma function** — Does not cover the audited rigorous near-sharp bracket. Material read: Complete accessible primary article text, including the introduction, Theorem 1, parameter comparison and numerical transition statement Method: Primary full-text web inspection Evidence: It states numerical evidence for \(\tau_0\in(212,213)\) and proves strict increase only for \(0<\tau\le25\).

Checked sources:
- Kupán, Márton and Szász, A result regarding monotonicity of the Gamma function, Acta Univ. Sapientiae Math. 9 (2017), complete accessible article text inspected.
- Zhao, Guo and Qi, A refinement of a double inequality for the gamma function, Publ. Math. Debrecen 80 (2012).
- NIST DLMF section 5.9 on Binet formulas.
- Resultary semantic search for the same gamma quotient and critical parameter.
- Assigned interval verifier and fresh full replay of its 0.001-width certificate.

Residual risks:
- The exact critical parameter and the endpoint behavior at \(\tau_9\) remain open.
- Equivalent later work under substantially different notation remains a best-of-knowledge originality risk.

## Scientific value — PASS

The result converts a previously numerical transition into a rigorous bracket shorter than \(0.074\) and raises the proven monotonicity endpoint from \(25\) to \(212.435\). It is a meaningful quantitative resolution of a named special-function monotonicity problem, with a reproducible certificate for the only computational segment.

Checked sources:
- Kupán, Márton and Szász, A result regarding monotonicity of the Gamma function, Acta Univ. Sapientiae Math. 9 (2017), complete accessible article text inspected.
- Zhao, Guo and Qi, A refinement of a double inequality for the gamma function, Publ. Math. Debrecen 80 (2012).
- NIST DLMF section 5.9 on Binet formulas.
- Resultary semantic search for the same gamma quotient and critical parameter.
- Assigned interval verifier and fresh full replay of its 0.001-width certificate.

Residual risks:
- The exact critical parameter and the endpoint behavior at \(\tau_9\) remain open.
- Equivalent later work under substantially different notation remains a best-of-knowledge originality risk.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
