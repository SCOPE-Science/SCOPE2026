# Scientific review: four-cube two-point configuration tori

## Correctness — PASS

The graph is specified at the level of labeled vertices and edges and the configuration space uses unordered distinct particles. Barnett--Farber's deleted-product cellular model applies, since all cube-graph vertices have degree four and the shortest cycle has four edges. The included verifier independently constructs the 120, 448 and 400 cells, checks the signed cellular chain identity and all 132 torus boundaries, and certifies mod-101 boundary rank 312. The 88 torus pivot columns have an exact determinant-\(+1\) cellular minor, so the 88-dimensional kernel is exactly their integral span, not merely a rational span. The orbit and quotient assertions are verified by all 384 automorphisms and exact integer Smith forms.

## Originality — PASS, with bounded literature risk

The claim is **not** a restatement of the general deleted-product model, planar graph cycle-product theory, or a Betti-number computation. The closest identified sources [1]--[4] do not give an exact square-face torus orbit classification and index-six parity lattice for the four-dimensional hypercube graph. The planar generation results cannot be applied directly because the four-cube graph is nonplanar. Indexed comparisons against other two-particle configuration calculations on Petersen, dodecahedral and cuboctahedral graphs concern different graph inputs and do not imply this four-cube finding. An equivalent unindexed specialized computation remains the main bibliographic uncertainty; absence of a search hit alone is not treated as a proof of originality.

## Mathematical value — PASS

The index-\(64\) obstruction distinguishes the rationally full collection of symmetry-natural nonparallel square tori from an integral top-homology basis. This is a structural integral lattice phenomenon within a graph-configuration problem, where product-cycle generation can fail for nonplanar graphs; the exact effect and restoration by either parallel orbit are not consequences of elementary Euler characteristic or Betti-number bookkeeping. The face pairs are canonical cube geometric objects, not an arbitrarily selected parameter slice.

## Sources, scope, and residual risks

Barnett--Farber [1] supplies the cellular deformation-retraction framework; Farber--Hanbury [2] and Barnett's thesis [3] provide the nearest graph-configuration context; An--Knudsen [4] separates planar generation from nonplanar examples. The principal mathematical risk is not the finite enumeration, which is completely specified and replayable, but an undiscovered equivalent specialized statement. All limits are described in the finding.

Self-review: passed. Independent audit: not yet performed.
