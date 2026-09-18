# Exact Haar moments remove sampling-dimension restrictions in sparse stochastic subspace descent

## Statement

Let \(n\ge 2\), \(1\le s\le n\), and let \(R\in\mathbb R^{s\times n}\) have orthonormal rows, \(RR^\top=I_s\). Consider an objective
\[
f(x)=g(Rx),
\]
where \(g:\mathbb R^s\to\mathbb R\) is differentiable, \(L\)-smooth, and bounded below. Let \(P_k\in\operatorname{St}(n,d)\), \(1\le d\le n\), be independent Haar-distributed orthonormal frames and run classical stochastic subspace descent
\[
x_{k+1}=x_k-\alpha P_kP_k^\top\nabla f(x_k).
\]
Define
\[
\theta_{n,s,d}
:=\frac{1}{n+2}\left(d+2+(s-1)\frac{n-d}{n-1}\right).
\]
Then the constant stepsize
\[
\boxed{\alpha_* = \frac{1}{L\theta_{n,s,d}}}
\]
satisfies
\[
\boxed{
\min_{0\le k<N}\mathbb E\|\nabla f(x_k)\|^2
\le
\frac{2Ln\theta_{n,s,d}}{dN}\bigl(f(x_0)-f_*\bigr),
}
\]
where \(f_*:=\inf_x f(x)\).

No lower bound on \(d\), logarithmic condition, or relation such as \(d\le s/16\) is needed. A simple ambient-dimension-free relaxation is
\[
n\theta_{n,s,d}\le d+s+1,
\]
so
\[
\boxed{
\min_{0\le k<N}\mathbb E\|\nabla f(x_k)\|^2
\le
\frac{2L(d+s+1)}{dN}\bigl(f(x_0)-f_*\bigr).
}
\]
In particular, for one-dimensional random subspaces \(d=1\),
\[
\theta_{n,s,1}=\frac{s+2}{n+2},\qquad
\alpha_* = \frac{n+2}{L(s+2)},
\]
and
\[
\min_{0\le k<N}\mathbb E\|\nabla f(x_k)\|^2
\le
\frac{2Ln(s+2)}{(n+2)N}\bigl(f(x_0)-f_*\bigr)
<\frac{2L(s+2)}{N}\bigl(f(x_0)-f_*\bigr).
\]
Thus a single random directional derivative per iteration already has stationarity complexity controlled by the intrinsic dimension rather than the ambient dimension in this exact-gradient SSD model.

## Exact Haar second moment

Write
\[
Q=PP^\top,\qquad B=RQR^\top.
\]
The key identity is
\[
\boxed{
\mathbb E[B]=\frac dn I_s,
\qquad
\mathbb E[B^2]=\frac dn\,\theta_{n,s,d} I_s.
}
\]
The first identity is the standard isotropy of a Haar rank-\(d\) projector. For the second, rotational invariance lets us take \(R=[I_s\;0]\). A diagonal entry of a Haar projector has
\[
Q_{11}\sim\operatorname{Beta}\!\left(\frac d2,\frac{n-d}{2}\right),
\]
so
\[
\mathbb E Q_{11}^2=\frac{d(d+2)}{n(n+2)}.
\]
Because \(Q^2=Q\), exchangeability of the off-diagonal entries gives, for \(i\ne j\),
\[
\mathbb E Q_{ij}^2
=\frac{d(n-d)}{n(n-1)(n+2)}.
\]
Hence
\[
\begin{aligned}
\mathbb E(B^2)_{11}
&=\mathbb E Q_{11}^2+
  \sum_{j=2}^{s}\mathbb E Q_{1j}^2\\
&=\frac dn\frac{1}{n+2}
\left(d+2+(s-1)\frac{n-d}{n-1}\right).
\end{aligned}
\]
The distribution of \(B\) is invariant under conjugation by every matrix in \(O(s)\), so \(\mathbb E[B^2]\) is a scalar multiple of \(I_s\), proving the identity.

## Expected-descent proof

Let \(y=Rx\), \(u=\nabla g(y)\). Since \(R\) has orthonormal rows,
\[
\nabla f(x)=R^\top u,
\qquad
\|\nabla f(x)\|=\|u\|.
\]
One SSD update induces
\[
y_+=y-\alpha Bu.
\]
By \(L\)-smoothness,
\[
g(y_+)\le g(y)-\alpha u^\top Bu+\frac{L\alpha^2}{2}u^\top B^2u.
\]
Conditioning on the current iterate and using the exact moments gives
\[
\mathbb E[g(y)-g(y_+)\mid y]
\ge
\frac dn\left(\alpha-\frac{L\theta_{n,s,d}}2\alpha^2\right)\|u\|^2.
\]
The quadratic coefficient is maximized at \(\alpha_*=1/(L\theta_{n,s,d})\), yielding
\[
\mathbb E[f(x)-f(x_+)\mid x]
\ge
\frac{d}{2Ln\theta_{n,s,d}}\|\nabla f(x)\|^2.
\]
Summation and \(f(x_N)\ge f_*\) give the stated stationarity bound.

The relaxation \(n\theta_{n,s,d}\le d+s+1\) follows from
\[
\frac{n-d}{n-1}\le 1,
\qquad
\frac n{n+2}<1.
\]

## Comparison with the September 2026 sparse-SSD theorem

