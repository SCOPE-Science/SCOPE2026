# The first finite-system gap between two on–off zero-range dynamics

## Finding

For the original on–off zero-range process with **three sites and two conserved particles**, and for the neighbor-gated exactly solvable modification of Hirschberg–Mukamel–Schütz, let \(c>0\) be the clock-activation rate in units where the departure rate from an active site containing \(n\) particles is \(n\). Let \(C(c)\) denote the stationary probability that the two particles occupy the same site. Both models hop uniformly to one of the other two sites and reset the destination to OFF upon arrival. The original model activates each OFF clock independently at rate \(c\). The modified model attempts clock activation at rate \(c\), accepting only if a uniformly sampled neighboring site's clock is ON.

The exact laws are
\[
C_{\mathrm{original}}(c)=\frac{(c+1)(c+2)}{3c^2+7c+3},\qquad C_{\mathrm{gated}}(c)=\frac{c+2}{3c+4}.
\]
Consequently, for every \(c>0\),
\[
C_{\mathrm{original}}(c)-C_{\mathrm{gated}}(c)
=\frac{c+2}{(3c+4)(3c^2+7c+3)}>0.
\]
The difference tends to \(1/6\) as \(c\downarrow0\) and is asymptotic to \(1/(9c^2)\) as \(c\to\infty\). This is the first possible discrepancy in site and particle count: with two sites and any positive conserved particle count, or with a single particle on any connected nearest-neighbor graph, the two dynamics agree on their accessible recurrent states.

## Assumptions and scope

There are three labelled sites on a triangle and exactly two indistinguishable particles. Each occupied ON site of occupation \(n\) emits at total rate \(n\) to a uniformly chosen distinct site. A receiving site becomes OFF, whatever its previous phase. OFF sites do not emit and independently switch ON at rate \(c>0\) in the original process. Empty sites are ON in the recurrent class. For the comparison process, an OFF clock changes to ON at rate \(c\) multiplied by the fraction of its neighboring sites that are ON (the modified clock rule of the cited 2012 work). These are continuous-time finite Markov processes. The statement is not about open reservoirs or many-site condensation in a thermodynamic limit.

## Proof

All eighteen states with occupied sites ON or OFF and empty sites ON communicate for the original model. Activation can reach a state with all clocks ON; particle hops and activations connect all occupancy patterns, and the state with two occupied OFF sites is reachable by successive arrivals at distinct occupied sites. Finite irreducibility proves uniqueness of the invariant probability.

Write \(Z=3c^2+7c+3\). The following weights are **per labelled configuration**, so that each double-occupation class has three states and each split-occupation clock class has three or six states. If both particles occupy one site, the weight is \(2(c+1)/(3Z)\) when that occupied site is OFF and \(c(c+1)/(3Z)\) when it is ON. If the particles occupy two sites, the weight is \(1/(3Z)\) when both occupied sites are OFF, \(2c/(3Z)\) when exactly one occupied site is ON (for each ordered choice of ON site), and \(2c^2/(3Z)\) when both are ON.

These weights sum to one because their combined numerator is \((c+1)(c+2)+(1+4c+2c^2)=Z\). Substitution into the generator balance at each of the eighteen states gives zero. Specifically, ON departures are at rate equal to the occupation, half directed to each other site; an arrival switches its receiver OFF; an OFF clock activates at rate \(c\). The accompanying standalone checker verifies every such equation using rational arithmetic. By uniqueness these are the stationary weights. Summing the six double-occupation states gives the first displayed expression.

For the neighbor-gated model, the published product-weight formula applies. With \(u(n)=n\), its one-site occupation weights, up to a common fugacity, are \(f(0)=1\), \(f(1)=(c+1)/c\), and \(f(2)=(c+1)(c+2)/(2c^2)\). Conditional on two particles across three sites, the total canonical weights of double and split occupations are respectively \(3f(2)\) and \(3f(1)^2\), giving \(C_{\mathrm{gated}}=(c+2)/(3c+4)\). Algebra yields the strictly positive difference above, with the stated limits.

Finally, in any process with only one particle, an OFF site must contain that particle; every neighboring site is ON, hence neighbor-gated and independent activation coincide. On a two-site system with any positive number of particles, a jump originates from an ON site and makes only its receiver OFF, so at most one OFF site occurs in the recurrent class; the other site is ON. Thus gating again changes no clock rate. Three sites and two particles are the smallest counts permitting simultaneous occupied OFF sites, exactly the mechanism responsible for the difference.

## Verification

Run `python verify_minimal.py` using the Python standard library. It constructs the eighteen-state original generator independently from the transition rules, recomputes the proposed stationary weights, and checks exact normalization and all eighteen master equations for each of 180 positive rational clock rates. It also verifies the closed clustering formula and its strict excess over the neighbor-gated canonical formula for each rate. These exact finite computations check the algebraic certificate; the proof of the all-parameter inequalities is the symbolic factorization displayed above.

## Relationship to prior work

Hirschberg, Mukamel and Schütz (2009) introduce the original clock-resetting zero-range mechanism and study many-site and mean-field condensation. Hirschberg et al. (2012), Section 5, prove a factorized stationary law for a **modified neighbor-gated clock** process and explicitly distinguish that dynamics from the original. The modified formula is used here as prior work, not claimed as new. Cavallaro, Mondragón and Harris (2015) analyze the open-boundary clocked process, including linear departure rates and exact one-site laws, but that setting does not supply the closed three-site invariant law. The new comparison is the first finite canonical witness and the exact signed all-rate gap between these two prescribed dynamics; a previously published finite-size computation could still cover it.

## Limitations

The result is specific to three sites, two particles, equal bidirectional hopping probabilities, and independent exponential clocks. It does not claim a many-site phase transition, a general inequality for more particles, or originality of the neighbor-gated product solution.

## References

1. O. Hirschberg, D. Mukamel, G. M. Schütz, *Condensation in Temporally Correlated Zero-Range Dynamics* (2009), arXiv:0906.0709, https://arxiv.org/abs/0906.0709.
2. O. Hirschberg, D. Mukamel, G. M. Schütz, *Motion of condensates in non-Markovian zero-range dynamics* (2012), arXiv:1207.1006, Section 5, https://arxiv.org/abs/1207.1006.
3. M. Cavallaro, A. Mondragón, R. J. Harris, *Temporally correlated zero-range process with open boundaries: Steady state and fluctuations* (2015), arXiv:1504.06309, https://arxiv.org/abs/1504.06309.
