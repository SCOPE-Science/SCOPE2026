# A sharp safe-zone threshold for restart-assisted Brownian absorption

## Finding
Let a standard Brownian particle start at the center of the open interval \((-L,L)\), where \(L>0\), and let \(a\in[0,L]\). It is absorbed at either endpoint. Independently, rate-\(r\) Poisson alarms occur. At each alarm before boundary absorption, the particle instantaneously restarts at the center if \(|X|<a\), and is instead immediately absorbed if \(|X|\ge a\). Let \(\tau_{r,a}\) denote the time until absorption, with the no-alarm process denoted by \(r=0\). The Brownian generator is \(\tfrac12\partial_x^2\).

For every \(r>0\), the exact mean absorption time is
\[
\mathbb E\tau_{r,a}=
\frac{\cosh(L\sqrt{2r})-1}{r\cosh((L-a)\sqrt{2r})},
\qquad \mathbb E\tau_{0,a}=L^2.
\]
There exists a strictly beneficial alarm rate, in the sense that \(\mathbb E\tau_{r,a}<L^2\) for some \(r>0\), **if and only if**
\[
\frac{a}{L}<1-\frac1{\sqrt6}.
\]
At and above this sharp safe-zone threshold, every positive alarm rate strictly *increases* the mean absorption time. For every fixed \(0<a<L(1-1/\sqrt6)\), at least one globally optimal positive rate exists.

The onset has an exact critical scaling. Set \(\delta=(1-a/L)^2-1/6\), and approach the threshold from \(\delta>0\). For sufficiently small \(\delta\), the global minimizing rate is unique and satisfies
\[
 r_{\mathrm{opt}}=\frac{540}{7L^2}\delta+O(\delta^2/L^2),
 \qquad
 \frac{\min_{r\ge0}\mathbb E\tau_{r,a}}{L^2}
 =1-\frac{270}{7}\delta^2+O(\delta^3).
\]
When \(a=0\), the infimum is zero as \(r\to\infty\), and it is not attained at finite rate.

## Assumptions and scope
The process is one-dimensional standard Brownian motion, restarted only at independent homogeneous Poisson alarms. The boundary endpoints are perfectly absorbing, and alarms have instantaneous outcomes. The policy depends on the position at an alarm: interior safe positions restart, complementary positions cause immediate completion. The strict inequality convention at \(|X|=a\) has no effect for \(r>0\) because Brownian positions at independent alarm times have continuous distributions. No traversal time, refractory period, drift, or partial boundary reactivity is included.

A Brownian winding model on a circle with shortest-route instantaneous returns corresponds to \(L=2\pi\) and \(a=\pi\); allowing \(a\) to vary describes a **controlled** return-versus-completion decision, not the unmodified shortest-route rule for every threshold.

## Proof
**1. One free attempt and renewal.** Let \(\sigma=\inf\{t\ge0: |B_t|=L\}\) and let \(E_r\) be an independent exponential clock of rate \(r\). Until the earlier of \(\sigma\) and \(E_r\), one attempt follows Brownian motion killed at \(\pm L\). Define its resolvent kernel
\[
G_r(0,x)=\int_0^\infty e^{-rt}\,p_t^{(-L,L)}(0,x)\,dt
=\frac{\sinh(\sqrt{2r}(L-|x|))}{\sqrt{2r}\cosh(L\sqrt{2r})}, \quad |x|<L.
\]
This kernel is continuous, vanishes at the boundaries, solves \((r-\tfrac12\partial_x^2)G_r(0,\cdot)=\delta_0\), and its derivative has jump \(-2\) at zero; these facts fix its normalization. Write
\[
Q_r=\int_{-L}^{L}G_r(0,x)\,dx
=\frac{1-\operatorname{sech}(L\sqrt{2r})}{r},
\]
\[
S_r=\int_{-a}^{a}G_r(0,x)\,dx
=\frac1r\left(1-\frac{\cosh((L-a)\sqrt{2r})}{\cosh(L\sqrt{2r})}\right).
\]
The mean duration of an attempt is \(Q_r=\mathbb E\min(\sigma,E_r)\); the probability that the attempt ends in a safe restart is \(rS_r\). After a safe restart the process is independent of the past and has the same law. Since \(rS_r<1\), the renewal identity gives
\[
\mathbb E\tau_{r,a}=Q_r+rS_r\,\mathbb E\tau_{r,a}
=\frac{Q_r}{1-rS_r}
=\frac{\cosh(L\sqrt{2r})-1}{r\cosh((L-a)\sqrt{2r})}.
\]
The \(r\downarrow0\) limit is \(L^2\), agreeing with the classical exit-time equation \(\tfrac12 u''=-1\), \(u(\pm L)=0\).

