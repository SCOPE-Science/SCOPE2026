# Zero avoidance and inverse-asymmetry revival counting for stationary telegraph dephasing

## Finding

Let a stationary two-state continuous-time Markov signal \(X_t\in\{+1,-1\}\) jump from \(+1\) to \(-1\) at rate \(a-\varepsilon\) and back at rate \(a+\varepsilon\), where \(a>0\), \(|\varepsilon|<a\), and \(v>0\). Define the phase-memory amplitude
\[
F_{\varepsilon}(t)=\mathbb E\exp\!\left(iv\int_0^t X_s\,ds\right),\qquad t\ge0.
\]

**All-time zero classification.** If \(\varepsilon\ne0\), then \(F_{\varepsilon}(t)\ne0\) for every finite \(t\ge0\), irrespective of \(v\). For \(\varepsilon=0\), positive-time zeros exist if and only if \(v>a\); in that regime, putting \(\omega=\sqrt{v^2-a^2}\), their complete list is
\[
t_j=\frac{(j+1)\pi-\arctan(\omega/a)}{\omega},\qquad j=0,1,\ldots.
\]

**Sharp singular revival count.** Suppose \(v>a\) and \(0<|\varepsilon|<a\). Let \(N(\varepsilon)\) be the number of connected components of
\[
\left\{t>0:\frac{d}{dt}|F_{\varepsilon}(t)|>0\right\}.
\]
This is finite for every nonzero \(\varepsilon\), whereas the symmetric model has infinitely many revival components. As the two jump rates coalesce,
\[
\boxed{\lim_{\varepsilon\to0,\ \varepsilon\ne0}|\varepsilon|N(\varepsilon)
=\frac{v^2-a^2}{2\pi v}\operatorname{arcosh}\!\left(\frac va\right).}
\]
Here the limit is two-sided, and no arbitrary time truncation is made.

**Sharp rounding of each zero.** For each fixed \(j\ge0\), there is a unique nearby local minimum time \(t_j(\varepsilon)=t_j+O_j(\varepsilon^2)\) for sufficiently small nonzero \(\varepsilon\), with
\[
\boxed{|F_{\varepsilon}(t_j(\varepsilon))|
=\frac{v^2(1+a t_j)e^{-a t_j}}{a(v^2-a^2)}|\varepsilon|
+O_j(|\varepsilon|^3).}
\]
The implicit constants in the fixed-\(j\) statement need not be uniform as \(j\to\infty\).

## Assumptions and scope

The state values are exactly \(\pm1\), the switching process is initialized in its stationary distribution \(\mathbb P(X_0=+1)=(a+\varepsilon)/(2a)\), and the quantity counted is the number of intervals of *strictly increasing coherence modulus*, not the number of local maxima of a different distinguishability, channel-capacity, or entanglement observable. Strictly positive switching rates are assumed; frozen limits are excluded. A constant shift in the two signal values multiplies the amplitude by a unit complex phase and leaves all modulus conclusions unchanged. The revival-count asymptotic requires fixed \(v>a>0\) as \(\varepsilon\to0\), with no simultaneous critical-coupling scaling.

## Proof

**1. Exact tilted-generator reduction.** Let \(p_+(t)\) and \(p_-(t)\) denote the phase-weighted state probabilities. The Feynman–Kac equations, including the stationary initial data, are
\[
\frac d{dt}\begin{pmatrix}p_+\\p_-\end{pmatrix}
=\begin{pmatrix}iv-a+\varepsilon&a+\varepsilon\\a-\varepsilon&-iv-a-\varepsilon\end{pmatrix}
\begin{pmatrix}p_+\\p_-\end{pmatrix},\qquad
\begin{pmatrix}p_+(0)\\p_-(0)\end{pmatrix}
=\frac1{2a}\begin{pmatrix}a+\varepsilon\\a-\varepsilon\end{pmatrix}.
\]
The characteristic roots are \(-a\pm z\), where
\[
z^2=a^2-v^2+2iv\varepsilon,\qquad b=a+iv\varepsilon/a.
\]
The branch of \(z\) is chosen with nonnegative real part; for \(\varepsilon\ne0\) its real part is strictly positive. Summing the two components gives
\[
F_{\varepsilon}(t)=e^{-at}\left(\cosh(zt)+\frac bz\sinh(zt)\right).
\]
At \(\varepsilon=0\) and \(v=a\), the continuous limit of this expression is \(e^{-at}(1+at)\).

