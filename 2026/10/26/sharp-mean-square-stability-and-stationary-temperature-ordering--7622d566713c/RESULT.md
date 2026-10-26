# Sharp mean-square stability and stationary-temperature ordering of two Poisson-midpoint selection laws

## Finding
For overdamped Poisson-midpoint integration of the scalar Ornstein–Uhlenbeck model, selecting exactly one random midpoint can have a strictly larger **mean-square stability interval** and a strictly smaller **stationary covariance bias** than the independent Bernoulli selection used in the Poisson variant. These are exact sharp finite-step statements, not asymptotic error bounds.

Fix any integer \(K\ge2\), any \(\lambda>0\), and macrostep \(h>0\). Set \(s=\lambda h\) and
\[
c=\frac{K-1}{2K},\qquad d_{\mathrm S}=\frac{K^2-1}{12K^2},\qquad d_{\mathrm B}=\frac{(K-1)^2(2K-1)}{6K^3}.
\]
Write S for one uniformly selected midpoint and B for independent midpoint indicators with probability \(1/K\). Their exact mean-square amplification factors are
\[
m_j(s)=\left(1-s+cs^2\right)^2+d_js^4,\quad j\in\{\mathrm S,\mathrm B\}.
\]
Their one-step additive noise second moments are
\[
n_{\mathrm S}(s)=\frac{2s}{\lambda}\bigl(1-2cs+cs^2\bigr),\qquad
n_{\mathrm B}(s)=n_{\mathrm S}(s)+\frac{2s^3(K-1)(K-2)}{3\lambda K^2}.
\]
For either law, define its **sharp mean-square stability threshold** \(s_j\) to be the unique positive zero of
\[
Q_j(s)=2-(1+2c)s+2cs^2-(c^2+d_j)s^3.
\]
The second moment converges to the finite stationary value \(V_j=n_j/(1-m_j)\) precisely for \(0<s<s_j\). At or above \(s_j\), the strictly positive injected noise precludes any stationary law of finite second moment. If \(K=2\), the two laws have identical one-step distribution. If \(K\ge3\), then
\[
0<s_{\mathrm B}<s_{\mathrm S};\qquad
\frac1\lambda<V_{\mathrm S}(s)<V_{\mathrm B}(s)\quad(0<s<s_{\mathrm B}).
\]
Thus the single-choice law has strictly smaller absolute stationary variance bias relative to the continuous-time Gibbs value \(1/\lambda\) whenever both are stable; it alone remains second-moment stable on \([s_{\mathrm B},s_{\mathrm S})\).

## Assumptions and scope
The target is the scalar stochastic differential equation \(dX_t=-\lambda X_t\,dt+\sqrt2\,dB_t\) with \(\lambda>0\). Each macrostep independently redraws its midpoint indicators and \(K\) independent standard Gaussian micro-increments. Both sampling laws use exactly the original, **theoretically analyzed Section 2.2 interpolation** with midpoint indices \(0,\ldots,K-1\); the predictor at index \(i\) depends on the first \(i\) Gaussian increments (not on increment \(i\) itself). Selection S chooses one index uniformly from all \(K\); selection B chooses each index independently with probability \(1/K\). This is distinct from later shifted-index experimental variants. The same \(K\) and macrostep \(h\) are compared, and each scheme has one expected selected index per macrostep. Second-moment stability means convergence of \(\mathbb E[X_n^2]\) for every square-integrable initialization to the finite invariant second moment; it is not pathwise stability and does not assert the stationary law is Gaussian.

## Proof
Let \(H_i\in\{0,1\}\) denote indicator \(i\), and let \(Z_0,\dots,Z_{K-1}\) be independent standard Gaussians. The published interpolation and unrolled update give the random affine recursion
\[
X_{n+1}=A_HX_n+\xi_H,\qquad
A_H=1-s+\frac{s^2}{K}\sum_{i=0}^{K-1}iH_i,
\]
\[
\xi_H=\sqrt{\frac{2s}{\lambda K}}\sum_{j=0}^{K-1}\left(1-s\sum_{i=j+1}^{K-1}H_i\right)Z_j.
\]
The sum over \(i>j\) follows because a midpoint at index \(i\) uses precisely earlier increments \(Z_0,\dots,Z_{i-1}\). In both laws, \(\mathbb E[H_i]=1/K\), so \(\mathbb E[A_H]=1-s+cs^2\). For S, \(\sum iH_i\) is uniform on \(\{0,\ldots,K-1\}\); its variance is \((K^2-1)/12\). For B, the independent indicator variance gives \(\operatorname{Var}(\sum iH_i)=(1/K)(1-1/K)\sum i^2\). Division by \(K^2\) proves the displayed \(d_j\) and \(m_j=\mathbb E[A_H^2]\).

