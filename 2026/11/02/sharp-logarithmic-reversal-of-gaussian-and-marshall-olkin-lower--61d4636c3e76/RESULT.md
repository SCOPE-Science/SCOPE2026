# Sharp logarithmic reversal of Gaussian and Marshall–Olkin lower-tail rankings

## Finding

Two bivariate copulas can have the same diagonal tail power and yet reverse their local ordering along an explicitly determined logarithmic boundary. This theorem gives the *unique* reversal boundary for the Gaussian copula and the symmetric Marshall–Olkin copula calibrated to that power.

Fix \(0<\rho<1\) and put
\[
\alpha=\frac{\rho}{1+\rho},\qquad
\beta=\frac{2\rho}{1+\rho},\qquad
\kappa=\frac{2}{1+\rho}=2-\beta.
\]
Let \(G_\rho(u,v)\) be the bivariate standard-Gaussian copula with correlation \(\rho\), and let
\[
M_\beta(u,v)=\frac{uv}{\max(u,v)^\beta},\qquad 0<u,v\leq1.
\]
For every sufficiently small \(u>0\), there is precisely one \(v_\rho(u)\in(0,u)\) satisfying \(G_\rho(u,v_\rho(u))=M_\beta(u,v_\rho(u))\). For \(0<v<v_\rho(u)\) the Gaussian probability is strictly larger; for \(v_\rho(u)<v\leq u\) it is strictly smaller.

Writing \(L=\log(1/u)\), the unique crossing has the exact asymptotic scale
\[
\boxed{\quad v_\rho(u)\sim c_\rho\frac{u}{L},\qquad
c_\rho=\frac1{4\pi}\left(\frac{(1+\rho)^2}{\sqrt{1-\rho^2}}\right)^{(1+\rho)/\rho}.\quad}
\]
More precisely, with
\[
K_\rho=\frac{(1+\rho)^2}{\sqrt{1-\rho^2}}(4\pi)^{-\alpha},
\]
for every fixed \(c>0\),
\[
\boxed{\quad\lim_{u\downarrow0}
\frac{G_\rho(u,cu/L)}{M_\beta(u,cu/L)}
=K_\rho c^{-\alpha}.\quad}
\]
The limit is greater than one exactly when \(c<c_\rho\). In the wider logarithmic wedge, for every fixed \(s\geq0\),
\[
\boxed{\quad\frac{G_\rho(u,uL^{-s})}{M_\beta(u,uL^{-s})}
\sim K_\rho L^{\alpha(s-1)}.\quad}
\]
The latter estimate holds uniformly for \(s\) in any bounded subset of \([0,\infty)\). Thus the reversal exponent \(s=1\) is independent of the correlation parameter, although the sharp multiplicative constant is not.

In particular, \(G_\rho\) is strictly *smaller* than \(M_\beta\) along every fixed positive ray approaching the origin, but they are **not ordered in either direction on any neighborhood of the origin**.

## Assumptions and scope

Only bivariate copulas and fixed \(0<\rho<1\) are considered. Both variables have uniform margins. \(u\downarrow0\) denotes a genuine asymptotic limit; \(v_\rho(u)\) is a threshold in the interval \((0,u)\) for all sufficiently small \(u\). No uniformity as \(\rho\to0\) or \(\rho\to1\) is claimed. The Gaussian copula is the distribution of \((\Phi(X),\Phi(Y))\) for standard correlated Gaussian \((X,Y)\). The Marshall–Olkin function above is a copula for \(0<\beta<1\).

## Proof

**1. Diagonal normal tail.** Let \(a=-\Phi^{-1}(u)>0\). For a centered bivariate standard normal pair with correlation \(\rho\), write \(Q(x,y)=(x^2-2\rho xy+y^2)/(1-\rho^2)\). At large thresholds \(a,b\) with \(b/a\to1\), integration of the bivariate normal density over the positive quadrant gives
\[
\Pr(X>a,Y>b)
=\frac{\exp[-Q(a,b)/2]}{2\pi\sqrt{1-\rho^2}\,\gamma_1\gamma_2}
\bigl(1+O_\rho(a^{-2}+b^{-2})\bigr),
\quad \gamma_1=\frac{a-\rho b}{1-\rho^2},\quad
\gamma_2=\frac{b-\rho a}{1-\rho^2}.
\]
To justify this uniform estimate without assuming it as an unproved lemma, substitute \(x=a+h\), \(y=b+k\) in the density. The exponent factors as \(-Q(a,b)/2-\gamma_1h-\gamma_2k-Q(h,k)/2\). Rescaling \(h=z/\gamma_1\) and \(k=w/\gamma_2\), the integral remaining after extracting \((\gamma_1\gamma_2)^{-1}\) differs from one by at most \(\mathbb E[Q(Z/\gamma_1,W/\gamma_2)/2]\), using \(0\leq1-e^{-x}\leq x\) for \(x\geq0\) and independent unit exponentials \(Z,W\). Because \(Q\) is nonnegative quadratic, this is \(O_\rho(a^{-2}+b^{-2})\) when \(b/a\to1\). The displayed approximation follows.

