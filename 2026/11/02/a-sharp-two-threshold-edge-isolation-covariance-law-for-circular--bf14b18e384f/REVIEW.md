# Scientific review

## Correctness — PASS

For independent uniform points on the circle, one marked vertex is isolated with probability \((1-2r)^{n-1}\), and all other vertices remain iid uniform on the complementary arc. The two-point conditional connection probability is the area of a diagonal strip divided by the arc-square area; its precise value is \(q=1-(\max\{1-3r,0\}/(1-2r))^2\). Separating incident from nonincident edges yields the stated exact covariance. The piecewise sign simplification is an elementary quadratic for \(r\le1/3\) and a strictly decreasing affine expression thereafter. The proof treats \(n=2\), \(3\le n\le5\), \(n=6\), \(n\ge7\), and boundary radii separately. Its derivation and the independent rational geometry and finite-grid checks agree. The asymptotic coefficient follows from \(q-2r=3r^2+O(r^3)\), rather than finite-size extrapolation.

## Originality — PASS, subject to historical-priority uncertainty

The inspected primary work on isolated vertices and connectivity (Penrose, arXiv:1311.3897), on excess-edge large deviations (Chatterjee–Harel, arXiv:1401.7577), and on one-dimensional soft isolation (Wilsher–Dettmann–Ganesh, arXiv:2007.06301) does not give the joint finite-sample edge–isolate covariance, the six-vertex onset, or its two exact sign thresholds. The available Zhao–Yagan–Gligor article description concerns one-dimensional isolation/connectivity, but its entire full text was not inspected. The likely closest general coverage consists of moment techniques for spatial geometric graph counts, which may imply the raw covariance integral without visibly supplying its global two-zero classification. Searches cannot certify an absolute priority claim. No equivalence or stronger published theorem was found among checked material.

## Mathematical value — PASS

The local number of isolated nodes and the edge count are two standard complementary diagnostics for network connectivity and density. For independent edges their covariance is always negative, so a sharp positive-covariance window under spatial dependence is a real structural reversal, not an arbitrary coefficient identity. The exact least sample size of six, two fully classified finite-radius transitions, and the sparse window threshold \(4/3\) provide interpretable, falsifiable mathematical boundaries.

## Literature and limits

The research uses the fixed-point-count circle model with a hard connection radius. Results for boundaries, soft models, or higher dimension are not proved. A 2015 relevant abstract was available but not its complete text, and the general 2003 book on random geometric graphs was not inspected in full; equivalent prior formulas could exist. This is a self-review, not independent validation.

Self-review: passed. Independent audit: not yet performed.
