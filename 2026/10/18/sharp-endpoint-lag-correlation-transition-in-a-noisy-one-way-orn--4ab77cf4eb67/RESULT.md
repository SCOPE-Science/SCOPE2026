# Sharp endpoint-lag correlation transition in a noisy one-way Ornstein–Uhlenbeck chain

## Finding

Consider a stationary, one-way chain of \(n\ge 2\) linear diffusions with damping \(a>0\), forward coupling \(g>0\), and independent noise intensity \(D>0\). Define its endpoint lag correlation by
\[
R_n(t)=\frac{\operatorname{Cov}(X_1(0),X_n(t))}
 {\sqrt{\operatorname{Var}(X_1)\operatorname{Var}(X_n)}}\qquad(t\ge0).
\]
Put \(m=n-1\), \(h=g/a\), \(E_m(z)=\sum_{j=0}^{m}z^j/j!\), and
\[
S_m(h)=\sum_{j=0}^{m}\binom{2j}{j}\left(\frac{h}{2}\right)^{2j}.
\]
The exact correlation profile is
\[
R_n(t)=\frac{(h/2)^m e^{-at}E_m(2at)}{\sqrt{S_m(h)}}.
\]
For every \(m\ge1\) this profile has **exactly one global maximum** at \(t_m=\lambda_m/(2a)>0\), where \(\lambda_m\) is the unique positive root of
\[
\sum_{j=0}^{m-1}\frac{\lambda_m^j}{j!}=\frac{\lambda_m^m}{m!}.
\]
This optimal lag is independent of coupling and noise, and obeys
\[
\lambda_m=2m-2+O(m^{-1}),\qquad at_m=m-1+O(m^{-1}).
\]
Writing \(M_m(h)=R_n(t_m)\), the maximum exhibits a sharp three-regime depth law:
\[
M_m(h)\sim
\begin{cases}
\sqrt{2/\pi}\,(1-h^2)^{1/4}h^m m^{-1/2},&0<h<1,\\
\pi^{-1/4}m^{-3/4},&h=1,\\
\sqrt2\,\pi^{-1/4}\sqrt{1-h^{-2}}\,m^{-1/4},&h>1.
\end{cases}
\]
For the critical coupling window \(h_m=\exp(\theta/m)\), for every fixed real \(\theta\), there is also an exact crossover:
\[
\lim_{m\to\infty}m^{3/4}M_m(h_m)=
\frac{\sqrt2\,\pi^{-1/4}e^\theta}
{\left(\int_0^1s^{-1/2}e^{2\theta s}\,ds\right)^{1/2}}.
\]
In contrast, the reverse endpoint correlation decays monotonically:
\[
\frac{\operatorname{Cov}(X_n(0),X_1(t))}
{\sqrt{\operatorname{Var}(X_1)\operatorname{Var}(X_n)}}
=\frac{(h/2)^m}{\sqrt{S_m(h)}}e^{-at}.
\]
Thus a directionally delayed maximum survives at every finite chain length, but its observable amplitude is exponentially small, \(m^{-3/4}\), or \(m^{-1/4}\), according as coupling lies below, at, or above damping. The algebraic regimes concern **normalized endpoint correlation**, not an unstable drift: all finite-chain drift eigenvalues equal \(-a\).

## Assumptions and scope

On one probability space take independent standard Brownian motions \(W_1,\ldots,W_n\) and solve the Itô system
\[
\begin{aligned}
dX_1(t)&=-aX_1(t)\,dt+\sqrt{2D}\,dW_1(t),\\
dX_j(t)&=(-aX_j(t)+gX_{j-1}(t))\,dt+\sqrt{2D}\,dW_j(t),\quad 2\le j\le n.
\end{aligned}
\]
The process is initialized in its unique centered stationary Gaussian law. \(D,a,g>0\); \(n\ge2\) is an integer. The limit \(m\to\infty\) keeps \(a,D\) fixed and takes the stated coupling regimes; no infinite-dimensional invariant process is asserted. \(E_m\), \(S_m\), \(h\), \(t_m\), and \(M_m\) are defined above. The normalizing standard deviations are strictly positive.

## Proof

