# Independent mathematical audit

## correctness

PASS

The transform follows by applying the driftless harmonic-oscillator semigroup to exp(ν·), times exp(−νa−ν²S/2), and doing its Gaussian integral. In inversion the exponent with extensive derivatives is λy−S√(2λ)/2+ν²/(2√(2λ)); stationarity and its positive real second derivative give exactly ℓ_S and S v_S. The leading transform replacement is uniform on the contour: |g|≤√2 Re g and the tanh error is O(exp(−2S Re g)), which absorbs the unbounded |g| multiplier; the sech term is bounded with ν²=O(S). After normalization the absolute contour integrand is bounded by a constant times exp[−S(Re g−g_S)/2], with a quadratic gap locally and sqrt(|u|) growth at infinity. Thus the local Gaussian integral gives the factor √2/(ℓ_S√(2πSv_S)), not just an exponential rate. For a fixed prefix, changing S and y by fixed amounts leaves a bounded first-derivative mismatch at the old saddle and does not change the leading Gaussian prefactor. Keeping the exact exponent change cancels both drift terms in the prefix Girsanov density. The limiting OU exponential is a true martingale on every bounded window: the explicit Itô form is bounded above there by exp[γ(t+x²)/2]. Scheffé gives path-space TV on that window. The positive saddle is unique, varies continuously with μ_T²/T and tends to 1/(2θ) when c=0. Local weak convergence on infinite path space is interpreted with extensions beyond T, e.g. constant continuation; tightness on each integer window yields tightness in the compact-open topology.

## originality

PASS

The distinct contribution is the drift-dependent critical saddle, associated sharp probability equivalent and resulting hard-budget OU limit for μ_T²/T with a positive limit. The driftless limit, the exact transform, and local ensemble equivalence methods are prior ingredients. The exact same-model prior theorem has a strictly smaller drift range and explicitly asks about the critical scale. The same-day two-endpoint result overlaps the initial-window limit at fixed drift but does not cover the critical scale; no priority inference is made from date alone.

## value

PASS

This resolves the named critical-scale question for the hard budget, showing that strong imposed drift changes the local confinement rate even though the growing linear drift cancels from the limit. The sharp prefactor and controlled finite-prefix probability ratios are quantitatively useful and establish more than a formal ground-state or exponential-order argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
