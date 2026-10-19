# Universal correlation reversal under a switching boundary reservoir

## Finding

Let \(N\geq2\). For the symmetric simple exclusion process (SSEP) on sites \(1,\ldots,N\) with a perpetually full left reservoir and a right reservoir switching between empty and full at positive rate \(\kappa\), let \(\eta_i\in\{0,1\}\) denote stationary occupancy. Every pair of distinct sites exhibits a reversal of the sign of its stationary connected correlation as the reservoir-switching rate increases.

More precisely, for \(1\leq i<j\leq N\), the stationary mean and two limiting covariances are exactly
\[
\mathbb E_\kappa\eta_i=1-\frac{i}{2(N+1)},
\]
\[
\lim_{\kappa\downarrow0}\operatorname{Cov}_\kappa(\eta_i,\eta_j)
=\frac{i\big((N+2)j-2(N+1)\big)}{4N(N+1)^2}>0,
\qquad
\lim_{\kappa\to\infty}\operatorname{Cov}_\kappa(\eta_i,\eta_j)
=-\frac{i(N+1-j)}{4N(N+1)^2}<0.
\]
Consequently every such pair has at least one finite positive switching rate at which its covariance vanishes. No uniqueness of a crossover is claimed for general \(N\). In the smallest nontrivial system, \(N=2\), the entire function is
\[
\operatorname{Cov}_\kappa(\eta_1,\eta_2)=
\frac{3-4\kappa-2\kappa^2}{36(2\kappa+1)(2\kappa+3)},
\]
with its **unique** positive zero at \(\kappa=\sqrt{10}/2-1\).

## Assumptions and scope

The process is a finite continuous-time Markov chain on \(\{0,1\}^N\times\{0,1\}\). For each bond \(i,i+1\), the two occupations are exchanged at rate one if they differ. At site \(1\), a particle is added at rate one whenever it is empty, with no removal there. The right boundary is controlled by an autonomous, symmetric two-state continuous-time Markov chain \(\zeta\), flipping \(0\leftrightarrow1\) at rate \(\kappa>0\). Conditional on \(\zeta=0\), an occupied site \(N\) loses its particle at rate one; conditional on \(\zeta=1\), an empty site \(N\) gains a particle at rate one. No other boundary transitions occur. All these clocks are conditionally independent given the current state. Time is normalized so each allowed nearest-neighbor exchange and each active reservoir update has rate one.

The joint chain is irreducible for every \(\kappa>0\) and therefore has a unique stationary law, under which all expectations below are taken. Switching is **of the boundary environment only**; it never instantaneously resets the particles. The limits are taken at each fixed finite \(N\), not uniformly in \(N\).

## Proof

**1. Constant-reservoir reference law.** Consider first the same SSEP with fixed reservoir densities \(a,b\in[0,1]\), implemented by left birth/death rates \(a,1-a\), right birth/death rates \(b,1-b\). The stationary one-site means solve the discrete harmonic equation with virtual boundary values \(m_0=a\), \(m_{N+1}=b\), hence
\[
m_i=a+(b-a)\frac{i}{N+1}.
\]
The stationary connected two-site moments, for \(i<j\), solve the discrete two-particle harmonic equation away from the neighboring-site boundary, vanish when a coordinate is at its reservoir boundary, and satisfy the adjacent-source equation from the exclusion interaction. Direct substitution gives the unique solution
\[
C^{a,b}_{i,j}=-\frac{(a-b)^2i(N+1-j)}{N(N+1)^2}.
\tag{1}
\]
For completeness, write \(C_{0,j}=C_{i,N+1}=0\). For \(j\ge i+2\), \(C_{i,j}\) is harmonic in the two coordinates. For adjacent \(j=i+1\), exact stationarity of \(\eta_i\eta_{i+1}\) yields
\[
C_{i-1,i+1}+C_{i,i+2}-2C_{i,i+1}=\frac{(a-b)^2}{(N+1)^2}.
\]
Formula (1) obeys these equations and the boundaries. Uniqueness follows from the finite absorbed two-particle exclusion chain (alternatively, the maximum principle for its Dirichlet problem). It also holds at \(a,b\in\{0,1\}\), either directly or by continuity from interior densities. In particular, with \((a,b)=(1,1)\) the only stationary configuration is full occupancy; with \((a,b)=(1,0)\) formula (1) supplies strictly negative pair covariance.

**2. Means at any switching rate.** Autonomy and symmetry of the boundary process give \(\mathbb E_\kappa\zeta=1/2\). Applying the joint generator to \(\eta_i\) gives \(m_{i-1}-2m_i+m_{i+1}=0\), with effective virtual boundary values \(m_0=1\) and \(m_{N+1}=1/2\). The right boundary contribution is exactly \(\mathbb E(\zeta-\eta_N)=1/2-m_N\), so no independence assumption involving \(\zeta\) and \(\eta_N\) is needed. Solving gives \(m_i=1-i/[2(N+1)]\) at every \(\kappa>0\).

