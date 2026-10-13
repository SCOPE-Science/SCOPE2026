# Exact admissibility and Spearman fold of the Darwish–Shahbaz copula

## Finding

Consider the rational function
\[
C_{\alpha}(u,v)=\frac{uv(1-\alpha u)(1-\alpha v)}{(1-\alpha)(1-\alpha uv)},\qquad (u,v)\in[0,1]^2.
\]
For real \(\alpha\), this formula defines a bivariate copula **if and only if** \(\alpha\le 1/2\). Thus the range \(-2\le\alpha\le1/2\) originally selected for this model is a proper subset of its full copula-valid parameter domain.

There is exactly one parameter \(\alpha_*<-2\) minimizing Spearman's rank correlation over all admissible parameters. It is characterized exactly as follows. For \(t>0\) set
\[
q=uv,\quad w=uv(1-u)(1-v),\quad
A(t)=\int_0^1\!\int_0^1\frac{w}{(1+tq)^2}\,du\,dv,\quad
B(t)=\int_0^1\!\int_0^1\frac{wq}{(1+tq)^2}\,du\,dv.
\]
There exists a unique \(t_*>2\) satisfying
\[
t_*^2B(t_*)=A(t_*).
\]
The unique minimizer is \(\alpha_*=-t_*\), with numerical values
\[
t_*\approx2.33900178182170,\qquad
\rho_S(C_{\alpha_*})\approx-0.15564754516173.
\]
The source's endpoint \(\alpha=-2\) instead gives \(\rho_S(C_{-2})\approx-0.15492736512498\). The improvement in the negative-rank-correlation minimum is small, but the larger structural distinction is exact: on the unrestricted negative branch, Spearman correlation decreases and then increases to zero, so **every correlation strictly between its minimum and zero is achieved by exactly two distinct negative parameter values**.

In addition, for every \(t>0\),
\[
\sup_{u,v\in[0,1]}|C_{-t}(u,v)-uv|\le\frac{1}{1+t},
\]
so the same family returns uniformly to the independence copula as \(\alpha\to-\infty\).

## Assumptions and scope

The parameter is any real number for which the displayed rational expression is a continuous function throughout the closed unit square. No particular parametric marginal distributions or data are assumed. A copula means a grounded, two-increasing distribution function with uniform \([0,1]\) margins. Spearman correlation is normalized as
\[
\rho_S(C)=12\int_0^1\!\int_0^1(C(u,v)-uv)\,du\,dv.
\]
All extremality statements concern this single rational copula family, not all copulas or its higher-dimensional or generalized constructions. Quoted decimals are reproducible numerical approximations, not certified rational enclosure bounds.

## Proof

**1. Algebraic identities and exact admissibility.** Direct differentiation gives
\[
C_{\alpha}(u,v)-uv=\frac{\alpha uv(1-u)(1-v)}{(1-\alpha)(1-\alpha uv)}
\]
and
\[
\frac{\partial^2C_{\alpha}}{\partial u\,\partial v}
=\frac{N_{\alpha}(u,v)}{(1-\alpha)(1-\alpha uv)^3},\quad
N_{\alpha}=\alpha(1-u)(1-v)+(1-\alpha u)(1-\alpha v)-\alpha(1-\alpha uv)^3.
\]
For \(\alpha=-t<0\), the denominator is positive and
\[
N_{-t}=(1+tu)(1+tv)+t\big[(1+tuv)^3-(1-u)(1-v)\big]>0,
\]
using \((1+tuv)^3\ge1\ge(1-u)(1-v)\).

