# Sharp covariance-sign transition in a discrete sequential–simultaneous shock model

## Finding
Consider two independent streams of Bernoulli shocks at times \(0,1,2,\ldots\). Each trial in the sequential stream succeeds with probability \(r\), and each trial in the simultaneous-fatal stream succeeds with probability \(v\). The first sequential success destroys one component, selected by an independent Bernoulli orientation with probability \(\theta\); the second sequential success destroys the remaining component. A simultaneous-fatal success destroys both components that remain. Let \(X_1,X_2\) be their two integer-valued failure times.

For all \(0<r,v,\theta<1\), put \(a=1-r\), \(b=1-v\), \(d=1-ab\), and \(c=\theta(1-\theta)\). Then
\[
\operatorname{Cov}(X_1,X_2)=\frac{ab}{d^2}-\frac{c r^2b^2}{d^4}.
\]
The covariance is strictly positive for **every** \(v\in(0,1)\) if and only if \(r\le 1-c\). If \(r>1-c\), there is exactly one common-shock probability \(v_*\in(0,1)\) where it vanishes; it is strictly negative for \(v<v_*\) and strictly positive for \(v>v_*\). In terms of the model's tied-outcome probability \(\pi=\Pr(X_1=X_2)\), the transition is
\[
\pi_* =\frac{1+a-\sqrt{(1-a)^2+4a^2/c}}{2a},\qquad
v_* =\frac{r\pi_*}{1-a\pi_*}.
\]
Although each orientation-conditioned pair has strictly positive covariance, the unconditioned pair can have negative covariance. This gives a sharp criterion for how random assignment of the first sequential failure competes with shared early-failure variability.

## Assumptions and scope
The shock streams and orientation variable are mutually independent, both shock streams have independent identically distributed trials, and trial numbering begins at zero. All stated parameters belong to \((0,1)\). The claim concerns the explicitly defined Bernoulli shock experiment in Section 5.1 of Lee and Cha (2026), not an arbitrary member of their more general nonhomogeneous family. The covariance-sign result does **not** assert unconditional negative quadrant dependence; covariance and quadrant-order properties are different.

Write \(A=\min(X_1,X_2)\) and \(B=\max(X_1,X_2)\). Let \(I\) be the orientation, independent of \((A,B)\), and choose \(I=1\) when the first sequential shock targets component 1. Accordingly \(X_1=A+(1-I)(B-A)\) and \(X_2=A+I(B-A)\), with \(\Pr(I=1)=\theta\). This specification also covers ties without ambiguity.

## Proof
**1. Ordered-lifetime law.** Before the first fatal event in either stream, each time step has joint no-shock probability \(q=ab\). A tie at time \(t\ge0\) occurs exactly when the common-fatal stream first succeeds at \(t\) and no earlier sequential success has occurred. Thus \(\Pr(A=B=t)=v q^t\). For integers \(0\le t<u\), a sequential success at \(t\) must precede the next fatal event at \(u\). At time \(t\) this has probability \(rb\); after \(u-t-1\) further no-shock steps the first subsequent shock is either a sequential success or a simultaneous-fatal success, with probability \(d=1-q\). Hence
\[
\Pr(A=t,B=u)=rb\,d\,q^{u-1},\qquad 0\le t<u.
\]
This direct event enumeration is sufficient to define the probability law, independently of any printed special-case parameterization.

**2. Independent waiting-time factorization.** Let \(L=B-A\). Summing and factoring the preceding expressions yields, for every \(t\ge0\),
\[
\Pr(A=t)=d q^t,\qquad
\Pr(L=0)=\frac vd,\qquad
\Pr(L=\ell)=rb\,q^{\ell-1}\quad(\ell\ge1),
\]
and \(\Pr(A=t,L=\ell)=\Pr(A=t)\Pr(L=\ell)\). The components \(A\) and \(L\) are therefore independent. Their distributions normalize because \(v+rb=d\). Elementary geometric-series identities give
\[
\operatorname{Var}(A)=\frac q{d^2},\qquad
\mathbb E[L]=\frac{rb}{d^2}.
\]
These formulas are exact for the complete infinite support.

**3. Covariance identity.** Since \(X_1=A+(1-I)L\) and \(X_2=A+IL\), independence of \(A,L,I\) gives
\[
\operatorname{Cov}(X_1,X_2)=\operatorname{Var}(A)
-\operatorname{Var}(I)(\mathbb E[L])^2
=\frac{ab}{d^2}-\frac{c r^2b^2}{d^4}.
\]
One direct way to verify the negative term is \((1-I)I=0\), while \(\mathbb E[1-I]\mathbb E[I]=c\). Conditioning on either value of \(I\) removes this negative term, giving \(\operatorname{Cov}(X_1,X_2\mid I)=\operatorname{Var}(A)=ab/d^2>0\).

