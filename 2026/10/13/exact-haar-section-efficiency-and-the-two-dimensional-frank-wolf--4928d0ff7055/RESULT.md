# Exact Haar-section efficiency and the two-dimensional Frank–Wolfe threshold

## Finding
For a random orthogonal \(d\)-dimensional section of \(\mathbb R^n\), \(n\ge2\), the **best possible uniform expected fraction** of the full Frank–Wolfe linear-oracle gap retained on the Euclidean unit ball is
\[
\boxed{c_{n,d}=\frac{d-1}{n-1}},\qquad 1\le d\le n.
\]
The infimum is approached when the gradient and inward boundary-normal directions coalesce. Thus two random section dimensions suffice for strictly positive universal expected progress, while a one-dimensional section has zero uniform expected-progress infimum. The same exact coefficient yields an improved expected-oracle guarantee, and hence improved open-loop sublinear bounds, for the strongly convex feasible sets considered in [1].

An equivalent **sharp projection-norm estimate**, valid for all pairs \(u,v\) of unit vectors, is
\[
\mathbb E_P\bigl(\|Pu\|-\|Pv\|\bigr)^2
\le \frac{n-d}{n(n-1)}\,\|u-v\|^2.
\tag{1}
\]
The coefficient in (1) cannot be reduced. It improves the squared-difference constant in [1, Corollary 4] by a factor of four and extends the estimate to \(d=1,2\).

## Assumptions and scope
Fix integers \(n\ge2\) and \(1\le d\le n\). Let \(P\in\mathbb R^{d\times n}\) be distributed according to Haar measure on the Stiefel manifold of **row-orthonormal** matrices, with \(PP^\top=I_d\). Put \(\Pi=P^\top P\), an orthogonal projector satisfying \(\Pi^2=\Pi\) and \(\operatorname{tr}\Pi=d\). Expectations are only over the sampled projector. For unit \(u,v\) with \(\rho=\langle u,v\rangle<1\), define the source's ball-section efficiency
\[
\Gamma(P;u,v)=\frac{\|Pu\|\|Pv\|-\langle Pu,Pv\rangle}{1-\rho}.
\tag{2}
\]
It is well-defined even when an individual projected vector vanishes; a denominator involving a projected norm is never used in (2). The geometry is Euclidean and real; no anisotropic or non-Haar distribution is covered.

For the exact ball-oracle formulation, let \(C=\{z\in\mathbb R^n:\|z\|\le1\}\), choose a boundary iterate \(x=-v\), and choose the linear convex objective \(f(z)=\langle u,z\rangle\). The full linear-oracle gap is \(\Delta_C(x)=1-\rho>0\). The random section is the feasible slice \(C\cap(x+\operatorname{range}(P^\top))\), with exact linear minimization inside this slice. For a general strongly convex set the transfer below additionally uses precisely the set and objective assumptions of [1]: compact strongly convex \(C\) with \(C^2\) boundary and a positive uniform interior rolling-ball radius, convex differentiable \(f\) with \(L\)-Lipschitz gradient, independent Haar sections, and exact section linear oracles.

## Proof
**1. A norm-difference identity.** Write \(F_P(z)=\|Pz\|\) for unit \(z\). Orthogonal invariance and trace give \(\mathbb E\Pi=(d/n)I_n\). The elementary polarization identity
\[
2\|Pu\|\|Pv\|=\|Pu\|^2+\|Pv\|^2-\bigl(F_P(u)-F_P(v)\bigr)^2
\]
therefore gives
\[
\mathbb E\Gamma(P;u,v)=\frac dn-\frac{\mathbb E\bigl(F_P(u)-F_P(v)\bigr)^2}{2(1-\rho)}.
\tag{3}
\]
Thus sharpness of the desired lower bound reduces to the sharp mean-square chordal contraction (1).

**2. A sharp chordal translation inequality on each great circle.** Choose orthogonal unit \(u,w\). For any \(\theta\in(0,\pi]\), put \(v=\cos\theta\,u+\sin\theta\,w\), and define the periodic function
\[
h_P(t)=\|P(\cos t\,u+\sin t\,w)\|.
\]
Since the norm and projector are nonexpansive, \(h_P\) is \(1\)-Lipschitz on the circle and hence belongs to periodic \(H^1\). For its Fourier coefficients \(a_k\), Parseval and the elementary telescoping inequality \(\lvert e^{ik\theta}-1\rvert\le\lvert k\rvert\lvert e^{i\theta}-1\rvert\) for every integer \(k\) yield
\[
\begin{aligned}
\frac1{2\pi}\int_0^{2\pi}\bigl|h_P(t+\theta)-h_P(t)\bigr|^2\,dt
&=\sum_{k\in\mathbb Z}|a_k|^2|e^{ik\theta}-1|^2\\
&\le 2(1-\cos\theta)\sum_{k\in\mathbb Z}k^2|a_k|^2\\
&=2(1-\cos\theta)\frac1{2\pi}\int_0^{2\pi}|h'_P(t)|^2\,dt.
\end{aligned}
\tag{4}
\]
Here the telescoping inequality follows by expressing \(e^{ik\theta}-1\) as a sum of \(\lvert k\rvert\) complex numbers of modulus \(\lvert e^{i\theta}-1\rvert\); the negative-\(k\) case follows by conjugation. This also proves (4) for nonsmooth norm curves by \(H^1\) approximation.

