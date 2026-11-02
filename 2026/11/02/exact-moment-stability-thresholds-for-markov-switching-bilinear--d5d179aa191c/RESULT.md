# Exact moment-stability thresholds for Markov-switching bilinear Controlled-Minimax

## Finding

A fixed-feedback discretization may contract along almost every trajectory while amplifying its mean square and every sufficiently high positive moment. For the two-state sign-switching bilinear games specified below, the almost-sure stability boundary and every positive-moment boundary admit explicit necessary-and-sufficient formulas. In particular, anti-persistent sign switching restores mean-square stability precisely after a strictly greater than one-half flip-probability threshold; independent signs never do so.

Put \(d=\lambda-1>0\), \(x=\eta c>0\), \(u=x\beta\), and \(v=x^2(\beta^2+d^2)\), and define
\[
 m_\pm=(1\pm u)^2+x^2d^2=1+v\pm2u,\qquad
 \Delta=m_+m_-=(1+v)^2-4u^2.
\]
For every nonzero deterministic initial state, the almost-sure exponential norm rate is
\[
 \lim_{n\to\infty}\frac1n\log\frac{\|z_n\|}{\|z_0\|}
 =\frac14\log\Delta\quad\text{almost surely}.
\]
Consequently, almost-sure exponential stability holds exactly when
\[
 \beta^2>d^2,\qquad 0<x<\frac{\sqrt{2(\beta^2-d^2)}}{\beta^2+d^2}.
\]
Assume these inequalities, and label the two strictly positive factors \(a=\min(m_+,m_-)\) and \(b=\max(m_+,m_-)\). Then \(0<a<1<b\) and \(ab<1\). For every real moment order \(q>0\), set \(A=a^{q/2}\), \(B=b^{q/2}\), and
\[
 p_q=\frac{(1-A)(B-1)}{A+B-2AB}\in(0,1).
\]
When the sign process changes sign with conditional probability \(p\in(0,1)\), the \(q\)-th absolute moment \(\mathbb E\|z_n\|^q\) decays exponentially if \(p>p_q\), tends to a finite strictly positive limit if \(p=p_q\), and grows exponentially if \(0<p<p_q\). At deterministic alternation \(p=1\), every positive moment decays exponentially. The curve \(q\mapsto p_q\) increases strictly and continuously from \(0\) to \(1\). Thus for every \(p\in(0,1)\), a unique finite critical moment order \(q_c(p)\) separates decaying and growing moments (with a nonzero limit at equality).

For \(q=2\), the critical flip probability is
\[
 p_2=\frac{4u^2-v^2}{2(4u^2-v-v^2)}>\frac12.
\]
Under independent equiprobable signs (\(p=1/2\)), the exact mean-square growth factor is \(1+v>1\), even in the almost-sure stable region. The exact rational instance \(\lambda=2\), \(\beta=-2\), \(x=1/5\) has \(a=2/5\), \(b=2\), \(\Delta=4/5\), \(p_2=3/4\), and \(p_4=7/8\). At \(p=4/5\), its second moment decays but fourth moment grows while every nonzero trajectory contracts almost surely.

## Assumptions and scope

For each integer \(k\ge0\), let the time-dependent real payoff be \(\mathcal L_k(\theta,\phi)=c\xi_k\theta\phi\), with \(c>0\). These games share the saddle state \((0,0)\). The stationary Markov sign process \((\xi_k)_{k\ge0}\) takes values \(\pm1\), starts uniformly on these two states, and has transition law
\[
 \mathbb P(\xi_{k+1}=-\xi_k\mid\xi_k)=p\in(0,1].
\]
The initial parameter vector \(z_0=(\theta_0,\phi_0)^\mathsf T\ne0\) is deterministic and independent of the sign process. Choose fixed \(\lambda_\theta=\lambda_\phi=\lambda>1\), arbitrary \(\beta\in\mathbb R\), stepsize \(\eta>0\), and unit scalar actuator gain. Apply at each step the discrete feedback-gradient update, not the continuous second-order controlled dynamics:
\[
 \begin{aligned}
 g_\theta&=\partial_\theta\mathcal L_k=c\xi_k\phi_k,&
 g_\phi&=\partial_\phi\mathcal L_k=c\xi_k\theta_k,\\
 \theta_{k+1}&=\theta_k-\eta g_\theta+\eta(\lambda g_\theta+\beta g_\phi),&
 \phi_{k+1}&=\phi_k+\eta g_\phi+\eta(\beta g_\theta-\lambda g_\phi).
 \end{aligned}
\]
All statements refer to the Euclidean norm, exact arithmetic, constant gains, and stationary sign initialization. There is no claim about nonlinear games, changing controllers, additive noise, or the separate second-order ODE model.

