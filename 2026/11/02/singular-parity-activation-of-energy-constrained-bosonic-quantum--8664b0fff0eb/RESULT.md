# Singular parity activation of energy-constrained bosonic quantum communication

## Finding

Consider one bosonic mode with number operator \(\hat n\) and the binary phase-noise channel
\[
\Phi_p(\rho)=(1-p)\rho+p(-1)^{\hat n}\rho(-1)^{\hat n},\qquad 0\le p\le\tfrac12.
\]
For a mean input photon-number budget \(E>0\), let \(Q_E\) and \(P_E\) be its **unassisted** energy-constrained quantum and private classical capacities, with average energy constrained across channel uses. Set \(r=(1-2p)^2\), define the binary entropy \(h_2(u)=-u\log_2u-(1-u)\log_2(1-u)\), with \(h_2(0)=h_2(1)=0\), and the thermal entropy \(g(m)=(m+1)\log_2(m+1)-m\log_2m\), with \(g(0)=0\). Write
\[
\eta_r(q)=\frac{1-\sqrt{1-4(1-r)q(1-q)}}2.
\]
Then the exact two capacities coincide and are given by the one-variable optimization
\[
Q_E(\Phi_p)=P_E(\Phi_p)=\max_{0\le q\le\min\{E,1\}}\left[g\!\left(\frac{E-q}{2}\right)+h_2(q)-h_2\!\left(\eta_r(q)\right)\right].\tag{1}
\]
For every \(r>0\), the maximizing \(q=q_r\) is unique and strictly between zero and \(\min\{E,1\}\). With \(m_r=(E-q_r)/2\) and \(t_r=m_r/(1+m_r)\), the unique maximizing number distribution is
\[
\Pr(\hat n=2k)=(1-q_r)(1-t_r)t_r^k,\qquad
\Pr(\hat n=2k+1)=q_r(1-t_r)t_r^k\quad(k\ge0).\tag{2}
\]
At complete parity dephasing \(p=1/2\) (\(r=0\)), the optimizer is exclusively even, and \(Q_E=P_E=g(E/2)\). At the identity endpoint \(p=0\) (\(r=1\)), the optimum is \(q_1=E/(1+2E)\) with capacity \(g(E)\).

Most notably, let \(L_E=\ln(1+2/E)>0\). As \(r\downarrow0\), for fixed \(E>0\), the odd-photon probability and the strict capacity advantage over an even-only code exhibit the **essential singularity**
\[
q_r\sim \frac1e\exp\left(-\frac{L_E}{2r}\right),\qquad
Q_E(\Phi_p)-g(E/2)\sim\frac{r}{e\ln2}\exp\left(-\frac{L_E}{2r}\right).\tag{3}
\]
Thus an arbitrarily small residual parity coherence activates a nonzero but nonperturbatively small odd-sector component and transmission-rate gain.

## Assumptions and scope

The bosonic Fock Hilbert space is \(\ell^2(\mathbb N_0)\); \(\hat n|k\rangle=k|k\rangle\). The channel is memoryless, with independent binary phase kicks \(0\) and \(\pi\), exactly the CPTP map above; it has no photon loss. The constraint is \(\operatorname{Tr}(\hat n\rho)\le E\) on the average input across uses. We evaluate ordinary unassisted quantum and private capacities in bits per channel use under the standard vanishing-error definitions. The results concern fixed positive \(E\), and in (3) the limit \(r\downarrow0\) is taken at fixed \(E\). No formula for interactive/two-way assisted capacities is asserted. The binary two-point phase measure is singular with respect to Lebesgue measure and is outside the probability-density hypothesis in the motivating paper's formulation.

## Proof

