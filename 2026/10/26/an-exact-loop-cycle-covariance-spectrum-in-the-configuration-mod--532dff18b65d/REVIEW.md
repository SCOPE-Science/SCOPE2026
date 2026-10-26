# Scientific review

## Correctness — PASS

The pairing probabilities \(1/P_r(Q)\) are exact. Removing two stubs at each vertex on a designated cycle removes precisely \(2d_v-3\) potential loop pairs; conditioning on the remaining matching establishes the mixed moment, and ordinary subtraction gives the covariance. The full-half-edge boundary is handled separately. The regular sign factor and fixed-length asymptotic coefficients follow algebraically. Independently programmed enumeration passes 549 rational comparisons for degree sequences of at most 12 half-edges (148,080 matching-cases), along with a grid of regular-degree sign assertions. Finite computation is not substituted for the general proof.

## Originality — PASS, subject to priority uncertainty

The 2004 short-cycle article concerns **simple** random regular graphs and supplies asymptotic Poisson laws, not this loop mixed moment. Janson's 2006 multigraph work analyzes loops and double edges rather than covariances with simple-vertex cycles of all lengths at least three. An earlier exact loop/parallel-pair covariance is an \(r=2\) predecessor, expressly excluded here. Targeted primary-source and scientific-record comparisons did not identify a dominating finite all-cycle result. The 1981 historical paper could not be read in full, and further literature could still establish priority.

## Mathematical value — PASS

The theorem describes a natural dependence matrix by cycle length, identifies a universal positive-to-negative degree threshold for all nonspanning cycles, and isolates a mathematically meaningful spanning-cycle exception. It derives exact arbitrary-degree corrections and the different decay scales for regular degree two and higher degrees. Neither short-cycle marginals nor asymptotic Poisson independence answers these finite-parameter sign questions.

## Closest literature and limitations

McKay–Wormald–Wysocka, *Short cycles in random regular graphs* (2004), DOI: 10.37236/1819; Janson, *The probability that a random multigraph is simple* (2006), arXiv:math/0609802v1. An earlier loop/parallel-edge-pair exact mixed-moment result is a distinct lower-length predecessor. The conclusions are restricted to uniform labeled-stub pairing multigraphs; general irregular-degree signs depend on the degree profile. The proof has not received external verification.

Self-review: passed. Independent audit: not yet performed.
