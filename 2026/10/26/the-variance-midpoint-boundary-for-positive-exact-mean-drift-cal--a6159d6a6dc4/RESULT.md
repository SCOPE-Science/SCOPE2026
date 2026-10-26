# The variance-midpoint boundary for positive exact-mean drift calibration on a three-site stochastic chain

## Finding
For any step size \(h>0\), rates \(p,q>0\), and nonnegative noise half-variances \(c_1,c_2,c_3\), consider the Gaussian-noise-first positive exponential step
\[
X^+=\exp(\operatorname{diag}(\Delta Z))\exp(h(K-C))X,\quad C=\operatorname{diag}(c_1,c_2,c_3),\quad \mathbb E\Delta Z_i=0,\quad \mathbb E(\Delta Z_i^2)=2c_ih,
\]
where the Gaussian increments may be correlated. The desired mean drift is the three-site feedforward chain
\[
M=\begin{pmatrix}0&p&0\\0&0&q\\0&0&0\end{pmatrix}.
\]
There exists a real Metzler drift \(K\) (off-diagonal entries nonnegative) making the one-step conditional mean **exactly** \(\mathbb E[X^+\mid X]=e^{hM}X\) for every nonnegative input \(X\) if and only if
\[
\boxed{\ 2c_2\ge c_1+c_3\ }.
\]
When it exists, \(K\) is unique, its diagonal is zero, its two nearest-neighbor couplings are strictly positive, and its long-range coupling has sign \(\operatorname{sgn}(2c_2-c_1-c_3)\). In particular the equality case has no direct long-range coupling. This classification holds for **every** \(h>0\) and all \(p,q>0\). When the inequality fails, no Metzler drift—allowing any diagonal and any extra edges—can give exact grid-point first moments through this noise-first splitting. The two-site counterpart, with arbitrary upper-triangular Metzler desired drift and any diagonal Gaussian noise variances, always admits a unique Metzler exact-mean correction. Thus three sites are dimension-minimal for this obstruction within acyclic feedforward systems.

For \(c_1=c_3=1,c_2=0,p=q=1\), the forced direct coupling is explicitly
\[
K_{13}=\frac{h e^h}{(e^h-1)^2}(h-\sinh h)<0,\qquad K_{13}=-\frac{h^2}{6}+O(h^4).
\]

## Assumptions and scope
The original positive Itô system has \(dX=MX\,dt+\sum_jD_jX\,dW_j\), with real diagonal \(D_j\), independent standard Brownian motions, and \(C=\tfrac12\sum_jD_j^2\). Every nonnegative vector \((c_i)\) is attainable (one independent Brownian driver per site suffices); cross-site correlations of \(\Delta Z\) do not affect their coordinatewise exponential means. The intended drift \(M\) has exactly the two positive arcs shown, zero diagonal and no direct \(1\)-to-\(3\) arc. The step holds \(K\) fixed, uses the same physical noise amplitudes, and requires a *homogeneous Metzler* corrected drift within the noise-first exponential family. Equalities are operator equalities, not just equalities for a single starting vector. Inputs are nonnegative and \(h,p,q>0\). No claim is made about arbitrary time-dependent calibrations, correlated non-diagonal diffusion, or non-exponential numerical methods.

## Proof
Let \(Z=\sum_jD_j\Delta W_j\). The integrating-factor algorithm with frozen drift \(K\) is precisely \(X^+=e^{\operatorname{diag}Z}e^{h(K-C)}X\): the conjugations by the previous integrating factor cancel, even for noncommuting \(K\) and diffusion matrices. Because the coordinatewise Gaussian moment-generating function gives \(\mathbb E[e^{Z_i}]=e^{c_ih}\), its mean step is \(e^{hC}e^{h(K-C)}\). Thus the exact-mean requirement is equivalent to
\[
e^{h(K-C)}=Q:=e^{-hC}e^{hM}=\begin{pmatrix}
d_1&h p d_1&h^2pq d_1/2\\0&d_2&h q d_2\\0&0&d_3
\end{pmatrix},\qquad d_i=e^{-c_ih}>0.
\]
If \(H=K-C\) is Metzler and \(e^{hH}=Q\), then \(H\) must be upper triangular. Indeed choose \(a\) so that \(H+aI\ge0\) entrywise. Since \(e^{hH}=e^{-ah}\sum_{n\ge0}h^n(H+aI)^n/n!\), any strictly positive below-diagonal entry of \(H\) would force the corresponding entry of \(Q\) strictly positive, a contradiction. Hence \(H\) has diagonal \(-c_i\) (unique real scalar logarithms). Its first superdiagonal entries are uniquely determined, because the first divided differences of the logarithm at positive arguments are strictly positive. The second superdiagonal is also determined uniquely since the coefficient of \(H_{13}\) in \((e^{hH})_{13}\) is a strictly positive exponential divided difference. Therefore the unique possible \(K\) is \(C+h^{-1}\log Q\), with \(\log Q\) the real triangular principal logarithm. This argument also proves existence and uniqueness of a Metzler calibrator in dimension two: the only off-diagonal entry of \(\log Q\) is \(Q_{12}\log[d_1,d_2]>0\) (continuous at repeated diagonal values).

