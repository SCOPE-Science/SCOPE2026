# A universal one-crossing law for pairwise protection in unrooted phylogenetic diversity

## Finding

Consider a finite unrooted phylogenetic tree with at least three taxon-labelled leaves and strictly positive edge lengths. Extinctions of different taxa are independent, but risks need not be identical. Suppose each taxon's extinction probability \(\varepsilon_i(t)\) is continuous, strictly increasing in a common risk-severity parameter \(t\in(0,1)\), and approaches zero and one at the respective endpoints. Guaranteed protection of a taxon replaces its extinction probability by zero. The benefit of protecting a pair jointly, minus the sum of their individual benefits, changes sign **exactly once** as severity rises: from negative (substitutability) to positive (complementarity). No ultrametric, binary branching, differentiability, or identical-risk hypothesis is needed.

More precisely, let \(X\) be the taxon set, and let \(F_t(S)\) be expected *unrooted* phylogenetic diversity when every taxon in \(S\subseteq X\) survives and each other taxon independently becomes extinct with probability \(\varepsilon_i(t)\). For distinct \(x,y\in X\), define
\[
 H_{xy}(t)=F_t(\{x,y\})-F_t(\{x\})-F_t(\{y\})+F_t(\varnothing).
\]
Let \(P_{xy}\) denote the edge path joining \(x\) and \(y\), and for any edge \(e\notin P_{xy}\), let \(B_e\) be the leaf set on the side of \(e\) that contains neither \(x\) nor \(y\). Writing \(\ell_e>0\) for edge length, the exact identity is
\[
 \boxed{H_{xy}(t)=Q(t)\left(\sum_{e\in E(T)}\ell_e-\sum_{e\notin P_{xy}}\frac{\ell_e}{\prod_{j\in B_e}\varepsilon_j(t)}\right),\qquad Q(t)=\prod_{j\in X}\varepsilon_j(t).}
\]
The factor in parentheses is continuous and strictly increasing from \(-\infty\) to the positive distance \(d_T(x,y)\). Thus a unique \(t_*\in(0,1)\) satisfies \(H_{xy}(t_*)=0\); it is strictly negative below and strictly positive above \(t_*\).

An immediate structural contrast is that once *any* species is already guaranteed protected, the expected unrooted diversity objective is monotone submodular in subsequently protected taxa. That anchored coverage property is a standard-type consequence of the edge representation and is not separately asserted as a new result.

## Assumptions and scope

The tree \(T\) is finite and connected, with leaves precisely the taxa \(X\), where \(|X|\ge3\). Internal vertices may have any degree at least three; subdividing edges is harmless. Every edge has a strictly positive finite length \(\ell_e\). Unrooted \(\operatorname{PD}(R)\) is the sum of lengths of edges in the minimal subtree joining \(R\) for \(|R|\ge2\), and by convention \(\operatorname{PD}(R)=0\) if \(|R|\le1\). In particular, this is *not* rooted diversity with a permanently surviving root.

For each \(t\in(0,1)\), each unprotected species \(i\) survives with probability \(1-\varepsilon_i(t)\) independently of all others. Each \(\varepsilon_i:(0,1)\to(0,1)\) is continuous and strictly increasing, and \(\lim_{t\downarrow0}\varepsilon_i(t)=0\), \(\lim_{t\uparrow1}\varepsilon_i(t)=1\). Protected species survive with probability one. Every fixed, ordered pair \(x\ne y\) is covered, without assuming a specific risk law or tied risks across species. No independence across values of \(t\) is required, since only their marginal distributions enter.

For precisely two leaves the interaction is always positive: the sole phylogenetic path is present if and only if both survive, so \(H_{xy}(t)=d_T(x,y)\varepsilon_x(t)\varepsilon_y(t)>0\). The three-taxon minimum in the theorem is therefore genuine. The theorem does not address correlated extinctions, nonmonotone individual risks, or a parameter interval that fails to cover the full near-zero through near-one severity range.

## Proof

