# A sharp endpoint-doublet transition for four surveys of Markovian ecological availability

## Finding
For four surveys over a fixed horizon in a stationary two-state availability model, with a shared imperfect detection probability, the globally detection-maximizing placement has a sharp short-horizon boundary regime. At short horizons, the four surveys form two independent detection replicates at each endpoint; after one explicit horizon threshold, the unique optimum is symmetric with two equal outer gaps strictly shorter than the middle gap. Perfect detection is the exceptional case: equal spacing is optimal for every positive horizon.

Write \(\pi\in(0,1)\) for the stationary probability of availability, \(d\in(0,1]\) for detection probability conditional on availability, \(\gamma>0\) for total availability-switching rate, and \(T>0\) for the observation horizon. Set
\[
\alpha=1-\pi d,\qquad \beta=1-(1-\pi)d,\qquad c=\pi(1-\pi)d^2,\qquad R=e^{-\gamma T}.
\]
The critical horizon is
\[
T_c=\gamma^{-1}\log\!\left(\frac{\alpha(\alpha+\beta)}{\alpha^2+c}\right).
\]
For \(0<d<1\), one has \(T_c>0\). If \(T\le T_c\), the unique optimum is at \((t_1,t_2,t_3,t_4)=(0,0,T,T)\). If \(T>T_c\), let \(u\in(R^{1/3},1)\) be the unique root of
\[
H(u)=cu^4+\alpha^2u^3-\alpha\beta Ru-\alpha^2R=0.
\]
The unique optimum is \((0,a,T-a,T)\) with \(a=-\gamma^{-1}\log u\), so \(0<a<T/3\). If \(d=1\), \(T_c=0\) and the unique optimum is the equally spaced schedule \((0,T/3,2T/3,T)\).

## Assumptions and scope
The site is known occupied, but an organism is temporarily available or unavailable. Its availability is a stationary continuous-time Markov chain \(Z_t\in\{0,1\}\), with rates \(0\to1\) equal to \(\gamma\pi\) and \(1\to0\) equal to \(\gamma(1-\pi)\). At each of four non-adaptive inspections \(0=t_1\le t_2\le t_3\le t_4=T\), detection occurs with probability \(d\) when \(Z=1\), and never when \(Z=0\). Conditional on the latent states, all inspection outcomes are independent, even when inspection times coincide (e.g. independent observers or independent instantaneous tests). The objective is the probability of detecting at least once; no inference-variance or field-cost claim is made.

If coincident inspections are forbidden, a boundary optimum is a sharp supremum approached by strictly ordered visits rather than an attained optimum. For the interior regime, all four times are distinct. The model assumes no occupancy turnover, no false positives and constant detection sensitivity.

