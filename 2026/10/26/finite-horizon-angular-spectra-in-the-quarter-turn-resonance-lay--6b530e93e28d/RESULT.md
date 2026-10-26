# Finite-horizon angular spectra in the quarter-turn resonance layer

## Finding
Fix \(\kappa>1\), set \(P=\pi/2\) and \(a=(\kappa-\kappa^{-1})/2\), and let
\[
B_\kappa=\operatorname{diag}(\sqrt\kappa,\kappa^{-1/2}),\qquad
A_{N,t}=B_\kappa R_{P+t/N}B_\kappa^{-1},
\]
where \(R_\phi\) denotes planar counterclockwise rotation. For each integer \(N\ge1\), real detuning \(t\), and initial line \(V_\theta=B_\kappa\operatorname{span}(\cos\theta,\sin\theta)\), define the average of the *acute unoriented* principal angles
\[
\alpha_N(\theta,t)=\frac1N\sum_{j=1}^N
\measuredangle\!\left(A_{N,t}^{j-1}V_\theta,A_{N,t}^jV_\theta\right),
\qquad \Sigma_N(t)=\{\alpha_N(\theta,t):\theta\in\mathbb R/\pi\mathbb Z\}.
\]
Define the \(P\)-periodic function and its sliding average by
\[
g_\kappa(x)=P-\arctan\!\big(a|\sin(2x)|\big),\qquad
F_{\kappa,t}(\theta)=\int_0^1 g_\kappa(\theta+tu)\,du,\qquad
\Sigma_\infty(t)=F_{\kappa,t}(\mathbb R/P\mathbb Z).
\]
Then, **uniformly in the initial line**, for every \(N\ge1\) and every real \(t\),
\[
\sup_\theta|\alpha_N(\theta,t)-F_{\kappa,t}(\theta)|
\le \frac{(\kappa+a)|t|}{N},\qquad
 d_{\mathrm H}(\Sigma_N(t),\Sigma_\infty(t))
\le \frac{(\kappa+a)|t|}{N}.
\]
The limit is always a compact interval; its width \(W_\kappa(t)=\max F_{\kappa,t}-\min F_{\kappa,t}\) has the following **complete detuning law**. At \(t=0\),
\[
\Sigma_\infty(0)=[P-\arctan a,P],\qquad W_\kappa(0)=\arctan a.
\]
For \(t\ne0\), write \(r=|t|-P\lfloor|t|/P\rfloor\in[0,P)\). Then
\[
\boxed{W_\kappa(t)=\frac2{|t|}\int_0^{r/2}
\left[\arctan(a\cos(2u))-\arctan(a\sin(2u))\right]du.}
\]
Consequently, \(\Sigma_\infty(t)\) is a singleton **exactly** for nonzero \(t\in P\mathbb Z\), and has positive width for all other detunings. Its singleton value is the period mean \(\overline g_\kappa=P^{-1}\int_0^Pg_\kappa(u)du\).
For each nonzero integer \(m\), the collapse is a **linear cusp**:
\[
W_\kappa(mP+\varepsilon)
=\frac{\arctan a}{|m|P}|\varepsilon|
+O_{\kappa,m}(\varepsilon^2)\qquad(\varepsilon\to0).
\]
The scale \(1/N\) is sharp in the following precise sense. For any real sequence \(\delta_N\to0\), set \(t_N=N\delta_N\), form the same matrices with \(\phi_N=P+\delta_N\), and take the corresponding finite-horizon sets. If \(t_N\to0\), these sets converge to \([P-\arctan a,P]\); if \(t_N\to t\in\mathbb R\), they converge to \(\Sigma_\infty(t)\); if \(|t_N|\to\infty\), they converge to the singleton \(\{\overline g_\kappa\}\). All set convergences are Hausdorff. Thus the finite-horizon angular interval undergoes an exact \(1/N\) resonant detuning crossover, whereas fixed-parameter long-time spectra cannot be substituted uniformly in this boundary layer.

## Assumptions and scope
The matrix family is real, invertible, autonomous for each \((N,t)\), and has elliptic unit-modulus eigenvalues. The singular limit simultaneously varies the matrix parameter \(\phi_N=P+t/N\) and the observation horizon \(N\). The average is *unscaled discrete-time* rotation of unoriented real lines, and \(\kappa>1\) is fixed. The limit statements are for each fixed real detuning, uniformly for detunings in any prescribed compact set; there is no assertion of uniform error for unbounded \(t\) independent of \(N\).

## Proof
**1. Exact geometry of the resonant increment.** If \(e_x=(\cos x,\sin x)^\top\), then \(A_{N,t}^jV_\theta=B_\kappa\operatorname{span}(e_{\theta+j(P+t/N)})\). At exact quarter-turn, the determinant of the pair \((B_\kappa e_x,B_\kappa e_{x+P})\) is \(1\), while the scalar product equals \(-a\sin(2x)\). Since the unoriented acute angle is \(\operatorname{atan2}(|\det|,|\operatorname{dot}|)\), the increment is precisely \(g_\kappa(x)=P-\arctan(a|\sin(2x)|)\). Its least positive period is \(P\), and it is \(2a\)-Lipschitz.

