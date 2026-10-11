# Exact two-site amplitude-resonance law for odd-order cyclic Gabor projectors

## Finding
For **every** odd integer \(N\ge5\), every \(a\in\{1,\ldots,N-1\}\) and every real amplitude \(z\), form the vector \(g\in\mathbb C^N\) that equals \(z\) at positions \(0,a\), and \(1\) elsewhere. Let \(R_N(a,z)\) denote the dimension over \(\mathbb C\) of the linear span of the \(N^2\) rank-one projectors in the full cyclic Gabor orbit. Put \(d=\gcd(N,a)\) and \(m=N/d\). Then \(R_N(a,1)=N\). For \(z\ne1\) the **exact rank-deficiency law** is
\[
\begin{aligned}
N^2-R_N(a,z)={}&(N-1)\mathbf1_{\{z=-1\}}
 +(N-3)\mathbf1_{\{z=1-N/4\}}\\
&+2(d-1)\mathbf1_{\{z=-3\}}\\
&+4d\sum_{k=1}^{(m-1)/2}\mathbf1_{\{z=-1-2\cos(2\pi k/m)\}}.
\end{aligned}
\]
Here each indicator is \(1\) exactly when its stated equality holds and \(0\) otherwise. All listed amplitudes are distinct, except that the \(z=-3\) term gives no loss when \(d=1\). Thus the formula determines **every** exceptional amplitude and every rank loss, with no generic-position assumption.

For example, at \(N=9\) the amplitude \(z=0\) gives rank \(77\) for separation \(a=1\), but rank \(69\) for \(a=3\). At \(N=5,a=1\), the strictly positive amplitude \(z=(\sqrt5-1)/2\) yields rank \(21\), whereas almost all real amplitudes give the full rank \(25\). This illustrates isolated calibration resonances even without a missing coordinate.

## Assumptions and scope
The cyclic group is \(\mathbb Z_N\), with odd \(N\ge5\), and \(\omega=e^{2\pi i/N}\). Let \(T_tg(j)=g(j-t)\) and \(M_bg(j)=\omega^{bj}g(j)\). The projectors are
\[
P_{t,b}=\frac{(M_bT_tg)(M_bT_tg)^*}{N-2+2z^2},\qquad t,b\in\mathbb Z_N.
\]
The denominator is positive. The span is taken over the complex matrix space \(M_N(\mathbb C)\). The statement is specifically for two **equal real** defect amplitudes at distinct positions; complex amplitudes and even orders are not classified here.

## Proof
Define the unnormalized ambiguity coefficients
\[
A(t,b)=\sum_{j\in\mathbb Z_N}g(j+t)\overline{g(j)}\,\omega^{-bj}.
\]
The exact finite Gabor projector-Gram diagonalization (Goldberger–Kang–Okoudjou, Theorem 1) gives
\[
R_N(a,z)=\#\{(t,b)\in\mathbb Z_N^2:A(t,b)\ne0\}.
\]
Normalization only rescales all ambiguity coefficients by a positive scalar. We now compute every zero explicitly, making no numerical approximation.

**Zero translation.** At \(t=0\),
\[
A(0,b)=N\mathbf1_{\{b=0\}}+(z^2-1)(1+\omega^{-ab}).
\]
For \(b=0\), this equals \(N-2+2z^2>0\). For \(b\ne0\), oddness of \(N\) makes \(1+\omega^{-ab}\ne0\), so there are exactly \(N-1\) zeros if and only if \(z=\pm1\).

