# Scientific review

## Correctness — PASS
The Markov resolvent is a positive geometric series, so row conservation and sufficiently small-scaled-step positivity follow directly. Exact two- and three-state rational formulas establish their complete minimal budgets. On directed cycles of dimension at least four, the group inverse \(K\) of \(I-P_n\) has positive one-step coefficient \((n-3)/(2n)\), which forces the negative large-step entry for every fixed even dyadic power. Uniform Fourier expansions when the power grows prove matching upper and lower half-logarithmic bounds on the minimum budget. Four-mode Fourier inversion gives the displayed critical limiting transition and a unique boundary root; its derivative and positivity arguments cover every \(q>0\). The standalone exact rational verifier passed 112 supplemental assertions; it does not replace the proof.

## Originality — PASS, conditional on available published comparisons
The closest motivating source is Blanes, Kopylov and Seydaoğlu (arXiv:2404.12789v1), whose inspected exposition provides Padé scaling and squaring and backward-error analysis, but no sign classification on directed Markov cycles. Sherlock (2021, DOI:10.1007/s00180-021-01102-6) develops a nonnegative uniformization-based matrix exponential scheme for Markov jump processes; it does not supply the computed Padé-power frontier. Recent work on rational-map high-step signs treats a single unsquared rational map; its accessible abstract does not imply the critical dyadic repeated-power limit. Related exact one-factor positivity conditions, other Padé degrees, and positivity filters do not imply the coupled \(m^2/h\) scaling or its root equation. Targeted public and mathematical-record searches found no covering statement. Residual risk: an unavailable full text or unindexed specialized result might contain an equivalent formula.

## Value — PASS
The directed-cycle generator is a minimal natural Markov benchmark with an exact strictly positive exponential, so negative numerical transition probabilities are immediately meaningful. The result identifies the sharp dimension at which *no fixed* number of Padé squarings guarantees probability positivity, quantifies how the minimum required budget grows, and yields an exact four-state phase boundary. These are qualitative numerical-reliability limits, not routine sign checks or arbitrary parameter slices.

## Closest literature and limitations
The Padé technique itself is established; so are general warnings that Crank–Nicolson is not positivity-preserving at large steps. The scope is the cyclic generator family, fixed degree-one Padé approximation, exact arithmetic, and a positivity-only budget. The asymptotic constant should not be read as a general finite-step threshold or accuracy-optimal algorithm. Primary literature may contain a not-yet-located specialized equivalent; independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
