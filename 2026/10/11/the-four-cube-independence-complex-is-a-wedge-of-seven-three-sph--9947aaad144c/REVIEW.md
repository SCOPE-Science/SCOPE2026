# Scientific review

## Correctness — PASS

The object is precisely the independence complex of the sixteen-vertex graph \(Q_4\), not a graph neighborhood complex or a generic grid. Enumerating all \(2^{16}\) vertex masks and applying the exact adjacency predicate yields \(742\) nonempty simplices. The full certificate specifies \(367\) pairs and an ordering of the entire \(742\)-face Hasse diagram. Every one of its \(2816\) directed cover relations is checked in the acyclic orientation; the eight unmatched cells have dimensions one zero and seven threes. The discrete-Morse theorem gives a CW homotopy model with precisely these cells, so all attaching maps from three-cells land in a point. Hence \(\operatorname{Ind}(Q_4)\simeq\bigvee^7 S^3\). Exact mod-two boundary ranks provide a distinct consistency check, but are not used as a substitute for the homotopy proof.

## Originality — PASS, with stated risk

This concerns the four-cube, equivalently the **two-direction periodic** four-by-four square grid. Bousquet-Mélou–Linusson–Nevo [2] establish explicit Morse/homotopy statements for **open and cylindrical**, not this toroidal quotient, while discussing toroidal alternating counts. Jonsson [3] explicitly constructs cross-cycles for periodic grids and notes that the complete integral homology is generally outside the main results; nonvanishing cross-cycles do not imply the exact rank seven or wedge decomposition. Matsushita–Wakatsuki [4] address **path-by-path** rectangular grids. Barmak's [5] triangle-free suspension theorem applies but does not specify the homotopy-type multiplicity. Kozlov's [1] simple-homotopy results do not classify this independence complex. Searches under four-cube/tesseract/\(C_4\square C_4\)/periodic-grid aliases found no implication covering the complete homotopy statement. Counting the independent sets and establishing general Morse technology are prior work, not claimed as new.

Residual risk: a less-indexed or differently phrased exact computation for this small toroidal quotient could already exist. This review does not establish exhaustive priority or provide independent certification.

## Value — PASS

The four-cube is the canonical smallest four-regular hypercube and also a genuinely fully periodic square-grid example, where open/cylindrical boundary arguments do not automatically apply. The exact seven-sphere homotopy type establishes all integral homology, absence of torsion, and simple connectivity, information not obtainable from published nonvanishing cross-cycle constructions or the alternating independent-set count alone. The \(742\)-face, \(367\)-pair certificate is small enough to provide a reusable rigorous benchmark for periodic hard-square and graph-complex computations. The value claimed is deliberately limited to this natural exact invariant and not to an unproved general theorem.

## Evidence and limitations

Core proof: `RESULT.md`; machine-checkable complete matching: `morse_certificate.json` and `verify_q4.py`; replay details: `VERIFICATION.md`. Closest material: [2] square-grid Morse complexes with open/cylindrical boundary conditions; [3] periodic cross-cycles; [4] rectangular grids; [5] a general suspension theorem. Exact ranks over integers come from the Morse homotopy type, not from a binary homology computation. Only this finite graph is classified.

Same-model review: passed. Independent audit: not yet performed.

## References

[1] Kozlov, https://arxiv.org/abs/math/0503613. [2] Bousquet-Mélou–Linusson–Nevo, https://arxiv.org/abs/math/0701890. [3] Jonsson, https://people.kth.se/~jakobj/doc/papers/crosstorus.pdf. [4] Matsushita–Wakatsuki, https://arxiv.org/abs/2203.16391. [5] Barmak, https://arxiv.org/abs/1007.0418.