**Translation \(t=\pm a\).** The two defect sets overlap at one coordinate. Direct expansion, for \(t=a\), gives
\[
A(a,b)=N\mathbf1_{\{b=0\}}+(z-1)\bigl(z+1+\omega^{ab}+\omega^{-ab}\bigr).
\]
At \(t=-a\) the non-background term is multiplied by the harmless phase \(\omega^{-ab}\); hence both translations have the same zero criterion. At \(b=0\), the coefficient is \((z+1)^2+N-4>0\). For \(b\ne0\) and \(z\ne1\), the coefficient vanishes exactly at
\[
z=-1-2\cos(2\pi ab/N).
\]
For residue \(ab\equiv0\pmod N\), this means \(z=-3\); there are \(d-1\) nonzero solutions \(b\), and two translations, accounting for \(2(d-1)\) zeros. For each \(k=1,\ldots,(m-1)/2\), the values of the cosine for \(ab\equiv\pm dk\pmod N\) are distinct. There are exactly \(2d\) solutions \(b\) across the two signs, so the two translations contribute \(4d\) zeros at the associated amplitude.

**All other nonzero translations.** If \(t\notin\{0,a,-a\}\), the four affected coordinates are distinct and
\[
A(t,b)=N\mathbf1_{\{b=0\}}+(z-1)(1+\omega^{-ab})(1+\omega^{tb}).
\]
For \(b\ne0\), neither cyclotomic factor can vanish when \(N\) is odd. Hence such entries are zero precisely for \(z=1\). For \(b=0\), the expression is \(N+4(z-1)\), vanishing exactly at \(z=1-N/4\). There are \(N-3\) eligible translations.

If \(z=1\), the window is constant and its ambiguity is nonzero exactly at the \(N\) coefficients with \(b=0\); thus \(R_N(a,1)=N\). Otherwise the four counted families exhaust all possible zeros. There is no overlap between the exceptional amplitudes: \(m\) is odd, so \(2\cos(2\pi k/m)\) cannot equal \(0\), \(\pm2\) for \(1\le k\le(m-1)/2\), and the cosine values for these \(k\) are distinct. If \(1-N/4=-1-2\cos(2\pi k/m)\), then the rational number \(2\cos(2\pi k/m)=N/4-2\) would be an algebraic integer, hence an integer; this is impossible since \(N\) is odd. The remaining comparisons reduce to the excluded even orders \(N=8,16\), or the same odd-order cosine obstruction. The displayed rank formula follows.

## Verification
The accompanying `check_two_amplitude.py` evaluates all \(N^2\) ambiguity entries directly from their defining finite sums and compares their zero counts with the closed formula for every odd \(N\in\{5,7,\ldots,25\}\), every spacing, and generic, boundary and cosine-resonant amplitudes: **2,392 cases passed**. A separate direct coordinate-elimination computation builds the rank-one projector family itself for selected \(N=5,7,9\): **42 cases passed**. These floating-point finite checks are reproducibility checks, not substitutes for the exact all-dimensional proof above. The equalities in the proof use root-of-unity identities and exact arithmetic of congruence classes.

## Relationship to prior work
Goldberger, Kang and Okoudjou establish the general projector-Gram rank/ambiguity-count identity and study incomplete cyclic Gabor measurements. Their Theorem 1 is explicitly used above; it does **not** compute the real two-defect rank-stratification formula. Previously documented exact laws for a **single** amplitude defect, or two completely erased coordinates (the special case \(z=0\)), determine different or strictly narrower parameter families. The present claim is the complete real-parameter law for **two equal defects at every nonzero spacing in all odd orders**, including the nonunit-gap multiplicities and additional nonzero-amplitude resonance strata. Recent work on stable finite Weyl–Heisenberg measurements provides broad context but not the same stated classification.

## Limitations
No statement is made about complex defect amplitudes, even-order groups, stability constants, or optimal experimental noise resistance. Full rank guarantees injectivity for the associated lifted measurement, not uniform numerical conditioning. An unindexed equivalent two-site calculation remains an originality risk. The finite checks involve floating-point zero thresholds; the unrestricted assertion rests entirely on the algebraic proof.

## References
Goldberger, A.; Kang, S.; Okoudjou, K. A., *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1, first public 2021-06-02, especially Theorems 1 and 2, https://arxiv.org/html/2106.01509v1 .

Zhu, X.; Wang, Y., *Uniformly Stable Minimal Weyl--Heisenberg Measurements Approaching the SIC Benchmark*, arXiv:2608.11850, 2026; motivating stability context, not used in the proof.
