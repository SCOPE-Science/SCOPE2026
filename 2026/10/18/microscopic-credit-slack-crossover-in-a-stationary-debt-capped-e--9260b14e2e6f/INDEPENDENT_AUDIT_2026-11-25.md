# Independent mathematical audit

## correctness

PASS

Using the donor rule as precisely specified at RESULT.md line 30, the weights obey G(k)g(k)=G(k−1). Symmetric edge weights and admissibility in both directions give detailed balance. Irreducibility follows by carrying a unit along a simple path from a positive vertex to an indebted one: relative to the initial state only the source and current carrier differ, so debt does not increase. Repeating reaches the nonnegative states, which communicate by analogous transports. Counting the negative sites and distributing debt and positive wealth gives the displayed partition function and weight q_N^b; independent enumeration at N=4,K=2,L=2 gave counts 10,40,90 and at q=3/2 slack probabilities 81/109,24/109,4/109 in increasing slack order. Near L_N the monotone adjacent-summand ratio, uniformly bounded away from one outside a band about π, concentrates the negative-site fraction at π=√r/(√r+√(1+r)): compare each outer tail to the mass across the inner half of the band, with exponentially small ratio. The adjacent debt-level loss multiplied by a_N converges uniformly on bounded a_N windows to [π/r+(1−π)/(1+r)]/κ=1/(κ√(r(1+r))). Telescoping gives the local exponential and ratio 1 on o(a_N) windows. The uniform exp(−d_N(s−1)_+) bound with a_N d_N bounded away from zero follows by combining the two summand losses; at b=1 the exact ratio N(N−1)/(K+1) diverges under a_N=o(N). Thus the local limits and scaled means follow by dominated Riemann sums at a_N and 1/h_N, and dominated geometric summation for q_N→q>1; no monotone approach of h_N to zero is needed. Analytic replay: frozen RESULT.md lines 30–77. The packaged verifier was inspected, not run; the finite enumeration does not establish the limits.

## originality

PASS

Pass for the simultaneous large-density/large-population slack theorem with the three bias scales and first moments. The exact reversible weighting, equal-rate composition count, and thermodynamic reserve law in fixed-density models are not new here. Their applicability does not include the uniform boundary asymptotic needed for these simultaneous limits.

## value

PASS

The remaining reserve is a directly meaningful stationary observable that disappears in the usual wealth-scale description. The three regimes distinguish order-a_N unused credit, the intermediate scale 1/h_N, and order-one geometric slack. The critical rate c+γ separates entropy-driven saturation from rate bias, and the first-moment control makes the result usable for comparing finite reserve utilization rather than merely reporting weak limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
