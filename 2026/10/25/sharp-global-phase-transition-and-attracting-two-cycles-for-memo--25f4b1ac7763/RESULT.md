# Sharp global phase transition and attracting two-cycles for memoryless Riemannian RMSProp on the circle

## Finding
For each \(\varepsilon>0\), the constant-step, deterministic, memoryless endpoint of the embedded-submanifold Riemannian RMSProp method has a *sharp global convergence threshold* \(\alpha=2\varepsilon\) for the linear objective on the unit circle. At equality, every orbit apart from the nonminimal stationary point converges to the minimum, with a sharp reciprocal-iteration error law unless it terminates finitely. For every larger step, a unique symmetric nonzero period-two orbit emerges and is locally attracting. Its onset is linear rather than the usual square-root scaling of smooth flips.

## Assumptions and scope
Let \(M=S^1=\{x\in\mathbb R^2:\|x\|_2=1\}\), \(f(x)=-x_1\), and \(\varepsilon>0\). Use the induced metric, \(P_x=I-xx^{\mathsf T}\), and the normalization retraction \(R_x(\eta)=(x+\eta)/\|x+\eta\|_2\) for \(\eta\in T_xM\). In the original projected-preconditioned RMSProp example of Sakai--Iiduka's Algorithm 1, take the full gradient, no momentum, zero second-moment memory \(\beta_2=0\), fixed step \(\alpha>0\), and \(H=\operatorname{diag}(|g_1|+\varepsilon,|g_2|+\varepsilon)\), with \(g=\operatorname{grad} f(x)\). Thus \(x^+=R_x(-\alpha P_x H^{-1}g)\). This is an endpoint specialization, **not** a claim about positive-memory RMSProp, AMSGrad, or the stochastic method. Angles \(\theta\in(-\pi,\pi]\) use \(x=(\cos\theta,\sin\theta)\); \(\theta=\pi\) is the nonminimal stationary point, excluded from the convergence assertion.

For every initial \(\theta_0\in(-\pi,\pi)\), the following hold:

