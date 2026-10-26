# A hidden rare-return tail at the weak-monitoring resonance of a two-site quantum walk

## Finding

Consider repeated, imperfect attempts to detect a particle at its initially occupied site in a two-site quantum walk. When the site-to-site rotation angle shrinks at the same rate as the click strength, the first-click time has a nontrivial continuous family of limiting distributions. Within that family there is an exceptional-point transition and an unexpected loss of uniform integrability at its resonant endpoint.

More precisely, write the click strength as \(0<\varepsilon<1\), the rotation angle as \(\phi_\varepsilon=\varepsilon\kappa_\varepsilon\), and the first detected step as \(N_\varepsilon\). Suppose \(\kappa_\varepsilon\to\kappa\in[0,\infty)\). Then \(\varepsilon N_\varepsilon\) converges in distribution to a nonnegative random variable \(Z_\kappa\) with survival function
\[
\Pr(Z_\kappa>t)=\left\|e^{tG_\kappa}e_0\right\|^2,\qquad
G_\kappa=\begin{pmatrix}-1/2&-i\kappa\\-i\kappa&0\end{pmatrix},\quad t\ge0.
\]
Here \(e_0=(1,0)^{\mathsf T}\). In terms of \(d_\kappa=\sqrt{1-16\kappa^2}\), the same survival probability is
\[
 e^{-t/2}\left(
 \left|\cosh(d_\kappa t/4)-\frac{\sinh(d_\kappa t/4)}{d_\kappa}\right|^2
 +\frac{16\kappa^2}{|d_\kappa|^2}|\sinh(d_\kappa t/4)|^2
 \right),
\]
with continuous interpretation at \(d_\kappa=0\). The two eigenvalues of \(G_\kappa\) meet at \(\kappa=1/4\), where the survival becomes \(e^{-t/2}[(1-t/4)^2+(t/4)^2]\).

For fixed \(\kappa>0\), all polynomial moments converge under this scaling. In particular,
\[
 \lim_{\varepsilon\to0}\varepsilon\,\mathbb E N_\varepsilon=2,
 \qquad
 \lim_{\varepsilon\to0}\operatorname{Var}(\varepsilon N_\varepsilon)
 =4+\frac{1}{2\kappa^2}.
\]
At \(\kappa=0\), the weak limit is instead exponential of rate one, with mean and variance one. Remarkably, if every \(\kappa_\varepsilon>0\), even if \(\kappa_\varepsilon\to0\) arbitrarily fast, the **exact** discrete mean is \(\varepsilon\mathbb E N_\varepsilon=2\), not one. More precisely, for each \(u>0\),
\[
 \lim_{\varepsilon\to0}
 \frac{\Pr\!\left(N_\varepsilon>
 \left\lfloor u/(\varepsilon\kappa_\varepsilon^2)\right\rfloor\right)}{4\kappa_\varepsilon^2}
 =e^{-4u},
 \qquad
 \operatorname{Var}(\varepsilon N_\varepsilon)
 \sim\frac{1}{2\kappa_\varepsilon^2}.
\]
Thus a fraction asymptotic to \(4\kappa_\varepsilon^2\) of the probability escapes to the much longer timescale \((\varepsilon\kappa_\varepsilon^2)^{-1}\), carrying the missing unit of mean. At the exactly resonant angle \(\phi_\varepsilon=0\) there is no such tail and \(\varepsilon\mathbb E N_\varepsilon=1\).

## Assumptions and scope

The Hilbert space is \(\mathbb C^2\) with orthonormal site vectors \(e_0,e_1\). Each discrete step first applies the unitary \(U_\varepsilon=\exp(-i\phi_\varepsilon\sigma_x)\), then performs the binary measurement with click Kraus operator \(D_\varepsilon=\sqrt\varepsilon\,|e_0\rangle\langle e_0|\) and no-click Kraus operator \(B_\varepsilon=\operatorname{diag}(\sqrt{1-\varepsilon},1)\). The initial state is \(e_0\); a click terminates the experiment. Its first occurrence defines \(N_\varepsilon\in\{1,2,\ldots\}\). The no-click propagator is
\[
 K_\varepsilon=B_\varepsilon U_\varepsilon,
 \qquad\Pr(N_\varepsilon>n)=\|K_\varepsilon^ne_0\|^2
 \quad(n\ge0).
\]
All limits are along \(\varepsilon\downarrow0\). The finite-angle exact-mean assertion assumes \(\phi_\varepsilon\notin\pi\mathbb Z\); the rare-return statements assume \(\kappa_\varepsilon>0\), \(\kappa_\varepsilon\to0\), and \(\phi_\varepsilon=\varepsilon\kappa_\varepsilon\). No uniform statement for large or unbounded \(\kappa_\varepsilon\) is asserted.

## Proof

