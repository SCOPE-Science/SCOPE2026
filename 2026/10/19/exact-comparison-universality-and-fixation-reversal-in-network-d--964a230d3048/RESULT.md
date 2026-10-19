# Exact comparison universality and fixation reversal in network donation games

## Finding

Consider a finite connected undirected simple graph with at least three vertices. Let \(P\) be its row-stochastic simple-random-walk matrix and give each vertex an arbitrary real social-comparison susceptibility \(\lambda_i\). For the donation game with payoff \(u=-cx+bPx\), positive \(b,c\), and death–birth competition based on \(F_i=\exp[\delta(u_i+\lambda_i(Pu)_i)]\), define **universal scalar reducibility** to mean that a *single* real number \(s\), independent of the game parameters and configuration, makes the probability of every particular surviving neighbor replacing every dead vertex coincide with the ordinary donation-game death–birth rule having fitness \(\exp(\delta s u_i)\). This equality is required for every \(b,c,\delta>0\), every \(x\in\{0,1\}^n\), and every death site.

**Theorem.** Universal scalar reducibility holds precisely in the following, possibly overlapping, cases:

1. \(\lambda_i=0\) at every vertex, with \(s=1\), on any connected graph.
2. The graph is complete bipartite \(K_{a,d}\), \(a,d\ge1\), and \(\lambda_i\) is constant on each bipartition part, with the two part values allowed to differ; here \(s=1\).
3. The graph is complete \(K_n\), and \(\lambda_i\equiv\lambda\); here \(s=1-\lambda/(n-1)\).

In particular, comparison is **completely invisible at every selection strength** on the specified complete bipartite graphs, even when opposite-signed susceptibilities are assigned to the two communities. On a complete graph comparison exactly rescales or reverses payoff differences. The stated classification is for parent-choice probabilities, rather than merely comparing one particular fixation statistic.

**Fixation consequence.** On \(K_n\), let \(R=\exp[-\delta(c+b/(n-1))(1-\lambda/(n-1))]\), the cooperator-to-defector fitness ratio in each mixed state. Starting with one cooperator, the exact fixation probability is
\[
\rho_1(R)=\begin{cases}
\displaystyle \frac{n-1}{n}\,\frac{1-R^{-1}}{1-R^{-(n-1)}}&R\ne1,\\[4pt]
\displaystyle\frac1n &R=1.
\end{cases}
\]
Consequently \(\rho_1<1/n\) for \(\lambda<n-1\), \(\rho_1=1/n\) for \(\lambda=n-1\), and \(\rho_1>1/n\) for \(\lambda>n-1\). These are mathematical consequences of extending the stated fitness rule to arbitrary real susceptibilities; the high-susceptibility reversal is not an empirical claim. The classical death–birth fixation formula for a constant fitness ratio is prior mathematics; the result here is the exact identification of \(R\) with the social-comparison mechanism together with the graph-wide reducibility classification.

## Assumptions and scope

The graph \(G=(V,E)\) is connected, finite, undirected, unweighted and loopless with \(n=|V|\ge3\). Every degree is positive; \(P_{ij}=1/\deg(i)\) for \(ij\in E\) and zero otherwise. An individual's strategy \(x_i=1\) means cooperation; \(x_i=0\) means defection. Benefits and costs are strictly positive and are independent model parameters. At each update a uniformly chosen vertex dies, and **each neighboring vertex** competes to replace it according to its relative fitness calculated from the pre-update configuration. The same comparison profile and scalar \(s\) must work for all configurations, selection strengths, and donation parameters. The scalar \(s\) is allowed to be negative, thereby representing selection reversal. All expressions concern the stochastic finite-population model, not an asymptotic approximation.

## Proof

