# Scientific review: finite-gain leader placement on paths

## Correctness — PASS

For exactly two equally pinned nodes on an unweighted path, positive definiteness follows from the graph quadratic form and the strictly positive grounding terms. The electrical-network diagonal-inverse identity yields equation (1) of `RESULT.md`; exact Gaussian elimination independently confirms the formula in 656 rational cases. Balancing outer tails is a strict discrete convexity statement, so the reduction to separation is globally exhaustive. All other separations in orders three through ten are eliminated by thirty-one universal-in-gain quadratic sign certificates; the two exceptional phase polynomials and strict root order yield the complete ten-vertex classification and all tie cases. In the infinite family, the continuous relaxation differs from the exact integer objective by only a nonnegative parity correction, and Descartes' rule plus explicit factored differences proves the strict gain-one/gain-two reversal for every integer parameter. No part of the infinite claim rests on sampling.

## Originality — PASS, with residual historical risk

Lin, Fardad and Jovanović (arXiv:1302.0450) already define the objective and give general combinatorial optimization methods. Fitch and Leonard (arXiv:1407.1569, Theorem 3) already give the joint-centrality expression for two finite-gain noisy leaders, including illustrative path optimizers at two gains; their explicit path theorem treats the noise-free regime. Patterson, McGlohon and Dyagilev (arXiv:1412.6595) address noise-free path/ring leaders. Patterson, Yi and Zhang (arXiv:1708.06873), in their full text, give a resistance-to-ground formulation, solve noise-free path placement and noisy cycle placement, but not noisy finite-gain path placement. None of those inspected statements gives the first ten-vertex nonmonotonicity, exact all-gain thresholds, or the strict infinite-family reversal. These results are more than direct restatement of a generic optimization formula: their global discrete parameter comparisons and all-gain sign certificates require additional mathematics. An equivalent specialization in further historical literature is possible. An inaccessible 2011 conference version of the early noisy-leader work remains a limited source-access risk.

## Value — PASS

The problem has a natural control interpretation: where to place two noisy feedback leaders for minimal steady-state error as gain changes. The finding fully classifies the first nonmonotone path and all its exact ties, proves that the smallest possible path has ten vertices, and establishes gain-driven *shrinking* optimal separation for arbitrarily large paths. Thus a plausible extrapolation from previously published larger-path numerical examples, namely monotone spreading as leaders become more strongly pinned, is not universally valid. The infinite-family phenomenon and closed algebraic thresholds give structural design information, not an arbitrary table entry.

## Restrictions and unperformed validation

The result concerns unweighted paths, two equal finite pinning gains, and unit covariance. The general finite-gain optimization on all path sizes or heterogeneous gains is not classified. Exact finite computations are independent consistency checks but not substitutes for the analytical argument. Historical originality remains provisional pending independent literature evaluation.

Self-review: passed. Independent audit: not yet performed.
