# Sharp phase-centred stability and bang–bang rigidity for two-mode circle concentration

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), equipped with unnormalised angular measure \(dt\), and let \(\mathcal A_1=\operatorname{span}_{\mathbb C}\{1,e^{it}\}\). Fix \(0<a<\pi\). For every measurable \(w:\mathbb T\to[0,1]\) with \(\int_{\mathbb T}w\,dt=2a\), write
\[
Z(w)=\int_{\mathbb T}w(t)e^{it}\,dt,\qquad
\lambda(w)=\sup_{0\ne p\in\mathcal A_1}
  \frac{\int_{\mathbb T}w(t)|p(t)|^2\,dt}
       {\int_{\mathbb T}|p(t)|^2\,dt}.
\]
Assume \(Z(w)\ne0\). Let \(\phi=\arg Z(w)\), define the Fourier-phase-centred arc \(I_\phi=\{t: |t-\phi|_{\mathbb T}<a\}\), and define the equal exchanged masses
\[
m=\int_{I_\phi}(1-w)\,dt
  =\int_{\mathbb T\setminus I_\phi}w\,dt.
\]
Then
\[
\boxed{\frac{a+\sin a}{\pi}-\lambda(w)
  \ \ge\ \frac{2\sin a}{\pi}\left(1-\cos\frac m2\right).}
\]
The bound is sharp *for every feasible exchanged mass*: precisely,
\[
0\le m\le2\min(a,\pi-a),\qquad m<\frac{2\pi}{3}.
\]
For every \(m\) in this domain, equality occurs exactly for rotations of the characteristic mask of
\[
E_{a,m}=(-a+m/2,a-m/2)\ \cup\
 (-a-m/2,-a)\ \cup\ (a,a+m/2)
\]
(up to null sets), with all intervals taken on \(\mathbb T\). This includes \(m=0\). Therefore the sharp small-mass coefficient is \(\sin a/(4\pi)\): the deficit is at least \(\sin a\,m^2/(4\pi)+O_a(m^4)\), and the extremal masks attain the corresponding asymptotic equality. In particular, **fractional observation masks cannot saturate the stability inequality except by becoming characteristic functions**.

## Assumptions and scope
All masks are essentially bounded real functions with \(0\le w\le1\) almost everywhere and mass \(2a\). Angles and intervals are modulo \(2\pi\); \(|s|_{\mathbb T}\) denotes shortest angular distance to zero. The phase arc depends on the *first complex Fourier moment*, not on an arbitrary rotation or a closest arc in symmetric-difference distance. The theorem requires \(Z(w)\ne0\), so its phase is well-defined. The range of \(m\) is necessary and sufficient for the equality examples; it is not a claim that each mask realises every \(m\).

## Proof
**1. Exact spectral reduction.** In the orthonormal basis \(\{1,e^{it}\}/\sqrt{2\pi}\), the positive concentration operator is the Hermitian matrix
\[
C_w=\frac{1}{2\pi}\begin{pmatrix}2a&Z(w)\\\overline{Z(w)}&2a\end{pmatrix}
\]
(up to interchanging the conjugate off-diagonal entries, depending on the inner-product convention). Its eigenvalues are \((2a\pm |Z(w)|)/(2\pi)\). Hence
\[
\lambda(w)=\frac a\pi+\frac{|Z(w)|}{2\pi}.
\]
For the indicator \(w=\mathbf1_{(-a,a)}\), \(Z=2\sin a\), so the interval value is \((a+\sin a)/\pi\).

**2. The two sharp fixed-mass rearrangements.** Rotate the mask by \(-\phi\) so that \(Z(w)>0\) is real. Write \(I=(-a,a)\) and \(A(t)=1-w(t)\) on \(I\), \(B(t)=w(t)\) on \(\mathbb T\setminus I\). Then \(0\le A,B\le1\) and each has integral \(m\). Since \(\cos t\) decreases strictly as the angular distance \(|t|_{\mathbb T}\) increases from zero to \(\pi\), the bathtub rearrangement principle gives the *sharp* bounds
\[
\int_I A(t)\cos t\,dt
 \ \ge\ 2\int_{a-m/2}^{a}\cos t\,dt
 =2\bigl(\sin a-\sin(a-m/2)\bigr),
\]
\[
\int_{\mathbb T\setminus I}B(t)\cos t\,dt
 \ \le\ 2\int_{a}^{a+m/2}\cos t\,dt
 =2\bigl(\sin(a+m/2)-\sin a\bigr).
\]
These inequalities also hold when \(\cos t\) is negative on part of the domain; their sole premise is monotonicity in the geodesic distance. The hypotheses \(m\le2a\) and \(m\le2(\pi-a)\) make the displayed caps geometrically feasible. Strict monotonicity implies that equality in either inequality forces \(A\) or \(B\), respectively, to be the indicator of the displayed boundary caps, apart from null sets.

