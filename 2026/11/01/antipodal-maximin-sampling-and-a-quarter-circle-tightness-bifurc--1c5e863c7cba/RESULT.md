# Antipodal maximin sampling and a quarter-circle tightness bifurcation for three Fourier modes

## Finding
Consider the first three Fourier modes on the circle, measured on two equal, disjoint arcs. Among all admissible arc separations, the configuration maximizing the **least captured energy** is always uniquely antipodal. The configuration minimizing the **normalized frame potential** is instead strictly non-antipodal when each arc has half-width below \(\pi/4\), and becomes uniquely antipodal at and above that threshold.

Precisely, for \(0<\ell<\pi/2\) and \(\ell\le\theta\le\pi/2\), let
\[
E_{\theta,\ell}=([\theta-\ell,\theta+\ell]\cup[-\theta-\ell,-\theta+\ell])\pmod{2\pi}.
\]
Let \(V=\operatorname{span}\{1,e^{it},e^{2it}\}\subset L^2(\mathbb T,dt/(2\pi))\), and write \(G\) for the positive \(3\times3\) matrix representing \(f\mapsto\int_{E_{\theta,\ell}}|f(t)|^2dt/(2\pi)\) on \(V\). Put
\[
c=\frac{2\ell}{\pi},\qquad A=\frac{\sin\ell}{\ell},\qquad B=\frac{\sin(2\ell)}{2\ell}=A\cos\ell.
\]
Then
\[
\max_{\ell\le\theta\le\pi/2}\lambda_{\min}(G(\theta,\ell))
=c(1-B),
\]
with equality **only at** \(\theta=\pi/2\). Define the scale-invariant frame-potential defect \(\mathcal F(\theta,\ell)=\|c^{-1}G(\theta,\ell)-I_3\|_{\mathrm{HS}}^2\). Its unique minimizer is
\[
\theta_{\mathrm{FP}}(\ell)=
\begin{cases}
\displaystyle\arccos\sqrt{\frac{\cos(2\ell)}{4\cos^2\ell}},&0<\ell<\pi/4,\\
\pi/2,&\pi/4\le\ell<\pi/2.
\end{cases}
\]
Moreover,
\[
\min_\theta\mathcal F(\theta,\ell)=
\begin{cases}
\displaystyle A^2\left(2-\frac{1}{2\cos^2\ell}\right),&0<\ell<\pi/4,\\
2B^2,&\pi/4\le\ell<\pi/2.
\end{cases}
\]
For \(0<\ell<\pi/4\), the frame-potential penalty incurred by using the maximin design is **exactly**
\[
\mathcal F(\pi/2,\ell)-\min_\theta\mathcal F(\theta,\ell)
=\frac{A^2\cos^2(2\ell)}{2\cos^2\ell}>0.
\]
The bifurcation is square-root:
\[
\frac\pi2-\theta_{\mathrm{FP}}(\ell)\sim\sqrt{\pi/4-\ell}
\qquad(\ell\uparrow\pi/4),
\]
whereas the frame-potential penalty is asymptotic to \(\tfrac{32}{\pi^2}(\pi/4-\ell)^2\). In the narrow-arc limit, the frame-potential optimal design captures **asymptotically only half** the worst-case energy of the maximin design:
\[
\lim_{\ell\downarrow0}
\frac{\lambda_{\min}(G(\theta_{\mathrm{FP}}(\ell),\ell))}{\lambda_{\min}(G(\pi/2,\ell))}=\frac12.
\]

## Assumptions and scope
All objects are over the complex field; the three standard Fourier basis vectors are orthonormal in the ambient normalized circle space. The two observation arcs have identical half-width \(\ell\) and centers at \(\pm\theta\). The range \(\ell\le\theta\le\pi/2\) parametrizes all non-overlapping configurations up to common rotation and exchange of the two arcs; boundary contact is allowed and is immaterial to integrals. The total normalized observation measure is always \(c=2\ell/\pi\), so the trace of \(G\) is fixed at \(3c\). Only separations of **two** equal arcs for the fixed **three-mode** band are optimized. Eigenvalue minima are over unit vectors in \(V\), not over the whole infinite Fourier space.

## Proof
**Exact Gram matrix.** Integrating \(e^{int}\) over each centered arc gives \(\int_{E_{\theta,\ell}}e^{int}dt/(2\pi)=2\sin(n\ell)\cos(n\theta)/(\pi n)\) for nonzero integers \(n\). Consequently, with \(x=\cos\theta\), \(u=Ax\), and \(y=B(2x^2-1)\),
\[
\frac Gc=\begin{pmatrix}1&u&y\\u&1&u\\y&u&1\end{pmatrix}.
\]
Reflection symmetry splits the matrix into a one-dimensional antisymmetric block, with eigenvalue \(1-y\), and a symmetric block with eigenvalues
\[
\lambda_\pm=1+\frac y2\pm\sqrt{\frac{y^2}{4}+2u^2}.
\]
These are eigenvalues of \(G/c\). The actual eigenvalues of \(G\) are these times \(c\).

