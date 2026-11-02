# Exact population-size identification from imperfectly detected herding dynamics

## Finding

Consider a stationary finite-population recruitment process with an unobserved population size \(N\geq2\), two positive spontaneous switching rates, and a positive imitation rate. At each census, only a fresh independent fraction of individuals currently choosing one option is detected. Four scalar second-order summaries—a mean, a variance, and covariances at two positive equally spaced lags—determine the detection probability and all positive dynamical rates *conditional on each feasible population size*. The possible integer population sizes form one explicit open interval, which can contain a single integer, finitely many integers, infinitely many integers, or none.

Write the observed mean, variance, and successive lag covariances as \(m,v,c_1,c_2\), with known lag \(\Delta>0\). For an interior model, set
\[
q=\frac{c_2}{c_1},\qquad s=\frac{c_1^2}{c_2},\qquad p=1-\frac{v-s}{m}.
\]
Necessary conditions are \(m>0\), \(0<c_2<c_1\), and \(0<v-s<m\). Define
\[
L=\frac{s+m^2}{pm},\qquad
U=\begin{cases}\dfrac{m^2}{pm-s},&pm>s,\\+\infty,&pm\leq s.\end{cases}
\]
The **complete feasible population-size set** is
\[
\boxed{\mathcal N=\{N\in\mathbb Z:\ N\geq2,\ L<N<U\}.}
\]
These conditions and \(\mathcal N\ne\varnothing\) are also sufficient: every such integer \(N\) corresponds to exactly one positive dynamical parameter triple and the displayed detection probability. For any feasible data, the set is unbounded exactly when \(s\geq pm\); otherwise it is finite. This is a sharp distinction about *aggregate second-order information*, not about the complete observation law.

## Assumptions and scope

The latent count \(X_t\in\{0,1,\ldots,N\}\) is the stationary irreducible continuous-time birth–death process with transitions
\[
\lambda_k=(N-k)(a+hk),\qquad
\mu_k=k[b+h(N-k)],
\]
for \(a,b,h>0\). Here \(a\) is spontaneous switching toward the observed option, \(b\) switching away, and \(h\) is pairwise recruitment in either direction. The \(N\) individuals and all rates are constant over the observation interval. The process is initially stationary.

A census at any prescribed time \(t\) reports \(Y_t\mid X_t=k\sim\operatorname{Binomial}(k,p)\), where \(0<p<1\) is unknown. Conditional on the entire latent trajectory, independently redrawn detection indicators are used at distinct census times. In particular, this is *not* a permanently tagged sample or persistent individual-specific visibility model. The four exact population summaries are
\[
m=\mathbb EY_0,\quad v=\operatorname{Var}(Y_0),\quad c_j=\operatorname{Cov}(Y_0,Y_{j\Delta})\quad(j=1,2).
\]
No claim is made about finite-sample precision, nonstationary data, heterogeneous imitation, or changing detection. The primary mathematical application is opinion and recruitment dynamics (MSC2020 91D30).

## Proof

Put \(A=a+b\), \(r=a/A\), and \(M=Nr\). The generator obeys
\[
\mathcal Gk=Na-Ak,
\]
so stationarity yields \(\mathbb EX=M\), and conditional expectation at lag \(t\geq0\) is
\[
\mathbb E[X_{u+t}\mid X_u]=M+(X_u-M)e^{-At}.
\]
For the second moment, the birth–death generator gives
\[
\mathcal G k^2=2k(Na-Ak)+Na+(b-a)k+2h k(N-k).
\]
Setting its stationary expectation to zero and substituting \(M\) gives the *exact finite-state* variance
\[
V=\operatorname{Var}(X)=Nr(1-r)\frac{A+Nh}{A+h}.
\]
Consequently \(\operatorname{Cov}(X_0,X_t)=Ve^{-At}\). Independent binomial thinning produces
\[
\mathbb EY=pM,\qquad \operatorname{Var}(Y)=p^2V+p(1-p)M,
\]
\[
\operatorname{Cov}(Y_0,Y_t)=p^2Ve^{-At}\quad(t>0).
\]
Hence \(q=e^{-A\Delta}\), \(s=p^2V\), and \(v-s=m(1-p)\), proving recovery of \(A=-\log q/\Delta\), \(s\), and \(p\).

For each proposed integer \(N\), define
\[
r_N=\frac{m}{Np},\qquad
R_N=\frac{s}{p^2Nr_N(1-r_N)}=\frac{s}{pm-m^2/N}.
\]
The recruitment variance factor satisfies \(R_N=(A+Nh)/(A+h)\). For \(N\geq2\), the existence of positive \(h\) is exactly \(1<R_N<N\), in which case
\[
\boxed{a=Ar_N,\quad b=A(1-r_N),\quad h=A\frac{R_N-1}{N-R_N}.}
\]
Algebraically \(R_N<N\) is equivalent to \(N>L\), which also implies \(0<r_N<1\); \(R_N>1\) is equivalent to \(N<U\) when \(pm>s\), and automatic otherwise. These conditions prove both necessity and sufficiency, together with uniqueness for known \(N\). The integer identified set therefore has no gaps; its sharp upper-bounded versus unbounded transition is \(s=pm\). Because **every positive-lag covariance** equals \(s e^{-At}\), observing further aggregate second-order lags cannot shrink \(\mathcal N\).

