# Sharp observation-scale equivalence of curved and complementary triadic public-goods games

## Finding

Let a finite population of \(N\ge3\) binary-strategy agents play the normalized two- and three-person public-goods game defined below. Compare the triadic power benefit \(3\alpha r(S/3)^\gamma\) with its complementary, or all-cooperator-only, benefit \(3\alpha r\mathbf 1_{\{S=3\}}\). The same pair interactions, imitation partner rule and independent flip-mutation are used in both dynamics. Put \(q=2/3\), \(\theta=\max_i d_i^{(3)}/(d_i^{(2)}+d_i^{(3)})\), and
\[
\delta_\gamma=\frac32\alpha r\theta |1-2\mu|q^\gamma.
\]
For every \(\gamma>0\), their one-update transition kernels \(P_\gamma,P_\infty\) satisfy
\[
\sup_s\|P_\gamma(s,\cdot)-P_\infty(s,\cdot)\|_{\rm TV}\le\min\{1,\delta_\gamma\}.
\]
For the **entire state trajectory** over \(T\) updates from the same arbitrary initial distribution, the total-variation distance of path laws is at most \(\min\{1,T\delta_\gamma\}\). The bound becomes \(\min\{1,KT\delta_\gamma\}\) for the joint experiment consisting of \(K\) independent trajectories with common model-independent initial laws. Any equal-prior test based on that experiment has success probability at most \(\frac12+\frac12\min\{1,KT\delta_\gamma\}\). With strictly positive mutation \(0<\mu\le1/2\), a sharper **information-theoretic** statement holds. Put \(\eta_\gamma=\delta_\gamma/2\). Then the relative entropy of the joint law of \(K\) independent length-\(T\) trajectories satisfies
\[
D_{\mathrm{KL}}(\mathcal P_\gamma^{\otimes K}\|\mathcal P_\infty^{\otimes K})
\le\frac{KT\eta_\gamma^2}{\mu(1-\mu)},
\]
and total variation is at most \(\min\{1,\eta_\gamma\sqrt{KT/[2\mu(1-\mu)]}\}\). In particular, \(KT=o((3/2)^{2\gamma})\) forces the optimal model-selection advantage to vanish. For the explicit four-agent witness, \(K\) independent **one-step restarts from the same witness state** admit reliable discrimination whenever \(K(2/3)^{2\gamma}\to\infty\). Thus \((3/2)^{2\gamma}\) is the sharp statistical experiment-scale exponent for that natural repeated one-step observation protocol.

If \(0<\mu\le\frac12\), both finite-state chains have unique stationary laws \(\pi_\gamma,\pi_\infty\). With \(\varepsilon=(2\mu/N)^N\),
\[
\|\pi_\gamma-\pi_\infty\|_{\rm TV}
\le\min\left\{1,\frac{N\delta_\gamma}{\varepsilon}\right\}.
\]
The base \(2/3\) cannot be replaced by a smaller universal exponential base: an explicit four-agent two-triad hypergraph has a one-step row-distance \(\Theta((2/3)^\gamma)\) when \(0\le\mu<1/2\) and \(\alpha r>0\).

## Assumptions and scope

Take a fixed finite hypergraph \(H=(V,E_2,E_3)\), where \(|V|=N\ge3\), pair hyperedges contain two distinct vertices, and triad hyperedges contain three distinct vertices. Each vertex participates in at least one game. The sets may be empty separately. Strategies are \(s_i\in\{0,1\}\). Let \(d_i^{(a)}\) count incident \(a\)-person games and set \(d_i=d_i^{(2)}+d_i^{(3)}>0\). For fixed finite \(r>0\) and \(\alpha>0\), define
\[
U_i^\gamma(s)=\frac1{d_i}\left[
\sum_{\{i,j\}\in E_2}\left(\frac r2(s_i+s_j)-s_i\right)
+\sum_{\{i,j,k\}\in E_3}\left(3\alpha r\left(\frac{s_i+s_j+s_k}{3}\right)^\gamma-s_i\right)
\right].
\]
Here a displayed triad sum runs over incident triads, once each. Define \(U_i^\infty\) by replacing the triad power benefit by \(3\alpha r s_i s_j s_k\). The pair payoffs and all costs are otherwise unchanged.

