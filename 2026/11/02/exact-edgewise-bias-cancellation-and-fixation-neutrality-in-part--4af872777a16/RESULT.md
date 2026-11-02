# Exact edgewise bias cancellation and fixation neutrality in partisan voter networks

## Finding

**Theorem (the complete neutrality locus).** On any finite, connected, undirected, loopless weighted graph with at least two vertices and strictly positive symmetric weights, let agents update under the partisan copying rule below. The weighted plus-opinion density \(M\) is a martingale for **every** initial opinion configuration if and only if the sum of the intrinsic preferences at the endpoints of **every** edge is zero. These assignments are exactly the all-zero assignment on arbitrary graphs and, when the graph is bipartite, the assignments with the same preference \(h\) on one part and preference \(-h\) on the other. Under such an assignment, the all-plus fixation probability is exactly the initial weighted density \(M\), independently of preference magnitude.

If the graph is bipartite, \(0<h<1\), and every agent initially holds its locally preferred opinion, then both possible consensus outcomes have probability \(1/2\). The time \(T_1\) to the first change of opinion obeys
\[
\Pr(T_1=t)=\left(\frac{1+h}{2}\right)^{t-1}\frac{1-h}{2},\qquad t=1,2,\ldots,
\]
and therefore \(\mathbb E[T_1]=2/(1-h)\) and \(\mathbb E[\tau]\ge 2/(1-h)\) for the consensus time \(\tau\). The bound is sharp, with equality on the two-vertex graph. For fixed finite graphs, the consensus probabilities remain unchanged as \(h\) approaches one from below even though the lower bound on expected consensus time diverges.

## Assumptions and scope

Let \(G=(V,E,w)\) be a finite undirected connected graph without self-loops or multiple edges, \(n=|V|\ge2\), with \(w_{uv}=w_{vu}>0\) for each \(\{u,v\}\in E\). Set \(d_u=\sum_{v:\{u,v\}\in E}w_{uv}>0\) and \(D=\sum_{u\in V}d_u=2\sum_{e\in E}w_e\). A fixed preference \(b_u\in(-1,1)\) and current opinion \(\sigma_u\in\{-1,+1\}\) belong to each vertex. At each discrete update attempt, choose an updater \(u\) uniformly from \(V\), sample a neighbor \(v\) with probability \(w_{uv}/d_u\), and if \(\sigma_u\ne\sigma_v\), change \(\sigma_u\) to \(\sigma_v\) with probability \((1+\sigma_vb_u)/2\); otherwise leave the state unchanged. This is the fixed-preference partisan copying mechanism of Zimmaro–Contucci–Kertész, with a symmetric weighted-neighbor extension. Define \(X_u=(1+\sigma_u)/2\) and \(M(X)=D^{-1}\sum_ud_uX_u\). Let \(\tau\) be the first all-plus or all-minus consensus time.

The claim applies to arbitrary fixed preference vectors in \((-1,1)^V\); the alternating-preference condition is **not** assumed when establishing its necessity. Fixation neutrality means the stated martingale and all-plus absorption probability for all initial configurations, not identical sample paths or equal consensus-time distributions to the unbiased voter model. The strict preference range excludes zealots and ensures almost-sure absorption.

## Proof

**1. Exact drift identity.** Fix a discordant edge \(e=\{u,v\}\), and first suppose \(X_u=0\), \(X_v=1\). Choosing \(u\) and then \(v\) contributes \(w_{uv}(1+b_u)/(2nD)\) to the expected change in \(M\), because the update probability is \(w_{uv}(1+b_u)/(2nd_u)\) and the weighted-density change is \(d_u/D\). Choosing \(v\) and then \(u\) contributes \(-w_{uv}(1-b_v)/(2nD)\). The sum is \(w_{uv}(b_u+b_v)/(2nD)\). Reversing the opinions gives the same expression. Concordant edges contribute zero. Consequently, **for every configuration**,
\[
\mathbb E[M(X_{t+1})-M(X_t)\mid X_t]
=\frac{1}{2nD}\sum_{\{u,v\}\in E:\,X_u\ne X_v}w_{uv}(b_u+b_v).
\]

**2. Sharp necessity by cuts.** Write \(c_{uv}=w_{uv}(b_u+b_v)\), and let \(C(S)=\sum_{\{u,v\}\in\delta(S)}c_{uv}\) be the weighted cut sum for \(S\subseteq V\). If \(M\) is a martingale from every starting configuration, applying the drift identity to the configuration whose plus set is \(S\) gives \(C(S)=0\) for all subsets \(S\). For any edge \(\{u,v\}\), cancellation of the other edges yields
\[
C(\{u\})+C(\{v\})-C(\{u,v\})=2c_{uv}.
\]
The left side vanishes, so \(c_{uv}=0\) and, since \(w_{uv}>0\), \(b_u+b_v=0\). The converse follows immediately by substituting this condition into the drift identity.

**3. Graph-theoretic classification.** Along every path, the constraints imply alternating signs and equal absolute preference. Connectedness implies that a single starting value determines every other preference. On an odd cycle, returning to the initial vertex reverses its preference and forces that preference to be zero; hence every preference is zero. Otherwise the connected graph is bipartite and the only possibilities are a constant \(h\in(-1,1)\) on one part and \(-h\) on the other. The case \(h=0\) is included.