For \(0\le\alpha\le1/2\), \(0\le1-\alpha uv\le1\), so \((1-\alpha uv)^3\le1-\alpha uv\). Consequently,
\[
N_{\alpha}\ge1-2\alpha(u+v)+\alpha(1+2\alpha)uv=:L_{\alpha}(u,v).
\]
This expression is affine separately in \(u\) and \(v\), so its minimum on \([0,1]^2\) occurs at a corner. The four corner values are \(1\), \(1-2\alpha\), \(1-2\alpha\), and \((1-\alpha)(1-2\alpha)\), all nonnegative. The density is therefore nonnegative. For every \(\alpha<1\) the function also satisfies \(C_{\alpha}(u,0)=C_{\alpha}(0,v)=0\) and \(C_{\alpha}(u,1)=u\), \(C_{\alpha}(1,v)=v\). Integrating its nonnegative continuous mixed density over any rectangle proves two-increasingness and the copula property.

For \(1/2<\alpha<1\), the mixed density at the corner \((0,1)\) equals \((1-2\alpha)/(1-\alpha)<0\), and by continuity is negative on an interior neighborhood: the function is not two-increasing. At \(\alpha=1\) its defining denominator vanishes identically. For \(\alpha>1\) it has a genuine pole at \(u=v=1/\sqrt{\alpha}\), where the numerator is strictly positive. Thus no other real \(\alpha\) defines a copula by this formula.