At each elementary update, sample focal \(i\) uniformly from \(V\), then sample a *distinct* comparison vertex \(j\) from a fixed probability kernel \(Q_i(j)\) supported on the other participants in games involving \(i\). Assume \(Q\) depends on the hypergraph, not on strategies, payoffs or \(\gamma\). Since all vertices are active, a nonempty support exists. The focal agent first copies \(s_j\) with probability \(L(U_j-U_i)\), where \(L(z)=1/(1+e^{-z})\), otherwise it keeps \(s_i\); independently it then flips its resulting strategy with probability \(\mu\in[0,1/2]\). The two chains use the same \(Q,\mu,r,\alpha,H\), and their initial distributions are common. This specifies precisely the stochastic variant to which the bounds apply. The stationary claim excludes \(\mu=0\). The results do not require thermodynamic limits or independence among agents.

## Proof

**1. Exact local reward truncation.** For an integer cooperative count \(S\in\{0,1,2,3\}\), the power-vs-product triad benefit difference is exactly \(3\alpha r((S/3)^\gamma-\mathbf1_{\{S=3\}})\), a nonnegative quantity. It vanishes for \(S=0,3\), equals \(3\alpha r(1/3)^\gamma\) for \(S=1\), and equals \(3\alpha r(2/3)^\gamma\) for \(S=2\). Consequently, uniformly in configurations,
\[
0\le U_i^\gamma(s)-U_i^\infty(s)
\le3\alpha r\frac{d_i^{(3)}}{d_i}(2/3)^\gamma
\le3\alpha r\theta(2/3)^\gamma.
\]
The two payoff increments being nonnegative also yields the stronger difference estimate \(|(U_j^\gamma-U_i^\gamma)-(U_j^\infty-U_i^\infty)|\le 3\alpha r\theta q^\gamma\), **not the sum of two sup norms**. Indeed, both increments lie in the same interval \([0,3\alpha r\theta q^\gamma]\). This observation sharpens the constants below.

