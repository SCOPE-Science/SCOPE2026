# Self-review

## Correctness — PASS
For any fixed target family, project the Johnson walk to membership in their finite union. The exact projected transition rates and stationary masses give an entrance/exit flux of \(k\binom{r-1}{s-1}/\binom ns+O(n^{-s-1})\). The pure-deletion limiting chain has a simple eigenvalue one and uniformly separated residual spectrum. Reversibility, a Rayleigh bound, and the bounded inverse of \(I-P\) on zero-mass rows control the quasistationary eigenvector. Its correction to the entrance flux is \(O(n^{-s-1})\). Spectral survival asymptotics are uniform across fixed-size intersection patterns and yield Poisson factorial moments, a Gumbel cover-time limit, and a first-order expectation bound. The supporting checker passed 556 exact and numerical assertions; it does not certify the infinite limit.

## Originality — PASS, with explicit priority risk
The directly motivating arXiv:2304.01145 (2023) states the fixed-parameter Markovian cover-time estimate as Conjecture 2.4, establishes the diagonal case, and gives a Gumbel law for independently sampled rounds. The present theorem gives the strict case with exact constant, stronger missed-target Poisson law and centered Gumbel limit. Earlier independent covering-design work does not cover dependent Johnson transitions. Searches across published records and primary literature identified no explicit stronger Johnson-shadow theorem. General hitting-time techniques are relevant but were not found stated in a form that supplies the overlap-uniform rate without this proof. An implicit earlier solution cannot be excluded.

## Mathematical value — PASS
This settles a natural, explicitly posed asymptotic conjecture across every fixed pair \(1\le s<r\), and determines the full limiting distribution, including the effect of clusters of revisits. The main added mathematical obstacle is dependence between the blocks and overlap between different target shadows, both addressed by a finite forbidden-chain spectral argument rather than independence assumptions.

## Verification scope and risks
The argument assumes stationary initialization, fixed parameters and arbitrarily large ground sets. A finite checker verifies small-chain projected probabilities, full-walk comparisons and eigenvalue asymptotics, but does not prove the limits. No quantitative error or growing-parameter theorem is claimed. Independent mathematical review and absolute literature-priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
