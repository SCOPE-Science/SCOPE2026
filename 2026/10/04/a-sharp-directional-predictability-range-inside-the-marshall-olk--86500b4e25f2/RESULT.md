# A sharp directional-predictability range inside the Marshall–Olkin copula family

## Finding

Consider the two-parameter Marshall–Olkin copula
\[
C_{\alpha,\beta}(u,v)
=
\min\{u^{1-\alpha}v,\,uv^{1-\beta}\},
\qquad 0<\alpha,\beta<1.
\]
Let
\[
t=\tau(C_{\alpha,\beta})\in(0,1)
\]
be Kendall's tau, and let \(\xi_{Y\mid X}\) denote Chatterjee's directional rank correlation with \(X\) as predictor and \(Y\) as response.

The classical Marshall–Olkin formulas are
\[
\tau
=
\frac{\alpha\beta}{\alpha+\beta-\alpha\beta},
\qquad
\rho_S
=
\frac{3\alpha\beta}{2\alpha+2\beta-\alpha\beta}.
\]
The directional Chatterjee formula is
\[
\xi_{Y\mid X}
=
\frac{2\alpha^2\beta}{3\alpha+\beta-2\alpha\beta}.
\]

Fixing \(t\), the complete range of directional predictive strength is
\[
\boxed{
\frac{16t^2}{(t+3)^2}
\le
\xi_{Y\mid X}
<
\frac{2t}{3-t}.
}
\tag{1}
\]

The lower endpoint is attained uniquely at
\[
\boxed{
\alpha_*(t)=\frac{4t}{t+3},
\qquad
\beta_*(t)=\frac{4t}{1+3t}.
}
\tag{2}
\]
The upper endpoint is not attained in the strict parameter square, but it is a sharp supremum approached as
\[
(\alpha,\beta)\to(1,t).
\]

By contrast, Spearman's rho contains no additional information once Kendall's tau is fixed:
\[
\boxed{
\rho_S=\frac{3t}{2+t}.
}
\tag{3}
\]
Hence every Marshall–Olkin copula on the same Kendall-tau fiber has exactly the same Spearman rho, even though its directional Chatterjee correlation can vary over the nontrivial interval (1).

The direction of asymmetry is also visible from the two Chatterjee coefficients:
\[
\boxed{
\operatorname{sgn}
\bigl(
\xi_{Y\mid X}-\xi_{X\mid Y}
\bigr)
=
\operatorname{sgn}(\alpha-\beta).
}
\tag{4}
\]

Finally, let
\[
\lambda_U=\min\{\alpha,\beta\}
\]
be the upper-tail dependence coefficient. At fixed \(t\),
\[
\boxed{
t<\lambda_U\le\frac{2t}{1+t}.
}
\tag{5}
\]
For a given admissible pair \((t,\lambda_U)\), the unordered parameter pair is uniquely determined. If
\[
\lambda=\lambda_U,
\]
then the other parameter is
\[
q
=
\frac{t\lambda}{\lambda(1+t)-t}.
\tag{6}
\]
Thus \((t,\lambda_U)\) identifies \(\{\alpha,\beta\}\), and the sign in (4) resolves which parameter belongs to which margin.

The weak-dependence scale separation is sharp. As \(t\downarrow0\),
\[
\xi_{\min}(t)
\sim
\frac{16}{9}t^2,
\qquad
\xi_{\sup}(t)
\sim
\frac23t,
\]
so the ratio between the largest and smallest compatible directional predictive strengths diverges like
\[
\frac{3}{8t}.
\]

## Assumptions and scope

The claim is for the strict two-parameter Marshall–Olkin family with \(0<\alpha,\beta<1\). Allowing the natural boundary values \(\alpha=1\) or \(\beta=1\) closes the right endpoint in (1).

Chatterjee's coefficient is directional. The formula displayed above follows the convention in which the first copula coordinate is the predictor. Transposing the copula exchanges \(\alpha\) and \(\beta\).

The result concerns exact population dependence coefficients. It does not address finite-sample estimation error or asymptotic efficiency of estimators.

## Proof

Write
\[
p=\alpha\beta,
\qquad
s=\alpha+\beta.
\]
From the Kendall formula,
\[
t=\frac{p}{s-p},
\]
so
\[
s=p\frac{1+t}{t}.
\]
Substitution into Spearman's formula gives
\[
\rho_S
=
\frac{3p}{2s-p}
=
\frac{3t}{2+t},
\]
which proves (3).

Now solve the fixed-tau equation for \(\beta\) in terms of \(\alpha\):
\[
\beta
=
\frac{t\alpha}{\alpha(1+t)-t}.
\tag{7}
\]
The constraints \(0<\alpha,\beta<1\) are equivalent to
\[
t<\alpha<1.
\]
Substituting (7) into the Chatterjee formula gives the one-variable function
\[
\Xi_t(\alpha)
=
\frac{2t\alpha^2}{\alpha(t+3)-2t}.
\tag{8}
\]
Its derivative is
\[
\Xi_t'(\alpha)
=
\frac{2\alpha t\,[\alpha(t+3)-4t]}
{[\alpha(t+3)-2t]^2}.
\tag{9}
\]
Therefore the unique critical point is
\[
\alpha_*=\frac{4t}{t+3},
\]
and the sign in (9) shows that it is the unique global minimum on \((t,1)\). Equation (7) then gives
\[
\beta_*=\frac{4t}{1+3t}.
\]
Substitution into (8) yields
\[
\Xi_t(\alpha_*)
=
\frac{16t^2}{(t+3)^2}.
\]

