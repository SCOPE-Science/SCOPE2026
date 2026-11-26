# Independent mathematical audit

## correctness

PASS

The frozen inequalities are mathematically sound: the decreasing Gram-cycle kernel gives the cube-sum bound and the missing lower face is bounded by u*B^(k-2)u with u_j=1/j; the logarithmic change of variables leaves the cyclic total-variation kernel, with c_k obtained by Fourier convolution. The weight normalization is exactly H_n and the Schur test gives support in [0,4]. In the repair, the lower trace bound still follows from cells starting at the lattice points and an anchor-length deficit at most (k-1)c_k. The new upper trace bound fixes one coordinate at i before integrating the other coordinates on cells ending at the integers. The integral over all positive remaining coordinates equals c_k/i (one Jacobian absent), strictly greater than the integral over the finite domain. This gives the claimed strictly signed finite defect, including n=1; k=1 is exact. Beta moments and compact support give the arcsine law. The frozen CHECK.py tests a relaxed upper bound with 2 in place of zeta(2). The independent /workspace/independent_checks.py check 4 tested the original bounds on 49 rational cases with a certified stricter upper constant; python3 /workspace/repairs/4/CHECK.py separately passed the repair's strict sign and kc_k bound in 49 cases, not the logarithmic refinement. Neither replay proves the all-parameter theorem.

## originality

PASS

Pass is for the repaired, strictly signed and order-explicit finite-size defect bound, not the original unqualified presentation of the moment/arcsine limits or a qualitative bounded remainder. Those asymptotic contents are covered or implied by Hardy-kernel theory. The repair credits this and proves a stronger finite inequality than the original. No inspected source gives or directly entails this signed bound.

## value

PASS

The repair specifies which side of the limiting energy moments each finite section lies on, and controls the deficit with constants explicit in n and k. This yields one-sided errors for polynomials with nonnegative nonconstant coefficients, which the normalized spectral law or a qualitative bounded remainder alone does not supply. It makes no claim of optimal constants or of a uniform asymptotic in growing k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