Ghosh--Ng--Poirion--Takeda (2026), Theorem 6, analyzes the same classical Haar SSD iteration for \(f(x)=g(Rx)\). Their theorem assumes
\[
\max\left\{1,2\log\frac{2n^2}{9s}\right\}\le d\le\frac{s}{16},
\qquad
\alpha=\frac{n}{18sL},
\]
and obtains
\[
\min_{0\le k<N}\mathbb E\|\nabla f(x_k)\|^2
\le
\frac{36Ls}{dN}\bigl(f(x_0)-f_*\bigr).
\]
Their proof controls the quadratic term using high-probability Gaussian singular-value bounds and a bad-event split. The exact Haar second moment above evaluates that quadratic term directly.

Whenever the source theorem's assumptions hold, \(d\le s/16\) and \(d\ge1\) imply \(s\ge16\), and
\[
n\theta_{n,s,d}\le d+s+1\le\frac98s.
\]
Consequently the new stationarity coefficient obeys
\[
\frac{2Ln\theta_{n,s,d}}d
\le \frac94\frac{Ls}{d},
\]
which is at least a factor \(16\) smaller than \(36Ls/d\). The new stepsize is correspondingly at least \(16\) times larger than \(n/(18sL)\) throughout that regime.

For example, at \((n,s,d)=(1000,512,32)\), which satisfies the source restrictions,
\[
\theta=\frac{264307}{500499}\approx0.528087,
\]
so the new coefficient multiplying \(L(f(x_0)-f_*)/N\) is
\[
\frac{33038375}{1000998}\approx 33.0054,
\]
versus \(576\) in Theorem 6, an exact improvement factor of approximately \(17.4517\). The corresponding dimensionless stepsizes are \(\alpha_*L\approx1.89363\) and \(125/1152\approx0.108507\).

## PL corollary

If \(g\) additionally satisfies the Polyak--Lojasiewicz inequality
\[
\|\nabla g(y)\|^2\ge 2\mu\bigl(g(y)-g_*\bigr),
\]
then the same one-step estimate yields
\[
\boxed{
\mathbb E[f(x_k)-f_*]
\le
\left(1-\frac{\mu}{L}\frac{d}{n\theta_{n,s,d}}\right)^k
\bigl(f(x_0)-f_*\bigr).
}
\]
The contraction factor lies in \([0,1)\) because \(\theta_{n,s,d}\ge d/n\).

## Rank-one sharpness

The stepsize and PL contraction are exact for the rank-one quadratic. Set \(s=1\) and
\[
g(y)=\frac L2y^2.
\]
For a unit active direction \(r\), let
\[
q=r^\top Qr.
\]
Then
\[
\mathbb E q=\frac dn,
\qquad
\mathbb E q^2=\frac{d(d+2)}{n(n+2)},
\qquad
\theta_{n,1,d}=\frac{d+2}{n+2}.
\]
Writing \(t=\alpha L\), the exact one-step objective contraction is
\[
\frac{\mathbb E g(y_+)}{g(y)}
=1-2t\frac dn+t^2\frac{d(d+2)}{n(n+2)}.
\]
Its unique minimizing constant stepsize is
\[
t_* = \frac{n+2}{d+2}=\frac1{\theta_{n,1,d}},
\]
with minimum contraction
\[
\boxed{
1-\frac{d(n+2)}{n(d+2)}
=1-\frac{d}{n\theta_{n,1,d}}.
}
\]
Thus the moment-optimal stepsize and the PL factor cannot be uniformly improved within constant-stepsize classical SSD even on this simplest low-dimensional quadratic family.

## Limitations

The result concerns exact-gradient classical SSD with independent Haar subspaces and globally \(L\)-smooth low-dimensional objectives of the form \(g(Rx)\). It is an expectation guarantee; individual iterations may increase the objective, especially because the optimal expected stepsize can exceed \(1/L\). It does not analyze finite-difference directional-derivative error, stochastic gradient noise, non-Haar subspaces, unknown or changing active subspaces, or the persistence-of-memory algorithm introduced by the source paper. The stepsize requires \(L\) and the intrinsic dimension \(s\) (or suitable safe bounds) to be known.

The beta-distribution moment used in the proof is classical geometric probability and is not claimed as new. The claimed contribution is the exact compressed-projector second moment in the sparse-SSD descent calculation, the resulting unrestricted intrinsic-dimension stationarity/PL rates, the quantitative sharpening of Theorem 6 of the September 2026 source, and the rank-one sharpness statement.

## Reproducibility

`artifacts/verify_exact_haar_ssd.py` uses exact rational arithmetic to verify the Haar moment identity, the numerical comparison with the source theorem at \((1000,512,32)\), the equality between rate and stepsize improvement factors in that example, limiting full-dimensional cases, and the rank-one sharpness formula. `artifacts/verified_output.txt` contains its executed output.

## References

1. S. Ghosh, C. Z. Q. Ng, P.-L. Poirion, and A. Takeda, *Gradient Descent with Stochastic Subspaces via Persistence of Memory*, arXiv:2609.18416v1 (2026). https://arxiv.org/abs/2609.18416v1
2. D. Kozak, S. Becker, A. Doostan, and L. Tenorio, *A stochastic subspace approach to gradient-free optimization in high dimensions*, Computational Optimization and Applications 79(2), 339--368 (2021). https://doi.org/10.1007/s10589-021-00271-w
3. P. Frankl and H. Maehara, *Some geometric applications of the beta distribution*, Annals of the Institute of Statistical Mathematics 42(3), 463--474 (1990). https://doi.org/10.1007/BF00049302
4. M. Derezinski, F. Liang, Z. Liao, and M. W. Mahoney, *Precise expressions for random projections: Low-rank approximation and randomized Newton*, NeurIPS 2020. https://arxiv.org/abs/2006.10653
