# Scientific review: dihedral two-particle wheel homology

## Correctness — PASS
The universal proof identifies the exact two-particle cubical deformation retract under the Prue–Scrimshaw subdivision criterion. The fiberwise two-cell boundary argument is integral and shows injectivity of the top differential for every wheel size, not merely a finite computation. The fixed-cell table checks orientation signs, including exchanged square factors; Hopf's trace identity and rational character equality yield the stated representation. Full modular ranks, signed chain identities, and every group-element trace were checked computationally for rim sizes 4–14. There is no inference from finitely many examples to the universal statement.

## Originality — PASS
The close wheel-specific primary source is Maciążek–Sawicki (2019), section 5.3, read directly in its full open article, including its wheel homology discussion. It proves nonequivariant homology statements and a product-cycle method but does not state or determine the complete dihedral action on first homology. Barnett–Farber (2009), Farber–Hanbury (2010), and Prue–Scrimshaw (2009) supply two-point graph-configuration and discretization theory rather than the all-wheel dihedral character. The most similar published database results concern wheel discrete-Morse complexes, wheel matching complexes, and different two-particle configuration graph families: equality of the word 'wheel' or use of a character method does not imply this specific representation. The checked prior results specify neither the three reflection traces nor both symmetry-quotient ranks. Residual risk is an unindexed equivariant reformulation, possibly deducible from an as-yet-unchecked presentation; absolute priority is not certified.

## Mathematical value — PASS
The graph-wheel family is a natural, historically studied testbed for graph braid topology and collision-free motion. Betti numbers leave all automorphism actions undetermined, yet the new exact character separates vertex-axis and edge-axis reflections when the rim is even and shows a genuine symmetry-quotient dichotomy: rank two after rotations, but rational acyclicity after full dihedral quotient. This is an all-parameter structural refinement, not a small numerical improvement or a special-case table.

## Boundaries of the finding
The result is rational, with a noncanonical module isomorphism; it does not assert a specified integral lattice, canonical cycle basis, or homotopy equivalence of the quotient to a point. The complete proof is in RESULT.md; `verification/check_wheel.py` supplies finite exact checks.

Self-review: passed. Independent audit: not yet performed.
