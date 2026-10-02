# Independent audit — 2026-10-01

## Final claim

Exact Bernoulli tail envelopes under infinite exchangeability

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

De Finetti reduces the tail probability to \(\mathbb E g_{n,k}(\Theta)\) with \(\mathbb E\Theta=p\). For \(2\le k\le n-1\), \(g''\) changes sign exactly at \((k-1)/(n-1)\), and \(h(\theta)=\theta g'(\theta)-g(\theta)\) has a unique zero \(\tau\) after that point. Therefore the tangent chord from the origin to \((\tau,g(\tau))\), followed by \(g\), is precisely the least concave majorant. Jensen gives the exact upper envelope and the displayed two-point directing measures attain it; complementing successes gives the lower envelope, and mixtures fill the interval. The proportional-threshold limits follow from Markov plus a two-point directing law just above the threshold. Independent numerical recomputation reproduced \(\tau_{10,6}=0.7443883029979592\) and the upper value 0.3688182435706505; the inspected verifier also checks the majorant on a broad finite grid, but the proof does not depend on that grid.

## Originality

Finite-exchangeable sharp bounds of Zaigraev--Kaniovski and Di Cecco optimize a larger finite polytope, while mixed-binomial ordering results compare fixed and random parameters but do not state the exact fixed-mean threshold envelope located here. The audited least-concave-majorant formula, matching extremizing directing measures, two-sided interval, and proportional-threshold collapse were not found in the inspected prior sources.

### Equivalent formulations

**Searches**
- Published-record semantic search: infinitely exchangeable Bernoulli exact tail envelope least concave majorant mixed binomial fixed mean
- Web search: least concave majorant binomial tail mixed binomial fixed mean
- Web search: infinitely extendible exchangeable Bernoulli exact k-out-of-n bounds

**Evidence**
- Searches found finite-exchangeable linear-programming bounds and general mixed-binomial ordering papers, but no matching exact one-moment binomial-mixture envelope.

**Reasoning**

By de Finetti the problem is a one-moment extremal mixed-binomial problem, so mixed-binomial and k-out-of-n formulations were explicitly treated as equivalent search targets.

### Broader coverage

**Searches**
- Zaigraev and Kaniovski, Statistics & Probability Letters 80 (2010)
- Di Cecco, Statistics & Probability Letters 81 (2011)
- Misra, Singh and Harner, Statistics & Probability Letters 65 (2003)

**Evidence**
- Zaigraev--Kaniovski and Di Cecco optimize arbitrary finite exchangeable Bernoulli laws, optionally with correlation. Misra--Singh--Harner study stochastic/variability orderings for binomial variables and mixtures.

**Reasoning**

The finite-exchangeable feasible set strictly contains the infinitely extendible binomial-mixture set, and mixture ordering does not give the exact fixed-mean threshold extremum.

### Exact database or table

**Searches**
- Published-record search for exact binomial-mixture threshold envelopes
- Reliability/k-out-of-n searches for fixed-mean mixed-binomial tables

**Evidence**
- No exact table of the tangent breakpoint \(\tau_{n,k}\) or the two-sided infinitely extendible envelope was located.

**Reasoning**

The theorem supplies an analytic envelope for every \(n,k,p\), not a recomputation of a known table.

### Claim versus prior implication

**Searches**
- Direct implication comparison via de Finetti, finite exchangeability bounds, and mixed-binomial convex ordering

**Evidence**
- De Finetti reduces the feasible laws to binomial mixtures but does not by itself identify the least concave majorant. The inspected finite bounds are weaker; the ordering paper does not produce the tangent-chord optimizer.

**Reasoning**

The exact envelope requires solving the one-moment variational problem for the S-shaped binomial tail; it is not mechanically the same as the finite-exchangeable or ordering results.

### Source inspections

- **Exact bounds on the probability of at least k successes in n exchangeable Bernoulli trials as a function of correlation coefficients** — FINITE_EXCHANGEABLE_BROADER_FEASIBLE_SET. Abstract and accessible paper text describing the finite exchangeable linear-programming optimization. It optimizes arbitrary finite exchangeable Bernoulli laws, not the infinitely extendible binomial-mixture subset.

- **Stochastic comparisons of Poisson and binomial random variables with their mixtures** — RELATED_ORDERING_NOT_EXACT_ENVELOPE. PDF title page/abstract and relevant paper sections on mixed-binomial versus fixed-binomial stochastic and variability orderings. The paper studies stochastic/variability comparisons, not the fixed-mean exact threshold envelope with tangent breakpoint.

### Checked sources
- https://doi.org/10.1016/j.spl.2010.02.023
- https://doi.org/10.1016/j.spl.2010.11.016
- https://doi.org/10.1016/j.spl.2003.07.002
- Published-record semantic search

### Residual risks
- Classical moment-problem and reliability literature is broad; an older equivalent concave-envelope formulation may exist even though targeted synonymous searches did not locate one.

## Value

The result gives the exact finite-sample feasible tail interval under a natural probabilistic structural assumption and identifies precisely how the extendibility improvement disappears at proportional thresholds. Exact extremizers and the asymptotic boundary are useful for reliability and exchangeable-data analysis.

## Limitations

Only infinite exchangeability and the one-dimensional marginal mean are constrained. Additional moments or finite extendibility lead to different feasible sets. Classical mixed-binomial and one-moment extremal literature is broad, so an older equivalent formulation remains a residual originality risk despite targeted searches and comparison with the closest finite-exchangeable and mixture-ordering papers.
