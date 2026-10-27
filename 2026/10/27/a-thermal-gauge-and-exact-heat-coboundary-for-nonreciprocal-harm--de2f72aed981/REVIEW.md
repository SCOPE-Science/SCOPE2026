# Scientific assessment — thermal gauge and heat coboundary

## Correctness — PASS

The theorem is conditional on positive bidirectional graph couplings, positive-definite symmetrized stiffness, and the stated bath conditions. The pathwise identity follows from an explicit positive diagonal symmetrizer and the Stratonovich quadratic chain rule; the Itô correction is accounted for. Calibrated stationarity and ordinary velocity-reversal detailed balance follow by separating the skew-adjoint Hamiltonian generator from the self-adjoint thermostat generators. For a chain, controllability and deterministic energy dissipation imply exponential mixing. The limiting heat law follows from the difference of independently sampled stationary quadratic energies, each Gamma distributed with shape equal to the particle count. With all sites thermostatted, comparing the stationary generator adjoint to its velocity reversal proves the temperature-weighted stiffness symmetry is necessary as well as sufficient. The packaged verifier passed 591 finite tests of independent algebraic and covariance consequences; these checks do not replace the proofs.

## Originality — PASS, with residual risk

Cheng, Li and Tu (arXiv:2609.09593v1) establish the harmonic-chain model, stationary reservoir currents, nonreciprocal power, and a rank-one long-time joint heat scaled cumulant-generating function. Their results imply a zero exponential growth rate for a particular weighted heat combination, but do not explicitly provide its exact finite-time energy-coboundary, its order-one stationary Gamma-difference law or the necessary-and-sufficient network cycle obstruction for velocity-reversal detailed balance. The diagonal symmetrizer and cycle-consistency principle are classical and are not claimed as new. Loos and coauthors' two-particle nonreciprocal refrigerator and broader Langevin irreversibility papers are particularly relevant; accessible descriptions do not settle the full graph classification. Their possible coverage of a two-site special case remains a substantive residual risk. No precisely equivalent published mathematical record was identified in the searches made; failed searches alone are not treated as proof of priority.

## Value — PASS

The new result supplies an exact finite-time identity behind a previously known long-time rank-one fluctuation structure, and determines the otherwise unresolved order-one distribution of its null-current combination. The network cycle condition draws a sharp physical boundary: tree-shaped directed couplings can be thermally calibrated to reversibility, whereas nontrivial circulation around even a single graph cycle prohibits such calibration for all positive bath temperatures in fully thermostatted systems. These statements directly address observability and design of nonreciprocal heat-transport networks; they are not arbitrary parameter substitutions or a table recomputation.

## Closest literature and limitations

The principal comparison is the full accessible text of Cheng, Li and Tu, arXiv:2609.09593v1, especially their Eqs. (15)--(17), (35), (40)--(43), and Appendices A--C. Related but materially different settings include Loos et al., arXiv:2211.05502 (two-site refrigerator), Loos and Klapp, arXiv:2008.00894 (nonreciprocal Langevin irreversibility), and Netz, arXiv:2009.07544 (Hamiltonian symmetric interactions and multiple baths). Some related complete texts were inaccessible. The necessity assertion is restricted to bath coupling at every vertex and ordinary velocity reversal. The Gamma difference limit assumes an initially stationary calibrated finite chain and asymptotically independent endpoint energies.

Self-review: passed. Independent audit: not yet performed.
