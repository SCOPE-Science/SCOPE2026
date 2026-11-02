# Scientific review

## Correctness

**PASS.** The exact-distance equations reduce a putative second source to a two-vertex exact transversal or a four-vertex incident-vertex cover of the four-edge support graph. Classification by odd cycle, number of tree components, and bipartition sizes exhausts all possibilities; elementary labeled-graph counting proves the exact formula for every \(n\ge5\). Both independent exhaustive programs reproduce the full formula and motif counts for \(n=5,6,7,8,9\). The infinite assertion rests on the graph argument rather than extrapolation from finite tests.

## Originality

**PASS, subject to residual priority risk.** The closest exact-two-substitution work (Papadopoulou et al., arXiv:2610.30001v1) determines worst-case read thresholds and investigates decoders, without a four-read pattern classification. Wang, Yaakobi and Zhang (arXiv:2606.05454, Theorem 10 and Section V) treat three reads and identify four-read characterization as a natural next question. Their disjoint-triple condition already subsumes three of the four infinite motif families as sufficient, but not the triangle-plus-disjoint-edge family or the exceptional length-five star; the new classification separates these cases exactly. Junnila et al. (arXiv:2606.09158) supply a general formula for intersections of Hamming balls, not this closed-form four-sphere singleton classification or labeled count. Targeted semantic-record searches revealed no exact equivalent. Such a formula could be derived by nontrivial specialization of more general counting machinery; unindexed earlier graph formulations remain a residual risk.

## Value

**PASS.** Four reads with error budget two are the smallest nontrivial test of the four-read characterization highlighted in the 2026 reconstruction literature. Besides determining the exact proportion of uniquely reconstructible four-read sets at every length, the result identifies and counts the configurations where all three-read subfamilies remain ambiguous. The exceptional star gives a particularly sharp strict separation between unique decoding and ordinary majority voting. The result is specific to exactly two binary substitutions and does not resolve the unrestricted four-read problem.

## Reproducibility and limits

The included scripts `verify_spheres.py` and `verify_graphs.py` are independently formulated, require only Python 3's standard library, and verify the five listed finite lengths. `verification_spheres.txt` and `verification_graphs.txt` record their outputs. Mathematical classification and counting cover all \(n\ge5\); finite enumeration is corroboration. No external audit or independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