## Proof
Put \(x=e^{-\gamma(t_2-t_1)}\), \(y=e^{-\gamma(t_3-t_2)}\), and \(z=e^{-\gamma(t_4-t_3)}\). Then \(0<x,y,z\le1\) and \(xyz=R\). The hidden-state transition matrix across a gap with exponential lag \(w\) is
\[
P(w)=\begin{pmatrix}1-\pi+\pi w&\pi(1-w)\\(1-\pi)(1-w)&\pi+(1-\pi)w\end{pmatrix}.
\]
With \(D=\operatorname{diag}(1,1-d)\) and stationary row vector \(v=(1-\pi,\pi)\), the probability \(F\) of no detections is \(vDP(x)DP(y)DP(z)D\mathbf1\). Direct matrix multiplication, retaining every possible availability path, gives
\[
F(x,y,z)=\alpha^4+c\alpha^2y+c\alpha(\alpha+\beta y)(x+z)+c(c+\beta^2y)xz. \tag{1}
\]
All coefficients needed below are strictly positive. At fixed \(y\), the product \(xz=R/y\) is fixed, so \(x+z\ge2\sqrt{R/y}\), with equality only when \(x=z\). Thus **every** global minimizer is symmetric: \(x=z=u\), \(y=R/u^2\), with \(\sqrt R\le u\le1\). Substitution in (1) yields
\[
F(u)=\alpha^4+c\beta^2R+c\left(\frac{\alpha^2R}{u^2}+2\alpha^2u+\frac{2\alpha\beta R}{u}+cu^2\right),
\qquad F'(u)=\frac{2c}{u^3}H(u).\tag{2}
\]
Here \(H''(u)=12cu^2+6\alpha^2u>0\). Furthermore,
\[
\frac{H(\sqrt R)}R=cR+\alpha(\alpha-\beta)\sqrt R-\alpha^2<0.
\]
Indeed the quadratic on the right, considered as a function of \(\sqrt R\in(0,1)\), is strictly convex and has endpoints \(-\alpha^2<0\) and \(c-\alpha\beta=d-1\le0\); convexity makes it strictly negative between them. Finally
\[
H(1)=\alpha^2+c-R\alpha(\alpha+\beta).
\]
If \(H(1)\le0\), strict convexity makes \(H(u)<0\) for \(\sqrt R\le u<1\), so (2) has its unique minimum at \(u=1\). If \(H(1)>0\), strict convexity and the opposite endpoint signs give exactly one zero inside \((\sqrt R,1)\), across which \(F'\) changes from negative to positive. This is the unique global minimum, not merely a stationary local minimum. The threshold for the two cases is precisely \(T=T_c\).

At the uniform-spacing point \(u_0=R^{1/3}\),
\[
H(u_0)=(c-\alpha\beta)R^{4/3}=-(1-d)R^{4/3}.
\]
For \(d<1\), this is strictly negative. Hence the minimizing \(u\) lies strictly to its right, implying \(a<T/3\), including the zero-gap case. For \(d=1\), the polynomial factors as \(H(u)=(1-\pi)[\pi u+(1-\pi)](u^3-R)\), so its unique root is \(R^{1/3}\); the threshold is zero. These computations prove every stated boundary and uniqueness assertion.

## Verification
The self-contained standard-library program `check.py` reproduces the no-detection matrix product as exact rational arithmetic and checks identity (1) on 750 independently selected rational configurations, alongside algebraic boundary and example assertions. It reports 758 successful assertions. These tests are corroborative, not exhaustive proof; the proof is the matrix identity, AM–GM reduction and the strict convexity argument above.

For an exact interior example take \(\pi=d=1/2\), \(\gamma=1\), \(e^{-T}=117/448\). The optimizer has outer lag factors \(u=3/4\), center lag factor \(13/28\), hence \(a=\log(4/3)\), \(T-2a=\log(28/13)\). Its no-detection probability is exactly \(6903/16384\). For the same model at \(T=\log(3/2)\), the optimum consists of endpoint doublets and the no-detection probability is \(31/64\). These are exact rational identities in the exponential gap variables.

## Relationship to prior work
Guillera-Arroita, Ridout and Morgan (2010) analyze occupancy-study allocation across sites and replicate visits, under a constant detectability model, with estimator precision as a main objective. Petitot et al. (2014) optimize amphibian occupancy-monitoring effort and visit periods empirically. Borchers and Langrock (2015) use Markov-modulated animal availability for line-transect inference. None of those inspected analyses gives the four-instant global probability-of-any-detection scheduling law, its sharp endpoint-doublet transition or its necessary strict outer-versus-inner gap ordering. A closely related three-observation scheduling law optimizes a different dimension and does not imply this four-observation global classification. Larger inspection-design and Markov-model optimization results might subsume the specialized conclusion; literature searches are not a guarantee of historical priority.

## Limitations
The finding is about an idealized known-occupied site and a fixed horizon, not the optimal number of visits, information about occupancy, adaptive schedules, correlated errors across simultaneous observers, or practical travel and deployment costs. The boundary case presumes independent tests at identical times; time separation constraints change the optimum. This is an analytical model; no ecological field data validate its use for particular species. The general \(n\)-visit optimum is not established. Historical priority has not been independently certified.

## References
1. Guillera-Arroita, G., Ridout, M. S., and Morgan, B. J. T. (2010), “Design of occupancy studies with imperfect detection,” *Methods in Ecology and Evolution*, 1, 131–139. First online 2010-05-04. https://doi.org/10.1111/j.2041-210X.2010.00017.x
2. Petitot, M., Manceau, N., Geniez, P., and Besnard, A. (2014), “Optimizing occupancy surveys by maximizing detection probability: application to amphibian monitoring in the Mediterranean region,” *Ecology and Evolution*, 4, 3538–3549. https://doi.org/10.1002/ece3.1207
3. Borchers, D. L., and Langrock, R. (2015), “Double-Observer Line Transect Surveys with Markov-Modulated Poisson Process Models for Animal Availability,” *Biometrics*, 71, 1060–1069. https://doi.org/10.1111/biom.12341
