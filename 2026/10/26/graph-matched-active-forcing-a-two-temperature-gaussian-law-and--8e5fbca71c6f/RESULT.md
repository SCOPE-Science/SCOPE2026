# Graph-matched active forcing: a two-temperature Gaussian law and simultaneous velocity-correlation reversal

## Finding

**Theorem (matched active noise and collective velocity domains).** Let \(G\) be any finite connected undirected weighted graph with \(n\geq3\) vertices and a real symmetric graph Laplacian \(L\). Consider inertial harmonic motion with a finite-persistence, spatially correlated Gaussian active force as specified below. Among strictly positive definite active-force covariance matrices that commute with \(L\), the unique covariance *shape* making all stationary particle velocities independent and identically distributed is
\[
\Sigma=c\bigl[(1+\gamma\tau)I+\tau^2 L\bigr],\qquad c>0.
\]
Its stationary position–velocity marginal, with the translation mode removed from position, is exactly a product of two Gaussian Gibbs distributions with different temperatures:
\[
T_{\mathrm{kin}}=T+\frac{c\tau}{m\gamma},\qquad
T_{\mathrm{conf}}=T+\frac{(1+\gamma\tau)c\tau}{m\gamma}>T_{\mathrm{kin}}.
\]
In particular, the active force still injects the strictly positive mean instantaneous power \(J_i=\mathbb E[v_i f_i]=c\tau/m\) at each vertex, and
\[
T_{\mathrm{conf}}-T_{\mathrm{kin}}=\tau J_i.
\]
Thus independence of *equal-time* velocities does not indicate vanishing activity or process-level equilibrium.

On every periodic ring with \(n\geq3\), let the two nearest-neighbor active-force covariances be \(\varepsilon\sigma^2\), the diagonal variances be \(\sigma^2>0\), and assume \(-1/2<\varepsilon<1/2\). With nearest-neighbor squared-frequency coupling \(w>0\), all pairs of *different* sites simultaneously reverse the sign of their stationary velocity covariance at the single admissible threshold
\[
\varepsilon_*=-\frac{\tau^2w}{1+\gamma\tau+2\tau^2w}.
\]
For every \(i\ne j\), the covariance is negative for \(\varepsilon<\varepsilon_*\), zero at equality, and positive for \(\varepsilon>\varepsilon_*\), regardless of ring size or separation. The matched graph covariance is precisely the ring covariance at this threshold.

## Assumptions and scope

All parameters \(m,\gamma,\tau,c\) are strictly positive; the thermal temperature \(T\) may be zero. The graph is connected, symmetric, and has nonnegative edge weights. Its Laplacian is positive semidefinite with one zero eigenvalue. Independent \(n\)-dimensional Brownian motions \(W\) and \(B\) drive the Itô system
\[
\begin{aligned}
  du_t&=v_t\,dt,\\
  dv_t&=(-\gamma v_t-Lu_t+f_t/m)\,dt+\sqrt{2\gamma T/m}\,dW_t,\\
  df_t&=-f_t\,dt/\tau+\sqrt{2/\tau}\,\Sigma^{1/2}dB_t.
\end{aligned}
\]
The active force therefore has stationary covariance \(\mathbb E[f_t f_s^\top]=\Sigma e^{-|t-s|/\tau}\). It is independent of thermal noise. Write \(P=I-\mathbf1\mathbf1^\top/n\), and define the centered position \(y=Pu\). The position center of mass need not have a stationary distribution and is never included in the stationary assertion. The joint process \((y,v,f)\) admits a unique stationary Gaussian distribution. The *rigidity/necessity* assertion quantifies only over symmetric positive definite \(\Sigma\) **commuting with \(L\)**; no uniqueness statement is made among noncommuting spatial noise covariances.

The ring uses \(S\), the cyclic shift matrix; \(L=w(2I-S-S^\top)\) and \(\Sigma=\sigma^2[I+\varepsilon(S+S^\top)]\). The interval \(-1/2<\varepsilon<1/2\) is a convenient strict positive-definite regime for every ring size. For \(n=3\), each pair consists of one ring edge (not a duplicated physical edge).

## Proof

