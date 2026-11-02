# Exact Poisson-weighted \(L^1\) approximation and least bounded symbols in a quadratic model space

## Finding
For \(0<r<1\), write
\[
P_r(t)=\frac{1-r^2}{1-2r\cos t+r^2},\qquad
F_r(b)=\frac1{2\pi}\int_{-\pi}^{\pi}P_r(t)|1+b e^{it}|\,dt
\quad (b\in\mathbb C).
\]
The **unique** minimizer of this weighted Hardy-boundary one-step approximation problem is
\[
\boxed{b_r=-\frac{2r}{1+r^2}},\qquad
\boxed{M_r=\min_{b\in\mathbb C}F_r(b)=F_r(b_r).}
\]
In particular, this is a closed algebraic formula for the optimizing coefficient, not an implicit minimization condition. The minimum also has a complete-elliptic-integral representation. Put \(c=2r/(1+r^2)\), \(m=-4c/(1-c)^2\), and \(n=-4r/(1-r)^2\). If
\[
K(m)=\int_0^{\pi/2}\frac{du}{\sqrt{1-m\sin^2u}},\qquad
\Pi(n,m)=\int_0^{\pi/2}\frac{du}{(1-n\sin^2u)\sqrt{1-m\sin^2u}},
\]
then
\[
\boxed{M_r=\frac{2(1-r^2)(1-c)}{\pi(1-r)^2}
\left(\frac mn K(m)+\left(1-\frac mn\right)\Pi(n,m)\right).}
\]
Here \(m,n<0\), so all integrals are ordinary, nonsingular real integrals.

For the degree-two Blaschke product \(\theta_r(z)=(r-z^2)/(1-rz^2)\), put \(K_{\theta_r}=H^2\ominus\theta_r H^2\), and define the norm-one rank-one truncated Toeplitz operator \(R_r=-e_1\otimes e_0\) in the orthonormal basis
\[
e_0(z)=\frac{\sqrt{1-r^2}}{1-rz^2},\qquad e_1(z)=ze_0(z).
\]
If \(A_\varphi^{\theta_r}=P_{K_{\theta_r}}M_\varphi|_{K_{\theta_r}}\), then its least possible bounded-symbol norm is **exactly**
\[
\boxed{\beta_r=\min\{\|\varphi\|_{L^\infty}:A_\varphi^{\theta_r}=R_r\}=M_r^{-1}.}
\]
More strongly, the optimal bounded symbol is unique modulo null sets. With \(w_r(x)=P_r(2x)\), \(g_r(x)=e^{ix}-c e^{-ix}\), it is
\[
\boxed{\varphi_r(e^{ix})=-\frac{\overline{g_r(x)}}{M_r|g_r(x)|}.}
\]
Since \(0<c<1\), this expression is continuous on the circle, and \(\|\varphi_r\|_\infty=M_r^{-1}\).

## Assumptions and scope
All statements hold for every fixed real \(r\) with \(0<r<1\). Circle integrals use normalized Lebesgue measure \(dx/(2\pi)\). Hardy spaces are those of the unit disk; inner products are linear in the first argument. The symbol equality means equality of compressions on the full two-dimensional model space. The complete elliptic integrals above use the parameter convention, not the modulus convention.

## Proof
**1. Existence and rigidity of the scalar extremal.** The positive density \(P_r\) is continuous, even, and has unit integral. The map \(b\mapsto F_r(b)\) is coercive since \(F_r(b)\ge |b|-1\), so a minimum exists. It is strictly convex on \(\mathbb C\cong\mathbb R^2\): equality in its convexity inequality for two distinct coefficients would require \(1+b_1e^{it}\) and \(1+b_2e^{it}\) to be collinear in the same real direction for almost every \(t\). Their nonconstant first-harmonic cross-product rules this out unless \(b_1=b_2\). Therefore the minimum is unique. Evenness of the weight gives \(F_r(\bar b)=F_r(b)\), so the unique minimizer must be real.

