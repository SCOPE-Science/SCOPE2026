# A sharp two-worker DIANA stability boundary under correlated half-dropout compression

## Finding

Consider the DIANA gradient-difference memory update described below with two identical scalar quadratic workers. Each worker transmits with marginal probability \(1/2\) in each round, but the two transmission indicators may be dependent. Let \(q\in[0,1/2]\) be the probability of simultaneous success (which also equals the probability of simultaneous failure). Then, for every deterministic \(x_0\ne0\) and zero initial memories, the complete phase diagram at normalized step size one is

\[
\begin{aligned}
0\le q<1/10 &: \quad \mathbb E[x_k^2]\longrightarrow0\ \text{geometrically},\\
q=1/10 &: \quad \mathbb E[x_k^2]\longrightarrow\frac6{19}x_0^2,\\
1/10<q\le1/2 &: \quad \limsup_{k\to\infty}\bigl(\mathbb E[x_k^2]\bigr)^{1/k}>1.
\end{aligned}
\]

In the first regime the entire three-component state converges geometrically in mean square. In the third regime the position's expected squared error grows exponentially along a subsequence. All three regimes have exactly one expected transmitted scalar per round; independent worker transmissions correspond to \(q=1/4\), which lies in the unstable regime.

## Assumptions and scope

Both local objectives are \(f_1(x)=f_2(x)=x^2/2\), with no additional regularizer, no gradient noise, and no momentum. Let the memories \(h_1,h_2\) start at zero and let the initial position be \(x_0\ne0\). The independent-across-rounds Bernoulli pairs \((\delta_1,\delta_2)\) have law

\[
\Pr(0,0)=\Pr(1,1)=q,\qquad
\Pr(0,1)=\Pr(1,0)=\tfrac12-q,\qquad 0\le q\le\tfrac12.
\]

