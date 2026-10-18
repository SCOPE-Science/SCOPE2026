# Mathematical review

## Correctness (C): PASS
The two-dimensional inverse sampling norm is reduced to a single peak-phase variable by differentiating \((1+rA)/(1+rB)\) in the balance parameter \(r\). A piecewise trigonometric maximization gives all three sharp boundary terms, and opposite monotonicity uniquely balances the two active terms. The third term is controlled because the optimal angle lies above half the arc width. Applying scalar estimates to all matrix coefficients proves complete boundedness with no larger constant. The proof covers every \(0<\theta<\pi\), \(0<s\le\theta\), and every positive matrix size. Finite diagnostics are supplementary.

## Originality (O): PASS, with priority risk
Ray's 2026 paper supplies the arc planes and operator-space motivation but classifies isometries rather than the conditioning of two chosen evaluations. The closest identified published claim for the same planes concerns an optimal *Hilbertian metric*, not point-sampling inversion; its implication does not determine the two-node conditioning law. Tikhonov and Yuditskii solve full-circle and positive-length-arc Remez problems; their results do not directly evaluate the two-point-normed inverse or optimize discrete reflection-symmetric node positions. A general polynomial-mesh paper was compared at abstract level only. Searches for aliases, symmetric sampling, operator-space amplification and two-point norming did not reveal a directly covering theorem; search absence is not novelty proof. Classical discrete norming inequalities remain the main residual priority risk.

## Mathematical value (V): PASS
The new arc planes have a natural two-dimensional reconstruction problem: exactly two samples are necessary and sufficient for injectivity. The full sharp conditioning law permits an exact sensor-design optimization, and shows why apparently natural endpoint sampling becomes arbitrarily ill-conditioned as the arc approaches a full circle while the optimal symmetric two-sample design stays bounded by \(\sqrt2\). The matrix-level identity makes the same design valid for all operator-valued coefficient matrices. This is a motivated, complete restricted classification rather than an arbitrary finite constant. It does not assert globally optimal asymmetric placement.

Self-review: passed. Independent audit: not yet performed.
