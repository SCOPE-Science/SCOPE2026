# Pairwise Coextinction Laws Do Not Determine Matching Capacity: A Sharp Nine-Species Boundary

## Finding

**Theorem.** Consider any two finite, connected, simple bipartite networks \(G,H\), each with \(a\geq1\) labeled plants and \(b\geq1\) pollinators, and no isolated species. Independently delete every pollinator with the same probability \(q\in(0,1)\). A plant is lost when all of its adjacent pollinators are deleted. Suppose that the two networks have the same multiset of pollinator degrees and that every corresponding plant has the same loss probability and every corresponding pair of plants has the same joint-loss probability, for all \(q\in(0,1)\). Let \(C_G(q)\) denote the expected maximum bipartite matching size after the pollinator deletions, with assignments optimized separately for each survival outcome.

If \(a+b\leq8\), then \(C_G(q)=C_H(q)\) for all \(q\in[0,1]\). This bound is sharp: with four plants and five pollinators there are networks satisfying **all** these conditions—including equality of the degrees of each corresponding pollinator—such that for every individual surviving-pollinator subset \(S\),
\[
\nu(G[S])\leq\nu(H[S]),
\]
with strict inequality for seven of the 32 subsets. Their exact expected-capacity gap is
\[
\boxed{C_H(q)-C_G(q)=q(1-q)^2(3-3q+q^2)>0}\qquad(0<q<1).
\]
In particular, nine is the minimum total number of species at which first- and second-order plant-loss laws, together with pollinator degrees, fail to identify expected matching-based service capacity among connected networks.

## Assumptions and scope

Plants are permanently present; only pollinators are deleted. The underlying bipartite graph is simple and initially connected. A surviving pollinator serves at most one plant and a plant receives at most one service assignment in the model period. Maximum matching is recomputed after deletions. The model is an idealized **capacity-constrained allocation**, not a claim that real pollinators are limited to one plant. Loss probabilities concern the *topological* event that a plant has no surviving pollinator; they do not describe demographic extinction.

Pollinator survival events are independent and exchangeable, with survival probability \(1-q\). The hypothesis on first- and second-order loss laws is labeled on the plant side; the pollinator-degree condition is even weaker than matching labeled pollinator degrees.

## Proof

**1. What the pairwise loss laws record.** Let \(N_i\) be the pollinator-neighbor set of plant \(i\), and put \(d_i=|N_i|\), \(c_{ij}=|N_i\cap N_j|\). The plant-loss event is the deletion of every pollinator in \(N_i\), so
\[
\Pr(i\text{ lost})=q^{d_i},\qquad
\Pr(i,j\text{ both lost})=q^{d_i+d_j-c_{ij}}.
\]
Thus equality of these laws for all interior \(q\) is equivalent to equality of all labeled \(d_i\) and \(c_{ij}\). The additional hypothesis specifies the multiset of pollinator degrees.

**2. At most three plants.** With \(a\leq3\), the data determine the number of pollinators realizing each exact nonempty neighborhood among the plants. For \(a=3\), the number having all three plant neighbors equals the number of degree-three pollinators; each pair-only count is the corresponding \(c_{ij}\) minus this triple count; each singleton-only count follows by subtracting its pair-only counts and the triple count from \(d_i\). The cases \(a=1,2\) are easier. Since no pollinator is isolated, this exhausts its possible neighbor sets. Hence the incidence graph is determined up to a permutation of pollinators, and consequently so is its expected matching capacity, for every \(b\).

**3. The remaining networks with at most eight vertices.** Necessarily \(4\leq a\leq7\) and \(1\leq b\leq8-a\). The accompanying exact exhaustive verifier considers every labeled incidence matrix by choosing each nonzero row mask from \(\{1,\ldots,2^b-1\}\), then retains precisely the connected matrices. For each matrix it forms the signature
\[
\big((d_i)_{i=1}^{a},(c_{ij})_{1\leq i<j\leq a},\text{sorted pollinator degrees}\big).
\]
For each surviving pollinator set \(S\), it calculates \(\nu(G[S])\) by a complete dynamic program over sets of already matched pollinators. The vectors
\[
h_k(G)=\sum_{\substack{S\subseteq[b]\\|S|=k}}\nu(G[S]),\qquad 0\leq k\leq b,
\]
are identical for all connected matrices sharing each signature. The exhaustive code checks all 28 guild-size pairs with \(a,b\geq1\) and \(a+b\leq8\), including the analytic small-plant cases. In the largest \(4\times4\) case, 36,317 connected labeled matrices form 1,986 signature groups, and every repeated group has an identical capacity vector. This is a finite completeness proof: every binary incidence matrix under the stated size bound appears in the enumeration.

