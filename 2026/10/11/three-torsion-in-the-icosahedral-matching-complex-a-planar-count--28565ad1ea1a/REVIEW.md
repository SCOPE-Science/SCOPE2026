# Review of the icosahedral matching-complex calculation

## Correctness — PASS
The full thirty-edge icosahedral graph and all 5,887 nonempty matching simplices are independently enumerated. An explicit 2,866-pair discrete-Morse matching is acyclic on all 23,130 nonempty face incidences and has critical cells only in degrees zero, three and four. Integral gradient-path reduction gives a \(109\times45\) signed boundary matrix of rank 44 modulo three and full rank modulo two. A specified 45-row minor has exact determinant three, forcing Smith factors \(1\) (forty-four times) and \(3\) (once). Since the resulting CW three-skeleton is a wedge of 109 three-spheres, these boundary degrees classify the four-cell attachments and prove \(\bigvee^{64}S^3\vee M(\mathbb Z/3,3)\). An independently programmed simplicial mod-prime rank calculation for primes two, three and five agrees with the predicted universal-coefficient behavior.

## Originality — PASS
The closest directly relevant published universal statement is Bayer–Jelić Milutinović–Vega, *Matching Complexes of Outerplanar Graphs*, Theorem 2 (outerplanar case) and Conjecture 11 (planar extension). The twenty-one-edge outerplanar bound excludes the thirty-edge icosahedral graph, and its three-torsion contradicts the conjecture. Shareshian–Wachs prove torsion for matching complexes of complete and complete bipartite graphs, not the ordinary matching complex of this planar graph. Engström's claw-free independence-complex results apply as background but do not calculate the invariant. Searches for the icosahedral graph under its graph and line-graph descriptions uncovered no theorem covering this exact homotopy type. This is not a proof of worldwide bibliographic uniqueness; an unindexed equivalent result remains a residual risk.

## Value — PASS
This is an explicit counterexample to an identified conjecture appearing as Conjecture 11 in a relevant recent research article. It answers that article's qualitative question about torsion in matching complexes by exhibiting three-torsion for a canonical planar graph. The exact Moore-space summand and sixty-four sphere summands go strictly beyond a mod-three detection and make the obstruction reproducible.

## Limits and references
The result is limited to this graph and ordinary matching complexes; it does not identify a smallest planar counterexample. Source texts inspected include Engström arXiv:math/0512420, Shareshian–Wachs arXiv:math/0409054 and Bayer–Jelić Milutinović–Vega arXiv:2411.04601v2 (notably the actual Conjecture 11 text). Two separate standard-library Python programs are included to check the finite computations. The calculated full homotopy type still awaits independent review.

Same-model review: passed. Independent audit: not yet performed.