**2. Rigorous zero exclusion.** For nonzero asymmetry write \(z=u+iw\) with \(u>0\). Equating the imaginary parts of \(z^2\) gives \(2uw=2v\varepsilon\). Therefore
\[
\operatorname{Re}(b\overline z)
=au+\frac{v\varepsilon w}{a}
=u\left(a+\frac{w^2}{a}\right)>0.
\]
Consequently \(|b-z|<|b+z|\). A positive-time zero of the displayed amplitude would require
\[
e^{2zt}=\frac{b-z}{b+z},
\]
whose left-hand modulus is \(e^{2ut}>1\) and whose right-hand modulus is strictly less than one. This is impossible. The initial value is one. For symmetric switching, the formula is strictly positive when \(v\le a\); for \(v>a\) it is \(e^{-at}[\cos(\omega t)+(a/\omega)\sin(\omega t)]\), giving exactly the listed simple zeros.

**3. Exact sign representation for revival intervals.** By conjugation symmetry, \(|F_{-\varepsilon}|=|F_{\varepsilon}|\), so consider \(\varepsilon>0\). Set
\[
c_+=\frac12\left(1+\frac bz\right),\quad c_-=\frac12\left(1-\frac bz\right),\quad
P=|c_+|^2,\quad Q=|c_-|^2,\quad H=c_+\overline{c_-}.
\]
Both coefficients are nonzero: \(b^2-z^2=v^2(1-\varepsilon^2/a^2)\ne0\). The real numbers \(u,w\) satisfy \(0<u<a\) and \(w>0\); the inequality \(u<a\) follows by squaring \(|a^2-v^2+2iv\varepsilon|<a^2+v^2\), which uses \(\varepsilon^2<a^2\). Direct differentiation of
\[
|F_{\varepsilon}(t)|^2=e^{-2at}
\left(Pe^{2ut}+Qe^{-2ut}+2\operatorname{Re}(He^{2iwt})\right)
\]
yields
\[
\frac{e^{2at}}2\frac d{dt}|F_{\varepsilon}(t)|^2
=R\cos(2wt+\vartheta)-A(t),
\]
where
\[
A(t)=(a-u)Pe^{2ut}+(a+u)Qe^{-2ut}>0,
\quad R=2\sqrt{a^2+w^2}|H|>0,
\quad\vartheta=\arg[(-a+iw)H].
\]
As \(A(t)\to\infty\), the derivative is eventually strictly negative. Every positive-derivative component lies inside an interval where the displayed cosine is positive. On each such cosine lobe the function \(R\cos(2wt+\vartheta)-A(t)\) is strictly concave, since \(A''(t)>0\) and the cosine is strictly concave where positive. Hence each lobe contains at most one revival component, and only finitely many lobes can contribute. Since \(F_{\varepsilon}\ne0\), the sign of the derivative of its modulus is exactly the sign of the displayed expression.

**4. Asymptotic number of contributing lobes.** Fix \(v>a\) and put \(\omega=\sqrt{v^2-a^2}\). As \(\varepsilon\downarrow0\),
\[
u=\frac v\omega\varepsilon+O(\varepsilon^3),\quad
w=\omega+O(\varepsilon^2),\quad
P,Q\longrightarrow P_0=\frac{v^2}{4\omega^2},\quad R\longrightarrow2vP_0.
\]
For every bounded interval of scaled times \(\tau=ut\), these imply uniformly
\[
\frac{A(\tau/u)}R\longrightarrow\frac av\cosh(2\tau).
\]
The limit increases from \(a/v<1\) and crosses one only at
\[
\tau_* =\frac12\operatorname{arcosh}(v/a)>0.
\]
For any fixed \(0<d<\tau_*\), all cosine-lobe centers with scaled times between zero and \(\tau_*-d\), apart from at most a bounded endpoint number, have \(A<R\) at their peaks and therefore contribute a revival. No lobe contributes after \((\tau_*+d)/u\): there \(A>R\), and the strict convexity of \(A\), together with its positive derivative at this threshold for small \(\varepsilon\), makes \(A\) increasing thereafter. At most one component lies in each lobe, whose centers are spaced by \(\pi/w\). Thus
\[
\frac{w(\tau_*-d)}{\pi u}+O(1)
\le N(\varepsilon)\le
\frac{w(\tau_*+d)}{\pi u}+O(1).
\]
Multiply by \(\varepsilon\), use \(\varepsilon w/u\to\omega^2/v\), and let \(d\downarrow0\). This gives the claimed exact coefficient. Conjugation symmetry gives the two-sided limit.

