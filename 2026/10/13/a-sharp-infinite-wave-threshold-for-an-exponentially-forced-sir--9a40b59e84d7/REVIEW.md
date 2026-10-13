# Self-review

## Correctness — PASS

For the exact closed SIR equations with \(\beta(t)=\beta_0e^{at}\), the transformation into \((Q,P)\) was differentiated from first principles and inverted. Polynomial cancellation gives the stated conserved Hamiltonian. Strict convexity and coercivity in logarithmic coordinates give compact regular cycles; their intersection with \(Q=1\) establishes the **if-and-only-if** energy cutoff \(E>\gamma+a\) for recurring prevalence maxima. The incidence claim follows from the opposite signs of its log derivative at the two \(Q\) extrema. The complement \(a\le0\) and \(a\ge\gamma\) was checked directly, as was global positivity. The exact example has energy greater than the threshold because \(\log2<1\). `verify.py` gives reproducible exact algebraic checks. Analytic periodicity, not time-series sampling, supports infinitely many peaks.

## Originality — PASS, with documented residual risk

The first-public 2026 source arXiv:2610.05556v1 formulates log-linear transmission and a data-oriented peak-complexity program, but neither a constant log-slope, two-endpoint infinite-wave construction nor this sharp energy threshold is established there. The closest structural predecessor, Maheshwari et al.'s CoSIR SIR–LV mapping, uses a feedback-selected rate and unscaled cyclical prevalence with finite-duration susceptible depletion. The current theorem uses a prescribed exponential rate and a separate scaling of both \(S\) and \(I\), giving global geometrically damped waves. Earn–Parsons conservation geometry and Perakis et al.'s piecewise-constant epidemic-wave model also do not imply this specific result. Direct semantic scholarly-record and literature searches covered exponential-rate aliases, Hamiltonian equivalences, SIR–LV reductions, prior source IDs, and the exact two-knot claim; no dominating statement was identified. Search coverage is not a proof of universal priority, and historical unnoticed equivalents remain possible.

## Mathematical value — PASS

This is not a routine alternate parameterization of classical Lotka–Volterra: it gives a sharp initial-condition invariant separating monotone and endlessly oscillatory prevalence in a real nonautonomous SIR epidemic, proves genuine incidence peaks, classifies growth-rate boundaries, and shows that **arbitrarily many strict peaks need not require more transmission-rate knots**. It supplies a precise structural stress test motivated by peak-preserving parsimony and delineates why bare peak count is distinct from amplitude-aware statistical complexity. Peaks decay exponentially; no empirical interpretation or exact posterior complexity is claimed.

## Scientific limits and closest literature

Constant-rate SIR cannot have repeated prevalence maxima, whereas CoSIR creates LV cycles using state-dependent feedback rather than a specified exponential law. Infinite-horizon exponential contact rates are unrealistic, and the eventual peaks become arbitrarily small. The closest known SIR–LV prior is expressly credited. No independent audit or empirical validation was performed.

Self-review: passed. Independent audit: not yet performed.
