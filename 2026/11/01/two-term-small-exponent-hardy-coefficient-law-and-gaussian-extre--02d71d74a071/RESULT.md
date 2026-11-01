# Two-term small-exponent Hardy coefficient law and Gaussian extremizers

## Finding
For every **fixed positive integer** \(k\), define the sharp analytic Hardy coefficient constant
\[
C_k(p)=\sup\{|[z^k]f|: f\in H^p(\mathbb D),\ \|f\|_{H^p}=1\}.
\]
Then, as \(p\downarrow0\),
\[
\boxed{C_k(p)=\frac{(k/e)^{k/2}}{k!}\left(\frac2p\right)^{k/2}
\left[1+\frac{(k-1)^2+1}{8}p+O_k(p^{3/2})\right].}
\]
For every fixed \(k\), sufficiently small \(p>0\) has a **unique normalized extremizer**, modulo multiplying the function by a unimodular constant and precomposing with a disk rotation. In its representation \(f(z)=P_s(z)^s\), with \(s=2/p\), \(P_s(z)=\sum_{j=0}^k a_jz^j\), real positive coefficients and \(\sum_j a_j^2=1\), the coefficients obey
\[
\begin{aligned}
a_0&=1-\frac{k}{2s}+O_k(s^{-2}),\\
a_1&=\sqrt{\frac{k}{s}}+O_k(s^{-3/2}),\\
a_2&=\frac{k-1}{s}+O_k(s^{-3/2})\quad (k\ge2),\\
a_j&=O_k(s^{-3/2})\quad (3\le j\le k).
\end{aligned}
\]
Consequently \(P_s\) is zero-free on the closed disk for large \(s\), and
\[
P_s(w/\sqrt s)^s\longrightarrow\exp(-k/2+\sqrt{k}\,w)
\]
locally uniformly for \(w\in\mathbb C\).

## Assumptions and scope
The Hardy norm is \(\|f\|_{H^p}^p=\sup_{0<r<1}\int_{0}^{2\pi}|f(re^{it})|^p\,dt/(2\pi)\). The integer \(k\ge1\) stays **fixed** while \(0<p<1\) tends to zero. \([z^k]f=f^{(k)}(0)/k!\). The power \(P_s^s\) is the analytic branch normalized positive at the origin; its polynomial base is outer and is normalized in \(H^2\). The external input is the outer-polynomial representation of all such extremizers from Brevig--Søvik, arXiv:2610.21788 (Corollary on coefficient functionals). No uniformity in growing \(k\) is claimed.

## Proof
**1. Reduction to a nonnegative polynomial problem.** The cited outer-extremizer theorem, together with the established polynomial factorization for coefficient functionals, gives for each extremizer \(f=P^s\) an outer polynomial \(P(z)=\sum_{j=0}^k a_jz^j\) with \(\sum_{j=0}^k|a_j|^2=1\). By a scalar phase assume \(a_0>0\). Once \(s>k\), the coefficient formula
\[
[z^k]P^s=\sum_{\ell=1}^k\binom{s}{\ell}a_0^{s-\ell}
\sum_{\substack{j_1+\cdots+j_\ell=k\\j_i\ge1}}
 a_{j_1}\cdots a_{j_\ell}
\]
has strictly positive real combinatorial weights. Replacing the coefficients by their moduli cannot decrease its absolute value and preserves their Euclidean norm. We first maximize this coefficient on the compact nonnegative coefficient sphere, without imposing outerness. Later we show that its maximizer is zero-free, making the reduction exact. The test polynomial with \(a_1^2=k/s\), \(a_0^2=1-k/s\), all other coefficients zero, proves the maximum has the positive order \(s^{k/2}\).

