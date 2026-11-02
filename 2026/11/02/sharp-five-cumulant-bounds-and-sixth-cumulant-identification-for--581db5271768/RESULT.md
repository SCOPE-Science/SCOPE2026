# Sharp five-cumulant bounds and sixth-cumulant identification for two-zone tracer timing

## Finding
Consider a conservative tracer transported through a fixed stream reach with unknown positive mobile travel time, two distinct exponential storage zones, and additive independent zero-mean Gaussian timing error of unknown positive variance. Exact knowledge of the first five population cumulants of observed passage time gives a *sharp, generally nontrivial open interval* for the timing-error variance, but does not identify the six physical parameters. A sixth cumulant determines every parameter up to exchange of the zone labels. Moreover, conditional on five cumulants, the sixth cumulant has an exact sharp lower bound, and every value above that bound is realized by exactly one admissible model.

Here is the complete, constructive classification. Write \(k_j\) for the \(j\)-th cumulant of the observed time, and set
\[
 c=\frac{k_3}{6},\qquad \mu=\frac{k_4}{24c},\qquad v=\frac{k_5}{120c}-\mu^2.
\]
There exists a **strictly positive** two-zone, distinct-rate, positive-noise model with the prescribed first five cumulants **if and only if**
\[
 c>0,\quad \mu>0,\quad v>0,\quad k_1>\frac{c}{\mu^2},\quad k_2>\frac{2c}{\mu}.
\]
When these inequalities hold, define for \(0<d<\mu\)
\[
 x_-(d)=\mu-d,\quad x_+(d)=\mu+\frac vd,\qquad
 w_-(d)=\frac{cv}{d^2+v},\quad w_+(d)=\frac{cd^2}{d^2+v},
\]
\[
 S_1(d)=\frac{w_-}{x_-}+\frac{w_+}{x_+},\qquad
 S_2(d)=\frac{w_-}{x_-^2}+\frac{w_+}{x_+^2}.
\]
Both \(S_1,S_2\) increase strictly from \(c/\mu,c/\mu^2\), respectively, to \(+\infty\). Consequently there are unique \(d_{\rm noise},d_{\rm mobile}\in(0,\mu)\) satisfying
\[
 S_1(d_{\rm noise})=\frac{k_2}{2},\qquad S_2(d_{\rm mobile})=k_1.
\]
Put \(d_*=\min\{d_{\rm noise},d_{\rm mobile}\}\). The **entire** compatible family is parameterized without duplication (after labeling by reciprocal return time) by \(0<d<d_*\), with mobile transit time \(m\), timing-error variance \(s^2\), exponential return rates \(\beta_\pm\), and capture rates \(\alpha_\pm\) given by
\[
 m=k_1-S_2(d),\qquad s^2=k_2-2S_1(d),\qquad
 \beta_\pm=\frac{1}{x_\pm(d)},\qquad
 \alpha_\pm=\frac{w_\pm(d)}{m x_\pm(d)^3}.
\]
In particular the **sharp set of permissible clock-error variances** is precisely
\[
 \boxed{\quad k_2-2S_1(d_*)<s^2<k_2-\frac{2c}{\mu}.\quad}
\]
The lower endpoint is nonnegative; it is zero exactly when \(d_{\rm noise}\leq d_{\rm mobile}\). Neither endpoint is attained inside the strictly positive, distinct-two-zone model.

The sixth cumulant satisfies the exact strictly decreasing law
\[
 k_6=720c\left[\mu^3+3\mu v+v\left(\frac vd-d\right)\right].
\]
Hence **six-cumulant compatibility** adds exactly the sharp inequality
\[
 \boxed{\quad k_6>K_{6,*}:=720c\left[\mu^3+3\mu v+v\left(\frac v{d_*}-d_*\right)\right].\quad}
\]
Every larger \(k_6\) occurs uniquely. Explicitly let
\[
 z=\frac{k_6/(720c)-\mu^3-3\mu v}{v},\qquad
 d=\frac{-z+\sqrt{z^2+4v}}{2};
\]
then the displayed formulas recover all six parameters. The lower bound and variance interval are both sharp, and the first five cumulants alone always admit infinitely many distinct admissible models.