For \(0<c<1\), differentiation under the integral gives
\[
\frac{d}{dc}F_r(-c)=\frac1{2\pi}\int_{-\pi}^{\pi}
P_r(t)\frac{c-\cos t}{\sqrt{1-2c\cos t+c^2}}\,dt.
\]
Set \(h=(1-r)/(1+r)\), \(v=(1-c)/(1+c)\), and \(u=\tan(t/2)\). Direct calculation yields
\[
\frac{d}{dc}F_r(-c)=\frac h\pi\int_{-\infty}^{\infty}
\frac{u^2-v}{(u^2+h^2)\sqrt{1+u^2}\sqrt{u^2+v^2}}\,du.
\]
At \(c=2r/(1+r^2)\) we have \(v=h^2\). Denote the resulting integrand by
\[
J_h(u)=\frac{u^2-h^2}{(u^2+h^2)\sqrt{1+u^2}\sqrt{u^2+h^4}}.
\]
It satisfies the exact inversion relation
\[
J_h(h^2/u)\frac{h^2}{u^2}=-J_h(u),\qquad u>0.
\]
Splitting the integral at \(u=h\) and substituting \(u\mapsto h^2/u\) in one part shows that its positive-half-line integral vanishes; the integrand is even, so the whole integral is zero. This exhibits a stationary point in \((0,1)\). Since \(F_r\) is strictly convex on the full complex plane, its unique global minimizer is \(b_r=-c\).

**2. Evaluation of the minimum.** Writing \(t=2u\) and using evenness gives
\[
M_r=\frac{2(1-r^2)}\pi\int_0^{\pi/2}
\frac{\sqrt{(1-c)^2+4c\sin^2u}}{(1-r)^2+4r\sin^2u}\,du.
\]
Factor \((1-c)/(1-r)^2\) from the integrand, and use the algebraic identity
\[
\frac{\sqrt{1-m s}}{1-n s}=
\frac{m/n+(1-m/n)/(1-n s)}{\sqrt{1-m s}}
\quad(0\le s\le1).
\]
The announced \(K\)-\(\Pi\) expression follows directly.

**3. Exact correspondence with bounded symbols.** The displayed basis is orthonormal because \(|e_0(e^{ix})|^2=|e_1(e^{ix})|^2=w_r(x)\) and \(w_r\) is \(\pi\)-periodic. For any essentially bounded \(\varphi\), define
\[
m_j(\varphi)=\frac1{2\pi}\int_{-\pi}^{\pi}\varphi(e^{ix})e^{-ijx}w_r(x)\,dx.
\]
The compression matrix in this basis is
\[
\begin{pmatrix}m_0(\varphi)&m_1(\varphi)\\m_{-1}(\varphi)&m_0(\varphi)\end{pmatrix}.
\]
Thus it represents \(R_r=-e_1\otimes e_0\) precisely when \(m_0=m_1=0\) and \(m_{-1}=-1\). For any such \(\varphi\), the test function \(g_r(x)=e^{ix}-c e^{-ix}\) gives
\[
1=\left|\frac1{2\pi}\int\varphi(e^{ix})g_r(x)w_r(x)\,dx\right|
\le \|\varphi\|_\infty \frac1{2\pi}\int w_r(x)|g_r(x)|\,dx
=\|\varphi\|_\infty M_r.
\]
The final equality uses the substitution \(t=2x\) and periodicity.

Now define \(\varphi_r=-\overline{g_r}/(M_r|g_r|)\). Its essential supremum is \(M_r^{-1}\), and its weighted mean is zero by the sign change under \(x\mapsto x+\pi\). The real and imaginary first variations of the smooth function \(b\mapsto F_r(b)\) at its minimizing point give
\[
\frac1{2\pi}\int\frac{\overline{g_r(x)}}{|g_r(x)|}
e^{-ix}w_r(x)\,dx=0.
\]
Hence \(m_1(\varphi_r)=0\). Since \(\int\varphi_r g_r w_r/(2\pi)=-1\), its remaining moment is \(m_{-1}(\varphi_r)=-1\). Therefore \(\varphi_r\) represents \(R_r\) and realizes the lower bound.

