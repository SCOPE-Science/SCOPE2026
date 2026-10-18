# Sharp universal period-slope minimum at the Schnakenberg Hopf boundary

## Finding
Consider the autonomous, two-species Schnakenberg kinetic system
\[
\dot x=a-x+x^2y,\qquad \dot y=b-x^2y.
\]
Fix any \(s\in(0,1)\) and, for a real unfolding parameter \(\mu\), set
\[
a=\frac{s(1-s^2-\mu)}2,\qquad
b=\frac{s(1+s^2+\mu)}2.
\]
There exists \(\varepsilon_s>0\) such that whenever \(0<\mu<\varepsilon_s\) the equations, in a fixed neighborhood of their positive equilibrium, have precisely one nonconstant periodic orbit up to time translation. It is orbitally asymptotically stable, and its **least** period in the original time variable obeys
\[
\boxed{T_s(\mu)=\frac{2\pi}{s}\left[1+
\frac{9s^4-5s^2+1}{6s^2}\,\mu+O_s(\mu^2)\right].}
\]
Thus the normalized right-hand period slope at the Hopf boundary is the explicitly bounded invariant
\[
\boxed{\lim_{\mu\downarrow0}\frac{T_s(\mu)/(2\pi/s)-1}{\mu}
=\frac{1+(3s-s^{-1})^2}{6}\ge\frac16,}
\]
with equality **if and only if** \(s=1/\sqrt3\). In particular, all admissible Hopf branches exhibit first-order nonlinear period slowing even though their linearized determinants, and hence their leading linear frequencies, are held fixed as \(\mu\) varies.

## Assumptions and scope
The parameters are real; \(0<s<1\), \(0<\mu<\varepsilon_s\), and \(\varepsilon_s\) is chosen less than \(1-s^2\) so that \(a,b>0\). The equilibrium is
\[
(x_*,y_*)=\left(s,\frac{b}{s^2}\right).
\]
Its Jacobian has trace exactly \(\mu\) and determinant exactly \(s^2\), for every \(\mu\) in the stated interval. The Hopf pair at \(\mu=0\) is \(\pm is\), and the real-part crossing speed with respect to \(\mu\) is \(1/2\). "Locally unique" means uniqueness among all sufficiently small periodic orbits arising in a fixed neighborhood of the equilibrium, not global uniqueness. The estimate \(O_s(\mu^2)\) allows its constant and admissible neighborhood to depend on fixed \(s\); no uniformity as \(s\downarrow0\) or \(s\uparrow1\) is asserted.

