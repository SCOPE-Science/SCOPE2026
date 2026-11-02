# Infinite-mean Gaussian momentum coefficients with bounded adaptive-heavy-ball iterates

## Finding

Consider the exact adaptive stochastic heavy-ball method (ASHBM) of Zeng--Han--Su--Xie, applied to the consistent identity system \(Ax=b\) with \(A=I_n\), \(b=0\), any deterministic \(x^0\ne0\), and \(n\ge2\). Take the rank-one sketches \(S_0,S_1\) to be independent \(N(0,I_n)\) vectors. Use the method's prescribed initial basic step and its *uncapped* optimal two-parameter ASHBM update at the second step. Write \(\alpha_1\) for the adaptive step and \(\beta_1\) for the adaptive momentum coefficient, and put \(k=n-1\).

All steps and coefficients are well defined almost surely. The exact distribution is \(\alpha_1^{-1}\sim\chi^2_k\). Thus, for every \(p>0\),
\[
\mathbb E[\alpha_1^p]=
\begin{cases}
2^{-p}\Gamma(k/2-p)/\Gamma(k/2),&0<p<k/2,\\
+\infty,&p\ge k/2.
\end{cases}
\]
The adaptive momentum has infinite absolute first moment **in every dimension**:
\[
\mathbb E|\beta_1|^p=
\begin{cases}
\displaystyle\frac{\Gamma((1-p)/2)\Gamma((p+1)/2)^2\Gamma((k-p)/2)}{\pi^{3/2}\Gamma(k/2)},&0<p<1,\\
+\infty,&p\ge1.
\end{cases}
\]
In dimension two, \(|\beta_1|\) is exactly the product of two independent absolute standard Cauchy variables. In particular, \(\mathbb E\sqrt{|\beta_1|}=2\) but \(\mathbb E|\beta_1|=\infty\).

Despite these nonintegrable *coefficients*, the optimizer output is an orthogonal projection and cannot grow:
\[
x^2=(I-P_{\operatorname{span}\{S_0,S_1\}})x^0,
\qquad \|x^2\|_2\le\|x^1\|_2\le\|x^0\|_2.
\]
Indeed,
\[
\mathbb E\|x^2\|_2^2=\frac{n-2}{n}\|x^0\|_2^2,
\]
where the right side is zero for \(n=2\). The analogous two independent steps of the no-momentum basic projection method have expected squared error \(((n-1)/n)^2\|x^0\|_2^2\). Thus ASHBM improves this exact two-step expected error by \(\|x^0\|_2^2/n^2\) while its separately represented momentum coefficient has no first absolute moment.

## Assumptions and scope

The system is \(I_nx=0\) over \(\mathbb R^n\), with integer \(n\ge2\) and nonzero deterministic starting state. All arithmetic is exact. Each rank-one sketch is a full unnormalized real Gaussian vector, with independent standard normal coordinates; the first two sketches are independent. This distribution has positive definite sketch covariance and satisfies the underlying method's nonzero-sketch condition almost surely. At iteration zero, the method uses the exact basic projection step with relaxation parameter one; iteration one uses the uncapped adaptive coefficients from equation (17) of Zeng--Han--Su--Xie. No claim is made for capped, regularized, finite-precision, or different-sketch implementations.

For a nonzero vector \(v\), let \(P_v=vv^\top/\|v\|_2^2\) be orthogonal projection onto its span. For a subspace \(L\), let \(P_L\) denote its orthogonal projector. For \(p>0\), divergent moments have value \(+\infty\) in the extended-real sense. The coefficient \(\beta_1\) is symmetric but has no Lebesgue expectation because its absolute first moment diverges.

## Proof