For an exact illustration, take \(m=2\), \((\alpha_1,\alpha_2)=(1/2,3/4)\), \((\beta_1,\beta_2)=(1,3)\), and \(s^2=1/4\). The six cumulants are
\[
 (k_1,k_2,k_3,k_4,k_5,k_6)
 =\left(\frac72,\frac{31}{12},\frac{19}{3},\frac{220}{9},\frac{3260}{27},\frac{19480}{27}\right).
\]
The first five by themselves imply the strict upper noise bound \(s^2<87/220\); the sixth recovers \(s^2=1/4\) and the other parameters exactly.

## Assumptions and scope
A mobile tracer particle requires a deterministic **active travel time** \(m>0\) to cross the reach. Independently for each zone \(i\in\{1,2\}\), storage entries occur as a Poisson process of intensity \(\alpha_i>0\) per unit *mobile* time; each entry contributes an independent exponential holding time of return rate \(\beta_i>0\). The two return rates are distinct. The particle does not advance while stored, there is no adsorption or loss, and spatial dispersion is neglected. With independent \(N_i\sim\operatorname{Poisson}(m\alpha_i)\) and \(E_{i,j}\sim\operatorname{Exp}(\beta_i)\),
\[
 T=m+\sum_{i=1}^2\sum_{j=1}^{N_i}E_{i,j},\qquad Y=T+G,
 \quad G\sim N(0,s^2),\quad s^2>0,
\]
where every variable on the right is independent except for its stated grouping. The zero mean of \(G\) is known; its variance is not. The population cumulants of \(Y\), not sample estimates, are assumed known. All conclusions concern this model only. The zone-label symmetry is resolved by ordering \(x_-=1/\beta_-<x_+=1/\beta_+\).

## Proof
**1. Cumulants and positive two-node representation.** The cumulant generating function is analytic near zero and equals
\[
 \log\mathbb E e^{tY}=mt+\frac{s^2t^2}{2}
 +m\sum_{i=1}^{2}\alpha_i\left(\frac{\beta_i}{\beta_i-t}-1\right).
\]
Thus \(k_1=m+m\sum_i\alpha_i/\beta_i\), \(k_2=s^2+2m\sum_i\alpha_i/\beta_i^2\), and for every integer \(j\ge3\), \(k_j=j!m\sum_i\alpha_i/\beta_i^j\). Put \(x_i=1/\beta_i\), \(w_i=m\alpha_i x_i^3\). It follows that
\[
 \frac{k_{3+r}}{(3+r)!}=\sum_{i=1}^2 w_i x_i^r \quad (r=0,1,2,3),
\]
while \(k_1=m+\sum_i w_i/x_i^2\) and \(k_2=s^2+2\sum_i w_i/x_i\).

**2. All representations of the first three node moments.** Write \(c=\sum_iw_i\), \(\mu=(\sum_iw_ix_i)/c\), and \(v=(\sum_iw_ix_i^2)/c-\mu^2\). Positivity and distinctness force \(c,\mu,v>0\). Conversely, any positive two-point measure on \((0,\infty)\) with these three statistics has one node \(a=\mu-d\), where \(0<d<\mu\), and its other node and weights are forced by the mean and variance constraints to be exactly \(x_+(d),w_-(d),w_+(d)\) above. The formulas give strictly positive distinct nodes and weights for every such \(d\). Thus there are no omitted representations.

**3. Positivity cuts out one sharp interval.** Direct differentiation of the displayed rational expressions gives
\[
 S_1'(d)=\frac{cv(d^2+v)}{(\mu-d)^2(\mu d+v)^2}>0,
\]
\[
 S_2'(d)=\frac{2cv(d^2+v)(-d^2+2\mu d+v)}{(\mu-d)^3(\mu d+v)^3}>0.
\]
Here \(-d^2+2\mu d+v>0\) because \(0<d<\mu\) and \(v>0\). Their limiting values at \(d\downarrow0\) are \(c/\mu,c/\mu^2\), and each diverges as \(d\uparrow\mu\). Therefore \(m=k_1-S_2(d)>0\) and \(s^2=k_2-2S_1(d)>0\) hold for some \(d\) if and only if the five stated strict inequalities hold; when they hold, the admissible set is exactly \((0,d_*)\). Since \(s^2(d)\) is continuous and strictly decreasing, its exact image is the stated open interval, not merely a bound. This also constructs infinitely many models sharing the five cumulants, showing five insufficient even locally.

