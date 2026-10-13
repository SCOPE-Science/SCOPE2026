# Exact admissibility and sharp rank-correlation ranges for the two-mode Legendre copula

## Finding

Consider the bivariate polynomial family introduced as equation (25) in [1]:
\[
 C_{\lambda_1,\lambda_2}(u,v)=uv+3\lambda_1 f(u)f(v)+5\lambda_2 g(u)g(v),
 \quad 0\le u,v\le1,
\]
where \(f(u)=u(1-u)\) and \(g(u)=2u^3-3u^2+u\). Write \(a=3\lambda_1\), \(b=5\lambda_2\), and define
\[
 H(b)=\begin{cases}
 1+b,&-1\le b\le\tfrac12,\\
 \sqrt{3b(2-b)},&\tfrac12\le b\le2.
 \end{cases}
\]
**The exact, necessary-and-sufficient admissibility criterion** is
\[
 \boxed{C_{\lambda_1,\lambda_2}\text{ is a copula}\ \Longleftrightarrow\ -1\le b\le2\text{ and }|a|\le H(b).}
\]
All boundary values are included. Over this entire family, Spearman's rho and Kendall's tau are exactly
\[
 \rho_S=\frac a3=\lambda_1,\qquad
 \tau=\frac{2a}{9}\left(1+\frac b{25}\right)
 =\frac{2\lambda_1}{3}\left(1+\frac{\lambda_2}{5}\right).
\]
In particular their sharp attainable ranges are
\[
 \boxed{|\rho_S|\le\frac1{\sqrt3}}\qquad\text{and}\qquad
 \boxed{|\tau|\le T_*:=\frac29\sqrt{3b_*(2-b_*)}
 \left(1+\frac{b_*}{25}\right)},
\]
where \(b_*=(\sqrt{171}-11)/2\) and \(T_*=0.40059171855462555\ldots\). The Spearman extrema occur precisely at \((a,b)=(\pm\sqrt3,1)\); the Kendall extrema occur precisely at \((a,b)=(\pm H(b_*),b_*)\), with the sign chosen accordingly. This is a classification for this **specified two-mode polynomial family only**.

## Assumptions and scope

Parameters \(\lambda_1,\lambda_2\) are arbitrary **real** numbers before imposing admissibility; no external sufficient triangle or sign restriction is assumed. A copula means a two-increasing cumulative distribution function on the unit square with both one-dimensional marginals uniform. The family has a continuous mixed derivative and already satisfies \(C(u,0)=C(0,v)=0\), \(C(u,1)=u\), \(C(1,v)=v\) for all parameter values. Therefore, it is a copula exactly when its continuous density \(\partial_u\partial_v C\) is nonnegative throughout the square.

Set \(x=2u-1\), \(y=2v-1\), and \(P_2(t)=(3t^2-1)/2\). Then
\[
 c(u,v)=1+a xy+b P_2(x)P_2(y),\qquad -1\le x,y\le1.
\]
The factors \(x\) and \(P_2(x)\) each integrate to zero under the uniform distribution on \([-1,1]\). Thus any nonnegative member already has unit uniform marginal densities.

## Proof

**Step 1: eliminate impossible second-mode parameters.** At \((x,y)=(1,1)\) and \((-1,1)\), nonnegativity forces \(1+b-|a|\ge0\), hence \(b\ge-1\). At \((x,y)=(1,0)\), it forces \(1-b/2\ge0\), hence \(b\le2\). Conversely, for \(-1\le b\le2\), the part \(1+bP_2(x)P_2(y)\) is nonnegative everywhere: \(P_2\in[-1/2,1]\), so the product lies in \([-1/2,1]\). This also verifies the axes \(xy=0\), where the first-mode term vanishes.

