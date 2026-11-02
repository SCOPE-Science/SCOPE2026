# Scientific review

## Correctness

PASS. The coefficient table matches the five-step BDFL formula of Jensen–Ketcheson–Lóczi, Table 1. Exact symbolic division verifies the characteristic equation at the backward-Euler decay factor, giving a sole positive resonance \(r=\sqrt5\). A quartic factor is accompanied by four disjoint Rouché disks certified via rational inequalities, not root-plot guesses. A five-mode Vandermonde formula controls both the nonzero derivative of the dominant oscillatory coefficient and the subdominant remainder. Uniform four-sample cosine bounds establish infinitely many positive and negative values off resonance and the logarithmic first-negative law. The main limitations are the specified scalar problem, positive fixed timestep, particular starter, exact arithmetic and a local punctured interval.

## Originality

PASS under the accessible-literature comparison, with a meaningful priority caveat. The defining five-step method is introduced in [1], whose Table 1 and Sections 3, 5 and 6 were inspected; the displayed numerical experiments use a different starter, and the source's stiffness and absolute-stability classifications do not imply positivity of this specified initialized scalar sequence. Classical root conditions and modal decompositions explain the general machinery but neither identify the algebraic resonance nor compare the newly computed quartic roots and first-negative delay. A prior published result on backward-Euler-started BDF2 gives a different recurrence and a square-root divergence at a positivity boundary, rather than a five-step resonance with a logarithmic delay. A separate earlier analysis of the three-step BDFL causal impulse also addresses a different observable and recurrence. Historical general theorems on the excitation of parasitic roots might subsume part of the analysis; exhaustive priority is not claimed.

## Mathematical value

PASS. The result isolates a genuine conditional positivity trap in the new A- and L-stable multistep construction: an apparently perfect positive scalar run at a single step size is not robust and nearby runs delay their first sign failure for a quantifiable logarithmic number of steps. This gives a structured test for positivity diagnostics and illustrates the distinction between eigenvalue stability and properties of initialized trajectories. The algebraic cancellation is forced by the method coefficients, not an arbitrarily selected numerical threshold. The result is not a statement about the source's preferred TR-BDF2 initialization or general nonlinear systems.

## Evidence and residual uncertainty

The exact proof and supplied checker can be reviewed independently. The motivating paper is T. Jensen, D. I. Ketcheson and L. Lóczi, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1 (2026-10-15), https://arxiv.org/abs/2610.22685. Classical root conditions are discussed by Driscoll and Braun at https://fncbook.github.io/v1.0/ivp/zerostability.html. This review does not claim independent mathematical certification, historical exhaustiveness, or numerical robustness of the positive resonant orbit.

Self-review: passed. Independent audit: not yet performed.
