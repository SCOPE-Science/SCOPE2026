# Review

## Correctness

PASS. On each open half-line the scalar SAM-plus-EMA-momentum map is affine with a common \(2\times2\) matrix. Solving the two alternating affine equations shows that the unique sign-consistent period-two orbit has amplitude \(c=s\rho/[2(1+\beta)-s]\), where \(s=\alpha\lambda(1-\beta)\). The matrix characteristic polynomial is \(r^2-(1+\beta-s)r+\beta\); the three real Jury inequalities reduce exactly to \(1-\beta>0\), \(s>0\), and \(2(1+\beta)-s>0\). This proves the sharp equivalence between orbit existence and local asymptotic stability. The determinant lower bound and discriminant give the exact \(\sqrt{\beta}\) rate plateau. Eliminating momentum yields the boundary/supercritical magnitude recurrence and proves linear versus at-least-geometric divergence for zero-momentum starts.

Risk: the result is not a global convergence theorem below the boundary and does not include a time-varying adaptive preconditioner. Both restrictions are explicit throughout the package.

## Originality

PASS. The inspected no-momentum SAM quadratic papers establish oscillatory/cycle behavior without the EMA momentum state. The inspected SAM stability paper analyzes momentum through a saddle-point diffusion approximation rather than an exact deterministic quadratic cycle frontier, and explicitly identifies broader momentum dynamics as a direction for further study. AdaSAM supplies the normalized EMA-momentum-plus-SAM update and stochastic nonconvex convergence bounds, but the inspected algorithm/theorem material does not give the necessary-and-sufficient scalar two-cycle boundary, cycle amplitude, local spectral plateau, or critical divergence law. MSAM uses accumulated momentum to choose the perturbation direction and therefore has a different map.

Targeted semantic searches over SAM, momentum, scalar quadratics, period-two cycles, stability thresholds, and the derived parameter combination found related stability results but no statement implying the complete claim. A residual terminology risk remains because the local matrix is a forced heavy-ball-type recurrence and an equivalent calculation could appear outside the SAM literature.

## Value

PASS. Constant-radius SAM is known to cycle rather than converge on positive quadratics, while practical implementations commonly combine sharpness-aware gradients with momentum. The exact formula shows how normalized EMA momentum changes the admissible cycle-stability window, how the cycle amplitude blows up at its edge, and where local rate improvement saturates at the determinant barrier \(\sqrt{\beta}\). The matching linear/geometric divergence law at and above the boundary turns the formula into a sharp diagnostic rather than a merely sufficient tuning rule.

Same-model review: passed. Independent audit: not yet performed.
