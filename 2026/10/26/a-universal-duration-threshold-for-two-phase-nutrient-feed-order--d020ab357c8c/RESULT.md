# A universal duration threshold for two-phase nutrient-feed ordering in a Monod chemostat

## Finding

Consider a chemostat whose limiting nutrient is externally supplied in two constant-concentration blocks of equal duration. At infinitesimal biomass, compare high-feed-first (HL) and low-feed-first (LH) schedules with identical total nutrient input. There is a universal duration threshold
\[
\Theta=\log(1+\sqrt{2})=0.8813735870195429\ldots
\]
independent of the nutrient concentrations, half-saturation constant, and microbial maximum growth rate. For \(D\tau\leq\Theta\), HL always yields strictly more cumulative rare-invader log growth, irrespective of the initial substrate. For \(D\tau>\Theta\), exactly one positive initial-substrate crossover exists: HL is better below it and LH is better above it.

## Assumptions and scope

Fix \(D,K,m,\tau>0\), feed concentrations \(0\leq\ell<h\), and initial nutrient \(s\geq0\). Nutrient \(S(t)\) and an infinitesimally rare microbial population \(x(t)\) obey
\[
S'(t)=D(c(t)-S(t)),\qquad x'(t)=\left(\frac{m S(t)}{K+S(t)}-D\right)x(t).
\]
The absence of the biomass-consumption term in the nutrient equation is the exact zero-biomass linearization of an ordinary Monod chemostat, **not** an approximation claimed to hold for substantial biomass. The feed \(c(t)\) is either \(h\) on \([0,\tau)\), \(\ell\) on \([\tau,2\tau]\), or the reverse. The two experiments have equal initial nutrient, identical parameters, equal total feed-concentration time integral, and no biomass-dependent feedback. Define
\[
G(s)=\int_0^{2\tau}\left(\frac{S_{HL}(t;s)}{K+S_{HL}(t;s)}-\frac{S_{LH}(t;s)}{K+S_{LH}(t;s)}\right)dt.
\]
Then \(\log[x_{HL}(2\tau)/x_{LH}(2\tau)]=mG(s)\) when the two initial rare-biomass levels agree. Thus the sign of \(G(s)\) ranks their finite-time multiplicative invasion gains. No threshold is claimed for the nonlinear competition system or for continued periodic operation.

## Proof

**1. Exactly one change of sign in the resource-order difference.** Put \(\Delta=h-\ell>0\). The solution on a constant-feed block is
\[
\Phi_c(z,t)=c+(z-c)e^{-Dt}.
\]
For \(d(t)=S_{HL}(t;s)-S_{LH}(t;s)\), direct solution gives, independent of \(s\),
\[
d(t)=\begin{cases}
\Delta(1-e^{-Dt}),&0\leq t\leq\tau,\\
\Delta\left[(2-e^{-D\tau})e^{-D(t-\tau)}-1\right],&\tau\leq t\leq2\tau.
\end{cases}
\]
Consequently \(d(t)>0\) for \(0<t<t_c\), \(d(t)<0\) for \(t_c<t\leq2\tau\), and the unique interior sign change occurs at
\[
t_c=\tau+D^{-1}\log(2-e^{-D\tau})\in(\tau,2\tau).
\]
The final inclusion holds because \(2-e^{-a}<e^a\) for \(a>0\).

**2. Strict single-crossing as initial nutrient increases.** For either schedule write
\[
S_j(t;s)=se^{-Dt}+b_j(t),\qquad Q_j(t)=e^{Dt}(K+b_j(t)),
\]
where \(b_j(t)=S_j(t;0)\geq0\). In the interior of a constant-feed block,
\[
Q'_j(t)=D e^{Dt}(K+c_j(t))>0.
\]
At the feed-switching instant \(Q_j\) is continuous; hence \(Q_j\) is strictly increasing on the whole interval. The Monod difference is
\[
\frac{S_{HL}}{K+S_{HL}}-\frac{S_{LH}}{K+S_{LH}}=d(t)w(t;s),\quad
w(t;s)=\frac{Ke^{2Dt}}{(s+Q_{HL}(t))(s+Q_{LH}(t))}>0.
\]
For \(s_2>s_1\geq0\), the ratio
\[
\frac{w(t;s_2)}{w(t;s_1)}=
\prod_{j\in\{HL,LH\}}\frac{s_1+Q_j(t)}{s_2+Q_j(t)}
\]
is strictly increasing in \(t\). Pairing the positive segment \(t<t_c\) with the negative segment \(t>t_c\), this implies the exact single-crossing property
\[
G(s_1)\leq0\quad\Longrightarrow\quad G(s_2)<0.
\]
Indeed, subtract the ratio at \(t_c\) from the strictly increasing ratio; its product with \(d(t)w(t;s_1)\) is negative on both segments. Therefore \(G\) has at most one zero, if any, and can cross only from positive to negative.

**3. The zero-substrate comparison is strictly positive.** Write \(v\in(0,\tau)\), \(p=1-e^{-Dv}\), \(q=(1-e^{-D\tau})e^{-Dv}>0\). Under \(s=0\), the first-block nutrient values are \(hp\) and \(\ell p\); in the second block at \(\tau+v\), they are \(\ell p+hq\) and \(hp+\ell q\). Define
\[
A=(K+hp)(K+\ell p),\quad B=(K+\ell p+hq)(K+hp+\ell q).
\]
Since \(h>\ell\geq0\), \(q>0\), \(B>A>0\). Adding the two signed Monod differences at times \(v\) and \(\tau+v\) yields
\[
K\Delta\left[\frac pA+\frac{q-p}{B}\right]=K\Delta\left[p\left(\frac1A-\frac1B\right)+\frac qB\right]>0.
\]
Integration over \(v\in(0,\tau)\) gives \(G(0)>0\).