**3. The expected squared tangential derivative.** For almost every \(P\), \(Pu\ne0\) and
\[
h'_P(0)=\frac{\langle Pu,Pw\rangle}{\|Pu\|}
=\frac{\langle\Pi u,w\rangle}{\sqrt{\langle\Pi u,u\rangle}}.
\tag{5}
\]
Take any orthonormal basis \(w_1,\ldots,w_{n-1}\) of \(u^\perp\). By rotational invariance each \(\mathbb E\bigl(h'_P(0)\bigr)^2\), with \(w=w_j\), has the same value. The projection identity \(\Pi^2=\Pi\) gives, almost surely,
\[
\begin{aligned}
\sum_{j=1}^{n-1}\frac{\langle\Pi u,w_j\rangle^2}{\langle\Pi u,u\rangle}
&=\frac{\|\Pi u\|^2-\langle\Pi u,u\rangle^2}{\langle\Pi u,u\rangle}\\
&=1-\langle\Pi u,u\rangle.
\end{aligned}
\]
Taking expectations and using \(\mathbb E\langle\Pi u,u\rangle=d/n\) proves the **exact** derivative moment
\[
\mathbb E|h'_P(0)|^2=\frac{1-d/n}{n-1}=\frac{n-d}{n(n-1)}.
\tag{6}
\]
Right-Haar invariance under every ambient rotation of the plane \(\operatorname{span}\{u,w\}\) makes \(\mathbb E|h_P(t+\theta)-h_P(t)|^2\) and \(\mathbb E|h'_P(t)|^2\) independent of \(t\). Integrate (4), average over \(P\), and insert (6) to get
\[
\mathbb E\bigl(F_P(u)-F_P(v)\bigr)^2\le
2(1-\cos\theta)\frac{n-d}{n(n-1)}=
\frac{n-d}{n(n-1)}\|u-v\|^2.
\tag{7}
\]
Every distinct unit pair admits this great-circle representation; antipodal pairs use any orthogonal \(w\).

**4. Sharpness including all dimensions.** Fix orthogonal unit \(u,w\), let \(v_\theta=\cos\theta\,u+\sin\theta\,w\), and send \(\theta\downarrow0\). For almost every \(P\), differentiability in (5) gives
\[
\frac{\bigl(F_P(v_\theta)-F_P(u)\bigr)^2}{\|v_\theta-u\|^2}\longrightarrow |h'_P(0)|^2.
\]
The quotient is at most \(1\) since \(F_P\) is \(1\)-Lipschitz in its Euclidean argument. Dominated convergence and (6) show that (7) is sharp as a **supremum**. Substituting (7) into (3) gives
\[
\mathbb E\Gamma(P;u,v)\ge \frac dn-\frac{n-d}{n(n-1)}=\frac{d-1}{n-1}.
\]
The same coalescing family attains this bound in the limit. For \(d=n\), the random projector is the identity and the bound is attained for every distinct pair; for \(d=1\), the sharp infimum is zero.

**5. Exact optimality for the ball linear oracle.** Let \(x=-v\in\partial C\) and \(f(z)=\langle u,z\rangle\). Parameterize feasible section points by \(y=-v+P^\top z\), \(z\in\mathbb R^d\). The ball constraint is \(\|z-Pv\|\le\|Pv\|\). The minimizer of \(\langle Pu,z\rangle\) over that ball is \(z=Pv-\|Pv\|Pu/\|Pu\|\), with the trivial \(Pu=0\) case treated separately. Consequently
\[
\Delta_{\mathrm{section}}(x)=\|Pu\|\|Pv\|-\langle Pu,Pv\rangle
=\Gamma(P;u,v)\,\Delta_C(x).
\tag{8}
\]
Since every \(u,v\) corresponds to an admissible ball/linear-objective pair, no uniform expected-oracle factor greater than \((d-1)/(n-1)\) is valid even within smooth convex linear objectives on Euclidean balls. This provides an optimization lower-bound witness, not just an angular calculation.

**6. General-set expected-rate consequence (existing geometric premises).** Proposition 3 of [1] shows, via an interior comparison ball and the three center/interior/boundary cases, that **any** uniform \(c_{n,d}\) in (2) yields the conditional Frank–Wolfe expected-oracle inequality
\[
\mathbb E[\langle\nabla f(x_k),s_k-x_k\rangle\mid x_k]\le
-\beta\,\Delta_C(x_k),\qquad
\beta=\kappa_{\mathrm{unif}}c_{n,d},\quad
\kappa_{\mathrm{unif}}=\min\{2\beta_C R_{\min},R_{\min}/D\}.
\tag{9}
\]
Here \(D\) is the diameter of \(C\), and \(\beta_C,R_{\min}\) are respectively the source's strong-set-convexity parameter and uniform interior rolling-ball radius. The boundary case is (8) applied to the comparison ball; the center case uses \(\mathbb E\|Pu\|\ge\mathbb E\|Pu\|^2=d/n\ge c_{n,d}\); and the interior case is the convex-combination inequality from [1, Lemma 7] between those two terms. Thus replacing \(c_{n,d}\) by the newly proved sharp \((d-1)/(n-1)\) is valid for all \(d\ge2\). Under the source's original assumptions, its smoothness/FW-gap recursion
\[
a_{k+1}\le(1-\alpha_k\beta)a_k+\frac{LD^2}{2}\alpha_k^2,
\qquad a_k=\mathbb E[f(x_k)-f^*],
\]
with \(\alpha_k=2/(\beta k+2)\), implies by induction
\[
a_k\le \frac{M}{k+2/\beta},\qquad
M=\max\left\{\frac{2a_0}{\beta},\frac{2LD^2}{\beta^2}\right\}.
\tag{10}
\]
This is an improvement and extension **only of the expected-oracle/open-loop argument**. No claim of a sharp general-set \(\kappa_{\mathrm{unif}}\) or of improvement to high-probability or short-step constants is made.

## Verification
The analytic proof requires only the Stiefel projection identity, Haar invariance, periodic Fourier Parseval, a telescoping bound, and dominated convergence. The accompanying `verify.py` checks the exact rational identity \(d/n-(n-d)/(n(n-1))=(d-1)/(n-1)\) for all \(2\le n\le200\) and \(1\le d\le n\); it also performs seeded Gaussian-orthogonal-frame Monte Carlo diagnostics in four dimensions. Running `python3 verify.py` produces `VERIFY_OK`. The finite numerical tests are diagnostics only; they do not replace Steps 1–6. In particular, no simulation establishes an all-dimensions inequality.

## Relationship to prior work
Poirion, Pokutta and Takeda [1, Proposition 1] give, for \(d\ge3\), the weaker estimate \(d/n-4(n-d)/(n(n-1))\le\mathbb E\Gamma\le d/n\), and [1, Proposition 7] gives \((d-1)/(96(n-1))\) for \(d\ge2\). The paper's Corollary 4 bounds the squared norm difference with four times the coefficient in (1), while its Proposition 3 and Theorem 1 explicitly admit any improved uniform expected section constant. None of these source statements supplies the exact infimum or its coalescing-angle sharpness. The result is not a reparameterization: the new Fourier-chordal mechanism identifies the optimal constant and reaches \(d=2\).

Kang and Oh [2] study random **normalized** spherical projections and establish expected geodesic-angle preservation. Their random angle is not the product-of-projected-norms weighted, unnormalized ball-oracle expression (2), and their angular expectation theorem does not imply (1) or the sharp Frank–Wolfe oracle guarantee. Classical Haar projection moments underpin (6), but (7) and the optimal oracle reduction (8) are the additional statements at issue.

## Limitations
The coefficient is sharp for the uniform comparison-ball efficiency and the corresponding exact boundary-ball linear oracle; it need not be the sharp expected rate factor for an arbitrary nonlinear feasible set. The infimum is established as a limit of nearby distinct directions and is not claimed to be realized at any separated pair when \(d<n\). The general-set rate transfer retains all source assumptions and the source geometric factor. No high-probability, almost-sure, short-step, inexact-subspace-oracle, non-Haar, or nonconvex-objective extension follows from this claim. Published and indexed-source comparison cannot exclude unindexed equivalent earlier work, and independent validation has not been performed.

## References
[1] P.-L. Poirion, S. Pokutta, A. Takeda, *Random-Subspace Frank--Wolfe over Strongly Convex Sets*, arXiv:2605.24819v1, first public 2026-05-24, https://arxiv.org/abs/2605.24819v1 . Main definitions and Proposition 1, Proposition 3, Theorem 1, Corollary 4, and Proposition 7 were inspected in the openly available complete preprint text, https://www.researchgate.net/publication/405263865_Random-Subspace_Frank--Wolfe_over_Strongly_Convex_Sets .

[2] S. Kang and H.-S. Oh, *Spherical random projection*, Journal of the Royal Statistical Society Series B 86 (2024), 1364–1382, doi:10.1093/jrsssb/qkae035, https://academic.oup.com/jrsssb/article/86/5/1364/7642961 . Theorem 3.1 and its normalization and distributional setting were inspected.
