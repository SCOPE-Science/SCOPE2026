# Scientific review

## Correctness — PASS

The exact finite-size moment law follows from explicit conditional pair probabilities for independently oriented edges and the Prüfer weighted-tree enumerator. The edge-inclusion identity is derived from the same enumerator by contraction and independently tested at small sizes. The difference between the strict negative random-shape covariance and positive long-path conditional covariance is evaluated algebraically. Logarithmic expansions establish the nonzero limiting correlation. A standard-library checker exhaustively enumerates every labeled orientation through seven vertices and completes 70 reproducible finite checks; no unbounded theorem relies on finite enumeration.

## Originality — PASS, with historical-priority risk

The closest inspected source results address a different statistical object: pairwise reachability on randomly oriented fixed graphs (Alm–Linusson 2009, Narayanan 2016) or source/sink counts on noncrossing trees with label-induced orientations (Okoth–Wagner 2015). The former do not give moments of global source/sink counts over a random Cayley tree, and the latter uses different tree and orientation measures. Related continuous-vertex-mark peak/trough counts also use dependent edge orientations and do not imply the present formulas. The assessed contribution is the full first/second-moment identity, strict all-size sign, fixed-shape reversal, and limiting correlation in the independent-edge random Cayley model. A general earlier bivariate orientation enumeration could still imply the result; historical priority remains provisional.

## Mathematical value — PASS

Sources and sinks are basic local counts of a directed acyclic graph. A uniform random Cayley tree with fair independent edge orientations is a canonical two-stage random DAG, so the global dependence of these counts is intrinsically motivated. The exactly signed covariance for every size contrasts sharply with positive correlations on fixed long paths, exposing a non-obvious annealed-versus-quenched shape effect. An explicit nonzero limiting correlation also gives a quantitative large-tree benchmark, not merely a moment recomputation.

## Scope and outstanding risks

The result is not asserted for independently marked and label-oriented trees, biased orientations, or arbitrary random-tree distributions. Earlier weighted orientation enumerators might implicitly cover the moment specialization. Independent mathematical validation and full historical priority certification are outstanding.

Self-review: passed. Independent audit: not yet performed.