**Existence and mode covariances.** The damping \(\gamma>0\) makes every nonzero Laplacian oscillator mode stable. The translation-mode velocity is a stable damped degree of freedom driven by a stable Ornstein–Uhlenbeck force. Eliminating only the translation-mode *position* gives an exponentially stable finite-dimensional linear Gaussian process, hence its unique stationary law. Because \(\Sigma\) and \(L\) are symmetric and commute, choose an orthonormal simultaneous eigenbasis, with Laplacian eigenvalue \(\lambda\geq0\) and force variance \(s>0\). Let \(D_\lambda=1+\gamma\tau+\tau^2\lambda\).

For each mode write \(q\) for position (when \(\lambda>0\)), \(v\) for velocity and \(f\) for active force. Stationarity of the cross-moments gives
\[
\mathbb E[qf]=\tau\mathbb E[vf],\qquad
\mathbb E[vf]=\frac{s\tau}{mD_\lambda}.
\]
For nonzero modes, stationarity of \(q^2\) gives \(\mathbb E[qv]=0\); kinetic balance gives the same velocity variance for zero and nonzero modes. Therefore
\[
\mathbb E[v^2]=\frac{T}{m}+\frac{s\tau}{m^2\gamma D_\lambda},\qquad
\mathbb E[q^2]=\frac{1}{\lambda}\left[\frac{T}{m}+\frac{(1+\gamma\tau)s\tau}{m^2\gamma D_\lambda}\right]\quad(\lambda>0).
\]
For every pair of distinct simultaneously diagonalized modes, cross-covariances vanish by uniqueness of the stable stationary solution. In matrix form,
\[
\operatorname{Cov}(v)=\frac{T}{m}I+\frac{\tau}{m^2\gamma}\,\Sigma\bigl[(1+\gamma\tau)I+\tau^2L\bigr]^{-1}.
\]
The centered displacement–velocity cross-covariance is zero. All claims here concern exactly the equal-time stationary covariance.

**Rigidity and two temperatures.** Jointly Gaussian particle velocities are independent and identically distributed exactly when their covariance is a scalar multiple of \(I\). Because \(\Sigma\) is positive definite, the active part of the displayed matrix has positive eigenvalues. It is a scalar matrix if and only if \(\Sigma[(1+\gamma\tau)I+\tau^2L]^{-1}=cI\) for some \(c>0\), proving the asserted unique covariance shape. At that choice, every modal velocity variance is \(T_{\mathrm{kin}}/m\), whereas every nonzero modal position variance is \(T_{\mathrm{conf}}/(m\lambda)\). The joint Gaussian law has zero displacement–velocity cross-covariance, so it factorizes as
\[
\mathcal P(dy,dv)=Z^{-1}\exp\!\left(-\frac{m\|v\|^2}{2T_{\mathrm{kin}}}-\frac{m\langle y,Ly\rangle}{2T_{\mathrm{conf}}}\right)dy_{\mathbf1^\perp}\,dv,
\]
where \(dy_{\mathbf1^\perp}\) is Lebesgue measure on the centered-position subspace. Finally, modal stationarity gave \(\mathbb E[vf]=s\tau/(mD_\lambda)\); matching makes this equal to \(c\tau/m\) in every mode. Orthogonality then gives \(J_i=\mathbb E[v_if_i]=c\tau/m\) for every original vertex. Subtracting the two displayed temperatures proves the power–temperature identity. Positive definiteness of the matched force follows from positivity of \(1+\gamma\tau+\tau^2\lambda\) for all modes; this covariance can be realized by independent vertex forces plus independent dipole forces along graph edges.