**2. Spearman correlation and derivative.** For \(t>0\), set \(R(t)=\rho_S(C_{-t})\) and \(L(t)=-R(t)\). The preceding difference identity yields
\[
L(t)=\frac{12t}{1+t}\int_0^1\!\int_0^1\frac{w}{1+tq}\,du\,dv>0.
\]
Differentiation under the integral sign is justified on each compact positive-\(t\) interval by bounded smooth integrands. In terms of \(A\) and \(B\) above,
\[
L'(t)=\frac{12}{(1+t)^2}\big(A(t)-t^2B(t)\big).
\]
Both \(A\) and \(B\) are strictly positive. Put \(H(t)=t^2B(t)/A(t)\). Let \(\mathbb E_{A,t}\) and \(\mathbb E_{B,t}\) be expectations under the probability densities proportional to \(w/(1+tq)^2\) and \(wq/(1+tq)^2\), respectively. Then
\[
\frac{H'(t)}{H(t)}
=\frac2t-2\mathbb E_{B,t}\!\left[\frac{q}{1+tq}\right]
+2\mathbb E_{A,t}\!\left[\frac{q}{1+tq}\right]>0,
\]
because \(0<q/(1+tq)<1/t\) almost everywhere under both measures. In particular \(H\) increases strictly from its limit \(0\) as \(t\downarrow0\).

To see that \(H=1\) has a root, observe directly that
\[
0<L(t)\le\frac{12}{1+t}\int_0^1\!\int_0^1\frac{w}{q}\,du\,dv
=\frac{3}{1+t}.
\]
Indeed, \(t/(1+tq)\le1/q\) for \(q>0\), and \(w/q=(1-u)(1-v)\). (Equivalently, use the uniform-copula bound proved below.) Hence \(L(t)\to0\) as \(t\to\infty\), while \(L(t)\to0\) as \(t\downarrow0\). Since \(L(t)>0\) for \(t>0\), it has an interior maximizer with \(L'=0\), so \(H=1\) has a solution. Strict increase of \(H\) proves uniqueness and shows \(L\) increases strictly before this point and decreases strictly afterwards.

To locate the maximizer beyond \(t=2\), write
\[
H(2)=4\frac{\int wq/(1+2q)^2}{\int w/(1+2q)^2}.
\]
Under the probability measure with density proportional to \(w\), the coordinates are independent \(\mathrm{Beta}(2,2)\) variables, giving \(\mathbb E[q]=1/4\). The tilt \((1+2q)^{-2}\) is strictly decreasing in the nondegenerate variable \(q\), so its covariance with \(q\) is strictly negative. Consequently, the weighted mean of \(q\) is strictly less than \(1/4\); hence \(H(2)<1\) and the unique root obeys \(t_*>2\).

For \(0<\alpha\le1/2\), the difference \(C_{\alpha}-uv\) is everywhere nonnegative and strictly positive in the interior; thus \(\rho_S(C_{\alpha})>0\). At \(\alpha=0\) it is zero. The unique minimizer over the entire valid domain therefore lies on the negative branch and is precisely \(\alpha_*=-t_*\).

**3. Return to independence and multiplicity.** For \(t>0\), the identity
\[
|C_{-t}-uv|=\frac{t}{1+t}\frac{uv(1-u)(1-v)}{1+tuv}
\le\frac{1}{1+t}
\]
follows from \(tuv/(1+tuv)<1\). This proves uniform convergence to independence. Since \(R(t)\) starts at zero, decreases strictly to its unique negative minimum, and tends back to zero without attaining it at finite \(t>0\), each strictly intermediate negative correlation has exactly two distinct negative preimages. These parameters also give genuinely different copulas: from the difference formula, \((C_{-t}-uv)/[uv(1-u)(1-v)]\) tends to \(-t/(1+t)\) as \(uv\) tends to zero through interior points, and that limit uniquely determines \(t\).

## Verification

The standalone file `check.py` uses symbolic differentiation to check the two central rational identities and the uniform marginal identities. It then evaluates \(A\), \(B\), and \(\rho_S\) by tensor-product Gauss–Legendre quadrature of degrees \(64\), \(96\), and \(144\), solving the unique root equation numerically. The three resolutions agree at the displayed precision. Finite density-grid tests are merely numerical cross-checks; the universal assertions follow from the analytical inequalities above.

Run `python check.py` with Python 3, NumPy, SciPy and SymPy installed. Numerical reproducibility gives \(H(2)\approx0.754523758\), \(H(3)\approx1.557655580\), and the values reported in the Finding section.

## Relationship to prior work

Darwish and Shahbaz (2026), equation (6), introduce exactly the rational family used here with the *chosen* interval \([-2,1/2]\); equation (19) computes its Spearman correlation on that interval. Appendix A establishes validity there and explicitly motivates the lower cutoff by unique dependence/concordance values. Those results are **not** a statement of maximal copula-validity or of the unique unrestricted Spearman extremum. The present proof extends validity to every negative parameter, identifies exactly where rank-correlation monotonicity turns, and describes the return to independence. It does not contest validity or the restricted-range conclusions of that paper.

Darwish, Shahbaz and Shahbaz (2024) study a different power-polynomial bivariate construction, not this rational denominator and its parameter domain. Ghosh, Bhuyan and Finkelstein (2022) construct a different piecewise negative-dependence copula attaining a wider range of negative correlations; a stronger dependence *magnitude* in another family does not imply the structural parameter theorem proved here. The general copula criteria and Spearman normalization are standard and are not claimed as new.

## Limitations

This is a mathematical classification of a particular bivariate formula, not an empirical validation or a proof about larger generalized or multivariate classes. The difference between the restricted and unrestricted minima is only about \(7.20\times10^{-4}\); its principal consequence is understanding validity and calibration ambiguity, not a large improvement in achievable negative dependence. The unique root is specified exactly by convergent integrals, rather than a closed elementary constant. Approximate digits are not formal interval certificates. Independent scholarly assessment of priority and correctness has not been performed.

## References

1. J. A. Darwish and M. Q. Shahbaz, *Efficient Modeling of the Energy Sector Using a New Bivariate Copula*, Mathematics **14** (2026), 540, https://doi.org/10.3390/math14030540. Section 3, Section 4.2 and Appendix A.
2. J. A. Darwish, S. H. Shahbaz and M. Q. Shahbaz, *A New Class of Bivariate Distributions: Properties, Estimation, and Modeling*, Mathematics **12** (2024), 4021, https://doi.org/10.3390/math12244021.
3. S. Ghosh, P. Bhuyan and M. Finkelstein, *On a Bivariate Copula for Modeling Negative Dependence: Application to New York Air Quality Data*, Statistical Methods & Applications **31** (2022), 1329–1353, https://doi.org/10.1007/s10260-022-00636-3; lawful open preprint https://arxiv.org/abs/2102.05386.