Two positive lags are generically necessary for this four-summary calibration: with only \(m,v,c_1\), let \(A'\) vary in a sufficiently small open interval about an interior model's \(A\), set \(s'=c_1e^{A'\Delta}\), \(p'=1-(v-s')/m\), and use the displayed reconstruction for the known \(N\). All strict inequalities persist locally, producing distinct positive parameter triples with exactly the same three summaries. This is a local nonidentifiability statement, not a denial of information in full time-series distributions.

## Verification

For an exact *unbounded* example, take \(N=4\), \(a=1\), \(b=2\), \(h=1\), \(p=3/4\), and \(\Delta=(\log2)/3\). Then
\[
(m,v,c_1,c_2)=(1,9/8,7/16,7/32),\quad L=5/2,\quad U=+\infty.
\]
Every integer \(N\geq3\) is a different compatible latent population size, each with explicitly reconstructed positive rates.

For an exact *singleton* example, take \(N=4\), \(a=9\), \(b=1\), \(h=1/100\), \(p=3/4\), and \(\Delta=(\log2)/10\). Then
\[
(m,v,c_1,c_2)=\left(\frac{27}{10},\frac{175797}{200200},\frac{20331}{200200},\frac{20331}{400400}\right),
\]
\[
L=\frac{3704}{1001},\qquad U=\frac{6006}{1501},\qquad \mathcal N=\{4\}.
\]
Thus the second-order summaries sometimes determine the unknown integer population size exactly, despite incomplete detection.

The standalone script `check.py` recomputes stationary weights from birth–death detailed balance using exact rational arithmetic for \(1{,}100\) parameter configurations, verifies the moment and inverse identities, and checks the claimed size sets and distinct compatible mechanisms in both examples. These finite checks corroborate but do not replace the all-parameter algebraic proof.

## Relationship to prior work

Kirman's recruitment model introduced spontaneous switches competing with copying. Moran, Fosset, Benzaquen and Bouchaud derived the continuum beta-type stationary law and relaxation modes. Holehouse and Moran gave exact finite-population time-dependent solutions, including asymmetric variants. Carro, Toral and San Miguel examined aggregate correlations and network heterogeneity in noisy-voter processes. These establish the underlying stochastic machinery and are not claimed as new.

The result here instead characterizes the **entire image and inverse fibers of four low-order observable summaries after independent, unknown binomial detection**, including the exact open integer interval of compatible unknown population sizes, its bounded/unbounded boundary, and the sharp requirement for a second lag. Royle's binomial observation framework and later closed-population N-mixture identifiability work address detection under different latent-population assumptions; their full repeated-visit laws are not identical to the moving-state second-order summaries here.

## Limitations

The result is a structural, exact-population-moment identification theorem. Moment estimation from finite correlated time series can be unstable; the logarithm and sharp integer bounds can magnify noise. Temporal stationarity, homogeneous and symmetric pairwise recruitment, binomial detection, conditional independence of fresh detection attempts, and known lag are essential. Unknown \(N\) is generally not identified from four moments, even if arbitrarily many second-order lags are added; the full joint law of observations may contain extra information. The result does not establish priority beyond the literature actually inspected, nor does it experimentally validate any behavioral model.

## References

- A. Kirman, “Ants, Rationality, and Recruitment,” *Quarterly Journal of Economics* **108** (1993), 137–156. https://doi.org/10.2307/2118498. Earliest verified public date: 1993-02-01.
- J. Moran, A. Fosset, M. Benzaquen and J.-P. Bouchaud, “Schrödinger's ants: A continuous description of Kirman's recruitment model,” *Journal of Physics: Complexity* **1** (2020), 035002. https://arxiv.org/abs/2004.06667.
- J. Holehouse and J. Moran, “Exact time-dependent dynamics of discrete binary choice models,” *Journal of Physics: Complexity* **3** (2022), 035005. https://arxiv.org/abs/2201.09573.
- A. Carro, R. Toral and M. San Miguel, “The noisy voter model on complex networks,” *Scientific Reports* **6** (2016), 24775. https://doi.org/10.1038/srep24775.
- J. A. Royle, “N-Mixture Models for Estimating Population Size from Spatially Replicated Counts,” *Biometrics* **60** (2004), 108–115. https://doi.org/10.1111/j.0006-341X.2004.00142.x.
