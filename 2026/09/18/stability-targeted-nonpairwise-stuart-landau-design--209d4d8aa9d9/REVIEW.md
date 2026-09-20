# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The source's Eqs. (8), (20), and (21) were specialized to unweighted all-to-all coupling exactly as in its coupling-design experiment. Direct symbolic differentiation gives a doubly repeated transverse synchrony exponent
\[
-3\varepsilon\cos\rho+(6\eta-9\varepsilon^2/(2a))\sin^2\rho
\]
and a circulant splay Jacobian whose nontrivial conjugate pair has real part
\[
(3/2)\varepsilon\cos\rho+6\eta\sin^2\rho+(9\varepsilon^2/(8a))\cos2\rho.
\]
The symbolic artifact independently reconstructs these identities from the phase vector field.

Expanding the two marginality equations with \(\eta=\kappa\varepsilon^2/a\) gives boundary shifts \((3/2-2\kappa)\varepsilon/a\) and \((4\kappa-3/4)\varepsilon/a\). Their difference vanishes at \(\kappa=3/8\). Eliminating \(\eta\) without expansion yields the exact quadratic \(2\varepsilon x^2-4ax-3\varepsilon=0\), and back-substitution verifies the stated \(x_*\) and \(\eta_*\). Numerical substitutions for \(\varepsilon/a=0.05,0.1,0.15\) agree with the asymptotic expansion and exact residuals simplify to zero.

The review explicitly distinguishes local linear-stability boundaries in the second-order phase model from global basin boundaries in the full Stuart-Landau system. No claim is made that higher-order remainders vanish or that other attractors are absent.

## Originality

The source paper explicitly introduces the engineered PN motifs, chooses \(\eta=\varepsilon^2/(4a)\) to cancel the asymmetric EN harmonic exactly and half the symmetric EN harmonic, and numerically observes that the physical-system stability boundaries move toward the first-order transition. It does not derive the synchrony/splay Jacobians of the engineered second-order model, the coefficient \(3/8\), the one-knob obstruction for keeping both boundaries individually at \(\pi/2\), or the exact finite-\(\varepsilon\) simultaneous-marginality formula.

Prior work already establishes that second-order phase reduction of Stuart-Landau networks produces nonpairwise interactions and analyzes synchrony/splay stability, and broader higher-order phase-oscillator literature analyzes how nonpairwise terms alter synchronized and twisted-state stability. Those general ingredients are not claimed as new here. Searches using the exact arXiv identifier and title together with `stability`, `synchrony`, `splay`, `3/8`, `coupling design`, `bistability`, and synonymous higher-order/nonpairwise terminology did not locate a source-specific correction, comment, or prior statement of the stability-targeted coefficient or exact balanced strength.

The principal residual originality risk is the very recent status of arXiv:2609.20632v1: author notes, talks, or unindexed material may contain the same stability calculation. No specifically identified inaccessible paper was found whose known statement closely matches the source-specific result. Originality is therefore only to the best of our knowledge.

## Value

The source's coupling design is motivated by recovering first-order Kuramoto-like behavior at finite coupling. The new calculation directly optimizes the local stability signature used in that phase-diagram comparison. It shows analytically that the source's harmonic-cancellation scaling reduces the leading synchrony-splay overlap by a factor of three relative to no engineered PN, but does not eliminate it; a different coefficient eliminates the leading overlap, and an exact finite-coupling correction does so inside the second-order reduced model. This separates two natural engineering objectives that are not equivalent.

## Scope and limitations

The result is confined to the three-node, unweighted, all-to-all, straight-isochrone setting of the source's design example. It is a local-stability theorem for the second-order truncated phase model, not a theorem about exact global bistability boundaries of the unreduced physical system. General network weights, independent strengths for the two PN motifs, curved isochrones, and higher-order reductions may change the optimum.
