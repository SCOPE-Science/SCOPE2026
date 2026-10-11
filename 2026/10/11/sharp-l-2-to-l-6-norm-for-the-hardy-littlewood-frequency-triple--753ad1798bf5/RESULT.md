# Sharp \(L^2\to L^6\) norm for the Hardy–Littlewood frequency triple
## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) carry normalized Haar measure and put \(P(t)=a+b e^{2\pi i t}+c e^{6\pi i t}\). Define \[R(r)=r^{10}+13r^9+44r^8+42r^7+6r^6-207r^5-148r^4+120r^3+81r^2+36r+32.\] There is a unique root \(r_*\) of \(R\) in \(547/500<r<219/200\). Put \[X_*=\frac{2(1-r_*^2)}{r_*^3+4r_*^2-3r_*-4},\qquad Y_*=\frac{(1-X_*)r_*^2}{1+r_*^2},\qquad Z_*=\frac{1-X_*}{1+r_*^2}.\] Then the sharp constant in \[\|P\|_{L^6(\mathbb T)}\le \mathsf C_{013,6} \bigl(|a|^2+|b|^2+|c|^2\bigr)^{1/2}\] is exactly \(\mathsf C_{013,6}^6=\Phi(X_*,r_*)\), where \[\Phi(X,r)=\frac{6X^3r^3+12X^3r^2-6X^2r^4-12X^2r^3-30X^2r^2-6X^2+6Xr^4+6Xr^3+12Xr^2+6X+r^4+8r^2+1}{(1+r^2)^2}.\] Numerically, \(\mathsf C_{013,6}^6=3.676690884789743\ldots\) and \(\mathsf C_{013,6}=1.242346821125471\ldots\). Every nonzero extremizer, and only those extremizers, is of the form \[(a,b,c)=\lambda\bigl(\sqrt{X_*},\sqrt{Y_*}e^{i\theta},\sqrt{Z_*}e^{3i\theta}\bigr),\qquad \lambda\in\mathbb C\setminus\{0\},\ \theta\in\mathbb R.\]

The squared-modulus profile is genuinely non-uniform:
\[
(X_*,Y_*,Z_*)=(0.334220497181418\ldots,0.362816605726877\ldots,0.302962897091705\ldots).
\]
Thus the unrestricted sharp norm is not attained by the idempotent or any equal-modulus trinomial on this support.

## Assumptions and scope
The domain is the one-dimensional torus \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Haar measure. The three frequencies are exactly \(\{0,1,3\}\); common translation or dilation of the frequencies gives an equivalent problem after modulation or reparameterization only when it preserves the same reduced support. Coefficients are arbitrary complex numbers. The statement concerns the operator norm from coefficient \(\ell^2\) to function \(L^6\), not the maximum-modulus norm and not the phase-only problem with prescribed coefficient moduli.

## Proof
By homogeneity, normalize
\[
|a|^2+|b|^2+|c|^2=1.
\]
Expanding the cube gives Fourier coefficients at frequencies \(0,1,2,3,4,5,6,7,9\). The only collision is at frequency \(3\), where the coefficient is \(b^3+3a^2c\). Parseval therefore gives
\[
\begin{aligned}
\|P\|_6^6={}&|a|^6+9|a|^4|b|^2+9|a|^2|b|^4+|b^3+3a^2c|^2\\
&+36|a|^2|b|^2|c|^2+9|b|^4|c|^2+9|a|^2|c|^4+9|b|^2|c|^4+|c|^6.
\end{aligned}
\]
For fixed moduli \(x=|a|\), \(y=|b|\), \(z=|c|\), the only phase-sensitive term is maximized exactly when
\[
b^3\overline{a^2c}>0.
\]
Under that alignment the objective becomes
\[
\begin{aligned}
F(x,y,z)={}&x^6+y^6+z^6+9x^4y^2+9x^4z^2+9x^2y^4+36x^2y^2z^2\\
&+9x^2z^4+9y^4z^2+9y^2z^4+6x^2y^3z.
\end{aligned}
\]
If one modulus vanishes, the problem reduces to two frequencies and
\[
\|u+v e^{2\pi i kt}\|_6^6=1+6|u|^2|v|^2\le \frac52
\]
after \(|u|^2+|v|^2=1\). On the other hand, the aligned equal-modulus point gives \(11/3\). Hence every global maximizer is interior and has the phase alignment above.