**1. Stationarity and exact endpoint covariance.** Let \(L\) be the lower shift matrix, so the drift is \(A=-aI+gL\) with \(L^n=0\). All its eigenvalues are \(-a<0\), hence the stationary Gaussian covariance is the convergent integral
\[
\Sigma=2D\int_0^\infty e^{As}e^{A^{\mathsf T}s}\,ds.
\]
The source coordinate has \(\Sigma_{11}=D/a\). For \(j\ge2\), stationarity of the product \(X_1X_j\), using independence of its Brownian increments, gives
\[
0=-2a\Sigma_{1j}+g\Sigma_{1,j-1},
\quad\text{so}\quad
\Sigma_{1j}=\frac Da\left(\frac g{2a}\right)^{j-1}.
\]
For each \(j\), the independent-noise representation gives
\[
X_j(t)=\sqrt{2D}\sum_{k=0}^{j-1}\frac{g^k}{k!}
\int_{-\infty}^t e^{-a(t-s)}(t-s)^k\,dW_{j-k}(s).
\]
Itô isometry and \(\int_0^\infty e^{-2as}s^{2k}ds=(2k)!/(2a)^{2k+1}\) yield
\[
\Sigma_{nn}=\frac Da\sum_{k=0}^{m}\binom{2k}{k}
\left(\frac g{2a}\right)^{2k}=\frac Da S_m(h).
\]
For \(t\ge0\), independent future noise contributes zero to \(\operatorname{Cov}(X_1(0),X_n(t))\), so matrix exponentiation and \(L^n=0\) give
\[
\begin{aligned}
\operatorname{Cov}(X_1(0),X_n(t))
&=(e^{At}\Sigma)_{n1}\\
&=e^{-at}\sum_{k=0}^{m}\frac{(gt)^k}{k!}\Sigma_{1,n-k}\\
&=\frac Da\left(\frac h2\right)^m e^{-at}E_m(2at).
\end{aligned}
\]
The first coordinate depends only on its own past and future noise, giving the reverse correlation formula. Dividing by the endpoint standard deviations proves the two exact profiles.

**2. The unique lag maximum.** With \(u=at\), differentiation gives
\[
\frac{d}{du}\big[e^{-u}E_m(2u)\big]
=e^{-u}\left[E_{m-1}(2u)-\frac{(2u)^m}{m!}\right].
\]
For \(z>0\), the ratio
\[
\frac{m!E_{m-1}(z)}{z^m}
=\sum_{\ell=1}^{m}\frac{m!}{(m-\ell)!z^\ell}
\]
is strictly decreasing continuously from \(+\infty\) to zero. It crosses one exactly once; the derivative changes from positive to negative there. The endpoint at infinity is zero. Hence the unique critical point is the unique global maximum. At its root, \(E_m(\lambda_m)=2\lambda_m^m/m!\). Thus
\[
M_m(h)=\frac{(h/2)^m}{\sqrt{S_m(h)}}
\frac{2e^{-\lambda_m/2}\lambda_m^m}{m!}.
\]

**3. Quantitative optimal-delay asymptotics.** The root equation can equivalently be written
\[
1=\sum_{\ell=1}^{m}\frac{(m)_\ell}{\lambda_m^\ell},
\]
where \((m)_\ell=m(m-1)\cdots(m-\ell+1)\). For any fixed real \(c\), splitting the sum at \(\ell=\lfloor m^{1/3}\rfloor\), expanding its low-order terms and bounding the remainder geometrically, gives
\[
\sum_{\ell=1}^{m}\frac{(m)_\ell}{(2m+c)^\ell}
=1-\frac{c+2}{m}+O(m^{-2}).
\]
Indeed \(\sum_{\ell\ge1}2^{-\ell}=1\), \(\sum_{\ell\ge1}\ell 2^{-\ell}=2\), and \(\sum_{\ell\ge1}\ell(\ell-1)2^{-\ell}=4\). Strict decrease of the left side in its denominator brackets the unique solution at \(\lambda_m=2m-2+O(m^{-1})\). Stirling's formula then yields
\[
\frac{2e^{-\lambda_m/2}\lambda_m^m}{m!}
\sim\frac{2^{m+1}}{\sqrt{2\pi m}},
\quad\text{whence}\quad
M_m(h)\sim\sqrt{\frac2{\pi m}}\frac{h^m}{\sqrt{S_m(h)}}.
\]
The last equivalence is valid even for a positive coupling \(h=h_m\) depending on \(m\), since the factor depending on \(m\) alone has a relative error tending to zero.

**4. Three regimes and critical window.** If \(0<h<1\), the generating function for central binomial coefficients gives
\(S_m(h)\to(1-h^2)^{-1/2}\). If \(h=1\), the exact identity
\[
S_m(1)=(2m+1)\binom{2m}{m}4^{-m}
\sim2\sqrt{m/\pi}
\]
gives the critical decay. If \(h>1\), divide the sum by its final term and reverse the index. The ratio of the \((m-k)\)-th term to the final term tends to \(h^{-2k}\); dominated geometric summation yields
\[
S_m(h)\sim\frac{h^2}{h^2-1}\frac{h^{2m}}{\sqrt{\pi m}}.
\]
Substitution into the maximum formula gives the stated three limits.

