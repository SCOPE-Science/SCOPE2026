# Exact endpoint slopes for the classical three-term Hardy--Littlewood majorant defect

## Finding
On the normalized circle \(\mathbb T=\mathbb R/\mathbb Z\), define
\[
P_\pm(x)=1+e^{2\pi i x}\pm e^{6\pi i x},
\qquad
\Delta(p)=\int_0^1\bigl(|P_-(x)|^p-|P_+(x)|^p\bigr)\,dx.
\]
Let \(a\in(0,1)\) be the unique root of
\[
a^3+a-1=0,
\]
and let \(b\in(0,1)\) be the unique root of
\[
b^3+b^2-1=0.
\]
Then the endpoint derivatives are
\[
\boxed{\Delta'(2)=3\log(a/b)+\frac{8a^2-5a+5b^2-5b+3}{6}}
\]
and
\[
\boxed{\Delta'(4)=15\log(a/b)+\frac{643a^2-576a+304b^2-293b+200}{60}}.
\]
Numerically,
\[
\Delta'(2)=0.0948207920539202998340578633\ldots>0,
\]
\[
\Delta'(4)=-0.5424530170069415436260322871\ldots<0.
\]
Thus the classical majorant defect opens linearly from the lower even endpoint and closes linearly at the upper even endpoint:
\[
\Delta(p)=\Delta'(2)(p-2)+O((p-2)^2)\qquad(p\downarrow2),
\]
\[
\Delta(p)=(-\Delta'(4))(4-p)+O((4-p)^2)\qquad(p\uparrow4).
\]

## Assumptions and scope
The statement concerns only the classical three-frequency pair \(1+e(x)\pm e(3x)\), where \(e(x)=e^{2\pi i x}\), and the derivatives of its continuous normalized \(p\)-moment defect at \(p=2\) and \(p=4\). It does not re-prove the known positivity of \(\Delta(p)\) throughout \(2<p<4\), nor does it assert corresponding closed forms for the general family \(1+e(x)\pm e((k+2)x)\).

Both trinomials are nonzero on the unit circle. Indeed, a unit-circle zero would imply \(|1+z|=1\), hence \(\operatorname{Re}z=-1/2\); substituting either cube root with that real part into \(1+z\pm z^3\) gives a nonzero value. Therefore \(p\mapsto\Delta(p)\) is real analytic near both endpoints and differentiation under the integral is legitimate.

## Proof
Write \(z=e^{2\pi i x}\). For a real polynomial \(P\) with no unit-circle zeros, reflect each zero outside the unit disk across the unit circle. If the resulting zeros inside the disk are \(\rho_1,\rho_2,\rho_3\), then on \(|z|=1\)
\[
\log|P(z)|=M(P)-\sum_{n\ge1}\frac{S_n(P)}{n}\cos(2\pi n x),
\qquad
S_n(P)=\rho_1^n+\rho_2^n+\rho_3^n,
\]
where \(M(P)\) is the logarithm of the product of the moduli of the original outside zeros. The series converges absolutely and uniformly because every reflected zero has modulus strictly less than one.

For \(P_+(z)=1+z+z^3\), the real inside zero is \(-a\); the other two zeros are outside. Their reflections have sum \(a^2\) and product \(a\). Hence \(M(P_+)=-\log a\), and reduction by \(a^3=1-a\) gives
\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\ \hline
S_n(P_+)&a^2-a&-a&a^2+2a-3&2-3a^2&2a^2+a-1&-3a^2-5a+5.
\end{array}
\]
For \(P_-(z)=1+z-z^3\), equivalently \(z^3-z-1=0\), the unique real outside zero is \(1/b\), while the complex conjugate pair lies inside. Thus \(M(P_-)=-\log b\), and reduction by \(b^3=1-b^2\) gives
\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\ \hline
S_n(P_-)&-b^2&b^2-b+1&-2b^2-b+3&-b&-b^2-3b+4&-3b^2-2b+3.
\end{array}
\]

Put \(G_\pm=|P_\pm|^2\). Their Fourier coefficients through degree three are
\[
G_+=3+(z+z^{-1})+(z^2+z^{-2})+(z^3+z^{-3}),
\]
\[
G_-=3+(z+z^{-1})-(z^2+z^{-2})-(z^3+z^{-3}).
\]
For \(G_+^2\), the nonnegative-frequency coefficients are
\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6)=(15,10,9,8,3,2,1),
\]
while for \(G_-^2\) they are
\[
(15,6,-7,-8,-1,2,1).
\]
If \(G^q=\sum c_nz^n\), orthogonality against the logarithmic Fourier series yields
\[
\int_0^1G(x)^q\log|P(x)|\,dx
=c_0M(P)-\sum_{n\ge1}\frac{c_nS_n(P)}{n}.
\]
Also
\[
\frac{d}{dp}\int_0^1|P(x)|^p\,dx
=\int_0^1|P(x)|^p\log|P(x)|\,dx.
\]
For \(p=2\), substituting the coefficients of \(G_\pm\) gives
\[
\sum_{n=1}^3\frac{c_{+,n}S_n(P_+)}n
=\frac{8a^2-5a-6}{6},
\]
\[
\sum_{n=1}^3\frac{c_{-,n}S_n(P_-)}n
=\frac{-5b^2+5b-9}{6},
\]
which gives the displayed formula for \(\Delta'(2)\). For \(p=4\), using \(G_\pm^2\) gives
\[
\sum_{n=1}^6\frac{c_{+,n}S_n(P_+)}n
=\frac{643a^2-576a-364}{60},
\]
\[
\sum_{n=1}^6\frac{c_{-,n}S_n(P_-)}n
=\frac{-304b^2+293b-564}{60},
\]
which gives the displayed formula for \(\Delta'(4)\).

The signs do not rely on floating-point quadrature. The bundled exact-arithmetic checker isolates \(a\) and \(b\) by rational bisection and bounds
\[
\log(b/a)=2\left(u+\frac{u^3}{3}+\frac{u^5}{5}+\cdots\right),
\qquad
u=\frac{b-a}{b+a},
\]
with a positive rational tail bound. This yields rational intervals strictly contained in \((0,\infty)\) for \(\Delta'(2)\) and in \(( -\infty,0)\) for \(\Delta'(4)\).

## Verification
Running `python verify_endpoint_slopes.py` from the package reproduces the exact convolution tables, the reduced power-sum identities, and rational interval certificates for both signs. The stored output is

`VERIFY_OK`

followed by isolating intervals whose displayed decimal images are
\[
0.094820792053920299834057863317307946<\Delta'(2)<0.094820792053920299834057863317307947,
\]
\[
-0.54245301700694154362603228711873620<\Delta'(4)<-0.54245301700694154362603228711873618.
\]
The decimal rendering is for readability; the checker performs the sign proof with exact rational arithmetic.

## Relationship to prior work
Krenedits proves \(\Delta(p)>0\) for \(2<p<4\). In the proof of the lower endpoint step, Lemma 7 establishes \(d'(1)>0\) for \(d(t)=\Delta(2t)/2\), and Remark 8 reports only the numerical value \(d'(1)\approx0.0948\), explicitly stating that the proof does not determine the value. Since \(d'(1)=\Delta'(2)\), the first boxed identity symbolically evaluates exactly the quantity singled out there. The second boxed identity supplies the analogous exact closing slope at \(p=4\).

The current version of Pan--You--Wang--Zhou--Zhang--Chen proves the full three-term majorant conjecture through resonant Fourier modes and records equality at the even exponents, but the inspected current text does not state these two exact endpoint constants. Its version history says that an earlier version contained a section on endpoint exponents; that earlier full text was not retrievable in the present source inspection, so possible overlap there remains an explicit originality risk rather than being treated as absent.

## Limitations
The formulas are specific to the classical \(k=1\) pair. They quantify endpoint transversality but do not give a new proof of the full interior inequality and do not imply analogous algebraic-logarithmic formulas for higher-frequency pairs. The unavailable earlier version of the recent all-\(k\) paper is a residual literature-comparison risk because its removed endpoint section could contain related endpoint information.

## References
1. S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, arXiv:1006.0409v1, first public 2010-06-02; primary MSC \(42A05\).
2. G. Pan, C. You, H. Wang, J. Zhou, W. Zhang, Y. Chen, *Mockenhaupt's Three-Term Hardy--Littlewood Majorant Conjecture*, arXiv:2609.09740v2, 2026.
