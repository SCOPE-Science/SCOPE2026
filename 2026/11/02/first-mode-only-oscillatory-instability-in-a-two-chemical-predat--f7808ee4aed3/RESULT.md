# First-mode-only oscillatory instability in a two-chemical predator–prey system

## Finding

**Theorem (exact oscillatory mode-selection window).** On the square \(\Omega=(0,\pi)^2\) with componentwise homogeneous Neumann conditions, consider the following four-field reaction–cross-diffusion system, with \(g>0\):

\[
\begin{aligned}
\partial_t u_1&=\tfrac3{10}\Delta u_1+\Delta v_1+u_1(1-2u_1+u_2),\\
\partial_t u_2&=\tfrac3{10}\Delta u_2-\Delta v_2+u_2(3-2u_2-u_1),\\
\partial_t v_1&=3\Delta v_1+g u_2-v_1,\\
\partial_t v_2&=3\Delta v_2+g u_1-v_2.
\end{aligned}
\]

Write
\[
 g_1 =\frac{85+189\sqrt{105}}{100}=20.2167369476\ldots,\qquad
 g_2=\frac{55+72\sqrt{205}}{50}=21.7176623311\ldots.
\]
For **every** \(g_1<g<g_2\), the strictly positive homogeneous equilibrium \((u_1,u_2,v_1,v_2)=(1,1,g,g)\) is linearly stable in the homogeneous Neumann mode; it is oscillatory unstable in **exactly the two first spatial modes** \(\cos x\) and \(\cos y\), each with one conjugate eigenvalue pair in the open right half-plane; and it is strictly linearly stable in **every remaining** spatial Neumann mode. No spatial mode has a real nonnegative growth exponent. Thus precisely four real unstable dimensions are present, all oscillatory. At \(g=g_1\), precisely those first two modes have purely imaginary conjugate eigenvalue pairs, crossed transversely as \(g\) increases. At \(g=g_2\), the next spatial mode \(q=2\) has a purely imaginary pair and crosses transversely into instability. In particular, \((g_1,g_2)\) is the **maximal positive-gain interval** with exactly the first Neumann harmonics unstable and every other mode strictly stable.

This is a statement about the entire linearized PDE spectrum, not only a sampled dispersion curve. It does not assert the existence or stability of nonlinear time-periodic patterns.

## Assumptions and scope

All diffusion and reaction coefficients in the displayed system are fixed except \(g\). The coupling is the *linear cross-diffusion through two produced and decaying chemicals* in the model of Shanmugasundaram, Saha, Makinde and Chattopadhyay [1], with \(d_{11}=d_{21}=3/10\), \(d_{12}=d_{22}=1\), \(d_3=d_4=3\), \(\mu_1=1\), \(\mu_2=3\), \(\lambda_1=\lambda_2=2\), \(\eta_1=\eta_2=1\), \(a_1=a_2=g\) and \(b_1=b_2=1\). The source's sufficient diffusion inequalities hold strictly: \(4d_{11}d_3=4d_{21}d_4=18/5>1\). Every parameter is positive throughout the theorem's window. The square has corners, but the elementary Neumann spectral calculation applies to this rectangle without a smooth-boundary assumption.

Linear stability means all eigenvalues of the particular Fourier-mode matrix have strictly negative real parts; oscillatory instability means a nonreal conjugate pair has strictly positive real parts. The Neumann eigenfunctions are \(\cos(mx)\cos(ny)\), with eigenvalues \(q=m^2+n^2\), for integers \(m,n\ge0\).

## Proof

**Equilibrium and exact dispersion relation.** Substitution proves that \((1,1,g,g)\) is a positive equilibrium. For a Neumann eigenvalue \(q\), the linearization in the ordered variables \((u_1,u_2,v_1,v_2)\) is
\[
 M(q)=\begin{pmatrix}
 -A&1&-q&0\\
 -1&-A&0&q\\
 0&g&-E&0\\
 g&0&0&-E
 \end{pmatrix},\quad A=2+\frac{3q}{10},\quad E=1+3q.
\]
An exact determinant expansion gives
\[
 p_q(z):=\det(zI_4-M(q))=
 \bigl((z+A)(z+E)\bigr)^2+(z+E-gq)^2.
\tag{1}
\]
The expression is a sum of squares for every real \(z\). Since \(A,E>0\), it is strictly positive for real \(z\ge0\): the only possible unstable eigenvalues are nonreal. In particular \(p_q(0)>0\) for all \(q\ge0\), so this instability cannot be detected by a negative constant term of the characteristic polynomial.

