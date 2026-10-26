# A reset-rate sign reversal in core–shell correlations of an expanding Thomas–Fermi condensate

## Finding

An expanding one-dimensional Thomas–Fermi condensate repeatedly returned to its original profile by a *common* Poisson clock has two qualitatively distinct stationary spatial-correlation regimes. For any core radius \(0<u<1\), inner shell radius \(c>1\), and outer shell radius \(v>c\), the normalized condensate masses in the disjoint windows
\[
C=[-u x_0,u x_0],\qquad S=[-v x_0,-c x_0]\cup[c x_0,v x_0]
\]
have **strictly positive covariance for sufficiently small positive reset rate and strictly negative covariance for sufficiently large reset rate**. There is therefore at least one sign-change rate for every such choice of windows; uniqueness is not asserted.

The dependence is quantified by sharp asymptotics. Let \(\omega>0\) denote the initial longitudinal trap frequency. Define \(\lambda(t)\) by
\[
\lambda''(t)=\frac{\omega^2}{\lambda(t)^2},\qquad
\lambda(0)=1,\quad\lambda'(0)=0,
\]
and let \(t_c\) be the unique positive time satisfying \(\lambda(t_c)=c\). For \(a>0\), set
\[
F_a(\lambda)=
\begin{cases}
1,&1\le\lambda\le a,\\[2pt]
\dfrac{3a}{2\lambda}-\dfrac{a^3}{2\lambda^3},&\lambda>a.
\end{cases}
\]
For the stationary age \(T_r\sim\operatorname{Exp}(r)\), the macroscopic mass fractions are
\[
A_r=F_u(\lambda(T_r)),\qquad
B_r=F_v(\lambda(T_r))-F_c(\lambda(T_r)),\qquad
K(r)=\operatorname{Cov}(A_r,B_r).
\]
Writing
\[
C_0=\int_0^\infty F_u(\lambda(t))
\bigl[F_v(\lambda(t))-F_c(\lambda(t))\bigr]dt,
\]
we prove \(0<C_0<\infty\) and
\[
\boxed{K(r)=rC_0+o(r)\qquad(r\downarrow0).}
\]
In the strong-reset regime,
\[
\boxed{K(r)=-C_\infty\frac{e^{-rt_c}}{r^2}\bigl(1+o(1)\bigr)
\qquad(r\to\infty),}
\]
where
\[
\boxed{C_\infty=\frac{3\lambda'(t_c)^2}{c^2}
\left[F_u(1)-F_u(c)\right]>0.}
\]
The strong-reset leading constant does **not** depend on the outer shell radius \(v\) (provided \(v>c\)). The exponential onset is set solely by the time for the expanding edge to reach the shell's inner boundary.

For instance, at \(u=1/2,c=3/2,v=2,\omega=1\),
\[
t_c=\frac{\sqrt3/2+\operatorname{arcosh}\sqrt{3/2}}{\sqrt2},
\qquad C_\infty=\frac{89}{486}.
\]

## Assumptions and scope

The model is precisely the resetting-and-expansion Thomas–Fermi hydrodynamic approximation analyzed in Mesquita–Kulkarni–Majumdar–Sabhapandit [1]. At age \(t\), the **normalized longitudinal density** is
\[
\rho(x,t)=\frac{3}{4x_0\lambda(t)}
\left(1-\frac{x^2}{x_0^2\lambda(t)^2}\right)_+,
\qquad \int_{\mathbb R}\rho(x,t)\,dx=1.
\]
Here \(x_0>0\) is the initial half-width, \(\omega>0\), \(r>0\), and \(0<u<1<c<v\) are fixed. The system restarts its whole density configuration instantaneously after independent exponential waiting times of rate \(r\); hence its steady-state age has density \(re^{-rt}\). The random fractions \(A_r,B_r\) are the integrated **conditional mean densities** at that random age, not microscopic shot-noise counts. The claim is at the level of the hydrodynamic/large-particle Thomas–Fermi approximation; it neither includes finite-particle quantum fluctuations nor asserts an exact many-body Schrödinger theorem.

Both spatial windows are symmetric. The outer shell is initially empty because \(c>1\), while the central window contains a strictly positive and strictly decreasing mass fraction during expansion. This geometry directly distinguishes new mass arriving beyond the original edge from mass remaining in the core.

## Proof

**1. Exact fractions.** Integration of the displayed normalized parabola over \([-a x_0,a x_0]\) gives \(F_a(\lambda)\). Consequently the two stationary window fractions are exactly \(A_r,B_r\) as stated. For \(0<u<1<c<v\), \(A(t)=F_u(\lambda(t))\) is continuous and strictly decreasing from \(A(0)=F_u(1)>0\) to zero. The shell fraction \(B(t)=F_v(\lambda(t))-F_c(\lambda(t))\) is exactly zero through \(t_c\), and strictly positive afterward. It eventually decreases toward zero.

**2. Expansion scale.** Multiplication of the scale equation by \(\lambda'\) gives the conserved energy
\[
\lambda'(t)^2=2\omega^2\left(1-\frac{1}{\lambda(t)}\right).
\]
The unique expanding solution satisfies
\[
t(\lambda)=\frac{\sqrt{\lambda(\lambda-1)}+
\operatorname{arcosh}\sqrt\lambda}{\sqrt2\,\omega},
\qquad \frac{dt}{d\lambda}=
\frac1{\sqrt2\,\omega}\sqrt{\frac\lambda{\lambda-1}}.
\]
Thus \(\lambda(t)\sim\sqrt2\,\omega t\) as \(t\to\infty\); both \(A(t)\) and \(B(t)\) are \(O(t^{-1})\), while their product is \(O(t^{-2})\).

**3. Weak resetting.** For any nonnegative measurable \(H\), write \(\mathcal E_r[H]=r\int_0^\infty e^{-rt}H(t)dt\). Since \(A(t)B(t)\) is strictly positive for \(t>t_c\) and integrable at infinity,
\[
\mathcal E_r[AB]=r(C_0+o(1))
\]
by dominated convergence. Boundedness at small times and the \(O(t^{-1})\) tails imply
\[
\mathcal E_r[A]=O(r\log(1/r)),\quad
\mathcal E_r[B]=O(r\log(1/r)),
\]
where dimensionful constants inside logarithms can be fixed by any time reference. Their product is \(o(r)\). Subtraction proves \(K(r)=rC_0+o(r)>0\) for all sufficiently small \(r>0\).

**4. Strong resetting.** For \(t\in(t_c,t_v)\), where \(t_v>t_c\) satisfies \(\lambda(t_v)=v\), the shell fraction equals \(1-F_c(\lambda(t))\). Taylor expansion at \(\lambda=c\) gives the nonzero quadratic onset
\[
1-F_c(c+\delta)=\frac{3\delta^2}{2c^2}+O(\delta^3).
\]
As \(\lambda'(t_c)>0\),
\[
B(t)=\frac{3\lambda'(t_c)^2}{2c^2}(t-t_c)^2
+O((t-t_c)^3)\qquad(t\downarrow t_c).
\]
A one-sided Laplace estimate (substituting \(s=r(t-t_c)\) and bounding the later interval by its exponential tail) yields
\[
\mathcal E_r[B]\sim
\frac{3\lambda'(t_c)^2}{c^2}\frac{e^{-rt_c}}{r^2}.
\]
The identical estimate with the smooth factor \(A(t)\) gives
\[
\frac{\mathcal E_r[AB]}{\mathcal E_r[B]}\to A(t_c).
\]
Meanwhile \(\mathcal E_r[A]\to A(0)\), by bounded convergence after scaling age \(s=rt\). Hence
\[
\frac{K(r)}{\mathcal E_r[B]}
=\frac{\mathcal E_r[AB]}{\mathcal E_r[B]}-\mathcal E_r[A]
\to A(t_c)-A(0)<0.
\]
Combining the limits gives the displayed sharp negative asymptotic. It depends on \(u,c,\omega\) but not \(v\), because for every fixed \(v>c\) the first nonzero term of the shell fraction occurs immediately after \(t_c\).

**5. Crossing.** The variables \(A(t),B(t)\) are bounded and continuous, and the exponential-age integrals vary continuously with \(r>0\) by dominated convergence locally uniformly in rate. Since \(K(r)\) is positive at small rates and negative at large rates, the intermediate value theorem gives at least one zero \(r_*\in(0,\infty)\). No monotonicity of \(K\) or uniqueness of \(r_*\) is inferred.

**6. Exact illustrative coefficient.** With \(u=1/2\) and \(c=3/2\), the fractions at expansion factors one and \(c\) equal \(11/16\) and \(13/27\), respectively. Also \(\lambda'(t_c)^2=2\omega^2/3\). Thus \(C_\infty=(89/486)\omega^2\). The first-window and shell definitions remain arbitrary within the stated strict inequalities.

## Verification

Run `python verify_core_shell.py` after extracting the standalone companion file in the same folder. It uses only Python 3 and SciPy. It independently integrates the original parabola, evaluates the transformed renewal integrals with the regular coordinate \(y=\sqrt{\lambda-1}\), checks multiple geometries and reset rates, and compares the analytic leading coefficient to an exact rational value. The packaged program passed **269 numerical assertions**. For the benchmark \((u,c,v,\omega)=(1/2,3/2,2,1)\), it found \(t_c\approx1.07798736542215\), \(C_0\approx0.173803480307507\), and \(C_\infty=89/486\approx0.183127572016461\). It obtains \(K(0.01)\approx0.00104553568921\) and \(K(0.1)\approx-0.00113930945186\). Numerical results corroborate, rather than replace, the asymptotic proof for all parameters.

## Relationship to prior work

Mesquita, Kulkarni, Majumdar and Sabhapandit [1] establish the scale equation, steady-state random-age distribution and the full counting statistics for **one** centered spatial window, with the microscopic quantum fluctuations neglected at leading large-particle order. The density, scaling law and one-window fraction formula here are used as established inputs, not claimed as discoveries. The present statement instead concerns **joint** counts in two disjoint windows and proves a for-all-geometries sign reversal and its two sharp rate asymptotics. Although the joint covariance can be constructed from their common-age representation, the classification and strong-reset onset coefficient are not stated in the inspected paper.

The general renewal/conditional-mixture approach was studied earlier for simultaneously reset Brownian gases [2,3]; a recent perspective [4] surveys dynamically emergent correlations. These works motivate comparisons, but concern predominantly noninteracting-particle ensembles and do not by themselves yield the present Thomas–Fermi core-shell asymptotic for an interacting condensate. The possibility of an implicit corollary in general mixture theory remains a priority risk, and independent assessment is outstanding.

## Limitations

The theorem is exact **within** the self-similar Thomas–Fermi hydrodynamic approximation and Poisson whole-cloud reset protocol. It does not establish a finite-particle quantum covariance, a sign for microscopic shot-noise fluctuations, a unique crossing rate, or a corresponding classification for other geometries, arbitrary reset laws or non-Thomas–Fermi cloud profiles. Every asymptotic holds with \(u,c,v,\omega\) fixed; no boundary-uniform simultaneous limits are asserted. Since the source's one-window full counting law determines the common latent expansion variable, an implicit-prior-coverage risk cannot be excluded without further independent literature assessment.

## References

[1] N. Mesquita, M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110v1 (first public September 29, 2026), https://arxiv.org/abs/2609.37110. Especially free expansion, Eq. (37) and Eqs. (39)–(42), stationary age Eqs. (48)–(49), and one-window counting Eqs. (63)–(69) and (91)–(92).

[2] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme Statistics and Spacing Distribution in a Brownian Gas Correlated by Resetting*, Phys. Rev. Lett. 130, 207101 (2023), https://doi.org/10.1103/PhysRevLett.130.207101.

[3] G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, Phys. Rev. E 113, 014120 (2026), https://doi.org/10.1103/vmhz-6h5s.

[4] S. N. Majumdar and G. Schehr, *Dynamically Emergent Correlations*, arXiv:2603.03162 (2026), https://arxiv.org/abs/2603.03162.