**Step 1: necessary and sufficient pairwise identity.** Fix a dying vertex \(j\) and two distinct neighbors \(i,k\in N(j)\). Equality of the two positive softmax probabilities in the original model and the scalar-payoff model implies equality of their fitness ratios. Taking logarithms and cancelling the arbitrary positive \(\delta\), one gets
\[
\left((1-s)(e_i-e_k)^\mathsf{T}+\lambda_i P_{i\cdot}-\lambda_k P_{k\cdot}\right)\,(-cx+bPx)=0.
\]
For every binary \(x\), this holds for all positive \(b,c\) separately. The coefficient of \(c\) vanishes for each coordinate vector \(x=e_v\); therefore
\[
\boxed{\lambda_iP_{i\cdot}-\lambda_kP_{k\cdot}=(s-1)(e_i-e_k)^\mathsf{T}}\tag{1}
\]
for every pair with a common neighbor. Conversely, (1) implies equality of all softmax ratios within each neighborhood, so it is sufficient. The independent benefit term then vanishes automatically because the matrix row multiplying the payoff is zero.

**Step 2: nontrivial rescaling forces a complete graph.** Suppose \(s\ne1\). If a common-neighbor pair \(i,k\) were nonadjacent, then the \(i\)-coordinate on the left of (1) would vanish, since \(P_{ii}=P_{ki}=0\), but the right would equal \(s-1\ne0\). Thus any two vertices sharing a neighbor are adjacent. A connected noncomplete graph contains an induced path on three vertices, whose endpoints are a nonadjacent common-neighbor pair. Therefore \(G=K_n\). In that graph every distinct pair has a third common neighbor \(j\), and the \(j\)-coordinate of (1) forces \(\lambda_i=\lambda_k\). Writing the common value \(\lambda\), use \(P_{ik}=1/(n-1)\) and \(P_{ii}=0\) in (1) to obtain \(s=1-\lambda/(n-1)\). This also directly verifies (1) on \(K_n\), for all real \(\lambda\).

**Step 3: invisible comparison.** Now suppose \(s=1\). Summing (1) over all coordinates, using the row sums of \(P\), gives \(\lambda_i=\lambda_k\) for any vertices having a common neighbor. Hence susceptibilities are constant on the connected components of the *common-neighbor graph*, whose edges join vertices having a common neighbor. Those components are the even-walk classes of the original connected graph: there is one if \(G\) is nonbipartite, and exactly the two bipartition parts if \(G\) is bipartite. In the nonbipartite case all susceptibilities equal a constant \(\lambda\). A nonzero constant together with (1) would make all rows of \(P\) equal (every pair is connected by a chain of common-neighbor pairs). Identical rows of a loopless stochastic matrix are impossible: their entry in column \(j\) would have to equal \(P_{jj}=0\) for all \(j\), contradicting row sum one. Therefore \(\lambda=0\).

If \(G\) is bipartite, susceptibility is constant within each side. If it vanishes everywhere we are in case 1. Otherwise choose a side with a nonzero constant. Equation (1) forces all \(P\)-rows on that side to be identical, hence all vertices on that side have exactly the same neighbor set (the row support). Connectedness implies that every vertex in the opposite side is adjacent to every vertex in the chosen side: indeed every opposite-side vertex has a neighbor there and that vertex shares the common support. This is precisely \(K_{a,d}\). Conversely on any \(K_{a,d}\), all vertices on one part share the same neighbor-payoff mean, and each dying vertex's competitors belong to the same part and have the same susceptibility. Their comparison offsets cancel in every ratio, establishing (1) with \(s=1\), even if the two part susceptibilities differ.

**Step 4: fixation calculation and sharp sign change on a clique.** A cooperator in a configuration containing \(k\) cooperators receives \(u_C=-c+b(k-1)/(n-1)\), whereas a defector receives \(u_D=bk/(n-1)\), so \(u_C-u_D=-c-b/(n-1)\) independent of \(k\). From Step 2 the effective cooperator-to-defector relative fitness is the same constant \(R\) in every mixed state. Let \(q_k^+\) and \(q_k^-\) denote the one-step probabilities of raising and lowering the cooperator count. Direct death–birth counting gives
\[
q_k^+=\frac{n-k}{n}\frac{kR}{kR+n-k-1},\qquad
q_k^-=\frac{k}{n}\frac{n-k}{(k-1)R+n-k}.
\]
Then the ratio telescopes across states:
\[
\prod_{k=1}^{j}\frac{q_k^-}{q_k^+}=\frac{n-1+j(R-1)}{(n-1)R^j},\qquad 1\le j\le n-1.
\]
The standard birth–death absorption identity \(\rho_1^{-1}=1+\sum_{j=1}^{n-1}\prod_{k=1}^j(q_k^-/q_k^+)\) yields the stated formula by summing a geometric series (and by continuity at \(R=1\)). Each mixed-state transition ratio \(q_k^-/q_k^+\) strictly decreases with \(R\), so \(\rho_1\) strictly increases with \(R\). The sign claims follow from \(R\gtreqless1\) exactly when \(\lambda\gtreqless n-1\).

