# A strict sixth-cumulant witness on the zero-kurtosis curve of a reversing active particle

## Finding

Consider a planar direction-reversing active Brownian particle confined by an isotropic harmonic force. Let \(X\) denote one Cartesian coordinate in its stationary distribution. On the *entire* curve where its fourth cumulant vanishes, the sixth cumulant is strictly negative, with an explicit dimensionless law.

With trap relaxation \(\mu>0\), propulsion speed \(v>0\), angular diffusivity \(D_R>0\), and reversal rate \(\gamma>0\), put \(d=D_R/\mu\). The previously identified zero-kurtosis curve is
\[
\gamma=\frac{7D_R+3\mu}{2}.
\]
On that curve,
\[
\boxed{\operatorname{cum}_6(X)=-\left(\frac v\mu\right)^6
\frac{15(3d+1)}{1024(d+1)^2(2d+1)^3(8d+3)}<0.}
\]
Furthermore, if \(\sigma^2=\operatorname{Var}(X)\), then the standardized sixth cumulant is
\[
\boxed{\frac{\operatorname{cum}_6(X)}{\sigma^6}
=-\frac{15(3d+1)}{2(d+1)^2(8d+3)}.}
\]
As \(d\) increases through all positive values this standardized cumulant increases strictly, taking *exactly* the interval \((-5/2,0)\). For example, \(D_R=\mu\) and \(\gamma=5\mu\) yield the exact value \(-15/22\) despite zero excess kurtosis.

This supplies a quantitative non-Gaussian witness precisely where a fourth-cumulant diagnostic is blind. The source paper already remarks that zero kurtosis need not imply Gaussianity; the claimed extension is the exact sixth-cumulant law, its strict sign, and its full range.

## Assumptions and scope

The particle has position \((X_t,Y_t)\), propulsion orientation \(\Phi_t\in\mathbb R/(2\pi\mathbb Z)\), harmonic relaxation \(\mu>0\), and constant propulsion speed \(v>0\):
\[
 dX_t=(-\mu X_t+v\cos\Phi_t)\,dt,\qquad
 dY_t=(-\mu Y_t+v\sin\Phi_t)\,dt.
\]
Independently, the angle has rotational Brownian diffusion with generator \(D_R\partial_\phi^2\), and at the points of a rate-\(\gamma\) Poisson process it jumps by \(\pi\). The latter is equivalent to the source formulation with an independently switching propulsion sign. No translational Brownian noise or positional resetting is included. Every assertion concerns the unique stationary law, and the inequalities assume \(D_R>0\).

For \(Z=\mu X/v\), \(d=D_R/\mu\) and \(g=\gamma/\mu\), time-rescaling gives the stationary generator
\[
 \mathcal Lf=(-z+\cos\phi)\partial_zf+d\partial_\phi^2 f
 +g\bigl(f(z,\phi+\pi)-f(z,\phi)\bigr).
\]
The angular process has the uniform invariant distribution and the stationary coordinate satisfies \(|Z|\le1\). Thus all moments used below exist. Because the angular diffusion is ergodic and the linear position dynamics contracts, this stationary law is unique. Rotational symmetry makes all odd moments of \(Z\) vanish.

## Proof

**Step 1: finite stationary moment recursion.** Define \(M_{n,k}=\mathbb E[Z^n e^{ik\Phi}]\) for integers \(n\ge0\) and \(k\in\mathbb Z\). Angular uniformity implies \(M_{0,0}=1\) and \(M_{0,k}=0\) for \(k\ne0\). Applying \(\mathbb E[\mathcal L(z^ne^{ik\phi})]=0\) gives, whenever \(n\ge1\),
\[
\boxed{M_{n,k}=\frac{n(M_{n-1,k-1}+M_{n-1,k+1})}
 {2\bigl(n+dk^2+2g\mathbf1_{k\text{ odd}}\bigr)}.}
\]
The denominator is positive. Starting from \(n=0\), this recursion uniquely and *exactly* computes each finite moment. Reality, angular reflection symmetry and parity permit restriction to the finite triangle \(|k|\le n\), with \(M_{n,k}=0\) for opposite parities of \(n,k\). No truncation of an infinite series is needed for moments of a specified order.

**Step 2: locate the fourth-cumulant-zero curve.** The first two nontrivial even coordinate moments computed from the recursion are
\[
 m_2=M_{2,0}=\frac1{2(d+2g+1)},\qquad
 m_4=M_{4,0}=\frac{3(4d+3)}{8(2d+1)(d+2g+1)(d+2g+3)}.
\]
These agree with the published stationary variance and fourth moment [1]. Direct subtraction yields
\[
 \kappa_4=m_4-3m_2^2
 =-\frac{3(7d-2g+3)}{8(2d+1)(d+2g+1)^2(d+2g+3)}.
\]
All denominator factors are positive for \(d,g>0\); hence \(\kappa_4=0\) is equivalent to \(g=(7d+3)/2\). This curve and its fourth-order property are prior results, not a new claim.

