# Sharper quantitative sparsity in the prime-gap distinct-product construction

## Corrected and strengthened result

Consider Chojecki's prime-gap greedy set A.  For a rejected prime gap v=(p_v,q_v), write x(v)=q_v and d(v)=q_v-p_v.  For a fixed parameter theta, call v short when d(v)<=p_v^theta and raw when its chosen witness crosses no earlier rejected gap.

At the original choice theta=1/20,

\[
\#\{v:\ v\text{ raw and short},\ x(v)\le X\}=O(X^{3/4+o(1)})
\]

and

\[
\sum_{\substack{v\text{ short rejected}\\x(v)\le X}}d(v)=O(X^{13/16+o(1)}).
\]

Thus the fixed-parameter conclusions of the original record remain valid.

There is, however, a stronger current parameterized consequence.  Runbo Li's newer preprint *Primes in almost all short intervals III* proves that, for every sufficiently large fixed B and sufficiently small fixed eta>0, all but O(X(log X)^(-B)) integers n in [X,2X] have a prime in the backward interval

\[
[n-n^{1/24+\eta},n].
\]

Consequently the long-gap part of Chojecki's argument can be run for every fixed theta>1/24: for a long prime gap, all endpoints n lying far enough to the right inside that gap have the Li interval contained in the prime-free gap, so they are exceptional; disjointness of prime-gap interiors converts Li's exceptional-count estimate into the same arbitrary-logarithmic saving for total long-gap mass.

For theta>1/24 sufficiently close to 1/24 (and in particular for theta<=1/20), the reduced-degree-ratio stratification gives

\[
A(\theta)=\frac12+5\theta
\]

for the raw short-gap count exponent.  Feeding this into Sneiderman's length-sensitive all-equal forest summation yields

\[
F(\theta)=(1-\theta)A(\theta)+2\theta
=\frac12+\frac{13}{2}\theta-5\theta^2.
\]

Therefore, for every delta>0, theta may be chosen just above 1/24 so that

\[
\sum_{\substack{v\text{ short rejected}\\x(v)\le X}}d(v)
=O_\delta\!\left(X^{439/576+\delta}\right),
\qquad
\frac{439}{576}=0.762152777\ldots .
\]

The exponent 439/576 is the limiting value F(1/24); it is an infimum from theta>1/24, not a claim at the endpoint itself.

Finally, the canonical set A still satisfies

\[
\forall C>0,\qquad |[1,X]\setminus A|=O_C\!\left(\frac{X}{(\log X)^C}\right).
\]

The distinct-consecutive-product property is unchanged.

## Proof of the improved raw count

For a raw witness Chojecki reduces the collision to

\[
\prod_{i=0}^{r-1}(x-i)=\prod_{j=0}^{s-1}(y+j),\qquad r>s\ge1,
\]

with x,y<=X.  Shortness gives s<=X^theta and

\[
r\le L:=\lceil X^\theta\log_2 X\rceil.
\]

Write h=(r,s), r=uh, s=vh, (u,v)=1 and u>v.  The split-product curve estimate gives, for fixed (r,s),

\[
N_{r,s}(X)\ll X^{1/u}(r^3\log X+r^4).
\]

If u=2, coprimality forces v=1, so (r,s)=(2h,h).  Hence only one parameter is summed:

\[
\sum_{u=2}N_{r,s}(X)
\ll X^{1/2}\sum_{h\le L/2}\big((2h)^3\log X+(2h)^4\big)
=O(X^{1/2}L^5\log X).
\]

If u>=3, summing crudely over all s<r<=L gives

\[
\sum_{u\ge3}N_{r,s}(X)\ll X^{1/3}L^6\log X.
\]

For theta<1/6, the first exponent is larger, so

\[
\#\{\text{raw short gaps up to }X\}
=O(X^{1/2+5\theta+o(1)}).
\]

At theta=1/20 this is X^(3/4+o(1)); at the limiting theta=1/24 it is X^(17/24+o(1)).

## Forest summation

