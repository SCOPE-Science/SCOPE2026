# Independent mathematical audit

## correctness

PASS

The repaired finding passes. The frozen line 28 incorrectly scaled an absolute error by c1: for c1<0 with at least one switch this predicts a negative L1 error. The repair gives c1 on signed weak errors and |c1| on the strong error, and clarifies the possibly vanishing term in RESULT.md and SLOGAN.txt. Independently, on a monotone inverse branch t(s), the transformed weight is phi=w(t(s))/|S'(t(s))|, with phi'(0) exactly [w'S' - wS'']/|S'|^3, for both orientations. The kernel is the derivative of the even potential F_delta(s)=sqrt(s^2+delta)-|s|. Integration by parts on a fixed symmetric interval gives O(delta) boundary terms and minus the integral of F_delta*phi'. On sqrt(delta)<=s<=r, F_delta(s)=delta/(2s)+O(delta^2/s^3), and the inner part gives O(delta); hence its mass is (delta/2)log(1/delta)+O(delta). Multiplying by phi'(s)-phi'(0)=O(|s|) costs O(delta). Away from roots the kernel is uniformly O(delta). For the strong statement the even absolute kernel integrates on a symmetric interval to 2(r+sqrt(delta)-sqrt(r^2+delta)); the Jacobian at zero supplies the leading factor and its O(|s|) difference costs at most O(delta log(1/delta)). No roots gives O(delta). For the double integrator the terminal weights are 1 and T-t, yielding respectively zero and +1/2 logarithmic coefficients; an odd integrand gives exact velocity cancellation at the midpoint. The supplied high-precision quadrature script was inspected, not executed. This is a fixed-profile comparison, not an optimal-solution convergence theorem.

## originality

PASS

Best-knowledge pass for the exact weighted log-bias coefficient with curvature and cancellation, the strong constant, and their terminal illustration at a fixed prescribed switch. The surrogate and inverse switching coordinate are not claimed new. The corrections to scaling and wording do not add a new priority claim.

## value

PASS

The exact coefficient determines which weighted fixed-profile observations have an ordinary O(delta) error and which suffer logarithmic amplification, even when net velocity bias cancels. The sharp strong mass answers a complementary question about control error without cancellation. This is useful for interpreting a prescribed-switch smoothing scheme already in use; it does not claim to predict errors after reoptimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