**5. Local rounding coefficient.** The simple symmetric zero at \(t_j\) makes \(|F_0(t)|^2\) have a nondegenerate local minimum. Since \(F_{-\varepsilon}=\overline{F_{\varepsilon}}\), the implicit-function theorem applied to \(\partial_t|F_{\varepsilon}|^2\) yields a unique nearby even-in-\(\varepsilon\) critical time \(t_j(\varepsilon)=t_j+O_j(\varepsilon^2)\). Direct differentiation of the exact formula at fixed \(t\) gives
\[
\left.\partial_\varepsilon F_{\varepsilon}(t)\right|_0
=\frac{iv e^{-at}}{a\omega^3}
\left[-a^2t\omega\cos(\omega t)
+(a^2+\omega^2+at\omega^2)\sin(\omega t)\right].
\]
At \(t=t_j\), the zero relation \(\cos(\omega t_j)=-(a/\omega)\sin(\omega t_j)\), together with \(|\sin(\omega t_j)|=\omega/v\), reduces its magnitude to \(v^2(1+a t_j)e^{-a t_j}/(a\omega^2)\). Evenness and analyticity of the squared minimum then produce the stated \(O_j(|\varepsilon|^3)\) remainder after taking a square root.

## Verification

Run `python3 verify.py` with Python 3.10 or later; it requires only standard-library modules. It independently propagates the tilted two-state Markov generator by fourth-order Runge–Kutta and compares it with the closed form (32 comparisons), tests 16 complex spectral/derivative identities, tests eight avoided-zero coefficients, and computes revival-component counts by a provably concave-lobe maximization for seven asymmetries. For \(a=1,v=2\), the theoretical counting coefficient is \(0.314400538709237\ldots\); the calculations at \(\varepsilon=0.002\) and \(0.001\) give respectively \(0.002N=0.314\) and \(0.001N=0.314\). This finite test is not used as a proof of the infinite-time or small-asymmetry theorem.

## Relationship to prior work

Wold, Brox, Galperin and Bergli (2012, arXiv:1206.2174v1) model thermally asymmetric telegraph switching in qubit dephasing; their Section II.B specifies the rate asymmetry and stationary occupations, while Equation (12) displays symmetric telegraph coherence. Feng, Ren, Cai and Peng (2026, DOI 10.1088/1674-1056/ae0398) derive the exact asymmetric two-state dephasing amplitude and show numerical short-time recovery and its suppression by rate asymmetry; their Equation (26) is equivalent to the exact amplitude used here. The present claim is **not** novelty of that expression or of the generic observation that asymmetry damps recoherence. It is the all-time zero/no-zero classification and, especially, the exact inverse-asymmetry asymptotic of the *number of distinct recovery intervals*, with the sharp coefficient and fixed-zero rounding law. Hadipour (2025, arXiv:2504.15808v1) uses symmetric jump rates and varies the initial RTN distribution, a different perturbation. An existing result on symmetric telegraph dephasing with additional depolarization counts entanglement-breaking revivals instead and gives logarithmic, not inverse-asymmetry, scaling; the counted observable and mechanism differ.

## Limitations

The asymptotic assumes stationary initialization, strictly positive *Markovian* telegraph switching rates, a single fluctuator, and fixed strong coupling \(v>a\). It concerns the recovery components of coherence modulus, not a universal measure of information backflow for other channels, not the number of zeros of an ensemble of several fluctuators, and not a uniform joint limit as \(v\downarrow a\). The exact amplitude itself and qualitative transient recovery under asymmetric telegraph noise were previously known. While targeted checks did not identify a prior equivalent revival-count theorem, unlocated work on complex zeros of finite-state Markov additive functionals could imply the result; an independent literature audit has not been carried out.

## References

- H. J. Wold, H. Brox, Y. M. Galperin, and J. Bergli, *Decoherence of a qubit due to a quantum fluctuator or to a classical telegraph noise*, arXiv:1206.2174v1 (public 2012-06-11), https://arxiv.org/abs/1206.2174.
- Y. Feng, J. Ren, X. Cai, and Y. Peng, *Quantum dephasing dynamics in the presence of asymmetric random telegraph noise*, Chinese Physics B **35**, 040204 (2026), DOI:10.1088/1674-1056/ae0398, https://cpb.iphy.ac.cn/article/cstr/32038.14.CPB.ae0398.
- M. Hadipour, *Quantum Speed Limits in Qubit Dynamics Driven by Bistable Random Telegraph Noise: From Markovian to Non-Markovian Regimes*, arXiv:2504.15808v1 (2025-04-22), https://arxiv.org/abs/2504.15808.
