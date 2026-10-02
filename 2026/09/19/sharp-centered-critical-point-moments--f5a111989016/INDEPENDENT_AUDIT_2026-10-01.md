# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-f5a111989016`

## Correctness — PASS

The final centered theorem follows from an exact product identity and a complete equality analysis. With \(p(z)=zq(z)\), Vieta gives \(\prod_{j=1}^{n-1}|\zeta_j|=|\prod_{k=1}^{n-1}z_k|/n\le 1/n\); AM-GM applied to \(|\zeta_j|^{-\lambda}\) gives the sharp lower bound for every \(\lambda>0\). Equality forces every nonzero zero onto the unit circle and every critical point onto the circle of radius \(n^{-1/(n-1)}\). Comparing the self-inversive coefficient relations of \(q\) and the rescaled derivative leaves only the endpoint coefficients and, exactly when \(n\) is odd, the middle coefficient. The resulting quadratic in \(z^{(n-1)/2}\) gives the stated sharp parameter interval. I independently checked the coefficient-support equation through degree twenty and the concavity argument that excludes all other supports. The radial stability estimates follow directly from the same product identity and \(x-1-\log x\ge0\).

### Correctness sources

- assigned RESULT.md
- independent symbolic coefficient-support check
- Tang Zhang, arXiv:2609.19126, accessible abstract/scope
- Hinkkanen–Kayumov 2010 and Sheil-Small geometric-polynomial background

### Correctness risks

- The theorem is centered at a distinguished zero \(0\); it does not resolve the harder noncentral Tang–Zhang range.
- No angular stability is proved.

## Originality — PASS

The current published search found no theorem implying the parity-dependent extremizer family or the all-positive-power stability theorem. Zhang's 2026 result supplies the centered quadratic lower bound but, in the material accessible in this run, not the simultaneous all-\(\lambda\) equality classification. Older equal-critical-radius literature is genuinely relevant, but the accessible secondary descriptions concern Smale-type critical-value estimates rather than classification of polynomials whose zeros are all unimodular and whose critical points all have one prescribed radius.

### equivalent_formulations

Searches:
- Resultary searches for centered reciprocal critical-point moments, equal critical radii, parity extremizers, and self-inversive equality families
- web searches for polynomials with zero constant term and all critical points of equal modulus

Evidence:
- The only exact current published match was the audited theorem.
- Older literature explicitly studies equal-critical-radius polynomials, so it was treated as a real comparison risk rather than ignored.

Reasoning:
Equivalent formulations via equality in the critical-radius product bound, simultaneous unimodularity of \(q\) and a rescaled derivative, and sparse self-inversive coefficient support were compared.

### broader_coverage

Searches:
- Tang–Zhang 2026 centered endpoint inequality
- Andrievskii–Ruscheweyh 1998 maximal-range survey
- Sheil-Small, Complex Polynomials
- Hinkkanen–Kayumov 2010

Evidence:
- The accessible older statements prove Smale-type bounds under equal critical moduli; they do not state the audited parity-dependent equality family.
- Zhang's accessible scope is a broader inequality but not a classification theorem.

Reasoning:
A stronger inequality does not mechanically imply this equality classification and radial stability package.

### exact_database_or_table

Searches:
- current Resultary polynomial-critical-point findings

Evidence:
- No exact database/table or finite classification covering these extremizers was located.

Reasoning:
The theorem is an infinite structural classification, not a table lookup.

### claim_vs_prior_implication

Searches:
- claim-by-claim comparison against the accessible older equal-critical-radius results

Evidence:
- Prior results use the hypothesis of equal critical moduli to obtain normalized critical-value inequalities; the audited result instead deduces and classifies equality in a root/critical-radius moment inequality.

Reasoning:
No inspected prior theorem implies the odd-degree one-parameter family or the stated quantitative stability.

### source_inspections

- **Beyond Sendov's conjecture: the quadratic Tang–Zhang inequality** — https://arxiv.org/abs/2609.19126. Trigger: Direct motivating source for the centered endpoint inequality. Material read: Abstract and bibliographic scope material; full text was not available for inspection. Method: Primary-source scope comparison. Assessment: Relevant but not decisive coverage; inability to inspect the full paper is recorded as a residual risk. Evidence: The accessible material advertises the global quadratic inequality rather than this centered all-power equality classification.
- **Complex Polynomials and Maximal Ranges: Background and Applications** — https://doi.org/10.1007/978-94-015-9086-0_3. Trigger: Older literature specifically cited for equal-critical-radius polynomials. Material read: Bibliographic and abstract material plus later secondary summaries; full text was not available for inspection. Method: Older-primary-source comparison with explicit access limitation. Assessment: Plausible overlap risk, but available descriptions concern maximal-range/Smale inequalities and do not establish coverage of the audited classification. Evidence: A 2017 survey slide deck lists equal-critical-radius polynomials as a class for which Smale's mean-value conjecture is known.
- **Smale's problem for critical points on certain two rays** — https://doi.org/10.1017/S1446788710000030. Trigger: Accessible primary context citing Sheil-Small's equal-critical-modulus theorem. Material read: Full accessible PDF passages discussing equal-modulus critical points. Method: Primary-literature implication comparison. Assessment: Not covering the audited equality classification. Evidence: It cites equal-critical-modulus hypotheses to derive Smale-type bounds, not the parity family here.

### checked_sources

- current Resultary centered-critical-point searches
- Tang Zhang arXiv:2609.19126
- Andrievskii–Ruscheweyh 1998 bibliographic record
- Hinkkanen–Kayumov 2010 full-text passage
- assigned RESULT.md

### residual_risks

- The full Tang–Zhang paper and the 1998 maximal-range chapter were not both available in full; a differently phrased historical classification could therefore still exist.
- Very recent concurrent work remains possible.

## Scientific value — PASS

The theorem gives the sharp value for every positive reciprocal moment, a complete extremizer classification with a genuine parity bifurcation, and quantitative radial stability. This is a natural exact boundary attached to a recent critical-point inequality, not an arbitrary finite slice or a parameter renaming.

### Value sources

- Tang–Zhang centered critical-point inequality
- assigned equality/stability theorem

### Value risks

- The contribution is deliberately centered and does not settle noncentral Sendov-type cases.

## Limitations

- Only the centered distinguished-zero setting is covered.
- The stability statement is radial, not angular.
- Originality is best-of-knowledge because two older/full primary sources could not both be inspected completely.

## Disposition

**PASSED**
