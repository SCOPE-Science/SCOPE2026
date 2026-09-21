# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The central identity is an algebraic rewriting of the standard equilibrium alternating-renewal covariance transform. For a stationary \(\{0,1\}\)-valued alternating renewal process with finite positive state-specific means, the transform is
\[
\widetilde C(s)=\frac{p(1-p)}s-\frac{1}{M s^2}\frac{(1-\phi_0)(1-\phi_1)}{1-\phi_0\phi_1}.
\]
Introducing \(r_i=\phi_i/(1-\phi_i)\) gives the exact factor \((1+r_0+r_1)^{-1}\). Strictly positive sojourns imply \(\phi_i(s)\to0\) as \(s\to\infty\), so the high-Laplace-frequency limit identifies \(M\); the stationary mean identifies the two state-specific means.

The explicit construction was checked symbolically. An Erlang-2 state-1 law with rate \(2a\) has renewal transform \(a/s-a/(s+4a)\). The proposed state-0 law has renewal transform \(b/s+a/(s+4a)\), so the sum is exactly \((a+b)/s\), the same as the exponential/exponential Markov model. Its rational Laplace transform has two positive poles and positive mixture weights because \(a+b\) lies strictly between the two positive denominator roots. Hence it is a genuine hyperexponential distribution, not a signed representation. Both means match those of the Markov comparator.

The stationary binary two-time joint law is determined by the one-time success probability and covariance, so matching both gives equality of every two-time transition table at every lag. The alternative is nevertheless non-Markov because the Erlang-2 state-1 exit hazard depends on elapsed age.

Limiting and edge cases were examined. The construction remains valid for arbitrary \(a,b>0\), including strongly asymmetric rates. No heavy-tail, atom-at-zero, or infinite-moment pathology is used.

## Originality

PASS, with a narrow claim. The equilibrium covariance transform itself is not new and is explicitly present in Akimoto (2023), Eq. (151), with classical antecedents in alternating-renewal theory. Work on random telegraph spectra likewise studies the forward map from waiting-time laws to correlation or spectral behavior. Duffy, King and Malone (2007) document ambiguity of much coarser long-range-dependence summaries for on/off models, which is related context but does not give equality of the entire two-time law.

The checked searches covered alternating-renewal autocorrelation/covariance, random-telegraph spectra, semi-Markov transition probabilities, identifiability, Markov versus non-Markov diagnostics, Erlang and hyperexponential holding times, and equivalent “same transition probabilities” terminology. No source located the exact inverse reduction to \(r_0+r_1\), the resulting observational-equivalence class, or the explicit phase-type construction that reproduces every two-state Markov two-time law while remaining non-Markov.

Akimoto (2023) was inspected at theorem/formula level through its open arXiv HTML. Dewanji and Kalbfleisch (1987) was available at abstract level and concerns estimation from windowed trajectories, a richer observation regime. Duffy, King and Malone (2007) was checked through bibliographic/abstract sources; its contribution concerns critical-exponent and wavelet ambiguity rather than exact all-lag pair-law aliasing. Older specialized reliability, ion-channel, random-telegraph, or semi-Markov literature could contain an equivalent inverse statement under different language, which remains the main originality risk.

## Value

PASS. The result gives an exact information boundary for a standard stochastic model. It shows that an exponential autocovariance, Lorentzian spectrum, or even the entire family of stationary two-time transition matrices cannot validate a Markov assumption within the alternating-renewal class. The counterexample is explicit, smooth, finite-dimensional phase-type, and works for every pair of Markov switching rates, so it is substantially stronger than a single exceptional parameter choice or a heavy-tail ambiguity.

The transform decomposition also explains what second-order data do identify and gives immediate positive identification results when one sojourn law is known or when the two laws are constrained to coincide.

## Limitations

The result is restricted to stationary two-state alternating renewal processes with independent positive sojourns and finite means. Full trajectory data, observed holding times, higher-order distributions, or age-conditioned transitions can distinguish the models. No claim is made for dependent successive sojourns, hidden observation noise, nonstationary initialization, or general multistate semi-Markov processes.
