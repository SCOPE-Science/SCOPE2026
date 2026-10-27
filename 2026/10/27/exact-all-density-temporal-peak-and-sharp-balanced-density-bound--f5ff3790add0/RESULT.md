# Exact all-density temporal peak and sharp balanced-density bound for cold two-stream growth

## Finding
For an ideal one-dimensional collisionless cold electrostatic two-stream dispersion relation, let the two positive *squared* component plasma frequencies be \(a,b>0\), and let their distinct stream velocities have separation \(V>0\). There is exactly one positive wavenumber maximizing temporal growth. The unique positive number \(r\) satisfying
\[
\frac ba=\frac{r^3(r+2)}{2r+1}
\]
gives the maximum growth rate and its wavenumber **for every positive density ratio**, without a dilute-beam or equal-beam assumption:
\[
\boxed{\ k_*V=\frac{\sqrt a\,(r^2+r+1)}{\sqrt{2r+1}},\qquad
\gamma_* =\frac{\sqrt{3a}\,r}{2\sqrt{2r+1}}.\ }
\]
If the total squared plasma frequency \(P=a+b\) is fixed, then the sharp bound is
\[
\boxed{\ \gamma_*^2\leq P/8,\quad \text{with equality precisely when }a=b.\ }
\]
Thus balancing the two densities uniquely maximizes the already-optimized temporal growth rate at fixed total plasma-frequency weight. The optimum growth rate does not depend on the nonzero velocity separation \(V\), whereas its optimizing wavenumber scales as \(V^{-1}\).

## Assumptions and scope
For real \(k>0\) and complex temporal frequency \(\omega\) with time convention \(e^{-i\omega t}\), consider exactly
\[
1=\frac{a}{(\omega-ku_1)^2}+\frac{b}{(\omega-ku_2)^2},\qquad a,b>0,\quad u_2>u_1,
\]
where \(V=u_2-u_1>0\). Relabeling the streams makes the ordering harmless. Put \(z=\omega-ku_1\), \(K=kV\). The growth rate is the positive imaginary part of the unique unstable root of
\[
1=\frac a{z^2}+\frac b{(z-K)^2}.
\]
This is an idealized longitudinal, unmagnetized, zero-temperature, nonrelativistic, linear temporal problem. No claim concerns transverse electromagnetic, kinetic-temperature, collisional, nonlinear or spatial-amplification effects.

## Proof
**1. Complete instability interval.** Multiply the dispersion relation by \(z^2(z-K)^2\) to obtain
\[
F(z,K)=z^4-2Kz^3+(K^2-a-b)z^2+2aKz-aK^2=0.
\]
For each \(K>0\), the real rational function \(f(z)=a/z^2+b/(z-K)^2\) has exactly one solution \(f(z)=1\) on each of \(( -\infty,0)\) and \((K,\infty)\). On \((0,K)\), its unique minimum is attained when \(z/(K-z)=(a/b)^{1/3}\), and that minimum is \((a^{1/3}+b^{1/3})^3/K^2\). Consequently, with
\[
K_c=(a^{1/3}+b^{1/3})^{3/2},
\]
exactly two quartic roots are real and the other two form a nonreal conjugate pair for \(0<K<K_c\). For \(K>K_c\) all four are real, and for \(K=K_c\) the middle two coincide on the real axis. Thus the unstable root \(z(K)\) with \(\Im z(K)>0\) is unique and simple on \((0,K_c)\). As \(K\downarrow0\), the limiting polynomial is \(z^2(z^2-a-b)\), so the imaginary part tends to zero. It also tends to zero as \(K\uparrow K_c\). Therefore a strictly positive global maximum exists in \((0,K_c)\).

