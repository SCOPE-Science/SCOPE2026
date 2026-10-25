# Independent mathematical audit

## correctness

PASS

For the post-draw independent-loss chain, exchangeable stationary q_k=P(A present) obeys q_k=s^k((1-k/n)q_k+(k/n)q_{k-1}). This yields exact full mass a_n=prod_{k=1}^n[1+(n/k)(s^{-k}-1)]^{-1}, s=1-c/n. With -n log s→c, continuous f_b(x)=log(1+(e^{bx}-1)/x) yields -log a_n/n→I(c) by uniform Riemann sums including x=0. The empty-start chain is monotonically dominated under common draws and per-label losses by stationarity, so P(T<=t)<=t a_n. Coupling arbitrary starts with identical randomness leaves an initial disagreement only if that label was unselected AND survived all losses, leading to TV<=n[(1-1/n)(1-c/n)]^t. An O(n^2) block reduces TV to <=a_n/2, giving conditional target probability >=a_n/2 at each endpoint, geometric upper tail and E T=exp(nI(c)+o(n)). Strict e^{cx}-1>cx yields I(c)>log(1+c). Independently solved n=3,p=1/3 stationary 8-state system, full mass 128/3105, matching product. This is a logarithmic rate, not a sharp prefactor or exponential limit law.

## originality

PASS

Cruciani–Dudeja arXiv:2602.20705 establishes the model and heuristically discusses c/n exponential mean-field scales, but not this unconditional exact I(c). Long arXiv:2605.14511 treats stationary entry for fixed loss rates and does not supply a uniform triangular-array c/n limit. Compared rare-target stationary-mass, first passage, and metastable mixing representations; only logarithmic equality of hit and inverse-mass scales is asserted, not an Exp-law equivalence. General Markov-chain tools can furnish the hitting/mixing step, and are credited; the new exact triangular stationary exponent and strict independence-gap require separate work.

## value

PASS

For the natural vanishing-loss regime singled out as metastable in the original careless coupon-collector model, this gives an unconditional explicit integral for the true exponential waiting scale and shows the independent-marginal heuristic gets the exponent wrong. The distinction is intrinsic rare-event dependency, not merely a numerical example or standard formula restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