Sneiderman's length-sensitive treatment of nonempty all-equal descendants says that if the raw-root exponent is A<1, their total terminal length has exponent

\[
(1-\theta)A+2\theta.
\]

Substituting A(theta)=1/2+5theta gives F(theta) above.  The raw roots themselves contribute exponent A(theta)+theta.

Let rho=(2-theta)^(-1).  The first unequal-edge branch has exponent

\[
E_1=(A(\theta)+\theta)\rho+5\theta,
\]

and the first long-root branch has exponent

\[
L_1=1-\rho+5\theta.
\]

At theta=1/24,

\[
A=\frac{17}{24},\quad
F=\frac{439}{576},\quad
A+\theta=\frac34,\quad
E_1=\frac{667}{1128},\quad
L_1=\frac{787}{1128}.
\]

Both competing branch exponents are strictly below F.  The coefficients controlling deeper-path monotonicity are also positive at the endpoint:

\[
A+\theta-\frac{4\theta}{1-\rho}=\frac{113}{276}>0,
\]

\[
(1-\rho)-\frac{4\theta\rho}{1-\rho}=\frac{341}{1081}>0.
\]

By continuity, the same inequalities hold for theta in a right neighborhood of 1/24.  This proves the strengthened parameterized short-gap estimate.  At theta=1/20 the values reduce to the previously filed 13/16, 4/5, 103/156 and 115/156 comparisons.

## Long gaps and density

Li III is stated for backward short intervals rather than the forward intervals used in one common presentation of the gap conversion.  This does not change the argument.  If (p,p^+) is a prime gap of length g>p^theta and choose eta with 1/24+eta<theta, then all but O(p^(1/24+eta)) integer endpoints n in a central/right portion of the gap satisfy

\[
[n-n^{1/24+\eta},n]\subset(p,p^+).
\]

Each such n is exceptional for Li III.  Distinct prime gaps have disjoint interiors, so summing exceptional endpoints over dyadic p-ranges bounds total long-gap length by O_C(X(log X)^(-C)) for every fixed C after choosing Li's B sufficiently large.  The short-gap power saving is stronger than any fixed logarithmic loss, yielding the displayed all-log-powers complement bound.

## Originality boundary

Chojecki's current construction uses a cruder all-pair summation that gives raw exponent 4/5 and short-gap mass 9/10.  Sneiderman's pinned public reconstruction improves the short-gap mass to 43/50 by summing all-equal descendant lengths more efficiently, but it keeps the same 4/5 raw exponent.  The improvement here is the reduced-degree-ratio observation that the X^(1/2) curve case u=2 is only the one-parameter family (2h,h), together with its combination with the length-sensitive forest sum.

The September 2026 Kielhorn Zenodo submission is closely related.  During the independent audit, authorized retrieval yielded its 13-page Lean formalization supplement, which formalizes a different connector-region construction and fixed parameter regime.  The accompanying main mathematical manuscript was not obtained and is not claimed to have been read; it remains a residual originality risk.

## Limitations

- The power exponents above concern the short-gap contribution.  The full complement is proved to have arbitrary fixed logarithmic savings, not a global power saving.
- The 439/576 exponent is a limiting infimum from theta>1/24; the Li theorem itself requires an exponent 1/24+eta.
- Originality is to the best of the searched and inspectable literature; the inaccessible main Kielhorn manuscript remains a stated limitation.

## References

1. Przemek Chojecki, *Distinct Consecutive Products*, arXiv:2609.17543.
2. Rob Sneiderman, *Audit and reconstruction of Chojecki's gap-greedy preprint on Erdos Problem 421 with a sharpened short-gap estimate*, pinned commit 318c112c7a70879d98d86d8c3d9a280d77dadb35, https://github.com/Robby955/erdos-421-audit/.
3. Runbo Li, *Primes in almost all short intervals III*, 2026 preprint, https://runbolicarey.com/assets/downloads/Primes_in_almost_all_short_intervals_III.pdf.
4. Ryan Kielhorn, *Distinct consecutive products in a density-one set via prime-gap deletions*, Zenodo DOI 10.5281/zenodo.21287064.
