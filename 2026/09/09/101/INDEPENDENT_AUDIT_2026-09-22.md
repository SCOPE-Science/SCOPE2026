# Independent audit — 2026/09/09/101

## Scope
Independent three-axis review of `2026/09/09/101` at source tree `abe8b0ef24c8e5605fb82b8afa27ef840cf99cec` on repository `SCOPE-Science/SCOPE2026`. The source tree on `main` matched the assignment tree at audit time.

## Correctness
**PASS.**
- Re-derived the two removed corner volumes s^4/24 each, giving Vol(K_s)=16-s^4/12.
- Re-derived K_s°=conv{±e_i,±u/(4-s)}; exactly one cross-polytope facet is visible at each new tip, and each added 4-simplex has volume s/[24(4-s)], giving Vol(K_s°)=2/3+s/[12(4-s)].
- Algebraic multiplication gives the stated D(s), D(s)/s→1/3, and the uniform lower bound D(s)≥2631s/8064.
- The inclusion (1-s/4)B⊂K_s gives δ≤-log(1-s/4)≤s(4+s)/16; hence D≥δ on the claimed interval. The fallback f=e^{-|x|} counterexample gives J=4, variance 2, and RHS 9/2.

## Originality
**PASS_NARROW.**
- Nazarov–Petrov–Ryabogin–Zvavitch proves qualitative strict local minimality of the cube in Banach–Mazur distance, not this diagonal-truncation exact product or linear one-sided rate.
- Targeted literature searches located the qualitative cube/Hanner stability literature but not the exact formula P(K_s)=(16-s^4/12)(2/3+s/[12(4-s)]) or the resulting every-C cubic-envelope obstruction. The priority claim is therefore confined to this exact family/calculation.

## Scientific value
**PASS.**
- The calculation directly tests a canonical diagonal truncation proposed as a flat Mahler-deficit direction and shows the proposed cubic obstruction is impossible; it therefore changes which local directions are viable in a stability search.

## Reproducibility
Exact rational identities and inequalities were independently recomputed; the committed verifier formulas were inspected and agree with the recomputation.

## Literature checked
- A remark on the Mahler conjecture: local minimality of the unit cube: https://arxiv.org/abs/0905.0867 — Strict local minimality of the cube in Banach–Mazur distance; qualitative local theorem.
- Minimal volume product near Hanner polytopes: https://arxiv.org/abs/1212.2544 — Local minimality near Hanner polytopes; comparison background.
- Stability of the reverse Blaschke–Santalo inequality for unconditional convex bodies: https://arxiv.org/abs/1302.5719 — Qualitative stability background for unconditional bodies.

## Publication disposition
`passed`. This audit file records a proposed publication change-set only; it does not state that any change has been applied to GitHub.

## Limitations
- Originality is asserted only for the exact diagonal family and exact rate after targeted searches, not as an unconditional global priority claim.
- The lower estimate δ≥s/8 remains unproved; it is not needed for the no-cubic-envelope or D/δ^2 conclusions.
- The verifier's introductory comment contains a stale phrase suggesting a quadratic-envelope falsification, while its executed checks and RESULT.md correctly conclude the opposite; this is a non-substantive comment defect.