## Proof

**1. Exact conformal factors.** Write \(J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\). Direct substitution gives
\[
 z_{k+1}=M_{\xi_k}z_k,\qquad
 M_\xi=(1+\xi u)I+\xi xdJ.
\]
Since \(J^\mathsf T=-J\) and \(J^\mathsf TJ=I\),
\[
 M_\xi^\mathsf TM_\xi=m_\xi I,\qquad
 \|z_n\|^2=\|z_0\|^2\prod_{k=0}^{n-1}m_{\xi_k}.
\]
Each factor is positive because \(xd>0\). Thus no iterate reaches zero from a nonzero start.

**2. Almost-sure boundary.** For \(0<p<1\), the symmetric sign chain is irreducible and aperiodic; at \(p=1\) it alternates periodically with exactly half of each sign asymptotically. In either case both occupation frequencies tend to \(1/2\) almost surely. Taking logarithms of the exact product gives the asserted exponent \(\frac14\log(m_+m_-)\). The product condition \(\Delta<1\) reduces, without division by a possibly signed quantity, to
\[
 x^2\left[x^2(\beta^2+d^2)^2-2(\beta^2-d^2)\right]<0.
\]
Because \(x>0\), this is equivalent to the two stated strict conditions. When \(\Delta\ge1\), Jensen's inequality applied to the logarithm of the product with the stationary law yields \(\mathbb E\|z_n\|^q\ge \|z_0\|^q\Delta^{qn/4}\) for all \(n\) and \(q>0\); therefore no positive moment tends to zero. These observations also establish that in the stable case the two factors straddle one, because \(m_++m_-=2(1+v)>2\) while their product is below one.

**3. Transfer identity.** In the stable case, relabel sign states so the squared norm factors are \(a,b\). Put
\[
 D_q=\operatorname{diag}(A,B),\qquad
 P_p=\begin{pmatrix}1-p&p\\p&1-p\end{pmatrix},\qquad
 T_q=P_pD_q.
\]
By summing probabilities of finite Markov paths, for all integers \(n\ge1\),
\[
 \frac{\mathbb E\|z_n\|^q}{\|z_0\|^q}
 =\left(\frac12,\frac12\right)D_qT_q^{n-1}
 \begin{pmatrix}1\\1\end{pmatrix}.
\]
For \(0<p<1\), \(T_q\) is strictly positive. Perron--Frobenius theory therefore yields a strictly positive leading coefficient and an exponentially smaller remainder, with growth factor
\[
 \rho_q=\frac{(1-p)(A+B)+\sqrt{(1-p)^2(A-B)^2+4p^2AB}}{2}.
\]
The exponent is \(\log\rho_q\). In particular, when \(\rho_q=1\), the expected moment converges to a finite nonzero limit, and when \(\rho_q\ne1\) its exponential growth or decay is strict. For \(p=1\), an exact two-step product has factor \(AB=(ab)^{q/2}<1\), giving decay at all positive orders, even though the chain is periodic.

**4. Unique flip threshold.** The positive matrix \(T_q\) is similar to the symmetric matrix \(D_q^{1/2}P_pD_q^{1/2}\), whose derivative in \(p\) is the negative semidefinite rank-one matrix
\[
 -\begin{pmatrix}\sqrt A\\-\sqrt B\end{pmatrix}
 \begin{pmatrix}\sqrt A&-\sqrt B\end{pmatrix}.
\]
Its largest eigenvalue is continuous and strictly decreasing for \(p\in(0,1)\): by the derivative formula for the simple Perron eigenvalue, a zero derivative would force a positive leading eigenvector proportional to \((\sqrt B,\sqrt A)^{\mathsf T}\). The symmetric transfer matrix maps that vector to \((A\sqrt B,B\sqrt A)^{\mathsf T}\), which cannot be proportional to it since \(A\ne B\). Thus the eigenvalue derivative is always strictly negative. At \(p=0\), the Perron value is \(B>1\); at \(p=1\), it is \(\sqrt{AB}<1\). Hence exactly one crossing occurs. Solving
\[
 \det(I-T_q)=(1-A)(1-B)+p(A+B-2AB)=0
\]
gives \(p=p_q\). Its denominator is strictly positive because
\[
 A+B-2AB=(1-A)(B-1)+(1-AB)>0.
\]
This proves the stated trichotomy, including the boundary.

