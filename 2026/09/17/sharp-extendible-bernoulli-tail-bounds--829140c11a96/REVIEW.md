# same-model review

This is a SCOPE Phase II **same-model review**, not independent validation.

## Correctness

**Verdict: PASS.**

The argument was attacked at the following points.

1. **Reduction to the right feasible class.** Infinite exchangeability of a
   Bernoulli sequence gives the de Finetti representation with a directing
   variable \(\Theta\in[0,1]\). The marginal constraint is exactly
   \(\mathbb E\Theta=p\), and the target tail is
   \(\mathbb E g_{n,k}(\Theta)\). No independence is assumed unconditionally.

2. **Shape of the binomial tail.** Direct differentiation gives
   \[
   g'_{n,k}(\theta)
   =n{n-1\choose k-1}\theta^{k-1}(1-\theta)^{n-k},
   \]
   and \(g''\) changes sign once, at \((k-1)/(n-1)\), for
   \(2\le k\le n-1\).

3. **Uniqueness of the tangent point.** For
   \(h(\theta)=\theta g'(\theta)-g(\theta)\),
   \(h'=\theta g''\), \(h>0\) just right of zero, and \(h(1)=-1\).
   Thus the post-inflection decrease crosses zero exactly once.

4. **Least-concave-majorant step.** The sign of
   \(d(g(\theta)/\theta)/d\theta\) proves the tangent chord dominates before
   \(\tau\). Tangency plus concavity of \(g\) after \(\tau\) makes the
   piecewise envelope concave. Any other concave majorant is forced above
   that chord by concavity and above \(g\) after \(\tau\), proving minimality.

5. **Attainment.** The stated two-point directing measure has mean \(p\) and
   exactly attains the linear branch. Degenerate directing measures attain
   the nonlinear branch. Complementation gives the exact lower endpoint.
   Convex mixing of whole exchangeable laws fills the interval.

6. **Finite-exchangeability comparison.** Zaigraev--Kaniovski's sharp
   marginal-only bounds were checked against the new interval. Strictness
   uses the strict form of Markov's bound for a nondegenerate binomial count
   when \(k<n\), plus complementation.

7. **Asymptotics.** The upper limit is bounded by Markov. A two-point directing
   law with a binomial parameter just above \(k_n/n\) attains the limit, using
   a Hoeffding estimate. The lower limit is the complement statement.

A standard-library numerical verifier independently recomputes representative
values and checks the majorant and discrete concavity conditions over 209
\((n,k)\) cases with 401 grid points each. The largest observed
\(g-U\) was \(1.221\times10^{-15}\), and the largest positive discrete
concavity residual was \(4.441\times10^{-16}\), both at floating-point scale.
These checks support but do not replace the analytic proof.

## Originality

**Verdict: PASS, to the best of our knowledge.**

Internal SCOPE checks immediately before publication searched the current
repository by the object and synonymous phrases including "exchangeable
Bernoulli", "de Finetti", "binomial tail", "concentration", and the exact Run
ID. No semantically overlapping successful record was located. Recent
repository changes were also inspected; repository search is not treated as a
proof of non-collision.

External searches included combinations of:

- "infinitely exchangeable Bernoulli at least k";
- "extendible exchangeable Bernoulli k-out-of-n";
- "binomial mixture fixed mean tail probability extremal";
- "mixed binomial given mean tail probability";
- "least concave majorant binomial tail";
- "concave envelope binomial tail";
- the tangent equation \(\theta g'(\theta)=g(\theta)\);
- finite/infinite exchangeability, reliability, and concentration terminology.

### Closest inspected literature

- **Zaigraev & Kaniovski (2010), DOI 10.1016/j.spl.2010.02.023.**
  The accessible theorem states the sharp marginal-only bounds
  \[
  \max\{(np-k+1)/(n-k+1),0\}\le R\le\min\{np/k,1\}
  \]
  for arbitrary finite exchangeable Bernoulli trials. This is directly
  reconciled in RESULT.md; the present theorem optimizes over the stricter
  infinitely extendible subclass.

- **Di Cecco (2011), DOI 10.1016/j.spl.2010.11.016.**
  The abstract says the 2010 marginal-only result is sharpened geometrically
  after also fixing correlation. It is close finite-exchangeability prior art,
  but the full article text was not accessible through the inspected route.

- **Misra, Singh & Harner (2003), DOI 10.1016/j.spl.2003.07.002.**
  The accessible record and inspected copy concern stochastic/variability
  comparisons between fixed and mixed binomials, including equal-mean cases.
  No exact fixed-mean threshold envelope matching the present formula was
  located.

- **Gottschling & Caprio (2026), arXiv:2603.10190.**
  Their current abstract centers exchangeable Hoeffding-style bounds at
  extremal conditional means in the support of the de Finetti mixture, rather
  than only the unconditional mean.

- **Lin, Frei & de la Peña (2026), arXiv:2606.17426.**
  Their current abstract decomposes concentration into conditional-sampling
  and latent-mixture fluctuations and controls the latter under additional
  assumptions. This is recent context for why a marginal-mean-only exact
  extremal calculation is relevant.

- **Tang (2026), DOI 10.3390/math14183291.**
  The open article develops finite/infinite weighted exchangeability and
  quantitative finite-to-mixture approximation. It does not surface the
  fixed-mean Bernoulli threshold optimization searched for here.

### Residual originality risks

The most plausible accessible gap is older mixed-binomial/moment-problem
literature. The general fact that a one-moment extremum equals a concave
envelope is standard, so an older source could have specialized it to the
binomial survival function without using exchangeability language.

The most relevant incompletely inspected source is **Di Cecco (2011)**:
only its abstract/metadata were available through the inspected route. Its
stated scope is finite exchangeability with fixed marginal and correlation;
it could contain a geometric observation useful for deriving a related
special case, although no evidence of the infinite-extendibility envelope was
found.

A second residual source is **A. Hald (1968), "The Mixed Binomial
Distribution and the Posterior Distribution of p for a Continuous Prior
Distribution," DOI 10.1111/j.2517-6161.1968.tb00736.x**. The accessible
summary describes asymptotic expansions for mixed-binomial and posterior
distributions, not fixed-mean extremal tails; the PDF text was not inspected
in this cycle.

Accordingly, originality is not claimed as certainty. The claimed
contribution is the explicit tangent envelope + exact two-sided feasible
interval + strict finite-extendibility gap + proportional-threshold collapse,
not the standard concave-envelope principle itself.

## Value

**Verdict: PASS.**

The result gives a closed structural answer to a natural robustness question
that sits directly between two active lines of work: sharp finite-exchangeable
Bernoulli bounds and concentration under infinite exchangeability. It also
isolates a useful boundary: infinite extendibility substantially restricts
finite-\(n\) tails, yet by itself does not asymptotically recover
unconditional-mean concentration. The extremizers are explicit and the
formula is directly computable.

## Access and search limitations

- The Di Cecco (2011) full text was not accessible through the inspected
  route; abstract and bibliographic records were inspected.
- The Hald (1968) publisher page exposed a summary, but the article body was
  PDF-only and was not inspected for this review.
- Search-engine coverage and GitHub code search can miss synonymous or
  unindexed formulations.
- A screenshot request for the accessible Zaigraev--Kaniovski PDF failed
  twice with a transient service error; the theorem text itself was available
  in parsed form and its exact formula was independently corroborated by
  bibliographic/search records. No conclusion was drawn from the screenshot
  failure.

## Review status

- `review_type`: `same_model_review`
- `independent`: `false`
- `independent_validation`: `false`
- `verification_state`: `same_model_reviewed`
