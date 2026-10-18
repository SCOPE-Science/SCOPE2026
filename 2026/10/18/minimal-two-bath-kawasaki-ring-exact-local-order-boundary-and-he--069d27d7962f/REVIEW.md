# Scientific review: minimal two-bath Kawasaki ring

## Correctness — PASS

The model has six two-up/two-down states with explicitly specified rate-one attempts per bond and acceptance factors \(p\) and \(q\) for uphill moves. The three reversal-pair probabilities are derived by detailed probability balance and checked in all six unaggregated equations. Direct substitution proves all four local correlations, the exact hot-bath energy flux and the entropy-production formula. Positivity of \(D\), strict monotonicity in hot acceptance, and the sharp sign boundary follow from elementary inequalities; the unique \(p=1\) dissipation maximum follows from the explicit derivative and two strictly opposing monotone functions. The standalone checker independently builds the microscopic generator, symbolically checks stationary identities, solves eighteen rational-rate generators, and verifies entropy production. All checks passed. No thermodynamic-limit claim is made.

## Originality — PASS with identified residual risk

Borchers, Pleimling and Zia (2014, arXiv:1411.6180) treat the two-temperature conserved Ising ring, focusing primarily on a spatially hot window, simulations and nonequilibrium ordering. The full accessible manuscript (model, results and appendices) was inspected. Borchers' 2015 dissertation, Chapter 4 §4.4 pp. 52–58, explicitly analyzes a **six-site two-hot-edge** example; it was materially inspected and is the closest source. Neither inspected text states or implies the **four-site, one-hot-edge, finite-two-bath correlation sign threshold and exact entropy-production optimum** derived here. Schmittmann and Schmüser (2002) use spin-flip rather than conserved dynamics. Renklioglu and Yalabik (2012) use a two-dimensional square-lattice geometry. The inspected primary scientific literature did not supply this formula. A previously published small-size calculation may still exist in unindexed sources, and no unsuccessful search establishes uniqueness.

## Mathematical value — PASS

The four-site half-filled ring is the smallest periodic conserved-spin model with an energy-changing swap; this minimality is proved, not merely asserted. On it, the exact local order and heat-current laws expose two physically different thresholds: strict entropy production at any unequal temperatures, but positive alignment at the heated bond only after a finite hot-to-cold contrast. The exact location of the entropy-production optimum relative to the alignment region characterizes the competition between bath driving and local ferromagnetic ordering. This is a finite-volume structural boundary and useful exact benchmark; it is not described as a phase transition or extrapolated to larger rings.

## Closest literature and limits

Primary: N. Borchers, M. Pleimling and R. K. P. Zia, *Non-equilibrium statistical mechanics of a two-temperature Ising ring with conserved dynamics*, Phys. Rev. E 90, 062113 (2014), arXiv:1411.6180. Closest extended work: N. J. Borchers (2015) thesis, Chapter 4 §4.4, six-site analysis. Comparators: B. Schmittmann and F. Schmüser (2002), spin-flip chain, and B. Renklioglu and M. C. Yalabik (2012), two-dimensional Kawasaki lattices. The model and general phenomenon are prior knowledge. The finite four-site algebraic classification is what is assessed here. Restricted geometry, positive cold temperature, no larger-ring inference, and incomplete bibliographic coverage remain limitations.

Self-review: passed. Independent audit: not yet performed.
