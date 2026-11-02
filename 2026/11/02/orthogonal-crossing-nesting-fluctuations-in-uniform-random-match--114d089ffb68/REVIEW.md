# Scientific assessment: crossing–nesting count fluctuations

## Correctness — PASS

The independent continuous-endpoint representation gives the uniform matching law after ranking. Conditional crossing/nesting projections are \(2b(a+c)\) and \(b^2+2ac\). Exact Dirichlet moments give \(\mathbb E[p_Xp_N]=1/9\) and equal projection variances \(1/45\); the mixed independence and finite covariance follow without approximation. The canonical-kernel remainder has variance \(\binom n2 8/45\), making the multivariate i.i.d. central limit theorem applicable after scaling by \(n^{3/2}\). The extracted standalone checker passed 652 exact assertions, including all matchings through seven edges. Quantifiers cover all integers \(n\ge2\), and the \(n=1\) undefined correlation is excluded. Boundary cases and normalization have been checked.

## Originality — PASS (qualified)

The selected literature includes the 2000 marginal crossing Gaussian theorem of Flajolet–Noy, the 2005 joint distribution identities of Klazar, and the 2006 complete bivariate polynomial of Kasraoui–Zeng. **Their existing general joint generating function already determines finite moments**, so the exact covariance is not presented as new on its own. The assessed theorem adds a localized, edge-label-level mixed indicator independence law and an explicitly proved **joint bivariate Gaussian limit**. The separate maxima asymptotic independence theorem of Baik–Jenkins concerns largest crossing/nesting sets and is not equivalent. Targeted published-record and primary-text comparisons did not find these particular claims. A nontrivial derivation from historical full joint generating functions remains possible, and independent historical-priority assessment is still needed.

## Mathematical value — PASS

The result distinguishes weak correlation from a true joint Gaussian independence limit in a natural random chord diagram model, while explaining the phenomenon through exact cancellation of the first-order mixed Hoeffding projections. Simultaneous normal approximation of crossing/nesting counts is a natural inference problem; neither univariate asymptotic normality nor equidistribution alone supplies the joint limit. The indicator orthogonality is more local than the classical enumeration and resolves the mechanism, not just a single finite moment.

## Closest literature and limits

Flajolet–Noy, Section 2 Theorem 3: single crossing count; Kasraoui–Zeng, Section 4 Proposition 4.4: full bivariate enumerator; Klazar, introduction and main distribution identities: joint count identities; Chen et al., Introduction and noncrossing/non-nesting maximum discussion: maximal patterns; Baik–Jenkins, Section 1: maximal sizes and Tracy–Widom limits. A broad generating-function result can encode the finite covariance; novelty is confined to the explicit independent mixed indicators and joint CLT. No rate or independent external validation is claimed.

Self-review: passed. Independent audit: not yet performed.
