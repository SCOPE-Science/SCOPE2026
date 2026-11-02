# Independent mathematical audit

## correctness

PASS

PASS: On grid {0,1}, exact pre-update y=(1-eta)x+eta b and floor(Ky)/K upward probability yield transition p=floor(K eta b)/K, q=ceil(K eta(1-b))/K, 0<p+q<=1 with q>0. Stationary pi1=p/(p+q) is unique and chain converges geometrically even in absorbing-zero regime. Ideal exact-probability rounding has stationary Bernoulli(b). The one-sided total-variation discrepancy b-p/(p+q) is bounded by min(1,1/(K eta)) through integer/fractional decomposition v=Keta=n+theta, vb=k+u; letting b↑1/v or b↑1 proves sharp supremum. Independent exact rational tests at K=1,4,8,16 and representative eta and 999 targets each verified all values and asymptotic approach. The bit threshold K eta→∞ follows exactly. Domain 0<eta,b<1 and K=2^r includes K=1.

## originality

PASS

StochasticA random-threshold floor scheme and one-step finite-bit bias are established prior art, along with ideal-rounding stationary laws. The exact two-state stationary minimax formula, absorption threshold and uniform eta-vs-bit criterion are not implied by finite-horizon or single-rounding error bounds in inspected predecessors. Equivalence to a known two-state quantizer Markov-chain calculation remains possible.

## value

PASS

Resource-constrained stochastic rounding on the smallest nontrivial quantization grid is a natural benchmark; an O(1/K) one-step bias becomes order-one invariant distortion if Keta stays bounded. The exact worst-target bit budget and absorption phase quantify an algorithmic effect even though they do not generalize automatically to neural nets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