**4. Exact sign diagram.** The tie mass and its inverse relation to \(v\) are
\[
\pi=\Pr(L=0)=\frac{v}{r+(1-r)v},\qquad
v=\frac{r\pi}{1-a\pi}.
\]
This is an increasing bijection of \((0,1)\). Eliminating \(v\) from the covariance identity gives
\[
\operatorname{Cov}(X_1,X_2)=
\frac{(1-\pi)(1-a\pi)}{r^2}
\left[a-c(1-\pi)(1-a\pi)\right].
\]
The first factor is positive. The function \((1-\pi)(1-a\pi)\) decreases strictly from \(1\) to \(0\) because its derivative is \(-(1+a)+2a\pi<0\) for \(\pi\in(0,1)\). If \(a\ge c\), the bracket is strictly positive on \((0,1)\), including at equality \(a=c\). If \(a<c\), the bracket increases strictly from \(a-c<0\) to \(a>0\), hence has exactly one zero. Solving the quadratic yields the displayed \(\pi_*\) and then \(v_*\); both belong to \((0,1)\). Because \(a=1-r\), the condition \(a<c\) is exactly \(r>1-c\). This proves all asserted signs and boundary cases.

## Verification
For \(r=0.9\) and \(\theta=1/2\), the threshold is \(\pi_*=0.5755710991019481\ldots\) and \(v_*=0.5496502702061786\ldots\). At \(v=0.1\) the covariance is \(-0.1305082769204929\ldots\), while at \(v=0.7\) it is \(+0.0112979568872812\ldots\). The standalone file `checker.py` constructs the ordered joint mass on a finite rectangle *independently* of the covariance formula and checks six parameter settings and the transition thresholds. It also checks that truncated total mass is close to one. Numerical truncation is only a consistency check; the infinite-support claims follow from the geometric-series proof above. Run `python3 checker.py` using Python 3.9 or newer.

## Relationship to prior work
Lee and Cha, *New Discrete Bivariate Distributions Generated from Discrete Time Point Process Model* (2026), establish general bivariate shock constructions and prove **positive quadrant dependence conditional on the first sequential-failure orientation** (Theorem 3). The present theorem instead classifies the **unconditional** sign of a second-order moment for their homogeneous Bernoulli experiment, including an exact tie-mass transition. Conditional positive quadrant dependence does not imply unconditional positive covariance under orientation mixing. The ordered-time factorization is the key additional reduction, not a mere renaming of the conditional-dependence theorem.

Huber and Marić (2014) treat extreme possible correlations across **all** bivariate couplings with geometric marginals, whereas this law has a random ordering and in general non-geometric margins. Prior bivariate reliability models from Lee and Cha (2017, 2024) and general homogeneous-shock literature address related negative dependence or different shock mechanisms; these do not establish this particular tie-mass phase boundary in the material inspected. An exact equivalent result in unavailable or unindexed sources cannot be excluded.

## Limitations
The result assumes constant independent Bernoulli shock probabilities and independent orientation. It does not extend without further work to time-varying intensities, dependent shocks, higher moments, rank correlation, or global quadrant dependence. The source literature also contains earlier general models capable of negative dependence; no claim is made that negative dependence in reliability models is new. A possible earlier undated preprint of the motivating paper means that its exact first day of public availability is not fully settled; 2026-04-25 is the earliest independently verified day-level public date for the cited DOI. Scientific novelty remains subject to further independent literature assessment.

## References
1. H. Lee and J. H. Cha (2026), *New Discrete Bivariate Distributions Generated from Discrete Time Point Process Model*, Methodology and Computing in Applied Probability **28**, article 41. DOI: https://doi.org/10.1007/s11009-026-10263-0 . Open full article: https://link.springer.com/article/10.1007/s11009-026-10263-0 .
2. M. Huber and N. Marić (2014), *Minimum correlation for any bivariate Geometric distribution*, arXiv:1406.1779, https://arxiv.org/abs/1406.1779 .
3. H. Lee, J. H. Cha, and G. Pulcini (2017), *Modeling Discrete Bivariate Data with Applications to Failure and Count Data*, Quality and Reliability Engineering International, DOI: https://doi.org/10.1002/qre.2118 .
4. H. Lee and J. H. Cha (2024), *New continuous bivariate distributions generated from shock models*, Statistics, DOI: https://doi.org/10.1080/02331888.2024.2339265 .
5. S. Wang and W. Li (2005), *Dependency measures under bivariate homogeneous shock models*, DOI: https://doi.org/10.1080/02331880412331329863 .