Conditional on \(H\), independent Gaussian increments show
\[
\mathbb E[\xi_H^2\mid H]=\frac{2s}{\lambda K}\sum_{j=0}^{K-1}\left(1-s\sum_{i=j+1}^{K-1}H_i\right)^2.
\]
For S, each inner sum is Bernoulli with mean \((K-j-1)/K\), so its square has the same expectation. For B, the inner sum has \(K-j-1\) independent Bernoulli summands: its second moment exceeds the single-choice value by \((K-j-1)(K-j-2)/K^2\). Summing these identities gives \(n_S\), \(n_B\), and their displayed difference. Direct subtraction also gives
\[
m_{\mathrm B}-m_{\mathrm S}=\frac{(K-1)(K-2)(3K-1)}{12K^3}s^4.
\]
The fresh noise has conditional mean zero, so \(\mathbb E[X_{n+1}^2]=m_j\mathbb E[X_n^2]+n_j\), and \(n_j>0\) for \(s>0\). For either law, \(1-m_j=sQ_j(s)\). Because \(c\ge1/4\) and \(d_j\ge0\),
\[
Q_j'(s)=-(1+2c)+4cs-3(c^2+d_j)s^2\le\frac13-2c<0.
\]
As \(Q_j(0)=2\) and \(Q_j(s)\to-\infty\), each has exactly one positive zero. The scalar second-moment recurrence converges iff \(m_j<1\). If so, the random affine iteration contracts in mean square, giving a unique finite-second-moment invariant law and \(V_j=n_j/(1-m_j)\). If not, any purported stationary law with finite second moment would contradict \(V=m_jV+n_j\) and \(n_j>0\). For \(K\ge3\), the strict positive multiplier difference implies \(s_B<s_S\). On their shared stable range, \(n_B\ge n_S>0\) and \(1-m_B<1-m_S\), whence \(V_B>V_S\). When \(K=2\), the only correction-sensitive midpoint is index \(1\); both laws give its indicator the same Bernoulli \(1/2\) law and the index-zero correction vanishes, proving equality in law.

Finally, the one-choice stationary variance always exceeds the correct continuous-time variance, since
\[
n_{\mathrm S}-\frac{1-m_{\mathrm S}}\lambda
=\frac{1}{\lambda}\left[\frac{s^2}{K}+(c^2+d_{\mathrm S})s^4\right]>0.
\]
Dividing by \(1-m_S>0\) establishes \(V_S>1/\lambda\) and, by strict ordering, \(V_B>1/\lambda\) throughout their common stable range.

## Verification
Run `python verify.py` with Python 3 and SymPy available. The standalone program checks symbolic amplification and noise-moment identities for arbitrary symbolic \(K\) and checks the full random-indicator and Gaussian-coefficient formulas by exact enumeration for \(2\le K\le7\). It also checks the monotonicity upper bound and rational root brackets. Its enumerations are checks, not proofs of the universal statements, which follow from the displayed sums and derivative argument.

For \(K=3\), numerical roots are \(s_B\approx1.658143759865\) and \(s_S\approx1.873254794863\). The exact values are defined by the corresponding cubic equations; approximations are illustrative only.

## Relationship to prior work
Kandasamy and Nagaraj [1] introduce the two selection laws and explicitly observe that selection without replacement has lower variance error. This qualitative variance claim and the sampling algorithms themselves are **not new**. The present result isolates a different, quantitative statement: all finite batch sizes, exact second-moment recurrences, unique sharp stability boundaries, their strict ordering, and exact stationary-temperature overdispersion comparison. Srinivasan and Nagaraj [2] analyze Poisson-midpoint sampling complexity for strongly log-concave targets, without giving the two-law all-step stationary stability classification established here. Existing variance and perturbation methods could potentially imply parts of the calculation; no assertion of exclusive priority is made.

## Limitations
The result is exact only for scalar additive-noise OU dynamics with independent fresh batches and the cited theoretical midpoint convention. It does not prove analogous dimension-free thresholds for noncommuting Hessians, nonlinear drifts, or underdamped dynamics. The invariant law of a scheme is generally not Gaussian. The lower stationary variance of S does not by itself imply improved total variation, Wasserstein, mixing-time, or finite-horizon error, although in this scalar model both stationary variances exceed the exact target variance.

## References
[1] S. Kandasamy and D. Nagaraj, *The Poisson Midpoint Method for Langevin Dynamics: Provably Efficient Discretization for Diffusion Models*, arXiv:2405.17068 (first public submission 2024-05-27); NeurIPS 2024, DOI 10.52202/079017-2109. In particular Section 2.2 and Appendix A.6.

[2] R. Srinivasan and D. Nagaraj, *Poisson Midpoint Method for Log Concave Sampling: Beyond the Strong Error Lower Bounds*, arXiv:2506.07614 (2025), Sections 2.2 and 3.
