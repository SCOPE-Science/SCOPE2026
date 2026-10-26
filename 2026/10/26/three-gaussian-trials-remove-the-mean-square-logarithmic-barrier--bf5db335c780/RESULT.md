# Three Gaussian trials remove the mean-square logarithmic barrier in randomized joint diagonalization

## Finding

Consider the unmodified Gaussian random-linear-combination algorithm for orthogonal joint diagonalization, with its best-of-trials off-diagonal Frobenius-loss selection rule. For the natural two-matrix, nearly commuting family
\[
 D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 \mathcal A_\varepsilon=\{D,\varepsilon X\},\quad 0<\varepsilon<1,
\]
there is an **exact all-trial probability law**, and the first, second, and third independent Gaussian trials occupy distinct sharp mean-square asymptotic regimes.

For each integer \(L\ge1\), independently draw \((g_{j1},g_{j2})\sim N(0,I_2)\), diagonalize \(g_{j1}D+\varepsilon g_{j2}X\) by an orthogonal \(Q_j\), and retain the trial with smallest
\[
 J_j=\|\operatorname{offdiag}(Q_j^{\mathsf T}DQ_j)\|_F^2
 +\|\operatorname{offdiag}(Q_j^{\mathsf T}\varepsilon XQ_j)\|_F^2.
\]
Write \(R_L=\sqrt{\min_{1\le j\le L}J_j}\). For \(Z_L=R_L/(\sqrt2\varepsilon)\), its full distribution is
\[
 \Pr(Z_L>z)=\begin{cases}
 1,&z\le1,\\
 \left[\dfrac2\pi\arcsin\sqrt{\dfrac{z^{-2}-\varepsilon^2}{1-\varepsilon^2}}\right]^L,
       &1<z<\varepsilon^{-1},\\
 0,&z\ge\varepsilon^{-1}.
 \end{cases}
\]
In particular, the squared error has the sharp behavior as \(\varepsilon\downarrow0\):
\[
 \begin{aligned}
 \mathbb E R_1^2&=2\varepsilon\quad\text{exactly},\\
 \mathbb E R_2^2&\sim\frac{16}{\pi^2}\varepsilon^2\log(1/\varepsilon),\\
 \mathbb E R_3^2&\sim\frac{48\log2}{\pi^2}\varepsilon^2,\\
 \mathbb E R_L^2&\sim2M_L\varepsilon^2\quad(L\ge3),
 \end{aligned}
\]
where \(1<M_L<\infty\) is the explicit constant
\[
 M_L=1+2\int_1^\infty z
 \left[\frac2\pi\arcsin(1/z)\right]^L\,dz,
 \qquad M_3=\frac{24\log2}{\pi^2}.
\]
Because \(\min_{Q\in O(2)}J(Q)=2\varepsilon^2\), **three independent Gaussian trials are necessary and sufficient for uniformly bounded mean-square loss relative to the optimal loss as \(\varepsilon\downarrow0\)** on this family (for each fixed trial count). Two trials leave a logarithmic penalty, while one trial loses an entire power of the perturbation size.

There is also a sharp *first*-moment transition:
\[
 \begin{aligned}
 \mathbb E R_1&=\frac{2\sqrt2\,\varepsilon}{\pi}
 K(\sqrt{1-\varepsilon^2})
 \sim\frac{2\sqrt2}{\pi}\varepsilon\log(4/\varepsilon),\\
 \mathbb E R_2&\sim \frac{16\sqrt2\,G}{\pi^2}\varepsilon,
 \end{aligned}
\]
where \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2t)^{-1/2}\,dt\) and \(G=-\int_0^{\pi/4}\log(\tan t)\,dt\) is Catalan's constant. The exact finite-\(\varepsilon\) distribution above also supplies every bounded positive moment.

## Assumptions and scope

Every assertion is for real symmetric \(2\times2\) matrices, \(0<\varepsilon<1\), exact arithmetic, independent standard *two-dimensional real Gaussian* trial weights, orthogonal eigenvectors of the weighted sum, and the source algorithm's objective (squared Frobenius off-diagonality summed over both input matrices). The random sum has simple spectrum almost surely for every such \(\varepsilon\); the choice of eigenvector signs and column order is immaterial to the loss. The trial count \(L\) is a positive integer fixed when taking the \(\varepsilon\downarrow0\) asymptotic.

The pair is a canonical normalized representative of two Frobenius-orthogonal traceless real symmetric \(2\times2\) matrices: orthogonal conjugation acts by rotation on the two-dimensional space spanned by \(D\) and \(X\), taking the first normalized member to \(D\) and its orthogonal companion to \(\pm\varepsilon X\). This extends the displayed law, with the same normalization, to every such pair.

The input is genuinely nearly commuting: it is within Frobenius distance \(\sqrt2\varepsilon\) of the commuting family \(\{D,0\}\). The theorem studies the actual randomized output, not a perturbation bound for a fixed prescribed eigenbasis. \(R_L\) denotes the **square root** of the joint off-diagonal objective, not the forward eigenvector error.

