# Two visits identify a nonparametric closed binomial N-mixture

**Same-model review: passed. Independent audit: not yet performed.**

## Setup

Let \(N\) be a nonnegative integer-valued latent abundance variable with
\[
0<\mu=\mathbb E N<\infty,\qquad \mathbb E N^2<\infty.
\]
At each sampling unit, suppose two repeated counts satisfy, conditionally on \(N\),
\[
Y_1\mid N\sim {\rm Bin}(N,p_1),\qquad
Y_2\mid N\sim {\rm Bin}(N,p_2),
\]
with \(p_1,p_2\in(0,1]\), and \(Y_1,Y_2\) conditionally independent given \(N\).
The distribution of \(N\) is otherwise completely unrestricted and is common across sampling units.

This is the standard closed binomial repeated-count observation mechanism, but without a Poisson, negative-binomial, zero-inflated, mixed-Poisson, finite-support, or other parametric assumption on abundance.

## Main theorem: two visits identify both detection probabilities

Write
\[
a_j=\mathbb E Y_j,\qquad
b_j=\mathbb E[Y_j(Y_j-1)],\qquad
c=\mathbb E[Y_1Y_2].
\]
Then
\[
\boxed{
p_1=\frac{c}{a_2}-\frac{b_1}{a_1},
\qquad
p_2=\frac{c}{a_1}-\frac{b_2}{a_2}.
}
\]
Consequently
\[
\boxed{\mu=\frac{a_1}{p_1}=\frac{a_2}{p_2}}
\]
and the first two factorial moments of the latent abundance are identified:
\[
\mathbb E[N(N-1)]=\frac{b_j}{p_j^2}.
\]

For equal detection probabilities \(p_1=p_2=p\), this becomes
\[
\boxed{
p=\frac{\mathbb E(Y_1Y_2)-\mathbb E[Y_1(Y_1-1)]}{\mathbb E Y_1}
=1-\frac{\operatorname{Var}(Y_1)-\operatorname{Cov}(Y_1,Y_2)}{\mathbb E Y_1}.
}
\]
The equal-\(p\) moment formula itself is not claimed as new: Dennis, Morgan and Ridout (2015) gave the equivalent method-of-moments expression for their mixed-Poisson N-mixture model. The point here is that the cancellation does not require mixed-Poisson or even overdispersed abundance, and it also works visit by visit when \(p_1\ne p_2\).

### Proof

Conditional binomial moments give
\[
\mathbb E Y_j=p_j\mathbb E N,
\qquad
\mathbb E[Y_j(Y_j-1)]=p_j^2\mathbb E[N(N-1)].
\]
Conditional independence of the two visits gives
\[
\mathbb E(Y_1Y_2)=p_1p_2\mathbb E N^2.
\]
Therefore
\[
\frac{\mathbb E(Y_1Y_2)}{\mathbb E Y_2}
-\frac{\mathbb E[Y_1(Y_1-1)]}{\mathbb E Y_1}
=
p_1\frac{\mathbb E N^2-\mathbb E[N(N-1)]}{\mathbb E N}
=p_1,
\]
and the second formula is symmetric.

## Full nonparametric identification of the abundance law

Let
\[
F(z)=\mathbb E z^N
\]
be the probability-generating function of the latent abundance and let
\[
G_j(s)=\mathbb E s^{Y_j}
\]
be the marginal pgf of visit \(j\). Binomial thinning gives
\[
G_j(s)=F(1-p_j+p_js),\qquad 0\le s\le1.
\]
Once \(p_j\) has been identified by the theorem, the observed marginal law of \(Y_j\) determines \(F(z)\) for every
\[
z\in[1-p_j,1].
\]
A probability pgf is analytic on the open unit disk. Since the interval \((1-p_j,1)\) has accumulation points inside that disk, the identity theorem implies that these values determine \(F\) uniquely throughout the unit disk, and therefore determine every coefficient
\[
\Pr(N=n),\qquad n=0,1,\ldots.
\]

Hence the exact joint law of two repeated counts structurally identifies
\[
\boxed{(p_1,p_2,\ \mathcal L(N))}
\]
within the stated nonparametric model class.

This is an identification statement, not a claim of numerically stable recovery. Recovering distant pgf coefficients from values on a proper subinterval can be severely ill-conditioned, especially when detection probabilities are small.

## Sharp one-visit versus two-visit boundary

With only one visit, the unrestricted model class is not globally identifiable. For example, if the observed count is
\[
Y\sim {\rm Poisson}(\lambda),
\]
then for every \(p\in(0,1]\),
\[
N\sim {\rm Poisson}(\lambda/p),\qquad Y\mid N\sim{\rm Bin}(N,p)
\]
produces exactly the same observed law. Thus neither \(p\) nor the latent abundance law is globally determined by one count marginal.

With two conditionally independent repeated counts and finite nonzero second moment, the theorem above identifies both visit-specific detection probabilities and then the entire latent law. Therefore, for the unrestricted closed binomial N-mixture class considered here, two visits form a sharp structural-identification threshold:
\[
\boxed{\text{one visit is globally nonidentifying; two visits are identifying}.}
\]

## More than two visits: overidentifying restrictions

