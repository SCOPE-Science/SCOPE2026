# Sharp exceedance–concentration dependence for Dirichlet compositions

## Finding

Let \(m\ge2\), let every \(\alpha_j>0\), and let \(X=(X_1,\ldots,X_m)\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_m)\). For every real \(q>1\), define the power-concentration statistic and tagged exceedance event by
\[
Q_q=\sum_{j=1}^m X_j^q,\qquad I_i(t)={\bf1}\{X_i>t\},\qquad 0<t<1.
\]
Put \(A=\sum_j\alpha_j\), \((z)_q=\Gamma(z+q)/\Gamma(z)\), and
\[
c_{i,q}=\frac{\sum_{j\ne i}(\alpha_j)_q}{(A-\alpha_i)_q},\qquad
\mu_q=\mathbb E Q_q=\frac{\sum_{j=1}^m(\alpha_j)_q}{(A)_q}.
\]
Then the entire covariance sign pattern of \(I_i(t)\) and \(Q_q\), as \(t\) ranges over \((0,1)\), is determined as follows:

* If \(c_{i,q}\le\mu_q\), then \(\operatorname{Cov}(I_i(t),Q_q)>0\) for every \(0<t<1\).
* If \(c_{i,q}>\mu_q\), there is exactly one \(t_{i,q}\in(0,1)\) where the covariance is zero; it is strictly negative for \(0<t<t_{i,q}\) and strictly positive for \(t_{i,q}<t<1\).

For a **symmetric** Dirichlet vector, with \(\alpha_j=\alpha>0\) for all \(j\), the second alternative occurs for every real \(q>1\). Consequently the exceedance count \(K_t=\sum_j I_j(t)\) has exactly one negative-to-positive covariance transition with \(Q_q\), for every \(m\ge2\), \(\alpha>0\), and \(q>1\).

For the quadratic Simpson–Greenwood concentration \(Q_2\), the transition is explicit even with unequal parameters. Fix \(i\), write \(a=\alpha_i\), \(b=A-a\), \(c=c_{i,2}\), and denote the beta density by \(f_{a,b}(t)=t^{a-1}(1-t)^{b-1}/B(a,b)\). Then
\[
\boxed{\operatorname{Cov}(I_i(t),Q_2)
=\frac{(1+c)t(1-t)f_{a,b}(t)}{A+1}
\left(t-\theta_i\right),}
\qquad
\theta_i=\frac{c(a+2b+1)-(a+1)}{A(1+c)}<1.
\]
Thus \(\theta_i\le0\) is exactly the no-reversal regime, while \(0<\theta_i<1\) gives the unique reversal at \(t=\theta_i\).

In the symmetric case, \(\theta_i=(\alpha+1)/(m\alpha+2)\) and
\[
\boxed{\operatorname{Cov}(K_t,Q_2)
=\frac{m(m\alpha+2)}{((m-1)\alpha+1)(m\alpha+1)}
\,t(1-t)f_{\alpha,(m-1)\alpha}(t)
\left(t-\frac{\alpha+1}{m\alpha+2}\right).}
\]
For uniform spacings (\(\alpha=1\)) this simplifies to
\[
\boxed{\operatorname{Cov}(K_t,Q_2)
=\frac{m-1}{m+1}t(1-t)^{m-1}\bigl((m+2)t-2\bigr).}
\]
The sharp uniform-spacing critical threshold is therefore \(2/(m+2)\), and at \(t=s/m\) with fixed \(s>0\),
\[
\lim_{m\to\infty}m\operatorname{Cov}(K_{s/m},Q_2)
=s(s-2)e^{-s}.
\]
Heterogeneous parameters may eliminate the reversal: for \(m=3\) and \(\alpha=(a,u,u)\), the first coordinate has
\[
\theta_1=\frac{u(4u+3-a)}{(a+2u)(3u+2)}.
\]
Hence its covariance with \(Q_2\) changes sign exactly once when \(a<4u+3\), and is positive at all \(0<t<1\) when \(a\ge4u+3\).

