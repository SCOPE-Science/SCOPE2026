# Minimum mean step for one-step second-moment isotropization under random-time implicit midpoint

## Finding

Fix a frequency \(\omega>0\). Consider the harmonic oscillator
\[
\dot q=p,\qquad \dot p=-\omega^2q,
\]
and write its energy-normalized state as \(u=(\omega q,p)^\top\). At each step apply the implicit midpoint rule using an independent, identically distributed random duration \(H\ge0\), independent of the initial state, with \(\mathbb EH<\infty\). For \(u_k\) after \(k\) steps, write \(S_k=\mathbb E[u_ku_k^\top]\). A second-moment matrix is **isotropic** if it is a scalar multiple of the identity. For centered initial ensembles, \(S_k\) is their usual covariance matrix; for deterministic initial states it is an *uncentered* second moment.

The following four assertions form one sharp characterization of one-step second-moment isotropization.

1. The property \(S_1=\tfrac12\operatorname{tr}(S_0)I_2\) for **every** square-integrable initial ensemble independent of \(H\) holds exactly when
\[
\mathbb E\left[\left(\frac{1+i\omega H/2}{1-i\omega H/2}\right)^2\right]=0.
\]
For every initially anisotropic \(S_0\), this condition is also necessary. If satisfied, it persists as \(S_k=\tfrac12\operatorname{tr}(S_0)I_2\) for every integer \(k\ge1\).

2. Every such isotropizing nonnegative-step law has the **sharp mean-duration lower bound**
\[
\boxed{\mathbb EH\ge\omega^{-1}.}
\]
Equality is attained uniquely by the equiprobable two-point law \(\mathbb P(H=0)=\mathbb P(H=2/\omega)=1/2\). Thus, if strict positivity \(H>0\) is required, this minimum is an unattained infimum.

3. Conversely, for **every** prescribed mean \(\mu>1/\omega\), a law supported at two strictly positive durations with equal probabilities achieves exact one-step isotropization. Explicitly put
\[
m=\omega\mu,\qquad s=\frac{m+2-\sqrt{m^2+8}}2,\qquad r=\frac{1+s}{1-s}.
\]
Then \(0<s<1<r\) and the equiprobable law \(H\in\{2s/\omega,2r/\omega\}\) has mean \(\mu\) and isotropizes. For example, when \(\mu=2/\omega\), its values are \(2(2-\sqrt3)/\omega\) and \(2\sqrt3/\omega\).

4. If steps are also constrained to \(0\le H\le h_{\max}\), **some** isotropizing law exists exactly when \(h_{\max}\ge2/\omega\). Under the stricter constraint \(0<H\le h_{\max}\), one exists exactly when \(h_{\max}>2/\omega\).

Every individual implicit-midpoint update preserves \(\|u\|_2^2\) exactly. The result is about ensemble phase mixing at potentially coarse steps, not fidelity to the exact state at the randomized accumulated physical time.

## Assumptions and scope

All vector spaces and parameters are real except the auxiliary complex phase. The oscillator has frequency \(\omega>0\), and all timesteps are scalar, exogenous and independent of the state. The iid assumption is needed only for the all-iterations formula; the one-step lower bound applies to any law of one nonnegative \(H\) with finite mean. The initial ensemble has finite second moment and is independent of the step sequence. A centered initial law with any non-isotropic covariance, such as an equiprobable pair of opposite nonzero states, tests the stated universal necessity. Allowing \(H=0\) means the identity midpoint update; the strict-positive case is separately characterized.

The natural time metric here is \(\mathbb EH\), the *mean elapsed physical time represented by one update*, rather than the number of function evaluations or the mean trajectory approximation error. The theorem supplies a sharp dephasing/energy-shell sampling benchmark, not a general-purpose timestep recommendation.

## Proof