**Exact witnesses.** On \(K_{2,3}\), susceptibilities \(7\) on one part and \(-3/2\) on the other leave all parent probabilities unchanged at every selection strength. On \(K_4\), taking \(b=3\), \(c=1\), \(\delta=\log2\), \(\lambda=9/2\) gives \(R=2\) and \(\rho_1=3/7>1/4\). Deleting an edge from \(K_{2,2}\) yields the path of four vertices: with \(b=2\), \(c=1\), \(x=(1,0,0,0)\), and uniform \(\lambda=1\), the competitor comparison contribution at a death in the second vertex differs by \(1/2\), so comparison is no longer invisible. Each witness is within the theorem's stated domain.

## Verification

The standalone `verify.py` uses exact Python rational arithmetic. It enumerates all connected labeled simple graphs on up to five vertices, verifying that the dimension of the comparison-invisible profile space is two for complete bipartite graphs and zero otherwise; this concerns \(\lambda\)-profiles with \(s=1\). It independently checks the death–birth fixation identity and sign for 54 exact parameter instances, all 160 replacement neighborhoods across the 32 binary states on a weighted-susceptibility \(K_{2,3}\) example, and the path counterexample. These are finite corroborations; the proof in Steps 1–4 establishes the all-graph, all-configuration statements.

To reproduce, use a standard Python 3 interpreter: `python verify.py`. No external Python packages are needed.

## Relationship to prior work

Xiong, Li, Kurths, Szolnoki and Feng (arXiv:2609.39012, first publicly posted 30 September 2026; later Communications Physics article) introduced the social-comparison fitness and death–birth model, and investigated weak selection, critical benefit-to-cost ratios, heterogeneous susceptibilities, and example networks. Their original derivations are assumed rather than claimed as new. The present result studies exact, all-intensity parent-choice equivalence on **every** connected unweighted graph and derives a topology classification. In particular, a complete bipartite network makes some nonzero, heterogeneous comparison profiles dynamically indistinguishable from no comparison, despite effects reported on other network families.

The finite death–birth fixation formula for an arbitrary fixed fitness ratio on a complete graph is classical and is not claimed to be a new fixation formula (compare Tkadlec et al., 2020). What is identified here is the exact effective ratio produced by this comparison fitness, including its neutral and selection-reversal thresholds. The common-neighbor and even-walk graph facts are standard; the mathematical contribution is the complete model-specific equivalence classification and its exact evolutionary consequence.

## Limitations

The classification is of equality of *individual parent probabilities for all possible games and states*. Other graphs or profiles might produce an equal fixation probability for one chosen \(b,c,\delta\) without satisfying that stronger universal definition. Only connected, unweighted, undirected, loopless graphs are treated. Large positive susceptibility is permitted by the mathematical fitness rule but is not asserted to be behaviorally realistic, nor necessarily included in optimization bounds of the motivating article. No stochastic-environment variability, empirical behavioral validity, or uniqueness in the entire literature is claimed. The originality comparison could miss unindexed equivalents.

## References

1. X. Xiong, Q. Li, J. Kurths, A. Szolnoki, M. Feng, *Social comparison shapes the evolution of cooperation in structured populations*, arXiv:2609.39012 (first posted 2026-09-30), Communications Physics (2026), DOI: 10.1038/s42005-026-02899-8.
2. J. Tkadlec, A. Pavlogiannis, K. Chatterjee and M. A. Nowak, *Limits on amplifiers of natural selection under death-Birth updating*, PLOS Computational Biology (2020), DOI: 10.1371/journal.pcbi.1007494; classical complete-graph formula.
3. A. McAvoy and B. Allen, *Fixation probabilities in evolutionary dynamics under weak selection*, Journal of Mathematical Biology (2021), DOI: 10.1007/s00285-021-01568-4.
