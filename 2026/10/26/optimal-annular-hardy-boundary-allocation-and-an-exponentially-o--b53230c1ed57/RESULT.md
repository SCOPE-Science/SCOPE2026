# Optimal annular Hardy boundary allocation and an exponentially oscillating thin-annulus bias

## Finding
Let \(0<q<1\), \(q<r<1\), and let \(t\in(0,1)\) be the proportion of unit total boundary norm allocated to the **outer** circle. The squared norm of evaluation at \(r\) is
\[
K_{q,t}(r)=\sum_{n\in\mathbb Z}\frac{r^{2n}}{t+(1-t)q^{2n}}.
\]
Write \(t_q(r)\) for the optimal outer mass and \(J_q(r)=K_{q,t_q(r)}(r)\) for the minimum squared evaluation norm. The following results hold.

1. **Global sharp design.** For every admissible \(q,r\) there is exactly one minimizer \(0<t_q(r)<1\). It increases strictly with \(r\), and
\[
t_q(q/r)=1-t_q(r),\qquad t_q(\sqrt q)=\tfrac12.
\]
In particular \(t_q(r)>1/2\) exactly when \(r>\sqrt q\).

2. **Thin annulus and nonperturbative oscillation.** Fix \(0<\alpha<1\), put \(q=e^{-h}\), \(r=e^{-\alpha h}\), \(E_h=e^{-\pi^2/h}\), and
\[
\Phi_\alpha(h)=\frac{\pi}{h}\log\frac{1-\alpha}{\alpha}+\pi\alpha.
\]
As \(h\downarrow0\),
\[
\boxed{t_q(r)=1-\alpha-\frac{4\pi\sin(\pi\alpha)}h E_h\cos\Phi_\alpha(h)+O_\alpha(E_h).}
\]
The sharp minimum is
\[
\boxed{J_q(r)=\frac{\pi}{2h\sin(\pi\alpha)\alpha^\alpha(1-\alpha)^{1-\alpha}}
\left[1+4\sin(\pi\alpha)E_h\sin\Phi_\alpha(h)+O_\alpha(h^{-2}E_h^2)\right].}
\]
For every fixed \(\alpha\ne1/2\), the sign of \(t_q(r)-(1-\alpha)\) reverses infinitely many times as \(h\downarrow0\). At \(\alpha=1/2\), the optimizer is **identically** \(1/2\) by symmetry, not merely asymptotically so. Error constants may depend on fixed \(\alpha\); uniform versions hold on compact subintervals of \((0,1)\).

3. **Thick annulus and the logistic midpoint window.** For \(h\to\infty\), fix \(L<\infty\) and \(|\lambda|\le L\), and set
\[
q=e^{-h},\quad r=e^{-h/2-\lambda},\quad \alpha=\tfrac12+\lambda/h.
\]
Then uniformly in \(\lambda\),
\[
\boxed{t_q(r)=\frac1{1+e^{2\lambda}}+O_L(e^{-h}),\qquad
J_q(r)=1+4e^{-h}\cosh^2\lambda+O_L(e^{-2h}).}
\]
For each fixed \(0<\alpha<1\), without restricting to the midpoint window, the thick-annulus leading laws are
\[
\frac{1-t_q(e^{-\alpha h})}{t_q(e^{-\alpha h})}=e^{-(1-2\alpha)h}(1+o(1)),\qquad
J_q(e^{-\alpha h})=1+\big(e^{-\alpha h}+e^{-(1-\alpha)h}\big)^2(1+o(1)).
\]
The last relation concerns the excess over the constant-function mode \(1\), not the full norm.

## Assumptions and scope
The annulus is \(\mathcal A_q=\{z\in\mathbb C:q<|z|<1\}\). A holomorphic Laurent series \(f(z)=\sum_{n\in\mathbb Z}c_nz^n\) is given the two-boundary Hilbert norm
\[
\|f\|_{q,t}^2=t\frac1{2\pi}\int_0^{2\pi}|f(e^{i\theta})|^2\,d\theta
+(1-t)\frac1{2\pi}\int_0^{2\pi}|f(qe^{i\theta})|^2\,d\theta.
\]
Weights are constant on each circle and sum to one. Boundary integration is **angular probability measure**, not arc length; changing conventions changes the correspondence between \(t\) and physical density. Point evaluation is at any point \(z\) with \(|z|=r\); rotation leaves its norm unchanged. The optimization varies only the two boundary masses, not the domain, the point, or nonconstant angular densities. Here and below \(J\) is the **squared** evaluation norm; the norm itself is \(\sqrt J\).

## Proof
**Reproducing-kernel reduction.** Parseval gives \(\|f\|_{q,t}^2=\sum_{n\in\mathbb Z}|c_n|^2[t+(1-t)q^{2n}]\). The sharp Cauchy–Schwarz inequality for evaluation gives \(K\) above and is attained by its reproducing kernel. For every fixed interior \(t\) the series converges absolutely; the positive modes are bounded by \(\sum_{n\ge0}r^{2n}/t\), and negative modes by \(\sum_{m\ge1}(q/r)^{2m}/(1-t)\).