**Rotation reduction.** Set \(t=\omega H/2\ge0\) and \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\). Since \(u'=\omega Ju\), implicit midpoint is exactly
\[
M(t)=(I_2-tJ)^{-1}(I_2+tJ)
=\frac1{1+t^2}\begin{pmatrix}1-t^2&2t\\-2t&1-t^2\end{pmatrix}.
\]
Thus \(M(t)^\top M(t)=I_2\), so the oscillator energy \(\tfrac12\|u\|_2^2\) is preserved on every path. Identifying \(u\) with \(z=u_1+iu_2\), the update is multiplication by \(\exp[-i\theta(t)]\), where \(\theta(t)=2\arctan t\in[0,\pi)\). Define
\[
Z(t)=\exp[2i\theta(t)]=\left(\frac{1+it}{1-it}\right)^2.
\]
Then \(z_1^2=\overline{Z(t)}z_0^2\). The traceless part of \(S_k\) is encoded by
\[
\mathbb E z_k^2=(S_k)_{11}-(S_k)_{22}+2i(S_k)_{12}.
\]
Consequently, with \(\gamma=\mathbb E Z(\omega H/2)\), independence yields \(\mathbb E z_k^2=\overline\gamma^{\,k}\mathbb E z_0^2\), whereas energy preservation fixes \(\operatorname{tr}S_k=\operatorname{tr}S_0\). This proves the exact isotropy criterion, its necessity for anisotropic \(S_0\), and persistence for \(k\ge1\). In particular, for a centered initial distribution the same statement concerns centered covariance, because the linear independent updates preserve a zero ensemble mean.

**A global dual polynomial certificate.** Rationalize the second harmonic:
\[
\operatorname{Re}Z(t)=\frac{1-6t^2+t^4}{(1+t^2)^2},\qquad
\operatorname{Im}Z(t)=\frac{4t(1-t^2)}{(1+t^2)^2}.
\]
Direct algebra gives the exact identity
\[
\boxed{t-\frac{1-\operatorname{Re}Z(t)-\operatorname{Im}Z(t)}2
=\frac{t(t-1)^2(t^2+2t+3)}{(1+t^2)^2}\ge0\quad(t\ge0).}
\]
If \(\mathbb EZ(t)=0\), integration of this identity (justified by finite \(\mathbb Et\)) gives
\[
\mathbb Et-\tfrac12
=\mathbb E\left[\frac{t(t-1)^2(t^2+2t+3)}{(1+t^2)^2}\right]\ge0.
\]
Since \(\mathbb EH=2\mathbb Et/\omega\), the lower bound follows. The nonnegative integrand vanishes exactly for \(t\in\{0,1\}\). Equality therefore forces support on these two points; the condition \(\mathbb EZ(t)=0\), together with \(Z(0)=1\) and \(Z(1)=-1\), forces both masses to be \(1/2\). This proves uniqueness of the extremizer and shows why equality cannot occur when \(H>0\) almost surely.

**All supercritical means.** For \(m=\omega\mu>1\), the displayed \(s\) is the smaller root of \(s^2-(m+2)s+(m-1)=0\). It satisfies \(0<s<1\). Setting \(r=(1+s)/(1-s)>1\), the quadratic identity gives \(s+r=m\). Furthermore
\[
\frac{r-s}{1+rs}=1,
\]
so the tangent subtraction formula shows \(\theta(r)-\theta(s)=\pi/2\). Thus \(Z(r)=-Z(s)\), and the equal-mass law has \(\mathbb EZ=0\) and mean physical duration \((s+r)/\omega=\mu\). Taking \(\mu\downarrow1/\omega\) yields the lower-bound endpoint law.

**Maximum-step frontier.** As \(t\) varies between \(0\) and \(\omega h_{\max}/2\), the unit complex value \(Z(t)=e^{4i\arctan t}\) traces an arc. If \(h_{\max}<2/\omega\), the arc has length strictly less than \(\pi\), so it lies in a strictly open semicircle and no average of its points can be zero. At equality the origin lies in the convex hull only through the two arc endpoints, which correspond to \(H=0\) and \(H=2/\omega\). Above the bound the previously exhibited endpoint law is admissible, and for a strict-positive cap above the bound a sufficiently small positive \(s\) has \(2r/\omega<h_{\max}\). These facts prove both cap thresholds.

## Verification

Run `python -m pip install -r requirements.txt` followed by `python verify.py`. The standalone symbolic checks reconstruct the midpoint matrix and its orthogonality, the two rational harmonic components, the globally nonnegative dual-certificate identity, the exact quarter-turn relation between the two constructed duration values, and isotropization for sample positive-semidefinite and symmetric second-moment matrices. Exact boundary and several positive finite-mean examples are checked separately. These finite and symbolic computations support the displayed algebra; the universal statements about arbitrary probability laws come from the integrated nonnegative identity, arc geometry and the analytical proof above.

## Relationship to prior work

Abdulle and Garegnani introduced random-time-step Runge--Kutta methods and proved that geometric integrators can retain exact first integrals, including the quadratic-invariant preservation of implicit midpoint. Their convergence/error results primarily concern vanishing timesteps and their geometric examples concern pathwise invariant preservation. The additional result proved here is a *sharp inverse design problem*: among all nonnegative timestep distributions, characterize precisely when a fixed-frequency oscillator can have all traceless second moments annihilated in one update, and find the minimum possible mean step and sharp support frontier.

Christiansen, Errica and Alesiani discuss timestep jitter for harmonic-oscillator Hamiltonian Monte Carlo, but use velocity Verlet, trajectory acceptance and autocorrelation-based objectives rather than this fixed-energy midpoint second-harmonic cancellation criterion. Published harmonic Langevin integrator analyses concern stochastic forcing and invariant-measure bias, not the energy-preserving exogenous-duration Cayley rotation considered here. Common rotation/Fourier facts and midpoint energy preservation are established tools and are not claimed as new.

## Limitations

Only the planar linear oscillator and one-step uncentered second moments (or centered covariance for zero-mean initial ensembles) are classified. The result does **not** make the state distribution uniform on its energy circle after one step: the optimal law has only two support points and cancels only the second angular harmonic. It does not imply convergence of a computed trajectory to the exact flow at a prescribed physical time, nor any optimum in numerical truncation error, CPU cost, nonlinear Hamiltonian dynamics, or arbitrary-frequency coupled oscillators. At the sharp mean endpoint the admissible law includes a zero-duration step; strictly positive laws attain exactly all larger means, not the endpoint. The theoretical claim is independent of numerical finite-sample diagnostics. No independent validation has been performed.

## References

1. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (first public version 2018-01-04), especially Sections 2, 6 and 9.5. https://arxiv.org/abs/1801.01340
2. H. Christiansen, F. Errica and F. Alesiani, *Self-Tuning Hamiltonian Monte Carlo for Accelerated Sampling*, arXiv:2309.13593 (2023), especially Sections III.3 and IV.1. https://arxiv.org/abs/2309.13593
3. E. Hairer, C. Lubich and G. Wanner, *Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations*, Springer, 2nd ed. (2006), Chapters IV and VI (standard midpoint and quadratic-invariant background).
