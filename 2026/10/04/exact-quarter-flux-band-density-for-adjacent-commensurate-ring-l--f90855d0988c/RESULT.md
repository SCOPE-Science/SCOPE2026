# Exact quarter-flux band density for adjacent commensurate ring lengths
## Finding
Consider the tightly connected magnetic ring chain of Baradaran--Exner--Lipovský, so the connecting edge has length \(\ell_1=0\), the two ring arcs have \(\ell_2+\ell_3=2\pi\), and the preferred-orientation vertex condition is the one used in their model. Fix quarter flux \(A=1/4\). For every integer \(m\ge1\), impose the adjacent commensurate ratio
\[
\frac{\ell_2}{\ell_3}=\frac{m}{m+1},\qquad
\ell_2=\frac{2\pi m}{2m+1},\qquad
\ell_3=\frac{2\pi(m+1)}{2m+1}.
\]
Let \(\Sigma_k=\{k>0:k^2\in\sigma(H)\}\) be the momentum spectrum and define its asymptotic density by
\[
P_m=\lim_{K\to\infty}\frac{|\Sigma_k\cap[0,K]|}{K}.
\]
If \(s_m\) denotes the odd member of the consecutive pair \(\{m,m+1\}\), then
\[
P_m=\frac34-\frac{1}{4(2m+1)s_m},
\qquad
s_m=\begin{cases}m,&m\text{ odd},\\m+1,&m\text{ even}.\end{cases}
\]
Consequently,
\[
\frac34-P_m=\frac{1}{4(2m+1)s_m}=\frac{1}{8m^2}+O(m^{-3}).
\]
Although \(\ell_2/\ell_3=m/(m+1)\to1\), these commensurate densities converge to \(3/4\). At the exactly symmetric ratio \(\ell_2=\ell_3=\pi\), the same source's symmetric-chain formula gives \(P=1/2\) at \(A=1/4\). Thus the high-energy momentum-band density is discontinuous at the symmetric length ratio along this natural sequence of adjacent rational ratios.

## Assumptions and scope
The statement concerns only the positive high-energy momentum spectrum of the tightly connected chain, not the negative spectrum and not finite-energy band locations. The magnetic parameter is fixed at \(A=1/4\), the ring circumference is normalized to \(2\pi\), and \(m\) ranges over all positive integers. The coupling length parameter in the preferred-orientation condition does not enter the limiting density, consistently with the leading high-energy criterion in the source.

The source derives, for the tightly connected chain, the high-energy band condition
\[
\sin\!\bigl((k-A)\pi\bigr)\sin\!\bigl((k+A)\pi\bigr)\sin(k\ell_3)\sin(k\ell_2)\ge0
\]
up to a relative error of order \(O(k^{-2})\). For commensurate \(\ell_2/\ell_3\), the leading sign pattern is periodic in \(k\), and the source explains that the momentum-band density is obtained from the fraction of one period on which this leading function is nonnegative.

## Proof
At \(A=1/4\),
\[
\sin\!\bigl((k-1/4)\pi\bigr)\sin\!\bigl((k+1/4)\pi\bigr)=-\frac12\cos(2\pi k).
\]
For the specified arc lengths, put
\[
x=\frac{2\pi k}{2m+1},\qquad r=2m+1.
\]
Then \(k\ell_2=mx\), \(k\ell_3=(m+1)x\), and \(2\pi k=rx\). Hence the limiting periodic band condition is
\[
-\cos(rx)\sin(mx)\sin((m+1)x)\ge0.
\]
The expression is invariant under \(x\mapsto2\pi-x\), so its density on \([0,2\pi)\) equals its density on \([0,\pi]\). Scale \(x=\pi t\), \(0<t<1\), and ignore the finite zero set. Define
\[
g(t)=\operatorname{sgn}\!\bigl(\sin(m\pi t)\sin((m+1)\pi t)\bigr),\qquad
q(t)=\operatorname{sgn}\!\bigl(-\cos(r\pi t)\bigr).
\]
The desired set is exactly where \(g(t)=q(t)\).

