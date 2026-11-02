# Arbitrarily many separated recession-exponent peaks from positive linear reservoirs

## Finding
For each fixed integer \(n\ge3\), a sum of \(n\) positive independent *linear* reservoir discharges can have at least \(n-1\) distinct, pronounced peaks in its instantaneous recession exponent. Moreover, each peak approaches the same nontrivial height \(9/8\), while intervening troughs approach \(1\). Thus a succession of apparent nonlinear-recession episodes does not, by itself, require nonlinear drainage physics.

## Assumptions and scope
Let \(n\ge3\) be fixed, \(R>1\), and \(t\ge0\). Define
\[
E_0=0,\qquad E_j=\sum_{k=1}^j2^{k-1}(n-k),\quad 1\le j<n,
\]
\[
Q(t)=\sum_{j=0}^{n-1}a_j e^{-\lambda_jt},\qquad
\lambda_j=2^j,\quad a_j=R^{E_j}>0.
\]
These are uncoupled linear reservoirs with discharge \(Q_j(t)=\lambda_j S_j(t)\), storage \(S_j(t)=a_j e^{-\lambda_j t}/\lambda_j\), and \(\dot S_j=-\lambda_jS_j\). Define the dimensionless *instantaneous* exponent
\[
\beta(t)=\frac{d\log(-Q'(t))}{d\log Q(t)}
=\frac{Q(t)Q''(t)}{Q'(t)^2}.
\]
All derivatives exist and \(Q>0\), \(Q'<0\). This is a local log-slope, not a power-law exponent estimated over an arbitrary observation interval.

**Theorem.** There is \(R_n>1\) such that, for every \(R>R_n\), \(\beta\) has at least \(n-1\) distinct strict local maxima \(t_{i,R}\), \(1\le i<n\), satisfying
\[
t_{i,R}=(n-i)\log R+\frac{\log 2+O_n(R^{-1})}{2^{i-1}},\qquad
\beta(t_{i,R})=\frac98+O_n(R^{-1}).
\]
For each \(2\le i<n\), there is a time strictly between consecutive peak neighborhoods at which \(\beta(t)\to1\) as \(R\to\infty\). In particular, arbitrarily many distinguishable peaks of nonvanishing height above \(1\) occur among positive linear reservoirs.

## Proof
**1. Adjacent-component transitions.** Write the logarithm of the unnormalized contribution of component \(j\) as \(L_j(t)=E_j\log R-2^j t\). Because
\[
E_i-E_{i-1}=2^{i-1}(n-i),
\]
adjacent lines \(L_{i-1}\) and \(L_i\) meet at \(T_i=(n-i)\log R\). The intersection times satisfy \(T_1>T_2>\cdots>T_{n-1}>0\) and successive differences equal \(\log R\).

For fixed \(i\in\{1,\dots,n-1\}\), put \(v=2^{i-1}(t-T_i)\). The ratio of the \(i\)-term to the \((i-1)\)-term is exactly \(s=e^{-v}\). Every nonadjacent component is exponentially suppressed in \(\log R\) throughout any bounded \(v\)-interval. Indeed, for \(j<i-1\), comparison at the successive transition \(T_{i-1}>T_i\) already places component \(i-2\) at most \(R^{-2^{i-2}}\) relative to component \(i-1\) at \(T_i\); earlier components have still smaller relative weights. For \(j>i\), the next transition \(T_{i+1}<T_i\) places component \(i+1\) at most \(R^{-2^i}\) relative to component \(i\), and later components are still smaller. At the end indices only the applicable side is present. For fixed \(n\), the total nonadjacent weight and its first two \(v\)-derivatives are therefore \(O_n(R^{-1})\) times the adjacent pair, uniformly on every compact \(v\)-interval. The derivatives merely multiply terms by constants depending on the fixed rates \(2^j\).

**2. Two-component limit.** Since \(\beta=(\sum w_j)(\sum\lambda_j^2w_j)/(\sum\lambda_jw_j)^2\) with \(w_j=a_je^{-\lambda_jt}\), the two adjacent rates \(\lambda_{i-1}\) and \(2\lambda_{i-1}\) yield, upon dividing by common factors,
\[
B(v)=\frac{(1+s)(1+4s)}{(1+2s)^2}
=1+\frac{s}{(1+2s)^2},\qquad s=e^{-v}.
\]
The preceding uniform estimates imply convergence of \(\beta(T_i+v/2^{i-1})\) to \(B(v)\) in \(C^2\) on compact intervals, with error \(O_n(R^{-1})\). Its derivative with respect to \(s\) is \((1-2s)/(1+2s)^3\). Therefore \(B\) has a unique nondegenerate strict maximum at \(s=1/2\), equivalently \(v=\log2\), with \(B=9/8\). Nondegeneracy gives a unique nearby critical point in a fixed small window and negative second derivative for sufficiently large \(R\), by the implicit-function theorem (or continuity of the derivative and second derivative). Its location and value differ by \(O_n(R^{-1})\), proving the stated asymptotics.

**3. Separation and troughs.** Fixed-size neighborhoods of the \(T_i\) are disjoint for sufficiently large \(R\), because neighboring centers are \(\log R\) apart. For \(2\le i<n\), set \(U_i=(T_i+T_{i-1})/2\). The component indexed \(i-1\) dominates all others at \(U_i\): it lies halfway between its left and right adjacent transitions, each at distance \((\log R)/2\), and all other transitions are farther away. Hence \(\beta(U_i)\to1\). The order \(T_i<U_i<T_{i-1}\), together with bounded peak offsets, places these troughs between successive strict maxima. This proves the theorem.

## Verification
An accompanying standard-library Python program, `check.py`, verifies an explicit exact-rational three-reservoir example and numerical peak/trough limits for fixed component counts \(3\le n\le9\). For \(n=3\) and \(R=100\),
\[
Q(t)=e^{-t}+10^4e^{-2t}+10^8e^{-4t}.
\]
At the three times \(\log R\), \(\log R+\log(4/3)\), \(\log R+\log2\), the middle \(\beta\) value is strictly larger than both endpoints. The same holds at \(2\log R-\log2\), \(2\log R+\log2\), \(2\log R+\log4\). These intervals are disjoint. Existence of two strict interior local maxima follows by continuity and analyticity. The general arbitrary-\(n\) theorem, however, is proved analytically by the transition and nondegeneracy argument, not by finite tests.

Reproduce via `python3 check.py` using only the Python standard library.

## Relationship to prior work
Clark and colleagues' field-to-hillslope account (2008 online) and Harman, Sivapalan and Kumar (2009) explicitly motivate heterogeneous linear stores as an explanation of apparent nonlinear catchment recessions. Gao and colleagues (2017) treat **two** parallel linear stores and time-varying apparent recession slopes; this already covers the one-transition/two-reservoir case and is not claimed as new. Roques and colleagues (2022) analyze recession exponents for vertically compartmentalized hillslopes, including two-component algebra. The present contribution is the constructive all-\(n\) bound of at least \(n-1\) *separate*, asymptotically equally tall local exponent peaks, at explicit times, with asymptotically linear-looking troughs.

## Limitations
The result constructs a particular exponentially separated hierarchy of initial storages and fixed drainage rates. It does not assert that real catchments commonly attain this hierarchy, that peaks survive measurement noise or finite-window regression, or that exactly \(n-1\) peaks is an upper bound. The threshold \(R_n\) is existential and depends on fixed \(n\); there is no uniform-in-\(n\) convergence assertion. Historical priority for the multi-peak construction is provisional: a more general theorem on positive exponential mixtures could imply it; earlier modeling literature was compared, but not every potentially relevant full text was accessible.

## References
- Clark, M. P. et al. (2008 online). "Consistency between hydrological models and field observations: linking processes at the hillslope scale to hydrological responses at the watershed scale." DOI: 10.1002/hyp.7154.
- Harman, C. J., Sivapalan, M. and Kumar, P. (2009). "Power law catchment-scale recessions arising from heterogeneous linear small-scale dynamics." DOI: 10.1029/2008WR007392.
- Gao, M. et al. (2017). "Using Two Parallel Linear Reservoirs to Express Multiple Relations of Power-Law Recession Curves." DOI: 10.1061/(ASCE)HE.1943-5584.0001518.
- Roques, C. et al. (2022). "Recession discharge from compartmentalized bedrock hillslopes." DOI: 10.5194/hess-26-4391-2022.