**1. Reconstructing the exact algorithm.** Write \(s=S_0\), \(z=S_1\), \(d=x^1-x^0\), and \(g=(z^\top x^1)z\). Since the first step is the exact one-row projection,
\[
x^1=x^0-\frac{s^\top x^0}{\|s\|_2^2}s,
\quad d=-\frac{s^\top x^0}{\|s\|_2^2}s,
\quad \langle x^1,d\rangle=0.
\]
For the identity system, the paper's second-step coefficients are
\[
\alpha_1=\frac{\|d\|_2^2(z^\top x^1)^2}{\|g\|_2^2\|d\|_2^2-\langle g,d\rangle^2},
\qquad
\beta_1=\frac{\langle g,d\rangle(z^\top x^1)^2}{\|g\|_2^2\|d\|_2^2-\langle g,d\rangle^2},
\]
and \(x^2=x^1-\alpha_1g+\beta_1d\). A nonzero deterministic \(x^0\) is almost surely neither parallel nor perpendicular to \(s\), so both \(x^1\) and \(d\) are nonzero. The second sketch is almost surely neither perpendicular to \(x^1\) nor parallel to \(d\); consequently the displayed denominator is nonzero almost surely.

**2. Exact scalar reduction and cancellation.** Set \(e=d/\|d\|_2\) and \(v=x^1/\|x^1\|_2\). They are orthonormal. By rotation invariance of the second Gaussian sketch,
\[
z=Ze+Uv+V,
\]
where \(Z,U\) are independent standard normals, \(V\) is independent Gaussian in the \((n-2)\)-dimensional orthogonal complement, and \(V=0\) when \(n=2\). Put \(W=Uv+V\), \(Y=\|W\|_2^2\), \(t=\|x^1\|_2\), \(r=\|d\|_2\). Substitution and cancellation give
\[
\boxed{\alpha_1=Y^{-1},\qquad \beta_1=(t/r)ZU/Y,\qquad
x^2=x^1-(tU/Y)W.}
\]
Since \(Y>0\) almost surely, the formulas are valid. The last is exactly projection of \(x^1\) onto \(W^\perp\). As \(W\perp s\), it also equals projection of \(x^0\) onto \(\operatorname{span}\{s,z\}^\perp\), establishing both norm inequalities. Notice that the individual terms \(-\alpha_1g\) and \(\beta_1d\) have potentially unbounded coefficients although their components along \(e\) cancel exactly.

**3. The step-size moment threshold.** The vector \(W\) is standard Gaussian in \(k=n-1\) dimensions. Thus \(Y\sim\chi_k^2\), independently of the first sketch. Integrating its gamma density proves the stated inverse-chi-square moment formula; the integral at zero converges precisely for \(p<k/2\).

**4. The unconditional momentum moment threshold.** Rotate the *first* sketch relative to the fixed direction \(x^0/\|x^0\|_2\), writing \(s=G_0(x^0/\|x^0\|_2)+G_\perp\), with \(G_0\sim N(0,1)\), \(G_\perp\sim N(0,I_k)\), independent. Projection geometry yields
\[
\frac{t}{r}=\frac{\|G_\perp\|_2}{|G_0|}.
\]
The first-sketch factor is independent of \(Z,U,W\). Let \(R=\|W\|_2\), and let \(T=U/R\) denote the first coordinate of its uniform spherical direction. Then \(R\sim\chi_k\), \(T\) is independent of \(R\), and \(|ZU/Y|=|Z||T|/R\). For \(0<p<\min(1,k)\), use independent factors and the familiar gamma integrals
\[
\mathbb E|G_0|^{-p}=\frac{2^{-p/2}\Gamma((1-p)/2)}{\sqrt\pi},\quad
\mathbb E\|G_\perp\|_2^p=\frac{2^{p/2}\Gamma((k+p)/2)}{\Gamma(k/2)},
\]
\[
\mathbb E|Z|^p=\frac{2^{p/2}\Gamma((p+1)/2)}{\sqrt\pi},\quad
\mathbb E|T|^p=\frac{\Gamma(k/2)\Gamma((p+1)/2)}{\sqrt\pi\Gamma((k+p)/2)},
\quad
\mathbb ER^{-p}=\frac{2^{-p/2}\Gamma((k-p)/2)}{\Gamma(k/2)}.
\]
Multiplication and cancellation give the stated expression for \(\mathbb E|\beta_1|^p\) when \(0<p<1\). For every \(p\ge1\), \(\mathbb E|G_0|^{-p}=+\infty\), and the independent remaining positive factor is almost surely nonzero; Tonelli's theorem proves \(\mathbb E|\beta_1|^p=+\infty\). When \(n=2\), both \(\|G_\perp\|_2/|G_0|\) and \(Z/U\) have absolute standard Cauchy laws and are independent, giving the stated product law and its \(p=1/2\) moment.