**Existence, uniqueness and radial monotonicity.** Put \(a=r\), \(b=q/r\), \(v_m=q^{2m}\). Pairing positive and negative modes yields
\[
K_{q,t}(r)=1+\sum_{m\ge1}\left(
\frac{a^{2m}}{t+(1-t)v_m}+\frac{b^{2m}}{1-t+tv_m}\right).
\]
Its first and second derivatives are
\[
K_t=\sum_{m\ge1}(1-v_m)\left[\frac{b^{2m}}{(1-t+tv_m)^2}-\frac{a^{2m}}{(t+(1-t)v_m)^2}\right],
\]
\[
K_{tt}=2\sum_{m\ge1}(1-v_m)^2\left[\frac{b^{2m}}{(1-t+tv_m)^3}+\frac{a^{2m}}{(t+(1-t)v_m)^3}\right]>0.
\]
As \(t\downarrow0\), the positive-mode series tends to \(\sum_{m\ge1}(r/q)^{2m}=\infty\); as \(t\uparrow1\), the negative-mode series tends to \(\sum_{m\ge1}r^{-2m}=\infty\). Fatou's lemma makes the divergence rigorous. Thus strict convexity gives an interior unique minimizer. At fixed \(t\), the displayed \(K_t\) is strictly decreasing as \(r\) increases, since \(b=q/r\) decreases and \(a=r\) increases. Its unique zero therefore increases with \(r\). Interchanging the two circles in the paired series gives \(K_{q,t}(r)=K_{q,1-t}(q/r)\), which proves reflection and midpoint identities.

**Exact thin-annulus Fourier formula.** For fixed \(\alpha\in(0,1)\) and \(h>0\), define
\[
F_{t,\alpha}(x)=\frac{e^{-2\alpha x}}{t+(1-t)e^{-2x}},\qquad
\widehat F_{t,\alpha}(\xi)=\int_{\mathbb R}F_{t,\alpha}(x)e^{-i\xi x}\,dx.
\]
The change \(y=e^{2x}\) and Euler's beta integral yield the **exact**, absolutely convergent transform
\[
\widehat F_{t,\alpha}(\xi)=\frac\pi2\frac{t^{\alpha+i\xi/2-1}(1-t)^{-\alpha-i\xi/2}}{\sin(\pi\alpha+i\pi\xi/2)}.
\]
The exponential decay of \(F\) and its derivatives justifies Poisson summation, so \(K_{e^{-h},t}(e^{-\alpha h})=\sum_{n\in\mathbb Z}F_{t,\alpha}(nh)\) is exactly
\[
\frac{\pi t^{\alpha-1}(1-t)^{-\alpha}}{2h\sin(\pi\alpha)}\left[
1+2\sum_{k\ge1}\operatorname{Re}\left\{
\frac{\sin(\pi\alpha)}{\sin(\pi\alpha+i\pi^2k/h)}
\exp\left(\frac{i\pi k}{h}\log\frac{t}{1-t}\right)
\right\}\right].
\]
Write \(C_h(t)=\frac{\pi}{2h\sin(\pi\alpha)}t^{\alpha-1}(1-t)^{-\alpha}\). Uniformly for \(t\) in every compact subset of \((0,1)\), the series and its first two \(t\)-derivatives satisfy
\[
K/C_h=1+4\sin(\pi\alpha)e^{-\pi^2/h}\sin\left(
\frac\pi h\log\frac t{1-t}+\pi\alpha\right)
+O_\alpha(e^{-2\pi^2/h}),
\]
where after taking \(j\in\{0,1,2\}\) derivatives the error is \(O_{\alpha,j}(h^{-j}e^{-2\pi^2/h})\). This follows by expanding the \(k=1\) hyperbolic sine denominator and summing \(k\ge2\) as a geometric tail.

