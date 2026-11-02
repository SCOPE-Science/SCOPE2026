# Sharp gain-optimal Floquet plateau and memory threshold for scalar RMSProp

## Finding

For the deterministic epsilon-outside RMSProp map on a one-dimensional positive quadratic, every gain above the minimizer-instability threshold admits exactly one primitive two-cycle, and that cycle is locally exponentially attracting at **every** such gain. Its two-step Floquet spectral radius has a globally minimal plateau, exactly equal to the memory-retention factor \(\beta\), and the sharp threshold \(\beta=1/9\) determines whether this plateau ends at a finite gain or extends to arbitrarily large gains.

Precisely, let \(\lambda,\varepsilon>0\), \(0<\beta<1\), and \(h>0\), and set
\[
F(x,v)=\left(x-\frac{h\lambda x}{\sqrt{\beta v+(1-\beta)\lambda^2x^2}+\varepsilon},\quad \beta v+(1-\beta)\lambda^2x^2\right),\qquad v\ge0.
\]
The unique nontrivial period-two orbit (up to cycling its two points) exists if and only if \(h>h_*=2\varepsilon/\lambda\). It is
\[
(r,\lambda^2r^2)\longleftrightarrow(-r,\lambda^2r^2),\qquad r=\frac h2-\frac\varepsilon\lambda>0.
\]
Put
\[
t=-1+3\beta+\frac{4(1-\beta)\varepsilon}{h\lambda},\qquad \theta_\pm=\frac{t\pm\sqrt{t^2-4\beta}}2.
\]
The two Floquet multipliers of the **two-step** map are exactly \(\theta_+^2\) and \(\theta_-^2\), with complex square root interpreted in the usual sense. Both have modulus less than one for every \(h>h_*\). In particular, for \(\rho=\max(|\theta_+|^2,|\theta_-|^2)\), one has \(\rho\ge\beta\), with equality if and only if \(|t|\le2\sqrt\beta\).

Define
\[
h_{\mathrm{in}}=\frac{4(1-\beta)\varepsilon}{\lambda(1-3\beta+2\sqrt\beta)}.
\]
This is always strictly larger than \(h_*\). If \(0<\beta<1/9\), also define
\[
h_{\mathrm{out}}=\frac{4(1-\beta)\varepsilon}{\lambda(1-3\beta-2\sqrt\beta)}.
\]
Then \(\rho=\beta\) **exactly** when \(h_{\mathrm{in}}\le h\le h_{\mathrm{out}}\); \(\rho>\beta\) outside that closed interval. If \(1/9\le\beta<1\), then \(\rho=\beta\) exactly when \(h\ge h_{\mathrm{in}}\). Thus the memory factor \(1/9\) is the exact threshold at which the gain-optimal spectral plateau becomes unbounded. At its endpoints the multipliers coincide and the two-step derivative is defective (not semisimple); the spectral-radius statement remains exact, but a uniform pure \(\beta^n\) operator-norm rate need not hold there.

As an exact instance, take \(\lambda=\varepsilon=1\), \(\beta=1/25\). The primitive cycle exists for \(h>2\), and its minimum two-step spectral radius is \(1/25\) **precisely for** \(3\le h\le8\). For \(h>8\) the cycle remains exponentially attracting, but its local spectral contraction worsens as \(h\) increases.

## Assumptions and scope

The physical state space is \(\mathbb R\times[0,\infty)\), with the indicated epsilon-outside square-root convention, a fixed deterministic quadratic loss \(f(x)=\lambda x^2/2\), no momentum or bias correction, and memory decay \(0<\beta<1\). A period-two orbit means two distinct phase-space points exchanged by \(F\). Floquet multipliers and local exponential attraction refer to the differentiable two-step map at those nonzero cycle points; no claim about global attraction basins is made. At \(h=h_*\) the nontrivial orbit has collapsed to the fixed point and is not counted as a primitive period-two orbit.

## Proof

**Step 1: every two-cycle is antipodal and has constant memory.** Suppose \((x_1,v_1)\) and \((x_2,v_2)\) form a nontrivial two-cycle. Neither position is zero, since \(F(0,v)\) has zero position forever. The equal-and-opposite displacements force \(x_1x_2<0\), and, writing \(a=\lambda|x_1|\), \(b=\lambda|x_2|\), \(u=\sqrt{v_1}\), \(w=\sqrt{v_2}\), the position equations imply \(a(u+\varepsilon)=b(w+\varepsilon)\). The two memory equations give
\[
(1+\beta)u^2=\beta a^2+b^2,\qquad(1+\beta)w^2=a^2+\beta b^2.
\]
If \(a>b\), the displacement identity gives \(au<bw\), whereas the displayed equations give \((1+\beta)(a^2u^2-b^2w^2)=\beta(a^4-b^4)>0\), a contradiction. The reversed case is identical. Hence \(a=b\), then \(u=w=a\), and \(x_2=-x_1\). The spatial multiplier on this orbit must be \(-1\), so \(\lambda|x_1|+\varepsilon=h\lambda/2\). This proves the exact orbit and both directions of the existence/uniqueness statement.

