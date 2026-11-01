# Uniform quantitative frames on the odd-denominator two-channel tent-spline lattice

## Finding
For the centered hat function \(g(t)=(1-|t|)_+\), fix an odd integer \(q\ge3\) and set \(a=4/(5q)\), \(b=5/2\). The system
\[
\mathcal G_q=\{e^{2\pi i mbt}g(t-na):m,n\in\mathbb Z\}
\]
is a frame for \(L^2(\mathbb R)\). More precisely, for all \(f\in L^2(\mathbb R)\),
\[
 A_q\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i mb\,\cdot}g(\cdot-na)\rangle|^2\le B_q\|f\|_2^2,
\]
where the *valid, not necessarily optimal*, constants are
\[
 B_q=\frac{338q}{125},\qquad
 A_q=\begin{cases}\frac2{63375},&q=3,\\[2mm]
\frac{128(173-26\sqrt{13})}{570375q^3},&q\ge5\text{ odd}.
\end{cases}
\]
Thus the complete arithmetic family of odd-denominator, numerator-two lattices at the noninteger modulation \(b=5/2\) has explicit global fiber conditioning.

## Assumptions and scope
The Fourier convention is \(M_b f(t)=e^{2\pi i bt}f(t)\); the integer indices range over all \(\mathbb Z\). The window is *unscaled*, supported in \([-1,1]\). Let \(\lambda=1/b=2/5\), \(z=e^{2\pi i\gamma}\), and define the finite Laurent polynomial
\[
 F_s(z)=\sum_{r\in\mathbb Z}(1-\tfrac25|s-r|)_+z^r.
\]
Only \(|s-r|<5/2\) contribute. The normalized Zibulski–Zeevi matrix for \(ab=2/q\) is
\[
 \Phi_{j,\ell}(x,\gamma)=\frac1{\sqrt5}F_{x-2\ell/q}((-1)^jz),\qquad j=0,1,\ 0\le\ell<q.
\]
Here \(x,\gamma\) are real modulo one. The rational-fiber theorem states that the eigenvalue bounds for \(\Phi\Phi^*\) are equivalent to the Gabor frame bounds in the stated Fourier normalization.

