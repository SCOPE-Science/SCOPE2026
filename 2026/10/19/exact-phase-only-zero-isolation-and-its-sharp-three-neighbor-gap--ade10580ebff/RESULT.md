# Exact phase-only zero isolation and its sharp three-neighbor gap on finite parabolas

## Finding
Let \(p\ge5\) be prime, \(\omega=e^{2\pi i/p}\), and let \(x_1,x_2,x_3\) be distinct elements of \(\mathbb F_p\). For three nonzero complex numbers of *the same modulus* \(\rho>0\), define the unnormalized parabolic Fourier sum
\[
F(a,b)=\sum_{j=1}^{3}c_j\omega^{a x_j^2+b x_j},\qquad(a,b)\in\mathbb F_p^2,\quad |c_1|=|c_2|=|c_3|=\rho.
\]
Put \(\varepsilon_p=2\pi/(3p)\) and
\[
\delta_p=\sqrt3\sin\varepsilon_p+\begin{cases}
\cos\varepsilon_p-1,&p\equiv1\pmod3,\\
1-\cos\varepsilon_p,&p\equiv2\pmod3.
\end{cases}
\]
Then: (i) \(F\) has **at most one zero** on \(\mathbb F_p^2\), and this is sharp; (ii) for each fixed ordered support triple, exactly \(2p^2\) coefficient classes modulo a common nonzero complex scalar have a zero; (iii) whenever \(F(v_0)=0\), one has the **exact sharp positive separation**
\[
\min_{v\in\mathbb F_p^2\setminus\{v_0\}}|F(v)|=\rho\delta_p,
\]
and the minimum is attained at exactly **three** distinct other frequencies. In particular \(\lim_{p\to\infty,\ p\text{ prime}}p\delta_p=2\pi/\sqrt3\).

For explicit neighboring frequencies, order the three support points, choose the cancellation orientation such that the normalized terms at \(v_0\) are \((1,\zeta,\zeta^2)\), where \(\zeta=e^{2\pi i/3}\). Write \(v=v_0+(a,b)\) and
\[
r=a(x_2^2-x_1^2)+b(x_2-x_1),\qquad s=a(x_3^2-x_1^2)+b(x_3-x_1)\pmod p.
\]
For \(p=3q+1\), equality occurs precisely at \((r,s)=(q,2q),(q,2q+1),(q+1,2q+1)\). For \(p=3q+2\), it occurs precisely at \((q,2q+1),(q+1,2q+1),(q+1,2q+2)\). For the conjugate cancellation orientation, negate both displayed coordinates.

## Assumptions and scope
All modular arithmetic in \((a,b),(r,s)\) and the points \(x_j\) is over the prime field \(\mathbb F_p\). The Fourier normalization here is the **raw sum**, without factors of \(p^{-1}\) or \(p^{-1/2}\). The coefficient phases are unrestricted on the unit circle, but their magnitudes must coincide and be nonzero. A coefficient class means a one-dimensional complex ray \([c_1:c_2:c_3]\); the equal-modulus property is invariant under that equivalence. The theorem does not assert a uniform lower bound for sums without any zero or for unequal coefficient magnitudes.

## Proof
**1. Reduction to a full two-dimensional root grid.** The three parabola points \(P_j=(x_j^2,x_j)\) are affinely independent in \(\mathbb F_p^2\), because the determinant of the two difference vectors equals, up to sign, \((x_2-x_1)(x_3-x_1)(x_3-x_2)\ne0\). Therefore \((a,b)\mapsto(r,s)\), defined in the finding, is a bijection of \(\mathbb F_p^2\). If \(F(v_0)=0\), three equally long complex vectors sum to zero. They consequently form an equilateral triple, so after a common phase normalization their ordered phases are exactly \((1,\zeta,\zeta^2)\) or \((1,\zeta^2,\zeta)\). In the first case every relative frequency value is, up to a common unimodular factor,
\[
G_p(r,s)=1+\zeta\omega^r+\zeta^2\omega^s.
\]
The other orientation has the same absolute-value distribution via \((r,s)\mapsto(-r,-s)\).