**4. Almost-sure absorption and fixation.** Since \(|b_u|<1\), every allowed copying of a discordant edge has strictly positive probability. From a nonconsensus configuration, selecting an agent already in the plus state and successively copying that opinion outward along a spanning tree produces all-plus consensus with positive probability in at most \(n-1\) opinion-changing attempts (and similarly for minus). Formally, specify at most \(n-1\) particular update attempts, with no moves at already-correct vertices, until consensus. Finiteness of the state space gives a common strictly positive lower bound on the probability of absorption within a fixed finite number of attempts from any nonabsorbing state. Iteration gives \(\Pr(\tau<\infty)=1\) and \(\mathbb E\tau<\infty\). The process \(M(X_{t\wedge\tau})\) is a bounded martingale. By bounded convergence, \(\mathbb E[M(X_\tau)]=M(X_0)\). At absorption, \(M(X_\tau)\) equals one or zero according as consensus is all-plus or all-minus. Thus
\[
\Pr(\text{all-plus consensus}\mid X_0)=\frac{\sum_ud_u X_u(0)}{D}.
\]

**5. Polarization and a sharp delay.** Suppose \(0<h<1\), \(V=V_+\sqcup V_-\) is the bipartition, preferences are \(+h\) on \(V_+\) and \(-h\) on \(V_-\), and the initial opinions agree with those preferences. By edgewise bipartiteness, \(\sum_{u\in V_+}d_u=\sum_{u\in V_-}d_u=\sum_{e\in E}w_e=D/2\), so \(M(X_0)=1/2\). Every sampled neighbor initially has the opposite opinion, and every proposed adoption conflicts with the updater's own preference. Therefore, at each attempt before the first flip the flip probability is exactly \((1-h)/2\); the state stays fixed after a failed attempt. This proves the displayed geometric law, the mean waiting time, and \(\tau\ge T_1\). On the two-vertex graph, the first flip is already consensus, giving equality. No claim is made for \(h=1\), at which the polarized initial state is absorbing and the optional-stopping conclusion fails.

## Verification

The independently constructed finite-state transition matrices in `verification/check.py` use exact rational arithmetic. For ten unweighted or nonuniformly weighted connected bipartite test graphs and two preference strengths, the script checks every configuration's drift equation and martingale property (456 configuration comparisons in total). It also solves 292 transient-state absorbing Markov equations and compares exact consensus probabilities to \(M\), verifies the polarized first-flip law, and exhibits a nonbipartite nonzero-drift contrast. Run with Python 3 and SymPy using `python verification/check.py`. Enumeration is finite supplementary evidence; the universal theorem follows from the five analytical proof steps above.

## Relationship to prior work

Zimmaro, Contucci and Kertész (2023) specify this fixed-preference microscopic update mechanism and analyze fully connected and modular interaction networks via deterministic mean-field and pair approximations, numerical simulations, and stability analysis. Those results motivate investigating the finite stochastic process, but do not state an exact cutwise martingale criterion for arbitrary weighted graphs or its sharp preference-dependent waiting law.

The classical voter literature already establishes weighted fixation for **unbiased** agents, including Sood and Redner's (2005) explicit complete-bipartite calculation. Hence the degree-weighted fixation law **at zero preference**, and its 50-50 polarized complete-bipartite special case, are prior results rather than claimed novelties. The present result is the extension to *nonzero, opposing fixed preferences* and its necessary-and-sufficient graph classification and sharp delay law. Masuda, Gibert and Redner (2010), Masuda and Redner (2011), and Borile, Maritan and Muñoz (2013) analyze intrinsically partisan or quenched-field voter models, principally mean-field, regular-lattice, or disorder effects, but their inspected statements do not imply this finite-network edgewise cancellation theorem. Absence of an indexed match is not a proof of global novelty.

## Limitations

The result relies on independent uniform choice of updater, symmetric strictly positive edge weights, the specified preference-sensitive adoption probability, two opinions, a fixed connected finite graph, and strictly subunit preferences. It does not classify the expected time to consensus beyond the exact first-flip law and the lower bound; it gives no asymptotic upper bound or mixing-time assertion. The theorem does not extend automatically to directed weights, adaptive graphs, zealots, media-driven updating, or other bias mechanisms. Existing literature may contain equivalent results under different terminology; independent validation remains outstanding.

## References

1. F. Zimmaro, P. Contucci, J. Kertész, *Voter-like Dynamics with Conflicting Preferences on Modular Networks*, arXiv:2303.09587 (first posted 2023-03-16); *Entropy* 25, 838 (2023), DOI:10.3390/e25060838. Original stochastic rule and mean-field/modular analyses.
2. V. Sood and S. Redner, *Voter Model on Heterogeneous Graphs*, arXiv:cond-mat/0412599; *Phys. Rev. Lett.* 94, 178701 (2005). Unbiased fixation on heterogeneous and complete-bipartite graphs.
3. N. Masuda, N. Gibert and S. Redner, *Heterogeneous Voter Models*, arXiv:1003.0768 (2010), *Phys. Rev. E* 82, 010103(R). Different conserved quantity in rate-heterogeneous voter dynamics; mean-field partisan model.
4. N. Masuda and S. Redner, *Can Partisan Voting Lead to Truth?*, arXiv:1012.2462; *J. Stat. Mech.* L02002 (2011). Partisan voter mean-field analysis and finite-network simulations.
5. C. Borile, A. Maritan and M. A. Muñoz, *The effect of quenched disorder in neutral theories*, arXiv:1304.0965 (2013). Voter dynamics with fixed local random preferences.
