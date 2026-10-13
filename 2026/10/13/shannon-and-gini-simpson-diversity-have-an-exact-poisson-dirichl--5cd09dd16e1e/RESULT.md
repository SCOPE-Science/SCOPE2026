# Shannon and Gini–Simpson diversity have an exact Poisson–Dirichlet covariance

## Finding

Let
\[
P=(P_i)_{i\ge1}\sim\operatorname{PD}(\alpha,\theta),
\qquad
0\le\alpha<1,
\qquad
\theta>-\alpha.
\]
Define the Shannon diversity
\[
H=-\sum_{i\ge1}P_i\log P_i
\]
and the Gini–Simpson diversity
\[
D=1-\sum_{i\ge1}P_i^2.
\]

Then
\[
\boxed{
\operatorname{Cov}(D,H)
=
\frac{\theta+\alpha}{(\theta+1)^2(\theta+2)}
}
\tag{1}
\]
and hence
\[
\operatorname{Cov}(D,H)>0
\]
throughout the nondegenerate parameter range.

Equivalently, if
\[
S_2=\sum_{i\ge1}P_i^2
\]
is Simpson concentration, then
\[
\boxed{
\operatorname{Cov}(S_2,H)
=
-\frac{\theta+\alpha}{(\theta+1)^2(\theta+2)}.
}
\tag{2}
\]

The exact marginal variances are
\[
\operatorname{Var}(D)
=
\frac{
2(1-\alpha)(\theta+\alpha)
}{
(\theta+1)^2(\theta+2)(\theta+3)
}
\tag{3}
\]
and
\[
\operatorname{Var}(H)
=
\frac{\theta+\alpha}{(\theta+1)^2(1-\alpha)}
+
\frac{1-\alpha}{\theta+1}\psi_1(2-\alpha)
-
\psi_1(\theta+2),
\tag{4}
\]
where \(\psi_1\) is the trigamma function. Therefore
\[
\boxed{
\operatorname{Corr}(D,H)
=
\frac{
(\theta+\alpha)/((\theta+1)^2(\theta+2))
}{
\sqrt{\operatorname{Var}(D)\operatorname{Var}(H)}
}.
}
\tag{5}
\]

For every fixed \(0\le\alpha<1\), as \(\theta\to\infty\),
\[
\boxed{
\operatorname{Corr}(D,H)
\longrightarrow
\frac{1}{
\sqrt{
2(1-\alpha)
\left(
(1-\alpha)\psi_1(1-\alpha)-1
\right)
}
}.
}
\tag{6}
\]

In particular, in the Dirichlet-process case \(\alpha=0\),
\[
\operatorname{Corr}(D,H)
\longrightarrow
\frac1{\sqrt{2(\pi^2/6-1)}}
=
0.8804959104\ldots.
\tag{7}
\]

Thus increasing concentration makes both diversities individually more concentrated, but it does not make their standardized fluctuations asymptotically independent.

## Assumptions and scope

The law is the two-parameter Poisson–Dirichlet law on ranked or size-biased random frequencies. The parameter region is
\[
0\le\alpha<1,
\qquad
\theta>-\alpha.
\]
At \(\alpha=0\), this means \(\theta>0\).

The Shannon entropy is finite in mean and variance in this parameter region. All logarithms are natural.

Equation (1) is an exact prior identity for the random probability vector itself. It is not a posterior covariance conditional on observed species counts.

The current MSC2020 classification used here is \(60G57\), random measures.

## Proof

For real exponents \(u,v>\alpha\), define
\[
S_u=\sum_{i\ge1}P_i^u.
\]

The two-parameter Poisson–Dirichlet sampling formula, or equivalently the first two size-biased frequencies, gives the mixed power-sum identity
\[
\boxed{
\mathbb E[S_uS_v]
=
\frac{
(1-\alpha)_{u+v-1}
+
(\theta+\alpha)
(1-\alpha)_{u-1}
(1-\alpha)_{v-1}
}{
(\theta+1)_{u+v-1}
},
}
\tag{8}
\]
where the generalized rising factorial is
\[
(x)_t=\frac{\Gamma(x+t)}{\Gamma(x)}.
\]

For completeness, split the product \(S_uS_v\) into equal-index and distinct-index terms. The equal-index contribution is
\[
\mathbb E S_{u+v}
=
\frac{(1-\alpha)_{u+v-1}}
{(\theta+1)_{u+v-1}}.
\]
For the distinct terms use the size-biased representation
\[
\widetilde P_1=V_1,
\qquad
\widetilde P_2=(1-V_1)V_2,
\]
with independent
\[
V_1\sim\operatorname{Beta}(1-\alpha,\theta+\alpha),
\qquad
V_2\sim\operatorname{Beta}(1-\alpha,\theta+2\alpha).
\]
Beta moments give the second term of (8). This also supplies an analytic expression in a neighborhood of \((u,v)=(2,1)\), so the logarithmic derivative below is justified directly from the explicit beta integrals.

Because
\[
H
=
-\left.\frac{\partial S_v}{\partial v}\right|_{v=1},
\]
equation (8) yields
\[
\mathbb E[S_2H]
=
-\left.
\frac{\partial}{\partial v}
\mathbb E[S_2S_v]
\right|_{v=1}.
\tag{9}
\]