**3. The exact nonlinear loss.** Subtracting the missing contribution from the interval and adding the exterior contribution gives
\[
\begin{aligned}
|Z(w)|&=\int_{\mathbb T}w(t)\cos t\,dt\\
&\le2\sin a-2\bigl(\sin a-\sin(a-m/2)\bigr)
 +2\bigl(\sin(a+m/2)-\sin a\bigr)\\
&=2\sin a\left(2\cos\frac m2-1\right).
\end{aligned}
\]
Substitution in the spectral formula proves the claimed bound. Since \(|Z(w)|>0\) and \(\sin a>0\), this last bound forces \(2\cos(m/2)-1>0\). As \(m\le2\min(a,\pi-a)\le\pi\), it is equivalent to \(m<2\pi/3\).

**4. Sharpness and all equality cases.** For any \(m\) satisfying both geometric bounds and \(m<2\pi/3\), take \(w=\mathbf1_{E_{a,m}}\). The two cap inequalities become equalities, and direct integration yields
\[
Z(w)=2\sin(a-m/2)+2\sin(a+m/2)-2\sin a
=2\sin a\left(2\cos\frac m2-1\right)>0.
\]
Its phase is therefore \(0\), so the arc \((-a,a)\) in the calculation is precisely the mask's actual Fourier-phase-centred arc. The exchanged mass is \(m\), and equality follows. Conversely, equality in the concentration deficit forces equality in both sharp rearrangements; their uniqueness fixes \(w\) to be \(\mathbf1_{E_{a,m}}\) in the phase-centred coordinates. Rotations account for arbitrary phases.

**5. Sharp small-mass modulus.** Taylor expansion gives
\[
\frac{2\sin a}{\pi}\left(1-\cos\frac m2\right)
 =\frac{\sin a}{4\pi}m^2+O_a(m^4).
\]
Every \(a\in(0,\pi)\) admits equality examples for all sufficiently small positive \(m\), so no larger leading coefficient can hold.

## Verification
The rank-two Gram matrix and its two eigenvalues were computed directly. Both extremal rearrangements are exact consequences of the monotonicity of \(\cos t\) on \([0,\pi]\), and all equality cases are reconstructed from the strict version of that monotonicity. Symbolic trigonometric simplification verifies the displayed closed formula for \(Z(\mathbf1_{E_{a,m}})\). The accompanying `check_concentration.py` uses standard-library finite-grid sampling of characteristic and fractional masks, and evaluates exact cap integrals numerically; it prints a success message when its assertions pass. The proof is independent of those finite numerical experiments.

## Relationship to prior work
Abreu and Speckbacher (arXiv:2607.19192v1, first public July 21, 2026), Theorem 2.1, prove that an arc maximizes the concentration over measurable sets for analytic trigonometric polynomials of *every* degree. Their result gives the endpoint comparison but not the sharp phase-centred nonlinear stability modulus, the complete two-cap equality locus at prescribed exchanged mass, the bound \(m<2\pi/3\), or the extension from sets to fractional masks. The present result concerns only the first nonconstant Fourier dimension and independently supplies these quantitative and rigidity statements.

Zelent (arXiv:2610.01299v1) studies quantitative concentration stability for the continuous real-line Paley–Wiener space, with a different concentration operator and geometric setting; the accessible abstract does not give this exact two-dimensional circular profile. García-Ferrero and Ortega-Cerdá (2025, DOI 10.1007/s00220-025-05292-8) investigate weighted complex polynomials on a spherical domain, not the present circle Toeplitz operator. Quantitative Hardy–Littlewood rearrangement theory, including Cianchi and Ferone (2008, DOI 10.1112/jlms/jdm116), is a potential general framework for the two cap steps; the exact sharp formula and complete equality classification above are separately established, rather than assumed from a general estimate.

## Limitations
The theorem is not a stability theorem for analytic trigonometric polynomials of arbitrary degree, the real-line Paley–Wiener space, or the closest arc under unconstrained rotations. It does not define a phase when the first Fourier moment vanishes, and the bound \(m<2\pi/3\) is conditional on the phase being well defined. Its proof is elementary once the two-dimensional spectral reduction and the fixed-mass rearrangements are identified. Quantitative rearrangement literature remains a genuine related-work overlap risk; the available full-text evidence does not establish exhaustive novelty. No independent external validation is claimed.

## References
1. Luís Daniel Abreu and Michael Speckbacher, *Optimal concentration in the Paley–Wiener space*, arXiv:2607.19192v1 (2026-07-21), especially §2 and Theorem 2.1. https://arxiv.org/abs/2607.19192
2. Denis Zelent, *Stability of concentration in the Paley–Wiener space*, arXiv:2610.01299v1 (2026-10-01). https://arxiv.org/abs/2610.01299
3. María Ángeles García-Ferrero and Joaquim Ortega-Cerdá, *Stability of the Concentration Inequality on Polynomials*, Comm. Math. Phys. 406 (2025), article 112. https://doi.org/10.1007/s00220-025-05292-8
4. Andrea Cianchi and Adele Ferone, *A strengthened version of the Hardy–Littlewood inequality*, J. London Math. Soc. 77 (2008), 581–592. https://doi.org/10.1112/jlms/jdm116
