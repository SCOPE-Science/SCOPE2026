# Exact sharpness spectrum for Bernoulli least-favorable noise
## Finding
Let \(X\sim\operatorname{Bernoulli}(p)\) with \(0<p<1\), and write \(\sigma^2=p(1-p)\). For a variance budget \(v\ge0\), define
\[
L_p(v)=\inf\left\{\operatorname{Var}(\mathbb E[X\mid X+Y]):Y\perp X,\ \operatorname{Var}(Y)\le v\right\}.
\]
Then the universal covariance bound
\[
L_p(v)\ge \frac{\sigma^4}{\sigma^2+v}
\]
is sharp exactly at the arithmetic set \(v=m\sigma^2\), where \(m\in\mathbb Z_{\ge0}\). If \(v=m\sigma^2\), every noise attaining this lower bound has, up to translation, the law \(\operatorname{Bin}(m,p)\). If \(v/\sigma^2\notin\mathbb Z_{\ge0}\), then
\[
L_p(v)>\frac{\sigma^4}{\sigma^2+v}.
\]

## Assumptions and scope
The signal is a nondegenerate Bernoulli random variable, the noise is independent and square-integrable, and only its variance is constrained. Translating \(Y\) does not change either the objective or its variance. The theorem classifies exact sharpness of the covariance lower bound; it does not give a closed form for \(L_p(v)\) between integer variance ratios.

## Proof
Let \(S=X+Y\). Independence gives
\[
\operatorname{Cov}(X,S)=\operatorname{Var}(X)=\sigma^2.
\]
Since \(\mathbb E[X\mid S]\) is the orthogonal projection of \(X\) onto functions of \(S\),
\[
\operatorname{Cov}(\mathbb E[X\mid S],S)=\sigma^2.
\]
Cauchy--Schwarz therefore yields
\[
\sigma^4\le \operatorname{Var}(\mathbb E[X\mid S])\operatorname{Var}(S)
=\operatorname{Var}(\mathbb E[X\mid S])\bigl(\sigma^2+\operatorname{Var}(Y)\bigr),
\]
which proves the stated lower bound under \(\operatorname{Var}(Y)\le v\).

Suppose equality holds at a positive budget. Equality in both inequalities forces \(\operatorname{Var}(Y)=v\) and equality in Cauchy--Schwarz. Center
\[
\widetilde X=X-p,\qquad \widetilde Y=Y-\mathbb EY,\qquad T=\widetilde X+\widetilde Y.
\]
Then
\[
\mathbb E[\widetilde X\mid T]=aT,
\qquad
a=\frac{\sigma^2}{\sigma^2+v}.
\]
Because \(-p\le\mathbb E[\widetilde X\mid T]\le1-p\), the variable \(T\), hence also \(\widetilde Y\), is bounded. Its characteristic function therefore extends to an entire function.

Let \(\phi_X(z)=\mathbb E e^{iz\widetilde X}\) and \(\phi_Y(z)=\mathbb E e^{iz\widetilde Y}\). Multiplying the affine-regression identity by \(e^{izT}\), taking expectations, and differentiating characteristic functions gives the entire identity
\[
(1-a)\phi_X'(z)\phi_Y(z)=a\phi_X(z)\phi_Y'(z).
\]
For Bernoulli \(X\),
\[
\phi_X(z)=e^{-ipz}\bigl((1-p)+pe^{iz}\bigr),
\]
and every complex zero of \(\phi_X\) is simple. Choose one such zero \(z_0\). The differential identity first forces \(\phi_Y(z_0)=0\). If that zero of \(\phi_Y\) has multiplicity \(k\ge1\), comparison of the first nonzero coefficients at \(z_0\) gives
\[
1-a=ak.
\]
Thus
\[
\frac{v}{\sigma^2}=\frac{1-a}{a}=k\in\mathbb Z_{>0}.
\]
Moreover the same differential identity implies \(\phi_Y=\phi_X^k\): away from the discrete zero set the logarithmic derivatives agree, while the multiplicity computation removes the apparent singularities, and the quotient equals one at the origin. Hence \(\widetilde Y\) has the law of a sum of \(k\) independent copies of \(\widetilde X\). Equivalently, \(Y\) is a translate of \(\operatorname{Bin}(k,p)\). The zero-budget case gives a constant noise and corresponds to \(k=0\).

Conversely, if \(m\in\mathbb Z_{\ge0}\) and \(Y\) is a sum of \(m\) independent \(\operatorname{Bernoulli}(p)\) variables independent of \(X\), exchangeability of the \(m+1\) Bernoulli summands gives
\[
\mathbb E[X\mid X+Y]=\frac{X+Y}{m+1},
\]
so
\[
\operatorname{Var}(\mathbb E[X\mid X+Y])=\frac{\sigma^2}{m+1}
=\frac{\sigma^4}{\sigma^2+m\sigma^2}.
\]
Thus the lower bound is attained at every integer ratio. Finally, existence of a least-favorable noise for every square-integrable nondegenerate signal, proved by Huang, turns the nonattainability argument into the strict inequality for every noninteger ratio.

## Verification
The proof is analytic. The accompanying checker uses exact rational arithmetic to verify the integer-ratio construction for several rational values of \(p\) and \(m\), verifies the variance formula, and checks the algebraic relation between the Cauchy equality slope and the integer multiplicity. These computations are consistency checks only; the infinite classification rests on the entire-function zero-multiplicity argument above.

## Relationship to prior work
Ernst, Kagan and Rogers formulate the least-favorable-noise problem, prove that sums of \(m\) i.i.d. copies are optimal at the corresponding integer variance multiples, and show a complete convolution-semigroup solution for infinitely divisible signals. Their Bernoulli section also shows that optimizers can become structurally more complicated as the variance budget increases. The present result supplies the converse for the Bernoulli signal: the simple covariance lower bound can be attained at no other variance budgets, and equality forces the noise law itself to be the matching shifted binomial.

Huang proves existence of a least-favorable noise for every nondegenerate square-integrable signal and proves variance-budget saturation. Existence is used here only to convert failure of equality for every individual noise into strict inequality for the infimum at noninteger ratios.

Classical discrete-regression characterization papers study binomial and related laws under specified conditional-distribution structures together with regression functions. The inspected Cacoullos--Papageorgiou theorem assumes a prescribed conditional law of one integer-valued variable given the other, including convolutional families; it does not state the variance-budget sharpness spectrum above. A 1985 Papageorgiou paper was also checked at the abstract level and likewise requires a conditional-distribution specification in addition to regression.

## Limitations
The exact value and optimizer of \(L_p(v)\) for noninteger \(v/\sigma^2\) are not determined. The result concerns the conditional-mean prediction objective, not channel capacity or classification error. The originality comparison is limited by the accessibility and indexing of older characterization literature; no covering theorem was found, but a differently phrased classical characterization remains a residual literature risk.

## References
1. P. A. Ernst, A. M. Kagan, and L. C. G. Rogers, *The least favorable noise*, arXiv:2103.09794; Electronic Communications in Probability 27 (2022), DOI:10.1214/22-ECP467.
2. D. Huang, *The existence of the least favorable noise*, arXiv:2303.09023.
3. T. Cacoullos and H. Papageorgiou, *Characterizations of discrete distributions by a conditional distribution and a regression function*, Annals of the Institute of Statistical Mathematics 35 (1983), 95--103, DOI:10.1007/BF02480967.
4. H. Papageorgiou, *On Characterizing Some Discrete Distributions by a Conditional Distribution and a Regression Function*, Biometrical Journal 27 (1985), 473--479, DOI:10.1002/bimj.4710270422.