## Proof
Let \(q=x-s\), introduce \(p=s[(x+y)-(s+b/s^2)]\), and rescale time by \(\tau=st\). Direct substitution gives the *exact*, parameter-dependent polynomial system
\[
\begin{split}
\frac{dq}{d\tau}&=p+\frac\mu s q+
\frac{1-3s^2+\mu}{2s^2}q^2+
\frac2s qp-\frac1s q^3+\frac1{s^2}q^2p,\\
\frac{dp}{d\tau}&=-q.
\end{split}
\]
Set \(A=(1-3s^2)/(2s^2)\), \(B=2/s\), \(C=-1/s\), and \(D=1/s^2\). At \(\mu=0\), the linear equations are \(q'=p\), \(p'=-q\). To determine the small-cycle frequency, use a Poincaré–Lindstedt expansion with first-harmonic amplitude \(r>0\):
\[
\begin{aligned}
q&=r q_1+r^2q_2+r^3q_3+\cdots,\\
p&=r p_1+r^2p_2+r^3p_3+\cdots,\\
\mu&=m r^2+O(r^4),\qquad
\theta=\Omega\tau,\qquad \Omega=1+\omega_2r^2+O(r^4),\\
q_1&=\cos\theta,\quad p_1=-\sin\theta.
\end{aligned}
\]
The order-two equations yield, after fixing the fundamental-harmonic gauge,
\[
q_2=\frac A3\sin2\theta+\frac B3\cos2\theta,\qquad
p_2=-\frac A2+\frac A6\cos2\theta-\frac B6\sin2\theta.
\]
The order-three forcing in the first equation is
\[
h(\theta)=\frac m s q_1+2Aq_1q_2+B(q_1p_2+q_2p_1)+Cq_1^3+Dq_1^2p_1.
\]
Its resonant Fourier coefficients, defined by integrating against \(\cos\theta\) and \(\sin\theta\) over \([0,2\pi]\) and dividing by \(\pi\), are exactly
\[
[h]_{\cos\theta}=\frac{4ms^2-1}{4s^3},\qquad
[h]_{\sin\theta}=\frac{9s^4-5s^2+1}{12s^4}.
\]
Eliminating the resonances in \(q_3''+q_3=2\omega_2q_1+h'(\theta)\) forces
\[
m=\frac1{4s^2}>0,\qquad
\omega_2=-\frac{9s^4-5s^2+1}{24s^4}.
\]
A cubic complex normal-form calculation, with \(z=q+ip\) and linear part \(z'=-iz\), separately gives the resonant coefficient
\[
\boxed{c_{21}=-\frac1{8s^3}+i\frac{9s^4-5s^2+1}{24s^4}.}
\]
In particular, \(\Re c_{21}<0\) for every \(s>0\), while the real linear eigenvalue part crosses zero with positive speed \(1/(2s)\) in \(\tau\)-time. The nondegenerate supercritical Hopf theorem therefore ensures that the formal branch is a genuine locally unique orbitally attracting periodic orbit with an analytic/smooth amplitude-squared parametrization. Its physical-time angular frequency is \(s\Omega\). Since \(r^2=4s^2\mu+O_s(\mu^2)\), expanding \(2\pi/(s\Omega)\) gives the stated formula with the indicated remainder. Finally,
\[
\frac{9s^4-5s^2+1}{6s^2}
=\frac{(3s-s^{-1})^2+1}{6}
\]
is at least \(1/6\), with equality exactly when \(3s^2=1\), as claimed.

## Verification
Run `python3 verify.py` using Python 3 and SymPy. It checks the original Jacobian determinant and trace, the exact nonlinear coordinate transformation, both order-two harmonic identities, the order-three Fourier projections, the period coefficient, the sharp square identity, and a separately normalized cubic complex normal form with zero nonresonant remainder through degree three. The symbolic checker reports `CHECK_OK` after all assertions pass. Direct numerical shooting at \(s=1/2\), \(s=1/\sqrt3\), and \(s=0.85\) with \(\mu=0.001\) and \(0.003\) additionally showed normalized slopes tending toward the exact formula; numerical checks are corroboration only and are not part of the proof.

## Relationship to prior work
Schnakenberg's 1979 article introduced simple autocatalytic kinetic reaction systems with limit-cycle behavior. Liu, Shi, Wang and Feng (2013), Section 2, analyze *these very equations* under \(\beta=a+b\) and \(\alpha=b-a\). Their Theorem 2.2 proves that \(\alpha=\beta^3\), \(0<\beta<1\), is a supercritical stable Hopf point, and their period statement supplies only the leading \(2\pi/\beta+o(1)\) as the branch tends to the equilibrium. They calculate the **real part** of a cubic Hopf coefficient for stability but do not state the physical-time period derivative in the determinant-preserving unfolding, the strict global sign of that derivative, or its sharp \(1/6\) minimum. Their displayed intermediate complex bilinear quantities are pertinent potential antecedents; the present claim does not assert that computing a cubic Hopf normal form is new.

Kusbeyzi Aybar, Ferčec, Aybar and Dukarić (conference contribution; published 2021) also study Hopf stability of the Schnakenberg system. The accessible chapter abstract does not state a period-slope theorem, but its full text could not be inspected; publication-priority uncertainty remains. Al Noufaey (2021) derives Lindstedt–Poincaré frequency corrections for one- and two-term Galerkin approximations to a *spatial* Selkov–Schnakenberg reaction–diffusion model, varying a linear conversion parameter and including diffusion-dependent terms. The displayed one-term frequency increase with the conversion parameter is not a result for the present exact homogeneous kinetic ODE along a fixed-determinant feed path; the two-term Galerkin approximation is likewise not an exact period coefficient for that ODE. Erban and Kang (2023) study broader chemical networks admitting multiple stable cycles, rather than a near-Hopf physical-time slope of this fixed two-species kinetic system. Earlier results on exact period responses in other kinetic models do not imply this parameter-specific coefficient: their nonlinear vector fields and the relation between parameter drift and harmonic forcing differ.

## Limitations
This is a local result for a particular, explicitly defined path through each Hopf point; it is not a statement of period monotonicity for large-amplitude cycles, nor does it cover a different parameter path, a spatial reaction–diffusion pattern, or \(s\) outside \((0,1)\). The coefficient gives first-order slowing, not a claim of global frequency optimization away from onset. A relevant inaccessible 2021 chapter and the original full 1979 paper leave historical-priority risk. This scientific derivation is supported by an algebraic checker, not by an independent mathematical audit.

## References
1. J. Schnakenberg, "Simple chemical reaction systems with limit cycle behaviour," *Journal of Theoretical Biology* **81** (1979), 389–400; published 1979-12-07. DOI: 10.1016/0022-5193(79)90042-0.
2. P. Liu, J. Shi, Y. Wang, and X. Feng, "Bifurcation analysis of reaction–diffusion Schnakenberg model," *Journal of Mathematical Chemistry* **51** (2013), 2001–2019. DOI: 10.1007/s10910-013-0196-x. Freely accessible author manuscript: https://jxshix.people.wm.edu/shi/2013-Liu-Shi-Wang-Feng-JMC.pdf.
3. I. Kusbeyzi Aybar, B. Ferčec, O. O. Aybar, and M. Dukarić, "Limit Cycles of the Schnakenberg Chemical Reaction Model," *CHAOS 2020* conference chapter (first online 2021-12-15), pp. 101–109. DOI: 10.1007/978-3-030-70795-8_8.
4. R. Erban and H. Kang, "Chemical Systems with Limit Cycles," *Bulletin of Mathematical Biology* **85** (2023). DOI: 10.1007/s11538-023-01170-3.
5. K. S. Al Noufaey, "Stability analysis for Selkov-Schnakenberg reaction-diffusion system," *Open Mathematics* **19** (2021), 46–62, especially Section 6. DOI: 10.1515/math-2021-0008.
6. T.-W. Hwang and H.-J. Tsai, "Uniqueness of limit cycles in theoretical models of certain oscillating chemical reactions," *Journal of Physics A* **38** (2005), 8211–8223. DOI: 10.1088/0305-4470/38/38/003.
