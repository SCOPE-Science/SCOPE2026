# A sharp symmetry-breaking threshold for dissipation-limited Taylor dispersion

## Finding

Fix a normalized parallel-plate channel of transverse width one, passive-scalar molecular diffusivity \(D>0\), prescribed positive mean axial velocity \(q>0\), and shear-dissipation budget \(E\geq12q^2\). Consider every real velocity profile \(u\in H^1_0(0,1)\) satisfying \(\int_0^1u(y)\,dy=q\) and \(\int_0^1|u'(y)|^2\,dy=E\), without requiring the flow to be nonnegative or pressure-driven.

The long-time Taylor–Aris effective diffusivity is \(D_{\mathrm{eff}}=D+\mathcal T[u]/D\), where
\[
\mathcal T[u]=\int_0^1\left[\int_0^y(u(s)-q)\,ds\right]^2dy.
\]
Its complete constrained maximizer set undergoes an exact **reflection-symmetry-breaking transition** at
\[
 E_c=q^2(12+s_c),\qquad s_c=\int_0^1\bigl(G_\alpha''(y)-f''(y)\bigr)^2dy=0.370205669468\ldots,
\]
where \(f(y)=3y^2-2y^3-y\), \(\alpha=4.730040744862\ldots\) is the smallest strictly positive solution of \(\cos\alpha\cosh\alpha=1\), and \(G_k\) is defined below. Thus \(E_c/(12q^2)=1.030850472455\ldots\). Below and at the threshold the maximizer is unique and symmetric about the channel midpoint; above it there are **exactly two** mirror-related maximizers. Their antisymmetric velocity components are proportional to \(\sqrt{E-E_c}\).

For \(0<k\le\alpha\), set \(t=y-1/2\), \(a=k/2\), \(\Delta_k=\sin a\cosh a-\cos a\sinh a\), and
\[
G_k(y)=\frac{\sinh(a)\sin(kt)-\sin(a)\sinh(kt)}{k\Delta_k}.
\]
The denominator is nonzero throughout this range: \(\Delta_k\) vanishes at \(k=0\) and its derivative with respect to \(a\) is \(2\sin a\sinh a>0\) for \(0<a\le\alpha/2<\pi\). Moreover \(G_k\to f\) as \(k\downarrow0\). Let \(e_1\) be the positive, reflection-even first eigenfunction of the clamped beam operator \(\partial_y^4\), normalized by \(\int_0^1|e_1''|^2=1\). It is explicitly proportional to
\[
\frac{\cosh(\alpha(y-1/2))}{\cosh(\alpha/2)}-\frac{\cos(\alpha(y-1/2))}{\cos(\alpha/2)}.
\]
The full classification, with all equalities attained, is:

1. If \(E=12q^2\), the unique admissible profile is \(u(y)=6q y(1-y)\) and \(\max\mathcal T=q^2/210\).
2. If \(12q^2<E<E_c\), there is a unique \(k\in(0,\alpha)\) satisfying \(\int_0^1|G_k''-f''|^2=(E-12q^2)/q^2\). The unique maximizer is \(u(y)=q[1+G_k'(y)]\), and \(\max\mathcal T=q^2\int_0^1G_k(y)^2dy\).
3. If \(E=E_c\), the unique maximizer is \(u(y)=q[1+G_\alpha'(y)]\).
4. If \(E>E_c\), the two and only two maximizers are
\[
u_\pm(y)=q[1+G_\alpha'(y)]\pm\sqrt{E-E_c}\,e_1'(y).
\]
In the last two cases, writing \(t_c=\int_0^1G_\alpha^2=0.006144379658715\ldots\), the maximum obeys the **exact linear high-budget law**
\[
\max\mathcal T=q^2t_c+\frac{E-E_c}{\alpha^4}\qquad(E\ge E_c).
\]
In particular, the optimum just at the threshold improves the Poiseuille Taylor contribution by approximately \(29.03\%\), while requiring approximately \(3.085\%\) more shear dissipation.

## Assumptions and scope

Profiles are real Sobolev \(H^1_0(0,1)\) functions with zero velocity at both walls, fixed **positive** section mean, and *exact* prescribed squared-gradient energy. Long-time passive scalar transport has uniform transverse molecular diffusivity, reflecting solute-wall boundaries, and a steady axial velocity independent of the axial coordinate. For a physical channel of height \(h\) rather than the normalized unit channel, the Taylor contribution is multiplied by \(h^2\) under the corresponding nondimensionalization; all statements here use unit transverse width. No positivity restriction is imposed on \(u\). The energy is a viscous dissipation proxy for constant-viscosity shear, but the profiles are freely designed rather than required to arise from a sole uniform pressure gradient.

## Proof

**Taylor cell reduction.** With \(w=u-q\), let \(F_u(y)=\int_0^yw(s)ds\), whose values vanish at both walls. The unique mean-zero Neumann solution of \(-D\phi''=w\) satisfies \(D\phi'=-F_u\), and integrating the cell energy gives \(D_{\mathrm{eff}}-D=D\int|\phi'|^2=\mathcal T[u]/D\). This is the classical planar Taylor–Aris cell formula. It holds for the stated Sobolev class by density.

**Exactly separating throughput and excess energy.** Write \(p(y)=6y(1-y)\), \(u=qp+v\), where \(v\in H^1_0(0,1)\) and \(\int v=0\). Let \(F(y)=\int_0^y v\). Then \(F\in H^2_0(0,1)\), meaning \(F(0)=F(1)=F'(0)=F'(1)=0\), and every such \(F\) produces exactly one permissible \(v=F'\). Since \((qp)''=-12q\) is constant, integration by parts gives \(\int (qp)'v'=0\). Therefore
\[
 E=12q^2+\int_0^1|F''|^2,\qquad
 \mathcal T[u]=\int_0^1|qf+F|^2,
\]
where \(f=3y^2-2y^3-y\). The first identity proves the sharp feasibility boundary \(E\ge12q^2\), with equality uniquely at Poiseuille flow.

**Clamped spectral inequality and the reflection sector.** On \(H^2_0(0,1)\), the best constant in \(\|Z\|_2^2\le\Lambda\|Z''\|_2^2\) is \(\Lambda=\alpha^{-4}\). This follows from the standard clamped-beam eigenproblem \(Z''''=\lambda Z\): imposing four clamped conditions yields \(\cos k\cosh k=1\), and its first strictly positive root \(k=\alpha\) has a simple, midpoint-even eigenfunction \(e_1\) as displayed above. The next beam eigenvalue is strictly larger. The cubic forcing \(f\) is midpoint-odd, so \(\int fe_1=0\).

**The subcritical stationary family.** A constrained stationary point of \(\|qf+F\|_2^2\) at excess energy \(\|F''\|_2^2=r^2\) satisfies
\[
 (\mu\partial_y^4-I)F=qf\quad\text{with clamped conditions}.
\]
For \(\mu>\Lambda\), put \(k=\mu^{-1/4}\in(0,\alpha)\). The unique midpoint-odd homogeneous function \(H=qG_k\) solves \(H''''=k^4H\), \(H(0)=H(1)=0\), and \(H'(0)=H'(1)=-q\). Direct substitution of the displayed sine–sinh formula verifies these four conditions and the ODE; thus \(F=q(G_k-f)\) is the unique stationary solution. In the orthonormal clamped eigenbasis \(\{e_j\}\) with eigenvalues \(\lambda_j\),
\[
 F=\sum_j\frac{\langle qf,e_j\rangle}{\mu\lambda_j-1}e_j,
 \qquad
 r^2=\sum_j\lambda_j\frac{|\langle qf,e_j\rangle|^2}{(\mu\lambda_j-1)^2}.
\]
The first coefficient vanishes by parity, while at least one higher coefficient is nonzero. Consequently \(r^2\) decreases *strictly* with \(\mu\), increases strictly with \(k\), and runs from zero to \(q^2s_c\) as \(k\uparrow\alpha\). Finite convergence at the endpoint follows because \(\lambda_2>\lambda_1\) and the first coefficient is zero. This proves existence and uniqueness of \(k\) throughout the claimed interval.

**Global optimality rather than just stationarity.** For any stationary \(F_*\) satisfying \(qf+F_*=\mu F_*''''\) and any admissible competing \(F\) with the same excess energy \(r^2\), two integrations by parts and the constraint yield the exact identity
\[
\|qf+F\|_2^2-\|qf+F_*\|_2^2
=\|F-F_*\|_2^2-\mu\|(F-F_*)''\|_2^2.
\]
For \(\mu>\Lambda\), the sharp clamped inequality makes the right side *strictly negative* unless \(F=F_*\); hence each subcritical stationary profile is the unique global maximizer.

At \(\mu=\Lambda\), the same explicit solution is \(F_c=q(G_\alpha-f)\), midpoint-odd and orthogonal (also in the second-derivative energy form) to \(e_1\). The inequality now gives equality **only** for competitors \(F=F_c+te_1\). Their excess energies are exactly \(q^2s_c+t^2\) under the stated normalization. If \(r^2=q^2s_c\), only \(t=0\) is feasible, giving a unique critical optimum. If \(r^2>q^2s_c\), exactly the two amplitudes \(t=\pm\sqrt{r^2-q^2s_c}\) are feasible, proving the asserted pair and excluding all other maximizers. The primitive entering the dispersion is \(qG_\alpha+te_1\); odd/even orthogonality and \(\int e_1^2=1/\alpha^4\) give the exact high-budget law. Since \(e_1'\) is midpoint-odd and nonzero, the two flows are genuinely distinct and reflect into each other.

## Verification

The standalone `verify_taylor.py` checks the clamped root, boundary conditions, parity, energy orthogonality, stationary identities, analytic critical energy and dispersion coefficients, exact supercritical equality, and independent polynomial-Galerkin constrained maximization with multiple budgets and randomized feasible competitors. It uses Python with NumPy and SciPy, requires no external data, and executes as `python verify_taylor.py`. The reported values for \(\alpha\), \(s_c\), and \(t_c\) are numerical approximations; exact constants are the formulas above. Finite computations check formulas but do **not** replace the infinite-dimensional global optimality proof.

## Relationship to prior work

Taylor's 1953 dispersion paper established the basic shear-enhanced transport mechanism. Ng (2010) treats Taylor–Aris dispersion for planar no-slip/slip pressure-driven velocity profiles, including fixed-throughput comparisons. Marbach and Alim (2019), especially Section III.C and Appendix D.3, optimize a **cylindrical** channel's long-time dispersion over profiles constrained by the **mean and an \(L^2\) velocity-deviation norm**, obtaining a Bessel function profile; they do not impose planar no-slip data together with the **squared transverse velocity-gradient budget**. Lunasin et al. (2012) study periodic-box finite-time passive-scalar mixing for prescribed energy/power budgets, a different objective and geometry. The present claim is only the fixed-mean, fixed-dissipation, planar constrained maximizer classification and its exact reflection transition, not a discovery of Taylor dispersion or a general method for quadratic Hilbert-space optimization.

## Limitations

Maximization does not constrain \(u\ge0\), so sufficiently high budgets can produce backflow; it also does not enforce a Navier–Stokes or Stokes forcing realization. The dispersion coefficient is a long-time, passive, dilute-scalar prediction with reflecting impermeable walls and constant transverse diffusivity; transient mixing, finite axial boundaries, electrokinetic forcing cost, turbulence, and reactive walls are not treated. The literature comparison cannot establish absolute historical priority. The threshold is proved for the exactly stated functional and Sobolev class, not for other budgets such as \(\int u^2\).

## References

1. G. I. Taylor, “Dispersion of Soluble Matter in Solvent Flowing Slowly through a Tube,” *Proc. R. Soc. A* **219** (1953), 186–203; first published 25 August 1953. https://doi.org/10.1098/rspa.1953.0139
2. C.-O. Ng, “How does wall slippage affect hydrodynamic dispersion?”, *Microfluidics and Nanofluidics* **10** (2011), 47–57; first published online 10 June 2010. https://doi.org/10.1007/s10404-010-0645-9
3. E. Lunasin, Z. Lin, A. Novikov, A. L. Mazzucato, C. R. Doering, “Optimal mixing and optimal stirring for fixed energy, fixed power, or fixed palenstrophy flows,” *J. Math. Phys.* **53** (2012), 115611. https://doi.org/10.1063/1.4752098
4. S. Marbach and K. Alim, “Active control of dispersion within a channel with flow and pulsating walls,” *Phys. Rev. Fluids* **4** (2019), 114202, especially Sec. III.C and Appendix D.3. https://doi.org/10.1103/PhysRevFluids.4.114202
