# Scientific review

## Correctness

PASS. The scalar comparison equivalence follows by an absolute-value necessity test and a two-stage Gaussian/Jensen sufficiency argument. The zero-sum absolute-norm inequality is sharp and its equality direction lies in the simplex frame image, giving the exact all-projection threshold. Every Gaussian block coupling reduces to a correlation matrix of scalar coefficients; its barycentre covariance has a trace bounded by \(1/d\), and the regular-simplex coupling realizes covariance \(I_d/d^2\). The endpoint rigidity follows by pushing the covariance identity through the Gram projector. The packaged `code/verify.py` passed 21552 exact assertions. Finite diagnostics do not replace the proof.

## Originality

PASS, qualified. The closest primary results are Jourdain–Pagès' general variational necessary/sufficient conditions (arXiv:2410.07958) and Guéant's exact equivalence for only two mixture components (arXiv:2610.07404v1, Sections 1.4, 3–4). A separately inspected October 2026 three-component counterexample uses a non-simplex, unequal-weight planar mixture and proves actual full convex-order failure, but does not yield the equal-weight simplex thresholds, dimensional factor, or endpoint coupling rigidity. Published-record and prior-claim searches found no covering result. Remaining risks: older Gaussian matrix-coupling optimization literature may contain the same trace bound; Jourdain–Pagès' complete journal body was not available, so no full-body absence claim is made. The proof does not assign novelty to the elementary simplex identity, zero-sum norm inequality, or Gaussian comparison tools separately.

## Mathematical value

PASS. The larger-mixture case is explicitly highlighted as unresolved in recent Gaussian convex-order research. A complete symmetric all-dimensional test family shows quantitatively how far a computationally meaningful Gaussian-block sufficient criterion can fall short of necessary directional tests, with sharp constants, a \(\\(\sqrt2\)\) asymptotic factor, and a unique extremal correlation structure. It is a structural diagnostic boundary, not a general negative answer for multivariate convex order. No downstream theorem is needed for this motivated exact boundary; its restrictions are stated.

## Literature and limitations

References and their distinct implications appear in RESULT.md. The sole unresolved substantial priority risk is unexamined older or inaccessible full-body literature subsuming this specific matrix-coupling computation. The mixed directions, scope, and all three certificate levels are not interchangeable.

Self-review: passed. Independent audit: not yet performed.