## Proof

**1. Exact eigenbasis identity.** Let \(a=g_1\), \(b=\varepsilon g_2\), and \(B=aD+bX\). Then \(B^2=(a^2+b^2)I\). With probability one, \(a^2+b^2>0\), so the orthogonal eigenbasis of \(B\) is well-defined up to signs/order. For any traceless symmetric matrix \(C=dD+xX\), its diagonal entries in that eigenbasis are \(\pm(da+xb)/\sqrt{a^2+b^2}\). Orthogonal invariance of the Frobenius norm gives
\[
 \|\operatorname{offdiag}(Q^{\mathsf T}CQ)\|_F^2
 =2(d^2+x^2)-\frac{2(da+xb)^2}{a^2+b^2}.
\]
Apply this identity first to \(C=D\), then to \(C=\varepsilon X\). The resulting one-trial objective is
\[
 J=\frac{2(b^2+\varepsilon^2a^2)}{a^2+b^2}
 =2\varepsilon^2\frac{g_1^2+g_2^2}{g_1^2+\varepsilon^2g_2^2}.
\]
Writing \((g_1,g_2)=r(\cos\phi,\sin\phi)\), the angle \(\phi\) is uniform on the circle and independent of \(r>0\), and therefore
\[
 Z_1=\frac{1}{\sqrt{\cos^2\phi+\varepsilon^2\sin^2\phi}}.
\]

**2. The exact probability law and restarts.** For \(1<z<1/\varepsilon\), the event \(Z_1>z\) is equivalent to
\[
 |\cos\phi|<\sqrt{\frac{z^{-2}-\varepsilon^2}{1-\varepsilon^2}}.
\]
A uniformly distributed circle angle gives probability \(2\arcsin(c)/\pi\) for \(|\cos\phi|<c\). Independence of the Gaussian trials and selection of the smallest objective raise this survival probability to the power \(L\). This proves the displayed distribution, including both endpoint branches.

**3. First trial.** Circle averaging yields
\[
 \mathbb E Z_1^2=\frac2\pi\int_0^{\pi/2}
 \frac{dt}{\cos^2t+\varepsilon^2\sin^2t}=\varepsilon^{-1},
\]
by \(u=\tan t\). Hence \(\mathbb E R_1^2=2\varepsilon\). The corresponding integral for \(\mathbb E Z_1\) is \(2K(\sqrt{1-\varepsilon^2})/\pi\). The standard elementary endpoint asymptotic of the complete elliptic integral, \(K(\sqrt{1-\varepsilon^2})=\log(4/\varepsilon)+o(1)\), gives the first-moment assertion.

**4. General squared moments.** Put
\[
 T_\varepsilon(z)=\frac2\pi\arcsin\sqrt{\frac{z^{-2}-\varepsilon^2}{1-\varepsilon^2}}
 \quad(1<z<1/\varepsilon),
\]
with survival extensions \(T_\varepsilon(z)=1\) for \(z\le1\) and \(0\) for \(z\ge\varepsilon^{-1}\). The tail-integration identity gives, for every \(L\ge1\),
\[
 \mathbb E Z_L^2=1+2\int_1^{1/\varepsilon}z\,T_\varepsilon(z)^L\,dz.
\]
For every fixed \(z>1\), \(T_\varepsilon(z)\to T_0(z)=(2/\pi)\arcsin(1/z)\). Also \(0\le T_\varepsilon(z)\le T_0(z)\le1/z\) for \(z\ge1\). If \(L>2\), the integrand has integrable envelope \(2z^{1-L}\), so dominated convergence gives \(\mathbb E Z_L^2\to M_L\).

For \(L=2\), write \(z=e^s\). On any logarithmically long central range \(R\ll z\ll\varepsilon^{-1}\),
\[
 T_\varepsilon(z)=\frac{2+o(1)}{\pi z}
\]
uniformly after first choosing a sufficiently large fixed lower cutoff and a sufficiently small fixed fraction of the upper cutoff. Thus \(2zT_\varepsilon(z)^2\) has leading coefficient \(8/(\pi^2 z)\), and the two fixed-width endpoint ranges contribute lower order compared with \(\log(1/\varepsilon)\). More explicitly, the upper range \(\delta/\varepsilon\le z\le1/\varepsilon\) contributes at most \(2\log(1/\delta)\), because \(T_\varepsilon\le1/z\); the lower range \(1\le z\le R\) is bounded independently of \(\varepsilon\). Squeezing the central range and then letting \(R\uparrow\infty\), \(\delta\downarrow0\) gives
\[
 \lim_{\varepsilon\downarrow0}\frac{\mathbb E Z_2^2}{\log(1/\varepsilon)}
 =\frac8{\pi^2}.
\]
Multiplying by \(2\varepsilon^2\) yields the asserted two-trial coefficient.

