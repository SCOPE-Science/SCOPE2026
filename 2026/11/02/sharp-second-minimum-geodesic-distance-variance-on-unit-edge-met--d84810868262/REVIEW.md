# Scientific review

## Correctness — PASS

The exact edge-pair integrations give \(\mathbb ED=\mathbb EX+1/(3m)\) and \(\mathbb ED^2=\mathbb EX^2+1/6\). The decomposition \(X=B+Z\), with \(B=\mathbf1_{E\ne F}\) and \(Z\ge0\), gives exactly \(\operatorname{Var}(D)-V_\star=\operatorname{Var}(Z)+4\mathbb EZ/(3m)\). For a nonstar, degree convexity forces \(p=\Pr(Z>0)\ge 2(m-2)/m^2\); basic edge-pair incidence also forces \(p\le (m-1)(m-2)/m^2<1-2(m-2)/m^2\). The conditional variance identity implies \(\operatorname{Var}(Z)\ge p(1-p)\), while \(\mathbb EZ\ge p\). Equality is unique to the once-subdivided star. No unproved computational extrapolation is needed. The included standalone program passed 19,544 exact finite tree checks, four direct shortest-route quadratures, and symbolic simplifications were separately checked.

## Originality — PASS, provisional historical priority

López de los Mozos–Mesa (2000; publicly dated electronic issue 2002-08-15) optimize variance from one *chosen facility* to a continuous-demand distribution, not variance between two independent random points. Puerto–Ricca–Scozzari (2009) optimize positions of path-shaped facilities, also a different problem. Garijo–Márquez–Silveira (2023, Proposition 4.4) prove star/path extremality for *mean* continuous distance. Prior explicit unit-tree distance laws and sharp first-moment gaps for nonstars provide strong related structure but do not give the variance-extremal claim merely by stochastic dominance: variance is not a stochastically increasing functional. The sharp conditional-variance lower bound using both incidence endpoints, and the unique second-minimum variance classification, require a new implication argument. No exact matching result was identified from the actual scientific searches. A previously unindexed equivalent extremal statement remains a priority risk. The 2009 publisher full text was not available in the inspected sources; its available abstract describes a different objective.

## Mathematical value — PASS

Variance of point-to-point travel distance measures dispersion of pairwise route lengths rather than network compactness as measured by their average. This classification finds the optimal topology and the *unique nearest competitor* across every size, with an exact positive second-place gap and an identity that measures the surplus by line-graph distance fluctuations. It answers a natural topology-optimization question and distinguishes genuine dispersion control from first-order stochastic or mean-distance control. No weighted-network or maximum-variance theorem is claimed.

## Limits and literature comparison

The equal-length assumption is essential to the edge-uniform decomposition; extending it to weighted trees is not justified. The numerical checks are finite. The first electronically day-verified historical source is 2002-08-15, while the paper's print issue is designated 2000; no more precise earlier public day was established. Relevant full text was inspected for the 2000 one-facility variance article and for the 2023 continuous mean-distance article, and an abstract was inspected for the 2009 path-facility variance work. There is no independent originality or correctness certification.

Self-review: passed. Independent audit: not yet performed.
