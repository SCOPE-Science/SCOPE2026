# Three-node trigonometric SBP: mathematical review

## Correctness — PASS
The three trigonometric traces are unisolvent on the specified frequency interval, so the nodal derivative is unique. A trigonometric cardinal function forces the interior point to be the midpoint from the SBP middle diagonal. Exact computation of the unique centered derivative and boundary diagonals forces all weights; the remaining SBP entries hold identically. Strict positivity is equivalent to \(\omega<2\pi/3\). The mass inequality follows from an explicitly positive derivative of \(H\), and Taylor/endpoint limits establish the quantitative constants. `verify_fsbp.py` cross-checks the exact formulas symbolically and seeded finite instances (668 passing checks). This is not an infinite computational proof.

## Originality — PASS under inspected-source comparison
The abstract existence theorem in Glaubitz–Nordström–Öffner (arXiv:2203.05479) covers function spaces generally; it does not give the sharp three-node interior-geometry and frequency threshold or norm-mass asymptotics. Haase–Winters–Glaubitz (arXiv:2610.30272v1) focuses on FSBP flux differencing and accuracy for broader spaces, not this classification. Bercik–Patrascu–Zingg (arXiv:2607.08934) treats optimized generalized quadrature, not this fixed three-node restriction. published-finding corpus and literature searches returned neighboring Fourier three-node/frame and quadrature results, but none with the exact SBP equivalence and mass statement. Residual priority risk: an unlocated specialist three-node trigonometric quadrature or FSBP example may contain the explicit answer. Search non-detection cannot establish universal priority.

## Mathematical value — PASS
This is a complete, sharp answer to the minimal-node positive-diagonal norm feasibility question that arises when deploying trigonometric-function-space SBP discretizations. The midpoint rigidity and loss of norm feasibility at \(2\pi/3\) are meaningful geometric/frequency design constraints. The forced constant mass mismatch and its blowup show that trigonometric exact differentiation, SBP energy compatibility, and physical constant quadrature cannot all be achieved in this minimal family. The constraint is practical only for this specifically defined discretization; it does not imply failure with extra nodes or arbitrary norms.

## Limits and comparison
The self-review reconstructs the proof but is not an independent mathematical audit. The baseline general-existence principle and classical trigonometric cardinal interpolation are prior work; only their sharp combined classification and mass consequence are asserted here. These statements do not establish any nonlinear entropy-stability failure or an unrestricted numerical PDE impossibility theorem.

Self-review: passed. Independent audit: not yet performed.