**Step 1: degradability, and reduction to number-diagonal states.** A Stinespring isometry for the channel has output vectors \(|k\rangle_B\otimes|e_{k\bmod 2}\rangle_F\), where
\[
|e_0\rangle=\sqrt{1-p}|0\rangle+\sqrt p|1\rangle,\qquad
|e_1\rangle=\sqrt{1-p}|0\rangle-\sqrt p|1\rangle.
\]
Their overlap is \(1-2p\). Consequently the complementary output is the mixture \((1-q)|e_0\rangle\langle e_0|+q|e_1\rangle\langle e_1|\), where \(q\) is the total input occupation of odd Fock levels. It can be obtained from the channel output by measuring number parity and preparing the corresponding \(|e_j\rangle\) state; hence \(\Phi_p\) is degradable even though its phase law is discrete. The number measurement/pinching of an input does not change the complementary state or its energy, and does not decrease the channel-output entropy. Therefore a number-diagonal input maximizes coherent information at fixed energy. The harmonic oscillator has a well-defined Gibbs state at each positive temperature, and all finite-energy input and output entropies are bounded by \(g(E)<\infty\). The standard energy-constrained degradable-channel coding theorem therefore gives \(Q_E=P_E=\sup_{\rho:\,\operatorname{Tr}(\hat n\rho)\le E}I_c(\rho,\Phi_p)\); this coding theorem is an established ingredient, not asserted as a new result.

**Step 2: evaluate the environment and optimize the conditional number distribution.** The complementary qubit's smaller eigenvalue is \(\eta_r(q)\): its determinant is \(4p(1-p)q(1-q)=(1-r)q(1-q)\). If \(N\) is the input Fock number and \(N=2K+P\), \(P\in\{0,1\}\), then \(\Pr(P=1)=q\), \(\mathbb E K\le(E-q)/2\), and
\[
I_c=H(N)-h_2(\eta_r(q))=h_2(q)+H(K|P)-h_2(\eta_r(q)).
\]
The maximum Shannon entropy of a nonnegative integer at mean \(m\) is \(g(m)\), uniquely attained by the geometric law \((1-t)t^k\), with \(t=m/(m+1)\). Concavity and strict increase of \(g\) give
\[
H(K|P)\le(1-q)g(\mathbb E[K|P=0])+qg(\mathbb E[K|P=1])\le g((E-q)/2).
\]
The inequalities are attained for both conditional laws geometric with common mean \((E-q)/2\), proving (1) and (2), including uniqueness of the distribution whenever \(0<q<1\).

**Step 3: unique optimum and endpoints.** The quantity \(h_2(q)-h_2(\eta_r(q))\) is the conditional entropy \(H(P|F)\) of a binary classical register conditioned on the two pure environment states. It is concave in \(q\) by strong subadditivity. Because \(g((E-q)/2)\) is strictly concave for \(E-q>0\), the objective in (1) is strictly concave throughout the feasible interior. For \(0<r<1\), its right derivative at \(q=0\) diverges to \(+\infty\): with \(c=1-r\), the first-order expansion in natural-log units is \(h(q)-h(\eta_r(q))=rq\ln(1/q)+(r+c\ln c)q+O(q^2|\ln q|)\). Its left derivative at the upper endpoint is negative infinite from \(g((E-q)/2)\) if \(E\le1\), or from the binary conditional entropy if \(E>1\). At \(r=1\), the same boundary behavior holds because the conditional entropy reduces to \(h_2(q)\). Thus the optimizer is unique and interior. At \(r=0\), \(h_2(q)=h_2(\eta_0(q))\), making the objective \(g((E-q)/2)\) strictly decreasing in \(q\). At \(r=1\), the unique maximal number distribution is the ordinary photon-number geometric law of mean \(E\); its odd probability is \(E/(1+2E)\), yielding \(g(E)\).