To determine the critical sign in three dimensions, use the resolvent representation of the logarithm, valid since \(Q\) has positive spectrum. Direct inversion of the triangular resolvent gives
\[
(\log Q)_{13}=\frac{h^2pqd_1}{2}\int_0^\infty\frac{t-d_2}{(t+d_1)(t+d_2)(t+d_3)}\,dt.
\]
For fixed \(d_1,d_3>0\), write the integral as
\[
J(b)=\int_0^\infty \frac{\frac12-\frac{b}{t+b}}{(t+d_1)(t+d_3)}\,dt.
\]
It is strictly decreasing in \(b>0\), since its derivative is \(-\int_0^\infty t/((t+b)^2(t+d_1)(t+d_3))\,dt<0\). Setting \(b=\sqrt{d_1d_3}\), the substitution \(t=d_1d_3/u\) preserves the positive measure \(dt/((t+d_1)(t+d_3))\) and reverses the sign of \((t-b)/(2(t+b))\); hence \(J(\sqrt{d_1d_3})=0\). It follows that the sign of \((\log Q)_{13}\) is that of \(\sqrt{d_1d_3}-d_2\), equivalently that of \(2c_2-c_1-c_3\). First superdiagonal entries are positive, so nonnegativity of \(K_{13}\) is necessary and sufficient for \(K\) to be Metzler.

For the explicit obstruction \((c_1,c_2,c_3)=(1,0,1)\), the divided-difference formula for the triangular logarithm simplifies to \(K_{13}=h e^h(h-\sinh h)/(e^h-1)^2\). Since \(\sinh h>h\) for all \(h>0\), it is strictly negative at every positive step size. Taylor expansion establishes the stated \(-h^2/6+O(h^4)\) behavior. This proves both the classification and its minimal dimension boundary. Finally, whenever the calibrator is Metzler, \(e^{h(K-C)}\ge0\) entrywise, and multiplication by the positive random diagonal \(e^{\operatorname{diag}Z}\) preserves nonnegative states almost surely; independent increments then give \(\mathbb E X_k=e^{khM}X_0\) for every integer \(k\ge0\).

## Verification
Run `python verify.py` with Python 3, NumPy and SciPy. The script independently computes matrix exponentials and real matrix logarithms for 132 parameter-step settings and six closed-form special cases, checking exact-mean operator identities, the threshold sign and the analytic special formula to floating-point tolerances. Its finite tests do not prove the continuous parameter classification; the integral sign argument above does. The verifier's `K` is computed directly from the matrix logarithm, not from the midpoint criterion.

## Relationship to prior work
Gurpegui Ramon, Tanaka and Rantzer, *L1 Optimal Control of Continuous-Time Stochastic Positive Systems*, arXiv:2607.03952v1 (2026-07-04), Section 1.1 and Algorithm 1, provide the integrating-factor positivity-preserving simulation motivating the frozen Gaussian-noise-first family. Their claimed performance concerns the continuous-time stochastic control problem, not exact weak moments at a finite simulation step. General matrix embedding theory addresses when a positive matrix admits a Metzler logarithm. In particular *Geometry-Aware Operator Families for Structured Representation Learning*, arXiv:2609.33089, Appendix I.33, exhibits a non-embeddable product of positive exponentials in dimension three. The present finding does **not** claim to discover non-embeddability in general; its specific new contribution is the complete variance-midpoint criterion for the given stochastic splitting and feedforward three-site family, uniformly at every step size, with the two-site boundary and an explicit obstruction formula. Earlier three-state Markov embedding analyses (e.g. Frydman and Lencastre et al.) give broader context and create residual priority uncertainty for the precise specialized criterion.

## Limitations
The result concerns a finite-dimensional feedforward drift, diagonal multiplicative Gaussian noise and a single frozen Metzler drift in a specified splitting order. It does not show impossibility of exact-mean positive numerical methods by other constructions, nor does it address higher weak moments, convergence order, or optimization of control policies. The mathematical proof is self-contained, but complete precedence against all classical matrix-embedding literature is not independently certified.

## References
1. A. Gurpegui Ramon, T. Tanaka, A. Rantzer, *L1 Optimal Control of Continuous-Time Stochastic Positive Systems*, arXiv:2607.03952v1, 2026-07-04. https://arxiv.org/abs/2607.03952
2. *Geometry-Aware Operator Families for Structured Representation Learning*, arXiv:2609.33089, Appendix I.33, 2026. https://arxiv.org/abs/2609.33089
3. P. Lencastre, F. Raischel, T. Rogers, P. G. Lind, *From empirical data to continuous Markov processes: a systematic approach*, arXiv:1510.07282 (2015), Sections on the embedding problem. https://arxiv.org/abs/1510.07282
4. H. Frydman, *The embedding problem for Markov chains with three states*, Mathematical Proceedings of the Cambridge Philosophical Society, DOI record: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/embedding-problem-for-markov-chains-with-three-states/38C9C76E6AAF0E71D957D5FE810767DB