**Step 1: Edge-event formula.** Removing any edge \(e\) partitions \(X\) into two nonempty sides \(A_e\) and \(B_e\). An edge belongs to the unrooted diversity subtree of the surviving taxon set exactly when at least one species survives on *each* side. For a forced-survivor set \(S\), define
\[
 q_A(S,t)=\begin{cases}0,&S\cap A_e\ne\varnothing,\\ \prod_{j\in A_e}\varepsilon_j(t),&S\cap A_e=\varnothing,\end{cases}
\]
and similarly for \(q_B(S,t)\). Independence gives
\[
 F_t(S)=\sum_{e\in E(T)}\ell_e[1-q_A(S,t)][1-q_B(S,t)]. \tag{1}
\]
This identity includes \(S=\varnothing\), and correctly yields zero unrooted diversity when no pair of taxa survives.

**Step 2: Exact signed second difference.** Fix \(x\ne y\) and one edge \(e\), and write \(Q_A=\prod_{i\in A_e}\varepsilon_i(t)\), \(Q_B=\prod_{i\in B_e}\varepsilon_i(t)\), so \(Q_AQ_B=Q(t)\). If \(e\in P_{xy}\), then \(x,y\) are on opposite sides and the second difference across the four forced-survivor sets is
\[
 1-(1-Q_A)-(1-Q_B)+(1-Q_A)(1-Q_B)=Q_AQ_B=Q(t).
\]
If \(e\notin P_{xy}\), both \(x,y\) lie on the same side, say \(A_e\). Then the four-term second difference is
\[
 (1-Q_B)-(1-Q_B)-(1-Q_B)+(1-Q_A)(1-Q_B)
 =-Q_A(1-Q_B)=Q(t)-\frac{Q(t)}{Q_B}.
\]
The away side \(B_e\) is exactly the \(B_e\) specified in the finding. Multiplying by \(\ell_e\) and summing over all edges proves the boxed identity.

**Step 3: Strict one-crossing.** Divide by the positive \(Q(t)\) and set
\[
 G(t)=\frac{H_{xy}(t)}{Q(t)}=L-\sum_{e\notin P_{xy}}\frac{\ell_e}{Q_{B_e}(t)},
 \qquad L=\sum_{e\in E(T)}\ell_e,
\]
where \(Q_{B_e}(t)=\prod_{j\in B_e}\varepsilon_j(t)\). Every \(B_e\) is nonempty, so each \(Q_{B_e}(t)\) is continuous and strictly increasing. Therefore each negative reciprocal term is strictly increasing. Since \(|X|\ge3\), a third taxon branches away from \(P_{xy}\), so at least one off-path edge exists. Consequently \(G\) is continuous and strictly increasing.

When \(t\downarrow0\), each \(Q_{B_e}(t)\to0\), and at least one positive-length reciprocal term diverges, giving \(G(t)\to-\infty\). When \(t\uparrow1\), every \(Q_{B_e}(t)\to1\), whence
\[
 \lim_{t\uparrow1}G(t)=L-\sum_{e\notin P_{xy}}\ell_e
 =\sum_{e\in P_{xy}}\ell_e=d_T(x,y)>0.
\]
The intermediate value theorem and strict monotonicity give a unique root \(t_*\), and \(Q(t)>0\) transfers the sign to \(H_{xy}(t)\). This is a proof for all real parameter values, not an inference from numerical sampling.

**Step 4: Anchored marginal property.** Fix any taxon \(a\) that is guaranteed to survive. Orient every edge away from the side containing \(a\), and denote the opposite taxon set by \(C_e\). For any additional protected subset \(U\subseteq X\setminus\{a\}\), the expected contribution of edge \(e\) is
\[
 \ell_e\left[1-\mathbf{1}_{\{U\cap C_e=\varnothing\}}
                  \prod_{i\in C_e}\varepsilon_i(t)\right].
\]
It is a weighted coverage function of \(U\) plus a constant, hence monotone submodular. Thus every second difference of protection effects *conditioned on an already protected anchor* is nonpositive for every fixed \(t\). This explains why the positive pair interaction proved above is specific to the initially unanchored unrooted objective.

**Step 5: Sharp example.** For the three-leaf unrooted unit-edge star, take \(x=1,y=2\) and equal extinction probabilities \(q\). The path length between \(x,y\) is two, while the unique off-path edge has away set \(\{3\}\). Hence
\[
 H_{12}(q)=q^3\left(3-\frac1q\right)=q^2(3q-1).
\]
The unique threshold is \(q_*=1/3\); at \(q=1/4\) the interaction is \(-1/64\), while at \(q=1/2\) it is \(1/8\). All signs and equalities are exact.

