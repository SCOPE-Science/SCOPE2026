# Independent Audit — 2026/09/17/sharp-extendible-bernoulli-tail-bounds--829140c11a96

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c3f6e3746b89c23dd0c28b177a0800eafc4fb32b`
- Disposition: **PASSED**

## Correctness

**PASS** — De Finetti reduces the problem exactly to maximizing or minimizing E[g_{n,k}(Theta)] over probability laws on [0,1] with E Theta=p. For 2<=k<=n-1, g' has the standard beta-density form and g'' changes sign once at (k-1)/(n-1). Thus h(theta)=theta g'(theta)-g(theta) rises then falls from positive near zero to h(1)=-1, giving a unique tangent point tau. The chord from the origin to (tau,g(tau)) followed by g itself is therefore the least concave majorant, proving the stated U_{n,k}; the endpoint cases k=1,n are correct. Complementing Bernoulli variables gives the lower envelope, and convex mixtures of directing laws with the same mean fill the entire interval. The proportional-threshold limits follow from Markov plus a two-point directing law just above the threshold (and by complement for the lower bound). No algebraic or endpoint error was found.

## Originality

**PASS** — The one-moment/least-concave-majorant principle is classical, and older work studies finite exchangeable Bernoulli bounds and stochastic comparisons for mixed binomials. However, targeted searches did not locate the explicit single-tangent binomial-tail formula giving the complete marginal-mean feasible interval for infinitely extendible Bernoulli sequences, together with its strict finite-n comparison and proportional-threshold collapse. The novelty is therefore the explicit specialization/package, not the underlying moment-problem principle.

## Scientific value

**PASS** — The theorem cleanly separates finite exchangeability from infinite extendibility under exactly one marginal constraint and gives extremizers rather than only inequalities. It also shows precisely why infinite exchangeability alone does not imply mean-centered concentration at proportional thresholds. The resulting formula is simple enough to be directly reusable in reliability, exchangeable-data uncertainty, and benchmark calculations.

## Sources

- Exact bounds on the probability of at least k successes in n exchangeable Bernoulli trials as a function of correlation coefficients (Alexander Zaigraev; Serguei Kaniovski): https://doi.org/10.1016/j.spl.2010.02.023 — Sharp finite-exchangeable bounds using linear programming; not restricted to infinitely extendible binomial mixtures.
- A geometric approach to a class of optimization problems concerning exchangeable binary variables (Davide Di Cecco): https://doi.org/10.1016/j.spl.2010.11.016 — Related finite exchangeable extremal-geometry framework with marginal/correlation information.
- Stochastic comparisons of Poisson and binomial random variables with their mixtures (Neeraj Misra; Harshinder Singh; E. James Harner): https://doi.org/10.1016/j.spl.2003.07.002 — Closest older mixed-binomial comparison literature found; it studies stochastic/variability orderings rather than this exact fixed-mean tail envelope.

## Limitations

- The theorem fixes only the marginal mean; additional information on the directing measure or correlations can shrink the feasible interval.
- The exactness concerns the worst-case expectation of a tail indicator under de Finetti mixing; Chernoff-style concentration questions are different.
- Classical mixed-binomial literature is broad, so a differently phrased older equivalent remains a residual originality risk, but no concrete covering theorem was located.

GitHub was read only as evidence; no repository mutation was performed. Open-access/preprint sources were checked first. Oxford Download was not needed for this record.