**Homogeneous mode and exact first-mode crossing.** At \(q=0\), (1) factors into \((z+1)^2((z+2)^2+1)\), with spectrum \(-1,-1,-2+i,-2-i\). For any \(q>0\), (1) is the product of the conjugate-coefficient quadratics
\[
 (z+A)(z+E)\ \pm i(z+E-gq).
\]
For the plus sign, an imaginary root \(z=i\omega\) must obey
\[
 \omega^2+\omega=AE,\qquad gq=E+(A+E)\omega.
\]
The negative root \(\omega_-=(-1-\sqrt{1+4AE})/2\) would require \(gq<0\), impossible for \(g>0\). The positive root \(\omega_+=(\sqrt{1+4AE}-1)/2\) gives the **only positive-gain crossing**
\[
 g_c(q)=\frac{E+(A+E)(\sqrt{1+4AE}-1)/2}{q}.
\tag{2}
\]
The conjugate quadratic crosses simultaneously at the opposite frequency. Implicit differentiation of the plus-sign quadratic at \(z=i\omega_+\) yields
\[
 \frac{d\operatorname{Re}z}{dg}
 =\frac{q(2\omega_++1)}{(A+E)^2+(2\omega_++1)^2}>0.
\]
At \(g=0\), all roots are stable: \(-E,-E,-A+i,-A-i\). Since (2) is the only possible crossing for \(g>0\), exactly one conjugate pair becomes unstable for each \(q>0\) once \(g>g_c(q)\). For \(q=1\), \(A=23/10\) and \(E=4\), so (2) simplifies to \(g_c(1)=g_1\) as stated. For \(q=2\), \(A=13/5\) and \(E=7\), so \(g_c(2)=g_2\). The spatial multiplicity of \(q=1\) is exactly two.

**All higher modes, without truncation, and sharpness.** Write \(p_q(z)=z^4+a_1z^3+a_2z^2+a_3z+a_4\). The quartic Routh–Hurwitz test uses
\(\Delta_2=a_1a_2-a_3\) and \(\Delta_3=a_1a_2a_3-a_3^2-a_1^2a_4\). Direct exact expansion gives
\[
 \Delta_2=\frac{1000gq+38907q^3+121500q^2+114900q+35000}{500}>0,
\]
\[
 \Delta_3=\frac{1089q^2+1980q+1000}{25000}\,H(q,g),
\]
with
\[
 \begin{aligned}
 H(q,g)={}&-1000g^2q^2+g(2700q^2-1000q)\\
 &+9801q^4+86427q^3+155520q^2+102600q+20000.
 \end{aligned}
\]
For fixed \(q\ge2\), \(H\) is concave in \(g\) on \([0,g_2]\). Its minimum occurs at an endpoint. The value \(H(q,0)\) has strictly positive coefficients in \(q\); at the algebraic gain \(g_2\), exact substitution yields
\[
 \begin{aligned}
 H(2+h,g_2)={}&9801h^4+164835h^3\\
 &+(485978+720\sqrt{205})h^2\\
 &+(381024+1440\sqrt{205})h\ge0
 \end{aligned}
\]
for all \(h\ge0\), with equality only at \(h=0\). Therefore \(\Delta_3>0\) for all \(q\ge2\) and \(0\le g<g_2\). Also \(a_1,a_2>0\) and \(a_4=(AE)^2+(E-gq)^2>0\). Finally,
\[
 a_3(q,g)=\frac{297q^3+2349q^2+(2850-100g)q+700}{50}>0
\]
for \(0\le g\le g_2<23\). Thus all quartic Routh–Hurwitz inequalities hold for **every** \(q\ge2\) and \(g<g_2\). At \(g=g_2\), the second eigenvalue \(q=2\) has a transverse imaginary crossing by (2), and larger eigenvalues remain stable. For any \(g>g_2\), the \(q=2\) mode stays unstable because it has exactly one crossing for positive \(g\). Hence the interval with only \(q=1\) unstable is sharp at both endpoints.
Finally, for Neumann modes on \((0,\pi)^2\), the spectrum of \(-\Delta\) is exactly \(\{m^2+n^2:m,n\in\mathbb N_0\}\). Its only eigenvalue strictly between zero and two is \(q=1\), of multiplicity two. Combining the preceding conclusions proves the exact instability count for \(g_1<g<g_2\), including the sharp thresholds at \(g_1\) and \(g_2\). \(\square\)