For \(L=3\), substitute \(z=\csc t\) in \(M_3\) and integrate by parts twice:
\[
 M_3=\frac{24}{\pi^3}\int_0^{\pi/2}\frac{t^2}{\sin^2t}\,dt
 =\frac{24}{\pi^3}\cdot\pi\log2
 =\frac{24\log2}{\pi^2}.
\]
The boundary terms vanish where needed because the original integrand is integrable for \(L>2\).

**5. First moment of two trials.** The same tail identity gives \(\mathbb E Z_2=1+\int_1^{1/\varepsilon}T_\varepsilon(z)^2\,dz\). Dominated convergence applies since \(T_\varepsilon(z)^2\le z^{-2}\). Substituting \(z=\csc t\) and integrating by parts yields
\[
 \lim_{\varepsilon\downarrow0}\mathbb E Z_2
 =\frac8{\pi^2}\int_0^{\pi/2}\frac{t}{\sin t}\,dt
 =\frac{16G}{\pi^2}.
\]
For the final equality, integrate by parts using \(d[\log\tan(t/2)]/dt=1/\sin t\).

**6. Optimality comparison.** For an arbitrary real orthogonal rotation \(Q\) by angle \(\theta\), direct conjugation gives
\[
 J(Q)=2(\sin^2(2\theta)+\varepsilon^2\cos^2(2\theta)).
\]
Since \(0<\varepsilon<1\), its minimum is exactly \(2\varepsilon^2\). Consequently the ratio \(\mathbb E J_{\mathrm{selected}}/(2\varepsilon^2)\) diverges like \(\varepsilon^{-1}\) for one trial, like \((8/\pi^2)\log(1/\varepsilon)\) for two trials, and converges to the finite positive constant \(M_L\) for each fixed \(L\ge3\). This proves the sharp three-trial frontier.

## Verification

The self-contained file `verify_rjd.py` (Python standard library only) recomputes the one-trial objective using two independent algebraic routes: the exact eigenprojector/Frobenius identity with rational inputs and direct real orthogonal rotations. It tests the analytic survival law against deterministic uniform-angle enumeration; independently integrates the exact distribution to recover the single-trial mean and the asymptotic two- and three-trial constants. Execute from the extracted package directory with `python verify_rjd.py`.

Finite checks are reproducibility diagnostics only. The all-parameter distribution and asymptotic theorems are established analytically above; no random simulation is used as an infinite proof.

## Relationship to prior work

He and Kressner's *Randomized Joint Diagonalization of Symmetric Matrices* (first public arXiv version, 14 December 2022) defines exactly this Gaussian random-combination algorithm and the same summed squared off-diagonal Frobenius objective; its Algorithm 1 selects the best of independent trials. Theorems 6 and 8 prove high-probability robust recovery with failure bounds proportional to an inverse error-amplification factor, and Section 3.4 describes numerically observed sharpening with multiple trials. These foundational statements and the generic advantage of restarts are **not** claimed as new. The contribution here is a fully solved noncommuting two-matrix benchmark with an exact finite-noise loss distribution, explicit first- and second-moment constants, and a proved sharp minimal trial count for optimal-order mean-square error. The general high-probability upper bounds do not specify these exact expectations or furnish this matching necessity example.

He and Kressner's later work on *simultaneous diagonalization by congruence* uses two weighted combinations and a generalized eigenvalue pencil, not the orthogonal one-combination RJD experiment analyzed here. Li, Lu, and Yu's *Vector-wise Joint Diagonalization of Almost Commuting Matrices* instead constructs approximate joint eigenvectors through manifold optimization. These methods have related goals but their claimed conclusions do not give the present loss distribution. Search and comparison cannot exclude an unpublished or differently formulated equivalent.

## Limitations

This is a sharp exact benchmark for a fixed dimension-two, two-matrix input family. It does not assert the same trial-count frontier for arbitrary near-commuting families, higher dimensions, complex random coefficients, non-Gaussian sampling, forward eigenvector errors, or finite-precision solvers. The ratio is asymptotic as the noise magnitude tends to zero with the number of trials fixed; the theorem does not optimize total runtime or the distribution of non-Gaussian trial weights. The originality assessment is best-knowledge rather than an independent priority certification.

## References

- H. He and D. Kressner, *Randomized Joint Diagonalization of Symmetric Matrices*, arXiv:2212.07248 (first submitted 14 December 2022); SIAM Journal on Matrix Analysis and Applications 45 (2024), 661–684. https://arxiv.org/abs/2212.07248
- H. He and D. Kressner, *A randomized algorithm for simultaneously diagonalizing symmetric matrices by congruence*, arXiv:2402.16557 (first submitted 26 February 2024). https://arxiv.org/abs/2402.16557
- B. Li, J. Lu, and Z. Yu, *Vector-wise Joint Diagonalization of Almost Commuting Matrices*, arXiv:2205.15519 (first submitted 31 May 2022). https://arxiv.org/abs/2205.15519