For \(T\ge3\), each detection probability \(p_j\) can be recovered using any other visit \(k\ne j\):
\[
p_j=
\frac{\mathbb E(Y_jY_k)}{\mathbb E Y_k}
-\frac{\mathbb E[Y_j(Y_j-1)]}{\mathbb E Y_j}.
\]
Thus the population quantities computed with different reference visits must agree. Equivalently,
\[
\frac{\mathbb E(Y_jY_k)}{\mathbb E Y_k}
=
\frac{\mathbb E(Y_jY_\ell)}{\mathbb E Y_\ell},
\qquad k,\ell\ne j.
\]
These are distribution-free overidentifying restrictions for the closed independent-binomial observation mechanism. Failure of these equalities can diagnose departures such as visit-to-visit dependence or detection heterogeneity not represented by fixed \(p_j\).

## Literature context and originality boundary

Royle (2004) introduced the binomial N-mixture framework for repeated counts and modeled site abundance through a mixing distribution, with Poisson as the basic example. Dennis, Morgan and Ridout (2015) derived moment estimators for a mixed-Poisson N-mixture model. Their equations imply, in the equal-detection case,
\[
p=(m_1-m_2+m_{12})/m_1,
\]
which is algebraically the equal-\(p\) specialization displayed above. That estimator and the Poisson correlation identity are therefore not claimed as new.

Nonparametric abundance distributions have also appeared in related ecological detection models. Guillera-Arroita, Ridout and Morgan (2012), for example, explicitly fit finite-support nonparametric site-abundance distributions in a continuous-detection model and discuss their relation to repeated-count N-mixtures. Barker et al. (2018) emphasized severe practical robustness and estimability problems for N-mixtures, including visit-varying detection, while Madsen and Royle (2023) reviewed continuing identifiability concerns.

To the best of our knowledge, the specific contribution here is the distribution-free identification theorem for the ordinary closed binomial repeated-count model: with an arbitrary count-valued abundance law of finite second moment, two visits identify visit-specific detection probabilities by the displayed cancellation formula, after which a marginal pgf identifies the entire unrestricted abundance distribution. The corresponding one-visit nonidentifiability example makes the one-versus-two visit boundary sharp. We did not find this full nonparametric theorem, its visit-specific formula, or the sharp threshold stated in the checked N-mixture, binomial-thinning, and nonparametric-abundance literature.

The main originality risk is that the argument is elementary once the conditional moment identities are written down, and an equivalent result may exist under terminology from repeated binomial thinning, random-size binomial mixtures, or older capture-count literature. Dennis et al. (2015) is especially close: the equal-\(p\) first-stage moment formula is already present there, but under a mixed-Poisson abundance model and without the unrestricted-law identification conclusion.

## Scientific limitations

The theorem depends on the closed-population model and on conditional independence of visits given \(N\). It also assumes a common visit-specific detection probability for all individuals and sampling units represented by the model. Individual heterogeneity in detection, site-level random detection effects, double counting within a visit, population change between visits, or residual dependence between visits can invalidate the moment cancellation.

The displayed moment identification requires \(0<\mathbb EN<\infty\), \(\mathbb EN^2<\infty\), and \(p_j>0\). The pgf uniqueness argument establishes population-level structural identification but not a well-conditioned nonparametric estimator. In finite samples, plug-in moment estimates may fall outside the admissible range and analytic continuation of a pgf may be unstable. The result therefore does not overturn the practical robustness concerns in the N-mixture literature.

## Reproducibility

`artifacts/verify_exact.py` uses exact rational arithmetic to check the moment-identification identities over a finite collection of latent abundance laws and detection probabilities, including underdispersed and overdispersed examples. `artifacts/VERIFICATION.txt` records the verified output. These computations support the algebraic proof but do not replace it.

## References

1. J. A. Royle, “N-Mixture Models for Estimating Population Size from Spatially Replicated Counts,” *Biometrics* 60 (2004), 108–115. https://doi.org/10.1111/j.0006-341X.2004.00142.x
2. E. B. Dennis, B. J. T. Morgan and M. S. Ridout, “Computational aspects of N-mixture models,” *Biometrics* 71 (2015), 237–246. https://doi.org/10.1111/biom.12246
3. G. Guillera-Arroita, M. S. Ridout and B. J. T. Morgan, “Models for species-detection data collected along transects in the presence of abundance-induced heterogeneity and clustering in the detection process,” *Methods in Ecology and Evolution* 3 (2012), 358–367. https://doi.org/10.1111/j.2041-210X.2011.00159.x
4. R. J. Barker, M. R. Schofield, W. A. Link and J. R. Sauer, “On the reliability of N-mixture models for count data,” *Biometrics* 74 (2018), 369–377. https://doi.org/10.1111/biom.12734
5. M. Kéry, “Identifiability in N-mixture models: a large-scale screening test with bird data,” *Ecology* 99 (2018), 281–288. https://doi.org/10.1002/ecy.2093
6. L. Madsen and J. A. Royle, “A review of N-mixture models,” *WIREs Computational Statistics* 15 (2023), e1625. https://doi.org/10.1002/wics.1625
7. F. W. Steutel and K. van Harn, “Discrete analogues of self-decomposability and stability,” *Annals of Probability* 7 (1979), 893–899.
