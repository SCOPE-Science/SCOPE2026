# The printed Burr-Hatke observed-information matrix has the wrong sign
## Finding
For the Burr-Hatke model,
\[
F(t;\alpha)=1-\frac{e^{-\alpha t}}{t+1},
\qquad
f(t;\alpha)=\frac{e^{-\alpha t}\{\alpha(t+1)+1\}}{(t+1)^2},
\qquad t>0,\ \alpha>0.
\]

Under the progressive Type-II censored sampling scheme used in the source, the parameter-dependent terms of the log-likelihood separate in \(\alpha_1\) and \(\alpha_2\). Direct differentiation gives
\[
\frac{\partial^2\ell}{\partial\alpha_1^2}
=-\sum_{i=1}^n\sum_{j=1}^k
\left(\frac{x_{ij}+1}{\alpha_1(x_{ij}+1)+1}\right)^2
\]
and
\[
\frac{\partial^2\ell}{\partial\alpha_2^2}
=-\sum_{i=1}^n
\left(\frac{y_i+1}{\alpha_2(y_i+1)+1}\right)^2,
\qquad
\frac{\partial^2\ell}{\partial\alpha_1\partial\alpha_2}=0.
\]

The source correctly defines observed Fisher information as
\[
I(\eta)=-\nabla^2\ell(\eta).
\]
It then prints both diagonal entries with the same minus signs as the Hessian. Those printed entries are therefore the Hessian, not the observed information.

The corrected matrix is
\[
\boxed{
I(\eta)=
\begin{pmatrix}
\displaystyle\sum_{i=1}^n\sum_{j=1}^k\left(\frac{x_{ij}+1}{\alpha_1(x_{ij}+1)+1}\right)^2&0\\[12pt]
0&\displaystyle\sum_{i=1}^n\left(\frac{y_i+1}{\alpha_2(y_i+1)+1}\right)^2
\end{pmatrix}.
}
\]
For every nonempty positive sample this matrix is positive definite, whereas the matrix printed in the article is negative definite.

The article next uses
\[
\operatorname{var}(\widehat\delta_{s,k})\approx\nabla g(\eta)^\top I(\eta)^{-1}\nabla g(\eta).
\]
With the printed negative matrix, this quadratic form is strictly negative whenever \(\nabla g(\eta)\ne0\). Thus the square roots appearing in the ordinary and logit-Wald intervals are not real-valued under the literal displayed formulas.

For a concrete positive censored sample with \(\alpha_1=1.3\) and \(\alpha_2=0.8\), the bundled replay evaluates the conventional \(k=s=1\) stress-strength reliability \(P(X>Y)\). It obtains
\[
\boxed{\operatorname{var}_{\mathrm{correct}}=0.020434480354064\ldots}
\]
and
\[
\boxed{\operatorname{var}_{\mathrm{printed}}=-0.020434480354064\ldots}.
\]

## Assumptions and scope
All observations and model parameters are positive, as required by the Burr-Hatke model. The result concerns the displayed analytic observed-information matrix and formulas that directly use its inverse.

The score equations and maximum-likelihood point estimates are unchanged. Bootstrap and Bayesian procedures are not reassessed.

The article reports numerical confidence intervals, so its computational implementation may already have used the positive matrix. No claim is made about unavailable software.

## Proof
The censoring-count terms in the log-likelihood are linear in the corresponding parameter, so they vanish after two derivatives. For a strength observation,
\[
\frac{\partial}{\partial\alpha_1}\log[\alpha_1(x_{ij}+1)+1]
=\frac{x_{ij}+1}{\alpha_1(x_{ij}+1)+1},
\]
and one more derivative gives the negative square appearing above. The stress calculation is identical. Separability gives zero cross derivative.

By definition, observed information is the negative Hessian, so negating these negative diagonal entries yields the positive matrix in the finding.

If \(D\) is the corrected positive diagonal matrix, the article's printed matrix is \(-D\). Hence
\[
(-D)^{-1}=-D^{-1}.
\]
For every nonzero vector \(v\),
\[
v^\top D^{-1}v>0,
\qquad
v^\top(-D)^{-1}v<0.
\]
Taking \(v=\nabla g(\eta)\) proves the delta-variance consequence.

## Verification
The standalone checker implements the two parameter-dependent log-likelihood components for a positive progressively censored sample. Central finite differences of the score agree with the analytic negative second derivatives; their negatives are positive observed-information entries.

For \(k=s=1\), the checker evaluates
\[
P(X>Y)=\int_0^\infty \frac{e^{-\alpha_1y}}{1+y}\frac{e^{-\alpha_2y}\{\alpha_2(1+y)+1\}}{(1+y)^2}\,dy
\]
and obtains a nonzero numerical gradient. Substitution gives the positive corrected variance and its exact negative under the printed matrix.

The finite calculation illustrates the general analytic sign proof.

## Relationship to prior work
The primary article itself defines observed Fisher information as the negative Hessian and then, in the next displayed formulas, retains the Hessian's negative signs in both diagonal entries. The contradiction is internal to consecutive formulas.

The source cites standard delta-method theory for the reliability variance. General likelihood theory fixes the negative-Hessian convention but does not supply this source-specific correction without differentiating the paper's censored likelihood.

Focused searches using the exact DOI, Burr-Hatke model name, progressive-censoring setting, observed-information terminology, delta-method variance, and correction terminology did not locate a published correction of these signs.

## Limitations
The result does not establish which sign was used in the authors' numerical code. It does not recompute every reported confidence interval. Bootstrap and Bayesian interval calculations are outside its scope. A recent or unindexed correction could exist.

## References
1. R. El-Desokey, M. M. El-Awady, H. Haj Ahmad, and A. El-Gohary, “Multicomponent stress-strength reliability inference under progressive Type-II censoring: A one-parameter model with applications to power systems and earthquake data,” AIMS Mathematics 11 (2026), 8031–8064. DOI: 10.3934/math.2026331.
2. G. W. Oehlert, “A Note on the Delta Method,” The American Statistician 46 (1992), 27–29. DOI: 10.1080/00031305.1992.10475842.
