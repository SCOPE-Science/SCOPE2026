# Two distinct exact prime-two Lyapunov spectra in a Blaschke Anosov torus map

## Finding
For the symmetric real-parameter Blaschke Anosov diffeomorphism \(T_\mu\) below, every \(0<\mu<1\) has exactly two geometrically distinct primitive period-two orbits. Their unstable Lyapunov exponents **per iterate** are explicitly
\[
\chi_\pm(\mu)=\operatorname{arcosh}\!\left(1+\frac{1-\mu^2}{2+\mu+\mu^2\mp\mu\sqrt{\mu^2+2\mu+5}}\right),
\qquad 0<\chi_-(\mu)<\chi_+(\mu).
\]
The positive-return multipliers for the respective two-iterate linearizations are \(e^{2\chi_\pm(\mu)}\), with reciprocal stable multipliers. At the cat-map limit the gap has the sharp onset
\[
\chi_+(\mu)-\chi_-(\mu)=\mu+O(\mu^2),\qquad \mu\downarrow0.
\]
At the singular end of the analytic hyperbolic family, the two exponents vanish at **different** rates:
\[
\chi_\pm(\mu)=\sqrt{2\pm\sqrt2}\,\sqrt{1-\mu}+O((1-\mu)^{3/2}),
\qquad \mu\uparrow1,
\]
so their ratio converges to the exact constant \(1+\sqrt2\). This is a complete, orbit-resolved prime-two expansion spectrum, not an assertion about all higher periods or about smoothness of the global splitting.

## Assumptions and scope
On the two-torus \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\), for \(0\le\mu<1\) and the symmetry parameter fixed at zero, define
\[
T_\mu(s,t)=\left(2s+t+f_\mu(s),\,s+t+f_\mu(s)\right)\bmod1,
\quad f_\mu(s)=\frac1\pi\arctan\frac{\mu\sin(2\pi s)}{1-\mu\cos(2\pi s)}.
\]
The denominator in the arctangent is strictly positive. In particular \(f_\mu\) is smooth, periodic, and odd on the circle, and \(T_0\) is the cat map with matrix \(A=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)\). A primitive period-two orbit is a pair of distinct torus points interchanged by \(T_\mu\). A positive unstable Lyapunov exponent per iterate for a two-cycle is half the logarithm of the unstable eigenvalue of the two-step derivative. The expansions at endpoints are one-sided within this parameter range; \(\mu=1\) is excluded.

For clarity define
\[
r(\mu)=\sqrt{\mu^2+2\mu+5},\qquad
s_\pm(\mu)=\frac1{2\pi}\arccos\left(\frac{\mu-1\pm r(\mu)}4\right),
\]
where \(0<s_+(\mu)<s_-(\mu)<1/2\). The exact two-cycles are
\[
\mathcal O_\pm=\bigl\{(s_\pm,2s_\pm),\,(-s_\pm,-2s_\pm)\bigr\}\pmod1.
\]

## Proof
**1. An algebraic solution of the antipodal two-cycle equations.** Oddness gives \(T_\mu(-s,-t)=-T_\mu(s,t)\). A point \((s,2s)\) is sent to \((-s,-2s)\) modulo one if and only if \(5s+f_\mu(s)\in\mathbb Z\); oddness then forces its second iterate to return. Put \(z=e^{2\pi i s}\). The arctangent definition yields the exact phase identity
\[
e^{2\pi i f_\mu(s)}=\frac{z-\mu}{z(1-\mu z)}.
\]
Therefore \(5s+f_\mu(s)\in\mathbb Z\) is equivalent to
\[
0=z^5-\mu z^4+\mu z-1
=(z-1)\left[z^4+(1-\mu)(z^3+z^2+z)+1\right].
\]
For the nonzero representatives \(s\in(0,1/2)\), let \(w=z+z^{-1}=2\cos(2\pi s)\). Division of the quartic by \(z^2\) gives
\[
w^2+(1-\mu)w-(1+\mu)=0,
\quad w_\pm=\frac{\mu-1\pm r(\mu)}2.
\]
The derivatives of the two roots are \(w_\pm\prime(\mu)=[1\pm(\mu+1)/r(\mu)]/2>0\), since \(r(\mu)>\mu+1\). Their endpoint ranges run from \((-1\pm\sqrt5)/2\) at zero to \(\pm\sqrt2\) at one, so both stay strictly between \(-2\) and \(2\) for \(0\le\mu<1\). The corresponding upper-half-circle roots are the stated \(s_\pm\), and their conjugates give \(-s_\pm\). Thus the four displayed points constitute two distinct primitive two-cycles.

**2. Exhaustiveness.** Direct differentiation gives
\[
p_\mu(s):=1+f'_\mu(s)=\frac{1-\mu^2}{1-2\mu\cos(2\pi s)+\mu^2}>0,
\quad DT_\mu(s,t)=B_\mu(s)=\begin{pmatrix}1+p_\mu(s)&1\\p_\mu(s)&1\end{pmatrix}.
\]
Every such matrix is strictly positive and has determinant one. Hence every derivative of \(T_\mu^2\), being the product of two strictly positive determinant-one matrices, is itself strictly positive and determinant one. For any positive \(2\times2\) matrix \(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) with \(ad-bc=1\), one has \(ad>1\), whence \(\operatorname{tr}>2\sqrt{ad}>2\). Consequently no fixed point of \(T_\mu^2\) has an eigenvalue one, for any \(\mu\in[0,1)\). By the implicit function theorem and compactness of the torus, the number of fixed points of \(T_\mu^2\) is locally constant in \(\mu\): every old fixed point persists uniquely, and an otherwise unaccounted sequence of new fixed points would have a limiting fixed point, contradicting local uniqueness. The interval \([0,1)\) is connected. At \(\mu=0\), the cat map has
\[
\#\operatorname{Fix}(T_0^2)=\bigl|\det(A^2-I)\bigr|=5.
\]
Finally, \(T_\mu\) has a unique fixed point: its equations imply \(s+f_\mu(s)\in\mathbb Z\), while \(s+f_\mu(s)\) increases strictly by one across a lift of the circle, since its derivative is \(p_\mu(s)>0\). Its only circle solution is \(s=0\), giving \(t=0\). Thus there are exactly four primitive period-two points, all constructed in step 1.

