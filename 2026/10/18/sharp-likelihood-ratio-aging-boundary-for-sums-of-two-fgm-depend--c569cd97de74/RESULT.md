# Sharp likelihood-ratio aging boundary for sums of two FGM-dependent exponentials

## Finding

Let \(X,Y\) have a common exponential rate \(\lambda>0\), with Farlie–Gumbel–Morgenstern (FGM) **survival** copula
\[\widehat C_\theta(u,v)=uv[1+\theta(1-u)(1-v)],\quad -1\le\theta\le1.\]
Write \(S=X+Y\). The density of \(S\) is log-concave (the increasing likelihood-ratio, or ILR, aging condition) **if and only if** \(-1\le\theta\le\theta_c\), for a universal threshold \(0<\theta_c<1\).

An exact one-dimensional extremal specification is as follows. For \(s>0\), put
\[\begin{aligned}
 r(s)&=e^{-s},\\
 C(s)&=4\big[s(s+1)r(s)-1\big],\\
 D(s)&=-4\big[4r(s)^2-2s^2r(s)+2sr(s)-4r(s)+1\big],\\
 T(s)&=\frac{C(s)+\sqrt{C(s)^2+4D(s)}}{2}\quad\text{when }D(s)>0.
\end{aligned}\]
Then
\[\boxed{\displaystyle\theta_c=\frac1{1+\max_{\{s>0:D(s)>0\}}T(s)}}\approx0.86025827309745.\]
The maximum is attained and positive. The displayed decimal is an exploratory numerical approximation of the exact variational constant, not a certified enclosure. The source paper proves that the sum is IFR for every allowed dependence parameter, so these two aging conditions separate strictly above the threshold.

## Assumptions and scope

The marginals are exactly exponential with the same positive rate. The dependence family is the ordinary bivariate FGM survival copula, with full parameter interval \([-1,1]\). The assertion concerns global log-concavity of the **sum's density** on its positive support, equivalent to ILR. It does not concern the joint-density's log-concavity, unequal-rate exponentials, or generalized FGM families. Common-rate scale changes leave log-concavity invariant, so it suffices to set \(\lambda=1\).

## Proof

**Density calculation.** Differentiate the survival copula twice and use the exponential marginals to obtain the joint density \(e^{-(x+y)}[1+\theta(1-2e^{-x})(1-2e^{-y})]\) for \(x,y>0\). Integrating over \(x+y=s\) gives
\[f_\theta(s)=e^{-s}g_\theta(s),\qquad
 g_\theta(s)=s+\theta\big[s-4+4(s+1)e^{-s}\big].\]
This density is positive for \(s>0\). Define \(g_0(s)=s\),
\[g_+(s)=g_1(s)=2s-4+4(s+1)e^{-s},\qquad
 g_-(s)=g_{-1}(s)=4[1-(s+1)e^{-s}].\]
