# Exact half-dropout mean-square stability frontier for scalar MARINA
## Finding

Consider MARINA on \(n\ge1\) identical scalar objectives
\[
f_i(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]
At every compressed communication, client \(i\) uses the unbiased scalar half-dropout operator
\[
Q_i(z)=2\delta_i z,
\qquad
\delta_i\sim\operatorname{Bernoulli}(1/2),
\]
independently across clients and iterations. This compressor has variance parameter
\[
\omega=1
\]
and expected scalar density
\[
\zeta_Q=\frac12.
\]
Use MARINA's density-matched refresh choice
\[
p=\frac{\zeta_Q}{d}=\frac12
\]
for the scalar case \(d=1\), and put
\[
s=\gamma\lambda.
\]

Then the exact mean-square stability interval is
\[
0<s<s_n,
\]
where
\[
s_n=
\frac{n+\sqrt{9n^2+16n}}{2(n+2)}.
\]
This boundary is necessary and sufficient for
\[
\mathbb E[x_k^2]\longrightarrow0.
\]

The frontier increases strictly with the number of independently compressed clients:
\[
s_1=1,
\qquad
s_n\uparrow2,
\]
and
\[
s_n=
2-\frac{8}{3n}
+O(n^{-2}).
\]
Thus independent client averaging recovers the ordinary gradient-descent stability ceiling
\[
s<2
\]
in the large-\(n\) limit.

The source MARINA theorem gives the general sufficient restriction
\[
s
\le
\frac{1}{1+n^{-1/2}}
\]
for this same density-matched scalar setup. That sufficient range tends to \(1\), while the exact scalar mean-square frontier tends to \(2\).

The exact boundary follows from a regenerative description. At every full-gradient refresh, the normalized estimator equals the current iterate. Between refreshes it is multiplied by independent compression factors. If \(A\) denotes the random multiplier taking one refreshed iterate to the next refreshed iterate, then
\[
\mathbb E[A^2]
=
\psi_n(s),
\]
where
\[
\psi_n(s)-1
=
\frac{
2s\left[(n+2)s^2-ns-2n\right]
}{
(1+s)\left[n+2ns-(n+1)s^2\right]
}.
\]
Throughout the candidate stability region the denominator is positive. Therefore
\[
\psi_n(s)<1
\]
holds exactly when
\[
(n+2)s^2-ns-2n<0,
\]
whose positive root is \(s_n\).

## Assumptions and scope

The objectives are identical deterministic scalar quadratics with a common minimizer at the origin. The clients use independent half-dropout compressors, and the full-gradient refresh coin is independent of all compression coins.

The refresh probability \(p=1/2\) is not an arbitrary slice: for this scalar compressor its expected density is \(\zeta_Q=1/2\), and the defining MARINA paper recommends \(p=\zeta_Q/d\).

Mean-square stability means convergence of the actual iterate second moment to zero. No claim is made about heterogeneous client Hessians, correlated compressors, partial participation, stochastic local gradients, or higher-dimensional coordinate interactions.

The comparison with the source stepsize is only a comparison with a general sufficient theorem. The exact scalar frontier does not invalidate that theorem.

## Proof

Write the normalized MARINA estimator as
\[
y_k=\frac{g_k}{\lambda}.
\]
The iterate update is
\[
x_{k+1}=x_k-sy_k.
\]

At a refresh,
\[
y_{k+1}=x_{k+1}.
\]
At a compressed iteration,
\[
y_{k+1}
=
y_k+
\frac1n
\sum_{i=1}^n
Q_i(x_{k+1}-x_k).
\]
Define
\[
Z_k=\frac2n\sum_{i=1}^n\delta_{i,k}.
\]
Then
\[
\mathbb E[Z_k]=1,
\qquad
\operatorname{Var}(Z_k)=\frac1n,
\]
and a compressed iteration gives
\[
y_{k+1}
=
(1-sZ_k)y_k.
\]

Consider the process only at full-gradient refresh epochs. Immediately after every refresh,
\[
y=x.
\]
Starting from a refreshed state \(x=a\), let \(K\) be the number of consecutive compressed iterations before the next refresh. Since \(p=1/2\),
\[
\mathbb P(K=k)=2^{-(k+1)},
\qquad
k=0,1,2,\ldots.
\]
For compressed-step multipliers
\[
R_j=1-sZ_j,
\]
define
\[
P_0=1,
\qquad
P_j=\prod_{\ell=1}^jR_\ell.
\]
The next refreshed iterate is
\[
a'
=
a\left(
1-s\sum_{j=0}^{K}P_j
\right).
\]
Hence, with
\[
S=\sum_{j=0}^{K}P_j,
\]
the refresh-to-refresh multiplier is
\[
A=1-sS.
\]

The random series satisfies the distributional recursion
\[
S\overset{d}{=}1+BRS',
\]
where \(B\sim\operatorname{Bernoulli}(1/2)\), \(R\) has the same law as \(1-sZ\), and \(S'\) is an independent copy of \(S\).

Put
\[
m=\mathbb E[S],
\qquad
Q=\mathbb E[S^2].
\]
Since
\[
\mathbb E[R]=1-s
\]
and
\[
\mathbb E[R^2]
=
1-2s+
\left(1+\frac1n\right)s^2,
\]
the first-moment recursion gives
\[
m
=
1+\frac12(1-s)m
=
\frac{2}{1+s}.
\]
The second-moment recursion gives
\[
Q
=
1+(1-s)m
+
\frac12
\left[
1-2s+
\left(1+\frac1n\right)s^2
\right]Q.
\]

Therefore
\[
\psi_n(s)
=
\mathbb E[(1-sS)^2]
=
1-2sm+s^2Q,
\]
and direct simplification yields
\[
\psi_n(s)-1
=
\frac{
2s\left[(n+2)s^2-ns-2n\right]
}{
(1+s)\left[n+2ns-(n+1)s^2\right]
}.
\]

Let \(s_n\) be the positive root of
\[
(n+2)s^2-ns-2n=0.
\]
One has
\[
s_n\ge1.
\]
At \(s=s_n\),
\[
(n+1)s_n^2-2ns_n-n<0,
\]
because the difference between the left-hand side and the boundary polynomial equals
\[
n-ns_n-s_n^2<0.
\]
Thus the second moment of the within-cycle multiplier is summable throughout
\[
0<s\le s_n,
\]
and the denominator in the displayed formula for \(\psi_n(s)-1\) is positive there.

Successive refresh cycles are independent and identically distributed after scaling. If \(X_j\) is the iterate at the \(j\)-th refresh, then
\[
\mathbb E[X_j^2]
=
x_0^2\psi_n(s)^j.
\]
If
\[
\psi_n(s)\ge1,
\]
mean-square convergence is impossible already on this refresh subsequence.

If
\[
\psi_n(s)<1,
\]
the refresh-epoch second moments decay geometrically. The expected squared amplification accumulated inside one cycle is finite because
\[
\frac12\mathbb E[R^2]<1
\]
throughout this range. Decomposing a fixed-time second moment according to its most recent refresh therefore gives a convergent regenerative convolution with a geometrically decaying cycle-start term. Hence
\[
\mathbb E[x_k^2]\to0.
\]
This proves the exact all-time mean-square frontier.

For monotonicity in \(n\), write
\[
F_n(s)=(n+2)s^2-ns-2n.
\]
At its positive root,
\[
1\le s_n<2.
\]
For fixed \(s\in[1,2)\),
\[
\frac{\partial F_n}{\partial n}
=
s^2-s-2<0,
\]
while
\[
\frac{\partial F_n}{\partial s}
=
2(n+2)s-n>0.
\]
Therefore the positive root increases strictly with \(n\). Expanding the closed form gives
\[
s_n
=
2-\frac{8}{3n}
+\frac{128}{27n^2}
+O(n^{-3}).
\]

## Verification

The accompanying `verify.py` checks the compressor moments by exact binomial enumeration, verifies the regenerative moment identities in rational arithmetic, checks the closed boundary formula for multiple client counts, and compares finite-state second-moment simulations with the predicted stable and unstable sides.

The computations are transcription guards. Necessity and sufficiency follow from the regenerative proof above, not from finite experiments.

## Relationship to prior work

Gorbunov, Burlachenko, Li, and Richtárik introduced MARINA as a compressed distributed method based on occasional exact-gradient refreshes and compressed gradient differences. Their theorem gives general sufficient stepsizes, and their density-matched corollary recommends
\[
p=\frac{\zeta_Q}{d}.
\]
For independent compressors, their scalar specialization gives the sufficient bound
\[
s\le(1+n^{-1/2})^{-1}
\]
used for comparison here. The inspected full text does not derive an exact scalar mean-square phase boundary.

Szlendak, Tyurin, and Richtárik later refined MARINA using correlated permutation compressors and Hessian variance. Their full text includes strongly convex quadratic experiments and reports that different compressors can tolerate substantially different tuned stepsizes. Their analysis improves general complexity bounds but does not give the half-dropout regenerative formula or the exact frontier above.

The present result isolates the smallest exact benchmark on which MARINA's refresh mechanism and client averaging can be separated algebraically. The large-client limit shows that independent compression noise is averaged away strongly enough for the exact scalar ceiling to recover the uncompressed value \(2\), whereas the generic sufficient theorem saturates at \(1\).

## Limitations

The exact formula uses identical scalar client Hessians and independent half-dropout compression. Heterogeneity changes the compressed-gradient-difference law and destroys the one-dimensional regenerative multiplier.

The result does not cover correlated permutation compressors, partial participation, stochastic local gradients, or VR-MARINA.

The mean-square frontier concerns stability, not the stepsize minimizing communication complexity or wall-clock time.

The comparison to the source theorem is deliberately one-sided: a sufficient theorem can be conservative on a special quadratic family without being incorrect.

Equivalent regenerative calculations may exist in the literature on randomly switched linear systems under terminology unrelated to MARINA; this remains the principal originality risk.

## References

1. Eduard Gorbunov, Konstantin P. Burlachenko, Zhize Li, and Peter Richtárik, “MARINA: Faster Non-Convex Distributed Learning with Compression,” arXiv:2102.07845v1, 2021.
2. Rafał Szlendak, Alexander Tyurin, and Peter Richtárik, “Permutation Compressors for Provably Faster Distributed Nonconvex Optimization,” arXiv:2110.03300v1, 2021.
