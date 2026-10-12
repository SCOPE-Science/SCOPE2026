# A re-entrant mean-square stability window for Markov-correlated gradient staleness

## Finding
Consider scalar delayed gradient descent on the strongly convex objective \(f(x)=x^2/2\), with the fixed normalized step \(h=6/5\):
\[
x_{t+1}=x_t-\frac65 x_{t-D_t}.
\]
The delay \(D_t\in\{0,1\}\) follows a stationary, symmetric two-state Markov chain, independent of the initial iterate, with \(\Pr(D_{t+1}=D_t\mid D_t)=p\), \(\Pr(D_{t+1}\ne D_t\mid D_t)=1-p\), and \(\Pr(D_0=0)=\Pr(D_0=1)=1/2\). For any deterministic \(x_{-1}=x_0\ne0\) and \(0<p<1\), let \(p_-<p_+\) denote the two roots in \((0,1)\) of
\[
432p^3-156p^2-305p+125=0.
\]
Then \(p_-=0.4267763163\ldots\), \(p_+=0.7912257350\ldots\), and the sharp classification is:

- If \(p_-<p<p_+\), the expected squared error \(\mathbb E[x_t^2]\) tends to zero geometrically.
- If \(p=p_-\) or \(p=p_+\), \(\liminf_{t\to\infty}\mathbb E[x_t^2]>0\).
- If \(0<p<p_-\) or \(p_+<p<1\), then for some \(c>0\) and \(\gamma>1\), \(\mathbb E[x_t^2]\ge c\gamma^t\) for all sufficiently large \(t\).

All delay chains have the identical one-time marginal \(\Pr(D_t=0)=\Pr(D_t=1)=1/2\). In particular, independent delays (\(p=1/2\)) are mean-square stable, while both sufficiently strong alternation and sufficiently strong persistence are unstable: changing only temporal dependence produces a bounded stability island.

## Assumptions and scope
The arithmetic is exact. The scalar quadratic curvature is one; \(h=6/5\) is the gradient step, not a time discretization of any particular service queue. A delay-zero update evaluates the current iterate, and a delay-one update evaluates exactly the preceding iterate. The delay sequence is exogenous, independent of the deterministic history, stationary, and first-order Markov. Its sole parameter is its probability \(p\) of retaining the previous delay state. No gradient-evaluation noise is added. The theorem is for \(0<p<1\); endpoints represent non-ergodic or periodic limiting delay laws and are not needed for the stated if-and-only-if result.

## Proof
**1. Exact update.** With \(y_t=(x_t,x_{t-1})^{\mathsf T}\), the two update matrices are
\[
A_0=\begin{pmatrix}-1/5&0\\1&0\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&-6/5\\1&0\end{pmatrix}.
\]
Every zero-delay event at time \(s\) resets the state to \(y_{s+1}=v x_s\), with \(v=(-1/5,1)^{\mathsf T}\). Write \(e_1=(1,0)^{\mathsf T}\) and \(r_L=e_1^{\mathsf T}A_1^L v\), for integer \(L\ge0\). The next zero-delay event follows after one step with probability \(p\), yielding the squared-amplitude factor \(r_0^2=1/25\). Otherwise there are exactly \(L\ge1\) successive one-delay steps before the next zero, with probability \((1-p)^2p^{L-1}\) and squared-amplitude factor \(r_L^2\).

**2. Positive renewal equation.** Define \(u_t=\mathbb E[x_t^2\mathbf1_{\{D_t=0\}}]\). Conditioning on the first zero-delay event and on the last preceding zero-delay event gives, for every integer \(t\ge0\),
\[
u_t=c_t+\sum_{g=1}^t b_g u_{t-g},\qquad
b_1=\frac p{25},\quad b_{L+1}=(1-p)^2p^{L-1}r_L^2\ (L\ge1),
\]
where \(c_0=x_0^2/2\) and, for \(t\ge1\),
\[
c_t=\frac{1-p}{2}p^{t-1}
\bigl(e_1^{\mathsf T}A_1^t(x_0,x_0)^{\mathsf T}\bigr)^2.
\]
All coefficients are nonnegative, \(c_0>0\), and \(b_1>0\). Put \(B(z)=\sum_{g\ge1}b_gz^g\) and \(C(z)=\sum_{t\ge0}c_tz^t\), so the formal generating function of \(u_t\) is \(U(z)=C(z)/(1-B(z))\).

**3. Exact mass of the renewal kernel.** For a symmetric moment vector \(m=(a^2,ab,b^2)^{\mathsf T}\), the one-delay map is
\[
K_1=\begin{pmatrix}1&-12/5&36/25\\1&-6/5&0\\1&0&0\end{pmatrix}.
\]
Let \(m_0=(1/25,-1/5,1)^{\mathsf T}\) and let \(e_1^{(3)}=(1,0,0)^{\mathsf T}\) act on this moment space. For \(0\le p<5/6\),
\[
\sum_{L\ge1}p^{L-1}r_L^2
=\bigl(e_1^{(3)}\bigr)^{\mathsf T}K_1(I-pK_1)^{-1}m_0
=-\frac{216p^2+5430p+6125}{25(6p-5)(36p^2+35p+25)}.
\]
This power series has nonnegative coefficients and a non-removable pole at \(p=5/6\); hence its sum diverges for \(p\ge5/6\). For \(0<p<5/6\), substitution gives
\[
1-B(1)=\frac{24(432p^3-156p^2-305p+125)}{25(6p-5)(36p^2+35p+25)}.
\]
The denominator is strictly negative on this interval. The cubic has exactly two roots in \((0,5/6)\): its derivative has a unique positive zero, it is positive at \(p=2/5\), negative at \(p=1/2\) and \(p=3/4\), and positive at \(p=4/5\). Thus \(B(1)<1\) precisely for \(p_-<p<p_+\), \(B(1)=1\) at the roots, and \(B(1)>1\) elsewhere below \(5/6\).

