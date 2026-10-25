# Independent mathematical audit

## correctness

PASS

Superpose vertex clocks of rates p,p,q to Poisson total R=2p+q. At each event the signed edge increment has conditional expectation (q/R) tanh(alpha artanh X_n), where X_n=(W1-W2)/(S0+n). Its martingale innovation is bounded and has conditional variance 1-(q/R)^2 F_alpha(X_n)^2. For alpha<1, |F_alpha(x)|<=|x| yields X_n->0, hence drift linearization a-1 with a=alpha q/R and limiting innovation variance one. Renlund’s stochastic approximation theorems supply Gaussian, log-critical, and a.s. polynomial regimes at contraction 1-a above/equal/below 1/2; Poisson time-change gives normalized imbalance limits and independent total-mass Gaussian noise, producing joint covariance R/4[[1+v,1-v],[1-v,1+v]] with v=1/(1-2a) and correlation -a/(1-a). At a>=1/2 count noise is negligible. Alpha_c=(2p+q)/(2q)<1 iff q>2p. Read source finite verify.py: evaluates exact increment probabilities, finite dynamic programming and unreinforced binomial distributions, not infinite-time proof.

## originality

PASS

Renlund (2011) proves the broad one-dimensional stochastic-approximation fluctuation trichotomy. Qin (2026) states homogenization of network WARM, not the exact three-vertex path covariance, physical-time scaling or critical firing-rate condition. This is an explicit reduction of a distinct graph-selection system to stochastic approximation, with a computed firing-rate-driven transition; it is not a claim to general CLTs. Resultary searches found nearby urn/statistical transition records but no exact graph law. Novelty is an application-specific phase diagram best-of-knowledge rather than a new abstract stochastic theorem. Qin full text was not accessible from the attempted arXiv/OA routes; authorized institutional retrieval was safety blocked; not proof of absence, retained risk.

## value

PASS

The smallest nontrivial graph with two competing reinforced edges exhibits a non-obvious sharp rate-imbalance threshold q>2p at which fluctuation scaling changes while limiting proportions remain 1/2. The explicit negative covariance/correlation under a<1/2 and distinct logarithmic/polynomial regimes are natural uncertainty invariants for the network model, with potential use in larger-graph local linearizations. Application of a known theorem alone would not count, but the model reduction plus parameter-sharp rate transition makes this a motivated exact model result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
