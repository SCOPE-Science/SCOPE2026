# The three-parameter EPQL marginal is exactly two-parameter Poisson quasi-Lindley

## Finding

The extended Poisson quasi-Lindley (EPQL) distribution defined in Definition 3.1 of Vardaki and Papageorgiou (2026) has **exactly the same collection of univariate count laws** as the two-parameter Poisson quasi-Lindley (PQL) family already presented in Definition 2.1 of that article. Its apparent third parameter does not increase marginal flexibility.

More precisely, for every \(\alpha>0\), \(\theta>0\), \(0<p<1\), and every integer \(y\geq0\), let \(\lambda=\theta/p\). Then
\[
\Pr_{\mathrm{EPQL}(\alpha,\theta,p)}(Y=y)
=\Pr_{\mathrm{PQL}(\alpha,\lambda)}(X=y).
\]
Conversely, **two EPQL parameter triples produce the same univariate law if and only if** their \(\alpha\) values agree and their \(\theta/p\) ratios agree. Every PQL distribution with positive parameters is represented by an admissible EPQL triple.

For any finite independent sample from this marginal law, the likelihood is constant on the curves \(\{(\alpha,\lambda p,p):0<p<1\}\). Consequently \(\theta\) and \(p\) are not separately identifiable from this univariate count sample; the three-parameter Fisher information, when defined, has a null vector \((0,\theta,p)\) and is singular. This is structural nonidentifiability, not a numerical estimation problem.

## Assumptions and scope

Only the **univariate** distributions in Eqs. (2.1), (2.2), (3.1), and (3.2) of the cited article are considered. The authors' explicit domains are \(\alpha>0\), \(\theta>0\), \(0<p<1\), and integer observations in \(\{0,1,2,\ldots\}\). The comparison PQL rate \(\lambda\) varies over all positive real numbers. No inference is made about joint distributions of two observed variables, known exposure factors, or sampling designs recording the underlying unthinned count.

The source's PQL mass function, written with rate \(\lambda\), is
\[
 f_{\mathrm{PQL}}(y;\alpha,\lambda)
 =\frac{\lambda}{\alpha+1}
 \frac{\alpha(\lambda+1)+\lambda(y+1)}{(\lambda+1)^{y+2}}.
\]
Its EPQL mass function is
\[
 f_{\mathrm{EPQL}}(y;\alpha,\theta,p)
 =\frac{p^y\theta}{\alpha+1}
 \frac{\alpha(\theta+p)+\theta(y+1)}{(\theta+p)^{y+2}}.
\]
Both are normalized probability laws on the nonnegative integers in the indicated parameter domains.

## Proof

**1. Exact family equality.** Substitute \(\theta=p\lambda\) into the EPQL mass function. The numerator contains \(p^y(p\lambda)\,p[\alpha(\lambda+1)+\lambda(y+1)]\), and the denominator contains \(p^{y+2}(\lambda+1)^{y+2}\); cancellation gives exactly \(f_{\mathrm{PQL}}(y;\alpha,\lambda)\). This calculation holds for every nonnegative integer \(y\), not just a finite sample. The same identity follows directly from the probability generating functions:
\[
 G_{\mathrm{EPQL}}(s)
 =\frac{\theta}{\alpha+1}
 \frac{\alpha(\theta+p-ps)+\theta}{(\theta+p-ps)^2}
 =\frac{\lambda}{\alpha+1}
 \frac{\alpha(\lambda+1-s)+\lambda}{(\lambda+1-s)^2}
 =G_{\mathrm{PQL}}(s).
\]
For the converse representation of any PQL law, take, for instance, \(p=1/2\) and \(\theta=\lambda/2\). Therefore the images of the two parameter families coincide exactly, not merely approximately.

**2. Completeness of the parameter equivalence classes.** For fixed positive \((\alpha,\lambda)\), write the PQL generating function as
\[
 G(s)=\frac{\lambda\alpha}{\alpha+1}\frac{1}{\lambda+1-s}
 +\frac{\lambda^2}{\alpha+1}\frac{1}{(\lambda+1-s)^2}.
\]
It has one finite pole, of order exactly two, at \(s=1+\lambda\), with strictly positive second-order coefficient \(\lambda^2/(\alpha+1)\). Equality of count distributions implies equality of their power-series generating functions on \(|s|<1\), hence equality of the rational functions. Equality of poles forces equal \(\lambda\); equality of the second-order coefficients then forces equal \(\alpha\). Thus the effective pair \((\alpha,\lambda)\) is uniquely identifiable as a distribution, and the full equivalence class is precisely \(\{(\alpha,\lambda p,p):0<p<1\}\).

