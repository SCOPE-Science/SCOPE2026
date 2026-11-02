# Independent mathematical audit

## correctness

PASS

The final theorem is precise for uniform random recursive trees with independent parent choices at arrivals t=2,...,n, root 1 excluded, leaf meaning outdegree zero at terminal time n, vague convergence on [0,infinity), and fixed finite ranks only. For prescribed 2<=i_1<...<i_r<=n the exact event probability is product_{j=1}^r (i_j-j)/(n-j): direct conditioning at each later arrival allows (t-1-#{i in S:i<t})/(t-1) candidate parents, which telescopes to that product. The exact joint inclusion probability is <= product_j (i_j-1)/(n-1); this follows factor by factor since (n-j)(i_j-1)-(n-1)(i_j-j)=(j-1)(n-i_j)>=0. On a fixed compact window i=1+O(sqrt(n)), for fixed r the difference between joint and product marginal probabilities is O_{r,R}(n^{-(r+1)/2}), thus summing O(n^{r/2}) subsets gives a vanishing error. The weighted marginal sums form Riemann sums approaching integral_0^infty (1-e^{-f(x)})x dx, and the joint domination bounds each factorial term by A_n^r/r!, with A_n uniformly bounded. Termwise limits therefore pass through the absolutely dominated inclusion-exclusion/Laplace series, yielding PPP(x dx). The intensity map x -> x^2/2 converts the ordered locations to unit-rate Poisson arrival times and the Gamma(k,1)/Rayleigh fixed-rank laws. The boundary cases n=2, all n-1 nonroot labels specified, and root exclusion are consistent. Independently enumerated each uniformly recursive tree for n=2..9 (40320 at n=9) and verified 510 exact subset joint probabilities against both the stated formula and a separate per-arrival avoidance product; independently checked first two bounded-window factorial moments for n=500,2000,8000,32000 tending to 1/2,1/4. Finite tests corroborate, and do not replace, the all-n symbolic proof.

## originality

PASS

A qualified best-of-knowledge finding. Specific-label outdegree laws (Kuba-Panholzer), fixed-dimensional joint degree/depth results (Lodewijks), total outdegree-profile fluctuations (Janson), and leaf-degree/total-leaf counts (Hartle-Krapivsky) do not state or imply, without substantial additional joint rare-event argument, the point process of zero-outdegree vertices with birth labels O(sqrt n), nor the full finite joint inclusion product. The materially inspected Hartle-Krapivsky manuscript treats the number of leaf neighbors per vertex, not whether a given early vertex remains childless. Resultary semantic queries found related root-degree/total-leaf covariance work but no matching oldest surviving leaf point-process theorem. Hidden historical equivalence, older joint generating functions, and incomplete access to some early full texts remain explicitly material risks; unsuccessful search is not a priority proof.

## value

PASS

The uniform random recursive tree is a standard natural stochastic model with asymptotically about n/2 leaves, but that global abundance does not predict the birth ages of the oldest surviving leaves. The result identifies the nontrivial square-root label scale and a full joint inhomogeneous Poisson rare-event process, not merely a marginal expectation: it gives all fixed ranked extremes via Gamma arrival times and an exact multivariate finite-size probability that isolates weak dependence. Such a structurally meaningful extreme-age law can serve as a reference point for the study of recursive-tree age profiles and altered attachment models; the precise scale/intensity and joint law are not mechanical consequences of total-leaf CLTs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