**1. Finite-time weak limit.** With \(\kappa_\varepsilon\to\kappa<\infty\), the elementary expansions \(\sqrt{1-\varepsilon}=1-\varepsilon/2+O(\varepsilon^2)\) and \(U_\varepsilon=I-i\varepsilon\kappa_\varepsilon\sigma_x+O(\varepsilon^2\kappa_\varepsilon^2)\) give
\[
 K_\varepsilon=I+\varepsilon G_\kappa+o(\varepsilon).
\]
Finite-dimensional Euler product convergence proves \(K_\varepsilon^{\lfloor t/\varepsilon\rfloor}\to e^{tG_\kappa}\) uniformly on compact \(t\)-intervals. Taking squared norms proves weak convergence through the survival functions. Since \(G_\kappa=-I/4+A_\kappa\) and \(A_\kappa^2=(1-16\kappa^2)I/16\), exponentiating the \(2\times2\) matrix yields the displayed hyperbolic formula, including its removable critical singularity.

**2. Moment identities for positive limiting coupling.** For \(\kappa>0\), the two eigenvalues \(\lambda_\pm=(-1\pm\sqrt{1-16\kappa^2})/4\) have strictly negative real parts, including at their defective meeting point \(\kappa=1/4\). Thus the solution \(W>0\) of \(G_\kappa^*W+WG_\kappa=-I\) exists. The expansion of \(K_\varepsilon^*WK_\varepsilon-W\) gives, for sufficiently small \(\varepsilon\), a uniform geometric bound \(\|K_\varepsilon^n\|\le C e^{-c\varepsilon n}\) at this fixed \(\kappa\). Hence all polynomial moments of \(\varepsilon N_\varepsilon\) are uniformly integrable and converge.

For the continuous survival, write \(\rho(t)=e^{tG_\kappa}|e_0\rangle\langle e_0|e^{tG_\kappa^*}\), \(x=\rho_{00}\), \(y=\rho_{11}\), and \(c=\operatorname{Im}\rho_{01}\). Direct matrix multiplication yields
\[
 x'=-x-2\kappa c,\qquad
 y'=2\kappa c,\qquad
 c'=\kappa(x-y)-\tfrac12c,
\]
with \((x,y,c)(0)=(1,0,0)\) and decay at infinity. Integrate first without a time weight and then after multiplying by \(t\). Integration by parts gives
\[
 \int_0^\infty(x,y,c)\,dt=(1,1,0),\qquad
 \int_0^\infty t(x,y,c)\,dt
 =\left(2,2+\frac1{4\kappa^2},-\frac1{2\kappa}\right).
\]
As \(\Pr(Z_\kappa>t)=x(t)+y(t)\), the survival integral formulas for the first and second moments yield \(\mathbb EZ_\kappa=2\) and \(\mathbb EZ_\kappa^2=8+1/(2\kappa^2)\), hence the asserted variance. At \(\kappa=0\), \(e^{tG_0}e_0=e^{-t/2}e_0\), so the limiting law is exponential of rate one.

**3. Exact discrete mean away from resonance.** Put \(P=|e_0\rangle\langle e_0|\) and \(X=\sum_{n\ge0}K_\varepsilon^nP(K_\varepsilon^*)^n\). For \(\phi_\varepsilon\notin\pi\mathbb Z\), no nonzero unitary invariant vector can remain in the no-click subspace: the only such vector would have to be \(e_1\), which the nontrivial rotation does not preserve. Hence the spectral radius of \(K_\varepsilon\) is strictly below one, and the sum converges to the unique solution of \(X=P+K_\varepsilon X K_\varepsilon^*\). But \(K_\varepsilon K_\varepsilon^*=I-\varepsilon P\), so \(X=I/\varepsilon\) solves this equation. Therefore
\[
 \mathbb EN_\varepsilon=\sum_{n\ge0}\|K_\varepsilon^ne_0\|^2
 =\langle e_0,\sum_{n\ge0}(K_\varepsilon^*)^nK_\varepsilon^ne_0\rangle
 =\operatorname{Tr}(X)=2/\varepsilon.
\]
The last equality follows by taking the trace of the positive Gramian, term by term. If \(\phi_\varepsilon=0\), the state stays at \(e_0\), the click time is geometric with parameter \(\varepsilon\), and its mean is \(1/\varepsilon\).