**3. Slow switching.** In the limit \(\kappa\downarrow0\), the joint invariant probability converges to the equal mixture of the invariant law with permanently empty right bath and the fully occupied configuration with permanently full right bath. This follows by the finite-state stationary equations: any subsequential limit is invariant in each frozen bath sector, whose stationary law is unique, while the autonomous bath retains weights \(1/2,1/2\). Let \(m_i^{(0)}=1-i/(N+1)\) and \(m_i^{(1)}=1\). The law of total covariance gives
\[
\lim_{\kappa\downarrow0}C_{i,j}(\kappa)
=\tfrac12 C^{1,0}_{i,j}
 +\tfrac14(m_i^{(1)}-m_i^{(0)})(m_j^{(1)}-m_j^{(0)})
=\frac{i\big((N+2)j-2(N+1)\big)}{4N(N+1)^2}.
\]
Because \(j\ge2\), its numerator bracket is at least \(2\), so the limit is strictly positive for all pairs.

**4. Fast switching.** As \(\kappa\to\infty\), finite-state averaging applies: the bath equilibrates to \(\operatorname{Bernoulli}(1/2)\) and the particle chain has left density \(1\) and averaged right density \(1/2\). One can see this directly by dividing the finite stationary equation by \(\kappa\), which forces equality of the two bath-sector probabilities for each particle configuration in every limit; summing the sector equations then gives the stationary equation for the averaged particle generator. That averaged chain has a unique stationary law. Formula (1) with \((a,b)=(1,1/2)\) therefore yields
\[
\lim_{\kappa\to\infty}C_{i,j}(\kappa)
=-\frac{i(N+1-j)}{4N(N+1)^2}<0.
\]
For \(\kappa>0\) the joint invariant distribution solves a nonsingular, finite linear system with polynomial dependence on \(\kappa\); its covariances are continuous. The intermediate value theorem proves at least one zero for each pair.

**5. Exact two-site threshold.** For \(N=2\), stationarity gives \(m_1=5/6\), \(m_2=2/3\). Put \(u_1=\mathbb E(\zeta\eta_1)\), \(u_2=\mathbb E(\zeta\eta_2)\). The generator equations are
\[
(2+2\kappa)u_1-u_2=\tfrac12+\kappa\tfrac56,
\qquad
(2+2\kappa)u_2-u_1=\tfrac12+\kappa\tfrac23.
\]
They yield \(u_1=(10\kappa^2+20\kappa+9)/(24\kappa^2+48\kappa+18)\). The equation for \(\eta_1\eta_2\) is \(0=m_2+u_1-2\mathbb E(\eta_1\eta_2)\), giving the claimed covariance after subtracting \(m_1m_2\). Its denominator is positive and the numerator \(3-4\kappa-2\kappa^2\) is strictly decreasing from positive to negative on \((0,\infty)\), with unique zero \(\sqrt{10}/2-1\).

## Verification

The standalone `verify.py` implements the entire joint generator independently of the proof's reduced moment formulas. Its exact symbolic two-site calculation reproduces the rational covariance and unique positive zero. Full stationary solves for all pairs in chains \(2\leq N\leq5\) verify the mean profile and both limiting signs numerically at switching rates \(10^{-6}\) and \(10^6\). The discrete reference covariance equations are checked over \(2\leq N\leq80\). The script runs with Python 3, NumPy, and SymPy via `python verify.py`. These finite checks are corroboration; the all-size assertion follows from the proof above.

## Relationship to prior work

Derrida, Lebowitz, and Speer give exact fixed-reservoir open-SSEP microscopic correlations, including their equation (7.13), which supplies the established negative-correlation baseline (1). They do not treat a common randomly switching boundary density. Santos and Schütz compute time-dependent correlations for a semi-infinite SSEP in contact with a **constant-density** reservoir; their dynamics do not provide the finite joint stationary switching-bath law. Later switching interacting-particle models include particles whose **hopping rate or type** changes in time against prescribed reservoirs; this is different from a single reservoir-level telegraph environment, and those results do not imply the stated all-pair crossover. The new assertion is the finite-chain crossover under boundary switching and, for two sites, its exact unique switching threshold—not the known constant-reservoir formula.

## Limitations

For \(N>2\) the proof establishes existence, not uniqueness, of positive finite crossover rates; it does not supply their values or monotonicity of covariance as a function of switching rate. The endpoint formulas take \(\kappa\to0\) or \(\kappa\to\infty\) with \(N\) held fixed; no uniform thermodynamic-limit statement is asserted. The analysis uses unit exchange and boundary update rates and a symmetric autonomous telegraph bath. Novelty is assessed against identified literature and is not a claim of exhaustive bibliographic completeness; independent validation has not been performed.

## References

1. B. Derrida, J. L. Lebowitz, and E. R. Speer, “Large Deviation of the Density Profile in the Steady State of the Open Symmetric Simple Exclusion Process,” arXiv:cond-mat/0109346 (first submitted 19 September 2001), particularly §7.2 and Eq. (7.13). https://arxiv.org/abs/cond-mat/0109346
2. J. E. Santos and G. M. Schütz, “Exact time-dependent correlation functions for the symmetric exclusion process with open boundary,” arXiv:cond-mat/0104147 (first submitted 9 April 2001). https://arxiv.org/abs/cond-mat/0104147
3. S. Floreani, C. Giardinà, F. den Hollander, S. Nandan, and F. Redig, “Switching Interacting Particle Systems: Scaling Limits, Uphill Diffusion and Boundary Layer,” Journal of Statistical Physics 186 (2022), article 33. https://doi.org/10.1007/s10955-022-02878-7
4. H. Spohn, “Long range correlations for stochastic lattice gases in a non-equilibrium steady state,” Journal of Physics A 16 (1983), 4275–4291. https://doi.org/10.1088/0305-4470/16/18/029
