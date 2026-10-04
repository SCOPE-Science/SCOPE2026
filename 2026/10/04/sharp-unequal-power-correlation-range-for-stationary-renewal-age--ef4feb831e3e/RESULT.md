# Sharp unequal-power correlation range for stationary renewal age and residual life

## Finding

Let a stationary renewal process have strictly positive interarrival time \(X\), and let
\(A\) and \(R\) denote the backward and forward recurrence times observed at stationarity.
Fix
\[
r,s>0,\qquad r\ne s,
\]
and assume
\[
\mathbb E X^{2r+1}+\mathbb E X^{2s+1}<\infty.
\]

Put
\[
c_{r,s}=B(r+1,s+1),
\qquad
a_r=\frac1{r+1},
\qquad
b_r=\frac1{2r+1}.
\]
Then
\[
\boxed{
\ell_{r,s}\le
\operatorname{Corr}(A^r,R^s)
<
u_{r,s},
}
\]
where
\[
\boxed{
\ell_{r,s}
=
\frac{c_{r,s}-a_ra_s}
{\sqrt{(b_r-a_r^2)(b_s-a_s^2)}}
}
\]
and
\[
\boxed{
u_{r,s}
=
c_{r,s}\sqrt{(2r+1)(2s+1)}.
}
\]

The lower endpoint is attained exactly by deterministic interarrivals.
The upper endpoint is not attained, but it is a sharp supremum.

Every value in
\[
(\ell_{r,s},u_{r,s})
\]
is attained by a stationary renewal process with a two-point interarrival law.

For exponential interarrivals,
\[
\operatorname{Corr}(A^r,R^s)=0
\]
for every positive pair \(r,s\), as expected from independence of stationary age and residual life.

When \(r=s\), the formulas reduce to the previously known equal-power envelope. The unequal-power case is the new statement here.

## Assumptions and scope

The interarrival law is strictly positive and has the moments needed to make both transformed variances finite.
No density assumption is required.

The process is stationary. The ordinary finite-time age/residual pair is not covered.

The theorem concerns Pearson correlation of unequal powers. It does not claim an analogous sharp range for rank correlations, mutual information, or conditional dependence.

## Proof

At a stationary inspection epoch, the containing renewal interval \(L=A+R\) has the size-biased interarrival law, and conditional on \(L\) the inspection location is uniform in that interval. Thus
\[
(A,R)=(UL,(1-U)L),
\]
where
\[
U\sim{\rm Unif}(0,1)
\]
is independent of \(L\).

Set
\[
M_r=L^r,\qquad M_s=L^s.
\]
Write
\[
\alpha_r=\mathbb E U^r=\frac1{r+1}=a_r,
\]
\[
\beta_r=\mathbb E U^{2r}=\frac1{2r+1}=b_r,
\]
and
\[
\gamma_{r,s}
=
\mathbb E\!\left[U^r(1-U)^s\right]
=
B(r+1,s+1)
=
c_{r,s}.
\]

Since \(U^r\) is strictly increasing and \((1-U)^s\) strictly decreasing,
\[
c_{r,s}<a_ra_s.
\tag{1}
\]

Using independence of \(U\) and \(L\),
\[
\operatorname{Cov}(A^r,R^s)
=
c_{r,s}\operatorname{Cov}(M_r,M_s)
+
(c_{r,s}-a_ra_s)\,
\mathbb E M_r\,\mathbb E M_s.
\tag{2}
\]
Also
\[
\operatorname{Var}(A^r)
=
b_r\operatorname{Var}(M_r)
+
(b_r-a_r^2)(\mathbb E M_r)^2,
\tag{3}
\]
and similarly
\[
\operatorname{Var}(R^s)
=
b_s\operatorname{Var}(M_s)
+
(b_s-a_s^2)(\mathbb E M_s)^2.
\tag{4}
\]

Because \(M_r\) and \(M_s\) are increasing functions of the same random variable,
\[
\operatorname{Cov}(M_r,M_s)\ge0.
\tag{5}
\]

For the lower bound, if the covariance in (2) is nonnegative there is nothing to prove because \(\ell_{r,s}<0\). Otherwise, (2) and (5) give
\[
\operatorname{Cov}(A^r,R^s)
\ge
(c_{r,s}-a_ra_s)\,
\mathbb E M_r\,\mathbb E M_s.
\]
Equations (3)--(4) give
\[
\sqrt{\operatorname{Var}(A^r)\operatorname{Var}(R^s)}
\ge
\sqrt{(b_r-a_r^2)(b_s-a_s^2)}\,
\mathbb E M_r\,\mathbb E M_s.
\]
Since the numerator is negative in the case under consideration, division yields
\[
\operatorname{Corr}(A^r,R^s)\ge\ell_{r,s}.
\]

Equality forces equality in both preceding estimates. Hence
\[
\operatorname{Var}(M_r)=\operatorname{Var}(M_s)=0,
\]
so \(L\) is deterministic. Conversely, deterministic \(L\) gives equality.

