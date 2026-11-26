# Independent mathematical audit

## correctness

PASS

The equal-block averaging operator is an orthogonal projection on L2; the forcing depends only on the two means and has range in that projection. Hence the means follow the stated exact smooth ODE and the residual is e^(-dt) times its initial value, also for arbitrary non-step L2 data. The bounded averaging and Lipschitz tanh give a globally Lipschitz vector field. On the antisymmetric line, z=L_-s>0 parametrizes the branch by u=d z/(L_- tanh z); tanh z-z sech^2 z is positive since its derivative is 2 z sech^2 z tanh z, so this maps bijectively to u>d/L_-. The block Jacobian eigenvalues divided by d are -1+(L_±/L_-)2z/sinh(2z). The antisymmetric mode is negative and the common mode changes sign once because sinh(2z)/(2z) is strictly increasing from 1 to infinity and L_+/L_->1. The exact residual identity lifts hyperbolic instability/stability; no nonlinear classification at the zero eigenvalue is claimed. In the consensus branch the formula with L_+ as denominator shows the larger eigenvalue is already negative whenever the nonzero branch exists, and the other is smaller. Thus four distinct stable equilibria coexist above u_*. Read, did not run, the source script. Fresh 55-digit working-precision bisection (/tmp/opencode/frozen-review-replay.py, section 4) corroborated z_*=1.08865949248265338, u_*=4.10098722992990467 and common-mode eigenvalues 0.06286519187 at u=4 and -0.21137394900 at u=4.5 for the given example. Uniqueness and full-L2 stability are analytic, not numerical.

## originality

PASS

The supported increment is the exact single secondary stability switch of the polarized branch and the resulting full-L2 coexistence of four stable equilibria in the stated strictly positive, zero-feedback, equal-two-block tanh model. The graphon flow, bifurcation methods, and polarization/multistability more generally are established antecedents.

## value

PASS

For a strictly cooperative positive kernel the initially unstable anti-aligned branch need not stay unstable: increasing gain past a sharp parameter-dependent boundary makes polarized states and same-sign equilibria simultaneously robust to arbitrary small L2 perturbations. Distinguishing saturation-induced stability from mere branch existence is a motivated gap in the near-onset picture. The exact two-block threshold is useful as a test case, without implying global basin behavior or an empirical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