The marginal means are
\[
\mathbb E S_2
=
\frac{1-\alpha}{\theta+1}
\tag{10}
\]
and
\[
\mathbb EH
=
\psi(\theta+1)-\psi(1-\alpha),
\tag{11}
\]
where \(\psi\) is the digamma function.

Differentiating (8) at \((u,v)=(2,1)\), using
\[
\frac{d}{dt}(x)_t
=
(x)_t
\left[
\psi(x+t)-\psi(x)
\right],
\]
and then subtracting the product of (10) and (11) gives
\[
\operatorname{Cov}(S_2,H)
=
-\frac{\theta+\alpha}{(\theta+1)^2(\theta+2)}.
\]
Since \(D=1-S_2\), equation (1) follows.

For the variance of \(D\), equation (8) at \(u=v=2\) gives
\[
\mathbb E S_2^2
=
\frac{
(1-\alpha)_3
+
(\theta+\alpha)(1-\alpha)^2
}{
(\theta+1)_3
}.
\]
Subtracting the square of (10) simplifies to (3).

The Shannon variance (4) follows from the standard Poisson–Dirichlet entropy second moment. Substitution of (1), (3), and (4) gives (5).

Finally,
\[
\operatorname{Cov}(D,H)\sim\theta^{-2}
\]
and
\[
\operatorname{Var}(D)
\sim
2(1-\alpha)\theta^{-3}.
\]
Using the trigamma recurrence
\[
\psi_1(2-\alpha)
=
\psi_1(1-\alpha)
-
\frac1{(1-\alpha)^2}
\]
and the large-argument expansion
\[
\psi_1(\theta+2)\sim\theta^{-1},
\]
equation (4) gives
\[
\operatorname{Var}(H)
\sim
\left[
(1-\alpha)\psi_1(1-\alpha)-1
\right]\theta^{-1}.
\]
Combining these three asymptotics proves (6), and (7) follows from
\[
\psi_1(1)=\frac{\pi^2}{6}.
\]

## Verification

The accompanying deterministic checker evaluates the mixed moment in two independent ways over a parameter grid.

The first route differentiates the gamma-ratio expression in (8) numerically at \(v=1\).

The second route evaluates the equal-index and distinct-index contributions directly from beta moments of the first two size-biased frequencies. Logarithmic beta moments are obtained by differentiating the beta integral.

For every checked parameter pair the two routes agree with the closed covariance (1) to high precision. The checker also verifies the variance formula (3), positivity and subunit magnitude of the exact correlation, and the large-\(\theta\) limit (6) for several values of \(\alpha\).

These finite numerical checks are supplementary. The proof for the full parameter region is the analytic differentiation of (8).

## Relationship to prior work

Cerquetti develops prior and posterior moments for Tsallis diversity under Gnedin–Pitman priors. In the two-parameter Poisson–Dirichlet specialization, the paper gives separate formulas for the mean and variance of fixed-order Tsallis diversity and for the mean and variance of Shannon entropy. Its full derivation uses power sums and exchangeable partition probabilities, but the inspected theorem statements and proofs do not state the cross-covariance between Shannon and Gini–Simpson diversity.

Archer, Park, and Pillow derive the mean and variance of Shannon entropy under Pitman–Yor priors by size-biased stick breaking. Their appendix gives precisely the first- and second-size-biased-frequency machinery needed for logarithmic moments, but the inspected full paper does not treat Simpson or Gini–Simpson diversity.

Recent work on Bayesian inference for the Gini–Simpson index describes Shannon and Gini–Simpson as two standard diversity measures but develops inference for the latter rather than their exact joint prior law.

The exact covariance in (1) is therefore a cross-index statement that is not supplied by the separate marginal moment formulas. The nonzero limit in (6) is an additional joint consequence: concentration suppresses the scale of both fluctuations without eliminating their standardized alignment.

## Limitations

The finding concerns the prior Poisson–Dirichlet random frequencies. Posterior covariances after observing species counts are not derived here.

The result does not claim that Shannon and Gini–Simpson diversity are monotonically related sample by sample; it is a second-order dependence statement.

General Gnedin–Pitman priors need not share the simple rational covariance (1).

Mixed power-sum formulas are classical tools in Poisson–Dirichlet theory. Although the closest full entropy/diversity sources were inspected and no equivalent cross-covariance statement was found, an older source may contain the same derivative consequence under different notation.

## References

1. A. Cerquetti, “Bayesian nonparametric estimation of Tsallis diversity indices under Gnedin–Pitman priors,” arXiv:1404.3441, first public version 2014-04-14.
2. E. Archer, I. M. Park, and J. W. Pillow, “Bayesian Entropy Estimation for Countable Discrete Distributions,” *Journal of Machine Learning Research* 15 (2014), 2833–2868; arXiv:1302.0328, first public version 2013-02-02.
3. J. Pitman and M. Yor, “The two-parameter Poisson–Dirichlet distribution derived from a stable subordinator,” *Annals of Probability* 25 (1997), 855–900.
4. P. G. Bissiri, S. Corradin, and A. Ongaro, “Nonparametric Bayesian inference for the Gini-Simpson index,” arXiv:2607.25737.