**5. Strict ordering across moment orders.** Write \(a=e^{-s}\), \(b=e^t\), where \(s>t>0\) follows from \(ab<1\), and put \(h=q/2\). Elementary rearrangement gives
\[
 \frac{p_q}{1-p_q}=
 \frac{2\sinh(sh/2)\sinh(th/2)}{\sinh((s-t)h/2)}.
\]
The logarithmic derivative of its right side is positive: the function \(y\mapsto y\coth y\) is strictly increasing for \(y>0\), so
\[
 s\coth(sh/2)-(s-t)\coth((s-t)h/2)>0,
\]
while the remaining \(t\coth(th/2)\) is positive. Moreover, the ratio tends to zero linearly as \(h\downarrow0\) and to infinity exponentially as \(h\to\infty\). Thus \(p_q\) increases strictly and continuously from zero to one. For each \(p\in(0,1)\), it crosses \(p\) at one finite \(q_c(p)\), completing the full moment hierarchy.

**6. Mean-square formula and witness.** Substitute \(q=2\), \(A=a\), \(B=b\), and \(m_\pm=1+v\pm2u\) into \(p_q\); simplification yields \(p_2=(4u^2-v^2)/[2(4u^2-v-v^2)]\). Its comparison with \(1/2\) follows from \(2(4u^2-v^2)-2(4u^2-v-v^2)=2v>0\). When \(p=1/2\), the signs are independent and the finite-time second moment is exactly \(\|z_0\|^2(1+v)^n\). Finally, the rational example has squared factors \(2/5\) and \(2\), so \(p_2=3/4\) and, using \(A=(2/5)^2\), \(B=2^2\), \(p_4=7/8\); the choice \(p=4/5\) lies strictly between these critical probabilities.

## Verification

The standalone `verify_switching.py` checks 711 symbolic, rational, exact finite-path, and floating-point identities, including direct multiplication of both matrices, Markov transfer identities against exhaustive sign-path enumerations through eight steps, critical thresholds, and the stated strict second/fourth moment separation. Run it with Python 3, NumPy, and SymPy using `python verify_switching.py`. These checks corroborate the derivations; the infinite-time and every-real-order assertions follow from the proof, not from finite tests.

## Relationship to prior work

Luo, Chen and Zhu introduce the Controlled-Minimax feedback and a discrete algorithm, and study continuous-time stabilization and empirical adversarial examples [1]. Their inspected analysis does not give these Markov-switching bilinear moment thresholds. Classical Markov jump linear systems already admit general necessary-and-sufficient spectral conditions for mean-square stability, including the condition in Ling and Deng [2]. The transfer operator in the proof is a scalar specialization of that established framework: the claim is not that the spectral approach or the qualitative almost-sure versus moment distinction is new. Tai [3] independently develops general covariance criteria for noisy Markov-switching affine recurrences, which reinforces that distinction but does not provide the explicit all-order phase diagram for this fixed-feedback zero-innovation bilinear update. The contribution here is the exact parameter domain, all-positive-orders thresholds, strict anti-persistence necessity, and simultaneously stable-second/unstable-fourth-moment witness for this particular controlled game.

## Limitations

This is a complete theorem only for the stated symmetric two-state Markov signs and conformal two-dimensional bilinear updates. It does not transfer unchanged to nonstationary initial signs, unequal gain channels, general nonsymmetric transition laws, additive noise, nonlinear games, complex spectra, or the continuous-time second-order controller. The near-certain trajectory convergence is not a claim of convergence of any fixed positive moment. The moment stability regions are for the unforced homogeneous recursion, not finite stationary covariances of an additively forced system. Historical priority for a possibly equivalent special case remains to be independently assessed.

## References

[1] Tianjiao Luo, Jianfei Chen, and Jun Zhu, *Controlled-Minimax: Stabilizing Adversarial Optimization via Control Theory*, arXiv:2610.12915 (first public 2026-10-09), https://arxiv.org/abs/2610.12915.

[2] Qiang Ling and Haojiang Deng, *A New Proof to the Necessity of a Second Moment Stability Condition of Discrete-Time Markov Jump Linear Systems with Real States*, Journal of Applied Mathematics (2012), article 642480, https://doi.org/10.1155/2012/642480.

[3] Wilson Tai, *Spectral Characterisation of Covariance Existence in Markov-Switching Affine Recurrences*, arXiv:2607.09994 (first public 2026-07-10), https://arxiv.org/abs/2607.09994.