**Ring sign theorem.** Write \(A=S+S^\top\), \(a=1+\gamma\tau+2\tau^2w\), and \(b=\tau^2w\); then the response matrix is \(D=aI-bA\) with \(a>2b>0\). Let \(G=D^{-1}\). The Neumann expansion
\[
G=\frac1a\sum_{k=0}^{\infty}\left(\frac ba A\right)^k
\]
converges, is entrywise nonnegative, and has \(G_{ij}>0\) for every pair \(i,j\) because the ring is connected. The active part of the velocity covariance is
\[
\frac{\sigma^2\tau}{m^2\gamma}(I+\varepsilon A)G.
\]
The identity \(AG=(aG-I)/b\) shows that for distinct vertices
\[
\operatorname{Cov}(v_i,v_j)=\frac{\sigma^2\tau}{m^2\gamma}
\left(1+\frac{a\varepsilon}{b}\right)G_{ij},\qquad i\ne j.
\]
Every factor besides the parenthesis is strictly positive, so *every off-diagonal entry* has the claimed sign simultaneously. Its sole zero is \(\varepsilon_*=-b/a\in(-1/2,0)\). At this point, \(\Sigma=(\sigma^2/a)D\), the matched force for \(c=\sigma^2/a\). This proves both the sharp transition and its equality case without an asymptotic or thermodynamic limit.

## Verification

The accompanying standalone `verify.py` uses NumPy and SciPy and directly solves the complete stationary Lyapunov equation for \((y,v,f)\), without assuming the derived modal covariance formula. It checks 40 random connected weighted graphs and 40 rings, the latter at five force-correlation parameters each. All 80 independent covariance-system tests passed. The largest absolute discrepancy was \(6.151\times10^{-14}\), including stationary residuals, graph-matched covariance and power, vanishing position–velocity covariance, and simultaneous off-diagonal ring signs. Execute `python verify.py` with NumPy and SciPy installed. These finite numerical checks do not prove the quantified theorems; the preceding stationary-moment and matrix-positivity arguments do.

## Relationship to prior work

Marini Bettolo Marconi, Löwen, and Caprini derive the harmonic active-chain spectra and equal-time velocity and displacement correlations for *spatially independent* active forces (arXiv:2401.07972v1, Sections II–IV and appendices, particularly the independent-noise assumption and velocity equations). Their modal response underlies the present calculation and is not claimed as new. The present theorem changes the spatial force covariance and classifies which covariances cancel all stationary intersite velocities, why the resulting marginal has two distinct temperatures despite continuing power injection, and the complete all-pair sign reversal on a periodic ring. No same-statement result was identified in the inspected source sections.

Goychuk, Kannan, and Kardar (arXiv:2401.14870v1) analyze correlations generated by delayed active forces in overdamped polymer dynamics, rather than the inertial graph-matched OU network considered here. Sarkar, Santra, and Basu (arXiv:2210.09035) study boundary-driven harmonic chains; their accessible abstract discusses bulk kinetic temperature but does not directly settle this bulk spatial-covariance rigidity. Classical linear systems and general Gaussian covariance-shaping theory could contain an implicit equivalent reformulation; the present theorem's novelty is assessed specifically as the explicit graph-noise structural classification and ring sign result, not as a new linear-response technique.

## Limitations

The results require linear harmonic forces, homogeneous \(m,\gamma,\tau\), and Gaussian Ornstein–Uhlenbeck active noise. The rigidity assertion assumes \(\Sigma L=L\Sigma\); the global sign theorem concerns periodic rings with nearest-neighbor active-force covariance and \(-1/2<\varepsilon<1/2\). Stationary position distributions refer only to the translation-quotiented coordinates. Equal-time Gaussian factorization does not imply equilibrium dynamics, absence of entropy production, or vanishing two-time correlations. The first source's full article was inspected, but an equivalent result in unidentified general covariance-shaping literature or the unavailable full text of the relevant 2023 correlated-force polymer paper remains a residual priority risk.

## References

1. U. Marini Bettolo Marconi, H. Löwen, and L. Caprini, *Active fluctuations in the harmonic chain: phonons, entropons and velocity correlations*, arXiv:2401.07972v1 (first posted 2024-01-15), https://arxiv.org/abs/2401.07972.
2. A. Goychuk, D. Kannan, and M. Kardar, *Delayed excitations induce polymer looping and coherent motion*, arXiv:2401.14870v1 (2024), https://arxiv.org/abs/2401.14870.
3. R. Sarkar, I. Santra, and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (2022), https://arxiv.org/abs/2210.09035.
4. A. Goychuk and collaborators, *Polymer folding through active processes recreates features of genome organization*, Proceedings of the National Academy of Sciences (2023), doi:10.1073/pnas.2221726120.
