# Scientific review: overlap-dependent super-coupon noncoverage

## Correctness

PASS. The one-round pair-inclusion count is determined by the union size; independent rounds give the exact joint noncoverage probability. Comparing it with the product of marginals gives an exact sign test. Strict increase of the hypergeometric inclusion probability with intersection proves the unique ordered sign transition. The dense-draw case is independently recovered by omitting one uniform point. A uniform falling-factorial logarithm expansion proves the square-root-scale pair ratio, and an integral mean-value identity yields the covariance scaling. All relevant parameter boundaries (feasible intersections, \(r<n\), positive round counts and noncritical asymptotic signs) are specified. The bundled checker passed 2,870 assertions but is corroborative, not a proof for all parameters.

## Originality

PASS, subject to priority risk. Athreya–Mukherjee–Mukherjee (arXiv:2304.01145, Lemma 3.1) supplies the underlying pair-inclusion count and establishes fixed-size coupon-cover limits; these are not newly claimed. The analyzed contribution is a uniform finite covariance-sign classification and a different growing-target, proportional-block square-root transition with its normalized covariance constant. Godbole–Janson (1996) concerns random covering-design thresholds and Poisson approximation, not this explicit signed two-target scaling in its accessible summary. Searches for equivalent overlap-covariance laws and comparisons with neighboring research records did not reveal equivalent coverage. It remains possible that sampling-association literature contains an equivalent, or that the result is derivable from a more general theorem not accessed here.

## Value

PASS. Pairwise dependence is an essential ingredient in second-moment and Poisson analyses of random covering designs. The classification identifies precisely when the intuitive claim that overlapping target sets have positive association fails, and explains why the crossover appears at the natural scale \(s\asymp\sqrt n\): this is where random target intersections have order-one size. The time-scaled limit quantifies the covariance relevant to observing a fixed proportion of targets. The Poisson intersection census further quantifies the global share of negatively correlated target pairs, including a majority among overlapping pairs in a natural proportional-block example. This is a structural dependency phase, rather than an arbitrary finite calculation; no unsupported downstream theorem is claimed.

## Closest literature and limits

The 2023 preprint, corresponding 2025 open-access article, and 1996 random-covering-design paper are the closest identified sources. The first source already contains the exact union inclusion probability, so novelty is not attributed to that elementary count. The older paper's full text was not available during comparison, and general sampling-theory priority is not settled. The result concerns independent rounds, two targets, and noncritical signs away from the equality curve.

Self-review: passed. Independent audit: not yet performed.
