# Sharp \(L^2\to\ell^4\) extension and character rigidity on the ternary split cone

## Finding

Let \(G=\mathbb F_3^2\) and let the split quadratic zero cone be
\[
S=\{(x,y)\in G:xy=0\}=\{(0,0),(1,0),(-1,0),(0,1),(0,-1)\}.
\]
Equip \(S\) with normalized counting measure, its dual group with counting measure, and set
\[
\mathcal E f(\xi)=\frac15\sum_{s\in S}f(s)\exp(2\pi i\langle\xi,s\rangle/3).
\]
Then the **sharp fourth-power endpoint inequality** is
\[
\boxed{\|\mathcal E f\|_{\ell^4(G)}^4
\le\frac{6561+297\sqrt{33}}{7400}\|f\|_{L^2(S)}^4.}
\]
Write \(t_*=(\sqrt{33}-1)/4\) and \(\omega=\exp(2\pi i/3)\). Apart from the zero function, **all equality cases** are
\[
\boxed{f(0,0)=t_*\lambda,\qquad
f(x,y)=\lambda\omega^{\alpha x+\beta y}\quad ((x,y)\in S\setminus\{(0,0)\}),}
\]
where \(\lambda\in\mathbb C\setminus\{0\}\) and \(\alpha,\beta\in\mathbb F_3\). Thus the intersecting lines are genuinely coupled: the unique optimal central-to-outer amplitude ratio is \(t_*>1\), and only restrictions of additive characters give optimal phases.

For the unnormalized additive convolution on \(G\), equivalently
\[
\boxed{\sum_{z\in G}|(f*f)(z)|^2
\le K\left(\sum_{s\in S}|f(s)|^2\right)^2,\qquad
K=\frac{729+33\sqrt{33}}{296}.}
\]
The nonconstant extremizer improves strictly on the optimal ratio \(3\) from functions supported on a single affine line and on the flat five-point value \(77/25\).

## Assumptions and scope

All functions \(f:S\to\mathbb C\) are allowed; they need not be real or nonzero at each point. Convolution treats \(f\) as zero off \(S\): \((f*f)(z)=\sum_{x\in G}f(x)f(z-x)\). The source norm obeys \(\|f\|_{L^2(S)}^2=\frac15\sum_{s\in S}|f(s)|^2\). Every numerical constant follows from these declared normalizations. The classification concerns this **single natural first odd-field split cone**, not arbitrary fields or varieties, and no family-wide extension result is asserted.

## Proof

**Fourier reduction.** Put \(M=\sum_{s\in S}|f(s)|^2\) and \(Q=\sum_{z\in G}|(f*f)(z)|^2\). Orthogonality of the nine characters of \(G\) gives
\[
\sum_{\xi\in G}|\mathcal Ef(\xi)|^4=\frac9{625}Q,
\qquad \|f\|_{L^2(S)}^4=\frac{M^2}{25}.
\]
The triangle inequality in each convolution fiber implies \(Q(f)\le Q(|f|)\); hence optimize first over nonnegative amplitudes.

**All nine pair-sum fibers.** In the order \((0,0),(1,0),(-1,0),(0,1),(0,-1)\), write the amplitudes as \(c,a,d,b,e\ge0\). Direct enumeration gives the exact polynomial
\[
\begin{aligned}
Q={}&(c^2+2ad+2be)^2+(2ca+d^2)^2+(2cd+a^2)^2\\
&+(2cb+e^2)^2+(2ce+b^2)^2
+4(a^2+d^2)(b^2+e^2),\\
M={}&c^2+a^2+d^2+b^2+e^2.
\end{aligned}
\]
This enumeration is not an approximation; the four off-axis convolution values are \(2ab,2ae,2db,2de\).

**Antipodal balancing.** Fix \(c,b,e\) and \(X=a^2+d^2\). Writing \(P=ad\), the entire dependence on the horizontal amplitudes beyond terms fixed by \(X\) is
\[
2P^2+4P\bigl(c^2+2be+c(a+d)\bigr).
\]
Under \(a,d\ge0\), both \(P\) and \(a+d\) are largest at \(a=d=\sqrt{X/2}\), and the displayed expression strictly increases when \(P\) is increased from below its maximum if \(X>0\). The same argument applies to \(b,e\). Thus an optimal nonnegative vector must have \(a=d=A\) and \(b=e=B\); any maximizer with both pairs nonempty must be balanced. For these vectors,
\[
\begin{aligned}
Q&=c^4+12c^2(A^2+B^2)+6(A^2+B^2)^2+12A^2B^2+8c(A^3+B^3),\\
M&=c^2+2(A^2+B^2).
\end{aligned}
\]

**Endpoint dichotomy.** If \(A=B=0\) the ratio \(Q/M^2\) equals \(1\). Otherwise set \(R=\sqrt{A^2+B^2}>0\), \(\tau=c/R\), and \(u=AB/R^2\in[0,1/2]\). Since \(A^3+B^3=R^3(1-u)\sqrt{1+2u}\),
\[
\frac Q{R^4}=\tau^4+12\tau^2+6+12u^2+8\tau(1-u)\sqrt{1+2u},\qquad
\frac M{R^2}=\tau^2+2.
\]
For fixed \(\tau\), differentiation of the only \(u\)-dependent terms gives
\[
24u\left(1-\frac{\tau}{\sqrt{1+2u}}\right).
\]
The parenthetical factor is increasing with \(u\), so any interior critical point is a minimum, not a maximum. Thus every maximum is at \(u=0\) or \(u=1/2\).