**2. Uniqueness and projective counting.** If \(G_p(r,s)=0\), the three unit vectors must again be a permutation of an equilateral triple. The orientation \((1,\zeta,\zeta^2)\) forces \(\omega^r=\omega^s=1\) and hence \((r,s)=(0,0)\). The reversed orientation would force a nontrivial cube root to be a \(p\)-th root of unity. This is impossible for prime \(p\ge5\). This proves uniqueness. Conversely, for each \(v_0=(a_0,b_0)\in\mathbb F_p^2\) and \(\sigma\in\{-1,1\}\), the coefficients
\[
c_j=\rho\zeta^{\sigma(j-1)}\omega^{-a_0x_j^2-b_0x_j},\qquad j=1,2,3,
\]
produce a zero at \(v_0\). The two orientations are projectively distinct, and uniqueness prevents different \(v_0\) from defining the same class. Since every possible cancellation is equilateral, these \(2p^2\) classes exhaust the possibilities.

**3. Exact root-grid separation lemma.** For any prime \(p\ge5\), the smallest value of \(|G_p(r,s)|\) over \((r,s)\ne(0,0)\) is \(\delta_p\), attained at the three pairs stated above. Here are elementary details for the global minimization. Set \(\alpha=\pi/p\), \(\varepsilon=2\alpha/3\), \(q=\lfloor p/3\rfloor\), and \(D_\pm(t)=\sqrt3\sin t\pm(1-\cos t)\). Fix \(r\) and put
\[
R_r=|1+\zeta\omega^r|=2\left|\cos\left(\frac\pi3+\frac{\pi r}{p}\right)\right|.
\]
The best \(s\) chooses the \(p\)-th root whose vector \(\zeta^2\omega^s\) is closest in angle to \(-(1+\zeta\omega^r)\). Consequently its minimum is at least
\[
h(r)=|R_r-1|,
\]
with equality when the closest angle matches exactly. The closest integer \(s\) is a nearest integer to \(r/2\) when \(\cos(\pi/3+\pi r/p)>0\), or to \((p+r)/2\) when that cosine is negative, modulo \(p\). Ties occur exactly when the indicated number is a half-integer.

The continuous function \(t\mapsto|2|\cos(\pi/3+\pi t/p)|-1|\) on \([0,p]\) has no interior local minimum except the three zeros at \(t=0,p/3,p\). Therefore, for integers \(r\notin\{0,q,q+1\}\), it suffices to test the four immediate outside neighbors \(1,p-1,q-1,q+2\) when these belong to the excluded set. The required bounds are, using \(D_\pm\) and \(\varepsilon=2\pi/(3p)\):

* \(h(1)=D_+(\alpha)>\delta_p\) whenever \(r=1\) is an outside neighbor (here \(p\ge7\));
* \(h(p-1)=D_-(\alpha)>\delta_p\);
* if \(p=3q+1\) and \(p\ge13\), then \(h(q-1)=D_+(2\varepsilon)>\delta_p\), while \(h(q+2)=D_-(5\varepsilon/2)>\delta_p\). For \(p=7\), the missing comparison at \(q-1\) is already the \(r=1\) case;
* if \(p=3q+2\) and \(p\ge11\), then \(h(q-1)=D_+(5\varepsilon/2)>\delta_p\), while \(h(q+2)=D_-(2\varepsilon)>\delta_p\). For \(p=5\), \(q-1=0\), not an outside neighbor.

All straightforward comparisons follow from monotonicity of \(D_+\) and of \(D_-\) on \((0,\pi/3)\), except two inequalities when \(p\equiv2\pmod3\): \(D_-(\alpha)>D_+(2\alpha/3)\) and \(D_-(2\varepsilon)>D_+(\varepsilon)\). For the first put \(t=\alpha/6\le\pi/30\); the desired difference is twice
\[
\sqrt3\cos(5t)\sin t-\sin^2(3t)-\sin^2(2t)>0.
\]
Indeed \(\sqrt3\cos(5t)\ge3/2>13\sin t\) and \(\sin(jt)\le j\sin t\) for \(j=2,3\). For the second put \(u=\varepsilon/2\le\pi/15\); the difference is twice
\[
\sqrt3\cos(3u)\sin u-\sin^2(2u)-\sin^2u>0,
\]
because \(\sqrt3\cos(3u)\ge\sqrt3\cos(\pi/5)>5\sin(\pi/15)\ge5\sin u\) and \(\sin(2u)\le2\sin u\). The numerical constants in these displayed strict comparisons follow, for example, from \(\pi<22/7\), \(\cos(\pi/5)>4/5\), and \(\sin t\le t\).

