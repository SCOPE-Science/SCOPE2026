# Independent mathematical audit

## correctness

PASS

For two-state symmetric exchange with mass one and two strictly positive starts, insert the published coefficients alpha_1=0,alpha_2=1,beta_1=2,beta_2=0 and MPE one-step weight denominators. Solving the two-by-two transfer system yields the displayed rational imbalance recurrence, with strictly positive components for all finite h>0. Jacobian at equilibrium has a=1/(1+4h), b=-8h²/[(1+2h)(1+4h)] and dominant negative spectral root modulus rho. p(-1),p(0),p(1) show local attraction; comparing p at MPE m proves rho>m. Implicit differentiation yields stationarity quartic 32h⁴+32h³−8h²−8h−1=0; exactly one positive root by Descartes, derivative sign changes from negative to positive. Independent symbolic reconstruction, 125 exact rational two-state updates and both asymptotic series match h*=.5365660925 and rho*=.767326988. Only a local equilibrium spectral claim, not global convergence.

## originality

PASS

Izzo et al. originated this very algorithm and its embedding, positivity and order conditions. Torlo–Öffner–Ranocha analyze other Patankar stability pathologies. The optimized exact Jacobian, specific quartic critical point, strict one-step MPE comparison and stiff-limit approach to nondamping are distinct and were not found as a stronger implication of inspected source theorems. Narrow but qualified priority.

## value

PASS

A sharp positive-step optimum and arbitrarily slow large-step relaxation are directly motivated failure modes for an unconditionally positive/conservative integrator; exact threshold and comparison separate positivity from efficiency and offer a reproducible design benchmark. Not a renaming of the source positivity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
