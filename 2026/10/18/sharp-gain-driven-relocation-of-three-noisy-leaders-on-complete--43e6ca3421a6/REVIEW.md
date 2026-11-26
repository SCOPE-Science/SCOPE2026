# Independent mathematical audit

## correctness

PASS

Connectedness plus a nonempty pinned set makes D=L+κD_S positive definite; the stationary Lyapunov equation with identity noise gives covariance D⁻¹/2. Permutation symmetry leaves four types. Inverting the rank-two cross block from the block-diagonal part gives the stated trace U+V+(VU′+UV′)/(1−UV); U≤m/3 and V≤3/m with at least one strict inequality. Subtracting the four expressions yields the three comparisons in RESULT.md, lines 43–59, with positive denominators. Expanding P_m at m=3+y makes every κ coefficient positive, ruling out a=2. The a=1 comparison is strictly negative for m≤7, and for m≥8 has a single positive quadratic root. The a=3 difference vanishes identically at m=3, is always negative for m≥6, and has exactly one positive zero for m=4,5 since the bracket decreases strictly from 3m² to minus infinity. This gives all strict regions and ties; dividing the positive κ_+ formula by m gives a limit of one. Independent exact Gauss–Jordan evaluation of the four Laplacian inverses for 45 rational (m,κ) rows confirmed the three differences (python -B /workspace/branches/audit-replay.py 2). The sign proof covers all admissible rows and irrational thresholds.

## originality

PASS

The all-finite-gain three-leader classification on K_(m,3), including the two threshold functions and strict finite-gain separation at m=6,7, survives the closest actual comparisons. The standard variance objective and general methods are not original here.

## value

PASS

Equal gain is an actionable control parameter in a natural symmetric network family. The exact classification shows distinct relocation modes (all three leaders or just one) and two adjacent graph sizes where the hard-grounding limit's ties hide a strict preference at every finite gain. This goes beyond computing traces for a few instances or tabulating candidates; it resolves all sizes and gain ties for this budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