1. If \(0<\alpha\le2\varepsilon\), then \(|\theta_{n+1}|<|\theta_n|\) whenever \(\theta_n\ne0\), hence \(\theta_n\to0\). When \(0<\alpha<2\varepsilon\), the local multiplier is \(1-\alpha/\varepsilon\); at \(\alpha=\varepsilon\), any nonterminating sequence has \(|\theta_{n+1}|/|\theta_n|^2\to1/\varepsilon\). At \(\alpha=2\varepsilon\), either a finite iterate equals zero, or the signs eventually alternate and \(\lim_{n\to\infty} n|\theta_n|=\varepsilon/2\).
2. If \(\alpha>2\varepsilon\), there is exactly one \(\theta_*\in(0,\pi/4)\) satisfying \(F_{\alpha,\varepsilon}(\theta_*)=-\theta_*\). Its symmetric primitive two-cycle \(\theta_*\leftrightarrow-\theta_*\) is locally attracting. With \(t_*=\tan\theta_*\), it is defined by the unique \(t\in(0,1)\) solving
\[
\alpha=\frac{2\sqrt{1+t^2}}{(1-t^2)D_\varepsilon(t)},\qquad
D_\varepsilon(t)=\frac{t^2}{\varepsilon+(\varepsilon+1)t^2}+\frac1{\varepsilon+t+\varepsilon t^2}.
\]
The cycle satisfies the sharp limiting laws
\[
\theta_*=\frac{\alpha-2\varepsilon}{2}+O_\varepsilon((\alpha-2\varepsilon)^2),\quad \alpha\downarrow2\varepsilon;
\qquad
\theta_*=\frac\pi4-\frac{\varepsilon+1/2}{\sqrt2\alpha}+O_\varepsilon(\alpha^{-2}),\quad\alpha\to\infty.
\]
Its period-return derivative is \(\mathcal M_{\alpha,\varepsilon}=(F'(\theta_*))^2\in[0,1)\) and
\[\mathcal M_{\alpha,\varepsilon}=1-\frac{2\sqrt2\varepsilon}{\alpha}+O_\varepsilon(\alpha^{-2})\qquad(\alpha\to\infty).\]
Only uniqueness among **symmetric** nonzero cycles is asserted; there is no classification of all periodic orbits or all basins above threshold.

## Proof
Write \(\tau=(-\sin\theta,\cos\theta)\). The intrinsic gradient is \(g=\sin\theta\,\tau=(-\sin^2\theta,\sin\theta\cos\theta)\). Its projected-preconditioned coefficient is
\[
w_\varepsilon(\theta)=\langle\tau,H^{-1}g\rangle=\sin\theta\left(\frac{\sin^2\theta}{\varepsilon+\sin^2\theta}+\frac{\cos^2\theta}{\varepsilon+|\sin\theta\cos\theta|}\right).
\]
The retraction rotates through \(-\arctan(\alpha w_\varepsilon(\theta))\), giving the *exact* map
\[F_{\alpha,\varepsilon}(\theta)=\theta-\arctan(\alpha w_\varepsilon(\theta)).\]
The coefficient is odd and strictly positive on \((0,\pi)\). For \(0<\theta<\pi/4\), put \(t=\tan\theta\); direct substitution yields \(w_\varepsilon(\theta)=tD_\varepsilon(t)/\sqrt{1+t^2}\). Set \(a=\varepsilon\), \(p=a+(a+1)t^2\), \(q=a+t+at^2\). Exact differentiation gives
\[
-D_\varepsilon'(t)p^2q^2=a^2(1-2t^2+4t^3-3t^4+4t^5)+2at^2(1-t+t^2+t^3)+t^4>0.
\]
Indeed the first polynomial equals \((1-t)(1+t-t^2)+3t^3(1-t)+4t^5>0\) for \(0<t<1\). The quantity \(\sqrt{1+t^2}/(1-t^2)\) increases strictly and \(D_\varepsilon(t)\) decreases strictly; therefore the defining function
\[A_\varepsilon(t)=\frac{2\sqrt{1+t^2}}{(1-t^2)D_\varepsilon(t)}\]
is strictly increasing, with limits \(2\varepsilon\) and \(+\infty\) at the two endpoints. The symmetric-cycle condition is exactly \(\arctan(\alpha w_\varepsilon(\theta))=2\theta\), equivalent to \(\alpha=A_\varepsilon(\tan\theta)\), so it has the stated unique solution if and only if \(\alpha>2\varepsilon\).

For the global convergence portion, if \(0<\theta<\pi/4\) and \(0<\alpha\le2\varepsilon<A_\varepsilon(\tan\theta)\), then \(\arctan(\alpha w_\varepsilon(\theta))<2\theta\). For \(\pi/4\le\theta<\pi\), it is automatically less than \(\pi/2\le2\theta\). Together with its strict positivity, this gives \(-\theta<F(\theta)<\theta\); odd symmetry handles negative angles. Hence \(|\theta_n|\) strictly decreases to zero, since any positive limiting magnitude would contradict continuity and the strict inequality.

Near the minimum, expansion from the positive and negative sides gives
\[w_\varepsilon(\theta)=\frac\theta\varepsilon-\frac{\theta|\theta|}{\varepsilon^2}+O_\varepsilon(|\theta|^3),\qquad F_{\alpha,\varepsilon}(\theta)=\left(1-\frac\alpha\varepsilon\right)\theta+\frac\alpha{\varepsilon^2}\theta|\theta|+O_{\alpha,\varepsilon}(|\theta|^3).\]
This proves the linear and quadratic local statements. At \(\alpha=2\varepsilon\), the sign eventually reverses for any nonterminating trajectory and the magnitudes obey \(r_{n+1}=r_n-(2/\varepsilon)r_n^2+O_\varepsilon(r_n^3)\). Subtracting reciprocals gives \(r_{n+1}^{-1}-r_n^{-1}=2/\varepsilon+O_\varepsilon(r_n)\); the Cesàro limit and \(r_n\to0\) yield \(nr_n\to\varepsilon/2\). Finite termination is separately allowed.

To prove local attraction, a second exact derivative identity is
\[
( D_\varepsilon(t)+t(1+t^2)D_\varepsilon'(t))p^2q^2
=a^3(1+t^2)^4+a^2t^2(2-t)(3t+1)(1+t^2)^2
+2at^4(2-t^2)(1+t^2)+t^6(1-t)>0.
\]
Since \(w_\varepsilon(\arctan t)=tD_\varepsilon(t)/\sqrt{1+t^2}\), this proves \(w_\varepsilon'(\theta)>0\) on \((0,\pi/4)\). At the symmetric cycle set \(s=\alpha w_\varepsilon'(\theta_*)\cos^2(2\theta_*)\). Then \(s>0\), while the strict increase of \(A_\varepsilon\) implies \(s<2\): differentiate \(\arctan(\alpha w_\varepsilon(\theta))-2\theta=0\) along \(\alpha=A_\varepsilon(\tan\theta)\); its partial derivative with respect to \(\alpha\) is positive, hence its fixed-\(\alpha\) derivative \(s-2\) is negative. Thus \(-1<F'(\theta_*)=1-s<1\). Oddness gives \(F'(-\theta_*)=F'(\theta_*)\), and the period-return derivative has modulus below one.

Finally, \(D_\varepsilon(t)=1/\varepsilon-t/\varepsilon^2+O_\varepsilon(t^2)\) gives \(A_\varepsilon(t)=2\varepsilon+2t+O_\varepsilon(t^2)\), proving linear onset. At \(t=1\), \(w_\varepsilon(\pi/4)=1/[\sqrt2(\varepsilon+1/2)]\) and \(w_\varepsilon'(\pi/4)=\varepsilon/[\sqrt2(\varepsilon+1/2)^2]\). Expanding \(\alpha w_\varepsilon(\theta_*)=\tan(2\theta_*)\) with \(\theta_*\uparrow\pi/4\) establishes the large-step amplitude. Substitution into \(s\), followed by \(\mathcal M=(1-s)^2\), gives the stated return multiplier asymptotics.

## Verification
Run the accompanying `verify_exact.py` with Python 3 and SymPy installed. It verifies the two polynomial derivative identities symbolically and supplements, but does not replace, the analytical proof with rational positivity evaluations and sampled orbit and multiplier checks. In particular, neither a finite sample nor a numerical nonlinear solve is used to prove global convergence or uniqueness.

## Relationship to prior work
Sakai and Iiduka (2024), arXiv:2409.00859v1, Algorithm 1 and Section 2.3, formulate precisely the projected, diagonal-preconditioned Riemannian RMSProp specialization used here. Their convergence analysis concerns step-size assumptions and general expected-gradient bounds; the exact normalization-retraction circle dynamics and sharp global/periodic transition are not stated there. Bock and Weiß (2022), arXiv:2210.02070, study Euclidean Adam two-cycles for scalar quadratics, with a different optimizer state and a different geometric map. Bensaid, Poëtte and Turpault (2024), arXiv:2407.15471v1, analyze convergence with adaptive line-search steps in Euclidean RMSProp and momentum, rather than the present fixed-step, memoryless embedded-manifold dynamics. Related nonconvergence phenomena do not imply the exact threshold, reciprocal-law coefficient, linear amplitude onset or return-map asymptotic established here.

## Limitations
The result is solely for a one-dimensional embedded manifold, deterministic gradients, \(\beta_2=0\), a fixed step, and the stated retraction and objective. The opposite stationary point is excluded from global minimizer convergence. Critical trajectories that reach the minimum in finitely many steps do not satisfy the nonterminating reciprocal-error asymptotic. Only a locally attracting symmetric two-cycle is classified above the threshold. This is not an independence certificate or a claim of publication priority; equivalent specialized results outside the inspected literature remain possible. Floating-point experiments establish no universal statements.

## References
1. Sakai and Iiduka, *A general framework of Riemannian adaptive optimization methods with a convergence analysis*, arXiv:2409.00859v1 (2024-09-01), https://arxiv.org/html/2409.00859v1.
2. Bock and Weiß, *Non-Convergence and Limit Cycles in the Adam optimizer*, arXiv:2210.02070 (2022), https://arxiv.org/abs/2210.02070.
3. Bensaid, Poëtte and Turpault, *Convergence of the Iterates for Momentum and RMSProp for Local Smooth Functions: Adaptation is the Key*, arXiv:2407.15471v1 (2024), https://arxiv.org/html/2407.15471v1.
