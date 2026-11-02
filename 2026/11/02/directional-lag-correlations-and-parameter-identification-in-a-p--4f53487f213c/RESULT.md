# Directional lag correlations and parameter identification in a partially reset Brownian probe–bath pair

## Finding

For the exactly specified two-coordinate viscoelastic Langevin model below, resetting only the probe produces a **strictly negative, single-peaked directional lag-covariance difference**. For all positive probe-reset rates \(r\), bath-friction ratios \(\gamma\), and lags \(t>0\), define
\[
\Delta(t)=\mathbb E[X_tQ_0]-\mathbb E[Q_tX_0]
\]
in stationarity. Put \(s=r+1+\gamma^{-1}\), \(p=r/\gamma\), and \(\lambda_\pm=(-s\pm\sqrt{s^2-4p})/2\). Then \(\lambda_-<\lambda_+<0\) and
\[
\boxed{\displaystyle
\Delta(t)=-\frac{2}{\gamma(r+2)+1}\,
\frac{e^{\lambda_+t}-e^{\lambda_-t}}{\lambda_+-\lambda_-}.}
\]
Thus \(\Delta(t)<0\) for every \(t>0\), tending to zero at both endpoints. Its magnitude has exactly one maximum, at
\[
\boxed{\displaystyle t_* = \frac{\log(\lambda_-/\lambda_+)}{\lambda_+-\lambda_-}>0.}
\]
The first two **right derivatives** \(d_1=\Delta'(0+)\), \(d_2=\Delta''(0+)\) determine both unknown positive model parameters uniquely: with \(S=-d_2/d_1\),
\[
\boxed{\displaystyle \gamma^{-1}=-\frac{S+1}{2}d_1,\qquad r=S-1-\gamma^{-1}.}
\]
There is also a probe-only version. Writing \(H(t)=\mathbb E[X_tX_0]\) and \(a=H(0)\), the calibrated stationary probe variance and initial right correlation slope determine the same parameters uniquely:
\[
\boxed{\displaystyle r=-\frac{2[H'(0+)+1]}{a},\qquad
\gamma=\frac{2-ra}{ra(r+2)-2(r+1)}.}
\]
All identities hold for every \(r,\gamma>0\), without a long-time, small-noise, or large-memory approximation. The bath coordinate must be observed for the first inverse formula but not the second. Thermal variance and probe relaxation time must be calibrated as specified below.

## Assumptions and scope

Let \(W,B\) be independent standard Brownian motions and \(N\) an independent homogeneous Poisson process with intensity \(r>0\). Between its jump times the real pair \((X,Q)\) satisfies, in the dimensionless units of the reference model,
\[
 dX=(Q-X)\,dt+\sqrt2\,dW,\qquad
 dQ=(X-Q)\gamma^{-1}\,dt+\sqrt{2/\gamma}\,dB,
\]
with fixed \(\gamma>0\). At each Poisson jump, \((X,Q)\mapsto(0,Q)\); the bath is **not** reset. The time unit is the bare probe relaxation time and the squared length unit is the thermal variance \(k_BT/k\). In particular both Langevin noises have known amplitudes; without that calibration the inverse identities require an additional unknown scale. Expectations are with respect to the unique stationary law and the stationary process at nonnegative lags. The theorem is a statement about stationary second-order temporal statistics, not equality of complete time-reversed path measures.

## Proof

**Existence and uniqueness.** For \(V(x,q)=x^2+\gamma q^2\), the full diffusion-and-jump generator satisfies
\[
 LV=4-2(x-q)^2-rx^2\le4-cV
\]
for some \(c=c(r,\gamma)>0\), since \(2(x-q)^2+rx^2\) is strictly positive definite. Nonexplosion, tightness of empirical distributions and the Feller property yield a stationary probability law with finite second moments. Couple two solutions with the same Brownian noises and the same Poisson jumps. Their difference \((U,R)\) has \(d(U^2+\gamma R^2)/dt=-2(U-R)^2\) between resets and loses \(U^2\) at a reset. Consequently \(d\mathbb E(U^2+\gamma R^2)/dt\le-c\mathbb E(U^2+\gamma R^2)\). The contraction proves stationary uniqueness (and mean-square convergence for finite-second-moment starts). Symmetry gives zero stationary means.

**Stationary covariance.** Write \(a=\mathbb E X^2\), \(b=\mathbb E XQ\), \(c_0=\mathbb E Q^2\). Applying the exact jump-diffusion generator to the three quadratic monomials gives
\[
 0=-(2+r)a+2b+2,\qquad
 0=c_0-(1+r+\gamma^{-1})b+\gamma^{-1}a,\qquad
 0=2\gamma^{-1}(b-c_0+1).
\]
Solving yields, with \(L=\gamma(r+2)+1\),
\[
 a=\frac{2[\gamma(r+1)+1]}{rL},\quad
 b=\frac{\gamma(r+2)+2}{rL},\quad
 c_0=b+1,\quad
 a-b=\frac{\gamma}{L}.
\]
These static equations and their elementary consequences are not asserted as previously unknown; they are used to establish the new lagged and inverse statements.

**Lagged covariance.** Conditional means solve the exact linear drift system \(m'(t)=Am(t)\), because the generator acts on linear observables as
\[
 A=\begin{pmatrix}-(1+r)&1\\\gamma^{-1}&-\gamma^{-1}\end{pmatrix}.
\]
Writing \(C=\begin{pmatrix}a&b\\b&c_0\end{pmatrix}\), the full stationary forward lag covariance matrix is \(K(t)=e^{At}C\) for \(t\ge0\). The characteristic polynomial of \(A\) is \(\lambda^2+s\lambda+p\). Its discriminant \((r+1-\gamma^{-1})^2+4\gamma^{-1}\) is strictly positive, and both roots are negative because \(s,p>0\). By the two-dimensional matrix exponential identity,
\[
 e^{At}=\frac{e^{\lambda_+t}-e^{\lambda_-t}}{\lambda_+-\lambda_-}A
 +\frac{\lambda_+e^{\lambda_-t}-\lambda_-e^{\lambda_+t}}{\lambda_+-\lambda_-}I.
\]
The identity term is symmetric after multiplication by \(C\), and the off-diagonal difference of \(AC\) is
\[
 (AC)_{12}-(AC)_{21}=c_0-(1+r)b-\frac{a-b}{\gamma}=-\frac2L.
\]
This proves the boxed formula and the strict sign. The positive factor \((e^{\lambda_+t}-e^{\lambda_-t})/(\lambda_+-\lambda_-)\) rises from zero, then decays to zero. Its derivative has precisely one zero, solving \(\lambda_+e^{\lambda_+t}=\lambda_-e^{\lambda_-t}\), giving the displayed \(t_*\). This also proves uniqueness of the peak and no finite-lag sign reversal.

**Inverse maps.** The scalar lag factor \(f(t)\) in the formula satisfies \(f(0)=0\), \(f'(0+)=1\), \(f''(0+)=-s\). Hence \(d_1=-2/L\) and \(d_2=-s d_1\). Writing \(u=\gamma^{-1}\), one has \(L=(s+1)/u\); therefore \(u=-(s+1)d_1/2\) and \(r=s-1-u\). These recover the unique original positive parameters, not merely an unordered pair of relaxation eigenvalues.

Finally \(H(0)=a>0\) and \(H'(0+)=(AC)_{11}=-(1+r)a+b\). Using \((2+r)a=2b+2\) reduces this to \(H'(0+)=-1-ra/2\), giving \(r\). Solving the formula for \(a\) for \(\gamma\) gives the second boxed expression. Its numerator and denominator are strictly positive for admissible \(r,\gamma>0\), because
\[
 \frac{2(r+1)}{r(r+2)}<a<\frac2r.
\]
The strict inequalities also prove injectivity and delimit the physically admissible inverse-data domain.

## Verification

The accompanying standard-library Python file `verify.py` checks independent exact-rational stationary generator equations and compares matrix-exponential evaluations against the displayed lag formula for a grid of positive parameters and times. It checks both inverse maps and the unique-peak condition. The script is a finite regression/consistency test, not an exhaustive numerical proof or a substitute for the arguments above. Run it with `python verify.py` from the directory containing this document and the script.

## Relationship to prior work

Santra and Das, *Resetting in a viscoelastic bath: the bath remembers* (arXiv:2603.17027, first posted 17 March 2026; New J. Phys. 28, 074601), introduced exactly this partially reset probe–bath dynamics and derived stationary and time-dependent **equal-time** moments and distributional limiting forms. Their model and moment-generator equations are the starting point here. The distinct claim established above concerns **stationary cross-time ordering** and an exact inverse characterization from lag derivatives (including a probe-only alternative). No claim of priority is made for the Markov-semigroup covariance identity itself or the static moments.

A related non-equilibrium coupled-bath tracer with selective resetting was also studied by Goswami (arXiv:2412.19564, 2024/2025). The abstract emphasizes relaxation and first-passage properties but its full text could not be examined here, so possible overlap with temporal correlations remains an explicit priority risk.

Biswas, Dubbeldam, Sandev and Pal, *A resetting particle embedded in a viscoelastic bath* (arXiv:2412.09260; Chaos 35, 031102, 2025), derived two-time correlations using a generalized Langevin renewal framework. Their probe autocorrelation under a renewed viscoelastic dynamics does not, from the examined equations and model, establish the direction-dependent two-coordinate cross-lag asymmetry of an auxiliary bath retained across probe resets, nor the two-jet inverse formulas. Standard finite-dimensional linear Markov-semigroup techniques do apply here; the contribution is the explicit non-reversible waveform and parameter-identification mechanism for the specified non-renewing reset model.

## Limitations

The result assumes the dimensionless linear single-bath-coordinate model, known thermal scale, independent equilibrium Langevin noise, stationary initial distribution, instantaneous full probe resets, a constant independent Poisson rate, and \(r,\gamma>0\). No statement is made about nonlinear baths, multiple memory modes, non-Poisson resets, finite sampling error, or full-path entropy production. While stationary existence and the second-order formulas are rigorous, the calculations alone do not establish literature-wide priority; independent validation has not occurred. If the bath coordinate is inaccessible, only the probe-only reconstruction is directly usable; its derivative estimates may be noise-sensitive in finite data.

## References

1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027 (first public version 17 March 2026); *New Journal of Physics* **28**, 074601 (2026), DOI:10.1088/1367-2630/ae868c.
2. K. Goswami, *Stochastic resetting in a nonequilibrium environment*, arXiv:2412.19564 (2024), *Physical Review E* **111**, 014150 (2025), DOI:10.1103/PhysRevE.111.014150.
3. A. Biswas, J. L. A. Dubbeldam, T. Sandev and A. Pal, *A resetting particle embedded in a viscoelastic bath*, arXiv:2412.09260 (2024); *Chaos* **35**, 031102 (2025), DOI:10.1063/5.0253019.