**2. Escape to infinity is impossible.** Put \(\varepsilon=s^{-1/2}\), \(a_j=\varepsilon u_j\) for \(1\le j\le k\), \(R^2=\sum_{j=1}^ku_j^2\), and \(a_0=(1-\varepsilon^2R^2)^{1/2}\). Denote by \(H_\varepsilon(u)=s^{-k/2}[z^k]P^s\) the normalized coefficient functional. For \(s\ge2k\), positivity, \(\binom{s}{\ell}\le s^\ell/\ell!\), and \(a_0^{s-\ell}\le a_0^{s-k}\) yield a constant depending only on \(k\) such that
\[
0\le H_\varepsilon(u)\le C_k\exp(-R^2/4)
\sum_{\ell=1}^k s^{(\ell-k)/2}R^\ell.
\]
In particular for \(R\ge1\) the right side is \(\le C'_k e^{-R^2/4}R^k\), uniformly in \(s\). Thus maximizers have \(R\le M_k\), independently of \(s\). On bounded sets the objective converges with all derivatives to
\[
H_0(u)=e^{-R^2/2}\frac{u_1^k}{k!}.
\]
Its unique nonnegative maximizer is \(u_*=(\sqrt{k},0,\ldots,0)\), with value \(c_k=(k/e)^{k/2}/k!\). Hence **every** maximizing sequence converges to \(u_*\). Its unconstrained Hessian is diagonal with values \(-2c_k\) in coordinate one and \(-c_k\) in all other coordinates. It is nonsingular and strictly negative definite.

**3. Uniqueness and positivity.** The expression \(H_\varepsilon(u)\) extends to a real-analytic function in \((\varepsilon,u)\) near \((0,u_*)\), because each product of generalized binomial factors and the powers \((1-\varepsilon^2R^2)^{(\varepsilon^{-2}-\ell)/2}\) has a convergent power series there. The implicit-function theorem yields exactly one stationary point near \(u_*\), smoothly dependent on \(\varepsilon\). All global maximizers lie near it. Moreover at a maximum with \(u_1>0\), a vanishing \(a_j\) for \(j\ge2\) has positive one-sided derivative: the coefficient contains the term linear in \(a_j\) times \(a_1^{k-j}\), while the derivative of \(a_0\) under the sphere constraint vanishes there. Thus all \(a_j\) are strictly positive for \(s>k\) sufficiently large. The implicit-function point is therefore the unique maximizer. Since \(\sum_{j\ge1}a_j=O_k(s^{-1/2})<a_0\), its polynomial is zero-free on \(|z|\le1\), hence outer; it indeed gives an admissible Hardy extremizer.

For complex coefficients to attain equality in the initial triangle inequality, the phases of the \(a_1^k\) term and each \(a_j a_1^{k-j}\) term must agree (all coefficients are nonzero). Thus after making \(a_0>0\), necessarily \(\arg a_j\equiv j\arg a_1\pmod{2\pi}\). All extremizers are obtained from the positive one by a disk rotation and unimodular multiplication.

**4. The second asymptotic coefficient.** Uniformly on bounded \(u\)-sets, the terms affecting the second-order maximal value are
\[
\begin{aligned}
H_\varepsilon(u)=e^{-R^2/2}\Bigg\{&\frac{u_1^k}{k!}
+\varepsilon\,\mathbf1_{k\ge2}\frac{u_2u_1^{k-2}}{(k-2)!}\\
&+\varepsilon^2\left[\frac{u_1^k}{k!}\left(\frac{kR^2}{2}-\frac{R^4}{4}-\frac{k(k-1)}{2}\right)
+\mathbf1_{k\ge3}\frac{u_3u_1^{k-3}}{(k-3)!}
+\mathbf1_{k\ge4}\frac{u_2^2u_1^{k-4}}{2(k-4)!}\right]\Bigg\}
+O_k(\varepsilon^3),
\end{aligned}
\]
where expressions accompanied by an indicator are **omitted** when the indicated index exceeds \(k\). This expansion follows by separating compositions of \(k\) into \(k\), \(k-1\), and \(k-2\) positive parts. Its remainder and the needed derivatives are uniform on a fixed neighborhood of \(u_*\).

Implicit differentiation at the critical point yields
\[
u_1=\sqrt{k}+O_k(\varepsilon^2),\qquad
u_2=(k-1)\varepsilon+O_k(\varepsilon^2)\ (k\ge2),\qquad
u_j=O_k(\varepsilon^2)\ (j\ge3).
\]
At \(u_*\) the direct \(\varepsilon^2\) term divided by \(c_k\) is \(-k^2/4+k/2\). The transverse optimization of \(u_2\), whose Hessian is \(-c_k\), adds \((k-1)^2/2\). Therefore
\[
\max H_\varepsilon
=c_k\left[1+\frac{(k-1)^2+1}{4}\varepsilon^2+O_k(\varepsilon^3)\right].
\]
Substitute \(s=\varepsilon^{-2}=2/p\) for the displayed theorem. The coefficient asymptotics follow from the expansions of the \(u_j\) and the unit-sphere constraint.

**5. Gaussian profile.** For each compact subset of the \(w\)-plane,
\[
P_s(w/\sqrt s)=1+\frac{-k/2+\sqrt{k}\,w}{s}+O_k(s^{-3/2})
\]
uniformly there. Raising to the power \(s\) gives \(\exp(-k/2+\sqrt{k}\,w)\), uniformly on compact sets. The local power is well-defined for large \(s\) because the polynomial is zero-free.

## Verification
All constant factors are relative to the normalized Haar circle measure and the \(k\)-th Taylor **coefficient**, rather than the derivative. The one-mode lower-bound family shows the scaling \(s^{k/2}\); the finite-dimensional compactness argument gives a matching all-function upper bound. Independent finite arithmetic tests in `check.py` check the binomial coefficient formula, the \(k=1\) exact extremal formula, and the predicted two-term expansion for explicit normalized polynomial perturbations with \(1\le k\le6\). The tests validate algebra only, not the all-\(k\) analytical argument.

## Relationship to prior work
Brevig and Søvik (2026, arXiv:2610.21788) prove that extremizers of continuous linear functionals on \(H^p\) are outer when \(0<p<1\), and their coefficient-functional corollary supplies the finite-polynomial representation used above. Brevig and Saksman (arXiv:1905.09547) develop coefficient extremal equations and calculate specific low-order sharp constants. Brevig, Grepstad, and Instanes (2022) study a related fixed-constant-term coefficient extremal problem. These results do not state the all-fixed-degree, small-exponent **two-term** profile, the eventual symmetry uniqueness, or the normalized exponential scaling limit proved here. No historical novelty claim is made for the cited polynomial representation or standard implicit-function theorem.

## Limitations
The estimates are for each fixed \(k\); they are not uniform in the joint regime \(k\to\infty\), \(p\to0\). The extremizer uniqueness is asserted only for sufficiently small \(p\) depending on \(k\). The argument depends on a published representation theorem, whose hypotheses include \(0<p<1\). Older unindexed literature or equivalent reformulations may bear on priority; independent historical and mathematical validation has not been performed. Nothing is claimed for general linear functionals beyond coefficient evaluation.

## References
1. O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, arXiv:2610.21788 (first public 15 October 2026), https://arxiv.org/abs/2610.21788 .
2. O. F. Brevig and E. Saksman, *Coefficient estimates for \(H^p\) spaces with \(0<p<1\)*, arXiv:1905.09547, https://arxiv.org/abs/1905.09547 .
3. O. F. Brevig, S. Grepstad and O. Instanes, *F. Wiener's Trick and an Extremal Problem for \(H^p\)*, doi:10.1007/s40315-022-00469-x, https://doi.org/10.1007/s40315-022-00469-x .