**Worst-case energy.** At \(\theta=\pi/2\), one has \(x=0\), \(y=-B\), and the three normalized eigenvalues are \(1-B,1,1+B\). For every \(x>0\), the identity
\[
\left(\frac{y^2}{4}+2A^2x^2\right)-\left(B+\frac y2\right)^2
=2x^2(A^2-B^2)>0
\]
holds because \(0<B<A\) for \(0<\ell<\pi/2\). Also \(B+y/2=B(x^2+1/2)>0\). Thus \(\lambda_-<1-B\) whenever \(x>0\). Since the smallest normalized eigenvalue never exceeds \(\lambda_-\), the unique maximin solution is \(x=0\), namely \(\theta=\pi/2\). This proves both the optimum and uniqueness over the complete admissible range.

**Frame-potential optimum.** With \(z=x^2\in[0,\cos^2\ell]\) and \(d=\cos^2\ell\), the squared Hilbert--Schmidt defect is exactly
\[
\mathcal F=4A^2z+2B^2(2z-1)^2
=A^2\bigl(4z+2d(2z-1)^2\bigr).
\]
It is strictly convex as a quadratic function of \(z\). The unconstrained unique minimum is at \(z_*=\tfrac12-\tfrac1{4d}=\tfrac{\cos2\ell}{4\cos^2\ell}\). If \(\ell<\pi/4\), then \(0<z_*<\cos^2\ell\); if \(\ell\ge\pi/4\), the minimum over the admissible range is at \(z=0\). Both cases give the displayed unique separation. Substitution supplies the minimum values and the exact defect penalty.

**Transition and narrow-arc loss.** Write \(\delta=\pi/4-\ell\downarrow0\). Then \(\cos^2\ell=\tfrac12+\delta+O(\delta^3)\) and \(z_*=\delta+O(\delta^2)\), yielding the square-root law by \(\pi/2-\arccos\sqrt{z_*}=\arcsin\sqrt{z_*}\). The penalty is \(4A(\pi/4)^2\delta^2+o(\delta^2)=\tfrac{32}{\pi^2}\delta^2+o(\delta^2)\). Finally, as \(\ell\downarrow0\),
\[
A=1-\frac{\ell^2}{6}+O(\ell^4),\qquad
B=1-\frac{2\ell^2}{3}+O(\ell^4),\qquad
\cos^2\theta_{\mathrm{FP}}=\frac14-\frac{\ell^2}{4}+O(\ell^4).
\]
Substituting into the exact expression for \(\lambda_-\) gives \(\lambda_{\min}(G(\theta_{\mathrm{FP}},\ell)/c)=\ell^2/3+O(\ell^4)\); at the antipodal design, the corresponding value is \(1-B=2\ell^2/3+O(\ell^4)\). The common factor \(c\) cancels and the ratio tends to \(1/2\). All expansions concern genuine analytic functions near the stated limits; no finite numerical sampling is used to infer uniform or global optimality.

## Verification
The standalone `checker.py` constructs the exact matrix, checks direct Fourier integration, the entire admissible geometry on multiple test widths, agreement between the analytical eigenvalue and Hilbert--Schmidt formulas, the exact optimality inequalities, the defect penalty, the critical square-root behavior, and the narrow-arc factor-two loss. In one reproducible execution, it passed 17,656 finite numerical assertions. That run is a consistency test only: the proof above independently covers all real \(0<\ell<\pi/2\) and all allowed separations.

## Relationship to prior work
Asipchuk and Drezels (2022 first public preprint) construct infinite exponential Riesz bases on split intervals and discuss their frame constants, but their Theorems 1.1--1.2 optimize neither a fixed three-frequency concentration Gram matrix nor two competing criteria over arc separation. Marceca, Romero and Speckbacher (2023 preprint) obtain broad non-asymptotic concentration eigenvalue-counting bounds, not an exact finite-band optimizer or this particular phase transition. Published finite-cyclic Fourier sampling results compare discrete Fourier point designs rather than two positive-width arcs. Existing exact-perfect-conditioning results for circular Fourier arc unions require at least as many arcs as observed consecutive modes; here there are only two arcs for three modes, so this is the natural first under-resourced geometry, with no exactly tight Gram matrix at these widths.

## Limitations
The classification assumes equal arc widths, two arcs, and exactly three consecutive frequencies. It does not assert an optimum over arbitrary measurable sets, unequal arcs, more Fourier modes, or alternative sampling weights. It provides exact finite-dimensional stability criteria but no general inverse-reconstruction algorithm. The novelty comparison uses inspected source results and current search records and cannot establish absolute historical priority; specialized design literature may contain earlier equivalent formulations. No independent mathematical validation has been performed.

## References
1. O. Asipchuk and V. Drezels, *Examples of exponential bases on union of intervals*, arXiv:2211.03821 (first public 2022-11-07), Canadian Mathematical Bulletin 66 (2023), 1296--1312. https://arxiv.org/abs/2211.03821 ; https://doi.org/10.4153/S0008439523000371.
2. F. Marceca, J. L. Romero and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685 (first public 2023-01-27), Archive for Rational Mechanics and Analysis 248 (2024), article 35. https://arxiv.org/abs/2301.11685 ; https://doi.org/10.1007/s00205-024-01979-9.
3. *Sharp Riesz conditioning for consecutive triples on finite cycles*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae.
4. *Consecutive Fourier bands minimize primitive-row frame potential at every modulus*, public research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-consecutive-fourier-bands-minimize-primitive-row-frame-potential--d824c1a982ba.