**Step 3: evaluate the sixth cumulant without assuming Gaussianity.** Substitute \(g=(7d+3)/2\) into the recurrence. Its successive values include
\[
 \begin{aligned}
 M_{2,0}&=\frac1{8(2d+1)},&
 M_{3,1}&=\frac3{64(2d+1)^2},\\
 M_{3,3}&=\frac3{64(2d+1)^2(8d+3)},&
 M_{4,2}&=\frac3{32(d+1)(2d+1)(8d+3)},\\
 M_{4,0}&=\frac3{64(2d+1)^2},&
 M_{5,1}&=\frac{15(8d^2+15d+5)}{1024(d+1)^2(2d+1)^2(8d+3)}.
 \end{aligned}
\]
At \(n=6,k=0\), the recursion and angular reflection symmetry give \(M_{6,0}=M_{5,1}\). Therefore the sixth raw moment is
\[
 m_6=\frac{15(8d^2+15d+5)}{1024(d+1)^2(2d+1)^2(8d+3)}.
\]
Symmetry makes the odd moments zero, so the sixth cumulant is
\[
 \kappa_6=m_6-15m_4m_2+30m_2^3
 =-\frac{15(3d+1)}{1024(d+1)^2(2d+1)^3(8d+3)}.
\]
Because \(X=(v/\mu)Z\), the physical sixth cumulant is \((v/\mu)^6\kappa_6\). All numerator and denominator factors show strict negativity for every \(d>0\).

**Step 4: determine the complete standardized range.** The variance on this curve is \(\mathbb E[Z^2]=1/[8(2d+1)]\). Hence \(\kappa_6/m_2^3=-15f(d)/2\), where
\[
 f(d)=\frac{3d+1}{(d+1)^2(8d+3)},\qquad
 f'(d)=-\frac{48d^2+33d+5}{(d+1)^3(8d+3)^2}<0.
\]
The continuous function \(-15f(d)/2\) is strictly increasing on \(d>0\) and has limits \(-5/2\) as \(d\downarrow0\) and \(0\) as \(d\to\infty\). The limits are not attained at a finite positive \(d\), establishing exactly the claimed open range.

## Verification

The accompanying `verify_sixth.py` constructs the finite moment triangle symbolically using SymPy and checks the generic second/fourth moments, zero-kurtosis locus, intermediate sixth-order Fourier moments, final cumulant, monotonicity derivative, endpoint limits, and the example at \(d=1\). It separately evaluates the stationary generator identity at four exact rational choices of positive angular diffusivity. Run `python verify_sixth.py` after installing `sympy>=1.12`; the recorded output appears in `verify_output.txt`. The symbolic checks are supplementary to the displayed finite-recursion proof, not evidence of a numerical infinite extrapolation.

## Relationship to prior work

Santra, Basu and Sabhapandit [1] define the same reversing active particle in a planar harmonic potential and explicitly derive its stationary variance, fourth moment, and excess kurtosis (Appendix A, equations (41), (47), (48)). They observe that kurtosis can vanish without Gaussianity, especially in the vanishing-angular-diffusion limit. These established facts are fully acknowledged; their explicit formulas stop at fourth order. The sixth-order coefficient, its strict negativity along the *full positive-diffusivity* zero-kurtosis locus, and the monotone image interval above are not stated in the inspected text of [1].

Chaudhuri and Dhar [2] construct a general moment method for harmonically confined active Brownian motion without Poisson directional reversals. Their operator lacks the odd-harmonic reversal damping that is essential here. Frydel [3] develops general moment-recurrence techniques for active oscillators; a general recurrence procedure can furnish a method for this calculation, but its available abstract does not state the evaluated sixth-order conclusion for the present reversing model. Full text of [3] could not be inspected, leaving a specific priority risk.

## Limitations

This result does not identify the full stationary probability density, describe transient moments, or establish any analogous sixth-cumulant sign for arbitrary confining potentials, translational Brownian noise, or positive but noncritical fourth cumulant. It does not claim that non-Gaussianity on this curve was previously unknown; rather, it supplies an exact quantitative witness where the fourth cumulant is zero. Although the process has bounded support at any finite parameters, its sixth-cumulant law gives genuinely finer information than that qualitative support argument. No independent scholarly priority or proof audit has been performed.

## References

[1] I. Santra, U. Basu and S. Sabhapandit, *Direction reversing active Brownian particle in a harmonic potential*, arXiv:2107.12640v1, first posted 27 July 2021, https://arxiv.org/abs/2107.12640 (Appendix A, equations (41), (47), (48)).

[2] D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234, first posted May 2020, https://arxiv.org/abs/2005.14234.

[3] D. Frydel, *Active oscillator: recurrence relation approach*, arXiv:2312.05406v1, first posted 8 December 2023, https://arxiv.org/abs/2312.05406 (abstract consulted; full text not inspected).
