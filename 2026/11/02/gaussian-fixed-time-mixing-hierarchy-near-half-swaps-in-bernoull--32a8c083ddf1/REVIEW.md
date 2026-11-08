# Independent mathematical audit

## correctness

PASS

Under a swap the new red count x-U+V is the difference of independent hypergeometrics. Exact mean is n/2+lambda(x-n/2), and conditional variance 2k(n-k)x(n-x)/(n^2(n-1)). For k/n->1/2, after one step X/n->1/2 uniformly; the next hypergeometric convolution has a discrete Gaussian local limit with variance n/8. Subsequent random-centre fluctuations are |lambda|O(sqrt n)=o(sqrt n). Comparing with stationary hypergeometric variance n/8 yields the exact Gaussian TV profile 2Phi(|lambda|^t|x-n/2|/sqrt(n/2))-1 uniformly for each fixed t>=2. At t=1, x=0 gives deterministic X1=k, so TV->1; delta=k-n/2 gives the n^(1-1/(2t)) windows. Independent exact transition matrices at (n,k)=(10,5),(20,10),(40,20) gave 2-step worst TV 0.0124626167,0.0064221943,0.0030893803, confirming trend, not theorem.

## originality

PASS

A strong earlier spectral analysis of the same urn process gives half-swap mixing bounds (at least three steps), rather than the precise two-step and variable-offset Gaussian fixed-time profile. Closely related generalized-swap and unequal-urn papers give bounded-time conditions or non-half parameter regimes. The claim is not a cutoff for growing time, but sharp fixed-t TV asymptotics as lambda->0. Full source access to one neighboring 2023 preprint was incomplete, so a derived spectral reformulation remains a live historical risk.

## value

PASS

The exact TV profile resolves the two-step endpoint for half swaps, with a hierarchy of critical offsets n^(1-1/(2t)) relevant to rapid urn mixing. It improves a bounded-time/three-step guarantee and supplies quantitative finite-time sensitivity rather than a new notational variant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