Finally, equality in the \(L^\infty\)-\(L^1\) pairing with the everywhere nonzero \(g_r\) forces the phase and magnitude of every optimal \(\varphi\) to agree almost everywhere with \(-\overline{g_r}/(M_r|g_r|)\). This proves uniqueness.

## Verification
The accompanying standalone `CHECK.py` uses high-precision quadrature to compare the direct minimum against its independent elliptic-integral expression, verify stationarity and lower competitors, replay the involution identity, and test all three weighted matrix moments of the claimed optimal symbol for five parameter values. Its successful run prints `CHECK_OK 70`. These finite checks are supplementary; the statements for every \(0<r<1\) follow from the explicit identities and convexity argument above.

## Relationship to prior work
Pan Ma's *Bounded Symbols and One-Component Inner Functions* (arXiv:2610.28417v1, first public 20 October 2026), Section 6, introduces precisely \(\theta_r\) and \(R_r\), gives the three moment constraints, and derives two-sided estimates and the sharp boundary-order asymptotic for \(\beta_r\). It does not identify the minimizing coefficient or determine the exact finite-parameter norm and unique optimal symbol. The present result starts from that moment formulation and solves the weighted complex \(L^1\) optimization rather than restating the published estimates.

Sam Looi's *Bounded symbols and one-component geometry* (arXiv:2610.31382, Section 4.3; earlier public version reported 7 October 2026) establishes a general weighted polynomial duality framework, including the degree-two family as a specialization. Its displayed degree-two estimates and norm comparisons do not optimize the pertinent weighted affine \(L^1\) functional or give the closed coefficient and elliptic formula. The general bounded-symbol theory of Baranov–Chalendar–Fricain–Mashreghi–Timotin (arXiv:0909.0131) and Baranov–Bessonov–Kapustin (arXiv:1009.5123) supplies background but does not itself imply the explicit optimizer. Bellavita and Virtanen (arXiv:2610.26232) address the one-component characterization rather than this exact finite-dimensional extremal.

## Limitations
This theorem concerns exactly the family of degree-two Blaschke products, the indicated rank-one operator, and \(r\in(0,1)\). It does not compute the worst bounded-symbol constant over all operators on the same model space or generalize to higher-degree inner functions. The result has undergone self-review but no independent audit. Although relevant accessible full texts were inspected, an earlier, differently phrased Poisson-weighted \(L^1\) extremal or equivalent symbol formula may remain unindexed; absence from searches is not proof of novelty.

## References
1. Pan Ma, *Bounded Symbols and One-Component Inner Functions*, arXiv:2610.28417v1 (20 October 2026), especially Proposition 6.1 and equations (6.4)–(6.8), https://arxiv.org/abs/2610.28417.
2. Sam Looi, *Bounded symbols and one-component geometry*, arXiv:2610.31382 (2026), especially Sections 2 and 4.3, https://arxiv.org/abs/2610.31382.
3. Carlo Bellavita and Jani A. Virtanen, *A proof of the Baranov--Bessonov--Kapustin conjecture*, arXiv:2610.26232 (2026), https://arxiv.org/abs/2610.26232.
4. A. Baranov, I. Chalendar, E. Fricain, J. Mashreghi and D. Timotin, *Bounded symbols and reproducing kernel thesis for truncated Toeplitz operators*, arXiv:0909.0131 (2009), https://arxiv.org/abs/0909.0131.
5. A. Baranov, R. Bessonov and V. Kapustin, *Symbols of truncated Toeplitz operators*, arXiv:1009.5123 (2010), https://arxiv.org/abs/1009.5123.