## Proof
**1. Reduce the fiber domain.** The Zak quasiperiodicity follows directly by reindexing:
\(F_{s+r}(z)=z^rF_s(z)\) for every integer \(r\). If \(q\) is odd, \(2\) is invertible modulo \(q\). Replacing \(x\) by \(x+1/q\) permutes columns via the congruence \(2\ell'\equiv2\ell-1\pmod q\). For each column the necessary integer shift is odd, so its row-dependent multiplier is a common \(\operatorname{diag}(1,-1)\), and its remaining multiplier is a unit-modulus column phase. Hence the eigenvalues of \(\Phi\Phi^*\) are \(1/q\)-periodic in \(x\). It suffices to prove all bounds for \(0\le x\le1/q\), any \(|z|=1\).

**2. Bound the norm uniformly.** The nonnegative coefficient sum is \(F_s(1)\le13/5\). Indeed it is integer-periodic and reflection-symmetric; on \(0\le s\le1/2\) the direct five-term sum equals \(13/5-2s/5\). Thus each normalized fiber entry has absolute value at most \(13/(5\sqrt5)\). It follows that
\[
\operatorname{tr}(\Phi\Phi^*)\le 2q\frac{169}{125}=\frac{338q}{125}=B_q.
\]

**3. A universal polynomial certificate for odd \(q\ge7\).** Write \(\delta=2/q\). For \(0\le x\le\delta/2\), both \(x\) and \(x+\delta\) belong to \([0,1/2]\), because \(3\delta/2\le3/7\). On this interval,
\[
 F_t(z)=\tfrac15[(1-2t)z^{-2}+(3-2t)z^{-1}+(5-2t)+(3+2t)z+(1+2t)z^2].
\]
Also \(F_{x-2+\delta}(z)=z^{-2}F_{x+\delta}(z)\). A direct expansion shows that the unnormalized two-column determinant (columns \(0,q-1\)) is
\[
 F_x(z)F_{x-2+\delta}(-z)-F_{x-2+\delta}(z)F_x(-z)
 =\frac{16}{25qz^5}(z^6-2z^4-z^2-1).
\]
The determinant of the *normalized* fiber submatrix is one fifth of this expression.

**4. The exceptional denominator \(q=5\).** The same formula holds on \(0\le x\le1/10\), with columns \((0,4)\). On \(1/10\le x\le1/5\), instead use columns \((3,4)\). Direct evaluation of the same five-term finite sums gives the normalized determinants, respectively,
\[
 \frac{16(z^6-2z^4-z^2-1)}{625z^5},\qquad
 \frac{16(z^6+z^4+2z^2-1)}{625z^5}.
\]
These agree continuously on their shared boundary, but that agreement is not required: either minor supplies a lower estimate on its interval.

**5. Unit-circle lower certificate.** Put \(y=z^2\) and let \(P_-(y)=y^3-2y^2-y-1\), \(P_+(y)=y^3+y^2+2y-1\). For \(|y|=1\) and \(v=\Re y\in[-1,1]\), exact multiplication yields
\[
 |P_-(y)|^2=|P_+(y)|^2=-8v^3+4v^2+8v+5.
\]
The cubic has global minimum
\[
 d=\frac{173-26\sqrt{13}}{27}>0
\]
on \([-1,1]\). Therefore, for all odd \(q\ge5\) and every fiber, one of the stated normalized minors has magnitude at least \(16\sqrt d/(125q)\).

**6. The exceptional denominator \(q=3\).** For \(0\le x\le1/3\), the normalized determinant of columns \((0,2)\) is
\[
 -\frac{2}{375z^5}P_x(z^2),
\]
where \(P_x(y)=\sum_{j=0}^4 c_j(x)y^j\) and
\[
\begin{aligned}
 c_0&=12x^2-16x+5, &c_1&=-12x^2-20x+5,\\
 c_2&=-12x^2+4x+17, &c_3&=-12x^2+28x-3,\\
 c_4&=12x^2+8x+1.&&
\end{aligned}
\]
On the entire interval \(0\le x\le1/3\), we have \(c_2\ge17\), \(c_0,c_4\ge0\), \(c_0+c_4\le6\), and \(|c_1|+|c_3|\le8\). The last inequality follows by splitting where the two coefficients change sign; if opposite-signed their absolute-value sum is \(|8-48x|\le8\), and if same-signed it equals \(|-24x^2+8x+2|\le8/3\). Thus \(|P_x(y)|\ge17-6-8=3\) on \(|y|=1\), and the normalized minor is at least \(2/125\) in modulus.

**7. Convert minors to frame bounds.** For a positive semidefinite \(2\times2\) Gram matrix \(G=\Phi\Phi^*\), Cauchy–Binet gives \(\det G=\sum_{i<j}|\det\Phi_{[i,j]}|^2\), while \(\lambda_{\min}(G)\ge\det G/\operatorname{tr}G\). Sections 3–6 and \(\operatorname{tr}G\le338q/125\) yield
\[
 \lambda_{\min}(G)\ge\begin{cases}
 (2/125)^2/(3\cdot338/125)=2/63375,&q=3,\\
 (16\sqrt d/(125q))^2/(338q/125)=128d/(21125q^3),&q\ge5\text{ odd}.
 \end{cases}
\]
The largest eigenvalue is at most the trace. The rational-fiber characterization completes the proof for every \(f\in L^2(\mathbb R)\).

## Verification
A standalone symbolic checker (`CHECK.py`, requiring SymPy as noted in `requirements.txt`) evaluates the relevant piecewise Zak Laurent sums at exact rational test points, verifies both \(q=5\) minors, the \(q=3\) quartic identity in each region, checks several \(q\ge7\) specializations, verifies both unit-circle polynomials and the lower-bound arithmetic. The unbounded range of odd \(q\) and all fiber positions are established by the displayed analytical identities and inequalities, **not** by a finite test suite.

## Relationship to prior work
Stangl and Frederick, arXiv:2609.00481 (first publicly submitted 2026-08-31), Theorems 2–4, solve the numerator-one case \(ab=1/q\) and expressly leave the converse for numerator \(p>1\) open. The present family uses numerator two and exhibits explicit uniform smallest-singular-value bounds. Atindehou–Frederick–Kouagou–Okoudjou, arXiv:1806.05614, Theorem 1, gives frame regions \(\Gamma_3\) and \(\Lambda_m\), none covering the point \(b=5/2\), \(0<a\le4/15\): \(\Gamma_3\) requires \(b\le2/(1+a)<2\); \(\Lambda_3\) requires \(a\ge1/2\); and \(\Lambda_m\), \(m\ge4\), requires \(a\ge(m-3)/(m-2)\ge1/2\). Ghosh–Selvan, arXiv:2304.11322, Theorem 3.2 computes a frame region for \(b<2\); Theorem 3.3 allows *dilation of the window* rather than the fixed window here. Other sufficient regions are possible and unindexed equivalent specializations cannot be excluded. A separate known result on the single rational curve \(ab=2/5\) covers \(21/10<b<5/2\), but does not include this endpoint or the all-odd-denominator conclusion.

## Limitations
The bounds are explicit certificates, not sharp frame bounds. This theorem concerns only \(b=5/2\) and odd \(q\ge3\); it does not establish the full numerator-two frame set, even-denominator analogues, or results uniform in modulation \(b\). Some earlier sufficient frame regions might imply isolated members of the family; the comparison above uses the explicit conclusions of inspected primary works. Independent mathematical validation has not been carried out.

## References
1. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481, first public 2026-08-31, https://arxiv.org/abs/2609.00481.
2. A. G. D. Atindehou, C. Frederick, Y. B. Kouagou and K. A. Okoudjou, *On the frame set of the second-order B-spline*, arXiv:1806.05614, https://arxiv.org/abs/1806.05614.
3. R. Ghosh and A. A. Selvan, *On Gabor frames generated by B-splines, totally positive functions, and Hermite functions*, arXiv:2304.11322, https://arxiv.org/abs/2304.11322.
4. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, Appl. Comput. Harmon. Anal. 4 (1997), 188–221. The matrix-fiber characterization is recalled as Theorem 4 of Reference 1.