For \(h_m=e^{\theta/m}\), the uniform central-binomial asymptotic away from index zero, with an integrable upper bound proportional to \(j^{-1/2}\), yields the Riemann-sum limit
\[
\frac{S_m(h_m)}{\sqrt{m/\pi}}
\longrightarrow \int_0^1s^{-1/2}e^{2\theta s}\,ds.
\]
Together with \(h_m^m=e^\theta\), this proves the crossover without interchanging the fixed-coupling limits improperly.

## Verification

The standalone script `verify.py` computes the stationary covariance independently by solving the continuous Lyapunov equation and computes finite-lag covariance by an independent matrix exponential. It checks 105 combinations of chain length, coupling, and lag for \(2\le n\le8\). It independently brackets the unique optimizer for \(1\le m\le250\), then compares all three predicted scaling coefficients and three critical-window profiles against finite-chain exact formulas. The output from an actual execution is `checks.txt`. This numerical verification supplements, rather than replaces, the unrestricted analytical proof above.

Run with `python verify.py` in a Python environment with NumPy and SciPy installed.

## Relationship to prior work

Pal and Gupta (arXiv:2609.05391, first available September 4, 2026) study nonreciprocal Ornstein–Uhlenbeck models, exceptional points, and polynomially dressed relaxation. That motivates examination of a completely specified one-way, equal-damping nearest-neighbor OU cascade. The cascade here is specified directly; it is **not asserted to be the same parameterization or stationary measure** as any particular chain in that preprint. The new mathematical object is the *maximum normalized endpoint time-lag correlation*, its unique coupling-independent maximizing lag, and the sharp three-regime depth asymptotics including the critical window.

Hennequin, Vogels, and Gerstner (2012) prove amplification results for random all-to-all triangular OU couplings, including a general Lyapunov recursion and discussions of finite memory in feedforward networks. The present calculation uses deterministic nearest-neighbor coupling with fresh independent noise at every site, and classifies a **specific directed endpoint cross-correlation peak**, not ensemble-averaged total noise amplification.

Browning, Jenner, Baker, and Maini (2024) analyze a unidirectional multicompartment system driven by **one OU noise input** with noise-free downstream compartments and derive its covariance/autocorrelation formulas. Its general Gaussian matrix identities are standard prerequisites. The present independent-noise-at-every-site model and critical three-regime normalized peak law are not obtained by substituting a parameter in their one-noise variance expression; the additional downstream noise changes the endpoint normalization to the partial central-binomial sum \(S_m(h)\), producing the critical transition.

An originality search of available research records and primary literature did not reveal the complete endpoint-peak classification. That absence is not a proof of novelty. The full September 2026 motivating preprint could not be inspected, leaving an explicit residual risk that its calculations, or another unindexed work, contain an equivalent conclusion.

## Limitations

The theorem is for finite open directed chains with identical damping, identical positive nearest-neighbor coupling, and independent equal-intensity white noises; it does not cover periodic chains, heterogeneous coefficients, colored or correlated noise, or nonlinear dynamics. Although the large-depth asymptotics vary sharply at \(g=a\), all finite chains remain dynamically stable. The theorem does not claim a thermodynamic stationary measure at \(n=\infty\), an entropy-production identity, or a causal intervention theorem. Independent expert audit and independent replication have not been performed.

## References

1. S. K. Pal and S. Gupta, “Non-reciprocally interacting Ornstein–Uhlenbeck processes: Exceptional points, Anomalous relaxation, Pseudo-equilibrium and Boundary refrigeration,” arXiv:2609.05391 (first submitted 2026-09-04), https://arxiv.org/abs/2609.05391.
2. G. Hennequin, T. P. Vogels, and W. Gerstner, “Non-normal amplification in random balanced neuronal networks,” *Physical Review E* **86**, 011909 (2012), DOI 10.1103/PhysRevE.86.011909, https://cbl.eng.cam.ac.uk/publications/hennequin-pre-2012.pdf.
3. A. P. Browning, A. L. Jenner, R. E. Baker, and P. K. Maini, “Smoothing in linear multicompartment biological processes subject to stochastic input,” *Physical Review E* **109**, 054405 (2024), DOI 10.1103/PhysRevE.109.054405, https://people.maths.ox.ac.uk/maini/PKM%20publications/528.pdf.
