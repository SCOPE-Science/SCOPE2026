# Finite-population sign reversal of radial cofluctuations in harmonically coupled active particles

## Finding

Consider the planar, globally harmonically attracted active-particle system defined below. For distinct particles \(i\ne j\), its stationary squared-distance covariance about the instantaneous centroid changes sign at an **exact finite-population persistence threshold**. The two standard orientation mechanisms have different thresholds even though their orientation autocorrelation functions agree exactly.

Write \(\mu=N\kappa\), \(\alpha=(\mu\tau)^{-1}\), \(R=v/\mu\), and \(m_2=R^2/(1+\alpha)\). The exact normalized covariance is

\[
\frac{N^2\operatorname{Cov}(|\ell_i|^2,|\ell_j|^2)}{m_2^2}
=\begin{cases}
\displaystyle\frac{\alpha-2+6/N}{\alpha+2},&\text{isotropic run-and-tumble (RTP)},\\[5pt]
\displaystyle\frac{2\alpha^2-7\delta_N\alpha-3\delta_N}{(\alpha+3)(2\alpha+1)},&\text{active Brownian orientation (ABP)},
\end{cases}
\qquad\delta_N=1-\frac3N.
\]

For \(N=2,3\), both covariances are strictly positive at every \(\alpha>0\). For every \(N\ge4\) there is exactly one sign reversal for each model, at

\[
\alpha_{\mathrm{RTP}}(N)=2\delta_N,
\qquad
\alpha_{\mathrm{ABP}}(N)=\frac{7\delta_N+\sqrt{49\delta_N^2+24\delta_N}}4.
\]

Both covariances are negative below their respective thresholds and positive above; equality holds at the threshold. Furthermore,
\(\alpha_{\mathrm{RTP}}(N)<\alpha_{\mathrm{ABP}}(N)\), so the **same fixed persistence parameter** produces positive radial covariance for RTP and negative radial covariance for ABP throughout the intervening open interval. The infinite-population threshold limits are \(2\) and \((7+\sqrt{73})/4\), respectively. The normalized covariance has a nontrivial limit when multiplied by \(N^2\), although the unnormalized correlation vanishes as \(N\to\infty\) at fixed parameters.

## Assumptions and scope

Fix integer \(N\ge2\), attractive coupling \(\kappa>0\), propulsion speed \(v>0\), and persistence time \(\tau>0\). In \(\mathbb R^2\), each position satisfies

\[
\dot r_j(t)=-\kappa\sum_{k\ne j}(r_j(t)-r_k(t))+v n_j(t),\quad j=1,\ldots,N.
\]

The unit-vector orientation processes \(n_j\) are mutually independent, stationary, isotropic, and follow one of two dynamics: RTP refreshes its angle uniformly on \([0,2\pi)\) at rate \(\tau^{-1}\); ABP has a stationary uniform initial angle and independent rotational Brownian motion with angular generator \(\tau^{-1}\partial_\theta^2\). No additional positional noise acts. Both mechanisms satisfy \(\mathbb E[n_j(t)\cdot n_j(s)]=e^{-|t-s|/\tau}\). The positions need not be stationary because their centroid can move; the relative positions \(\ell_j=r_j-N^{-1}\sum_k r_k\) have a unique stationary law obtained from a pullback integral. All covariances in the theorem refer to that law, and all parameters are strictly positive as specified.

## Proof

**Exact reduction without a Gaussian population approximation.** Let \(\bar r=N^{-1}\sum_jr_j\). With \(\mu=N\kappa\), direct subtraction gives
\(\dot\ell_j=-\mu\ell_j+v(n_j-\bar n)\). Set

\[
Z_j(t)=v\int_{-\infty}^{t}e^{-\mu(t-s)}n_j(s)\,ds.
\]

The \(Z_j\) are independent, centered, planar isotropic vectors with \(|Z_j|\le R\). Exactly, for every finite \(N\),
\(\ell_j=Z_j-\bar Z=\sum_k P_{jk}Z_k\), where \(P=I-\mathbf1\mathbf1^{\mathsf T}/N\). This identity is not a central-limit or Gaussian approximation.

**The single-particle moments.** Let \(z=Z/R\), rescale time by \(\mu\), and encode the orientation as \(e^{i\theta}\). Then \(\dot z=-z+e^{i\theta}\). For \(p,q\) nonnegative integers and integer \(k\), put \(F_{p,q,k}=\mathbb E[z^p\bar z^{\,q}e^{ik\theta}]\). Stationarity and the orientation generator yield, whenever \(p+q>0\),

\[
F_{p,q,k}=\frac{pF_{p-1,q,k+1}+qF_{p,q-1,k-1}}{p+q+\alpha g(k)},
\quad F_{0,0,k}=\mathbf1_{\{k=0\}},
\]

with \(g(k)=\mathbf1_{\{k\ne0\}}\) for RTP and \(g(k)=k^2\) for ABP. The recursion terminates at total degree zero and has strictly positive denominators at positive degree. Applying it at total degrees two and four gives, for \(m_2=\mathbb E|Z|^2\) and \(m_4=\mathbb E|Z|^4\),

\[
m_2=\frac{R^2}{1+\alpha},\qquad
m_4=\begin{cases}
\displaystyle\frac{2R^4}{(1+\alpha)(2+\alpha)},&\mathrm{RTP},\\[5pt]
\displaystyle\frac{R^4(4\alpha+3)}{(1+\alpha)(2\alpha+1)(\alpha+3)},&\mathrm{ABP}.
\end{cases}
\]