**2. One-update bound and path coupling.** The derivative \(L'(z)=L(z)(1-L(z))\) is at most \(1/4\). Holding a sampled pair \((i,j)\) fixed, imitation probabilities therefore differ by at most \((3/4)\alpha r\theta q^\gamma\). For \(s_i=s_j\), no disagreement is possible because both proposed next bits equal the current bit. For \(s_i\ne s_j\), applying flip mutation maps the probability of copying to a final-bit probability with derivative \(|1-2\mu|\). Hence, conditional on the same \((i,j)\), the two possible output distributions have total-variation distance at most
\[
\delta'_\gamma=\frac34\alpha r\theta |1-2\mu|q^\gamma.
\]
Mixing over the same payoff-independent focal and comparison distributions cannot increase total variation. Thus the **sharper bound** \(\delta'_\gamma\) holds for the one-step kernels and all subsequent displayed estimates may be strengthened by substituting \(\delta'_\gamma\) for \(\delta_\gamma\). In particular, the stated bound with \(\delta_\gamma=2\delta'_\gamma\) is valid.

Take a maximal coupling of the two one-step laws whenever their states agree; once a mismatch occurs, couple arbitrarily. Conditional on no earlier mismatch, its probability at the next update is at most \(\delta'_\gamma\), implying that the complete path laws have total-variation distance at most \(\min\{1,T\delta'_\gamma\}\), hence the claimed \(T\delta_\gamma\) bound. Product couplings for \(K\) independent paths give \(KT\delta_\gamma\). The optimal equal-prior binary testing success probability is exactly \((1+\|\mathcal P_\gamma-\mathcal P_\infty\|_{\rm TV})/2\), yielding the asserted operational bound.

**2a. Quadratic information bound.** If \(0<\mu\le1/2\), the output bit conditional on a sampled \((i,j)\) is Bernoulli with probability lying in \([\mu,1-\mu]\) under both models. The two probabilities differ by at most \(\eta_\gamma=(3/4)\alpha r\theta(1-2\mu)q^\gamma\). For Bernoulli laws the relative-entropy inequality \(D_{\mathrm{KL}}(\operatorname{Ber}(a)\|\operatorname{Ber}(b))\le(a-b)^2/[b(1-b)]\) follows from \(D_{\mathrm{KL}}\le\chi^2\). Since \(b(1-b)\ge\mu(1-\mu)\), the conditional KL divergence is at most \(\eta_\gamma^2/[\mu(1-\mu)]\). The law of \((i,j)\) is identical between models, so the chain rule for the augmented \((i,j,\text{next bit})\) and data processing give the same KL bound for the observed one-step transition kernel. Applying the Markov path chain rule from a common initial distribution gives \(D_{\mathrm{KL}}(\mathcal P_\gamma\|\mathcal P_\infty)\le T\eta_\gamma^2/[\mu(1-\mu)]\). \(K\) independent paths multiply KL by \(K\); Pinsker's inequality yields the displayed \(\sqrt{KT}\) total-variation bound. All KL laws have the same supports because mutation is positive.

**3. Minorization and stationary law.** Suppose \(0<\mu\le1/2\). For any initial state \(s\) and any target state \(t\), prescribe an update sequence visiting all \(N\) focal vertices in a fixed order. Its probability is \(N^{-N}\). Irrespective of the copying outcome, the chance that the post-mutation bit equals the specified target bit is at least \(\mu\). Therefore, for either kernel,
\[
P^N(s,t)\ge(\mu/N)^N.
\]
Summing these \(2^N\) bounds produces a common Doeblin minorization \(P^N(s,\cdot)\ge\varepsilon\nu(\cdot)\), where \(\nu\) is uniform on the \(2^N\) strategy profiles and \(\varepsilon=(2\mu/N)^N\). This proves irreducibility, aperiodicity, and uniqueness of the invariant probability for each chain. It also makes \(P_\infty^N\) contract differences of probability measures in total variation by at least a factor \(1-\varepsilon\).

The telescoping identity for Markov kernels and the one-step estimate give \(\sup_s\|P_\gamma^N(s,\cdot)-P_\infty^N(s,\cdot)\|_{\rm TV}\le N\delta_\gamma\). Comparing their invariant laws via
\[
\pi_\gamma-\pi_\infty
=\pi_\gamma(P_\gamma^N-P_\infty^N)
+(\pi_\gamma-\pi_\infty)P_\infty^N
\]
shows \(\varepsilon\|\pi_\gamma-\pi_\infty\|_{\rm TV}\le N\delta_\gamma\). The trivial upper bound one completes the proof.

**4. Witness showing the base is optimal across hypergraphs.** Take four vertices and exactly two triads \(\{1,2,3\},\{1,2,4\}\), with no pair games, and state \(s=(1,1,0,1)\). The first triad has cooperative count two and the second three. The payoff increments relative to the complementary model are \(\frac32\alpha r q^\gamma\) at vertices \(1,2\), \(3\alpha r q^\gamma\) at vertex \(3\), and zero at vertex \(4\). Vertex \(3\) can compare only with vertices \(1,2\), both cooperators. In the complementary game both comparison payoffs equal \((3\alpha r-2)/2\), while the focal payoff is zero; the two models' logistic arguments for these comparisons differ exactly by \(-\frac32\alpha r q^\gamma\). Therefore, the probability of the transition changing only vertex \(3\) from zero to one differs by
\[
\frac{1-2\mu}{4}
\left[L\left(\frac{3\alpha r-2}{2}\right)
-L\left(\frac{3\alpha r-2}{2}-\frac32\alpha r q^\gamma\right)\right]
= c\,q^\gamma+o(q^\gamma),
\]
where \(c=\frac38(1-2\mu)\alpha r L'((3\alpha r-2)/2)>0\) whenever \(\alpha r>0\) and \(\mu<1/2\). Thus a one-step row TV distance is bounded below by this positive order. No universal bound with a strictly smaller exponential base can hold in the stated class. This does not assert the prefactor in the upper bound is optimal.

For the statistical **converse**, independently restart the four-agent process in this one state, run just one update, and record the indicator of the transition changing the third vertex from defecting to cooperating. It is Bernoulli with respective probabilities \(p_\infty\in(0,1)\) and \(p_\gamma=p_\infty-cq^\gamma+o(q^\gamma)\). The KL/Pinsker bound above proves no equal-prior test on \(K\) such observations improves on chance asymptotically if \(Kq^{2\gamma}\to0\). Conversely, compare the sample proportion with \((p_\infty+p_\gamma)/2\); Chebyshev's inequality bounds each misclassification probability by \(1/[K(p_\infty-p_\gamma)^2]\). Thus the error tends to zero when \(Kq^{2\gamma}\to\infty\). This supplies a matching **exponential detection-scale classification** for the specified resettable experiment. It does not claim every uncontrolled continuous trajectory can achieve the same rate.

## Verification

The finite-state numerical sanity check in `verify.py` enumerates all \(16\) strategy states of the four-agent witness, constructs both Markov kernels, checks payoff and one-step bounds at several exponents, checks the KL quadratic inequality, verifies the \(N\)-step minorization, and checks convergence of the witness row-distance divided by \((2/3)^\gamma\). The executable returns `VERIFY_OK`. These finite checks corroborate signs and normalizations; the all-hypergraph theorem rests on the preceding inequalities rather than enumeration.

## Relationship to prior work

Tang and Rao introduce precisely the normalized power-payoff and complementary triad payoff, and report that both can generate qualitatively similar discontinuous cooperation transitions on simulated higher-order networks. Their formulas and computational conclusions motivate the question; the elementary payoff limit is already implicit in their definitions and is **not** claimed as new. The contribution here is a quantitative equivalence theorem for the entire finite-population Fermi-mutation process, including KL/Pinsker trajectory indistinguishability, a matching sharp sample-complexity exponent for resettable experiments, invariant-law control, and a sharp universal convergence base.

The nonlinear social-dilemma framework of Hauert, Michor, Nowak and Doebeli treats synergy, discounting and qualitative evolutionary outcomes but not these two specific hypergraph-game Markov kernels. Work on threshold public-goods games studies other threshold rewards. Classical finite-state Markov-chain sensitivity and Doeblin techniques underlie our argument; neither perturbation theory in general nor logistic Lipschitzness is claimed as new.

## Limitations

The results concern a fixed finite hypergraph and payoff-independent comparison sampling. The invariant-law bound requires positive independent flip mutation and deteriorates rapidly with \(N\); no uniform large-population statement or bound for metastable transition times is asserted. The source's numerical first-order-like transition is not here upgraded to a rigorous thermodynamic phase transition. Real implementations using a different mutation or partner-sampling convention must be checked against the explicitly stated update rule. The full space of unindexed prior work cannot be excluded.

## References

1. F. Tang and W. Rao, “Curvature of Collective Returns Reshapes the Cooperation Transitions in Higher-Order Public Goods Games,” *Axioms* **15**(8), 617 (2026), DOI: 10.3390/axioms15080617, published 19 August 2026. https://www.mdpi.com/2075-1680/15/8/617. Model Equations (1)–(4), Fermi imitation procedure and Section 6.
2. C. Hauert, F. Michor, M. A. Nowak and M. Doebeli, “Synergy and discounting of cooperation in social dilemmas,” *J. Theor. Biol.* **239** (2006), 195–202, DOI: 10.1016/j.jtbi.2005.08.040. https://pmc.ncbi.nlm.nih.gov/articles/PMC2891160/.
3. H. Wang et al., “Evolutionary dynamics of threshold public goods games on random hypergraphs,” *Chaos Solitons Fractals* **199** (2025), article 116582, DOI: 10.1016/j.chaos.2025.116582.
4. I. C. F. Ipsen and C. D. Meyer, “Uniform Stability of Markov Chains,” *SIAM J. Matrix Anal. Appl.* (1994), DOI: 10.1137/S0895479892237562 (general perturbation background).
