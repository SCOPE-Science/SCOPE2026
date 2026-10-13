# Heavy-tail phase transition for the Gamma shape and rate UMVUEs
## Finding
Let \(X_1,\ldots,X_n\) be independent observations from the Gamma law with shape \(\alpha>0\) and rate \(\lambda>0\), and assume \(n\ge4\). Papadatos writes the complete sufficient statistic as \((X,Y)\), where \(X=\sum_{i=1}^nX_i\), \(X\) and \(Y\) are independent, and
\[
f_Y(y)=K(\alpha)y^{\alpha-1}(1-y)^cG(y),\qquad 0<y<1,
\]
with \(c=(n-3)/2\), \(G(y)=\sum_{m\ge0}d_m(1-y)^m\), \(d_m>0\), and \(d_0=G(1-)>0\). His shape UMVUE is
\[
U_0= c\frac{Y}{1-Y}-\frac{YG'(Y)}{G(Y)}.
\]
Put \(p=c+1=(n-1)/2\). Then
\[
\Pr\{U_0>t\}\sim C_0t^{-p},\qquad
C_0=\frac{K(\alpha)d_0c^p}{p},
\]
so \(\mathbb E[U_0^q]<\infty\) exactly for \(0<q<p\).

When \(\alpha>1/n\), Papadatos's rate UMVUE is
\[
U_1=\frac{nU_0-1}{X}.
\]
Set \(a=n\alpha\), \(Z=|nU_0-1|\), \(C_Z=n^pC_0\), and \(C_V=\lambda^a/\Gamma(a+1)\). Its absolute tail has the exact three-regime asymptotic
\[
\Pr\{|U_1|>t\}\sim
\begin{cases}
C_V\,\mathbb E[Z^a]t^{-a},&a<p,\\
pC_ZC_V\,t^{-p}\log t,&a=p,\\
C_Z\lambda^p\dfrac{\Gamma(a-p)}{\Gamma(a)}t^{-p},&a>p.
\end{cases}
\]
In particular,
\[
\mathbb E|U_1|^q<\infty\quad\Longleftrightarrow\quad 0<q<\min\{p,a\}.
\]
The rate estimator therefore changes tail mechanism at \(\alpha=(n-1)/(2n)\): below this value the small-\(X\) inverse-Gamma factor dominates, above it the large-\(U_0\) factor dominates, and at equality the product acquires an additional logarithm.

## Assumptions and scope
The claim uses the Gamma parameterization with density proportional to \(x^{\alpha-1}e^{-\lambda x}\). The shape statement holds for every \(\alpha>0\), \(\lambda>0\), and integer \(n\ge4\). The rate statement is restricted to \(\alpha>1/n\), exactly the domain on which the cited source establishes unbiasedness of \(U_1\). The constants \(K(\alpha)\), \(G\), and \(d_0\) are those of the cited density of \(Y\); no asymptotic approximation to them is assumed.

## Proof
Write \(z=1-y\). The power series for \(G\) at \(y=1\) gives \(G(y)\to d_0\) and \(G'(y)\to-d_1\) as \(y\uparrow1\). Therefore
\[
zU_0(y)=cy-z y\frac{G'(y)}{G(y)}\longrightarrow c,
\]
and
\[
f_Y(1-z)\sim K(\alpha)d_0z^c.
\]
Thus the contribution from \(Y\uparrow1\) satisfies
\[
\Pr\{U_0>t,\ Y>1/2\}\sim
K(\alpha)d_0\int_0^{c/t}z^c\,dz
=\frac{K(\alpha)d_0c^p}{p}t^{-p}.
\]
It remains to show that the other endpoint cannot contribute on this power scale. Since \(G'<0\), the estimator is nonnegative. The source proves \(\mathbb E_\beta U_0=\beta\) for every \(\beta>0\); substituting its density implies, for every \(\beta>0\),
\[
\int_0^{1/2}y^\beta|G'(y)|\,dy<\infty.
\]
Because \(|G'|\) is decreasing, this entails \(y^{\beta+1}|G'(y)|\to0\) as \(y\downarrow0\). For any fixed \(q\ge1\), choose \(0<\beta<\alpha/q\). Using \(G(y)\ge d_0\), the \(q\)-th-power density contribution of \(y|G'(y)|/G(y)\) near zero is bounded by a constant times
\[
y^{\alpha+q-1}|G'(y)|^q=O\!\left(y^{\alpha-q\beta-1}\right),
\]
which is integrable. For \(0<q<1\), \(U_0^q\le1+U_0\). Hence the \(Y\downarrow0\) part has moments of every positive order and therefore has tail smaller than every fixed power. The displayed regular-variation asymptotic follows, and the standard tail-integral identity gives \(\mathbb E[U_0^q]<\infty\) exactly when \(q<p\).

For the rate estimator, independence of \(X\) and \(Y\) is part of the cited sufficient-statistic decomposition. Since \(Z=|nU_0-1|\), the shape-tail result gives
\[
\Pr\{Z>t\}\sim C_Zt^{-p},\qquad C_Z=n^pC_0.
\]
Also \(X\sim\operatorname{Gamma}(a,\lambda)\), so, with \(V=1/X\),
\[
\Pr\{V>t\}=\Pr\{X<t^{-1}\}\sim C_Vt^{-a},\qquad C_V=\frac{\lambda^a}{\Gamma(a+1)},
\]
and
\[
\mathbb E[V^q]=\lambda^q\frac{\Gamma(a-q)}{\Gamma(a)}\quad\text{for }0<q<a.
\]
If \(a<p\), the variable \(Z\) has a moment of order strictly larger than \(a\), so the product-tail lemma for a regularly varying factor gives \(\Pr\{ZV>t\}\sim C_V\mathbb E[Z^a]t^{-a}\). If \(a>p\), the same lemma with the factors reversed gives \(\Pr\{ZV>t\}\sim C_Z\mathbb E[V^p]t^{-p}\), which is the third displayed case.

At \(a=p\), both factors have tails with the same index. For independent nonnegative \(A,B\) satisfying \(\Pr\{A>t\}\sim C_At^{-p}\) and \(\Pr\{B>t\}\sim C_Bt^{-p}\), integration by parts gives
\[
\mathbb E[B^p;B\le t]\sim pC_B\log t.
\]
Splitting the product event at fixed lower and upper truncations, applying the tail equivalence uniformly on the central range, and then sending the truncations outward yields
\[
\Pr\{AB>t\}\sim pC_AC_Bt^{-p}\log t.
\]
Applying this with \(A=Z\) and \(B=V\) proves the critical case. Finally, Tonelli and independence give \(\mathbb E|U_1|^q=\mathbb E[Z^q]\mathbb E[V^q]\) as an extended nonnegative integral, so finiteness is equivalent to \(q<p\) and \(q<a\).

## Verification
The source's Theorem 2.1 was checked for the exact formula for \(U_0\), the density of \(Y\), positivity and monotonicity properties of \(G\), and the finite-variance threshold. Corollary 2.1 was checked for \(U_1=(nU_0-1)/X\), the independence of \(X\) and \(Y\), the unbiasedness condition \(\alpha>1/n\), and the published variance condition. Substituting \(q=2\) into the new moment criterion gives precisely the source's thresholds: \(n\ge6\) for the shape estimator, and additionally \(\alpha>2/n\) for the rate estimator. This agreement is an internal consistency check, not an independent validation.

## Relationship to prior work
Papadatos derives the UMVUE formulas and proves the binary second-moment statements: the shape estimator has finite variance exactly for \(n\ge6\), while the rate estimator, when \(n\ge6\), has finite variance exactly for \(\alpha>2/n\). The proof already identifies the two endpoint mechanisms needed for the variance calculation, but it does not state the full positive-moment spectrum, a regularly varying tail for either estimator, the exact tail constants, the transition at \(\alpha=(n-1)/(2n)\), or the logarithmic critical product law. Earlier work of Glaser and Nandi derives distributions for geometric-mean/arithmetic-mean ratios in Gamma samples; those papers concern the ratio distribution itself rather than the later UMVUEs or their product-tail phase diagram.

## Limitations
The result describes upper-tail magnitude, not finite-sample risk under bounded loss, bias robustness, or optimality relative to alternative estimators. The critical product argument uses standard regular-variation machinery; the new content is its exact application to these UMVUEs and the resulting constants and phase boundary. The searches performed did not reveal a published statement of this phase diagram, but an older equivalent result under different estimator-tail terminology remains a residual literature risk.

## References
1. N. Papadatos, “On point estimators for Gamma and Beta distributions,” arXiv:2205.10799v1, 2022; later published in *The American Statistician* 78 (2024), 412–417, DOI:10.1080/00031305.2024.2332766.
2. R. E. Glaser, “The Ratio of the Geometric Mean to the Arithmetic Mean for a Random Sample from a Gamma Distribution,” *Journal of the American Statistical Association* 71 (1976), 480–487, DOI:10.1080/01621459.1976.10480373.
3. S. B. Nandi, “On the Exact Distribution of a Normalized Ratio of the Weighted Geometric Mean to the Unweighted Arithmetic Mean in Samples from Gamma Distributions,” *Journal of the American Statistical Association* 75 (1980), 217–220, DOI:10.1080/01621459.1980.10477456.