## Assumptions and scope

All concentration parameters are strictly positive and finite; all coordinates are strictly between zero and one almost surely. The exponent is real and strictly greater than one. The quadratic closed forms require \(q=2\). \(K_t\) counts Dirichlet **mass components**, not categories discovered in a separate multinomial sample. In the broken-stick representation, \(m\) is the number of gaps (obtained from \(m-1\) independent uniform cuts of an interval, or \(m\) independent circular uniform points).

The result concerns covariance, not stochastic ordering or independent exceedances. At the excluded boundary \(q=1\), \(Q_1=1\) and every covariance is zero.

## Proof

Fix \(i\), put \(a=\alpha_i\), \(b=A-a>0\), and write \(Y=X_i\). The Dirichlet aggregation and neutrality identities give \(Y\sim\operatorname{Beta}(a,b)\). Conditional on \(Y=x\), the remaining normalized proportions have Dirichlet parameters \((\alpha_j)_{j\ne i}\). Their power moments yield
\[
g(x):=\mathbb E(Q_q\mid Y=x)=x^q+c_{i,q}(1-x)^q.
\]
Thus, writing \(f\) for the beta density and \(\mu_q=\mathbb E g(Y)\),
\[
H(t):=\operatorname{Cov}(I_i(t),Q_q)
=\int_t^1\bigl(g(x)-\mu_q\bigr)f(x)\,dx,
\qquad H(0)=H(1)=0.
\tag{1}
\]
For \(q>1\), \(g\) is strictly convex on \((0,1)\), decreases initially and increases ultimately, with a unique interior minimum, while \(g(0)=c_{i,q}\) and \(g(1)=1>\mu_q\). The last inequality is strict because \(Q_q<1\) almost surely. The minimum of \(g\) is strictly less than \(\mu_q\), since \(Y\) is nondegenerate.

If \(c_{i,q}\le\mu_q\), the continuous function \(g-\mu_q\) has exactly one zero \(v\in(0,1)\), and is strictly negative on \((0,v)\) and positive on \((v,1)\). Equation (1) shows that \(H\) increases from zero to a positive maximum and then decreases to zero; hence \(H(t)>0\) for every interior threshold.

If \(c_{i,q}>\mu_q\), strict convexity gives precisely two roots \(0<u<v<1\) of \(g-\mu_q\). Consequently \(H\) decreases below zero on \((0,u)\), increases strictly on \((u,v)\), and decreases to zero from above on \((v,1)\). There is one and only one interior zero, necessarily in \((u,v)\). This proves the full tagged classification.

For symmetry, \(c_{i,q}=(m-1)(\alpha)_q/(((m-1)\alpha)_q)\) and \(\mu_q=m(\alpha)_q/(m\alpha)_q\). The map
\[
z\longmapsto\frac{(z)_q}{z}=\frac{\Gamma(z+q)}{\Gamma(z+1)}
\]
is strictly increasing for \(z>0\) when \(q>1\), since its logarithmic derivative is \(\psi(z+q)-\psi(z+1)>0\) and the digamma function \(\psi\) is strictly increasing. Evaluating this increase at \((m-1)\alpha\) and \(m\alpha\) proves \(c_{i,q}>\mu_q\). Symmetry then gives \(\operatorname{Cov}(K_t,Q_q)=m H(t)\), completing the general-power assertion.

For \(q=2\), neutrality gives \(g(x)=x^2+c(1-x)^2\) and
\[
\mu_2=\frac{a(a+1)+c b(b+1)}{A(A+1)}.
\]
Let \(\theta_i\) be as in the finding and define
\[
F(t)=\frac{(1+c)t(1-t)f_{a,b}(t)}{A+1}(t-\theta_i).
\]
The elementary beta-density identity
\[
\frac{d}{dt}\bigl[t(1-t)f_{a,b}(t)\bigr]
=(a-At)f_{a,b}(t)
\]
and direct coefficient comparison show \(F'(t)=-(g(t)-\mu_2)f_{a,b}(t)=H'(t)\). Both functions tend to zero as \(t\uparrow1\), even for beta parameters below one, so \(F=H\) on \((0,1)\). Since \(0<c\le1\),
\[
A(1+c)-\bigl[c(a+2b+1)-(a+1)\bigr]
=2a+b+1-c(b+1)>0,
\]
so \(\theta_i<1\). The sign formula therefore gives the complete quadratic classification, including the boundary \(\theta_i=0\).

