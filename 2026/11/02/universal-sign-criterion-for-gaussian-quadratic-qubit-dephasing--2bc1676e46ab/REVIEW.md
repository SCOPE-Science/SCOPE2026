# Self-review

## Correctness — PASS
The trace-class Gaussian covariance representation, self-adjoint quadratic-form determinant, positive Loewner family for fixed-sign modulation, min–max eigenvalue monotonicity, and qubit dephasing-channel CP criterion jointly give the forward direction for every admissible Gaussian bath. Every sign-changing bounded modulation has a decrease in the absolute primitive; a static Gaussian witness gives a strict coherence revival, and a coupled stationary Ornstein–Uhlenbeck process with arbitrarily slow **positive** relaxation preserves it. The all-quantifier steps are analytic, not inferred from simulation. The standalone program passed 518 finite checks, with a fixed random seed and independent determinant comparison.

## Originality — PASS, subject to residual priority risk
Cai et al. (arXiv:2407.06074) explicitly analyze quadratic noise for chosen OU/telegraph processes; Cywiński (arXiv:1308.3102) investigates qubit dynamical-decoupling switching functions with quadratic Gaussian noise; Norris et al. (arXiv:1512.01575) analyze qubit non-Gaussian noise spectroscopy. Their cited physical objects, pulse-induced echo, Gaussian quadratic determinants, and fixed-bath behaviors are not new here. The evaluated distinction is a sharp **universal covariance-quantified** CP-divisibility iff for all bounded modulations, with a finite-memory mixing witness for each forbidden control. published-finding corpus and primary literature comparisons uncovered no same full claim. The strongest residual risk is that a more general mathematical or quantum-control theorem outside the inspected sources implies this classification; no publication-priority guarantee is given.

## Mathematical value — PASS
Bath-independent dephasing divisibility is a mathematically meaningful and physically motivated robustness criterion; allowing arbitrarily correlated Gaussian baths makes the control classification nontrivial. The converse remains physically pertinent because it uses mixing stationary Gaussian noise rather than infinite-memory quenched disorder. The theorem gives a full control-sign boundary and highlights why decay observed for one bath does not prove robustness for every bath.

## Scope and verification limits
Results concern classical centered quadratic Gaussian dephasing, commuting qubit dynamics and finite horizons. They do not assert multi-time process tensor Markovianity, entanglement dynamics, noise spectroscopy completeness, quantum bath back-action, or uniform decoherence for a sign-changing control in each individual covariance. Independent scientific validation and exhaustive priority search remain pending.

Self-review: passed. Independent audit: not yet performed.
