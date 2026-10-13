# Every exponentiated modified Lindley hazard eventually decreases to its limit from above
## Finding
Let
\[
F(x;\theta,\alpha)=F_X(x;\theta)^\alpha,\qquad x>0,\quad \alpha,\theta>0,
\]
be the exponentiated modified Lindley (EML) distribution, and put
\[
u=\theta x,\qquad a=\frac{1}{1+\theta}.
\]
The modified Lindley baseline survival is
\[
s_0(x)=1-F_X(x;\theta)=e^{-u}(1+aue^{-u}).
\]
Then
\[
\frac{h(x;\theta,\alpha)}{\theta}
=
1+
\left[
\frac{u-1}{1+\theta}-\frac{\alpha-1}{2}
\right]e^{-u}
+
O(u^2e^{-2u})
\qquad(x\to\infty),
\]
and
\[
\frac{d}{du}\left(\frac{h}{\theta}\right)
=
\left[
\frac{2-u}{1+\theta}+\frac{\alpha-1}{2}
\right]e^{-u}
+
O(u^2e^{-2u}).
\]
Therefore
\[
\lim_{x\to\infty}
\frac{e^{\theta x}}{\theta x}
\{h(x;\theta,\alpha)-\theta\}
=
\frac{\theta}{1+\theta},
\]
and
\[
\lim_{x\to\infty}
\frac{e^{\theta x}}{\theta x}h'(x;\theta,\alpha)
=
-\frac{\theta^2}{1+\theta}.
\]
Thus every EML hazard approaches \(\theta\) from above and is strictly decreasing for all sufficiently large \(x\). The leading terminal law is independent of \(\alpha\).

For \(\alpha>1\), the source's left-endpoint expansion implies
\[
h(x;\theta,\alpha)\sim
\frac{\alpha\theta^{2\alpha}}{(1+\theta)^\alpha}x^{\alpha-1},
\]
so the hazard is increasing sufficiently near zero. For \(\alpha=1\),
\[
h(0+;\theta,1)=\frac{\theta^2}{1+\theta},
\qquad
h'(0+;\theta,1)=
\frac{\theta^2(2\theta+3)}{(1+\theta)^2}>0.
\]
Hence every EML model with \(\alpha\ge1\) has at least one interior local maximum.

## Assumptions and scope
The parameters satisfy \(\alpha,\theta>0\), and the model is exactly the EML law obtained by the Lehmann exponentiation \(F_X^\alpha\) of the modified Lindley baseline.

“Eventually decreasing” means that some finite parameter-dependent threshold exists after which \(h'(x)<0\). The smallest such threshold is not determined.

The result proves existence but not uniqueness of an interior maximum when \(\alpha\ge1\). It does not classify all stationary points for \(0<\alpha<1\).

## Proof
The baseline density is
\[
f_0(x)
=
\theta e^{-u}
\left[1+a(2u-1)e^{-u}\right],
\]
so
\[
\frac{h_0}{\theta}
=
\frac{1+a(2u-1)e^{-u}}{1+aue^{-u}}
=
1+a(u-1)e^{-u}+O(u^2e^{-2u}).
\]

For any exponentiated CDF \(F^\alpha\), writing \(s=1-F\),
\[
h_\alpha=h_0 M_\alpha(s),
\qquad
M_\alpha(s)=
\frac{\alpha s(1-s)^{\alpha-1}}{1-(1-s)^\alpha}.
\]
As \(s\downarrow0\),
\[
M_\alpha(s)=1-\frac{\alpha-1}{2}s+O(s^2).
\]
Because
\[
s_0=e^{-u}+O(ue^{-2u}),
\]
we obtain
\[
M_\alpha(s_0)=
1-\frac{\alpha-1}{2}e^{-u}+O(ue^{-2u}).
\]
Multiplication gives the stated hazard expansion.

The exact hazard is analytic in \(e^{-u}\) with coefficients polynomial in \(u\) for large \(u\). Differentiating the exact expression and expanding gives
\[
\frac{d}{du}\left(\frac{h}{\theta}\right)
=
\left[
a(2-u)+\frac{\alpha-1}{2}
\right]e^{-u}
+
O(u^2e^{-2u}).
\]
The term \(ue^{-u}\) dominates both \(e^{-u}\) and \(u^2e^{-2u}\). Hence the first correction to \(h/\theta\) is eventually positive, whereas the derivative is eventually negative. Since \(u=\theta x\),
\[
h'(x)=\theta^2\frac{d}{du}\left(\frac{h}{\theta}\right),
\]
which yields both scaled limits.

For \(\alpha>1\), survival tends to one at the origin, so the source's density asymptotic is also the hazard asymptotic. Differentiating its positive leading power gives \(h'(x)>0\) near zero. At \(\alpha=1\), differentiating the exact baseline hazard gives
\[
\left.\frac{d}{du}\frac{h_0}{\theta}\right|_{u=0}
=
\frac{2\theta+3}{(1+\theta)^2}>0.
\]
Thus, for every \(\alpha\ge1\), the derivative is positive near zero and negative in the far tail. Continuity forces at least one interior local maximum.