In the symmetric case \(c=(\alpha+1)/((m-1)\alpha+1)\), so substitution gives the two symmetric formulas. The uniform case uses \(f_{1,m-1}(t)=(m-1)(1-t)^{m-2}\). Substituting \(t=s/m\), multiplying by \(m\), and taking limits gives \(s(s-2)e^{-s}\). For the three-component example, substituting \(c=(u+1)/(2u+1)\), \(b=2u\) into \(\theta_i\) gives its stated expression and exact parameter boundary.

## Verification

The accompanying standalone `verify_exceedance_concentration.py` evaluates beta-tail polynomial integrals using Python's exact rational arithmetic, without numerical integration or fitted constants. Running `python verify_exceedance_concentration.py` produced `PASS: 888 exact rational beta-tail/covariance comparisons`, including several asymmetric Dirichlet parameters, the zero-boundary vector \((7,1,1)\), the no-reversal vector \((8,1,1)\), symmetric parameter families, and higher integer powers.

The all-parameter and all-real-exponent claims follow from the analytic argument above, not from finite tests. For the quadratic formula, the independent exact integration checks do not reuse the beta-derivative identity used in the proof.

## Relationship to prior work

Royen (arXiv:1008.4059; earliest public date 2010-08-24) develops exact distribution representations and quantiles for the Dirichlet quadratic power sum, including Greenwood's statistic; its inspected introduction and main theorems concern marginal laws rather than covariance with threshold-exceedance counts or one-switch classification. Huillet and Paroissin (arXiv:0809.4181; earliest public date 2008-09-24) analyze finite Dirichlet partitions, diversity power sums, and richness of **sampled** species; those sampled-count results do not imply the present random-mass exceedance law. Goldstein and Reinert (arXiv:1207.1460; earliest public date 2012-07-05) provide the general beta Stein operator. That operator is an available method for deriving the quadratic formula, but does not state the Dirichlet power-sum sign classification, the symmetric real-power one-switch theorem, or the asymmetric no-switch boundary.

Related indexed results on covariance of empirical sample richness with a collision-based Simpson estimator, and on richness versus occupancy frequency counts, were inspected in full. They concern statistics computed from finite iid categorical draws, not exceedances of latent Dirichlet proportions. An earlier uniform-spacing result giving covariance of each **ranked gap length** with the quadratic sum supplies integrated information but does not determine the pointwise exceedance-covariance sign.

## Limitations

The theorem identifies covariance signs, not full conditional stochastic ordering or inferential test power. It does not assert any monotone single-switch property for the **sum** of exceedance indicators under arbitrary nonidentical Dirichlet parameters: the asymmetric classification is tagged-coordinate-wise. For \(q\ne2\), the switch is characterized uniquely but not given in elementary closed form. The proof does not classify dependent non-Dirichlet compositions or sample-based occupancy exceedance statistics. Classical beta integral identities and Dirichlet moments provide the core ingredients, so priority under a different ecological or spacing-statistics notation remains an explicit historical risk.

## References

1. T. Huillet and C. Paroissin, “Sampling from Dirichlet populations: estimating the number of species,” arXiv:0809.4181, first publicly submitted 2008-09-24, https://arxiv.org/abs/0809.4181.
2. T. Royen, “The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic,” arXiv:1008.4059, first publicly submitted 2010-08-24, https://arxiv.org/abs/1008.4059.
3. L. Goldstein and G. Reinert, “Stein's method for the Beta distribution and the Pólya–Eggenberger urn,” arXiv:1207.1460, first publicly submitted 2012-07-05, https://arxiv.org/abs/1207.1460.
