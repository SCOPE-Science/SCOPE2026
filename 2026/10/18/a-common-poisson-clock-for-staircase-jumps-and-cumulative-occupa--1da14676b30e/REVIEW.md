# Scientific review: a common Poisson clock for staircase jumps and occupation

## Correctness — PASS

The exact regenerative construction uses iid uniform down-jump factors and independent exponential seeds to generate geometric waiting times. The logarithms of the down-jump factors are unit exponentials, producing a genuine rate-one Poisson clock independent of the holding-time seeds. The global waiting-time reward discrepancy is integrable and bounded uniformly by four in expectation. Exponential tail bounds bracket the completed jump count between Poisson counts at logarithmic depths \(t\pm10\log t\). Independent marks in that band and the incomplete last interval give an overall \(O_{\mathbb P}(\log t)\) error simultaneously for jump count and scaled occupation. The compound-Poisson characteristic exponent proves the bivariate Gaussian limit and its covariance matrix \(\begin{psmallmatrix}1&1\\1&2\end{psmallmatrix}\). Every step holds uniformly over all deterministic \(p_n\) satisfying \(np_n\to\infty\). The standalone checker passed 4,996 finite exact-identity/sanity assertions; finite testing is not used as proof of the limit.

## Originality — PASS (remaining priority risk)

Yoshida's arXiv:2604.22637v1 was inspected across its 11 pages. Its Theorems 1–4 address state marginals, joint survival, the marginal jump-count PGF and the marginal occupation Laplace transform; its Theorem 5 addresses martingales. The assessed claim is neither a restatement of those marginals nor the elementary running-minimum realization: it constructs a *joint* marked-Poisson coupling with an explicit logarithmic-order error, and allows a triangular jump probability tending to zero. The known scalar running-minimum CLTs and strong invariance results of Gouet (1989), Berkes–Horváth (2001), and Fahrner (2001) are specifically excluded from the novelty claim. Marginal results do not determine the off-diagonal covariance or a simultaneous coupling. Published-record searches found no explicitly equivalent bivariate coupling. Complete full-text comparison with the older articles could not be completed, which is a genuine residual priority risk rather than evidence of absence.

## Value — PASS

The joint dependence of number of downward jumps and integrated height is a natural observable for staircase dynamics. Their marginal transforms alone do not yield joint confidence regions or correlation. The construction identifies a common compound-Poisson mechanism, the nonzero asymptotic correlation \(1/\sqrt2\), and a quantitative error much smaller than the central-limit scale. It is robust even when the jump parameter vanishes, provided the effective observation horizon \(np_n\) diverges. The statement is a nontrivial joint limit with a shared probabilistic coupling, not merely a one-observable textbook CLT.

## Relevant literature and limitations

- N. Yoshida (2026), arXiv:2604.22637v1: same stochastic chain; separate finite-time transforms, no demonstrated joint marked coupling in the inspected text.
- R. Gouet (1989), DOI:10.1016/0167-7152(89)90125-9: classical sums-of-minima asymptotic theory; only abstract and bibliographic evidence available.
- I. Berkes and L. Horváth (2001), DOI:10.1016/S0304-4149(00)00056-9: scalar logarithmic averages and strong approximation; only abstract available.
- I. Fahrner (2001), DOI:10.1016/S0304-4149(00)00103-4: strong invariance principles that encompass scalar running-minimum fluctuations; complete article inaccessible in this comparison.
- S. I. Resnick, *Extremal processes and record value times*: classical extremal-process embedding and jump times; only abstract accessible.

The proof does not address \(np_n\) bounded, other jump multipliers, optimality of the logarithmic coupling error, or external independent validation. Earlier joint record-process theory could contain equivalent statements that were not accessible for full comparison.

Self-review: passed. Independent audit: not yet performed.
