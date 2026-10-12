# Assessment of one-leaf clique quantum-walk instability

## Correctness: PASS

The three-dimensional invariant block is exact, with a polynomial \(f_m(x)=x^3-(m-2)x^2-mx+(m-2)\) checked symbolically. Its three real spectral roots are separated into two bounded and one diverging branch by explicit sign changes. The marked-vertex cofactor residue yields masses converging to \((1\pm1/\sqrt5)/2\) and a vanishing high-energy weight. The reverse triangle inequality bounds the marked return discrepancy **uniformly over all times**, and the fixed positive time \(\pi/\sqrt5\) attains the sharp limit. Explicit bulk and mixed-entry decompositions bound every other core complex-amplitude discrepancy uniformly by a quantity vanishing with clique size. Independent finite numerical matrix exponentials and symbolic identities corroborate the algebra; the proof, not the samples, covers every \(m\geq3\) in its asymptotic statement.

## Originality: PASS, subject to literature risk

The two closest relevant texts have been compared by implications rather than titles. *Irrational quantum walks* (arXiv:2208.08971v1, Sections 1, 4 and 5) gives general spectral methods and supremum techniques but does not state the perturbation family, the constant, or the induced-graph comparison. *Quantum walks on join graphs* (arXiv:2312.06906v1, Sections 11–12) gives a decay bound in joins and asks what happens for general induced subgraphs. The present graph is not a join; its nonvanishing limiting defect is incompatible with extending the join decay bound to arbitrary induced subgraphs. The potentially related *Localization Without Disorder* (arXiv:2603.05643v1, Sections II–III and VII) studies **normalized** adjacency Hamiltonians on barbell and multi-clique families, and time-averaged localization, not the same unnormalized adjacency comparison. The remaining risk is a separately published equivalent one-pendant clique result or an unlocated general perturbation theorem implying it. Negative searches cannot eliminate that risk.

## Value: PASS

This is a sharp, motivated boundary to a published quantitative research question about stability of quantum walks on induced subgraphs, with the complete graph explicitly named as a case of interest. The exact positive constant, fixed witnessing time and pointwise localization of the obstruction distinguish it from an arbitrary toy graph computation. It warns against extrapolating uniformly vanishing join bounds to a far weaker induced-subgraph hypothesis. The conclusion does not require a classification of all defect graphs to be useful.

## Closest literature and limitations

The result is confined to unweighted adjacency dynamics with a single leaf attached to a distinguished clique vertex; it does not address other perturbations or Hamiltonian conventions. A previous literature treatment of the exact one-leaf limit, if identified, would supersede the originality judgment. The accompanying finite tests do not constitute an infinite proof.

Self-review: passed. Independent audit: not yet performed.