**4. Resonant rare tail and diverging variance.** Assume now \(\kappa_\varepsilon>0\to0\). Write \(q=\sqrt{1-\varepsilon}\), \(\phi=\varepsilon\kappa_\varepsilon\). The two eigenvalues of \(K_\varepsilon\) satisfy
\[
 \lambda^2-(1+q)\cos\phi\,\lambda+q=0.
\]
They are distinct and real for all sufficiently small \(\varepsilon\). Label them slow and fast by proximity to one and \(q\), respectively. An expansion of this quadratic with uniform remainder for \(\varepsilon\to0\) and \(\kappa_\varepsilon\to0\) gives
\[
 1-\lambda_{\rm slow}=2\varepsilon\kappa_\varepsilon^2(1+o(1)),
 \qquad
 1-\lambda_{\rm fast}=\frac\varepsilon2(1+o(1)).
\]
Use the exact spectral projections on the initial vector,
\[
 v_{\rm slow}=\frac{K_\varepsilon-\lambda_{\rm fast}I}
 {\lambda_{\rm slow}-\lambda_{\rm fast}}e_0,
 \qquad v_{\rm fast}=e_0-v_{\rm slow}.
\]
Their entries imply \(\|v_{\rm slow}\|^2=4\kappa_\varepsilon^2(1+o(1))\), \(\|v_{\rm fast}\|=O(1)\); in fact the slow vector has component \(-2i\kappa_\varepsilon(1+o(1))\) on \(e_1\) and a component \(O(\kappa_\varepsilon^2)\) on \(e_0\). Since
\[
 K_\varepsilon^ne_0=\lambda_{\rm slow}^nv_{\rm slow}
 +\lambda_{\rm fast}^nv_{\rm fast},
\]
the fast term is negligible, even relative to \(\kappa_\varepsilon\), when \(n=\lfloor u/(\varepsilon\kappa_\varepsilon^2)\rfloor\), and the slow squared amplitude tends to \(4\kappa_\varepsilon^2e^{-4u}\), proving the tail assertion.

For the variance, use the exact tail-sum identity \(\mathbb EN_\varepsilon^2=\sum_{n\ge0}(2n+1)\|K_\varepsilon^ne_0\|^2\). In the spectral expansion, the slow squared term contributes
\[
 \varepsilon^2\|v_{\rm slow}\|^2
 \frac{1+|\lambda_{\rm slow}|^2}{(1-|\lambda_{\rm slow}|^2)^2}
 \sim\frac{1}{2\kappa_\varepsilon^2}.
\]
The fast squared contribution is \(O(1)\) and the cross contribution is \(O(\kappa_\varepsilon)\), after multiplying by \(\varepsilon^2\): the denominator of each fast or cross geometric derivative is of order \(\varepsilon^2\). The \(+1\) tail-sum terms are lower order. Subtracting \((\varepsilon\mathbb EN_\varepsilon)^2=4\) proves the claimed variance equivalence. All estimates are joint, requiring no prescribed rate of \(\kappa_\varepsilon\to0\).

## Verification

The standalone `verify.py` reconstructs the integrated density and time-weighted moment identities symbolically, compares the closed survival formula with direct matrix exponentials, checks the finite-step mean by a discrete Lyapunov solve, and tests the resonant spectral-projection/tail expansions numerically. Execute `python verify.py` with NumPy, SciPy and SymPy installed. The script is a finite check; the all-parameter statements follow from the analytic argument above. The critical roots, the zero-coupling endpoint and the nonuniform integrability are treated explicitly in the proof.

## Relationship to prior work

Heine, Barkai, Ziegler and Tornow, *Quantum Walks: First Hitting Times with Weak Measurements* (2025; arXiv:2506.21168), formulate the same weak-probe two-level detection protocol and derive exact mean return times, including the discontinuity at exact resonance. That exact mean is prior knowledge, not the present contribution. Ziegler, Heine and Tornow, *Monitoring of quantum walks with weak measurements* (2026; arXiv:2603.26933), provide exact finite-strength spectral representations for return-time moments and describe sharp variance peaks near resonance. Their general finite-parameter formulas are prior knowledge. The present theorem isolates a simultaneous small-probe/small-rotation limit, its exceptional-point family of full probability laws, and a quantitatively normalized rare-return tail explaining the nonuniform moment limit. These asymptotic conclusions were not identified as stated results in the inspected papers. Yin, Ziegler, Thiel and Barkai (2019; arXiv:1903.03394) analyze large first-return fluctuations under projective rather than weak monitoring. Exact finite-strength formulas may provide an alternative route to the limit and remain a potential implication risk.

## Limitations

The construction is a two-site, initially detected quantum walk with real rotation angle and a single rank-one weak detector. A continuous weak-probe scaling and a separate doubly resonant scaling are established; no uniform law for unbounded rotation-to-click ratio is claimed. The limiting distributions do not mean that finite-angle resonant first-return probabilities are identical. The result does not provide a multidimensional classification or quantum-trajectory fluctuation theorem for other detectors. Published general spectral expressions may subsume these formulas after additional, currently unverified singular asymptotic analysis; literature-wide priority and independent audit are not established.

## References

1. T. Heine, E. Barkai, K. Ziegler and S. Tornow, *Quantum Walks: First Hitting Times with Weak Measurements*, arXiv:2506.21168 (first public version 2025-06-26), https://arxiv.org/abs/2506.21168.
2. K. Ziegler, T. Heine and S. Tornow, *Monitoring of quantum walks with weak measurements*, arXiv:2603.26933 (first public version 2026-03-27), https://arxiv.org/abs/2603.26933.
3. R. Yin, K. Ziegler, F. Thiel and E. Barkai, *Large fluctuations of the first detected quantum return time*, arXiv:1903.03394 (2019), https://arxiv.org/abs/1903.03394.
4. M. Kewming and collaborators, *First Passage Times for Continuous Quantum Measurement Currents*, arXiv:2308.07810 (2023), https://arxiv.org/abs/2308.07810.
