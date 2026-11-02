# Two-patch ecological occupancy covariance has a sharp catastrophe-driven double reversal

## Finding

A minimal two-habitat continuous-time occupancy chain can change from negative to positive and back to negative **stationary cross-patch covariance** as the rate of spatially shared clearing events increases. The reversals occur precisely inside an explicit, nonempty region of biologically interpretable transition rates. Outside that region two reversals are impossible.

Let \(a,b,e>0\) and \(d\geq0\) be rates as defined below. Put
\[
F(d)=(2b-a)d^2+2(b^2+3be-2ae)d+4e^2(b-a).
\]
For the binary stationary occupancy indicators \(X_1,X_2\), the covariance has exactly the sign of \(F(d)\). For each fixed \(d\), the unique colonization rate making the covariance zero is
\[
b_c(d)=\frac{a(2e+d)}{\sqrt{(e+d)^2+2ad}+e+d}.
\]
If \(a\leq2e\), this critical rate is strictly decreasing in \(d\). If \(a>2e\), it instead has a unique strict minimum
\[
b_* =2\sqrt{e(a+2e)}-3e,\qquad
 d_* =\frac{2e(b_*+e)}{b_*-e},\qquad
 e<b_*<a/2.
\]
Consequently the covariance displays **two distinct strict sign reversals as \(d\) grows from zero to infinity if and only if**
\[
a>2e\quad\text{and}\quad b_*<b<a/2.
\]
In that region the only zeroes are the strictly positive rates
\[
d_{\pm}=
\frac{b^2+3be-2ae\ \pm\ b\sqrt{b^2+6be+e^2-4ae}}{a-2b},
\qquad 0<d_-<d_+,
\]
and covariance is negative for \(0\leq d<d_-\), positive for \(d_-<d<d_+\), and negative for \(d>d_+\). At \(b=b_*\), with \(a>2e\), there is a unique zero at \(d=d_*\) but no sign reversal. This complete critical-rate curve also classifies all one-switch, zero-switch, and equality cases.

For the exact rates \((a,b,e)=(10,4,1)\),
\[
F(d)=-2(d-2)(d-6).
\]
The stationary covariance at \(d=0,4,8\) is respectively \(-60/3721\), \(20/15129\), and \(-60/40401\). The two critical catastrophe rates are exactly \(d_-=2\) and \(d_+=6\).

## Assumptions and scope

There are two exchangeable habitat patches, each either empty (state \(0\)) or occupied (state \(1\)). The continuous-time Markov chain has states \(00,10,01,11\) and the following complete list of nontrivial jumps:

- When both patches are empty, \(00\to10\) and \(00\to01\), each at rate \(a\).
- When one patch is occupied, \(10\to11\) and \(01\to11\), each at rate \(b\). The effective establishment rate \(b\) may differ from \(a\), allowing either facilitation or inhibition by occupancy of the other patch.
- Each occupied patch has local extinction rate \(e\): \(10\to00\) and \(01\to00\), each at rate \(e\); \(11\to10\) and \(11\to01\), each at rate \(e\).
- An independent, simultaneous clearing event arrives at rate \(d\), sending any nonempty state to \(00\); it has no state change when the system is already empty. Events sending an occupied singleton to \(00\) combine with local extinction in the total generator rate \(e+d\).

The chain is irreducible for all specified rates, including \(d=0\), and has a unique stationary probability distribution. All covariance statements refer to a single observation time drawn from that stationary law; they are not claims about temporal autocorrelation, observed detection errors, finite-time transients, or population persistence without external colonization. The independent immigration-like rate \(a\) remains positive throughout.

The model isolates a potential competition-for-establishment mechanism: when occupancy of the other habitat decreases effective colonization, \(b<a\). It does not assume this effect always occurs in ecological systems. The sharp two-reversal region requires \(b<a/2\); in particular, the commonly used additive-colonization regime \(b\geq a\) cannot show this effect.

## Proof

**1. Stationary law.** By exchangeability write \(\pi=(u,v,v,w)\) for states \(00,10,01,11\). The inflow–outflow balance of \(11\) and \(00\) gives
\[
(2e+d)w=2bv,\qquad 2au=2(e+d)v+dw.
\]
Set
\[
h=\frac{2b}{2e+d},\quad k=\frac{e+d+bd/(2e+d)}a,\quad Z=k+2+h.
\]
Then \(w=hv\), \(u=kv\), and normalization gives the unique stationary distribution
\[
(u,v,v,w)=(k,1,1,h)/Z.
\]
These two balances together with normalization imply the remaining generator balances, or they may be verified by substitution. All entries are strictly positive.

**2. Covariance sign.** The indicator probabilities are \(\mathbb P(X_1=1)=\mathbb P(X_2=1)=(v+w)\) and \(\mathbb P(X_1=X_2=1)=w\). Therefore
\[
\operatorname{Cov}(X_1,X_2)=w-(v+w)^2
=uw-v^2=\frac{kh-1}{Z^2}
=\frac{F(d)}{a(2e+d)^2Z^2},
\]
with \(F\) exactly as stated. The denominator is strictly positive for every allowed parameter, so covariance zeroes and signs are precisely those of \(F\).