For the upper bound, if the covariance in (2) is nonpositive the positive number \(u_{r,s}\) is already an upper bound. If the covariance is positive, then by (1),
\[
\operatorname{Cov}(A^r,R^s)
<
c_{r,s}\operatorname{Cov}(M_r,M_s).
\]
Moreover, (3)--(4) imply
\[
\sqrt{\operatorname{Var}(A^r)\operatorname{Var}(R^s)}
\ge
\sqrt{b_rb_s\,
\operatorname{Var}(M_r)\operatorname{Var}(M_s)}.
\]
Therefore
\[
\operatorname{Corr}(A^r,R^s)
<
\frac{c_{r,s}}{\sqrt{b_rb_s}}\,
\operatorname{Corr}(M_r,M_s)
\le
\frac{c_{r,s}}{\sqrt{b_rb_s}}
=
u_{r,s}.
\]
Thus the upper endpoint is never attained.

It remains to prove sharpness and interval filling. Let the stationary interval length \(L\) have a two-point law on
\[
\{1,M\}.
\]
For every nondegenerate such law, \(L^r\) and \(L^s\) are affine functions of the same Bernoulli indicator, hence
\[
\operatorname{Corr}(L^r,L^s)=1.
\]
Choose
\[
\Pr(L=M)=M^{-t}
\]
with any fixed
\[
0<t<2\min\{r,s\}.
\]
As \(M\to\infty\), for both powers the squared mean becomes negligible compared with the variance:
\[
\frac{(\mathbb E L^r)^2}{\operatorname{Var}(L^r)}\to0,
\qquad
\frac{(\mathbb E L^s)^2}{\operatorname{Var}(L^s)}\to0.
\]
Substitution into (2)--(4) therefore gives
\[
\operatorname{Corr}(A^r,R^s)\to u_{r,s}.
\]

Any two-point law of \(L\) is the size-biased law of a positive two-point interarrival distribution. Indeed, if \(H\) is the law of \(L\), define
\[
\mu=
\left(\int x^{-1}\,dH(x)\right)^{-1},
\qquad
dF(x)=\mu x^{-1}\,dH(x).
\]
Then \(F\) is a probability law with mean \(\mu\) and size-biased law \(H\).

Finally, for fixed \(M\), the correlation varies continuously with the mixing probability of the two-point law. It equals \(\ell_{r,s}\) at a deterministic endpoint, while choices above can be made arbitrarily close to \(u_{r,s}\). The intermediate value theorem therefore realizes every value in the open interval.

For exponential interarrivals, the stationary age and residual life are independent, so every transformed correlation is zero.

## Verification

A standalone checker accompanies the theorem. For unequal integer powers it computes all beta constants exactly, constructs rational two-point and multi-point renewal laws, reconstructs the stationary age/residual mixed moments, and checks the two-sided bounds.

It separately verifies exact lower-endpoint equality for deterministic interarrivals and numerically follows the explicit two-point construction toward the upper endpoint.

The finite replay is supplementary. The proof for arbitrary positive real \(r,s\) is the covariance decomposition and the two-point sharpness argument above.

## Relationship to prior work

Nair and Sankaran study the stationary renewal age/residual pair as a bivariate Schur-constant equilibrium distribution. Their full 2014 paper gives the joint density
\[
g(x,y)=\frac{f(x+y)}{\mathbb E X}
\]
and records the ordinary linear correlation in terms of the second and third moments of the interarrival law. It does not give unequal-power correlation bounds.

A published related theorem gives the complete distribution-free range of
\[
\operatorname{Corr}(A^r,R^r)
\]
for equal powers. Its own limitations explicitly leave the unequal-power problem open. The proof there collapses to a single moment ratio because the two transformed marginals have the same variance; that reduction is unavailable when \(r\ne s\).

The present theorem resolves the unequal-power gap by a different decomposition: the common random interval length contributes a nonnegative covariance term, while the uniform split contributes the fixed negative term. This separates the two effects strongly enough to produce sharp universal endpoints despite the absence of a one-parameter moment reduction.

Targeted searches for mixed-power, unequal-power, Schur-constant, and stationary-renewal correlation formulas did not locate an equivalent theorem.

## Limitations

The theorem is stationary and distribution-free; it does not address finite-time renewal transients.

The upper endpoint is only a supremum. Approaching it requires increasingly heterogeneous two-point interval lengths.

The originality assessment is based on targeted searches and full-text comparison with the closest stationary Schur-constant source and the published equal-power result. Older dependence-model literature may contain an equivalent inequality under different terminology.

## References

1. N. U. Nair and P. G. Sankaran, “Modelling lifetimes with bivariate Schur-constant equilibrium distributions from renewal theory,” *METRON* 72 (2014), 331–349, DOI 10.1007/s40300-014-0045-0, published online 2014-06-03.
2. S. Katz, P. Naor, and R. Shinnar, “Moments of age and remaining life in renewal processes,” *Journal of Applied Probability* 10 (1973), 307–316, DOI 10.2307/3212348.
3. K. G. Gakis and B. D. Sivazlian, “The correlation of the backward and forward recurrence times in a renewal process,” *Stochastic Analysis and Applications* 12 (1994), 543–549.