On the diagonal \(b=a\), \(\gamma_1=\gamma_2=a/(1+\rho)\) and \(Q(a,a)=2a^2/(1+\rho)\). Mills' ratio yields \(u=\phi(a)a^{-1}(1+O(a^{-2}))\), whence \(a^2\sim2L\) and
\[
G_\rho(u,u)\sim \frac{(1+\rho)^2}{2\pi\sqrt{1-\rho^2}a^2}
\exp[-a^2/(1+\rho)]
\sim K_\rho u^\kappa L^{-\alpha}.
\]
The second equality follows by inserting \(\exp(-a^2/2)\sim\sqrt{2\pi}\,a u\), with \(\kappa=2/(1+\rho)\) and \(\alpha=(2-\kappa)/2\). This also verifies the stated constant \(K_\rho\).

**2. A genuinely moving ray.** Let \(t=t(u)\geq0\) satisfy \(t=O(\log L)\) and put \(v=ue^{-t}\) and \(b=-\Phi^{-1}(v)\). Subtracting the logarithmic Mills expansions at \(a\) and \(b\),
\[
\frac{b^2-a^2}{2}+\log(b/a)=t+O_\rho(L^{-1}),
\qquad a\,(b-a)=t+O\!\left(\frac{(1+t)^2}{L}\right).
\]
Indeed \(a^2\asymp L\), \(b/a\to1\) and \(b-a=O((1+t)/a)\), so both the logarithmic ratio and the quadratic correction are bounded by the displayed error. In particular \((b-a)^2=o(1)\) and \(\gamma_i(a,b)/\gamma_i(a,a)=1+o(1)\), uniformly over \(0\leq t\leq S\log L\) for any fixed \(S\).

The exact identity
\[
Q(a,b)-Q(a,a)=\frac{2(1-\rho)a(b-a)+(b-a)^2}{1-\rho^2}
\]
and Step 1 therefore give the moving-ray ratio
\[
\frac{G_\rho(u,ue^{-t})}{G_\rho(u,u)}
=e^{-t/(1+\rho)}(1+o(1)),
\]
**uniformly** for \(0\leq t\leq S\log L\). This uniformity is essential: fixed-ray asymptotics alone would not license substituting a varying direction.

For \(v\leq u\) the Marshall–Olkin copula is exactly \(M_\beta(u,v)=u^{1-\beta}v=u^\kappa e^{-t}\). Combining with the diagonal expression gives
\[
\frac{G_\rho(u,ue^{-t})}{M_\beta(u,ue^{-t})}
=K_\rho L^{-\alpha}e^{\alpha t}(1+o(1)).
\]
Putting \(t=s\log L\) gives the wedge formula; putting \(t=\log(L/c)\) gives the sharp constant crossover. Since \(\alpha>0\), the critical constant is \(c_\rho=K_\rho^{1/\alpha}\), exactly as displayed.

**3. Existence and uniqueness of the crossing.** Fix \(u\in(0,1)\). Conditioning a bivariate Gaussian on the second uniform coordinate \(V=t\),
\[
G_\rho(u,v)=\int_0^v h_u(t)\,dt,
\quad h_u(t)=\Phi\!\left(\frac{\Phi^{-1}(u)-\rho\Phi^{-1}(t)}{\sqrt{1-\rho^2}}\right).
\]
Because \(\rho>0\), \(h_u(t)\) is continuous and strictly decreasing in \(t\). Thus the average \(G_\rho(u,v)/v\) is strictly decreasing for \(0<v\leq u\). Dividing by the constant \(u^{1-\beta}\) shows \(G_\rho(u,v)/M_\beta(u,v)\) is strictly decreasing in \(v\in(0,u]\).