**5. Output accuracy.** Because the two independent Gaussian vectors span a uniformly random two-plane in \(\mathbb R^n\), rotational invariance and trace of its projector yield \(\mathbb E\|P_{\operatorname{span}\{s,z\}}x^0\|_2^2=(2/n)\|x^0\|_2^2\). Pythagoras gives the expected error \((n-2)/n\). For the basic method, a single independent standard Gaussian projection reduces conditional squared error by the factor \((n-1)/n\), hence two consecutive steps have factor \(((n-1)/n)^2\). The difference is exactly \(1/n^2\) times the starting squared norm. This completes the proof.

## Verification

The supplied `verify_ashbm.py` reconstructs the paper's second-step coefficient formulas independently of the reduced Gaussian-frame formulas, compares the two over 1,000 seeded random first/second sketch pairs across dimensions \(2,3,4,8\), and checks the exact two-dimensional termination property. Six independent Gaussian Monte Carlo runs compare finite fractional coefficient moments to the closed forms, with divergent step-size moments explicitly excluded from finite-moment comparisons. The check succeeds with Python 3, NumPy and SciPy by executing `python verify_ashbm.py` in the package's file directory. These finite checks corroborate algebra but do not prove any moment threshold; the proof above uses gamma-density integrals and Tonelli's theorem.

## Relationship to prior work

Zeng--Han--Su--Xie introduced the adaptive stochastic heavy-ball scheme and its two-parameter projection representation. Their equation (17) and Algorithm 3 are assumed without modification. Their convergence analysis and equivalence to a stochastic conjugate-gradient formulation are established work, not claimed here. The new statement concerns the **exact distributions and critical integrability exponents of the coefficients** under Gaussian rank-one sampling, contrasted with the exactly bounded and quantifiably improving update in the same experiment. The random coefficients are not the deterministic Polyak heavy-ball coefficients studied by Goujaud--Taylor--Dieuleveut, nor the fixed-parameter stochastic momentum in Loizou--Richtárik. The usual inverse-chi-square and Gaussian-ratio laws are classical ingredients; applying them to the *specific published adaptive coefficients*, including the first-sketch dependence of momentum, establishes the combined phenomenon. Priority over all earlier formulations is not independently certified.

## Limitations

Only two exact iterations of the stated identity-system ASHBM with independent unnormalized Gaussian rank-one sketches are analyzed. The bounds do not assert heavy-tailed *optimizer iterates*, loss divergence, practical finite-precision instability, or universal behavior for nonidentity matrices. The coefficient integrability results are in exact arithmetic; finite-precision consequences require separate analysis. The two-dimensional termination and squared-error improvement rely on orthogonal projection structure already implicit in the original algorithm. The paper's general convergence guarantees are not strengthened here. No independent scientific audit has been performed.

## References

1. Y. Zeng, D. Han, Y. Su, J. Xie, *On adaptive stochastic heavy ball momentum for solving linear systems*, arXiv:2305.05482, first version 9 May 2023; SIAM Journal on Matrix Analysis and Applications 45 (2024), 1259--1286. Algorithm 3, equation (17), and Section 5.
2. B. Goujaud, A. Taylor, A. Dieuleveut, *Quadratic minimization: from conjugate gradient to an adaptive heavy-ball method with Polyak step-sizes*, arXiv:2210.06367 (2022), Sections 1--2.
3. N. Loizou, P. Richtárik, *Momentum and stochastic momentum for stochastic gradient, Newton, proximal point and subspace descent methods*, arXiv:1712.09677 (2017), Sections 1--4.