For \(r=0\), the value \(s=0\) gives the unique zero, and every other \(s\) gives \(|G_p(0,s)|=|\omega^s-1|\ge2\sin\alpha>\delta_p\); the last inequality follows from \(\sin\alpha\ge\alpha-\alpha^3/6\) and \(\delta_p\le\sqrt3\varepsilon+\varepsilon^2/2\), with \(0<\alpha\le\pi/5\).

Only \(r=q,q+1\) remain. For \(p=3q+1\), the nearest-angle rule gives \(s=2q,2q+1\) at \(r=q\), and \(s=2q+1\) at \(r=q+1\). For \(p=3q+2\), it gives \(s=2q+1\) at \(r=q\), and \(s=2q+1,2q+2\) at \(r=q+1\). Direct trigonometric substitution shows that all three values have modulus \(D_-(\varepsilon)\) in the first congruence class, or \(D_+(\varepsilon)\) in the second. No other \((r,s)\) is tied. This proves the lemma.

**4. Transfer back to \(F\).** By the affine independence in step 1, every pair \((r,s)\) corresponds to exactly one frequency difference \(v-v_0\). The root-grid lemma therefore gives the claimed exact minimum and the exact threefold multiplicity. Taylor expansion of the trigonometric expression yields \(\delta_p=2\pi/(\sqrt3 p)+O(p^{-2})\).

## Verification
Run `python verify.py` (Python 3 standard library). It exhaustively evaluates the root-grid minimum and all equality coordinates for every prime \(5\le p\le251\), and independently reconstructs parabolic Fourier sums for many coefficient triples and both orientations. The script tests exactly one zero, sharp separation, and threefold next-minimum multiplicity. It reports `VERIFY_OK 1384774 numeric comparisons; all primes 5..251 and sampled parabolic triples`. These finite floating-point checks are a supplement to the analytic universal proof, not its logical basis.

## Relationship to prior work
Li's 2026 finite-parabola theorem treats arbitrary complex coefficients, allowing as many as **two** zeros for three-point support. The equal-modulus restriction here yields at most one and, more importantly, a sharp *nonzero-amplitude gap*, a three-neighbor equality classification, and an exact count of zero-bearing projective phase configurations. General three-sparse finite-vector-space uncertainty results provide coarse support-cardinality spectra for arbitrary complex coefficients; they do not imply this exact phase-only gap. A published three-point *cyclic* phase-only zero theorem studies a one-dimensional character grid, not simultaneous quadratic and linear parabolic frequency variables. The grid-gap problem here is a different quantitative invariant. The established elementary geometry of zero sums of three unit complex numbers is used without a novelty claim.

## Limitations
This result concerns exactly three support points on a prime-field parabola with equal nonzero coefficient magnitudes; it does not cover composite moduli, larger supports, general coefficient amplitudes, or generic stability under perturbing the coefficients away from the equal-modulus zero-bearing family. For normalized Fourier transforms the gap must be rescaled by the chosen normalization. Only scientific novelty with respect to the accessible literature has been assessed; unindexed equivalent root-grid extremal formulas remain a historical-priority possibility. No independent audit or formal proof certification is claimed.

## References
1. Dongwei Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030, first submitted 2026-09-11, https://arxiv.org/abs/2609.16030 .
2. *Fourier-zero rigidity for unimodular three-point signals on cyclic groups*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fourier-zero-rigidity-for-unimodular-three-point-signals-on-cycl--a8ba65401394 .
3. *Exact three-sparse Fourier support spectra on elementary Abelian odd-prime groups*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-sparse-fourier-support-spectra-on-elementary-abelian--ca0d22e76a34 .
