# Three dimensions are minimal for unbounded second-step Heavy-Ball objective spikes

## Finding
Consider the Heavy-Ball iteration
\[
x_{k+1}=x_k-\alpha Ax_k+\beta(x_k-x_{k-1})
\]
on the SPD quadratic
\[
f(x)=\frac12x^{\mathsf T}Ax,
\qquad
0<\mu I\preceq A\preceq LI,
\qquad
\kappa=\frac L\mu>1,
\]
with the classical optimal quadratic parameters
\[
\alpha=\frac{4}{(\sqrt L+\sqrt\mu)^2},
\qquad
\beta=\left(\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}\right)^2,
\]
and the standard zero-velocity initialization \(x_{-1}=x_0\).

Write
\[
\rho=\frac{\sqrt\kappa-1}{\sqrt\kappa+1}.
\]
For every two-dimensional SPD problem of exact condition number \(\kappa\), the second-step objective ratio satisfies the sharp bound
\[
\boxed{
\frac{f(x_2)}{f(x_1)}
\le
G_2(\kappa)
=
\left[
\frac{(\sqrt\kappa-1)(5\sqrt\kappa+1)}{(\sqrt\kappa+1)(3\sqrt\kappa+1)}
\right]^2
}
\]
whenever \(x_1\ne0\). Equality is attained by starting in the largest-eigenvalue direction. Therefore
\[
f(x_2)\le f(x_1)
\quad\text{for every two-dimensional problem}
\]
if and only if
\[
\boxed{\kappa\le9+4\sqrt5}.
\]
Also
\[
G_2(\kappa)\uparrow\frac{25}{9}
\qquad(\kappa\to\infty).
\]

In three dimensions there is no finite condition-number-only bound at all. Define
\[
\lambda_*=\frac1\alpha
=\frac{(\sqrt L+\sqrt\mu)^2}{4}.
\]
For every \(\kappa>1\),
\[
\mu<\lambda_*<L.
\]
Thus
\[
A=\operatorname{diag}(\mu,\lambda_*,L),
\qquad x_{-1}=x_0=e_2
\]
has exact condition number \(\kappa\), yet
\[
x_1=0,
\qquad
x_2=-\beta e_2.
\]
The first gradient update hits the minimizer exactly and the momentum term immediately pushes the iterate away from it. Perturbing the middle eigenvalue gives arbitrarily large but finite values of \(f(x_2)/f(x_1)\). Hence dimension three is minimal for unbounded second-step objective amplification at fixed exact condition number.

For the exact example \(\kappa=4\),
\[
A=\operatorname{diag}\!\left(1,\frac94,4\right),
\qquad
\alpha=\frac49,
\qquad
\beta=\frac19,
\qquad
x_{-1}=x_0=e_2,
\]
and
\[
f(x_0)=\frac98,
\qquad
f(x_1)=0,
\qquad
f(x_2)=\frac1{72}.
\]
With the nearby middle curvature \(20/9\), the ratio is finite but already
\[
\frac{f(x_2)}{f(x_1)}
=\frac{516961}{6561}
>78.
\]

## Assumptions and scope
The quadratic is homogeneous only to simplify notation; translating a general strongly convex quadratic to its minimizer gives the same error recurrence. Exact arithmetic is assumed.

The parameters are the classical asymptotically optimal Heavy-Ball parameters for an SPD quadratic with known spectral endpoints \(\mu\) and \(L\). The initialization \(x_{-1}=x_0\) is the standard zero-momentum initialization, so the first completed update is an ordinary gradient step.

The two-dimensional statement fixes the matrix condition number exactly. In two dimensions this forces the spectrum to be precisely \(\{\mu,L\}\). The three-dimensional construction uses an additional interior eigenvalue while retaining the same exact endpoints.

The claim concerns the local objective ratio from the first completed step to the second. It does not contradict the asymptotic convergence rate of Heavy-Ball, nor does it claim divergence of the iterates.