At \(u=0\) just one full coordinate line is occupied. The ordinary three-point Fourier transform of that line, together with \(\sum |\widehat g|^4\le(\sum |\widehat g|^2)^2\), gives \(Q\le3M^2\). This is sharp on a single line but not globally.

At \(u=1/2\), \(A=B>0\). Put \(z=c/A\). Then
\[
F(z)=\frac Q{M^2}=\frac{z^4+24z^2+16z+36}{(z^2+4)^2},\qquad
F'(z)=-\frac{16(z+1)(2z^2+z-4)}{(z^2+4)^3}.
\]
For \(z\ge0\), the derivative changes sign only at \(t_*=(\sqrt{33}-1)/4\), from positive to negative. Exact substitution yields
\[
F(t_*)=\frac{729+33\sqrt{33}}{296}>3.
\]
Therefore the global maximum occurs only with the stated positive amplitudes. Multiplying by the normalization factor \(9/25\) proves the sharp extension inequality.

**Complete equality phases.** Since all five optimal amplitudes are strictly positive, equality in \(Q(f)\le Q(|f|)\) requires aligned phases for every pair of summands in each convolution fiber. Write \(f(s)=|f(s)|e^{i\theta_s}\). At the two nonzero horizontal axis sums,
\[
\theta_0+\theta_{+x}\equiv2\theta_{-x},\qquad
\theta_0+\theta_{-x}\equiv2\theta_{+x}\pmod{2\pi}.
\]
Hence \(3(\theta_{+x}-\theta_0)\equiv0\) and \(\theta_{-x}-\theta_0\equiv-(\theta_{+x}-\theta_0)\). The vertical pair satisfies the analogous equations. Thus phases restrict to a scalar multiple of exactly one additive character \(\omega^{\alpha x+\beta y}\); conversely such a character makes every fiber coherent and attains equality. This proves necessity and sufficiency, including the zero function separately.

## Verification

The accompanying `artifacts/check.py` reconstructs all nine convolution fibers, verifies the antipodal-balancing polynomial and both reduced one-variable derivatives symbolically, and proves equality of the radical expression and closed-form sharp constant by exact simplification. It additionally tests 350 deterministic complex coefficient vectors against direct nine-frequency Fourier sums and the inequality, tests all nine optimal character modulations, and computes the flat-input energy \(77\). Its executed result is `VERIFY_OK symbolic_identities=7 random_complex_cases=350 Fourier_values=3150 equality_modulations=9 constant_energy=77`. Exact identities and analytic inequalities in the proof, not random testing, establish the theorem for all complex inputs.

## Relationship to prior work

Iosevich–Koh and Koh–Shen developed finite-field Fourier extension estimates for quadratic and algebraic curves. The latter's Theorem 1.1 concerns the uniform-in-field-cardinality \(L^2\to L^4\) extension property and explicitly excludes plane polynomials with linear factors: the split cone here is precisely a reducible boundary case, at the first odd field size. Neither paper's relevant theorem supplies this fixed-field optimal constant or equality family.

González-Riquelme–Oliveira e Silva treat sharp inequalities for paraboloids and four-dimensional cones; González-Riquelme–Ismoilov treat four-dimensional cones. Their explicit surface classes do not include this two-dimensional union of coordinate lines. Existing published work on all attainable Fourier-support sizes for five-point subsets of \(\mathbb F_3^2\) includes this very support but concerns zeros and cardinalities rather than the fourth-moment optimum. Published small-field phase results for anisotropic three-dimensional spheres concern different sets and do not imply the present nonconstant center-to-outer ratio. The sharp norm and rigidity statement is the claim assessed here, not a general extension framework or an uncertainty-support theorem.

## Limitations

Only the precise five-point split cone over \(\mathbb F_3\) is addressed. The result does not assert analogous constants or maximizing structures for \(\mathbb F_q\) with larger \(q\), nor a uniform extension estimate over increasing fields. The exact formula is a finite-dimensional analytic theorem, not a statement about continuous cones. Literature searches and full-text comparison of relevant theorem sections cannot establish global priority; older equivalent optimizations of finite union-of-subgroups convolution energy may exist. No independent mathematical audit has been performed.

## References

1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (first public 28 April 2008).
2. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240v1 (first public 22 March 2010), Theorem 1.1 and §2.
3. A. Iosevich, D. Koh, H. Lee, T. Pham and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387v1 (first public 29 June 2018).
4. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first public 26 May 2024).
5. C. González-Riquelme and T. Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields*, arXiv:2509.05600v1 (first public 6 September 2025).
6. *Complete exact-support five-point Fourier spectrum on \(\mathbb F_3^2\)*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-exact-support-five-point-fourier-spectrum-on-f3-2--ae1a86146a92.
7. *Small-field phase dichotomy for anisotropic sphere extremizers*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-small-field-phase-dichotomy-for-anisotropic-sphere-extremizers--973050ba74a9.
