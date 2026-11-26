# Independent mathematical audit

## correctness

PASS

At the critical attention value, for M=max(|z|,|v|)>0 the held-v flow points strictly inward at z=±M since tanh(LM)<LM. Thus for every fixed h>0 the continuous update is strictly inside the interval, and the positive convex-average jump puts the other coordinate strictly inside as well, including at gain 1. Compact-annulus continuity proves convergence for all real initial pairs, and inward invariance bounds the continuous trajectory between jumps. Nonzero nonnegative initial data give strictly positive samples after one jump: if z starts positive it cannot hit zero in finite time, and if only v starts positive, the vector field at z=0 is positive. This includes α=0; the nonlinear deficit may vanish on the first interval if v=0, without affecting the proof. For g=γ_h, q=e^(−ah), D=1−q+gq, the left stationary probability vector is (gq,1−q)/D. Its scalar component s satisfies s_next=s−(g/D)δ with δ the integrated nonlinear flow deficit, and y=z−v satisfies y_next=(1−g)(qy−δ). Positivity gives δ=O(s³) and s_next/s→1. Consequently y/s→0 by the strictly stable ratio recursion, and both states equal s+o(s), uniformly inside each dwell. Substitution into the cubic tanh deficit gives δ/s³→(dL²/3)(1−q)/a. Thus s_next^(−2)−s^(−2)→2C and telescoping gives the stated jump-time limit; t/n→h gives the real-time limit. Oddness gives the negative-quadrant limit, not a mixed-sign amplitude. Inverting C gives 1/C=(a/K)[1/g+1/(e^(ah)−1)] with K=dL²/3, yielding strict increase in g and h. For x=ah the sign of the h-derivative of C/h is the sign of gxe^(−x)−(1−e^(−x))D, strictly negative since xe^(−x)<1−e^(−x) and D≥g. This also covers g=1, and C/h→K at small h.

## originality

PASS

Best-of-knowledge pass for the specific global nonovershooting critical dyad result with its sharp coefficient on both clocks and the strict dwell-time reversal. The tanh dyad model, the pitchfork location, and the general cubic inverse-square-root exponent are prior inputs or mechanisms, not credited as new. The same-model supplement's cubic coefficient is for a −1 flip at an opinionated equilibrium, not the neutral +1 pitchfork. Same-day and later critical-relaxation records do not state the exact dyad coefficient or relate the two clocks. The full same-model article was not recovered in this review, so priority is not certified.

## value

PASS

At the critical threshold linear stability alone is inconclusive. Global attraction for the whole nonovershooting regime is useful, and the explicit sharp constant determines the real asymptotic tuning tradeoff: increasing dwell improves relaxation when measured in updates and degrades it when measured on the physical clock. The inverse-square-root exponent by itself would not resolve this question, or determine the common amplitude of both coordinates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