These one-particle fourth-moment formulas are known; the recurrence independently reconstructs them for the present exact finite-\(N\) system.

**The two-particle fourth-order contraction.** For independent, centered, isotropic planar vectors \(Z_k\) having the common moments \(m_2,m_4\), and deterministic real coefficient arrays \(a,b\), an expansion by coincident index patterns proves

\[
\operatorname{Cov}\left(\left|\sum_ka_kZ_k\right|^2,
\left|\sum_kb_kZ_k\right|^2\right)
=m_2^2\left(\sum_ka_kb_k\right)^2
+(m_4-2m_2^2)\sum_ka_k^2b_k^2.
\]

Indeed, \(\mathbb E[Z_kZ_k^{\mathsf T}]=(m_2/2)I_2\), so for independent distinct indices \(k,l\), \(\mathbb E[(Z_k\cdot Z_l)^2]=m_2^2/2\); repeated-index contractions contribute \(m_4\). This establishes the identity without requiring Gaussian fourth moments.

For different projection rows \(P_i,P_j\),
\(\sum_kP_{ik}P_{jk}=-1/N\) and \(\sum_kP_{ik}^2P_{jk}^2=(2N-3)/N^3\). Therefore

\[
\operatorname{Cov}(|\ell_i|^2,|\ell_j|^2)
=\frac{m_2^2}{N^2}\left[1-\frac{2N-3}{N}\left(2-\frac{m_4}{m_2^2}\right)\right].
\]

Substitution gives the two expressions in the Finding section. In the RTP case \(2-m_4/m_2^2=2/(\alpha+2)\); in the ABP case it is \((7\alpha+3)/((\alpha+3)(2\alpha+1))\).

**Sign classification.** For \(N=2,3\), substitution into the displayed rational formulas shows strict positivity for every \(\alpha>0\). If \(N\ge4\), then \(\delta_N>0\): the RTP sign is that of \(\alpha-2\delta_N\), and the ABP sign is that of \(2\alpha^2-7\delta_N\alpha-3\delta_N\). The latter quadratic is negative at zero, has strictly positive derivative for \(\alpha\ge7\delta_N/4\), and has one positive and one negative root; its unique positive root is the claimed expression. Evaluating that quadratic at \(2\delta_N\) gives \(-6\delta_N^2-3\delta_N<0\), proving the strict ordering of thresholds. Their large-\(N\) limits follow directly.

## Verification

The included standalone `verify.py` uses only the Python standard library. Run `python verify.py` after extracting it. It independently obtains the radial moments from the finite-degree Markov-generator recurrence using exact rational arithmetic; checks the centered-projection contraction against the closed formulas for both models over a finite parameter grid; enumerates the complete configuration space of independent four-direction isotropic vectors for populations of size two through six; and checks exact threshold signs and a concrete four-particle example. Its completed run produced **1,421 exact-rational assertions, all passing**.

For \(N=4\), \(\alpha=1\), and \(R=1\), the exact pairwise covariances are \(+1/384\) for RTP and \(-1/1536\) for ABP, illustrating the opposite signs without a numerical approximation. These finite tests are consistency checks, not a proof for the infinite family; the argument above supplies the universal proof.

## Relationship to prior work

Dutta and Basu, *Collective Ring Formation in Active Matter* (arXiv:2607.16905v1, first publicly posted July 18, 2026), introduce the same globally harmonic active-particle model, examine its tagged-particle radial and orientation distributions, and give the underlying isolated-particle second and fourth radial moments (their equations (60)–(62)). Those results are credited. The present contribution is instead an **exact finite-population joint statistic of two different particles** with a complete sign-threshold classification and a model-discriminating interval. It does not assert new one-particle fourth moments or a new Gaussian central-limit approximation.

Singh and Kundu, *Crossover behaviours exhibited by fluctuations and correlations in a chain of active particles* (arXiv:2012.13910), study nearest-neighbor harmonic chains and predominantly second-order coordinate correlations. That graph, observable, and order of correlation differ from the complete-graph fourth-order radial statistic considered here. The general independent-vector moment contraction is elementary and not claimed as new. A close full-text comparison of these relevant works and searches for prior squared-radius cross correlations found no exact matching sign classification; this is a qualified priority assessment rather than a guarantee of uniqueness.

## Limitations

The formula applies only to identical planar independent-orientation particles with complete-graph linear attractive forces and no positional diffusion; it is not a theorem for hard-core interactions, nonlinear potentials, or inertial dynamics. It concerns stationary relative positions, not stationary absolute positions or time-integrated transport. With \(\mu,v,\alpha\) fixed as the population varies (that is, \(\kappa=\mu/N\)), the covariance is of order \(N^{-2}\); detecting its sign experimentally may require substantial sampling. The isolated-particle moment inputs are established literature, and a general known moment identity may make the final deduction short; broader unindexed prior statements could contain an equivalent pairwise implication. No independent scientific review or publication-priority certification is claimed.

## References

1. D. Dutta and U. Basu, *Collective Ring Formation in Active Matter*, arXiv:2607.16905v1 (2026-07-18), https://arxiv.org/html/2607.16905.
2. P. Singh and A. Kundu, *Crossover behaviours exhibited by fluctuations and correlations in a chain of active particles*, arXiv:2012.13910 (2020-12-27), https://arxiv.org/abs/2012.13910.