Set \(X=x^2\) and \(r=y/z\). Then
\[
y^2=\frac{(1-X)r^2}{1+r^2},\qquad z^2=\frac{1-X}{1+r^2},
\]
and direct substitution gives exactly the function \(\Phi(X,r)\) stated in the finding. Its derivatives factor as
\[
\frac{\partial\Phi}{\partial r}=
-\frac{6r(X-1)^2}{(1+r^2)^3}
\left[X(r^3+4r^2-3r-4)+2r^2-2\right]
\]
and
\[
\frac{\partial\Phi}{\partial X}=
-\frac{6}{(1+r^2)^2}
\left[-3X^2r^3-6X^2r^2+2Xr^4+4Xr^3+10Xr^2+2X-r^4-r^3-2r^2-1\right].
\]
At an interior critical point the first equation gives
\[
X=\frac{2(1-r^2)}{r^3+4r^2-3r-4}.
\]
Feasibility forces \(r>1\). Writing \(B(r)=r^3+6r^2-3r-6\), the additional condition \(X<1\) is equivalent to \(B(r)<0\). The polynomial \(B\) has one positive root above \(1\), and its signs at \(57/50\) and \(23/20\) place that root below \(23/20\). Thus every interior maximizer has \(1<r<23/20\).

Substitution of the displayed expression for \(X\) into \(\partial\Phi/\partial X=0\), clearing the nonzero denominator, gives exactly \(R(r)=0\). The accompanying exact rational Sturm computation proves that \(R\) has exactly one root on \((1,23/20)\), and isolates it further to
\[
\frac{547}{500}<r_*<\frac{219}{200}.
\]
On this isolating interval the denominator in the formula for \(X\) is negative and \(B(r)<0\), so \(0<X_*<1\). Therefore the global maximizer is the unique interior critical point. The phase equality then reconstructs all extremizers: after a common complex scalar, the phase relation \(3\arg b=2\arg a+\arg c\) is exactly the one-parameter family stated in the finding.

## Verification
`artifacts/verify.py` uses only Python's standard library. It constructs the Sturm chain with exact `Fraction` arithmetic; proves that \(R\) has exactly one root in \((1,23/20)\) and in the smaller rational interval \((547/500,219/200)\); verifies the cleared stationarity identity exactly; checks the feasibility signs; reconstructs \((X_*,Y_*,Z_*)\) and the sharp constant; and replays the full cubic self-convolution formula on 20,000 random complex coefficient triples.

The actual packaged replay terminates with
`VERIFY_OK sturm_feasible_roots=1 r=1.094331386704356 X=0.334220497181418 Y=0.362816605726877 Z=0.302962897091705 K=3.676690884789743 C6=1.242346821125471 random_cases=20000 max_random=3.674059471999777`.
The random replay is corroborative only. The universal maximization follows from the analytic reduction plus the exact Sturm certificate.

## Relationship to prior work
Neuwirth's archive-era trinomial paper studies arbitrary three-frequency spectra with arbitrary coefficient moduli, but in the maximum-modulus norm; its principal results concern maximum points, phase dependence, multiplier norms, and Sidon constants. It does not determine the \(L^2\)-to-\(L^6\) norm considered here. Krenedits studies the classical Hardy--Littlewood support \(\{0,1,3\}\) for signed idempotent trinomials at non-even exponents; the even-exponent equality mechanism is Parseval, but unrestricted amplitude optimization at exponent \(6\) is not computed there.

A previously published exact even-moment formula for arbitrary three-frequency *unimodular* sums covers the phase response on \(\{0,1,3\}\), but explicitly leaves non-unimodular coefficient magnitudes and higher-resonance optimization outside its claim. The present result solves precisely that unrestricted amplitude optimization at the first cubic resonance. A separate sharp \(L^2\)-to-\(L^6\) result for the consecutive support \(\{0,1,2\}\) has a different collision geometry and does not imply the value or extremizers above.

## Limitations
The theorem is for the single reduced frequency triple \(\{0,1,3\}\) and exponent \(6\); it does not classify all three-point supports or other exponents. The algebraic optimizer is specified by an isolating interval for a degree-ten polynomial rather than a radical expression. The Sturm calculation is exact and finite, but the random complex replay is not used as proof. A residual originality risk remains that an older low-degree Nikolskii or trinomial-norm table encodes the same constant under different terminology; targeted exact-value, resonance, amplitude, and support searches did not locate such a source.

## References
1. Stefan Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first submitted 2007-03-08; primary MSC 42A05.
2. Sándor Krenedits, *Three-term idempotent counterexamples in the Hardy-Littlewood majorant problem*, arXiv:1006.0409v1, first submitted 2010-06-02; primary MSC 42A05.
