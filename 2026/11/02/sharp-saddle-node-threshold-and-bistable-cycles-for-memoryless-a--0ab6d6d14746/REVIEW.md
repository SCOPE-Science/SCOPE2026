# Mathematical review

## Correctness — PASS

For the exactly specified memoryless Adam map, the positive radial multiplier is \(\nu(r)=\eta/(r+\varepsilon r^{-(p-2)})\). The denominator is strictly convex with its unique global minimum at \(r_*=((p-2)\varepsilon)^{1/(p-1)}\); its level \(\eta/2\) therefore has zero, one, or two positive roots across the stated threshold. This establishes the global one-step contraction below threshold and the complete count of **symmetric** cycles, not nonsymmetric cycles. Direct differentiation gives the exact two-step derivative and its signs on the two roots. A local radial contraction argument separately proves the origin attracts nearby points for every step; a Taylor expansion proves the square-root collision, and a telescoping reciprocal-power argument proves the convergence exponent for nonterminating trajectories. The exact cubic witness checks the attracting/repelling distinction. The self-contained `artifacts/verify.py` passed 3970 finite checks. None of the infinite-quantifier statements rests on those finite checks.

## Originality — PASS with documented priority risk

The published-note searches for superquadratic Adam, smoothed normalized descent and period-two saddle nodes returned related quadratic AdamW, Polar-Express and Padam notes, but their equations do not imply the reported superquadratic phase diagram. Both quadratic smoothed-normalization examples have a nonzero gain and a flip of origin stability, whereas the present \(p>2\) map has gain vanishing at zero, a permanently attracting origin and two coexisting cycles created away from zero. Padam has a running historical maximum and is another recurrence. Full mathematical texts of these three closest published notes were read. The 2026 motivating arXiv abstract, public figure descriptions and substantive paper summaries were inspected, but its full manuscript was unavailable; these accessible materials treat the two-memory spike phase diagram rather than the exact memoryless saddle-node classification. This prevents an exhaustive assertion of historical novelty, but no inspected claim or stronger theorem covers the result. The known local bifurcation methods are not claimed as new.

## Value — PASS

This is a sharp global stepsize threshold for every real initial point on a natural strictly convex superquadratic test loss and a complete classification of its *symmetric* nonzero two-cycles. The simultaneous stability of the minimizer and a nonzero oscillation is qualitatively different from the quadratic flip model and matters when interpreting convergence and persistent objective floors in normalized optimization. The square-root splitting and algebraic relaxation provide quantitative diagnostics. The limitations to zero memory, scalar power loss and symmetric cycles are essential; the result does not assert behavior for full Adam or general neural-network training.

Self-review: passed. Independent audit: not yet performed.