For each worker, use the unbiased half-dropout compressor \(\mathcal C_i(u)=2\delta_i u\), a scalar instance of the general unbiased-compressor formulation of DIANA (not the original paper's scalar \(p\)-quantizer). The memory learning rate is \(\alpha=1/2\) and the primal step size is \(\gamma=1\). With the old iterate and old memories on every right-hand side, the update is

\[
 d_i=2\delta_i(x-h_i),\quad
 h_i^+=h_i+\tfrac12d_i,\quad
 x^+=x-\tfrac12\bigl(h_1+h_2+d_1+d_2\bigr).
\]

Thus \(\mathbb E[\mathcal C_i(u)]=u\), and each worker has an unchanged marginal transmission law for all \(q\). The joint compressor law changes only the cross-worker dependence, not the number of workers, local objective, or communication budget.

## Proof

Write \(z=(x,h_1,h_2)^{\mathsf T}\). Conditional on \((\delta_1,\delta_2)=(a,b)\), the exact update is \(z^+=M_{ab}z\), where

\[
M_{ab}=\begin{pmatrix}
1-a-b & a-\tfrac12 & b-\tfrac12\\
a & 1-a & 0\\ b&0&1-b
\end{pmatrix}.
\]

The initialization and pair law are symmetric under exchange of the workers. Consequently the covariance has the exchangeable form

\[
S_k=\mathbb E[z_k z_k^{\mathsf T}]=
\begin{pmatrix}X_k&U_k&U_k\\U_k&H_k&V_k\\U_k&V_k&H_k\end{pmatrix},
\qquad (X_0,U_0,H_0,V_0)=(x_0^2,0,0,0).
\]

Multiplying \(M_{ab}S_kM_{ab}^{\mathsf T}\) and weighting by the four joint probabilities gives the exact closed recurrence \(v_{k+1}=T(q)v_k\), for \(v=(X,U,H,V)^{\mathsf T}\), with

\[
T(q)=\begin{pmatrix}
2q&-4q&\tfrac12&2q-\tfrac12\\
-q&2q&-\tfrac14&\tfrac14-q\\
\tfrac12&0&\tfrac12&0\\
q&1-2q&0&q
\end{pmatrix}.
\]

A direct determinant calculation gives

\[
\det(zI-T(q))=\frac z8\bigl(8z^3-(40q+4)z^2+(36q-4)z+1-6q\bigr).
\]

For the monic cubic factor put \(a=-5q-1/2\), \(b=(9q-1)/2\), \(c=(1-6q)/8\). The degree-three Schur reduction divides the reciprocal-polynomial difference by \(z\), producing the quadratic with coefficients \(A=1-c^2\), \(B=a-cb\), \(C=b-ca\). Since \(|c|<1\), the cubic is strictly Schur-stable precisely when \(A+B+C>0\), \(A-B+C>0\), and \(A>|C|\). Here

\[
\begin{aligned}
A+B+C&=\frac{(6q+7)(1-10q)}{64},\\
A-B+C&=\frac{3(3-2q)(82q+7)}{64},\\
A-C&=\frac{204q^2-292q+91}{64},\\
A+C&=\frac{-276q^2+316q+35}{64}.
\end{aligned}
\]

All four expressions are positive throughout \(0\le q<1/10\). For the last two this follows immediately by bounding \(q\) in that interval (the first polynomial decreases but remains positive; the second is at least \((35-276/100)/64\)). Thus every eigenvalue of \(T(q)\), including its additional zero eigenvalue, lies strictly inside the unit disk. This proves geometric decay of all second moments in that regime.

For the remaining regimes, the scalar generating function \(F_q(t)=\sum_{k\ge0} X_k t^k/x_0^2\) is exactly

\[
F_q(t)=\frac{(t-2)^2\bigl((6q-1)t-2\bigr)}{(6q-1)t^3+(4-36q)t^2+(4+40q)t-8}.
\]

At \(q=1/10\) it simplifies to

\[
F_{1/10}(t)=\frac{(t-2)^2(t+5)}{(t-1)(t^2-20)}.
\]

Its only pole on the unit circle is the simple pole at \(t=1\), and its residue factor satisfies \(\lim_{t\to1}(1-t)F_{1/10}(t)=6/19\). The other poles lie at \(\pm\sqrt{20}\), outside the unit disk. Coefficient extraction therefore proves \(X_k/x_0^2\to6/19\).

For \(1/10<q\le1/2\), the denominator of \(F_q(t)\) is \(-8\) at \(t=0\) and \(10q-1>0\) at \(t=1\). Hence it has a root \(t_*\in(0,1)\). The numerator never vanishes at such a root, because \((t-2)^2>0\) and \((6q-1)t-2<0\) whenever \(0<t<1\) and \(q\le1/2\). Thus \(F_q\) has a genuine pole inside the unit disk. Its coefficients \(X_k/x_0^2\) are nonnegative, so the Cauchy–Hadamard formula yields \(\limsup_{k\to\infty}(X_k)^{1/k}\ge1/t_*>1\). This completes the three-way classification.

## Verification

Run `python3 verify.py` with the pinned dependency in `requirements.txt`. It recomputes all four update matrices, the covariance transfer matrix, characteristic polynomial, rational generating function, critical residue, and four Schur expressions by exact symbolic arithmetic. It independently enumerates weighted update histories for five rational correlation values through six rounds and compares their exact squared-error means with the transfer recurrence. These finite checks are diagnostic; the infinite-horizon conclusions are proved above.

## Relationship to prior work

Mishchenko, Gorbunov, Takáč, and Richtárik introduced the gradient-difference memory update (arXiv:1901.09269, Algorithm 1). Condat, Yi, and Richtárik analyze the general unbiased-compressor DIANA form and give sufficient linear-convergence step bounds in EF-BV (arXiv:2205.04180, Section 3.2 and Appendix B). Those bounds do not imply the unit-step correlated-worker phase diagram: the stated positive-variance sufficient step condition is smaller than one in this instance. Szlendak, Tyurin, and Richtárik study correlated unbiased compressors for the different MARINA method (arXiv:2110.03300), using variance inequalities rather than the exact DIANA memory covariance spectrum.

A prior exact independent-compressor DIANA calculation determines the stability boundary as the worker count varies, but fixes independent compressor randomness. Its two-worker case covers \(q=1/4\) only. The present result instead determines the full cross-worker coupling parameter at fixed worker count and fixed step, including the critical positive error floor; neither the independent-only theorem nor the general sufficient bounds yield that conclusion. The analytical increment is the closed joint-coupling moment law and its sharp Schur/pole transition.

## Limitations

This is an exact-arithmetic statement for two identical scalar quadratics, zero initial memory, unit primal step, memory learning rate one half, and independent rounds. It does not classify arbitrary initial memories, unequal curvatures, other step sizes, multiple dimensions, general network topologies, or almost-sure convergence. Bernoulli whole-message transmission is a general unbiased compressor rather than the original paper's scalar quantizer. Existing sufficient-convergence theorems remain valid inside their own step-size assumptions. The novelty comparison cannot exclude equivalent unpublished or poorly indexed specialized computations; independent validation is not claimed.

## References

1. K. Mishchenko, E. Gorbunov, M. Takáč, P. Richtárik, *Distributed Learning with Compressed Gradient Differences*, arXiv:1901.09269, first public version 2019-01-26, https://arxiv.org/abs/1901.09269.
2. L. Condat, K. Yi, P. Richtárik, *EF-BV: A Unified Theory of Error Feedback and Variance Reduction Mechanisms for Biased and Unbiased Compression in Distributed Optimization*, arXiv:2205.04180, first public version 2022-05-09, https://arxiv.org/abs/2205.04180.
3. R. Szlendak, A. Tyurin, P. Richtárik, *Permutation Compressors for Provably Faster Distributed Nonconvex Optimization*, arXiv:2110.03300, first public version 2021-10-07, https://arxiv.org/abs/2110.03300.