## Verification

The accompanying standalone Python 3 program `verify_unrooted_pd.py` requires only the standard library. Run `python3 verify_unrooted_pd.py`. It independently enumerates every possible set of naturally surviving taxa on a three-leaf star and a non-ultrametric five-leaf binary tree, with three different rational extinction profiles per tree. The program checks 120 forced-protection configurations against the edge formula, 39 pairwise interaction identities against direct state enumeration, and 369 anchored submodularity inequalities. It also checks the exact three-leaf threshold, the rational values on opposite sides, and normalized monotonicity for a heterogeneous increasing family on a five-leaf tree.

A successful run prints:

`VERIFY_OK edge_probabilities=120 pair_hessians=39 anchored_margins=369 homogeneous_three_leaf_threshold=1/3 heterogeneous_normalized_increase=PASS`

These finite computations only check the stated algebra on test instances. The universal sign and uniqueness conclusions are established by Steps 1–3, not by finite enumeration.

## Relationship to prior work

Steel (2005) established foundational greedy optimization results for deterministic unrooted phylogenetic diversity; it neither studies random extinction nor two-protection interactions. Steel, Mimoto and Mooers (2007), especially their Theorem 3.2 and its appendix proof, derive exact single-taxon marginal expected unrooted diversity under arbitrary independent heterogeneous extinction probabilities. Their theorem supplies the underlying first-order edge-product identity; the present second-difference formula can be derived from it and is not claimed as an independent discovery of the first-order formula. The additional statement assessed here is the uniform **strict, exactly-one sign reversal for every pair along every complete coordinatewise increasing extinction-risk trajectory**, with an explicit boundary at two taxa and the anchored-submodularity contrast. The examined source develops HED/HEDGE single-species indices, not this parameterized pairwise sign theorem.

Hartmann and Steel (2006) study the Noah's Ark problem with a rooted diversity objective and a deterministic root. Its monotonicity and coverage arguments do not entail the positive high-risk interaction of two initially unprotected taxa under the *unrooted* objective. Subsequent complementary-subset and conservation-prioritization work, including Jensen et al. (2016), motivates selecting species jointly. Its complete text was not accessible in this inspection, so possible prior coverage of the present exact second-difference or global one-crossing result remains a risk. The adjacent rooted species-priority problem concerns single-protection optimization and is not the same pairwise statement.

## Limitations

No universal switch is asserted for correlated extinctions or risk paths where some species' extinction probabilities decrease as others increase. A restricted range of severities may show no crossover even when all risks are monotone. The theorem does not incorporate ecological feedback, uncertain tree structure, nonzero protection failure, economic costs, or optimal multi-species budgets. Its two-protection interaction does not by itself determine the best individual conservation action. The algebra is a deterministic consequence of the independent-risk model and requires no claim of an empirically observed transition.

## References

1. Steel, M. (2005). *Phylogenetic Diversity and the Greedy Algorithm*. Systematic Biology 54(4), 527–529. DOI: 10.1080/10635150590947023. First verified publication date: 2005-08-01.
2. Steel, M., Mimoto, A., and Mooers, A. Ø. (2007). *Hedging Our Bets: The Expected Contribution of Species to Future Phylogenetic Diversity*. Evolutionary Bioinformatics 3. DOI: 10.1177/117693430700300024. Especially Theorems 3.2 and 4.1 and the appendix.
3. Hartmann, K., and Steel, M. (2006). *Maximizing Phylogenetic Diversity in Biodiversity Conservation: Greedy Solutions to the Noah's Ark Problem*. Systematic Biology. DOI: 10.1080/10635150600873876.
4. Mooers, A. Ø., Faith, D. P., and Maddison, W. P. (2008). *Converting Endangered Species Categories to Probabilities of Extinction for Phylogenetic Conservation Prioritization*. PLoS ONE. DOI: 10.1371/journal.pone.0003700.
5. Jensen, E. L., Mooers, A. Ø., Caccone, A., and Russello, M. A. (2016). *I-HEDGE: Determining the Optimum Complementary Sets of Taxa for Conservation Using Evolutionary Isolation*. PeerJ 4:e2350. DOI: 10.7717/peerj.2350.
