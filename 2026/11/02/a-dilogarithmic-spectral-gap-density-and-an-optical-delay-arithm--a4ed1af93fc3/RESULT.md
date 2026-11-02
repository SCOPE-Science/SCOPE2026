# A dilogarithmic spectral-gap density and an optical-delay arithmetic discontinuity in binary wave crystals

## Finding

For a lossless, nondispersive, one-dimensional periodic binary wave crystal with two strictly positive layer impedances \(Z_1\ne Z_2\) and layer traversal times \(\tau_1,\tau_2>0\), let \(\mathcal G(\tau_1,\tau_2)\) be the limiting fraction of **angular-frequency length** occupied by forbidden Bloch propagation frequencies, as defined below. Write
\[
\kappa=\frac{|Z_1-Z_2|}{Z_1+Z_2}\in(0,1).
\]
If \(\tau_1/\tau_2\) is irrational, then this limit exists, is independent of both traversal times, and has the exact value
\[
\boxed{\mathcal G_{\mathrm{irr}}(\kappa)=\frac4{\pi^2}\bigl[\operatorname{Li}_2(\kappa)-\operatorname{Li}_2(-\kappa)\bigr].}
\]
Here \(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\) for \(|z|<1\). If the traversal times are equal, then
\[
\boxed{\mathcal G_{1:1}(\kappa)=\frac2\pi\arcsin\kappa,\qquad \mathcal G_{\mathrm{irr}}(\kappa)>\mathcal G_{1:1}(\kappa)\quad(0<\kappa<1).}
\]
Moreover, for all coprime positive integers \(p,q\), the rational-ratio limit \(\mathcal G(p,q)\) exists, and as \(\max\{p,q\}\to\infty\) through such pairs,
\[
\mathcal G(p,q)\longrightarrow\mathcal G_{\mathrm{irr}}(\kappa).
\]
In particular the sequence of ratios \(\tau_1/\tau_2=n/(n+1)\to1\) has gap densities approaching \(\mathcal G_{\mathrm{irr}}(\kappa)\), **not** the density at the exactly equal ratio. The infinite-frequency density is therefore discontinuous at the equal-traversal-time design.

## Assumptions and scope