Since
\[
C_G(q)=\sum_{k=0}^{b}h_k(G)(1-q)^kq^{b-k},
\]
identical vectors imply identical expected capacity throughout \([0,1]\).

**4. An exact nine-species witness.** Label the plants \(1,2,3,4\) and pollinators \(a,b,c,d,e\). Specify neighborhoods of plants as
\[
\begin{aligned}
G:&\quad \{a,d,e\},\ \{b,c\},\ \{a,c\},\ \{a,b\},\\
H:&\quad \{b,c,e\},\ \{a,d\},\ \{a,c\},\ \{a,b\}.
\end{aligned}
\]
Both graphs are connected. The plant degrees are \((3,2,2,2)\), and the labeled pollinator degrees are \((3,2,2,1,1)\). The six labeled common-neighbor counts in lexicographic pair order are \((0,1,1,1,1,1)\) in both graphs. Thus the required individual and pairwise plant-loss laws coincide exactly.

Direct matching enumeration yields
\[
(h_0,\ldots,h_5)(G)=(0,5,19,27,17,4),\qquad
(h_0,\ldots,h_5)(H)=(0,5,20,30,20,4).
\]
More strongly, the difference \(\nu(H[S])-\nu(G[S])\) is one exactly when \(d,e\in S\) and \(S\cap\{a,b,c\}\) contains at most two pollinators, and is zero otherwise. There are \(1+3+3=7\) strictly improving subsets. Therefore
\[
\begin{aligned}
C_H(q)-C_G(q)
&=(1-q)^2q^3+3(1-q)^3q^2+3(1-q)^4q\\
&=q(1-q)^2(3-3q+q^2).
\end{aligned}
\]
The last factor is \(1+(1-q)+(1-q)^2\), which is positive throughout the stated open range. At \(q=1/2\), the respective expected capacities are \(9/4\) and \(79/32\), differing by \(7/32\). When every pollinator survives, **both** networks instead have maximum matching size four. This completes sharpness.

## Verification

Run `python3 verify.py` from the directory containing this document and the standalone verifier. The program uses integer bitsets and exhaustive state enumeration only; it requires Python 3 with no external packages. It enumerates each connected labeled bipartite network through eight total vertices, groups its labeled plant degrees, pairwise common-neighbor counts, and pollinator-degree multiset, and compares the exact expected-matching coefficient vectors. It separately enumerates all 32 survival states for both nine-species networks, checks their matching values, pointwise dominance, the seven strict states, and exact coefficient vectors.

The verified finite bound is exhaustive only through eight total vertices, as explicitly stated. The nine-species construction is a direct exact witness. Neither the code nor the theorem provides a classification of all larger networks.

## Relationship to prior work

Memmott, Waser, and Price (first public online appearance 6 December 2004) studied secondary plant loss under pollinator removals in ecological bipartite networks. Their plant-loss model motivates the first- and second-order laws here, but their study counts plants retaining at least one pollinator; it does not impose a one-pollinator/one-plant allocation cap or study maximum matching.

Bock and Rautenbach (2018), especially their Section 3, characterize achievable **static** matching numbers among bipartite realizations of prescribed degree sequences. That stronger general matching framework does not imply equality or inequality of the full rank profile after all subsets of pollinators are independently removed, much less this pairwise-loss-law separation and sharp finite threshold. Devoto and colleagues (2012) discuss functional complementarity and redundancy in ecological restoration; their accessible abstract provides additional application context rather than an exact matching-capacity theorem.

## Limitations

The result does not model pollinator visit frequencies, pollinator multi-plant activity, habitat feedback, imperfect interaction detection, or correlated species removal. It does not imply that any actual ecosystem of nine species exhibits this phenomenon. The sharpness assertion is restricted to connected binary networks, homogeneous independent pollinator deletion, and the exact pairwise information and matching-capacity definition above. Equivalence to an older formulation in transversal-matroid rank reliability or matching theory remains a bibliographic risk.

## References

1. Memmott, J., Waser, N. M., and Price, M. V. (2004). “Tolerance of pollination networks to species extinctions.” *Proceedings of the Royal Society B* 271, 2605–2611. DOI: 10.1098/rspb.2004.2909. Author-hosted full text: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf. Published online 2004-12-06.
2. Bock, F., and Rautenbach, D. (2018). “The matching number of tree and bipartite degree sequences.” arXiv:1808.09650, version first posted 2018-08-29. https://arxiv.org/abs/1808.09650.
3. Devoto, M., Bailey, S., Craze, P., and Memmott, J. (2012). “Understanding and planning ecological restoration of plant–pollinator networks.” *Ecology Letters* 15, 319–328. DOI: 10.1111/j.1461-0248.2012.01740.x. First online appearance 2012-01-18.