**2. Classify every stationary growth point.** Differentiate the dispersion relation along the simple unstable root. Writing
\[
w=\frac{z-K}{z}=1-\frac Kz,
\]
yields exactly
\[
z'(K)=\frac{b}{a w^3+b}.
\]
Since \(\Im z>0\), one has \(\Im w>0\). A stationary value of \(\Im z\) requires \(\Im z'=0\), and hence \(w^3\) is real. There are only two possible rays in the upper half-plane: \(w=r e^{i\pi/3}\) or \(w=r e^{2i\pi/3}\), with \(r>0\). In either case the defining dispersion equation implies
\[
K^2=(1-w)^2\left(a+\frac b{w^2}\right),
\]
which must be real and positive.

For \(w=r e^{i\pi/3}\), its imaginary part vanishes only if \(b/a=r^3(2-r)/(2r-1)\). Positivity of \(a,b\) forces \(1/2<r<2\), but then the right side reduces to \(-a(r^2-r+1)^2/(2r-1)<0\), an impossibility. For \(w=r e^{2i\pi/3}\), vanishing of its imaginary part instead gives precisely
\[
\frac ba=\frac{r^3(r+2)}{2r+1},\qquad
K^2=\frac{a(r^2+r+1)^2}{2r+1}>0.
\]
The function on the right of the first equation increases strictly from zero to infinity because its derivative is \(6r^2(r+1)^2/(2r+1)^2>0\). Therefore there is *at most one* stationary growth wavenumber. Existence of a positive interior maximum from step 1 shows that this candidate is attained and is the unique global maximum. From \(z=K/(1-r e^{2i\pi/3})\), direct rationalization gives
\[
\Re z_* =\frac{\sqrt a\,(r+2)}{2\sqrt{2r+1}},\qquad
\Im z_* =\frac{\sqrt{3a}\,r}{2\sqrt{2r+1}},
\]
and the formulas for \(k_*\) and \(\gamma_*\) follow. Every other wavenumber has smaller positive growth, or zero growth outside the unstable interval.

**3. Sharp fixed-total-density bound.** Express \(a=P/(1+b/a)\) in terms of \(r\). The preceding formula yields
\[
\gamma_*^2=\frac{3Pr^2}{4(r^4+2r^3+2r+1)}.
\]
The exact factorization
\[
r^4+2r^3-6r^2+2r+1=(r-1)^2(r^2+4r+1)\geq0
\]
proves \(\gamma_*^2\leq P/8\), with equality only at \(r=1\), equivalently \(a=b\). At equality, \(\gamma_*=\sqrt{P/8}\) and \(k_*V=\sqrt{3P/2}\). These cases attain the bound, completing sharpness.

## Verification
The standalone `verify.py` requires NumPy, SciPy and SymPy and runs `python verify.py`. It checks the two complex stationary-ray algebraic identities, the real positivity/negativity branches and the density-balance factorization symbolically. It then reconstructs roots from the full quartic and independently optimizes the growth curve for positive parameter triples, checking the analytical peak, instability cutoff and sharp balanced bound. A seeded set of 558 triples produced 7,254 successful numerical assertions. Numerical tests corroborate but do not replace the global proof.

## Relationship to prior work
The basic longitudinal cold two-stream dispersion and its dilute/equal-component limits are classical. Lapuerta and Ahedo's 2002 *General parametric analysis of the linear two-stream instability*, especially their cold-beam equation (14), discussion of CBI types and equations (15)–(16), supplies a directly matching forward dispersion and asymptotic peak formulas, but its inspected result does not give the all-positive-ratio exact stationary-ray parametrization, unique optimal wavenumber, or the sharp total-frequency balance inequality. Bret, Firpo and Deutsch (2004) study a broader electromagnetic wave-vector geometry, including longitudinal waves; their wider physical model does not automatically assert the exact present one-dimensional extremal formula. Bret, Gremillet and Dieckmann (2010), Table I, tabulate dilute and equal-density limits rather than a complete all-ratio peak. Rightley and Uzdensky (2018) treat symmetric delta-streams and quantum/kinetic extensions; their symmetric specialization is not a claim about arbitrary positive \(a,b\). This comparison is against substantive inspected material, not a proof of first discovery: unexamined classical plasma references could contain equivalent formulas.

## Limitations
This finding is for the ideal cold 1D electrostatic temporal branch only. At finite temperature, finite collisionality, relativistic drift or nonparallel perturbation, the fastest physical instability may be different. The bound fixes \(a+b\), not conserved stream kinetic energy; equal plasma weights need not optimize an experiment with velocity-dependent density constraints. Historic priority remains uncertain because the 2004 electromagnetic article's complete original PDF and all older textbook treatments were not fully inspected. Neither finite root sampling nor absence of an exact phrase in searched databases establishes originality.

## References
1. V. Lapuerta and E. Ahedo, *General parametric analysis of the linear two-stream instability*, Physics of Plasmas **9** (2002), 1513–1519, DOI: `10.1063/1.1464893`. The accessible archival copy has a visible download stamp of 26 April 2002.
2. A. Bret, M.-C. Firpo and C. Deutsch, *Collective electromagnetic modes for beam-plasma interaction in the whole k space*, Physical Review E **70** (2004), 046401, DOI: `10.1103/PhysRevE.70.046401`, published 4 October 2004.
3. A. Bret, L. Gremillet and M. E. Dieckmann, *Multidimensional electron beam-plasma instabilities in the relativistic regime*, Physics of Plasmas **17** (2010), 120501, DOI: `10.1063/1.3514586`.
4. S. Rightley and D. A. Uzdensky, *Linear electrostatic waves in two-population quantum plasmas*, arXiv:`1807.01458` (2018), especially section IV A and pages 19–20.