The positive envelope \(C_h\) has its unique minimum at \(t_0=1-\alpha\), with \(C_h'(t_0)=0\) and \(C_h''(t_0)/C_h(t_0)=1/[\alpha(1-\alpha)]\). To justify perturbation at the true optimizer, the relative oscillatory term is uniformly \(O(e^{-\pi^2/h})\) globally in \(t\), since the complex exponent has unit modulus for real \(t\). For any fixed small neighborhood of \(t_0\), the strictly larger envelope outside it forces the true minimizer into that neighborhood. Local derivative estimates and strictly positive curvature then give displacement \(O(h^{-1}e^{-\pi^2/h})\). Substituting \(t_0\) into the phase, and differentiating, gives
\[
t_q(r)-t_0=-\frac{4\pi\sin(\pi\alpha)}h e^{-\pi^2/h}\cos\Phi_\alpha(h)
+O_\alpha(e^{-\pi^2/h}).
\]
Substituting that displacement into the objective changes the relative value only by \(O_\alpha(h^{-2}e^{-2\pi^2/h})\), proving the stated formula for \(J\). For \(\alpha\ne1/2\), the coefficient \(\log[(1-\alpha)/\alpha]\) of \(1/h\) in the phase is nonzero, so sequences along which its cosine is \(+1\) and \(-1\) both accumulate at \(h=0\). The asymptotic remainder is smaller by a factor \(O(h)\), proving infinitely many sign reversals by continuity. The symmetric \(\alpha=1/2\) case follows from the exact reflection identity.

**Thick-annulus scale.** Set \(r=e^{-h/2-\lambda}\) and \(q=e^{-h}\). Uniformly for \(|\lambda|\le L\) and \(t\) in any fixed compact subinterval of \((0,1)\), the paired series and its first two derivatives yield
\[
K_{q,t}(r)=1+e^{-h}\left(\frac{e^{-2\lambda}}t+\frac{e^{2\lambda}}{1-t}\right)+O_L(e^{-2h}).
\]
The leading strictly convex bracket is minimized at \(t=(1+e^{2\lambda})^{-1}\), with minimum \((e^{-\lambda}+e^{\lambda})^2=4\cosh^2\lambda\). Uniform derivative control and a positive local Hessian of size \(e^{-h}\) show that the true optimizer differs by \(O_L(e^{-h})\), giving both displayed thick-annulus formulas. For fixed \(\alpha\) away from the moving logarithmic center, comparing the exact paired-series derivative with its \(m=1\) term at \(t_0=a/(a+b)\), where \(a=e^{-\alpha h}\), \(b=e^{-(1-\alpha)h}\), shows that higher modes are a vanishing relative perturbation; thus \(t_q(r)/t_0\to1\) and \((1-t_q(r))/(1-t_0)\to1\). The remaining fixed-\(\alpha\) assertions follow.

## Verification
A standalone finite-sum checker `annular_opt_check.py` verifies strict positivity of the Hessian, numerical root conditions, exact reflection, direction of radial bias, and the thin/thick limiting formulas over 270 individual tests. An independent high-precision script `high_precision_bias.py` resolves exponentially small changes of sign and verifies the first Fourier correction at \(h=0.6,0.45,0.3\), including differences at the scale \(10^{-13}\). The scripts use SciPy and mpmath and can be invoked with `python annular_opt_check.py` and `python high_precision_bias.py`. These finite checks **support** the formulas but do not establish the all-parameter theorem; the analytic proof above does.

## Relationship to prior work
The annular Szegő kernel and its **weighted bilateral series and theta-product representations** are not new. Gafai–Murid–Wahid (2022), particularly §5, obtain the weighted kernel and study its zeros. Their weight ratio is equivalent to \((1-t)/t\) here after an overall kernel normalization. Jain–Verma (2023) prove regularity and weight dependence of weighted Szegő kernels for planar domains. Ameur–Charlier–Cronvall (2024) encounter oscillatory theta functions and weighted annular Szegő kernels in random-normal-matrix asymptotics; oscillations of such kernels are therefore not claimed as a new general phenomenon. Gafai et al. (2023) also study zeros in doubly connected domains. The subject here differs: **global minimization over fixed total boundary mass at a specified interior evaluation point**, strict radial behavior of that minimizing mass, its beyond-all-orders sign-changing deviation from harmonic measure, and the thick-annulus logistic transition. The known bilateral formula is an input, not a novelty claim.

## Limitations
The boundary mass is constant along each circle; no optimization over arbitrary angular weight functions or general multiply connected domains is asserted. The asymptotics fix \(\alpha\) or bound \(\lambda\) as indicated, and do not assert joint uniformity when \(\alpha\) approaches 0 or 1 in the thin regime. The sign-reversal theorem excludes the symmetric midpoint, where the deviation is exactly zero. Numerical tests are not a substitute for proof. Historical priority is not mathematically decidable by finite literature searches; equivalent parametrizations in uninspected literature remain a risk. Independent validation has not been performed.

## References
- N. S. Gafai, A. H. M. Murid, and N. H. A. A. Wahid, *Infinite Product Representation for the Szegő Kernel for an Annulus*, arXiv:2202.09114v1 (2022), especially §§2 and 5. https://arxiv.org/abs/2202.09114
- A. Jain and K. Verma, *Weighted Szegő Kernels on Planar Domains*, arXiv:2308.07021v1 (2023), especially §§1–2. https://arxiv.org/abs/2308.07021
- Y. Ameur, C. Charlier, and J. Cronvall, *Random Normal Matrices: Eigenvalue Correlations Near a Hard Wall*, Journal of Statistical Physics (2024), doi:10.1007/s10955-024-03314-8, §3. https://doi.org/10.1007/s10955-024-03314-8
- N. S. Gafai, A. H. M. Murid, S. Naqos, and N. H. A. A. Wahid, *Computing the zeros of the Szegő kernel for doubly connected regions using conformal mapping*, AIMS Mathematics **8** (2023), 12040–12061, doi:10.3934/math.2023607. https://doi.org/10.3934/math.2023607
