# Independent mathematical audit

## correctness

PASS

A reset-to-reset regenerative cycle has finite mean m/p, with geometric number N of jump-labelled prior events: P(N=n)=p q^n, where T=min(J,S), q=P(J<S), p=1-q, m=ET. A length-biased current inter-event holding interval yields equilibrium elapsed B with Laplace b(s)=[1-E exp(-sT)]/(s m), independent of all prior event labels and durations; past jump-event durations U are i.i.d. T given J<S. Thus A=B+sum_(1..N)U and X=sum_(1..N) centred Gaussian jumps; summing geometric characteristic/Laplace factors proves E exp(ikX-sA)=p b(s)/[1-q h_J(s) exp(-sigma^2*k^2/2)]. At x nonzero, posterior count weights are proportional to n^-1/2 exp(-a n-r^2/(2n)), a=-log q, r=|x|/sigma. Gaussian inverse-Laplace integral plus Poisson summation gives Z_a(r)=sqrt(pi) sum_(j integer) (a+2pi*i*j)^-1/2 exp[-r sqrt(2(a+2pi*i*j))]; j=0 dominates with exponentially separated modes, yielding density p/(sigma*beta) exp(-beta*r), beta=sqrt(2a), and exact constant count corrections 1/(2a),1/(2a^2) from first two a derivatives. The conditional N CLT follows from local expansion of log Z, and conditional independent jump-duration sums give A CLT with variance mu^2/beta^3+nu/beta; equilibrium age B/sqrt(r) vanishes in probability. Exact exponential-clock transform and strict log(1+u)<u comparison follow. Independently checked nine posterior tail/mean/variance instances and 18 exact exponential joint-transform cases, not replacing infinite/asymptotic arguments.

## originality

PASS

Li–Zhang–Liu (arXiv September 2026) introduced precisely the competing-renewal-clock CTRW and derived the stationary marginal position characteristic function with Gaussian diffusion approximation; this formula and compound-geometric tails are expressly credited. The new assessed combination is exact joint position–physical-reset-age transform for arbitrary clocks, sharp conditional far-field jump-count constants/variance, and correlated bivariate rare-event clock CLT, plus strict rate-vs-diffusion calibration. Colantoni–Pagnini is a more general reset CTRW formulation in a different direction, not an exact conditioned competing-clock theorem. General compound geometric Cramér–Lundberg theory may imply part of the marginal tail, so no isolated marginal novelty is claimed. An OA original full-text version was accessible earlier in this research run; subsequent alternate arXiv HTML/PDF attempts became unavailable and Oxford authenticated retrieval reported VPN disconnected, leaving a specific full-text access risk but not automatic O failure.

## value

PASS

The jump count that realizes a rare Gaussian displacement is linear in distance rather than quadratic, and the correlated physical reset age is a distinct measurable clock. The theorem supplies sharp density/conditional-moment corrections, exact general-clock joint Laplace–Fourier transform, and rigorous bivariate fluctuations. It also shows a strict exponential rare-tail error from a common diffusion approximation, making a substantive quantitative link between renewal theory and resetting-walk physics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
