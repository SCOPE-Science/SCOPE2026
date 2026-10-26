# An exact post-descent period-two window for sinusoidal star networks

## Finding
For every integer \(n\ge4\), the unit-weight \((n+1)\)-vertex star supports an explicit symmetric prime-period-two orbit for every \(\kappa=(n+1)h>2\). Its complete full-dimensional stability interval is **exactly** \(2<\kappa<\pi\); at \(\kappa=\pi\) all two-step multipliers equal \(1\), while for \(\kappa>\pi\) the orbit is a repeller. Throughout the stable interval the orbit has an open attracting basin and persists for sufficiently small unequal positive edge weights. These are statements about this specified orbit, not a census of every two-cycle.

## Assumptions and scope
Let \(n\ge4\), and orient all \(n\) edges of the unit-weight star away from its central vertex. The edge-difference torus is \(\mathbb T^n=(\mathbb R/2\pi\mathbb Z)^n\). The reduced sinusoidal map is
\[
G_h(z)=z+hK\sin z\pmod{2\pi},\qquad K=I_n+\mathbf 1\mathbf 1^{\mathsf T},\quad h>0,
\]
where sine acts componentwise. The spectrum of \(K\) consists of \(n+1\) in the direction \(\mathbf1\) and \(1\) on its orthogonal complement (multiplicity \(n-1\)). Set \(\kappa=(n+1)h\). An attracting cycle means that every eigenvalue of its two-step derivative has modulus strictly less than \(1\); a repelling cycle has all moduli strictly greater than \(1\).

## Proof
The diagonal circle \(\mathcal D=\{t\mathbf1:t\in\mathbb R/2\pi\mathbb Z\}\) is invariant because \(K\mathbf1=(n+1)\mathbf1\). Its scalar update is \(f_\kappa(t)=t+\kappa\sin t\pmod{2\pi}\). For \(0<\delta<\pi\), the symmetric pair \(t_\pm=\pi\pm\delta\) is interchanged **without any winding** if and only if
\[
\kappa\sin\delta=2\delta,\qquad \kappa=\frac{2\delta}{\sin\delta}.
\]
The derivative of \(2\delta/\sin\delta\) is positive on \((0,\pi)\): its numerator is \(2(\sin\delta-\delta\cos\delta)\), and \(\sin\delta-\delta\cos\delta\) has derivative \(\delta\sin\delta>0\) and vanishes at \(0\). The ratio ranges strictly from \(2\) to infinity. Thus for each \(\kappa>2\) there is precisely one such \(\delta\), and the points are distinct modulo \(2\pi\). Since \(\sin t_+=-\sin\delta\) and \(\sin t_-=\sin\delta\), direct substitution proves both transition equations. Taylor expansion gives \(2\delta/\sin\delta=2+\delta^2/3+O(\delta^4)\), proving \(\delta\sim\sqrt{3(\kappa-2)}\) at onset.

At each of these two states, \(\cos t_\pm=-\cos\delta\) and
\[
DG_h(z_\pm)=I_n-h\cos\delta\,K.
\]
The same real symmetric derivative occurs at both orbit points. Its eigenvalues are \(1-\kappa\cos\delta\) (simple) and \(1-h\cos\delta\) (multiplicity \(n-1\)). Squaring gives the **complete two-step spectrum**
\[
\mu_\parallel=(1-\kappa\cos\delta)^2,\qquad
\mu_\perp=(1-\tfrac{\kappa}{n+1}\cos\delta)^2\quad\text{(multiplicity \(n-1\)).}
\]
The parameter \(\kappa=\pi\) corresponds exactly to \(\delta=\pi/2\). For \(0<\delta<\pi/2\), the identity \(\kappa\cos\delta=2\delta\cot\delta\in(0,2)\) yields \(|1-\kappa\cos\delta|<1\) and, because \(n+1>1\), also \(|1-h\cos\delta|<1\). Therefore both multipliers lie in \([0,1)\). At \(\delta=\pi/2\), cosine vanishes, and the full derivative of each single step is the identity. For \(\pi/2<\delta<\pi\), cosine is negative, so both single-step eigenvalues exceed \(1\) and both two-step multiplier types exceed \(1\). This establishes all asserted sharp stability regimes, with no numerical approximation or external theorem.

Finally, allow edge weights \(a_1,\ldots,a_n>0\) and set \(A=\operatorname{diag}(a_1,\ldots,a_n)\). The perturbed star map is \(G_{h,A}(z)=z+hKA\sin z\pmod{2\pi}\). At the unit-weight attracting two-cycle, no eigenvalue of \(D(G_h^2)\) equals \(1\). The implicit function theorem therefore continues each isolated fixed point of \(G_{h,A}^2\) uniquely for \(A\) close to \(I_n\). The two continuations are mapped into one another by \(G_{h,A}\), remain distinct, and retain their strict multiplier bounds by continuity. Thus they form one attracting prime-period-two cycle for all sufficiently close positive weights, with an open basin by the local contraction theorem.

## Verification
The self-contained analytic argument proves the existence, uniqueness within the specified symmetric branch, exact multiplier formulas and full claimed parameter classification for **every** integer \(n\ge4\). A separate numerical checker recomputes both transitions and all eigenvalues at \(n\in\{4,5,8\}\), \(\kappa\in\{2.1,2.5,\pi,3.5,5\}\) and confirms the formulas to absolute error below \(10^{-8}\). It tests representative instances only and is not used to infer general truth.

## Relationship to prior work
Buescu, D'Aniello and Oliveira (2026), arXiv:2610.10993v1, derive this network's reduced phase map, the star Gram matrix, and the sharp Lyapunov-descent threshold \(h<2/(n+1)\); their detailed global Morse–Smale theorem is restricted to paths and the three-leaf star at smaller steps. The present statement instead studies the post-descent regime \(h>2/(n+1)\) for stars with at least four leaves. A prior local flip analysis for path networks concerns a different graph family and provides neither the star's exact \(\pi/(n+1)\) stability boundary nor its full transverse spectrum. Scalar sine-map flip calculations alone do not establish transverse attraction in the \(n\)-dimensional star; that extra calculation is explicit above. No global conclusion about Morse–Smale dynamics or every attractor follows.

## Limitations
The exact stability cutoff applies only to the specified **diagonal symmetric two-cycle**, not to all two-cycles or all invariant sets. At the nonhyperbolic boundary \(\kappa=\pi\), no nonlinear basin classification is asserted. Small edge-weight perturbations are treated locally for each strictly attracting parameter, with no uniform perturbation radius claimed. The relation to older discrete phase-oscillator literature is not exhaustively settled; priority is subject to independent verification.

## References
Buescu, J., D'Aniello, E., Oliveira, H. M. (2026). *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, initial public submission 2026-10-07, https://arxiv.org/abs/2610.10993.

Verwoerd, M. and Mason, O. (2008). *Global Phase-Locking in Finite Populations of Phase-Coupled Oscillators*, SIAM Journal on Applied Dynamical Systems 7, 134–160, https://doi.org/10.1137/070686858. Background for continuous-time fixed-point phase locking, not a claim of the present discrete period-two formula.
