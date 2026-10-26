# Self-review

## Correctness

**PASS.** Every distribution is defined by an independent per-cycle mixture of two valid exponential couplings. The stationary renewal-reward identity isolates the probability of the same active run at both observed times and proves the entire covariance and MSD. The regenerative cumulant generating exponent is the simple analytic root of \(\mathbb E[e^{-\lambda(U+V)}\cosh(kvU)]=1\); Taylor expansion gives the fourth-cumulant rate with its exact moments. The beta-integral derivatives provide the two zeta constants, and a rational lower bound rigorously proves the positive endpoint. The affine dependence on \(\theta\) gives a unique threshold. The packaged checker reproduces all critical expansion identities and independently evaluates implicit roots (55 assertions). Risk: the asymptotic uses standard exponential renewal regularity; the proof makes the nonarithmetic and exponential-moment assumptions explicit. Finite checks do not substitute for the proof.

## Originality

**PASS on the inspected scientific scope, with explicit priority uncertainty.** Datta–Beta–Großmann 2024 provides the physically natural run/turn model and second-order transport theory, but not this paired-duration sign-reversal construction. Santra–Olsen–Gupta 2024 computes higher cumulants for switching with phase-wise independent sampled times; its product-denominator formula does not yield a within-cycle dependence law by straightforward parameter substitution. The dependent CTRW framework of Niemann–Kantz 2008 is mathematically broad, but its accessible abstract does not demonstrate the exact isocovariant opposite-sign counterexample or unique \(\theta\) boundary. This last priority comparison remains limited by inaccessible full text; no claim of database-proved novelty or independent review is made. Other compared mathematical statements address different renewal observables and do not state this construction.

## Scientific value

**PASS.** Correlated run and immobilization durations are natural for intermittent motion in structured media. The construction shows that even the *entire* second-order stationary velocity law and the exact MSD leave a physically meaningful leading non-Gaussian transport sign unidentified. The exact copula interpolation and rigorous threshold answer which dependence strengths reverse the fourth cumulant. This is stronger than a generic fourth-moment computation or a marginal waiting-time substitution; it supplies a benchmark for distinguishing transport mechanisms using higher-order observations. It does not assert a thermodynamic phase transition or finite-sample detectability.

Self-review: passed. Independent audit: not yet performed.
