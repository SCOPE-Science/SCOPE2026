# Review

## Correctness

**PASS.** The constant test function in the weak formulation eliminates the no-flow divergence term and gives \(M'=Q-\mathcal L\). Under \(\lambda/S=\kappa\), this closes to \(M'+\kappa M=Q\), whose exact solution yields the stated transfer function. Conversely, the right initial derivative \(\mathcal L'(0^+)=Q(0)\int (\lambda/S)w\) varies with the normalized spatial profile \(w\) unless \(\lambda/S\) is almost everywhere constant. The assumptions, quantifiers, and no-flow boundary condition are explicit.

## Originality

**PASS, scoped to the iff characterization and heterogeneous-coefficient extension.** Butler and Tsou (2003) treat scale-invariant total leakage in the homogeneous Hantush–Jacob setting and use image-well arguments for representative bounded geometries. The checked full text notes that a completely general proof had not been obtained for the more complicated geometries under discussion. The present proof applies directly to heterogeneous transmissivity and to spatially varying storage and leakance when their ratio is constant, and it gives a necessity condition from the initial leakage slope. The exact transfer function for arbitrary pumping schedules is part of the same claim. The inspected Butler–Tsou full text does not state the explicit coefficient iff criterion. The Hantush–Jacob full text was not inspected, so no noncoverage conclusion is drawn from it. This remains a best-knowledge comparison, not a proof of global uniqueness.

## Value

**PASS.** Total leakage is a key water-budget quantity, yet spatial drawdown can vary strongly with geometry and transmissivity. The theorem gives an exact aggregate leakage calculation without solving the spatial field when the local leakance/storage timescale is uniform, and the converse gives a practical diagnostic: heterogeneous ratios make even the initial aggregate response depend on pump placement. The result is a natural structural classification with a clear use in groundwater budgeting, not a claim about local heads or contaminant transport.

## Closest literature and limitations

The closest source is Butler and Tsou (2003), DOI 10.1029/2002WR001484. Hantush and Jacob (1955), DOI 10.1029/TR036i001p00095, is the classical model antecedent; only its abstract and bibliographic record were inspected, so it is not used as evidence that the extension is absent there. The main residual risk is that the simple integrated conservation law or an equivalent coefficient criterion may be implicit in standard groundwater texts not located by the searches. The claim is deliberately limited to the explicit iff condition and arbitrary-schedule transfer function under the stated assumptions.

Self-review: passed. Independent audit: not yet performed.