**Step 2: minimize the exact coefficient allowance.** Fix \(b\in[-1,2]\). Because \(P_2\) is even and the signs of \(x\) and \(y\) can be independently reversed, simultaneous nonnegativity for \(xy\ne0\) is equivalent to
\[
 |a|\le \inf_{0<s,t\le1}
 Q_b(s,t),\qquad Q_b(s,t):=
 \frac{1+bP_2(s)P_2(t)}{st}.
\]
Let \(w=st\) and \(R=s/t+t/s\). For each \(0<w\le1\), the feasible interval is \(2\le R\le w+w^{-1}\), with the lower bound at \(s=t=\sqrt w\) and the upper bound at \((s,t)=(1,w)\) or its transpose. Exact expansion gives
\[
 Q_b=\frac{1+b/4}{w}+\frac{9b}{4}w-\frac{3b}{4}R.
\]
For \(-1\le b\le0\), the coefficient of \(R\) is nonnegative. The minimum at fixed \(w\) is therefore attained at \(R=2\), giving
\[
 q_-(w)=\frac{1+b/4}{w}+\frac{9b}{4}w-\frac{3b}{2}.
\]
Its derivative \(-(1+b/4)/w^2+9b/4\) is strictly negative, including \(b=-1\). Thus the global minimum is \(q_-(1)=1+b\).

For \(0\le b\le2\), the coefficient of \(R\) is nonpositive, so the minimum at fixed \(w\) occurs at \(R=w+w^{-1}\), giving
\[
 q_+(w)=\frac{1-b/2}{w}+\frac{3b}{2}w.
\]
When \(0\le b\le1/2\), this function decreases on \((0,1]\), so its minimum is \(1+b\). When \(1/2<b<2\), the unique minimizing product is
\[
 w_b=\sqrt{\frac{2-b}{3b}}\in(0,1),
\]
and the minimum is \(2\sqrt{(1-b/2)(3b/2)}=\sqrt{3b(2-b)}\). At \(b=2\), \(q_+(w)=3w\) and its infimum is zero as \(w\downarrow0\); \(a=0\) is both necessary and sufficient. This proves exactly the piecewise bound \(|a|\le H(b)\), with no hidden open boundary conditions.

The necessity is constructive. If \(b\le1/2\) and \(|a|>H(b)\), the sign-opposed corner \((x,y)=(1,-\operatorname{sgn}a)\) makes the density negative. If \(1/2<b<2\), the point \((x,y)=(1,-\operatorname{sgn}(a)w_b)\) makes it negative. If \(b=2\), any \(a\ne0\) makes it negative for sufficiently small opposite-signed \(y\). This establishes sharpness of every boundary arc.

**Step 3: compute the two rank correlations from their definitions.** The Spearman formula \(\rho_S=12\int_0^1\!\int_0^1 C\,du\,dv-3\) directly yields \(\lambda_1\), because \(\int_0^1 f=1/6\) and \(\int_0^1 g=0\). Kendall's formula is \(\tau=4\int_0^1\!\int_0^1 C\,c\,du\,dv-1\). Polynomial expansion gives a linear term \(2\lambda_1/3\), vanishing pure quadratic terms, and a mixed contribution \(2\lambda_1\lambda_2/15\). Indeed
\[
 \int_0^1 f(u)g'(u)\,du=-\frac1{30},\quad
 \int_0^1 g(u)f'(u)\,du=\frac1{30},
\]
so the mixed contribution is \(4(2)(3)(5)\lambda_1\lambda_2(1/30)^2=2\lambda_1\lambda_2/15\). The identities follow for every parameter pair; the copula condition is needed only for interpreting them as rank correlations.

**Step 4: optimize exactly.** Because \(1+b/25>0\) throughout \([-1,2]\), maxima of absolute rank correlations occur at \(|a|=H(b)\). The largest \(H(b)\) is \(\sqrt3\), uniquely at \(b=1\), proving the Spearman bound. For Kendall, \(H(b)(1+b/25)\) increases through \([-1,1/2]\). On \((1/2,2)\) its derivative has the sign of \(25-22b-2b^2\), which has precisely one zero in that interval: \(b_*=(\sqrt{171}-11)/2\). The derivative switches from positive to negative there; endpoints are smaller. This proves the sharp Kendall bound and all extremizers.

