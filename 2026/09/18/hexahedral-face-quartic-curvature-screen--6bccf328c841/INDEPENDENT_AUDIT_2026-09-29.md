# Independent audit — 2026-09-29

Record: `2026/09/18/hexahedral-face-quartic-curvature-screen--6bccf328c841`  
Assigned and audited source tree: `923190d4000b5e4be610e4769fe027fe83ae1983`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The curvature screen is correct for the displayed face-polynomial class. Along the parabola vertex s_*(t), direct differentiation gives h'=P/(4a^2). If a is constant, h''''=-6b_2^2/a; if a is nonconstant, division b=aℓ+r with constant remainder r gives h''''=-6r^2 a_1^4/a^5. Thus h'' is concave on every positive-a interval. Four distinct zeros of h' would force a zero of h'''' by repeated Rolle when the inequality is strict, while the equality case reduces h to a low-degree polynomial, proving the three-root bound. Two distinct interior minima would force h'' signs +,-,+ at ordered points, impossible for a concave h''. The Hessian Schur complement gives det∇²f=2a h'', and at P=0 this becomes P'/(2a), so the simple-root curvature screen is exact. Independent symbolic expansion also reproduces the rational three-root witness with slopes -18/25, 9/25, -18/25.

## Originality

**qualified_structural_refinement**. Zhang's September 2026 paper is the substantive prior result: it proves boundary sufficiency/global-boundary minimization and reduces boundary minimization to finitely many points found by quartic root solving. Earlier certified hexahedron validation relies on different Bernstein/subdivision machinery. Targeted current searches did not locate the special identity h''''≤0, the consequent one-minimum theorem, or the stationary Hessian formula P'/(2a) in the hexahedral-validation literature. The record is therefore best viewed as a sharp post-root-solve structural refinement of Zhang's new reduction, not a new validation theorem from scratch.

## Scientific value

**useful_exact_candidate_reduction**. The theorem gives a rigorous way to discard all saddle-capable interior roots after quartic isolation and cuts the number of interior jacdet evaluations from as many as four per face to at most one. It also supplies a conceptual explanation via concavity of h''. The gain is real but localized: the algebraic quartic solve itself is unchanged and no finite-precision runtime theorem is established.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/hexahedral-face-quartic-curvature-screen--6bccf328c841
- https://arxiv.org/abs/2609.19926
- https://arxiv.org/abs/1706.01613
- https://doi.org/10.1145/3554920

## Limitations

- The result only filters stationary candidates after the quartic roots are isolated; it does not reduce the quartic algebraic degree.
- The three-root sharpness example is for the abstract face-polynomial coefficient class and is not shown to arise from a physical trilinear hexahedron.
- The public source paper is extremely recent, so concurrent or not-yet-indexed refinements cannot be excluded.
- The theorem concerns trilinear hexahedral jacdet face restrictions and does not automatically extend to higher-order elements.
