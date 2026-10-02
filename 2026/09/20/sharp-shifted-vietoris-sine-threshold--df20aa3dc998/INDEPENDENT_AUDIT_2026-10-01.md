# Scientific audit — 2026-10-01

## Final claim assessed

Sharp exponent threshold and endpoint boundary layer for shifted Vietoris sine sums

## Correctness — PASS

PASS. The sufficiency is exactly Theorem 2.1 of Sangal--Swaminathan for \(lpha,eta\ge0\) and \(\lambda+\mu\ge1\). For \(s=\lambda+\mu<1\), pairing consecutive terms in the even alternating sum is an alternating Riemann-sum identity. Applied to \(u^{1-s}\), it gives the endpoint slope coefficient \(-1/2\); the shifted-coefficient correction is lower order. Applied to \(u^{-s}\sin(yu)\), whose derivative is integrable at zero for \(s<1\), the same pairing gives \(n^sS_n(\pi-y/n)	o-	frac12\sin y\). Thus every fixed \(0<y<\pi\) yields negative even partial sums for large \(n\). These are infinite asymptotic arguments, not finite experiments.

## Originality — PASS

PASS to the best of current knowledge. The complete Sangal--Swaminathan primary text was inspected. It proves positivity for the shifted-power family when \(\lambda+\mu\ge1\) and cites Belov's endpoint criterion, but contains no necessity theorem, no below-threshold failure result and no \(1/n\) boundary-layer limit. Searches in Vietoris refinements, Kwong's nonnegative-sine-polynomial work, and published mathematical records found no earlier theorem giving this exact shifted-family threshold or universal profile.

### equivalent_formulations

Searches: arXiv:1705.03759 full text; search: shifted Vietoris coefficients sharp threshold lambda plus mu necessity; Resultary: shifted Vietoris sine threshold boundary layer

Evidence: The primary theorem proves only the sufficient range \(\lambda+\mu\ge1\). No inspected source states the alternating-slope asymptotic or the scaled endpoint profile.

Reasoning: Belov's alternating criterion is an equivalent route to necessity, but applying it to this regularly varying shifted family requires the new asymptotic calculation.

### broader_coverage

Searches: arXiv:1607.08314 Kwong nonnegative sine polynomials; DOI 10.1002/mana.200810029 Vietoris refinement; Sangal--Swaminathan references on positive trigonometric sums

Evidence: The inspected broader literature treats other coefficient families or sufficient positivity refinements.

Reasoning: No inspected stronger theorem specializes to the exact shifted-power threshold and boundary-layer profile.

### exact_database_or_table

Searches: Published-record semantic search for the coefficient family and threshold; search for the asymptotic coefficient -1/2 with shifted Vietoris sums

Evidence: No exact prior theorem or data table was located.

Reasoning: This is an analytic asymptotic theorem rather than a numerical-table question.

### claim_vs_prior_implication

Searches: Sangal--Swaminathan Theorem 2.1 and Belov criterion in its preliminaries; Kwong 2016 sine-polynomial family

Evidence: The prior sufficient theorem does not imply failure below the threshold, and the general criterion alone does not supply the shifted-family asymptotics.

Reasoning: The paired alternating Riemann-sum argument supplies the missing implication and quantitative profile.

## Scientific value — PASS

PASS. The result makes the exponent hypothesis of a published Vietoris-type theorem exact and explains the failure mechanism quantitatively on the natural endpoint scale. The universal leading profile, independent of the shifts, is a structural sharpening rather than a routine parameter check.

## Source inspections

- **Vietoris type theorem related to positivity of trigonometric polynomials** — https://arxiv.org/abs/1705.03759. Material read: Complete primary text around the coefficient definition, Belov criterion, Theorem 2.1 and the sine/cosine positivity results. Assessment: PRIMARY_SOURCE_PROVES_SUFFICIENCY_ONLY. Evidence: Theorem 2.1 proves sine positivity for \(lpha,eta\ge0\) and \(\lambda+\mu\ge1\); no sharp converse or endpoint asymptotic is stated.
- **A New Family of Nonnegative Sine Polynomials** — https://arxiv.org/abs/1607.08314. Material read: Primary abstract and accessible manuscript material describing its different coefficient families and low-degree classifications. Assessment: RELATED_DIFFERENT_FAMILY. Evidence: The paper concerns different sine-polynomial coefficient patterns and does not state the shifted-power threshold or the claimed scaled endpoint limit.

## Limitations and residual risks

The result classifies the sine family and simultaneous sine/cosine positivity, not cosine positivity alone below the threshold. Only the leading fixed-\(y\) endpoint profile is derived. A differently phrased theorem for regularly varying coefficients remains a residual originality risk.

- A general regularly-varying-coefficient theorem could imply the converse under terminology not found in the searches.
- No claim is made about the optimal cosine-only threshold below \(s=1\).

## Disposition

**passed**