The endpoint limits are
\[
\lim_{\alpha\downarrow t}\Xi_t(\alpha)
=
\frac{2t^2}{1+t},
\qquad
\lim_{\alpha\uparrow1}\Xi_t(\alpha)
=
\frac{2t}{3-t}.
\]
For \(0<t<1\),
\[
\frac{2t}{3-t}
>
\frac{2t^2}{1+t},
\]
so the right-hand limit is the sharp supremum. Continuity of \(\Xi_t\) on the fixed-tau fiber gives the complete interval (1).

For the directional asymmetry, the transposed copula exchanges \(\alpha\) and \(\beta\). Direct subtraction gives
\[
\xi_{Y\mid X}-\xi_{X\mid Y}
=
\frac{
2\alpha\beta(\alpha-\beta)(\alpha+\beta-2\alpha\beta)
}{
(3\alpha+\beta-2\alpha\beta)
(\alpha+3\beta-2\alpha\beta)
}.
\tag{10}
\]
Every factor except \(\alpha-\beta\) is strictly positive on \((0,1)^2\), proving (4).

For the tail coefficient, suppose without loss of generality that
\[
\lambda_U=\alpha\le\beta.
\]
Along the fixed-tau fiber, equality \(\alpha=\beta\) occurs at
\[
\alpha=\beta=\frac{2t}{1+t}.
\]
The maximally asymmetric boundary has \(\alpha\downarrow t\) and \(\beta\uparrow1\). Hence (5). Solving (7) with \(\alpha=\lambda\) gives (6). This determines the unordered pair, while (4) determines its orientation.

The two small-\(t\) expansions follow directly from the exact endpoint formulas.

## Verification

The accompanying exact-rational checker samples rational Marshall–Olkin parameters, reconstructs their Kendall and Spearman coefficients, and verifies (3) identically.

It then samples rational values of \(t\) and rational positions on the fixed-tau fiber, reconstructs \(\beta\) from (7), and checks the bounds in (1) without floating-point comparisons. It verifies the exact optimizer (2), the directional sign identity (10), the upper-tail range (5), and the unordered reconstruction formula (6).

Finite replay is not used to infer the theorem. The proof is the exact algebra and one-variable derivative analysis above.

## Relationship to prior work

Dobrowolski and Kumar study the two-parameter Marshall–Olkin family and give the classical closed forms for Kendall's tau, Spearman's rho, and upper-tail dependence. Their full 2014 article also studies Gini association and mutual information. It does not contain Chatterjee's rank correlation, which was introduced later.

Ansari and Rockel derive the closed form
\[
\xi_{Y\mid X}
=
\frac{2\alpha^2\beta}{3\alpha+\beta-2\alpha\beta}
\]
for the Marshall–Olkin family. Their article studies Schur ordering and dependence properties across many copula families. The inspected Marshall–Olkin calculation gives the parameter formula but does not state the fixed-Kendall sharp interval (1), its unique minimizer, the weak-dependence scale separation, or the parameter-orientation criterion (4).

A later exact-region paper determines the global attainable region of Chatterjee's xi and Spearman's rho over all bivariate copulas. That universal result does not by itself determine the exact conditional fiber inside the two-parameter Marshall–Olkin subfamily. Its public preprint and abstract were checked as a stronger-coverage risk.

Targeted searches for fixed-Kendall Marshall–Olkin fibers, Chatterjee-xi extrema, parameter identification, and directional asymmetry did not locate formulas (1), (2), or (4).

## Limitations

The result is family-specific. It does not imply that Kendall tau and Spearman rho are redundant in general copula families.

The upper endpoint in (1) is not attained when both Marshall–Olkin parameters are required to be strictly below one.

The originality assessment is targeted. An equivalent elimination argument may exist in unpublished notes, software documentation, or specialized copula-calibration literature under different terminology.

## References

1. E. Dobrowolski and P. Kumar, “Some properties of the Marshall–Olkin and generalized Cuadras–Augé families of copulas,” *Australian Journal of Mathematical Analysis and Applications* 11(1), Article 2 (2014), published 2014-02-19.
2. J. Ansari and M. Rockel, “Dependence properties of bivariate copula families,” arXiv:2310.17307, first submitted 2023-10-26; later *Dependence Modeling* 12 (2024), DOI 10.1515/demo-2024-0002.
3. J. Ansari and M. Rockel, “The exact region and an inequality between Chatterjee's and Spearman's rank correlations,” arXiv:2506.15897, first submitted 2025-06-18; later *Journal of Multivariate Analysis* 214 (2026), Article 105630.