Let \(E_j,\rho_j,\ell_j>0\) be constant longitudinal elastic modulus, density, and thickness of layer \(j\in\{1,2\}\). Repeat the two-layer cell periodically along the whole real line. In the time-harmonic equation \(-(E(x)y')'=\omega^2\rho(x)y\), impose continuity of displacement \(y\) and traction \(Ey'\) across the interfaces. Define \(c_j=\sqrt{E_j/\rho_j}\), \(\tau_j=\ell_j/c_j\), and \(Z_j=\sqrt{E_j\rho_j}\). The same scalar normal-incidence transfer relation holds for appropriate electromagnetic impedances in isotropic, positive, nondispersive dielectric stacks.

For real \(\omega\ge0\), let \(M(\omega)\in\mathrm{SL}_2(\mathbb R)\) be the period transfer matrix and let \(F(\omega)=\tfrac12\operatorname{tr}M(\omega)\). The forbidden set is
\[
\mathcal B=\{\omega>0:|F(\omega)|>1\},\quad
\mathcal G(\tau_1,\tau_2)=\lim_{\Omega\to\infty}\frac{\operatorname{Leb}(\mathcal B\cap(0,\Omega))}{\Omega}.
\]
This is Lebesgue density **in angular frequency \(\omega\)**, not a density of states, a finite-bandgap width, an energy-weighted fraction, or a fraction of a prescribed finite frequency window. All densities discussed below take the high-frequency limit with all physical parameters held fixed. The result is for strictly unequal impedances \(0<\kappa<1\); equal impedances give no open gaps and zero density.

## Proof

**1. Exact Floquet discriminant.** With state vector \((y,Ey')^T\), propagation through one layer is represented by
\[
M_j(\omega)=
\begin{pmatrix}
\cos(\omega\tau_j)&\sin(\omega\tau_j)/(\omega Z_j)\\
-\omega Z_j\sin(\omega\tau_j)&\cos(\omega\tau_j)
\end{pmatrix}.
\]
Each matrix has determinant one. Multiplying them and taking half the trace gives
\[
F(\omega)=\cos(\omega\tau_1)\cos(\omega\tau_2)
-m\sin(\omega\tau_1)\sin(\omega\tau_2),\qquad
m=\frac12\left(\frac{Z_1}{Z_2}+\frac{Z_2}{Z_1}\right)>1.
\]
A real Bloch phase exists exactly when \(|F|\le1\); \(|F|>1\) is forbidden. Put \(A=(1+m)/2\) and \(B=(m-1)/2\). Then \(A-B=1\) and \(B/A=\kappa^2\). On setting \(u=\omega(\tau_1+\tau_2)\) and \(v=\omega(\tau_1-\tau_2)\), the discriminant becomes \(F=A\cos u-B\cos v\).

**2. Irrational-traversal-time average.** If \(\tau_1/\tau_2\notin\mathbb Q\), the linear flow \(\omega\mapsto(\omega\tau_1,\omega\tau_2)\pmod{2\pi}\) is equidistributed in the two-torus. This follows by averaging every nonconstant Fourier character; its frequency \(h\tau_1+j\tau_2\) is nonzero for nonzero integer pair \((h,j)\). The map \((\phi_1,\phi_2)\mapsto(u,v)=(\phi_1+\phi_2,\phi_1-\phi_2)\) preserves normalized Haar measure (it is a finite covering of the torus). The boundary \(|A\cos u-B\cos v|=1\) has zero Haar measure because it is the zero locus of a nonconstant real-analytic function. Hence the indicator of the forbidden set is also equidistributed.

For fixed \(v\), the measure fraction in \(u\) with \(F>1\) is
\[
\frac1\pi\arccos\frac{1+B\cos v}{A}
=\frac2\pi\arcsin\!\left(\kappa|\sin(v/2)|\right).
\]
The analogous fraction for \(F<-1\) has the same \(v\)-average, by translating \(v\mapsto v+\pi\). Therefore
\[
\mathcal G_{\mathrm{irr}}(\kappa)
=\frac8{\pi^2}\int_0^{\pi/2}\arcsin(\kappa\sin t)\,dt.
\]
If \(I(\kappa)\) denotes the integral, differentiation under the integral is valid for \(0<\kappa<1\) and gives
\[
I'(\kappa)=\int_0^{\pi/2}\frac{\sin t}{\sqrt{1-\kappa^2\sin^2t}}\,dt
=\frac{\operatorname{artanh}\kappa}{\kappa}.
\]
Because \(I(0)=0\), termwise integration of \(\operatorname{artanh}\kappa/\kappa=\sum_{j\ge0}\kappa^{2j}/(2j+1)\) yields
\[
I(\kappa)=\sum_{j\ge0}\frac{\kappa^{2j+1}}{(2j+1)^2}
=\tfrac12[\operatorname{Li}_2(\kappa)-\operatorname{Li}_2(-\kappa)],
\]
which proves the first box.

**3. Equal traversal times and a strict density gap.** If \(\tau_1=\tau_2=\tau\), the discriminant is \(F=1-(1+m)\sin^2(\omega\tau)\). Hence \(|F|>1\) holds on exactly a proportion \(2\arcsin\kappa/\pi\) of each \(\pi/\tau\) period.

For strict comparison define \(f(v)=2\arcsin(\kappa\sin(v/2))\) on \([0,\pi]\). A direct derivative gives
\[
f''(v)=-\frac{\kappa(1-\kappa^2)\sin(v/2)}{2[1-\kappa^2\sin^2(v/2)]^{3/2}}<0\quad(0<v<\pi).
\]
Since \(f(0)=0\) and \(f(\pi)=2\arcsin\kappa\), strict concavity implies \(\pi^{-1}\int_0^\pi f(v)\,dv>f(\pi)/2\). The irrational density is \((2/\pi)\) times this average and the equal-time density is \(f(\pi)/\pi\); their strict ordering follows.

**4. Rational approximants and the arithmetic discontinuity.** If \(\tau_1/\tau_2=p/q\) in lowest positive terms, after rescaling frequency the flow is the closed torus geodesic \(t\mapsto(pt,qt)\pmod{2\pi}\). Its frequency-gap density is its normalized period average, so the limit exists. Let coprime \((p_n,q_n)\) satisfy \(\max(p_n,q_n)\to\infty\). For each fixed nonzero integer Fourier pair \((h,j)\), the line average of \(e^{i(hp_n+jq_n)t}\) eventually vanishes, since any integer solution of \(hp_n+jq_n=0\) would require \((p_n,q_n)\) to be a fixed coprime direction determined by \((h,j)\). Thus the line measures converge weakly to two-torus Haar measure, first on trigonometric polynomials and then on continuous functions. The forbidden-set boundary has zero Haar measure, so its indicator averages converge to \(\mathcal G_{\mathrm{irr}}\). Taking \((p_n,q_n)=(n,n+1)\) proves discontinuity at the equal ratio.

**5. Contrast laws.** From the convergent dilogarithm series, as \(\kappa\downarrow0\),
\[
\mathcal G_{\mathrm{irr}}=\frac8{\pi^2}\left(\kappa+\frac{\kappa^3}{9}+O(\kappa^5)\right),\qquad
\mathcal G_{1:1}=\frac2\pi\left(\kappa+\frac{\kappa^3}{6}+O(\kappa^5)\right).
\]
Their density ratio tends to \(4/\pi\). Writing \(\varepsilon=1-\kappa\downarrow0\), differentiation of the dilogarithmic formula gives
\[
1-\mathcal G_{\mathrm{irr}}=\frac{4\varepsilon}{\pi^2}\left[\log\frac2\varepsilon+1\right]
+O(\varepsilon^2\log(1/\varepsilon)),\qquad
1-\mathcal G_{1:1}=\frac{2\sqrt2}{\pi}\sqrt\varepsilon+O(\varepsilon^{3/2}).
\]
The first deficit is logarithmically corrected linear; the second is square-root. These are consequences of the same exact density theorem, not separate independent claims.

## Verification

Run `python verify.py` with Python 3 and `mpmath` installed. The code checks independent transfer-matrix multiplication against the scalar Floquet discriminant; evaluates the universal density through dilogarithms, the original phase integral and independent angular quadrature; compares direct high-frequency sampling for an irrational traversal-time ratio and exactly equal traversal times; checks reciprocal impedance invariance, strict density ordering, and weak/strong contrast asymptotics. The finished package's checker passed 88 diagnostic assertions. These finite checks are not substitutes for the equidistribution, concavity and limit arguments above.

For \(Z_1/Z_2=2\), the resulting irrational-ratio gap density is approximately \(0.273667040349\), versus \(0.216346895939\) for equal traversal times. The difference of approximately \(0.057320144410\) is a fraction of angular-frequency length, not an absolute frequency or intensity.

## Relationship to prior work

The exact binary-layer Floquet discriminant, the criterion for permitted Bloch propagation, and the special behavior of equal optical traversal times are established in the primary literature, especially Iantchenko (2010, equations (3)–(7) and the equal-traversal-time discussion) and Xiao–Zhang–Chan (2014, equation (2) and Appendix A). Their relevant inspected material treats spectral bands, resonances or interface states. The present claim concerns a different observable: the exact infinite-frequency **Lebesgue fraction of forbidden frequencies**, its dilogarithmic evaluation for irrational traversal-time ratios, its strict comparison with the exactly commensurate case, and its discontinuity under high-order rational approximation. Neither the elementary existence of a band gap nor the prior transfer-matrix formula is asserted as new. A prior full spectral discriminant provides the starting data but does not itself state or evaluate the frequency-occupancy invariant or this discontinuity.

## Limitations

The limiting fraction need not approximate a prescribed finite frequency window, especially near a high-order rational traversal-time ratio. The ratio is considered irrational mathematically, not certified by finite experimental precision. If material dispersion or losses become significant at high frequency, the high-frequency limit need not describe measured spectra. Frequency-weighting by \(\omega^2\), oblique incidence, transverse mode coupling and disordered layering are outside scope. The formula is not an integrated density of states and implies no optimality for a specific first band gap. Historical priority beyond inspected primary literature and the targeted scholarly searches is not guaranteed.

## References

1. A. Iantchenko, *Resonance spectrum for one-dimensional layered media*, arXiv:1005.2743v1 (first submitted 2010-05-16), especially equations (3)–(7), Section 2 and Section 7; https://arxiv.org/abs/1005.2743.
2. M. Xiao, Z. Q. Zhang and C. T. Chan, *Surface Impedance and Bulk Band Geometric Phases in One-Dimensional Systems*, arXiv:1401.1309v1 (first submitted 2014-01-07), *Physical Review X* **4**, 021017 (2014), especially equation (2), Section II.A and Appendices A–D; https://arxiv.org/abs/1401.1309; doi:10.1103/PhysRevX.4.021017.