**Step 2: exact two-step characteristic polynomial.** At the positive point set \(r=h/2-\varepsilon/\lambda\), \(S=\lambda r+\varepsilon=h\lambda/2\). Direct differentiation of the original \((x,v)\) map gives
\[
J_+=\begin{pmatrix}-1+4(1-\beta)r/h&2\beta/(h\lambda^2)\\2(1-\beta)\lambda^2r&\beta\end{pmatrix}.
\]
By the odd/even symmetry of the position/memory updates, \(J_-=RJ_+R\), where \(R=\operatorname{diag}(-1,1)\). The two-step Jacobian is \(J_-J_+=(RJ_+)^2\). Writing \(K=RJ_+\), direct multiplication gives
\[
\operatorname{tr}K=1+\beta-\frac{4(1-\beta)r}{h}=t,\qquad\det K=\beta.
\]
Thus the characteristic polynomial of \(K\) is \(z^2-tz+\beta\), and the two-step multipliers are the squares of its roots.

**Step 3: strict attraction for every supercritical gain.** Because \(0<r/h<1/2\), we have
\[
1+\beta-t=\frac{4(1-\beta)r}{h}>0,\quad1+\beta+t=2(1+\beta)-\frac{4(1-\beta)r}{h}>4\beta>0,\quad0<\beta<1.
\]
The degree-two Schur criterion therefore places both roots of \(z^2-tz+\beta\) strictly inside the unit disk. Since the cycle points have strictly positive memory, the map is smooth in their neighborhoods and the strict spectral bound implies local exponential attraction.

**Step 4: sharp spectral optimum and its two memory regimes.** The root product is \(\beta\), hence the two-step spectral radius is at least \(\beta\). Equality holds exactly when the two roots are a complex-conjugate pair or coincide, equivalently \(|t|\le2\sqrt\beta\). As \(h\) increases from \(h_*\) to infinity, \(t\) decreases continuously and strictly from \(1+\beta\) toward \(-1+3\beta\). Solving \(t=2\sqrt\beta\) gives \(h_{\mathrm{in}}\); the inequality \((1-\sqrt\beta)^2>0\) shows \(h_{\mathrm{in}}>h_*\). A finite solution of \(t=-2\sqrt\beta\) exists precisely when \(1-3\beta-2\sqrt\beta>0\). Factoring with \(q=\sqrt\beta\) gives \(1-3q^2-2q=(1-3q)(1+q)\), positive precisely for \(\beta<1/9\). This proves both plateau descriptions. At either finite endpoint, \(K\) has repeated eigenvalue \(\pm\sqrt\beta\); its off-diagonal entry \(-2\beta/(h\lambda^2)\) is nonzero, so \(K\) and its square have a nontrivial Jordan block.

## Verification

A standalone standard-library checker `checker.py` verifies exact rational orbit instances at gains \(3,4,8\) with \(\lambda=\varepsilon=1\), \(\beta=1/25\), checks the rational Jacobian identities and two-step characteristic data, and independently tests numerical Jacobians, multipliers, and plateau boundaries over a deterministic parameter grid. These computations audit the algebra and examples; the universal quantifiers follow from Steps 1–4, not finite sampling. Execute `python3 checker.py` from the same directory.

## Relationship to prior work

Loh, Mireles James, Xu, and Tao (2026), arXiv:2610.30078v1, establish antipodal symmetry for period-two orbits (Lemma 5.1), the sharp existence boundary (Theorem 5.3), and attraction of a branch sufficiently close to that boundary (Theorem 5.7). Their proof already gives the general two-step factorization and block-Jacobian formula (equations (43)–(44)), ingredients specialized here rather than claimed as new; Section 8.3.1 reports one-dimensional attraction as a computational observation. The present statement proves global-in-gain local attraction for the scalar two-cycle and gives the exact two-step spectral-rate phase diagram and the memory threshold \(1/9\). The earlier RMSProp global-stability theorem of Dimitrieski et al. (2026), arXiv:2603.15823, addresses convergence to the minimizer below the gain threshold, not the supercritical two-cycle. Prior analysis of continuous-time RMSProp central flows does not provide this discrete, epsilon-outside Floquet spectrum. The critical-gain equality case has a separate asymptotic theory; the result here concerns strictly supercritical gain and does not claim novelty for equality.

## Limitations

The result is one-dimensional, deterministic, epsilon-outside, and quadratic, and only proves *local* exponential attraction of the specified period-two orbit. It does not claim every trajectory converges to that orbit, nor classify other attractors for different update conventions or higher-dimensional Hessians. The plateau concerns linearized two-step spectral radius. At defective plateau endpoints, the actual linear error can carry a polynomial prefactor; the exact spectral radius is still \(\beta\). The source comparison supports a provisional originality assessment, not independent priority certification.

## References

1. K. Loh, J. D. Mireles James, Z. Xu, M. Tao, *The Dynamics of RMSProp Beyond the Stability Threshold* (2026), arXiv:2610.30078v1, https://arxiv.org/abs/2610.30078 .
2. N. Dimitrieski, M. C. Honecker, C. Scherer, C. Ebenbauer, *Global Stability and Step Size Robustness of RMSProp* (2026), arXiv:2603.15823, https://arxiv.org/abs/2603.15823 .
3. J. Cohen et al., *Understanding Optimization in Deep Learning with Central Flows* (2025), relevant RMSProp companion exposition, https://centralflows.github.io/part3/ .
