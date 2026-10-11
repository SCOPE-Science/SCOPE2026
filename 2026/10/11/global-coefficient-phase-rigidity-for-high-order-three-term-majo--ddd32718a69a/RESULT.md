# Global coefficient-phase rigidity for high-order three-term majorants

## Finding
For every integer \(k\ge23\), every real \(2k<p<2k+2\), and \(N=k+2\), set
\[
T_{k,p}(\phi)=\frac1{2\pi}\int_0^{2\pi}
\left|1+e^{it}+e^{i\phi}e^{iNt}\right|^p\,dt,
\qquad\phi\in\mathbb R.
\]
The function \(T_{k,p}\) is even and \(2\pi\)-periodic, **strictly increasing on \((0,\pi)\)**, and strictly decreasing on \((\pi,2\pi)\). Hence its unique minimizing unimodular coefficient is \(e^{i\phi}=1\) and its unique maximizing coefficient is \(e^{i\phi}=-1\). In particular, every other phase has a norm strictly between the two sign choices.

The conclusion has a quantitative uniform cosine form. Put \(s=p/2=k+\alpha\), \(0<\alpha<1\), and
\[
A_{k,s}=\frac{2^{2s+1}\Gamma(s+1)^2\sin(\pi\alpha)}{\pi}>0,
\qquad I_{k,s}=\int_0^\infty J_{k+2}(r)J_{k+1}(r)J_1(r)r^{-2s-1}\,dr>0,
\]
\[
\varepsilon_k=\frac45\left(\frac{19}{20}\right)^{k-23},\qquad
\overline T_{k,p}=\frac1{2\pi}\int_0^{2\pi}T_{k,p}(\psi)\,d\psi.
\]
Then, simultaneously for all permitted \(k,p\),
\[
2A_{k,s}I_{k,s}(1-\varepsilon_k)\sin\phi
\le T'_{k,p}(\phi)\le
2A_{k,s}I_{k,s}(1+\varepsilon_k)\sin\phi
\quad(0<\phi<\pi),
\]
\[
\left|T_{k,p}(\phi)-\overline T_{k,p}
 +2A_{k,s}I_{k,s}\cos\phi\right|
 \le2A_{k,s}I_{k,s}\varepsilon_k\qquad(\phi\in\mathbb R).
\]
Thus the leading cosine describes the full coefficient-phase response, not only the values at the two sign choices; its relative uniform error decays geometrically with \(k\).

## Assumptions and scope
The circle has normalized Lebesgue measure, all Fourier coefficients are defined with the convention \(e^{it}\), and Bessel functions \(J_n\) are of the first kind. The degree and exponent conditions are \(k\in\mathbb Z\), \(k\ge23\), \(N=k+2\), and real \(p\in(2k,2k+2)\). The numerical threshold 23 is a **sufficient threshold from explicit estimates**, not a claimed optimal threshold. At either even endpoint \(p=2k\) or \(p=2k+2\), the norm is independent of the coefficient phase, by the collision-free multinomial expansion for powers below \(N\).

## Proof
Write \(H(\theta,\psi)=|1+e^{i\theta}+e^{i\psi}|^2\) and
\[
c_s(m,n)=\frac1{(2\pi)^2}\int_{[0,2\pi]^2}H(\theta,\psi)^s e^{-i(m\theta+n\psi)}\,d\theta\,d\psi.
\]
For \(s\ge23\), this function has sufficiently many square-integrable derivatives for its Fourier series and the derivative series below to converge absolutely. Restricting \(\psi=N\theta+\phi\) selects only indices \((m,n)=(-Nq,q)\). Conjugation symmetry makes the selected coefficients real, giving
\[
T_{k,p}(\phi)=\overline T_{k,p}+2\sum_{q\ge1}c_s(-Nq,q)\cos(q\phi).
\tag{1}
\]
For clarity, the special-function identities used next are recalled with their justifications. Applying the circular integral representation of \(J_0(r\sqrt H)\) in the two angular variables produces the triple product \(J_{Nq}(r)J_{(N-1)q}(r)J_q(r)\). A Mellin transform first establishes its relation to \(c_s(-Nq,q)\) for \(-1/4<\operatorname{Re}s<0\); individual-mode analytic continuation extends the identity to \(-3/4<\operatorname{Re}s<qN\). Therefore, for \(s=k+\alpha\),
\[
I_q(s)=\int_0^\infty J_{Nq}(r)J_{(N-1)q}(r)J_q(r)r^{-2s-1}\,dr,
\qquad
c_s(-Nq,q)=-A_{k,s}(-1)^{N(q-1)}I_q(s).
\tag{2}
\]
The integral converges absolutely: the Bessel orders sum to \(2Nq\), giving integrability at zero when \(s<qN\), while the fixed-order large-argument decay suffices at infinity for \(s>0\). In particular, \(c_s(-N,1)=-A_{k,s}I_1(s)\).