## Verification

Run `python3 verify.py` in a directory containing the supplied standalone script. It uses only Python's standard library. It exactly integrates the bivariate polynomials over rational coefficients, verifies the rank-correlation polynomial identities on the six nodes determining every total-degree-two polynomial in the parameters, and checks density coefficients and normalization. It also runs 33,371 deterministic numerical positivity and sharpness probes across the complete parameter interval, and checks the algebraic critical-point relation. The observed final line is `VERIFICATION_OK`. The finite probes are **not** an exhaustive certificate for all real parameters; that continuum conclusion follows from Steps 1–4 of the proof.

## Relationship to prior work

Longla [1], first public on 21 August 2023, introduces exactly this two-term family in equation (25), with a sufficient coefficient condition \(3|\lambda_1|+5|\lambda_2|\le1\), and discusses Spearman and Kendall association. The same full formula appears in the revised preprint [2] and the open-access 2024 publication [3]. The later paper of Longla and Mous-Abou Hamadou [4] specifies a larger but still linear sufficient subregion with \(|\lambda_1|\le1/3\); this does not supply the exact nonlinear admissibility boundary. A subsequent multivariate extension [5] uses a sufficient absolute-coefficient constraint and contains the two-term bivariate structure as a special case, without a necessary-and-sufficient two-parameter boundary. The 2026 article [6] treats 1-dependent **cross-mode** copulas rather than the diagonal two-mode density considered here.

In contrast, the criterion above holds **if and only if** throughout the entire real parameter plane and makes the valid point \((\lambda_1,\lambda_2)=(1/\sqrt3,1/5)\) explicit. This contradicts treating the earlier sufficient Spearman bound \(1/3\) as a bound for the full polynomial family. The Kendall identity here is obtained by direct integration of equation (25); equation (26) displayed in [1] and [3] is algebraically different from that integral. The present proof does not rely on that displayed expression. Published searches for equivalent formulations, polynomial-density positivity domains, and rank-correlation extrema disclosed no complete covering theorem; a previously unnoticed equivalent calculation remains possible.

## Limitations

This result is confined to the fixed bivariate polynomial family with exactly the first two **diagonal** shifted-Legendre terms. It does not classify copulas with additional higher-degree or cross-mode terms, determine their statistical efficiency, or establish any confidence-interval or mixing theorem. Correlation extrema do not characterize all rank-correlation pairs. The formula for Kendall's tau is proven for the explicitly defined polynomial, not asserted to correct every related parameterization. Published-priority assessment is bounded by inspected accessible literature; independent external validation has not been performed.

## References

[1] M. Longla, *New copula families and mixing properties*, arXiv:2308.11074v1, 21 August 2023, section 2.2.2, equations (25)–(26), https://arxiv.org/pdf/2308.11074v1.

[2] M. Longla, *New copula families and mixing properties*, arXiv:2308.11074v2, 10 January 2024, https://arxiv.org/pdf/2308.11074.

[3] M. Longla, *New copula families and mixing properties*, *Statistical Papers* 65 (2024), 4331–4363, doi:10.1007/s00362-024-01559-9, https://link.springer.com/article/10.1007/s00362-024-01559-9.

[4] M. Longla and M.-A. Hamadou, *Estimation problems for some perturbations of the independence copula*, *Statistical Papers* (2025), doi:10.1007/s00362-025-01778-8, section 4.1, https://link.springer.com/article/10.1007/s00362-025-01778-8.

[5] M.-A. Hamadou and M. Longla, *An Extension of the d-Variate FGM Copula with Application*, arXiv:2509.07281v1 (2025), section 2, https://arxiv.org/html/2509.07281.

[6] M. Longla et al., *Copulas, m-dependence, and Markov chains*, *TEST* (2026), section 2.1, doi:10.1007/s11749-026-01003-0, https://link.springer.com/article/10.1007/s11749-026-01003-0.