**4. A universal asymptotic moment sets the transition.** Dominated convergence over the fixed compact time interval gives
\[
\lim_{s\to\infty}\frac{s^2G(s)}K=I:=\int_0^{2\tau}d(t)e^{2Dt}\,dt.
\]
Integrating the explicit two branches of \(d(t)\), with \(E=e^{D\tau}>1\), gives
\[
I=\frac{\Delta(E-1)^2}{2D}(1+2E-E^2).
\]
Thus \(I<0\) exactly when \(E>1+\sqrt2\), equivalently \(D\tau>\Theta\); there is then a positive unique zero by continuity, step 2, and step 3.

If \(I\geq0\), even equality at \(D\tau=\Theta\) allows no finite zero: for any finite \(s\), the ratio of the limiting weight \(Ke^{2Dt}\) to \(w(t;s)\) equals \((s+Q_{HL}(t))(s+Q_{LH}(t))\), strictly increasing in \(t\). The same one-sign-change argument applied to this weight ratio shows that \(G(s)\leq0\) would force \(I<0\), a contradiction. Hence \(G(s)>0\) at all finite \(s\) whenever \(D\tau\leq\Theta\). This establishes both regimes and their exact boundary.

## Verification

For explicit evaluation define the constant-feed Monod integral
\[
J(z,c)=\tau-\frac K{D(K+c)}\log\left(\frac{(K+c)e^{D\tau}+z-c}{K+z}\right),\qquad
\Phi_c(z)=c+(z-c)e^{-D\tau}.
\]
Then the zero defining the crossover can be computed without time discretization from
\[
G(s)=J(s,h)+J(\Phi_h(s),\ell)-J(s,\ell)-J(\Phi_\ell(s),h).
\]
For \(D=K=\tau=1\), \(h=4\), \(\ell=1\), the unique critical starting substrate is
\[
s_*=53.1340923371102330498336150935937076927\ldots.
\]
The included `chemostat_finite_feed_verification.py` checks the closed-form formula against independent numerical quadrature for 1,000 pseudorandom admissible parameter sets (fixed seed), checks the safe-duration sign in 503 of those cases, and recomputes the example root at 70-digit working precision. Run `python chemostat_finite_feed_verification.py` with `mpmath` and `scipy` available. These finite experiments are diagnostic; the preceding argument is the infinite-parameter proof.

## Relationship to prior work

Hsu (1980) studies Monod/Holling-II nutrient responses under smooth periodic forcing and long-term competition; its model motivates the zero-biomass variational system here. Butler, Hsu and Waltman (1985) study periodic **washout** and coexistence, rather than a finite two-block order comparison. Stephanopoulos, Frederickson and Aris (1979) treat periodically varying reactor inputs and Floquet stability; their publisher abstract discusses species coexistence rather than the particular initial-substrate crossover and parameter-free duration boundary. The latter paper was not available for full-text checking, so that absence of coverage is **not** asserted for the whole paper. Smith (1981) is likewise concerned with oscillating-chemostat coexistence. The present theorem is limited to a two-block finite-time rare-invader multiplicative-gain comparison, and might admit reformulation as an order-weighted single-crossing theorem.

## Limitations

The theorem neither optimizes arbitrary time-dependent feeding histories nor predicts positive-biomass feedback, asymptotic invasion exponents, sustained coexistence, or nonlinear management outcomes. It assumes constant positive dilution, Monod uptake, two **equal** durations, and nonnegative feed concentrations. An earlier or general rearrangement inequality could subsume its finite-duration classification. Some directly related historical full texts, notably the 1979 variable-input reactor paper, were inaccessible; originality therefore retains a specific unresolved literature risk. The catalog date for the Hsu (1980) motivating source is reported as 1980-04-01; original day-of-public-release documentation has not been independently recovered.

## References

1. S. B. Hsu (1980), *A Competition Model for a Seasonally Fluctuating Nutrient*, Journal of Mathematical Biology 9, 115–132, doi:10.1007/BF00275917. Author-hosted full text: https://www.math.nthu.edu.tw/~sbhsu/JMB1980.pdf .
2. G. J. Butler, S. B. Hsu and P. Waltman (1985), *A Mathematical Model of the Chemostat with Periodic Washout Rate*, SIAM Journal on Applied Mathematics 45, 435–449, doi:10.1137/0145025. Full text: https://www.math.nthu.edu.tw/~sbhsu/Hsu1985.pdf .
3. G. Stephanopoulos, A. G. Frederickson and R. Aris (1979), *The Growth of Competing Microbial Populations in a CSTR with Periodically Varying Inputs*, AIChE Journal 25, 863–872, doi:10.1002/aic.690250515. Publisher abstract inspected; full text not inspected.
4. H. L. Smith (1981), *Competitive Coexistence in an Oscillating Chemostat*, SIAM Journal on Applied Mathematics, doi:10.1137/0140042. Abstract-level comparison.
5. OpenAlex record W1995744938, catalog publication date of reference 1: https://openalex.org/W1995744938 .