## Verification

Run `python verify.py` with Python 3 and SymPy (verified with SymPy 1.14.0). It reconstructs the actual \(4\times4\) modal determinant, the compact factorization (1), exact Hurwitz coefficients and minors, the all-\(q\) positive shift certificate, the first-mode Routh sign, and both radical thresholds (2). In the explicit rational case \(g=21\), the first-mode polynomial is
\[
 p_1(z)=z^4+\frac{63}{5}z^3+\frac{5909}{100}z^2+\frac{2048}{25}z+\frac{9341}{25},
\]
and \(\Delta_3(1,21)=-15742961/3125<0\), giving a second exact first-mode instability check. Finite numerical eigenvalue diagnostics are not used as an infinite-mode certificate; the shifted polynomial proves the assertion for all higher modes.

## Relationship to prior work

The motivating 2026 source [1], in its model and Section 6, analyzes the same four-field chemical-mediated cross diffusion and emphasizes stationary Turing instability through the sufficient test \(A_4<0\), supplemented by numerical dispersion plots. Here \(A_4=p_q(0)>0\) for **every** \(q\), while an oscillatory mode is unstable. Thus its displayed sufficient test cannot imply this result. Earlier attraction–repulsion chemotaxis studies [2] report time-periodic modes with one motile population and two chemicals, while the prey-taxis system [3] has two predators and one prey but no pair of produced chemicals; their qualitative oscillatory mechanisms do not identify this four-field balanced-gain spectral threshold or the exact first-mode-only window. Wave instabilities in cross-diffusive systems are not claimed to be new in general. The contribution is the source-model-specific, exact analytic window and exhaustive Neumann mode selection.

## Limitations

This is a linearized spectral theorem on a rectangular habitat, not a claim about nonlinear periodic or traveling waves, their stability, or global positivity and boundedness of arbitrary trajectories. At the endpoint \(g=g_1\), the first Neumann eigenvalue is spatially double: a standard *simple-eigenpair* Hopf theorem cannot be invoked without equivariant/degenerate analysis. The theorem does not classify additional unstable modes beyond \(g_2\), or make claims for different domain spectra. The original model's cross-diffusion convention is used literally; physical interpretation of each flux and nonlinear well-posedness at large amplitude are separate questions. Literature comparisons cannot certify priority against every unpublished or inaccessible source.

## References

[1] G. Shanmugasundaram, J. Saha, O. D. Makinde and J. Chattopadhyay, *Asymptotic stability and diffusion-driven pattern formation in a predator-prey system with two chemicals*, arXiv:2604.18129, first submitted April 20, 2026. https://arxiv.org/abs/2604.18129

[2] P. Liu, J. Shi and Z.-A. Wang, *Pattern formation of the attraction-repulsion Keller-Segel system*, Discrete and Continuous Dynamical Systems B 18 (2013), 2597–2625. https://doi.org/10.3934/dcdsb.2013.18.2597

[3] K. Wang, Q. Wang and F. Yu, *Stationary and time-periodic patterns of two-predator and one-prey systems with prey-taxis*, arXiv:1508.03909. https://arxiv.org/abs/1508.03909

[4] V. N. Biktashev and M. A. Tsyganov, *Spontaneous traveling waves in oscillatory systems with cross diffusion*, Physical Review E 80 (2009), 056111. https://doi.org/10.1103/PhysRevE.80.056111