**2. Quantitative finite-horizon reduction.** A continuous lift of the direction angle of \(B_\kappa e_x\) has derivative \(\big(\kappa\cos^2 x+\kappa^{-1}\sin^2 x\big)^{-1}\le\kappa\). Therefore, by the metric triangle inequality for principal angles, replacing a one-step rotation \(P+t/N\) by \(P\) changes each increment by at most \(\kappa|t|/N\), with the starting direction kept fixed. By the exact periodicity in step 1, this yields
\[
\left|\alpha_N(\theta,t)-\frac1N\sum_{j=0}^{N-1}g_\kappa(\theta+jt/N)\right|\le\kappa|t|/N.
\]
The left Riemann-sum error relative to \(\int_0^1g_\kappa(\theta+tu)du\) is at most \((2a)|t|/(2N)=a|t|/N\), uniformly in \(\theta\). Combining the inequalities proves the stated bound. The images of a common compact parameter space under two functions differing uniformly by at most \(\delta\) have Hausdorff distance at most \(\delta\), proving the set bound.

**3. Sliding-window extrema and the width formula.** The periodic function \(g_\kappa\) is even and strictly decreases with circular distance from \(0\) for distances in \([0,P/2]\). For \(t\ne0\), the length-\(|t|\) integral is the sum of \(\lfloor|t|/P\rfloor\) full periods plus one interval of length \(r\). For \(0<r<P\), the interval integral is largest when its center is \(0\pmod P\) and smallest when its center is \(P/2\pmod P\). This follows, for instance, by differentiating the centered integral \(J_r(c)=\int_{c-r/2}^{c+r/2}g_\kappa(u)du\): on \((0,P/2)\) its derivative is \(g_\kappa(c+r/2)-g_\kappa(c-r/2)<0\) using circular unimodality, and it is symmetric about both endpoints. The difference between extremal averages equals
\[
\frac2{|t|}\int_0^{r/2}\big[g_\kappa(u)-g_\kappa(P/2+u)\big]du.
\]
On this integration domain \(0\le u<P/2\), the bracket is exactly \(\arctan(a\cos2u)-\arctan(a\sin2u)\), giving the boxed formula. For \(r=0\) all windows are unions of full periods and the average is independent of initial line. Conversely, strict circular unimodality makes the residual-window maximum strictly exceed its minimum whenever \(0<r<P\). The case \(t=0\) is simply the range of \(g_\kappa\).

**4. Resonance cusps.** When \(r\downarrow0\), the integral in the width formula equals \(\tfrac r2\arctan a+O_\kappa(r^2)\). When \(r\uparrow P\), its full-period limit is zero and its terminal integrand is \(-\arctan a\), giving \(\tfrac{P-r}{2}\arctan a+O_\kappa((P-r)^2)\). At a nonzero resonance \(mP\), one of \(r\) and \(P-r\) equals \(|\varepsilon|\) to first order, while \(|t|=|m|P+O(|\varepsilon|)\). This proves the linear-cusp formula with the stated remainder.

**5. Sharpness of the detuning scale.** Substitute \(t_N=N\delta_N\) into the uniform estimate, which becomes \(\sup_\theta|\alpha_N(\theta,t_N)-F_{\kappa,t_N}(\theta)|\le(\kappa+a)|\delta_N|\to0\). As \(t_N\to t\in\mathbb R\), the sliding integrals converge uniformly in \(\theta\) by the Lipschitz estimate, including \(t=0\). For \(|t_N|\to\infty\), remove all complete periods from the sliding integral to obtain \(\sup_\theta|F_{\kappa,t_N}(\theta)-\overline g_\kappa|\le P\operatorname{osc}(g_\kappa)/|t_N|\to0\). The same image-set Hausdorff argument completes the three regimes.

## Verification
The supplementary reproducibility program `scripts/check_angular.py` independently computes principal angles from dot products and determinants, compares their finite averages with the sliding-integral approximation and its uniform bound, checks the extremal-width quadrature against direct optimization over sampled phases for several anisotropies and detunings, and checks the cusp slope. See `reports/check_output.txt` for the actual recorded run. Numerical diagnostics check finitely many instances; the statements for all \(N\), all real \(t\), and all lines follow only from the preceding proof.

## Relationship to prior work
Beyn and Hüls, *Angular spectra of linear dynamical systems in discrete time* (2024 preprint; 2025 journal), Example 2.8, gives fixed-matrix elliptic spectra and distinguishes rational from irrational rotation angles. Proposition 4.7 treats fixed-system finite-horizon Hausdorff convergence under a uniform Cauchy condition. Beyn and Hüls, *Angular maps for visualizing rotational dynamics* (2026), develops finite-horizon algorithms and angular maps. Neither inspected treatment gives the simultaneous matrix/horizon scaling \(P+t/N\), its quantitative limit, the width for every detuning, or the exact collapse and cusp laws. Standard periodic Riemann sums are a proof ingredient, not an asserted priority claim; a broader uninspected uniform near-resonance theorem remains a possible source of coverage.

## Limitations
The theorem treats only two-dimensional real constant conjugated rotations, the quarter-turn center, fixed anisotropy above one, and the unoriented one-dimensional principal-angle observable. It does not assert that the limiting finite-horizon set equals the infinite-time angular spectrum of any individual off-resonant matrix, nor establish a nonlinear-trajectory or higher-Grassmannian analogue.

## References
1. W.-J. Beyn and T. Hüls, *Angular maps for visualizing rotational dynamics*, CRC 1283 preprint 26018, submitted 2026-09-18; arXiv:2609.24753v1, 2026-09-21. https://www.sfb1283.uni-bielefeld.de/preprints/sfb26018.pdf
2. W.-J. Beyn and T. Hüls, *Angular spectra of linear dynamical systems in discrete time*, arXiv:2404.02694v1 (2024), *Discrete and Continuous Dynamical Systems B* 30 (2025), 1859–1902. https://www.sfb1283.uni-bielefeld.de/preprints/sfb24021.pdf
