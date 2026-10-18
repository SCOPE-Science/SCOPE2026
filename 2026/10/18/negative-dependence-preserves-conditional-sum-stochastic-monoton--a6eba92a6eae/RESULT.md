# Negative dependence preserves conditional-sum stochastic monotonicity for exponential FGM pairs

## Finding

**Theorem (sharp separation of conditional stochastic and likelihood-ratio orders).** Let \(\lambda>0\), let \(\theta\in[-1,1]\), and let \((X,Y)\) have exponential margins of common rate \(\lambda\) and a Farlie–Gumbel–Morgenstern (FGM) copula
\[
 C_\theta(u,v)=uv\{1+\theta(1-u)(1-v)\},\qquad 0\le u,v\le1.
\]
Put \(S=X+Y\). For **every** \(0<s_1<s_2\), there is a coupling of the regular conditional vectors given \(S=s_1\) and \(S=s_2\) in which **both components increase strictly almost surely**. Thus
\[
 (X,Y)\mid\{S=s_1\}\ <_{\mathrm{st}}\ (X,Y)\mid\{S=s_2\}
\]
in the coordinatewise multivariate usual stochastic sense; in particular, for every coordinatewise nondecreasing measurable function with existing expectations, its conditional expectation is nondecreasing in the observed sum.

By contrast, the conditional laws of either single coordinate are increasing in **likelihood-ratio order** as the sum increases **if and only if** \(\theta\ge0\). For \(-1\le\theta<0\) the likelihood ratio is strictly **decreasing** within the common interior support for every pair of distinct sum levels, while the strict usual stochastic ordering above continues to hold.

## Assumptions and scope

The FGM copula has density \(1+\theta(1-2u)(1-2v)\), and each margin has density \(\lambda e^{-\lambda x}\) on \(x>0\). For \(s>0\), conditioning on \(S=s\) means the continuous regular conditional law defined by disintegrating the joint density along \(x+y=s\). All inequalities are for every real parameter and every positive conditioning level stated, including the endpoint dependence parameters \(\theta=\pm1\). Strict vector ordering means existence of a coupling whose two coordinates are strictly larger at the larger sum almost surely; it does not mean a strictly larger expectation for every nonconstant coordinatewise nondecreasing function.

Rescaling \((X,Y,S)\) by \(\lambda\) reduces the proof to \(\lambda=1\). For \(0<x<s\), put \(u=e^{-x}\), \(v=e^{x-s}\), and
\[
 H_\theta(x,s)=1+\theta(1-2u)(1-2v),\qquad
 Z_\theta(s)=\int_0^s H_\theta(x,s)\,dx.
\]
The conditional density of \(X\mid S=s\) is \(H_\theta(x,s)/Z_\theta(s)\) on \((0,s)\); \(H_\theta>0\) there even at \(\theta=\pm1\). Exchangeability makes the law symmetric around \(s/2\).

## Proof

### Likelihood-ratio classification for nonnegative and negative dependence

Direct differentiation yields the exact mixed logarithmic derivative
\[
 \frac{\partial^2}{\partial x\,\partial s}\log H_\theta(x,s)
 =\frac{2\theta v\{1+\theta(1-2u)^2\}}{H_\theta(x,s)^2}.
\]
For \(0\le\theta\le1\) it is nonnegative, so the conditional densities satisfy monotone likelihood ratios on the common portion \((0,s_1)\); the support of the larger-sum law extends to \((0,s_2)\), preserving the likelihood-ratio order. The case \(\theta=0\) is the uniform conditional distribution on \((0,s)\). For \(-1\le\theta<0\), the displayed derivative is strictly negative since \(|1-2u|<1\); hence the ratio of the conditional density at \(s_2\) to the one at \(s_1\) strictly decreases in \(x\in(0,s_1)\). Accordingly, the asserted *increasing* likelihood-ratio ordering fails for every \(s_1<s_2\).

### Exact conditional-CDF derivative for negative dependence

Take \(\theta=-r\) with \(0\le r\le1\), fix \(0<t<s\), and abbreviate
\[
 c=1-e^{-t}>0,\qquad d=e^t-1-2t,\qquad z=e^{-s}.
\]
The endpoint weights satisfy
\[
 H_0(x,s)=1,\qquad
 H_{-1}(x,s)=2\{e^{-x}+e^{x-s}-2e^{-s}\},
\]
and \(H_{-r}=(1-r)H_0+rH_{-1}\). Therefore the conditional CDF \(F_s(t)=\Pr(X\le t\mid S=s)\) is \(N(s,t)/Z(s)\), where
\[
 \begin{aligned}
 N(s,t)&=(1-r)t+2r(c+zd),\\
 Z(s)&=(1-r)s+4r\{1-(1+s)z\}.
 \end{aligned}
\]
Both are positive on their domains. Differentiating with \(t\) fixed gives the **exact identity**
\[
 \begin{split}
 N_s Z-N Z_s={}&-(1-r)^2t\\
 &-2r(1-r)\{c+(1+s)zd+2stz\}\\
 &-8r^2z\{sc+(1-z)d\}.
 \end{split}
\]
All three braces and terms on the right have the indicated strictly negative contribution. If \(d\ge0\), their positivity is immediate. Suppose \(d<0\). Since \((1+s)e^{-s}\) decreases and \(d<0\),
\[
 c+(1+s)e^{-s}d\ge c+(1+t)e^{-t}d>0,
\]
where the strict last inequality follows by multiplying by \(e^t\) and using
\[
 (2+t)e^t-(2+3t+2t^2)
 =\sum_{k=3}^{\infty}\frac{(k+2)t^k}{k!}>0.
\]
For the other brace, set \(G(s)=sc+(1-e^{-s})d\). At \(s=t\),
\[
 G(t)=(1-e^{-t})(e^t-1-t)>0,
\]
while for \(s\ge t\),
\[
 G'(s)=c+e^{-s}d\ge c+e^{-t}d
 =2\{1-(1+t)e^{-t}\}>0.
\]
Thus \(N_s Z-N Z_s<0\) for every \(0<t<s\) and every \(r\in[0,1]\), proving
\[
 \frac{\partial}{\partial s}F_s(t)<0\qquad (0<t<s,\ \theta\in[-1,0]).
\]
For \(t\in[s_1,s_2)\), the smaller-sum CDF is \(1\) and the larger-sum CDF is strictly below \(1\). Hence the conditional one-dimensional laws increase strictly in usual stochastic order for \(\theta\le0\). The likelihood-ratio argument already gives the same conclusion for \(\theta\ge0\).