## Verification
The included checker evaluates the exact EML hazard, not the truncated asymptotic formula. It verifies that the difference between the exact hazard and its first-order expansion, and likewise the difference between the exact derivative and its first-order expansion, are both on the predicted \(u^2e^{-2u}\) scale for several parameter pairs.

It also checks positive hazard derivative near the origin and negative derivative in the far tail for representative \(\alpha\ge1\) values.

These calculations are consistency tests only. The infinite-domain statements follow from the analytic expansions above.

## Relationship to prior work
Sarhan et al. give the exact EML CDF, survival, and hazard, derive its left-endpoint behavior, and state that increasing \(\alpha\) lowers the hazard at each fixed \(x\), with that effect becoming negligible in the right tail. Their hazard section and plots do not state the side from which the limiting hazard is reached, the eventual derivative sign, or the forced interior maximum for every \(\alpha\ge1\).

Gupta, Gupta, and Gupta develop the general Lehmann alternative \(F^\alpha\). They give the corresponding hazard factorization and sufficient conditions for preserving increasing- or decreasing-failure-rate classes. Their detailed examples concern Weibull, exponential, gamma, and Pareto baselines. The modified Lindley baseline is not globally IFR or globally DFR, so their simplest preservation theorem does not settle the present case.

Chesneau, Tomy, and Gillariose introduced the one-parameter modified Lindley baseline. The present theorem concerns the interaction of its specific tail correction with an arbitrary positive exponentiation parameter. Focused searches combining the EML name and DOI with terminal hazard, limiting rate, eventual decrease, and hidden-maximum terminology did not locate the two scaled limits or the all-\(\alpha\ge1\) maximum theorem.

## Limitations
The theorem does not prove uniqueness of the interior maximum. For \(0<\alpha<1\), the hazard diverges at the origin and is eventually decreasing at infinity, but intermediate turning points are not classified.

The asymptotic expansion does not give the smallest finite point after which the hazard decreases, so a turnaround can occur beyond a convenient plotting window.

The full text of the original modified Lindley paper was not available from the checked public sources during comparison. Its abstract and the exact baseline formulas reproduced in the EML source were inspected; this leaves residual uncertainty about baseline-only statements, not about the exponentiated-\(\alpha\) derivation.

## References
1. A. M. Sarhan, A. S. M. Al Luhayb, R. Alotaibi, and M. E. Sobh, “The exponentiated modified Lindley distribution with diverse biomedical and epidemiological applications,” AIMS Mathematics 11 (2026), 2313–2340. DOI: 10.3934/math.2026093.
2. R. C. Gupta, P. L. Gupta, and R. D. Gupta, “Modeling failure time data by Lehmann alternatives,” Communications in Statistics — Theory and Methods 27 (1998), 887–904. DOI: 10.1080/03610929808832134.
3. C. Chesneau, L. Tomy, and J. Gillariose, “A new modified Lindley distribution with properties and applications,” Journal of Statistics and Management Systems 24 (2021), 1383–1403. DOI: 10.1080/09720510.2020.1824727.