The interior sign-change points of \(g\) are strictly ordered as
\[
z_{2i-1}=\frac{i}{m+1}\quad(1\le i\le m),\qquad
z_{2i}=\frac{i}{m}\quad(1\le i\le m-1),
\]
because
\[
\frac{i}{m+1}<\frac{i}{m}<\frac{i+1}{m+1}.
\]
The sign-change points of \(q\) are
\[
c_j=\frac{j+1/2}{r},\qquad 0\le j\le2m.
\]
Near \(t=0\), \(g\) is positive and \(q\) is negative. After the extra first jump \(c_0\), the two alternating sign patterns agree except on the displacement intervals between the paired jumps \(z_j\) and \(c_j\), and after the extra last jump \(c_{2m}\). Indeed, for every \(1\le j\le2m-1\), one has \(c_{j-1}<z_j<c_{j+1}\), so these displacement intervals do not overlap. Therefore the total mismatch measure is
\[
M_m=\frac1r+\sum_{j=1}^{2m-1}|z_j-c_j|.
\]
For the odd and even indexed jumps,
\[
\left|z_{2i-1}-c_{2i-1}\right|
=\frac{|m+1-2i|}{2(m+1)r},
\]
and
\[
\left|z_{2i}-c_{2i}\right|
=\frac{|2i-m|}{2mr}.
\]
Thus
\[
M_m=\frac1r+
\frac{1}{2(m+1)r}\sum_{i=1}^{m}|m+1-2i|
+
\frac{1}{2mr}\sum_{i=1}^{m-1}|2i-m|.
\]
If \(m=2h\), the two absolute-value sums are \(2h^2\) and \(2h(h-1)\), respectively, giving
\[
M_m=\frac14+\frac{1}{4(2m+1)(m+1)}.
\]
If \(m=2h+1\), the sums are \(2h(h+1)\) and \(2h^2\), giving
\[
M_m=\frac14+\frac{1}{4(2m+1)m}.
\]
Since \(P_m=1-M_m\), both cases combine into
\[
P_m=\frac34-\frac{1}{4(2m+1)s_m}.
\]

It remains to justify using the leading sign condition for the limiting density. In one period the leading trigonometric polynomial has only finitely many zeros. Given any \(\varepsilon>0\), remove \(\varepsilon\)-neighborhoods of those zeros. On the remaining compact set its absolute value has a positive minimum, whereas the source's relative \(O(k^{-2})\) correction tends uniformly to zero along successive high-energy periods. Hence the exact and leading band indicators agree there for all sufficiently large periods. The removed proportion can be made arbitrarily small, so the asymptotic density equals the periodic sign-measure computed above.

At the exactly symmetric ratio \(\ell_2=\ell_3=\pi\), the source gives
\[
P=1-\frac1\pi\arccos(\cos(2\pi A)).
\]
Setting \(A=1/4\) yields \(P=1/2\), while the formula above gives \(P_m\to3/4\). This proves the discontinuity claim.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to construct all sign-change points for \(1\le m\le200\), computes the exact measure of the nonnegative periodic sign product, independently evaluates the jump-displacement formula, and checks both against the closed form. It also performs dense midpoint checks for representative values of \(m\) and verifies the symmetric-chain value \(1/2\) at quarter flux. Running `python verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Baradaran, Exner and Lipovský derive the magnetic tight-chain high-energy condition above. For rational \(\ell_2/\ell_3\) they state that universality fails and describe numerical root counting; they explicitly say they were unable to give a closed form for the commensurate probability in general. For incommensurate arc lengths they obtain
\[
P=\frac12+2A-4A^2\qquad (A\bmod 1/2),
\]
which equals \(3/4\) at \(A=1/4\). They separately derive the symmetric-chain formula yielding \(1/2\) at quarter flux. The present claim supplies an exact all-\(m\) commensurate family, its \(m^{-2}\) approach to \(3/4\), and the resulting discontinuity at the symmetric ratio.

Band and Berkolaiko establish edge-length independence of momentum-band density for generic edge lengths of periodic quantum graphs. That generic universality does not cover this rational commensurate family; the magnetic ring-chain paper itself emphasizes the distinction between rational and incommensurate arc-length ratios.

## Limitations
No formula is claimed here for arbitrary coprime rational ratios \(p/q\), for magnetic flux other than \(A=1/4\), or for finite-energy convergence rates of the exact band indicator to the limiting periodic sign condition. The discontinuity concerns the high-energy momentum-band density as a function of edge-length ratio; it does not assert discontinuity of the spectrum as a closed set.

## References
1. M. Baradaran, P. Exner, J. Lipovský, *Magnetic ring chains with vertex coupling of a preferred orientation*, arXiv:2201.01502v1 (5 January 2022), later J. Phys. A: Math. Theor. 55 (2022) 375203, DOI:10.1088/1751-8121/ac820b. Relevant material: Sec. 3.1, especially equations (34)--(37).
2. R. Band, G. Berkolaiko, *Universality of the momentum band density of periodic networks*, arXiv:1304.6028v1; Phys. Rev. Lett. 111 (2013) 130404, DOI:10.1103/PhysRevLett.111.130404.
3. M. Baradaran, P. Exner, M. Tater, *Ring chains with vertex coupling of a preferred orientation*, arXiv:1912.03667v1; Rev. Math. Phys. 33 (2021) 2060005, DOI:10.1142/S0129055X20600053.
