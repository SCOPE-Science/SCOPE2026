# Mathematical assessment

## Correctness — PASS

For generic Gaussian objectives, graphical-zonotope normal cones correspond bijectively to acyclic orientations. A complete-bipartite orientation has a unique alternating sequence of labeled class blocks; the independent Gaussian rank measure assigns its cone the exact probability equal to the within-block permutation count divided by the total permutation count. Squaring and multiplying by the labeled-block multiplicity yields the formal factorial-series coefficient. The bound on normalized weighted positive compositions follows by merging adjacent blocks and uniformly bounding the two-block reciprocal-binomial sum. Only configurations with one large-class block survive at first asymptotic order; their exact contribution is the inverse-binomial sum. The min/max angle classifications follow by factorial convexity and run balancing. A standard-library checker independently enumerated 2,818 orientation signatures from 15 small bipartitions, compared three exact methods, and tested nine large-side coefficients. No finite check is used as a substitute for the analytic proof.

## Originality — PASS, with residual risk

The central claim is the collision probability of two independent random Euclidean objectives and its fixed-small-side asymptotic. Padrol–Pilaud–Poullot establish the family and normal fans; Iriarte's earlier result already implies the maximum-angle orientations, which are not claimed as new. Carballosa–Khera–Reyes and Cameron–Glass–Rekvényi–Schumacher enumerate the orientations without their squared normal-cone weights. Stinson–Gleich–Constantine study Gaussian normal-cone vertex sampling in general, but their inspected probability and algorithmic sections do not give the present complete-bipartite coefficient or asymptotic. Neither the relevant retrieved mathematical record summaries nor the inspected primary source sections imply the new exact and asymptotic collision law. An equivalent calculation under lonesum-matrix or weighted-linear-extension terminology may exist and remains a bibliographic risk.

## Mathematical value — PASS

The collision functional is the exact probability that repeated spherical optimization returns an already observed vertex, equivalently the order-two effective number of direction-visible vertices. The exact coefficient evaluates this statistic for every complete bipartition, while the sharp fixed-small-side limit demonstrates polynomial effective visibility in a family with exponentially many distinct vertices. This contrast is a substantive geometric sampling phenomenon and connects normal-cone geometry to randomized vertex enumeration. Its naturality is independent of the previously known maximum-angle extremizers.

## Scope of claims

The formula uses the induced Euclidean metric in the zero-sum hyperplane and applies to positive integer bipartition sizes. The asymptotic holds only when one class size remains fixed. References and risk statements do not certify global novelty. Independent mathematical verification has not taken place.

Self-review: passed. Independent audit: not yet performed.