We reconstruct the positive leading-mode bound needed for the comparison. Neumann's product formula gives
\[
J_N(r)J_{N-1}(r)=\frac2\pi\int_0^{\pi/2}
J_{2N-1}(2r\cos\theta)\cos\theta\,d\theta.
\]
Applying the Weber--Schafheitlin formula to the resulting integral of \(J_{2N-1}(Ar)J_1(r)r^{-2s-1}\) shows it is nonnegative for \(0<A<1\): the hypergeometric numerator parameters are \(2-\alpha,1-\alpha\). For \(1<A<2\), Euler's transformation gives a positive factor times \({}_2F_1(\alpha,2k+3+\alpha;2;A^{-2})\ge1\). Retaining this interval, using \(A/(1+A^2)\ge2/5\), \((4-A^2)^{-1/2}\ge1/\sqrt3\), and substituting \((A^2-1)/A\in(0,3/2)\), yields the explicit estimate (also derived in Proposition 4.3 of the cited paper)
\[
I_1(s)\ge L(k,\alpha):=
\frac{9\Gamma(2-\alpha)}{20\sqrt3\,\pi\Gamma(s+N)(2s+2)}
\left(\frac9{16}\right)^s>0.
\tag{3}
\]

For the **new all-phase comparison**, the standard inequalities
\( |J_j(r)|\le\min\{1,(r/2)^j/j!\}\) for integers \(j\ge0\) yield, by splitting the Mellin integral at \(R_q=2[(Nq)!((N-1)q)!q!]^{1/(2Nq)}\),
\[
|I_q(s)|\le R_q^{-2s}\left(\frac1{2qN-2s}+\frac1{2s}\right),
\qquad R_q\ge\kappa Nq,\quad\kappa=\frac{29}{50}.
\tag{4}
\]
The last lower bound follows from the factorial estimate \(j!\ge(j/e)^j\) (Lemma 5.2 of the cited paper), and applies to every integer \(q\ge1\) for \(N\ge6\). For \(q\ge2\), put
\[
B_N(s)=\frac1{4N-2s}+\frac1{2s},\qquad
U(s)=1+\frac2{2s-3}.
\]
As \(s>3/2\), integral comparison gives
\[
\sum_{q\ge2}q^2|I_q(s)|
\le (\kappa N)^{-2s}B_N(s)\sum_{q\ge2}q^{2-2s}
\le (\kappa N)^{-2s}B_N(s)2^{2-2s}U(s).
\tag{5}
\]
Divide the right-hand side by (3). With \(N=k+2\), write
\[
R(k,\alpha)=\frac{80\sqrt3\,\pi}{9}
\frac{\Gamma(s+N)}{\Gamma(N-s)}(2s+2)
B_N(s)U(s)\left(\frac{10000}{7569N^2}\right)^s.
\tag{6}
\]
We prove the entirely explicit bound \(R(k,\alpha)<\varepsilon_k\). At fixed \(N\ge25\), both \(B_N(s)\) and \(U(s)\) decrease in \(s\in[N-2,N-1]\). Using \(\psi(x)<\log x\), obtained from strict convexity of \(\log\Gamma\), differentiation of (6) yields
\[
\frac{d}{ds}\log R(k,\alpha)
<\log\left(\frac{10000}{7569N^2}(N^2-s^2)\right)+\frac1{s+1}
<\log(1/4)+1/24<0.
\tag{7}
\]
Hence \(R(k,\alpha)\le R(k,0)\). At \(\alpha=0\),
\[
R(k,0)=\frac{80\sqrt3\,\pi}{9}(2k+2)!
\left(\frac1{2k+8}+\frac1{2k}\right)
\left(1+\frac2{2k-3}\right)
\left(\frac{10000}{7569(k+2)^2}\right)^k.
\tag{8}
\]
For \(k=23\), the elementary strict bounds \(\pi<22/7\), \(\sqrt3<7/4\) and exact rational arithmetic give \(R(23,0)<0.766630<4/5\). Moreover the two parentheses before the exponential factor in (8) decrease with \(k\), so for \(k\ge23\),
\[
\frac{R(k+1,0)}{R(k,0)}
<\frac{40000}{7569}\exp\!\left(-\frac{2k}{k+3}\right)
\le\frac{40000}{7569}e^{-23/13}<\frac{19}{20}.
\tag{9}
\]
The last strict comparison follows by bounding \(e^{23/13}\) below by its degree-four Taylor polynomial, an exact rational inequality. Combining (7)--(9) proves
\[
\sum_{q\ge2}q^2|I_q(s)|<I_1(s)\varepsilon_k.
\tag{10}
\]
The included exact-rational script reproduces the two numerical-free inequalities underlying (8)--(9); the uniform inequalities (7) and (9) are analytic and do not rely on finite tests.