### Coordinatewise almost-sure coupling

For each \(s>0\) let \(Q_s(a)\), \(0<a<1\), be the quantile of \(X\mid S=s\). Strict CDF inequalities on the common support imply that \(Q_{s_1}(a)<Q_{s_2}(a)\) for every \(a\in(0,1)\). Exchangeability and positivity of the conditional density imply
\[
 Q_s(1-a)=s-Q_s(a).
\]
For one shared uniform random variable \(U\) on \((0,1)\), the vector \((Q_s(U),Q_s(1-U))\) therefore has the conditional law of \((X,Y)\mid S=s\), and **both** coordinates strictly increase from \(s_1\) to \(s_2\). This proves the multivariate statement.

## Verification

Run `python verify_fgm.py` using Python's standard library. It checks the key mixed-derivative identity with exact rational arithmetic and the CDF integrals, strict CDF ordering, and likelihood-curvature signs on representative numerical grids. The code is supplementary: the displayed identities and strict inequalities, not finite experiments, prove the all-parameter theorem. The calculation of \(N_s Z-N Z_s\) was also independently expanded symbolically, confirming exact equality of both sides.

## Relationship to prior work

Efron's classical monotonicity theorem assumes independence and log-concave margins. Saumard and Wellner (2018, Section 3.3.2) explicitly analyze the Morgenstern copula **with uniform margins**; their negative-parameter example does not cover an exponential marginal transformation because conditioning on the *sum* is not invariant under nonlinear coordinate transformations. Pellerey and Navarro (2021, Propositions 2.1 and 2.2) establish likelihood-ratio and multivariate stochastic-order conclusions under slice total-positivity hypotheses; the present negative-parameter family violates those hypotheses, but still satisfies strict vector stochastic monotonicity. Ortega-Jiménez and collaborators (2022/2023, FGM example; also Ortega-Jiménez's 2022 thesis, Section 6.3.1) verify the positive-parameter slice-total-positivity regime. The negative-parameter ordinary stochastic-order result here is logically different from that positive-parameter likelihood-ratio guarantee. Navarro (2022) examines ageing classes of the **sum** of FGM-dependent exponentials, not conditional ordering given that sum.

## Limitations

Only equal-rate exponential margins and the bivariate FGM copula are classified. The result does not assert likelihood-ratio order when \(\theta<0\), nor extend automatically to unequal rates, other margins, different copulas, or more than two components. No statement about exact risk-allocation formulas or optimal couplings outside the conditional problem is made. The originality comparison is based on inspected accessible primary literature, not a guarantee that no equivalent result exists in unindexed earlier sources. Independent external validation has not been performed.

## References

1. F. Pellerey and J. Navarro, "Stochastic monotonicity of dependent variables given their sum," *TEST* 31 (2022), 543–561, first online 11 October 2021, DOI: 10.1007/s11749-021-00789-5. Primary MSC2020: 60E15.
2. A. Saumard and J. A. Wellner, "Efron's monotonicity property for measures on R2," *Journal of Multivariate Analysis* 166 (2018), 212–224, DOI: 10.1016/j.jmva.2018.03.005; preprint arXiv:1707.04472, Section 3.3.2.
3. P. Ortega-Jiménez, F. Pellerey, M. A. Sordo and A. Suárez-Llorens, "Note on Efron's Monotonicity Property Under Given Copula Structures," *Building Bridges between Soft and Statistical Methodologies for Data Science* (2022/2023), 303–310, DOI: 10.1007/978-3-031-15509-3_40.
4. P. Ortega-Jiménez, *Stochastic Orders Applied to Insurance and Economics*, doctoral thesis, University of Cádiz, November 2022, Chapter 6, https://rodin.uca.es/bitstream/handle/10498/33603/Thesis_PatriciaOrtegaJimenez.pdf.
5. J. Navarro, "Preservation of ILR and IFR aging classes in sums of dependent random variables," *Applied Stochastic Models in Business and Industry* (2022), DOI: 10.1002/asmb.2657.
