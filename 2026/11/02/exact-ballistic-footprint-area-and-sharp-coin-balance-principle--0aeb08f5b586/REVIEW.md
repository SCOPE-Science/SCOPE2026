# Scientific review: exact ballistic-velocity footprint

## Correctness — PASS

The theorem is about the area of the **joint asymptotic velocity spectrum**, not an initial-state-weighted probability measure. The support ellipses are taken explicitly from Asahara–Funakawa–Seki–Suzuki (arXiv:2408.09578v1, equations (14)–(19)), with their one-ellipse endpoint from section II.2. The new proof verifies the quadrant crossing, splits the area integral along the correct two arcs, evaluates both integrals and resolves the arcsine branches. Its derivative gives strict fixed-speed optimality, and elementary global inequalities prove the sharp quadratic area deficit. The endpoint expansion establishes the square-root coefficient. The attached standard-library verifier passed 6,837 tests, including independently sampled Bloch group velocities and direct numerical integration; the analysis, not the tests, proves the infinite-parameter statement. Scientific risks: none identified within the stated parameter range. No finite-time dynamics or initial-state-specific support statement is inferred.

## Originality — PASS with residual priority risk

The arXiv 2024 source and its 2025 revision establish the two-ellipse support and the maximal coordinate speed; these premises are NOT new. The revision also credits earlier single-ellipse support results and a known circle at the balanced full-speed point. The tested claim instead computes the full two-parameter area, proves its unique fixed-speed optimum, and gives an exact globally sharp imbalance stability inequality plus a singular endpoint profile. Targeted searches for those equivalents and implications found no prior full statement in the examined primary articles or research records. The 2011 Di Franco–Mc Gettrick–Machida–Busch and 2008 Watabe–Kobayashi–Katori–Konno full-text PDFs establish narrower single-ellipse support families and do not state the two-ellipse area envelope. As always, a missed result or a different geometric derivation may exist; priority is not independently certified.

## Mathematical value — PASS

The planar ballistic footprint is a natural geometric invariant of the spectrum of possible long-time propagation velocities. Maximal coordinate speed alone fixes only two one-dimensional projections, not the two-dimensional accessible region. The exact area distinguishes walks of equal maximal speed (for example, areas approximately 0.7722013 and 0.4443634 at speed 0.6), and the unique balanced optimum solves a concrete coin-parameter design problem. The sharp global quadratic stability coefficient quantifies how any imbalance reduces that footprint; the nonanalytic square-root speed-limit deficit identifies a meaningful geometric boundary layer. This is neither a renaming nor a table lookup, and its mathematical use requires no additional downstream theorem. Its significance remains confined to this walk family and to velocity-spectrum geometry.

## Sources and limitations

Primary source: K. Asahara, D. Funakawa, M. Seki, A. Suzuki, arXiv:2408.09578v1 (2024-08-18), https://arxiv.org/html/2408.09578v1 ; revised analysis arXiv:2408.09578v2 (2025-11-14), https://arxiv.org/html/2408.09578v2 . Comparators: C. Di Franco et al., arXiv:1107.4400 (2011), https://arxiv.org/pdf/1107.4400 ; K. Watabe et al., arXiv:0802.2749 (2008), https://arxiv.org/pdf/0802.2749 . The result does not optimize a probability distribution over initial states, describe finite-time spatial area, or assert priority over all unpublished or unindexed work.

Self-review: passed. Independent audit: not yet performed.