Finally, differentiating (1) and using (2), the \(q=1\) term equals \(2A_{k,s}I_1(s)\sin\phi\). For positive integers \(q\), \(|\sin(q\phi)|\le q\sin\phi\) on \([0,\pi]\). Therefore (10) bounds the entire derivative tail by \(2A_{k,s}I_1(s)\varepsilon_k\sin\phi\), proving the two derivative inequalities and strict monotonicity. Likewise \(\sum_{q\ge2}|I_q(s)|\le\sum_{q\ge2}q^2|I_q(s)|\) proves the uniform cosine remainder. Evenness and periodicity finish the stated phase classification.

## Verification
Run `python3 verify_phase.py` (Python standard library). It exactly certifies the rational comparison at \(k=23\), the Taylor lower bound for \(e^{23/13}\), and supplementary exact recurrence comparisons for 101 subsequent degrees. The script reports `VERIFY_OK`. No numerical calculation is used to assert the bounds for an unbounded set of indices; those follow from (7) and (9).

## Relationship to prior work
Pan, You, Wang, Zhou, Zhang and Chen established that the two **sign choices** have strictly different \(L^p\) norms in these exponent intervals; they proved positivity of the first Bessel resonance and controlled only the remaining **odd** resonances, which suffice for the difference between phases zero and \(\pi\). Here the complete continuum of unimodular phases is controlled. The key new step is the \(q^2\)-weighted estimate for **every** resonance \(q\ge2\), yielding global derivative positivity and uniform cosine response. Results concerning the first phase-sensitive **even moment** concern a different exponent at or after the first multinomial collision and do not imply the stated non-even phase theorem. Previous finite-cyclic phase minimax questions optimize on sampled groups rather than normalized integrals over the circle.

## Limitations
The sufficient threshold \(k\ge23\) is not claimed sharp; computational experiments for smaller degrees are not an infinite proof and are not part of this statement. The bound is relative to the positive first-mode amplitude, which tends to zero as \(p\) approaches either adjacent even integer; at the endpoints the norm is phase-independent. The result asserts no general majorant principle for unrelated frequencies or polynomials, and no claim of uniqueness among all coefficient magnitudes. An equivalent phase theorem may exist outside the literature reviewed here. Independent external validation has not been performed.

## References
1. G. Pan, C. You, H. Wang, J. Zhou, W. Zhang and Y. Chen, *Mockenhaupt's Three-Term Hardy--Littlewood Majorant Conjecture*, arXiv:2609.09740v2 (first public version 9 September 2026), §§2--6.
2. S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, J. Math. Anal. Appl. **388** (2012), 136--150, doi:10.1016/j.jmaa.2011.09.053.
3. S. Krenedits, *On Mockenhoupt's conjecture in the Hardy--Littlewood majorant problem*, J. Contemp. Math. Anal. **48** (2013), 91--109, doi:10.3103/S1068362313030011.
4. NIST Digital Library of Mathematical Functions, Bessel product, integral and hypergeometric identities, §§10.9, 10.22, 15.8.