**Step 4: essential singularity.** Work temporarily with natural entropies, writing \(\widetilde F_r(q)=(\ln2)F_r(q)\). Put \(m_0=E/2\), \(L_E=\ln(1+1/m_0)\), \(c=1-r\). Uniformly for \(0<r\le1/2\) and sufficiently small \(q>0\), differentiation of the two exact eigenvalue expressions gives
\[
\widetilde F_r'(q)=-\frac{L_E}{2}+r\ln(1/q)+c\ln c+O_E(q|\ln q|),\tag{4}
\]
and integration gives
\[
\widetilde F_r(q)-\widetilde F_r(0)
=q\big[-L_E/2+r(\ln(1/q)+1)+c\ln c\big]+O_E(q^2|\ln q|).\tag{5}
\]
Uniform convergence of \(F_r\) to \(g((E-q)/2)\) as \(r\downarrow0\), compactness of the admissible \(q\)-interval, and strict endpoint uniqueness imply \(q_r\to0\). For \(q=\exp(-L_E/(4r))\), (4) is strictly negative for small \(r\), whereas the derivative at smaller positive \(q\) tends to positive infinity. Strict concavity consequently implies \(0<q_r<\exp(-L_E/(4r))\), so \(q_r|\ln q_r|=o(r)\). Insert \(q=q_r\) in (4), use \((1-r)\ln(1-r)=-r+O(r^2)\), and solve:
\[
\ln(1/q_r)=\frac{L_E}{2r}+1+o(1).
\]
This establishes the first asymptotic in (3). Combining the stationarity identity (4) and the integrated expansion (5), with the exponentially small remainders, gives \(\widetilde F_r(q_r)-\widetilde F_r(0)=rq_r(1+o(1))\). Division by \(\ln2\) gives the second formula (3). These are genuine analytic limits, not inferences from finite sampling.

## Verification

The included `verify.py` constructs the complementary qubit's spectrum independently from its density-matrix determinant and compares it with \(\eta_r(q)\). It checks endpoint thermal-capacity identities at five energy budgets, stationary interior maxima for 16 energy/noise pairs, 200 independently sampled finite Fock distributions against the entropy upper envelope, and the exponentially small asymptotic regimes at 110-digit arithmetic precision. Running `python verify.py` with the included `requirements.txt` produced: `PASS: 382 independent finite and high-precision assertions`. Exact channel/capacity and limiting claims are proved above; numerical checks are corroboration only.

## Relationship to prior work

Arqand and Smith, *No advantage from classical assistance for energy-constrained bosonic dephasing channels* (arXiv:2610.13854v1, first public 2026-10-09), establish a general Fock-diagonal coherent-information characterization for bosonic phase-noise probability densities and explicitly leave concrete-noise optimization open. Their stated phase-noise density assumption excludes the two-point measure treated here, so this finding independently derives the degradable-channel unassisted reduction. Lami and Wilde (arXiv:2205.05736) derive the unconstrained capacities of general bosonic dephasing channels, not the present finite-energy parity optimum or singular asymptotic; their published formulation also uses a phase density. Arqand, Memarzadeh and Mancini (arXiv:2007.03897) study Gaussian diffusion in phase rather than binary \(0/\pi\) kicks. Wilde and Qi (arXiv:1609.01997) supply the established energy-constrained degradable-channel capacity theorem invoked in Step 1. The present contribution is the exact geometric-in-each-parity optimizer and its nonperturbative noise-endpoint behavior, not the background capacity or entropy theorems.

## Limitations

The theorem does not cover photon loss, general continuous phase distributions, adaptive classical assistance, hard per-block photon cutoffs, correlated channel uses, finite-block coding rates, or joint limits in which \(E\) varies with \(r\). The probabilistic channel has perfect noiseless even/odd Fock sectors at complete parity dephasing; the essential singularity measures the tiny incremental advantage of mixing those sectors at incomplete dephasing. Priority relative to any as-yet-unidentified special treatment of finite-energy binary parity-phase noise is not independently certified.

## References

1. A. Arqand and G. Smith, *No advantage from classical assistance for energy-constrained bosonic dephasing channels*, arXiv:2610.13854v1 (2026-10-09). https://arxiv.org/html/2610.13854v1
2. L. Lami and M. M. Wilde, *Exact solution for the quantum and private capacities of bosonic dephasing channels*, Nature Photonics 17, 525–530 (2023), arXiv:2205.05736. https://doi.org/10.1038/s41566-023-01190-4
3. A. Arqand, L. Memarzadeh and S. Mancini, *Quantum capacity of a bosonic dephasing channel*, Phys. Rev. A 102, 042413 (2020), arXiv:2007.03897. https://arxiv.org/abs/2007.03897
4. M. M. Wilde and H. Qi, *Energy-constrained private and quantum capacities of quantum channels*, IEEE Trans. Inf. Theory 64, 7802–7827 (2018), arXiv:1609.01997. https://arxiv.org/abs/1609.01997