**3. Unique fixed-disturbance colonization threshold.** For every fixed \(a,e>0\) and \(d\geq0\), the expression
\[
F(d)=2db^2+2(e+d)(2e+d)b-a(2e+d)^2
\]
is strictly increasing in \(b\), starting negative at \(b=0\), and tending positive for large \(b\). The positive root obtained by rationalizing the quadratic formula is the displayed \(b_c(d)\). At \(d=0\) it equals \(a\). Its large-disturbance expansion is
\[
b_c(d)=\frac a2+\frac{a(2e-a)}{4d}+O(d^{-2}).
\]
At \(d=0\), implicit differentiation gives \(b_c'(0)=-a(a+e)/(2e^2)<0\). [Indeed \(F_b(0,a)=4e^2\) and \(F_d(0,a)=2a(a+e)\).]

**4. Complete critical-curve shape.** Differentiate \(F\) along its zero curve. Since
\[
F_b=2(2bd+d^2+3ed+2e^2)>0,
\]
a stationary point of \(b_c(d)\) is equivalent to \(F=F_d=0\). The discriminant of \(F\), considered as a polynomial in \(d\) with fixed \(a,b,e\), is
\[
\operatorname{disc}_d F=4b^2(b^2+6be+e^2-4ae).
\]
For a finite, positive stationary \(d\), the latter must vanish. Its unique positive possible \(b\) is \(b_* =2\sqrt{e(a+2e)}-3e\), and substituting into \(F_d=0\) yields \(d_*=2e(b_*+e)/(b_*-e)\). This is positive exactly when \(b_*>e\), equivalently \(a>2e\). At \(a=2e\), the apparent degenerate alternative \(b=a/2=e\) has \(F=-4e^3\), not zero, so no stationary point is lost through a vanishing quadratic coefficient. Thus there is no finite critical point for \(a\leq2e\), whereas for \(a>2e\) there is exactly one.

The derivative is initially negative. Continuity and the absence of additional critical points make \(b_c\) strictly decreasing when \(a\leq2e\). For \(a>2e\), the large-disturbance expansion approaches \(a/2\) from below, so the unique critical point must be a strict minimum. Moreover, \(b_*>e\), and \(b_*<a/2\) follows from
\[
(a+6e)^2-16e(a+2e)=(a-2e)^2>0.
\]
This proves the claimed shape, including all equality boundaries.

**5. Two switches and their exact locations.** The set of \(d\geq0\) for which covariance is positive at fixed \(a,b,e\) is precisely the set \(\{d:b>b_c(d)\}\). When \(a\leq2e\), this set is an interval (possibly empty or all), so two reversals cannot occur. When \(a>2e\), the unique strict minimum of \(b_c\), its starting value \(a\), and its limiting value \(a/2\) show that exactly two crossings occur if and only if \(b_*<b<a/2\). In that case \(b_c(d)=b\) has precisely two positive solutions, and its monotone branches establish the signs between them. Solving the quadratic \(F(d)=0\) gives the displayed \(d_\pm\); its radicand is strictly positive in this parameter region. At the lower boundary there is one double zero; at the upper boundary there is only a single finite crossing, since \(b=a/2\) reduces \(F\) to a nonconstant linear polynomial. All remaining cases follow from whether the horizontal line \(b\) lies above, below, or tangent to the critical curve.

To make the zero-, one-, and two-crossing boundaries explicit: if \(a\leq2e\), then \(b\leq a/2\) gives negative covariance at every finite \(d\); \(a/2<b<a\) gives exactly one crossing from negative to positive; and \(b\geq a\) gives positive covariance for \(d>0\) (at \(b=a,d=0\) covariance is zero). If \(a>2e\), \(b<b_*\) gives negative covariance at all \(d\), \(b=b_*\) a unique zero without sign change, \(b_*<b<a/2\) two sign reversals, \(a/2\leq b<a\) one negative-to-positive crossing, and \(b\geq a\) positive covariance for \(d>0\). At \(b=a/2\) the single zero is \(d=4e^2/(a-2e)\).

**6. Exact witness.** For \(a=10,b=4,e=1\), substitution gives \(F(d)=-2(d-2)(d-6)\). The exact stationary vectors at \(d=0,4,8\) are respectively
\[
(1,10,10,40)/61,\qquad (23,30,30,40)/123,\qquad(61,50,50,40)/201.
\]
Their cross-products \(uw-v^2\) yield the three rational covariances stated above. This is a strict negative–positive–negative pattern with nonzero covariance in all three exhibited regimes.

## Verification

The standalone standard-library Python program `verify.py` independently constructs the four-state generator and solves its stationary linear system by rational Gaussian elimination; it then compares the solution with the closed form, verifies all balance equations and the covariance sign polynomial over 288 exact-rational parameter combinations (including 1,152 generator-balance checks). It also checks the two exact roots and strict signs at the stated witness, tests the fixed-disturbance threshold on a broader grid, and checks the unique tangency formulas numerically at several parameter values. A complete replay prints `VERIFY_OK assertions=2103`.

The proof of the infinite parameter classification is the algebra in Sections 1–5, **not** this finite enumeration or the numerical tangent checks. The code requires only Python 3 and the standard library: `python3 verify.py`.

## Relationship to prior work

Prior theoretical ecology established that correlated landscape destruction and local recolonization can have opposing effects on metapopulation survival. Johst and Drechsler (2003) investigated spatially correlated disturbance and time to extinction through a spatial simulation. Cornell and Ovaskainen (2008) developed a full perturbation analysis for a spatially extensive, dynamically correlated landscape, with the objective of mean patch occupancy. Wilcox, Cairns and Possingham (2006) analyzed disturbance, patch recovery and quasi-stationary persistence. Strasser and colleagues (2010) treated stochastic disturbance using demographic matrix products and growth-rate sensitivities. These are related in mechanism but differ in state space, observable and regime of analysis from the present two-site irreducible jump chain.

Fidino, Simonis and Magle (2018) provide a general multistate dynamic occupancy statistical framework, deriving stationary state probabilities from a transition matrix. This general stationary-matrix operation alone does not state or imply the exact positive/negative covariance discriminant and double-reversal phase diagram without a parameter correspondence and sign classification.

Calcagno, Cunniffe and Hamelin (2022) showed that patch disturbance can generate apparent positive and negative **between-species** co-occurrence associations via species-specific patch-age profiles. That is an important warning about interpreting association, but differs from the current **between-habitat, same-species** stationary generator and its two catastrophe-rate sign reversals.

In particular, a standard positive additional-neighbor-colonization model has \(b\geq a\), for which the present theorem actually **excludes** both negative covariance and reentrance. The new qualitative behavior requires inhibitory net colonization \(b<a/2\) as well as the sharp immigration-to-local-extinction condition \(a>2e\). Earlier observations of nonmonotone synchrony or correlated destruction in different models do not establish these necessary-and-sufficient conditions.

The full texts of some potentially related older accounts, especially Johst and Drechsler (2003) and Wilcox and colleagues (2006), were not accessible for exhaustive comparison. The result therefore makes no claim of historically certified priority. No general theorem for arbitrary landscape graphs is asserted.

## Limitations

This is a two-patch Markov benchmark with exchangeable habitats, constant exponentially timed transition hazards, global complete resets and perfect state observation. It does not infer a rate from ecological field data; no inference about species abundance, nonlinear demographic dynamics, uneven patch quality or larger habitat networks follows. The presence of an inhibitory establishment effect is a hypothesis that must be assessed for each application. Cross-sectional stationary covariance is not by itself a prediction of extinction time or resilience. Published equivalence under a different ecological or reliability-theory vocabulary remains a residual priority risk, and no independent scientific validation has been performed.

## References

1. Johst, K., and Drechsler, M. (2003). *Are spatially correlated or uncorrelated disturbance regimes better for the survival of species?* Oikos 103, 449–456. First public 21 October 2003. https://doi.org/10.1034/j.1600-0706.2003.12770.x
2. Cornell, S. J., and Ovaskainen, O. (2008). *Exact asymptotic analysis for metapopulation dynamics on correlated dynamic landscapes*. Theoretical Population Biology 74, 209–225. Full author manuscript: https://eprints.whiterose.ac.uk/id/eprint/4943/1/cornells1.pdf ; https://doi.org/10.1016/j.tpb.2008.07.003
3. Wilcox, C., Cairns, B. J., and Possingham, H. P. (2006). *The role of habitat disturbance and recovery in metapopulation persistence*. Ecology 87, 855–863. https://doi.org/10.1890/05-0587
4. Strasser, C. A., Neubert, M. G., Caswell, H., and Hunter, C. M. (2010). *Contributions of high- and low-quality patches to a metapopulation with stochastic disturbance*. Theoretical Ecology 5, 167–179. https://doi.org/10.1007/s12080-010-0106-9
5. Fidino, M., Simonis, J. L., and Magle, S. B. (2018). *A multistate dynamic occupancy model to estimate local colonization–extinction rates and patterns of co-occurrence between two or more interacting species*. Methods in Ecology and Evolution 10, 233–244. https://doi.org/10.1111/2041-210X.13117
6. Calcagno, V., Cunniffe, N. J., and Hamelin, F. M. (2022). *Metacommunity dynamics and the detection of species associations in co-occurrence analyses: Why patch disturbance matters*. Functional Ecology 36, 1483–1499. https://doi.org/10.1111/1365-2435.14047