**3. Orbit multipliers.** Since \(p_\mu\) is even, the derivative at both members of either orbit equals \(B_\mu(s_\pm)\). Thus \(DT_\mu^2=B_\mu(s_\pm)^2\) on that orbit. A positive determinant-one matrix with trace \(2+p\) has eigenvalues \(e^{\pm\operatorname{arcosh}(1+p/2)}\). Using \(2\cos(2\pi s_\pm)=w_\pm\) in \(p_\mu\) gives
\[
p_\pm(\mu)=\frac{2(1-\mu^2)}{2+\mu+\mu^2\mp\mu r(\mu)},
\]
which gives the claimed \(\chi_\pm\). The denominators are positive by the original positive Poisson kernel. Because \(w_+>w_-\), the positive kernel satisfies \(p_+>p_-\) for \(\mu>0\). As arcosh is increasing, the inequality \(\chi_+>\chi_-\) is strict throughout \((0,1)\).

**4. Sharp endpoints.** At \(\mu=0\), \(w_\pm=(-1\pm\sqrt5)/2\), \(p_\pm=1\), and \(\chi_\pm=\operatorname{arcosh}(3/2)\). Differentiating the closed form at zero gives
\[
\chi'_\pm(0)=\frac{-1\pm\sqrt5}{2\sqrt5},
\]
so the derivative of the gap is exactly one. As \(\varepsilon=1-\mu\downarrow0\), \(w_\pm\to\pm\sqrt2\), and the explicit rational kernel expression yields
\[
p_\pm(1-\varepsilon)=(2\pm\sqrt2)\varepsilon+O(\varepsilon^2).
\]
The elementary expansion \(\operatorname{arcosh}(1+x)=\sqrt{2x}+O(x^{3/2})\) proves the two square-root laws and the ratio \(\sqrt{(2+\sqrt2)/(2-\sqrt2)}=1+\sqrt2\).

## Verification
The standalone `verify.py` reconstructs the reciprocal quartic identity symbolically, verifies the Jacobian and trace formulas, evaluates the exact radical roots at representative parameter values with high precision, checks the two-cycle equations by direct iteration, and compares both endpoint asymptotics. Its output is supplemental to the universal proof above. Reproduce with `python verify.py` using Python, SymPy, and mpmath. All exact conclusions use the preceding algebra and the compactness/implicit-function argument, not finite enumeration.

## Relationship to prior work
Bandtlow, Just and Slipantschuk (2024) used precisely this analytic toral family to study the regularity of its hyperbolic splitting. Their complete publicly accessible paper provides the nonlinear map, the unique fixed point and its Jacobian trace, the invariant cone fields, and numerical local expansion plots. It does not give the two distinct prime-two orbits' closed-form multipliers or their sharp singular-edge ratio. The family itself is older: Slipantschuk, Bandtlow and Just (2016) introduced its Blaschke realization and determined the spectrum of an analytic transfer operator; that analytic-operator result does not furnish the orbit-resolved formulas proved here. The 2022 rational-Anosov spectral framework studies general weighted transfer operators and complex-domain fixed points, not this specific real prime-two expansion splitting. Standard hyperbolicity and continuation facts are used in the count; none is presented as new.

## Limitations
Only the inversion-symmetric slice (phase parameter fixed to zero) and primitive period-two orbits are classified. No claim is made about higher periods, all invariant measures, or quantitative regularity of the global stable and unstable bundles. The endpoint \(\mu=1\) is not an Anosov map in this family and is not included in the statement. Priority risk remains from possible unindexed orbitwise calculations or derivations using periodic-orbit trace formulas; the exact numerical constants are not proof of priority. All review described here is self-review, and independent mathematical validation has not been conducted.

## References
1. O. F. Bandtlow, W. Just, J. Slipantschuk, *A numerical study of rigidity of hyperbolic splittings in simple two-dimensional maps*, arXiv:2402.14770v1 (first public 2024-02-22), *Nonlinearity* **37** (2024), 045007, https://doi.org/10.1088/1361-6544/ad2b58. Full published text: https://wrap.warwick.ac.uk/id/eprint/183798/7/Bandtlow_2024_Nonlinearity_37_045007.pdf.
2. J. Slipantschuk, O. F. Bandtlow, W. Just, *Complete spectral data for analytic Anosov maps of the torus*, arXiv:1605.02883v1 (2016-05-10), https://arxiv.org/abs/1605.02883.
3. J. Slipantschuk, O. F. Bandtlow, W. Just, *Resonances for rational Anosov maps on the torus*, arXiv:2211.05925v1 (2022-11-10), https://arxiv.org/abs/2211.05925.