As \(v\downarrow0\), \(h_u(t)\to1\), so this ratio tends to \(u^{\beta-1}>1\). At \(v=u\), Step 1 gives ratio asymptotic \(K_\rho L^{-\alpha}\to0\), which is less than one for all sufficiently small \(u\). Strict monotonicity and continuity yield exactly one crossing and the two strict sign regions. To locate it, bracket the crossing between \((c_\rho-\varepsilon)u/L\) and \((c_\rho+\varepsilon)u/L\) using Step 2, for \(0<\varepsilon<c_\rho\), and then let \(\varepsilon\downarrow0\). This proves \(v_\rho(u)\sim c_\rho u/L\).

Finally, for any fixed \(w_1,w_2>0\), the same normal-tail expansion with \(t=O(1)\) yields
\[
G_\rho(uw_1,uw_2)\sim
K_\rho (uw_1)^{\kappa/2}(uw_2)^{\kappa/2}L^{-\alpha},
\]
while \(M_\beta(uw_1,uw_2)=u^\kappa M_\beta(w_1,w_2)\) for small \(u\). Hence \(G_\rho/M_\beta\to0\) along every positive ray. But at \(v=c u/L\) with \(c<c_\rho\), that ratio tends to a number greater than one. Both sign regions occur arbitrarily close to the origin; neither copula locally dominates the other.

## Verification

`checker.py` evaluates bivariate Gaussian orthant integrals using an independent one-dimensional Gauss–Laguerre quadrature representation (not the proof's two-dimensional tail approximation), with numerically stable log-normal probabilities. It compares the calculated ratios with \(K_\rho c^{-\alpha}\) and checks strict signs on both sides of \(c_\rho\) for three correlation values and multiple tail depths. Run `python checker.py` after installing NumPy and SciPy per `requirements.txt`. The observed run reported 63 successful numeric assertions. They do not replace the infinite-limit proof above.

## Relationship to prior work

Li and Joe (2026, arXiv:2603.27458, first public 2026-03-29) analyze conditional copula risk probabilities and explicitly note that Gaussian tail approximations need not be uniform away from the diagonal. The theorem above supplies a sharp logarithmic boundary and exact crossover constant for a natural comparison of two copulas with identical diagonal tail order.

Siburg and Strothmann (2022, arXiv:2210.06842) investigate local stochastic dominance and exhibit a different nonlocal-ordering example based on a Clayton copula and a Marshall–Olkin copula on a power curve. It does not determine the Gaussian–Marshall–Olkin logarithmic boundary. Furman et al. (2016, arXiv:1607.04736) prove diagonal optimality of maximal Gaussian tail-dependence indices under fixed-product paths, not a cross-model order or a moving-path constant.

Siburg (arXiv:2610.35325, publicly posted 2026-10-26) gives a fixed-direction Gaussian copula expansion and intermediate-tail-order comparisons; it does not derive this moving-direction comparison or its unique crossing. Its fixed-direction asymptotics are not being substituted into a varying direction here; the required uniform bound is proved separately. Earlier orthant-tail estimates, including Savage's method, supply classical background but not this calibrated boundary statement.

## Limitations

The result compares exactly one calibrated two-family pair, for fixed \(0<\rho<1\); it does not classify arbitrary copulas. The unique-crossing assertion is along the vertical section \(0<v\leq u\), not a claim about all two-dimensional crossing curves. Rates uniform as \(\rho\) approaches either endpoint, finite-sample guarantees for the asymptotic threshold, and extensions to higher dimensions are not established. The associated historical-priority assessment is limited to the primary full texts and searches listed in the review; an older implicit application of Gaussian moderate-deviation theory cannot be ruled out. No independent audit has been performed.

## References

1. X. Li and H. Joe, *Extreme Value Inference for CoVaR and Systemic Risk*, arXiv:2603.27458 (2026), https://arxiv.org/html/2603.27458v1.
2. K. F. Siburg and C. Strothmann, *Multivariate tail dependence and local stochastic dominance*, arXiv:2210.06842 (2022), https://arxiv.org/abs/2210.06842.
3. E. Furman, A. Kuznetsov, J. Su and R. Zitikis, *Tail dependence of the Gaussian copula revisited*, arXiv:1607.04736 (2016), https://arxiv.org/abs/1607.04736.
4. K. F. Siburg, *Comparing and measuring intermediate tail dependence*, arXiv:2610.35325 (2026), https://arxiv.org/html/2610.35325v1.
5. I. R. Savage, *Mills' ratio for multivariate normal distributions*, Journal of Research of the National Bureau of Standards B 66 (1962), 93–96.
