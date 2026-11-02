# Scientific review: four-round step-two generalized Petersen graphs

## Correctness

**PASS.** The cyclic-gap strategy has an explicit invariant with thresholds \(B_r=3\cdot2^r\) and proves the infinite tail from index \(24\) upward. At zero remaining rounds, gaps below three determine adjacency, including outer steps of length one, spokes at offset zero, and inner steps of length two. Each induction step chooses a valid split of a long gap. The exact rank-type recursion enumerates every one-point extension, with tuple symmetry used only for memoization. The packaged exact orbit-reduced program computed all indices from \(5\) to \(24\); an independent direct edge-set program verified the common range from \(5\) to \(16\). No finite enumeration is treated as a proof about the infinite tail.

## Originality

**PASS, subject to historical priority risk.** The closest inspected primary treatments provide general Ehrenfeucht–Fraïssé graph methodology (Pikhurko–Verbitsky, arXiv:1003.4865) and generalized Petersen odd-girth/colouring formulas (Daneshgar–Madani, arXiv:1501.06551). Neither inspected full text contains the exact ten-class rank-four partition. Research-index searches for generalized Petersen, four-round, elementary equivalence, cyclic cubic/bicirculant graphs did not identify a covering theorem. The closest indexed step-two Petersen result addresses Vietoris–Rips homotopy rather than finite-model-theoretic equivalence. A priority risk from unindexed older graph-logic literature remains.

## Mathematical value

**PASS.** The classification is complete and sharp for a natural cubic graph sequence containing the Petersen graph and the dodecahedral graph. It exposes a nonmonotone low-index logical collision (\(11\) and \(13\), but not \(12\)), a genuinely stabilized tail at \(15\), and an optimal \(30\)-vertex representative bound. The proof combines a general cyclic-gap principle with a small, reproducible exact finite boundary, giving a reusable way to analyze other periodic bounded-offset graph sequences.

## Closest coverage and limitations

The cited sources do not compute the claimed theory partition, but absence from the inspected sources is not evidence of absolute uniqueness. The exact computation is independently reproduced only through index \(16\); indexes \(17\) through \(24\) are checked by the symmetry-reduced exact recursion and the full infinite tail by a separate mathematical lemma. The theorem is restricted to the uncoloured, simple, undirected adjacency language at rank four.

Self-review: passed. Independent audit: not yet performed.
