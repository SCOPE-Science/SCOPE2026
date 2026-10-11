# Scientific review

## Correctness — PASS

The claim uses the geometric-realization graph Čech definition, not the discrete-metric convention. The general facet lemma [1] reduces the complete filtration to integer thresholds. The explicit relative elementary collapse at threshold two checks every one of its forty free-face deletions. The threshold-three simplices and all covering incidences are enumerated exhaustively, and a deterministic 219-pair discrete-Morse matching is certified acyclic, leaving exactly one zero-cell and thirty-six three-cells. Forman's theorem then proves the integral wedge decomposition. Independent mod-two boundary ranks corroborate the dimensions. The packaged `verify.py` was executed successfully from its actual file path. This is an exhaustive finite certificate, not an unproved extrapolation from examples.

## Originality — PASS, with residual risk

The 2022 paper [1] describes the general Čech construction and classifies large-scale **hypercube** examples. Its graph-recovery theorem covers the scale-two Petersen homotopy type but not the threshold-three homotopy type or whole barcode. Previte's 2014 thesis [2] studies distance-set neighborhoods centered on single **vertices**, recording the Petersen Betti number six at even scale and triviality at full diameter; its construction is not the 15-edge-neighborhood union nerve at odd scale. Direct searches for Petersen graph Čech scale three, closed edge-neighborhood nerve, Kneser graph equivalence, and wedge-of-thirty-six third spheres did not identify a dominating theorem; related Petersen matching and total-cut complex results have different defining face conditions. Non-indexed equivalents remain a risk, and search failure by itself is not a novelty certificate.

## Value — PASS

The Petersen graph is a canonical connected cubic, triangle-free, diameter-two strongly regular graph. The first odd threshold outside the small-radius nerve regime exhibits a jump from six persistent integral circle classes to thirty-six three-sphere classes. A complete natural filtration and a precise combinatorial explanation of the jump provide useful structural information beyond a one-scale Betti calculation, and distinguish the edge-midpoint Čech nerve from the known even-scale vertex-neighborhood complexes. The numerical invariant has a clear object- and filtration-level motivation.

## Closest sources and limitations

[1] H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (2022); pp. 1–4 establish definitions and Lemmas 2.2–2.3, with later sections dedicated to hypercube calculations. [2] C. Previte, *The D-Neighborhood Complex of a Graph*, Colorado State University thesis (2014); §3.2 explicitly computes the Petersen vertex-neighborhood case. The finite algorithm gives a fully reproducible mathematical proof when its complete incidence checks are accepted; it is not an independent external audit. Unindexed overlapping work remains possible.

Same-model review: passed. Independent audit: not yet performed.
