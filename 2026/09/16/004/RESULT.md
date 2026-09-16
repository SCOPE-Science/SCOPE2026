# Valuative obstruction: the Li–Miao v2 ceiling overshoots the stratified volume bound

## Context

Li–Miao (arXiv:2506.17420v3) prove that a K-semistable Fano manifold X not isomorphic to P^n satisfies (-K_X)^n <= 2^n n^n, with equality only for P^1 x P^{n-1} or a smooth quadric. Their method tests K-semistability via divisorial valuations centered on a minimal rational curve f: P^1 -> X. Question 4.20 of that paper asks a stratified refinement: if X (n >= 4) contains a minimal rational curve of anticanonical degree 3 <= d <= n-1, is (-K_X)^n <= vol(P^{d-1} x P^{n-d+1})? The source paper leaves this open after correcting an error about l >= 3 valuations (Remark 4.4).

## Definitions

Let f^*T_X = O(2) + O(1)^{d-2} + O^{n-d+1}, d = (-K_X . f(P^1)). Li–Miao define globally defined valuations v_1, v_2 by v_l(psi) = min{|I| + l|J|} in adapted charts. For l = 2 (weights (1^{d-2}, 2^{n-d+1})), the leading H0-count yields phi(x) in (25)/(27) with primitive Phi(x) in (26)/(28), log discrepancy A = A_X(v_2) = (d-2) + 2(n-d+1) = 2n-d, and T the unique root of Psi(T) := (T-A)phi(T) - Phi(T) = 0. By Corollary 2.5, K-semistability gives V := (-K_X)^n <= phi(T). Let B(n,d) := vol(P^{d-1} x P^{n-d+1}) = C(n,d-1) d^{d-1} (n-d+2)^{n-d+1}.

## Result

The v_2 valuative ceiling phi(T) strictly exceeds the conjectured stratified bound B(n,d) at every computed pair (n <= 10, all 3 <= d <= n-1), with ratio phi(T)/B in [1.040, 1.134]. In particular at the sharp self-consistent case (n,d) = (4,3): phi(T) approx 505.6 > 486 = B(4,3), T approx 7.079, with exact rational certificate T in (7,7.1) and phi(T) > 492.75 > 486. The l = 1 ceiling is uniformly worse, and the exact H0 twist changes only O(1) terms with the same leading coefficient. Hence Question 4.20 cannot be proved by the globally defined v_1/v_2 valuations alone; any proof must invoke a new divisor or classification input.

## Proof / evidence

Anchor (4,3), l = 2: r = n-d+1 = 2, A = 5. With y = x-3 >= 0, phi(y) = (243+216y+54y^2)/4 and Phi(y) = (972/5+243y+108y^2+18y^3)/4, verified against (27)-(28) with continuity phi(0) = 243/4, Phi(0) = 243/5. Then Psi(y) = (y-2)phi(y) - Phi(y) satisfies Psi(4) = -26.1 < 0 < Psi(4.1) = 7.389 (from phi(4.1) = 509.085, Phi(4.1) = 1061.6895). Since Psi' = (x-A)phi' > 0 past A, the root y_T in (4,4.1), i.e. T in (7,7.1), is unique, and phi increasing gives phi(T) > phi(7) = 1971/4 = 492.75 > 486 = B(4,3). Every number is hand-checkable rational arithmetic. Notably P^2 x P^2 itself has minimal degree 3 and volume 486, yet the method ceiling is ~505. Parametric evidence: stdlib bisection on Psi (200+ iterations) reproduces the table (e.g. (5,4): 6136.0 vs 5760; (6,4): 88018.4 vs 81920; (10,7): 17508419986.6 vs 15441431250). Controls with l = 1 give uniformly larger ceilings (e.g. (4,3): 560; (5,4): 7189). Closed sums verified against direct quadrature and brute-force lattice counts; continuity at x = d confirmed.

## Limitations

The anchor certificate is fully rigorous exact arithmetic. The parametric table is computed floating-point evidence (independently cross-checked by quadrature and lattice counts), not interval-certified at every pair. The finding obstructs the v_1/v_2 method only; it neither proves nor disproves Question 4.20 itself. Valuations with l >= 3 are not globally defined (Li–Miao Remark 4.4) and cannot rescue the route without new comfortable-embedding input.

## Reproducibility

Run `python3 output/artifacts/valuation_ceiling.py` (stdlib only) to regenerate the l = 2 table and compare against B(n,d); change ell=1 for controls. The anchor certificate can be checked by hand from Section 2 formulas above.

## References

- C. Li, M. Miao, On the volume of K-semistable Fano manifolds, arXiv:2506.17420v3, Sec 4, Question 4.20.
- C. Li, M. Miao, K. Zhang, The sharp volume gap for Kaehler manifolds with positive Ricci curvature, arXiv:2608.08193 (beta-volume generalization).