**3. Exact likelihood and Fisher-information degeneracy.** For observations \(y_1,\ldots,y_n\) with \(n\geq1\), the EPQL log likelihood is
\[
 \ell(\alpha,\theta,p;y_1,\ldots,y_n)
 =\sum_{i=1}^{n}\log f_{\mathrm{PQL}}(y_i;\alpha,\theta/p).
\]
Because this function is constant when \((\theta,p)\) are jointly rescaled by a positive factor that stays in the parameter domain, differentiating at the interior parameters gives
\[
 \theta\,\frac{\partial\ell}{\partial\theta}
 +p\,\frac{\partial\ell}{\partial p}=0.
\]
This holds for every possible sample, so its score vector is orthogonal to the nonzero vector \((0,\theta,p)\) for every observation. Taking expected score outer products gives an information matrix with this vector in its kernel whenever the Fisher information exists. Any interior maximum of the marginal likelihood belongs to a continuum of equivalent triples.

## Verification

The standalone standard-library checker `check_epql.py` evaluates the two probability mass functions using exact rational arithmetic at \(65\) values of \(y\) for each of four distinct rational parameter triples. It likewise compares the probability generating functions at five rational arguments, verifies normalization at \(s=1\), and checks rescaled-triple invariance; all \(284\) equality tests pass. In particular, \((\alpha,\theta,p)=(1,1,1/2)\) and \((1,4/5,2/5)\) are different admissible triples with the same effective rate \(\lambda=2\), and each assigns probability \(5/9\) to zero. Exact symbolic simplification independently gives the PMF ratio \(1\), PGF difference \(0\), and the score-direction identity \(0\).

Run `python3 check_epql.py` from the directory containing this file. These finite checks corroborate the derivations but do not constitute the proof for all parameters or all count values; the algebraic identity and rational-function pole argument above do.

## Relationship to prior work

Vardaki and Papageorgiou (2026) provide both formulas as Eqs. (2.1) and (3.1) and remark that EPQL reduces to PQL when \(p=1\) (Remark 3.1), although their definition has \(0<p<1\). They also suggest greater marginal flexibility from an exposure/weighting factor. The stronger statement established here is that **every** admissible \(p\) already produces a PQL distribution with rate \(\theta/p\), and the marginal data cannot distinguish \(p\) from the rate. This is an exact comparison of the two stated families, not a claim to have invented a new count law.

Grine and Zeghdoudi (2017) introduce the base two-parameter PQL law. Altun (2019) studies a two-parameter mean/shape reparameterization of PQL, but not the three-to-two collapse of the 2026 EPQL definition. Chesneau and coauthors (2022) develop a binomial-discrete Poisson-Lindley model, identified by the 2026 source as the \(\alpha=\theta\) subfamily of EPQL (Remark 3.3). That constrained subfamily does not state the unrestricted \(\alpha\)-dependent equivalence classes or its general rank loss. The classical fact that thinning a mixed Poisson law rescales its mixing intensity supplies useful background; the contribution here is the exact collapse and inferential consequence for the subsequently published EPQL specification.

## Limitations

The result neither invalidates a **bivariate** construction nor asserts that \(p\) is unidentifiable from jointly observed variables. In the first bivariate model, conditional binomial observations can carry information about \(p\) that a single EPQL marginal does not. A known external exposure parameter can also remove the ambiguity. Likewise, any model placing independent restrictions on \(\theta\) and \(p\) is outside the unrestricted parameter domain studied here.

The source already contains the two algebraic ingredients, so the claim is a structural correction and identifiability clarification rather than priority for a general binomial-thinning theorem. The full twenty-four-page 2022 antecedent was not available for complete inspection; its accessible abstract/introduction and the explicit restricted-parameter identification in the 2026 source were compared. Possible unindexed source-specific equivalences remain an originality risk. No claim is made about unreported implementation or fitting procedures.

## References

1. M. Vardaki and H. Papageorgiou, “Poisson quasi-Lindley and Poisson-new XLindley univariate and bivariate models: derivation techniques and automobile insurance applications,” *AIMS Mathematics* **11** (2026), 3772–3810, DOI: 10.3934/math.2026154. See Definitions 2.1 and 3.1 and Remarks 3.1–3.4. https://www.aimspress.com/aimspress-data/math/2026/2/PDF/math-11-02-154.pdf
2. R. Grine and H. Zeghdoudi, “On Poisson Quasi-Lindley Distribution and its Applications,” *Journal of Modern Applied Statistical Methods* **16** (2017), 403–417, DOI: 10.22237/jmasm/1509495660. https://jmasm.com/index.php/jmasm/article/download/944/944/2711
3. E. Altun, “A new model for over-dispersed count data: Poisson quasi-Lindley regression model,” *Mathematical Sciences* **13** (2019), 241–247, DOI: 10.1007/s40096-019-0293-5. https://link.springer.com/article/10.1007/s40096-019-0293-5
4. C. Chesneau, H. S. Bakouch, Y. Akdoğan and K. Karakaya, “The Binomial-Discrete Poisson-Lindley Model: Modeling and Applications to Count Regression,” *Communications in Mathematical Research* **38** (2022), 28–51, DOI: 10.4208/cmr.2021-0045. https://www.global-sci.com/cmr/article/view/9064
