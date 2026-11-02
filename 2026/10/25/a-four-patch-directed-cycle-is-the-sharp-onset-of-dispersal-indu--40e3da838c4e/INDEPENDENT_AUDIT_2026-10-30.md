# Independent mathematical audit

## correctness

PASS

PASS: At the unique positive equilibrium K=r-eta*d, maximum/minimum principles force all patch values to K. Linearization simplifies to vdot_j=d(v_{j-1}-v_j)-K v_j(t-tau). Fourier eigenvalues zeta imply modal characteristic equation z=q(zeta-1)-exp(-z*s), q=d/K,s=K*tau. At a potential imaginary crossing of z=-A+iB-exp(-zs), one must have 0<=A<=1 and frequency B+sqrt(1-A^2), with first delay acos(-A)/(B+sqrt(1-A^2)); the alternative signed-frequency branch is later. The uniform delay is s=pi/2; for n=2 transverse delayed crossing is later, for n=3 s3=(pi/2+t)/(cos(t)+sin(t)/sqrt(3))>pi/2 by a positive convex comparison. For n=4 quarter-phase zeta=+/-i gives s_rot=acos(-q)/(q+sqrt(1-q^2)); strict concavity of (pi/2)(sin t+cos t-1)-t ensures exactly one interior positive switching root q*=sin(t*)~0.5814567017105. Crossings have positive real derivative (B+R)R/((1+sA)^2+s^2 R^2), and the uniform scalar crossings also go rightward, establishing stability before and instability after first crossing. Independent modal residuals and numerical unique-root check passed; their finite sampling is not the all-parameter proof.

## originality

PASS

PASS (best-of-knowledge): Same vocabulary of rotating waves does not make the modal characteristic equations identical; checked against precise q, s and n thresholds. A general theorem on all circulant delay equations might imply this specialization, but the inspected primary statements do not provide the exact all-rate n<=4 first-crossing ordering or q*. Explicit modal roots and their rightward crossings establish the full claimed all-delay result beyond perturbative literature. Stronger unlocated characteristic-equation theorems are a priority caveat. Specific priority and access qualifications are recorded below.

## value

PASS

PASS: Gives explicit minimal directed homogeneous ring size for a rotating mode to destabilize before synchronization and a complete sharp all-dispersal mode-order diagram in a natural delay-patch family. Distinguishes spatial phase pattern rather than merely generic Hopf existence, without claiming nonlinear oscillations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