**2. Exact phase boundary, including the equality case.** Put \(c=1-a/L\in[0,1]\), \(y=L\sqrt{2r}>0\), and normalize by the no-alarm mean:
\[
R(y,c):=\frac{\mathbb E\tau_{r,a}}{L^2}
=\frac{2(\cosh y-1)}{y^2\cosh(cy)}.
\]
For every integer \(n\ge0\),
\[
\frac{2}{(2n+2)!}\ge\frac{1}{6^n(2n)!}.
\]
Equality holds for \(n=0,1\) and strict inequality for \(n\ge2\): the inequality is equivalent to \(2\cdot6^n\ge(2n+1)(2n+2)\), checked directly for \(n=0,1,2\), and propagated by induction because the quadratic right-hand side grows by a factor smaller than six. Comparing the absolutely convergent even power series yields, for every \(y>0\),
\[
\frac{2(\cosh y-1)}{y^2}
>\cosh(y/\sqrt6).
\]
If \(c\le1/\sqrt6\), monotonicity of \(\cosh\) on the positive reals gives \(R(y,c)>1\) for every \(y>0\). Conversely, expansion at the origin gives
\[
R(y,c)=1+\left(\frac1{12}-\frac{c^2}{2}\right)y^2+O(y^4).
\]
If \(c>1/\sqrt6\), the quadratic coefficient is negative, so every sufficiently small positive \(y\) gives \(R(y,c)<1\). This proves the if-and-only-if threshold, including strict non-improvement exactly at the boundary. For \(0<a<L\), the same expression grows like \(2e^{a\sqrt{2r}}/(L^2(2r))\) in normalized units, equivalently \(\mathbb E\tau_{r,a}\sim e^{a\sqrt{2r}}/r\), as \(r\to\infty\), ensuring existence of a positive global minimizer whenever improvement is possible. For \(a=0\), the mean is asymptotic to \(1/r\).

**3. Critical optimization law.** Set \(z=y^2\) and \(\delta=c^2-1/6\). The normalized expression is analytic in \((z,\delta)\) near \((0,0)\), and its Taylor expansion is
\[
R=1-\frac{\delta z}{2}+\frac7{4320}z^2
+O(\delta z^2+z^3).
\]
At \(\delta=0\), step 2 shows strict inequality \(R(z,0)>1\) for \(z>0\); moreover the large-\(z\) divergence is uniform for \(c\) in a sufficiently small neighborhood of \(1/\sqrt6\), which lies below one. Therefore every minimizing \(z\) for \(\delta\downarrow0\) must tend to zero. Since \(\partial_z^2R(0,0)=7/2160>0\), the implicit-function theorem applied to \(\partial_zR=0\) gives a unique positive local minimizer for sufficiently small \(\delta>0\), and it is necessarily the unique global minimizer. Solving the stationary equation gives
\[
z_{\mathrm{opt}}=\frac{1080}{7}\delta+O(\delta^2).
\]
Since \(r=z/(2L^2)\), the first critical asymptotic follows. Substitution into the Taylor expansion gives \(R_{\min}=1-(270/7)\delta^2+O(\delta^3)\), completing the proof.

## Verification
A standalone script, `verify_threshold.py`, independently solves the backward finite-difference equations for the Brownian mean with state-dependent alarm outcomes, compares its center value to the closed formula, samples parameter values on both sides of the geometric threshold, and tests the critical scaling. It executed successfully with 157 checks; the largest reported relative discrepancy between its finite-difference solver and the exact mean was below \(1.55\times10^{-3}\). Numerical checks support but do not replace the all-parameter argument above. Run with Python 3, NumPy and SciPy: `python verify_threshold.py`.

## Relationship to prior work
Grange, *Winding number of a Brownian particle on a ring under stochastic resetting* (arXiv:2111.15241), specifies the geometrically shortest return with fixed safe region \((-\pi,\pi)\) for an interval \((-2\pi,2\pi)\) and develops its renewal law. The present theorem treats a variable feedback threshold and identifies the exact **global beneficial-reset phase boundary** and near-critical optimal-rate and gain scaling. The renewal principle itself is not new. Pal–Prasad (arXiv:1812.03009) and Chen–Huang (arXiv:2109.11101) analyze standard resetting in bounded domains with absorption at fixed boundaries; their resetting events do not terminate the attempt conditionally on position. Resetting and absorption models with occupation-time thresholds, such as Bressloff (arXiv:2205.13989), have a different stopping rule. These comparisons delimit the claimed contribution; no general priority or independent validation is asserted.

## Limitations
The critical threshold is specific to Brownian diffusion with instantaneous outcomes and a centered symmetric feedback region. General drift, other diffusivities (beyond deterministic time rescaling), non-Poisson alarms, finite return times, and nonsymmetric thresholds are not covered. Existence of a finite positive global optimum is shown for beneficial \(0<a<L\), but global uniqueness away from the critical regime is not claimed. The result is analytical; the finite-difference tests are not proofs and do not establish physical feasibility. Literature searches cannot certify global novelty, and a related bounded-domain paper was available only in abstract during the priority comparison.

## References
1. P. Grange, *Winding number of a Brownian particle on a ring under stochastic resetting*, arXiv:2111.15241 (first public version 2021-11-30); Journal of Physics A 55 (2022), 155003. https://arxiv.org/abs/2111.15241
2. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009; Physical Review E 99 (2019), 032123. https://arxiv.org/abs/1812.03009
3. H. Chen and F. Huang, *First passage of a diffusing particle under stochastic resetting in bounded domains with spherical symmetry*, arXiv:2109.11101; Physical Review E 105 (2022), 034109. https://arxiv.org/abs/2109.11101
4. P. C. Bressloff, *Diffusion in a partially absorbing medium with position and occupation time resetting*, arXiv:2205.13989. https://arxiv.org/abs/2205.13989