## Proof
Let \(p_k(\lambda)\) be the modal multiplier defined by
\[
x_k^{(\lambda)}=p_k(\lambda)x_0^{(\lambda)}.
\]
Zero-velocity initialization gives
\[
p_0(\lambda)=1,
\qquad
p_1(\lambda)=1-\alpha\lambda,
\]
and
\[
p_2(\lambda)
=(1+\beta-\alpha\lambda)p_1(\lambda)-\beta
=(1-\alpha\lambda)^2-\beta\alpha\lambda.
\]

Put
\[
r=\sqrt\kappa,
\qquad
\rho=\frac{r-1}{r+1}.
\]
Then \(\beta=\rho^2\), while
\[
\alpha\mu=(1-\rho)^2,
\qquad
\alpha L=(1+\rho)^2.
\]
At the two endpoint curvatures,
\[
p_1(\mu)=\rho(2-\rho),
\qquad
p_2(\mu)=\rho^2(3-2\rho),
\]
and
\[
p_1(L)=-\rho(2+\rho),
\qquad
p_2(L)=\rho^2(3+2\rho).
\]
Therefore the endpoint adjacent-step amplification factors are
\[
g_\mu
=
\frac{|p_2(\mu)|}{|p_1(\mu)|}
=
\frac{\rho(3-2\rho)}{2-\rho},
\]
and
\[
g_L
=
\frac{|p_2(L)|}{|p_1(L)|}
=
\frac{\rho(3+2\rho)}{2+\rho}.
\]
Their difference is
\[
g_L-g_\mu
=
\frac{2(r-1)^2}{(r+3)(3r+1)}>0.
\]

For a two-dimensional matrix of exact condition number \(\kappa\), diagonalization gives
\[
f(x_j)
=
\frac12\sum_{\lambda\in\{\mu,L\}}
\lambda p_j(\lambda)^2 c_\lambda^2.
\]
Hence, whenever \(f(x_1)>0\),
\[
\frac{f(x_2)}{f(x_1)}
\]
is a weighted average of \(g_\mu^2\) and \(g_L^2\). Its exact supremum is therefore \(g_L^2\), attained on the \(L\)-eigenvector. Rewriting \(g_L\) in terms of \(r\) gives
\[
g_L
=
\frac{(r-1)(5r+1)}{(r+1)(3r+1)}.
\]
The condition \(g_L\le1\) is equivalent to
\[
r^2-4r-1\le0,
\]
so
\[
r\le2+\sqrt5
\]
and therefore
\[
\kappa\le(2+\sqrt5)^2=9+4\sqrt5.
\]
Taking \(r\to\infty\) gives \(g_L\to5/3\), hence \(G_2(\kappa)\to25/9\).

Now consider dimension three. Since
\[
\alpha\mu=(1-\rho)^2<1<(1+\rho)^2=\alpha L,
\]
the curvature
\[
\lambda_*=\frac1\alpha
\]
lies strictly between the endpoints. At this mode
\[
p_1(\lambda_*)=0,
\qquad
p_2(\lambda_*)=-\beta.
\]
Thus the diagonal matrix with spectrum \(\{\mu,\lambda_*,L\}\), started in the middle eigendirection, satisfies
\[
x_1=0,
\qquad
x_2=-\beta x_0,
\]
so Heavy-Ball leaves the minimizer immediately after landing on it.

For a perturbed interior curvature defined by
\[
\alpha\lambda=1+\varepsilon,
\]
one has
\[
p_1=-\varepsilon,
\qquad
p_2=\varepsilon^2-\beta(1+\varepsilon).
\]
Therefore
\[
\frac{f(x_2)}{f(x_1)}
=
\left[
\frac{\varepsilon^2-\beta(1+\varepsilon)}{\varepsilon}
\right]^2
\to\infty
\qquad(\varepsilon\to0).
\]
Because a two-dimensional SPD matrix with exact condition number \(\kappa\) has no room for an interior eigenvalue, the preceding finite bound proves that dimension three is minimal.

## Verification
The embedded `verify.py` checks all closed-form endpoint identities after substituting \(\rho=(r-1)/(r+1)\), verifies the threshold equation
\[
\kappa=9+4\sqrt5,
\]
and replays the exact \(\kappa=4\) reset example using rational arithmetic.

