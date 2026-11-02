# Scientific review

## Correctness — PASS

The claim is proved for every integer \(n\ge2\), every \(0<\alpha\le1\), each deterministic vector in \([0,1]^n\), and all integer \(t\ge0\). Key independent steps: (i) conditional independence and identical action averages give exact pathwise disagreement damping; (ii) conditional Bernoulli variance gives the scalar inhomogeneous recurrence for \(h_t=\mathbb E[p_t(1-p_t)]\); (iii) its decaying closed form forces the bounded martingale limit to be binary, without borrowing a disputed general convergence argument; (iv) the martingale terminal conditional expectation identifies \(h_t\) as actual squared distance to terminal consensus; (v) convexity under a fixed-sum constraint proves both sharp dispersion bounds. Exact arithmetic checks reproduce 380 time slices in 80 finite-state parameter cases and 117 dispersion extremum grid profiles. Unproved by code: arbitrary real parameters and infinite time; proved analytically above.

## Originality — PASS with priority uncertainty

The 2017 initiating work specifies the general update and binary herding conclusion, includes conditional-variance identities, and treats convergence speed by simulation and a late-stage heuristic. It does not supply the two-exponential finite-time mean-square identity, pathwise deterministic disagreement-to-covariance reduction, or exact sharp fixed-mean dispersion envelope in its inspected main text and appendix. A 2020 public paper emphasizes stubborn-agent convergence and critiques the earlier proof; its reviewed portions do not give the new complete-mixing finite-time expression. The 2024 paper establishes strong convergence and moment convergence according to its public abstract, but its entire full text was not obtained, leaving the material possibility of an equivalent quantitative result. The originality assessment is best-knowledge, not an independent novelty certificate. Additional claim-level semantic comparisons were made against published related findings, including other consensus and stochastic-error models whose transition kernels and quantities do not imply this Bernoulli-herding formula.

## Value — PASS

Exact finite-horizon herding risk in a stochastic social model is a motivated quantitative gap beyond eventual convergence. The theorem simultaneously gives a calculable two-rate law, a sharp worst-case initial-polarization penalty at a fixed final outcome probability, and the covariance geometry of the whole population. Unlike an isolated small-size enumeration, the strict order and its attained extrema hold for all population sizes, learning rates and horizons. In particular the formula distinguishes slower ensemble-square convergence from previously noted pathwise late-stage decay. Applications outside the specified complete interaction are not asserted.

## Limits and remaining scientific risks

The uniform self-inclusive trust matrix is necessary to the proof's scalar closure. The existence of unpublished or uninspected equivalent results remains possible, particularly in the inaccessible full text of the 2024 article and specialized stochastic-gossip literature. No independent audit or external validation has been performed.

Self-review: passed. Independent audit: not yet performed.
