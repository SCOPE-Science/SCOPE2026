# Independent mathematical audit

## correctness

PASS

For scalar unit rows normalize e=1 and let J~Bin(D,beta), k=max(1,floor(qD)). If update clean, J<k forces Q>=1 and acceptance (error zero), whereas J>=k permits Q=0 and rejection (error one). If update corrupted and J<=D-k, at least k calibration residuals equal one, hence Q<=1 and accepted |v0|<=2, sharp at v0=2 with ties; if J>D-k, v0=B and corrupted calibration residual B-1 attain B². Joint indicator-adapted selections achieve both extrema, giving R=(1-beta)Pr(J>=k)+4beta+beta(B²-4)Pr(J>D-k). R>=4beta, and for beta<1/4 any beta<q<1-beta gives both tails vanishing with D, proving the quarter boundary. Strict binomial-upper-tail bounds uniformly Theta(D^-1/2 exp(-D KL(1-q||beta))) and first-crossing logarithmic inversion yield (2/I)ln B -(1/(2I))ln ln B+O(1) without assuming monotone risk in D. No finite D controls all unbounded B. Independently checked 420 conditional finite-grid cases and exact ties; these are not proof of the asymptotic.

## originality

PASS

The exact unconditional scalar finite-D minimax functional, sharp beta=1/4 contraction boundary, and two-term B-dependent batch size were not supplied by the inspected high-probability streaming or finite-sample quantile-Kaczmarz papers. Corruption catastrophe itself and the streaming rule are explicitly prior art.

## value

PASS

A natural exact worst-case design question for a published stochastic projection update: gives practical analytic calibration bounds and a sharp feasibility threshold while explaining why excluded rare batches undermine unconditional risk. This is not a mere restatement of high-probability convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
