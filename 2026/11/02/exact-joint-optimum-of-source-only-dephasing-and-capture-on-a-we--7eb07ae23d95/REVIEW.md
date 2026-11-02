# Scientific review: exact weighted-star dephasing/capture optimum

## Correctness — PASS

The claim fixes the Lindblad normalization, the initial state, all rate domains and the mean-time objective. The three-dimensional invariant subspace is exact even for an arbitrarily weighted original star. The displayed integrated density solves the full reduced Poisson equation and, after embedding, the original generator equation. A Hilbert–Schmidt dissipativity argument excludes nondecaying eigenoperators in the reachable block, establishing that its trace is the true mean capture time. Two strict equality conditions yield the unique global optimum. The coherent dark state establishes the zero-noise boundary. The standalone code passes 96 unequal-coupling full-space comparisons, three finite-time comparisons, and 345 joint-optimum parameter groups. Critical computations support but do not replace the analytic proof.

## Originality — PASS on currently inspectable evidence; priority risk retained

Plenio–Huelga (2008) gives the foundational local-dephasing/Lindblad transport model, but its relevant derived results concern linear chains and finite-time or transfer-efficiency objectives, not the explicit mean-hitting-time star optimization. Kassal–Aspuru-Guzik (2012), whose model and analytical solution were read, uses homogeneous dephasing, uniform competing loss, and trapping efficiency on one-dimensional chains/circles; neither their formulas nor their limiting cases imply source-only weighted-star joint rate independence. Pepe–Pouthier–Yalouz (2023) was inspected through the model, results, and appendices: its extended stars have energy-defect branches, uniform dephasing, delocalized periphery preparation and the time to 50-percent absorption, unlike the present exact mean-time result. Semantically closest published mathematical-result records concern different mechanisms (state transfer without a sink, dephasing-bath approximation, or decoherence in entanglement). The 2004 Gaab–Bardeen work is particularly relevant; its abstract and secondary literature disclose a qualitative joint trap/coherence optimum. Its inaccessible full text may include stronger special cases, so historical priority cannot be certified. No inspected complete claim implies the exact rate formulas, and this material but unresolved access risk is explicitly retained.

## Mathematical value — PASS

The optimization addresses a motivated quantum-transport design problem: localized preparation populates a dark state without noise, while strong noise or strong trapping produces a Zeno bottleneck. A sharp, all-weight, all-network-size theorem specifies an actual optimal noise level and independent optimal capture strength; this gives a robust, falsifiable design law, not a small arbitrary parameter slice. It is distinct from a mere numerical search because both optima and the mean time are closed and globally exact.

## Remaining limitations

Full historical priority is unverified, particularly the 2004 source. Assumptions exclude additional environmental channels, initial mixed states, energy detuning, and source-independent dephasing. The original full Liouvillian has inaccessible dark states, so strict decay is asserted only on the excited preparation's invariant block.

Self-review: passed. Independent audit: not yet performed.