Because \(\log f_\theta=-s+\log g_\theta\), its logarithmic curvature has the sign of
\[\mathcal D_\theta(s)=g_\theta(s)g_\theta''(s)-\big(g_\theta'(s)\big)^2.\]

**All negative dependence is strictly ILR.** Write \(q=-\theta\in[0,1]\). Then \(g_\theta=(1-q)g_0+qg_-\), and direct differentiation gives
\[\begin{aligned}
\mathcal D_0&=-1,\\
\mathcal D_-&=16e^{-s}\big(1-s-e^{-s}\big)<0,\\
\mathcal C_-&:=g_0g_-''+g_-g_0''-2g_0'g_-'=-4s(s+1)e^{-s}<0.
\end{aligned}\]
The general quadratic identity for the logarithmic-curvature numerator of a linear combination yields
\[\mathcal D_\theta=(1-q)^2\mathcal D_0+q(1-q)\mathcal C_-+q^2\mathcal D_-<0\]
for every \(s>0\). The first strict inequality uses \(e^{-s}>1-s\).

**Positive dependence has one sharp parameter boundary.** When \(0\le\theta\le1\), write \(g_\theta=(1-\theta)g_0+\theta g_+\). Direct differentiation yields
\[\begin{aligned}
\mathcal D_+&=g_+g_+''-(g_+')^2=D(s),\\
\mathcal C_+&:=g_0g_+''+g_+g_0''-2g_0'g_+'=C(s),\\
\mathcal D_\theta&=-(1-\theta)^2+\theta(1-\theta)C(s)+\theta^2D(s).
\end{aligned}\]
Moreover \(C(s)<0\) for every \(s>0\), because \(e^s>s(s+1)\). The latter follows from the Taylor bound \(e^s\ge1+s+s^2/2+s^3/6\) and the strictly positive polynomial \(1-s^2/2+s^3/6\) (its minimum on the positive half-line equals \(1/3\) at \(s=2\)).

For \(0<\theta\le1\), set \(t=(1-\theta)/\theta\ge0\). Then \(\mathcal D_\theta/\theta^2=D(s)+tC(s)-t^2\). If \(D(s)\le0\), this is nonpositive for all \(t\ge0\). If \(D(s)>0\), its only nonnegative root is \(t=T(s)>0\), and it is nonpositive precisely for \(t\ge T(s)\). Thus global log-concavity is equivalent to \(t\ge \sup_{D(s)>0}T(s)\).

**The maximum exists and the threshold is nontrivial.** The continuous function \(D(s)\) tends to \(-4\) as \(s\downarrow0\) and as \(s\to\infty\), so \(\{s>0:D(s)>0\}\) lies in a compact positive interval. It is nonempty: at \(s=3/2\),
\[D(3/2)=-16r^2+22r-4>0,\quad r=e^{-3/2}.\]
Indeed, the alternating Taylor sums of orders 19 and 20 give \(223/1000<r<224/1000\), and the quadratic is strictly increasing and positive throughout this rational interval (its value at \(223/1000\) is positive). The function \(T\) extends continuously by zero to the boundaries where \(D=0\), since there \(C<0\). Therefore it attains a positive finite maximum. Reversing the substitution \(t=(1-\theta)/\theta\) establishes the claimed exact \(\theta_c\), including equality at the boundary.

Finally, since \(\lambda\) only rescales the argument of the density by a positive factor, the classification holds for every \(\lambda>0\).

## Verification

The included standalone `verify.py` performs exact rational arithmetic on the crucial \(s=3/2\) curvature witness, including rigorous alternating-series brackets for \(e^{-3/2}\). It also checks the derivative identities against numerical differentiation and reproduces a numerical approximation to the variational threshold on a fine grid. Finite computations do not prove the maximization or the infinite-parameter classification; those follow from the preceding analytical argument.

## Relationship to prior work

Navarro and Pellerey (first publicly available November 26, 2021), Example 2, give the same FGM–exponential sum and prove IFR for every parameter. From a plot of the log-density in their Figure 3, they also **informally report** preservation of ILR across the displayed parameters. Their reported ILR visual inference is not valid for large positive \(\theta\): the exact curvature above is positive near \(s=3/2\) at \(\theta=1\). The current result supplies the sharp boundary and separates the two aging classes without disputing their IFR proof. Their general log-concavity sufficiency theorems do not provide this full parameter characterization.

Navarro and Sarabia (published online December 23, 2020) studied aggregate risks for several copulas, including FGM, with hazard-rate comparisons. The article's abstract was inspected, but its full text was unavailable through accessible routes; possible stronger prior coverage is a residual originality risk. Pellerey and Navarro (published online October 11, 2021) treat conditional stochastic monotonicity given the sum, a different property. Earlier bivariate exponential aggregation work may also contain partially equivalent formulas, but no explicit threshold was found in the accessible material.

## Limitations

The threshold is specified by an exact bounded one-variable maximization, not a proved elementary closed-form constant. Its displayed decimal value is an un-certified numerical evaluation. No uniqueness of the maximizing \(s\) is needed or claimed. No theorem is offered for heterogeneous exponential rates, other dependence families, or arbitrary sums of ILR variables. Literature priority remains subject to independent full-text verification of inaccessible risk-aggregation papers; the scientific result is not independently audited.

## References

1. J. Navarro and F. Pellerey, “Preservation of ILR and IFR aging classes in sums of dependent random variables,” *Applied Stochastic Models in Business and Industry* 38 (2022), 240–261, DOI: `10.1002/asmb.2657`. First published November 26, 2021, full text reviewed at `https://onlinelibrary.wiley.com/doi/full/10.1002/asmb.2657`.
2. J. Navarro and J. M. Sarabia, “Copula representations for the sum of dependent risks: models and comparisons,” *Probability in the Engineering and Informational Sciences* 36 (2022), 320–340, DOI: `10.1017/S0269964820000649`. First published December 23, 2020; only abstract/references accessible.
3. F. Pellerey and J. Navarro, “Stochastic monotonicity of dependent variables given their sum,” *TEST* 31 (2022), 543–561, DOI: `10.1007/s11749-021-00789-5`. First published October 11, 2021; distinct conditional problem, primary MSC2020 60E15.