It also verifies the nearby finite-ratio witness
\[
A=\operatorname{diag}\!\left(1,\frac{20}{9},4\right),
\qquad
x_{-1}=x_0=e_2,
\]
for which
\[
p_1=\frac1{81},
\qquad
p_2=-\frac{719}{6561},
\]
and therefore
\[
\frac{f(x_2)}{f(x_1)}
=
\frac{516961}{6561}.
\]

The unboundedness statement is analytic; finite computation is not used as an infinite proof.

## Relationship to prior work
The 2014 Heavy-Ball convergence paper by Ghadimi, Feyzmahdavian, and Johansson states the Heavy-Ball recurrence and recalls Polyak's optimal quadratic parameters
\[
\alpha=\frac{4}{(\sqrt L+\sqrt\mu)^2},
\qquad
\beta=\left(\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}\right)^2.
\]
Its focus is global convergence and convergence rates, not adjacent objective spikes on quadratic spectra.

Danilova, Kulakova, and Polyak later gave a dedicated analysis of non-monotone Heavy-Ball behavior. They study peak effects for second-order recurrences, show that optimal Heavy-Ball parameters can produce strong non-monotonicity, and analyze endpoint eigenmodes under standard initialization. That work establishes the qualitative phenomenon and motivates restart and Lyapunov safeguards. The inspected full text does not state the interior-curvature reset \(\alpha\lambda=1\), the resulting unbounded second-to-first objective ratio for every \(\kappa>1\), the minimal dimension-three statement at fixed exact condition number, or the exact two-dimensional bound with frontier \(9+4\sqrt5\).

A published result in the comparison collection gives an analogous three-dimensional objective-spike phenomenon for exact-parameter Nesterov acceleration. That is a different recurrence: the gradient is evaluated at an extrapolated point, and its polynomial dynamics and sharp statements do not imply the Heavy-Ball formulas above.

Targeted searches for Heavy-Ball second-step amplification, hitting the minimizer and leaving it, the constant \(9+4\sqrt5\), and interior-eigenvalue reset behavior did not locate an implication-equivalent result.

## Limitations
The theorem concerns the first two completed updates with the classical spectral-endpoint parameters and zero-velocity initialization. Other initial momenta can have different transients.

The infinite ratio is a local adjacent-iterate phenomenon. It does not mean that \(f(x_2)\) is large relative to \(f(x_0)\); at the exact reset mode,
\[
f(x_2)=\beta^2f(x_0)<f(x_0).
\]
Thus the result should be read as a sharp failure of objective monotonicity and adjacent-step relative control, not as global divergence.

The literature already establishes Heavy-Ball peak effects and non-monotonicity in broader qualitative terms. The originality claim is specifically the exact dimension split, the unbounded second-to-first ratio for every nontrivial condition number, and the sharp two-dimensional formula and threshold.

## References
1. E. Ghadimi, H. R. Feyzmahdavian, and M. Johansson, “Global convergence of the Heavy-ball method for convex optimization,” arXiv:1412.7457, first version 2014-12-23; European Control Conference, 2015, DOI 10.1109/ECC.2015.7330562.
2. M. Danilova, A. Kulakova, and B. Polyak, “Non-monotone Behavior of the Heavy Ball Method,” arXiv:1811.00658, 2018-11-01.
3. B. T. Polyak, “Some methods of speeding up the convergence of iteration methods,” USSR Computational Mathematics and Mathematical Physics 4(5) (1964), 1–17, DOI 10.1016/0041-5553(64)90137-5.
4. J.-F. Aujol, Ch. Dossal, and A. Rondepierre, “Convergence Rates of the Heavy Ball Method for Quasi-strongly Convex Optimization,” SIAM Journal on Optimization 32(3) (2022), 1817–1842, DOI 10.1137/21M1403990.
5. “Two Accelerations for First-Order Optimization: A Comparative Review of Heavy Ball and Nesterov Acceleration,” Mathematics 14(19) (2026), 3460, DOI 10.3390/math14193460.