**4. Stability and growth.** When \(B(1)<1\), both \(B\) and \(C\) have finite exponential moments: the one-delay matrix has eigenvalues of modulus \(\sqrt{6/5}\), and \(p<5/6\). Some \(z>1\) therefore satisfies \(B(z)<1\) and \(C(z)<\infty\). Since \(U(z)<\infty\) has nonnegative coefficients, \(u_t=O(z^{-t})\). Conditioning on the last zero-delay event yields the exact identity for \(t\ge1\):
\[
\begin{split}
\mathbb E[x_t^2]={}&\frac12p^{t-1}
\bigl(e_1^{\mathsf T}A_1^t(x_0,x_0)^{\mathsf T}\bigr)^2
+\frac1{25}u_{t-1}\\
&+\sum_{L=1}^{t-1}(1-p)p^{L-1}r_L^2u_{t-L-1}.
\end{split}
\]
The last-zero convolution has an exponential moment near \(z=1\). It follows that \(\mathbb E[x_t^2]\) decays geometrically.

If \(B(1)>1\), or if \(B(1)=\infty\), positivity and continuity imply a unique \(\zeta\in(0,1)\) such that \(B(\zeta)=1\). For the infinite-mass case, \(\zeta<5/(6p)\), the convergence radius of the kernel. The transformed coefficients \(b_g\zeta^g\) form an aperiodic probability distribution with finite positive mean \(\zeta B'(\zeta)\), and the transformed forcing \(c_t\zeta^t\) is summable. The elementary discrete renewal theorem therefore gives
\[
\lim_{t\to\infty}\zeta^tu_t
=\frac{C(\zeta)}{\zeta B'(\zeta)}>0.
\]
Consequently \(\mathbb E[x_t^2]\ge u_t\) grows exponentially. At \(B(1)=1\), the same renewal theorem with \(\zeta=1\) gives \(u_t\to C(1)/B'(1)>0\), and hence a positive lower limit for the expected squared error. All claimed regimes follow.

## Verification
The accompanying `verify.py` recomputes the rational moment-map determinant, the one-delay resolvent, the polynomial \(B(1)\), sign brackets locating both roots, and the exact Lyapunov identity at \(p=1/2\). For independent delays the certificate is
\[
Q=\begin{pmatrix}100/3&-25/2\\-25/2&25\end{pmatrix}\succ0,
\quad Q-\tfrac12(A_0^{\mathsf T}QA_0+A_1^{\mathsf T}QA_1)=I.
\]
The script also checks 28 exact weighted-path moment identities, 24 instances of the zero-event renewal recurrence, and 21 of the last-zero decomposition. For example, the exact renewal masses are \(B(1)=236/175>1\) at \(p=1/4\), \(B(1)=91/103<1\) at \(p=1/2\), and \(B(1)=54557/47525>1\) at \(p=4/5\). Run `python verify.py` with SymPy installed as specified in `requirements.txt`. The general statements are proved analytically; finite enumeration and computation are consistency checks only.

## Relationship to prior work
Dutta, Joshi, Ghosh, Dube, and Nagpurkar (2018) analyze asynchronous SGD under stochastic staleness, including non-independent staleness, and give sufficient convergence bounds and delay compensation. Their Theorem 3 and supplemental proof do not assert an exact phase diagram for a stationary two-state Markov delay process at a fixed overrelaxed step. Arjevani, Shamir, and Srebro (2020; public preprint 2018) analyze sharp rates for fixed, not Markov-switched, delay on quadratic functions, using generating functions. Their model does not imply the dependence-induced re-entrant stability interval above. General Markov jump linear-system moment criteria explain why moment operators can be used; the exact cubic and the renewal-based sharp transition for this stale-gradient update are the specific contribution here. These comparisons are limited to inspected sources; absence of another publication from searches does not establish exhaustive priority.

## Limitations
The result is not a theorem about a physical asynchronous-worker queue: the two-state Markov delays are assumed exogenous. It uses a particular overrelaxed scalar step and strongly convex quadratic objective; it neither proves that correlation is always harmful nor extends automatically to nonlinear, noisy, high-dimensional, or delay-adaptive methods. It is a mean-square statement, not an almost-sure convergence classification. The spectral or renewal mechanism alone does not establish a universal stability theorem for arbitrary delay distributions. Independent assessment and exhaustive priority verification are not claimed.

## References
1. S. Dutta, G. Joshi, S. Ghosh, P. Dube and P. Nagpurkar, *Slow and Stale Gradients Can Win the Race: Error-Runtime Trade-offs in Distributed SGD*, AISTATS/PMLR 84 (2018), 803–812, https://proceedings.mlr.press/v84/dutta18a.html ; earliest public preprint arXiv:1803.01113 (2018-03-03).
2. Y. Arjevani, O. Shamir and N. Srebro, *A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates*, PMLR 117 (2020), 111–132, https://proceedings.mlr.press/v117/arjevani20a.html ; arXiv:1806.10188 (2018-06-26).
3. I. Mitliagkas, C. Zhang, S. Hadjis and C. Ré, *Asynchrony Begets Momentum, with an Application to Deep Learning*, arXiv:1605.09774 (2016). Different geometric/queuing-derived asynchrony model.