**4. Sixth cumulant, sharpness and uniqueness.** For a two-point law with mean \(\mu\), variance \(v\), and nodes \(\mu-d,\mu+v/d\), the third centered moment is \(v(v/d-d)\). Expanding its third raw moment gives
\[
 \sum_iw_ix_i^3=c[\mu^3+3\mu v+v(v/d-d)].
\]
This proves the formula for \(k_6\). Its derivative with respect to \(d\) is \(-720cv(1+v/d^2)<0\), so it maps \((0,d_*)\) bijectively onto \((K_{6,*},\infty)\). Solving its quadratic relation gives the displayed positive solution for \(d\), after which every parameter is reconstructed uniquely. The strict endpoints correspond either to a vanishing positive physical parameter, or to a singular vanishing-weight/infinite-return-time limit; they cannot be attained under the hypotheses.

## Verification
Run `python3 checks/reproduce.py` from the extracted package root. Its standard-library-only exact-rational checks reconstructed 729 admissible parameter sets, matched all six cumulants, verified the two-node moment identities and compatibility inequalities, and constructed a second distinct strictly positive model sharing the sample's first five cumulants but not its sixth. The universal equalities, inequalities, completeness and strict optimality above follow from the proof, not from the finite checks.

## Relationship to prior work
Marion, Zaramella and Bottacin-Busolin (2008) formulated river solute transport using multiple storage zones and Poisson capture counts. Luo, Cirpka, Dentz and Carrera (2008) developed temporal-moment relations for arbitrary mass-transfer memory functions. Kelleher and colleagues (2013) emphasized practical identifiability limits in transient-storage calibration. Day-Lewis and Singha (2008) inferred mass-transfer parameters using *both* mobile and bulk geoelectrical moments, a different data design. Gaussian-noise cancellation of higher cumulants and finite exponential reconstruction by Prony-type methods are established general mathematical tools. The claim here is not that those tools or multizone transport are new: the specifically characterized five-cumulant feasible noise interval, sharp sixth-cumulant lower edge, and corresponding exact physical reconstruction concern their joint model under a single passage-time measurement distribution. Broader finite-moment inverse theory may subsume this specialization; priority remains provisional.

## Limitations
Structural population-level identification is not statistical consistency or stable estimation from finitely many measurements. Sixth-order cumulants can be extremely sensitive to rare delayed arrivals and measurement truncation. The conclusions assume exactly two distinct positive exchange rates, Poisson trapping in active mobile time, exponential holds, deterministic mobile travel time, Gaussian *zero-mean* independent clock error, no hydrodynamic dispersion, and full mass recovery. Equal return rates collapse the two zones into one; unknown clock bias, general measurement error, spatially variable transport and noisy finite samples fall outside the theorem. The published full-text comparison was limited to the accessible material described in the review; priority is not independently certified.

## References
1. Marion, A., Zaramella, M., and Bottacin-Busolin, A. (2008), *Solute transport in rivers with multiple storage zones: The STIR model*, Water Resources Research 44. DOI: 10.1029/2008WR007037. Publicly dated 14 October 2008.
2. Luo, J., Cirpka, O. A., Dentz, M., and Carrera, J. (2008), *Temporal moments for transport with mass transfer described by an arbitrary memory function in heterogeneous media*, Water Resources Research 44. DOI: 10.1029/2007WR006262. Publicly dated 18 January 2008.
3. Day-Lewis, F. D., and Singha, K. (2008), *Geoelectrical inference of mass transfer parameters using temporal moments*, Water Resources Research 44. DOI: 10.1029/2007WR006750.
4. Kelleher, C., et al. (2013), *Identifiability of transient storage model parameters along a mountain stream*, Water Resources Research 49. DOI: 10.1002/wrcr.20413.
5. Kumaresan, R., Tufts, D. W., and Scharf, L. L. (1984), *A Prony method for noisy data: Choosing the signal components and selecting the order in exponential signal models*, Proceedings of the IEEE 72, 230–233. DOI: 10.1109/PROC.1984.12849.
6. Ueng, F.-B., and Su, Y.-T. (1997), *Blind identification and deconvolution algorithms using higher-order cumulants* (repository bibliographic abstract consulted). General high-order Gaussian-noise cancellation, not the river-specific interval theorem.
