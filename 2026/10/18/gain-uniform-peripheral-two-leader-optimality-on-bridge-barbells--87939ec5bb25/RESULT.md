# Gain-uniform peripheral two-leader optimality on bridge barbells

## Finding
Let \(B_m\), for an integer \(m\ge3\), be the graph formed from two vertex-disjoint copies of \(K_m\) by adding exactly one bridge edge between distinguished vertices (the *hubs*). Every other vertex is called *peripheral*. Equip all edges with unit conductance and let \(L_m\) denote the combinatorial Laplacian. For any gain \(\kappa>0\) and every two-element vertex set \(S\), put
\[
J_m(S;\kappa)=\operatorname{tr}\left(L_m+\kappa\operatorname{diag}(\mathbf1_S)\right)^{-1}.
\]
Then **all and only** the globally minimizing sets \(S\) consist of one peripheral vertex in each of the two cliques. In particular, neither bridge endpoint is ever an optimal equal-gain leader, for any finite positive gain.

The minimum is exactly
\[
\boxed{J_m^*(\kappa)=
\frac{2\big[\kappa^2(2m^2+5m-10)+\kappa(m^3+6m^2-4m)+m^3\big]}
{\kappa m\big[\kappa(m+4)+2m\big]}.}
\]
For a white-noise consensus model with independent unit-intensity disturbances, the total stationary variance is one half of this trace; the optimal placement sets are unchanged.

## Assumptions and scope
The two clique sizes are equal and at least three. All internal edges and the unique bridge have conductance exactly one. Leaders are two distinct vertices, each with the *same* finite gain \(\kappa>0\); all nonleaders have gain zero. The trace is defined because the grounded Laplacian is positive definite for every nonempty leader set on a connected graph. No conclusions about unequal gains, unequal clique sizes, non-unit edge weights, or more leaders are asserted.

## Proof
Each automorphism of \(B_m\) permutes peripheral vertices within a clique and may exchange the cliques. Hence two-element leader sets have exactly five orbits: opposite-clique peripheral/peripheral (\(PP_o\)); opposite-clique hub/peripheral (\(HP_o\)); the two hubs (\(HH\)); same-clique hub/peripheral (\(HP_s\)); and same-clique peripheral/peripheral (\(PP_s\)). The last type exists because \(m\ge3\).

For each orbit, partition the vertices of each clique into its singleton hub, its pinned peripheral vertices (if any), and its unpinned peripheral vertices (if any). Omit empty parts. On the subspace of vectors constant on each part, the matrix \(M=L_m+\kappa\operatorname{diag}(\mathbf1_S)\) is represented by an equitable quotient \(Q\). If part \(i\) has size \(s_i\), then for distinct parts \(i,j\), \(Q_{ij}=-s_j\) when all edges between the two parts exist, and \(Q_{ij}=0\) otherwise. The diagonal is the graph degree plus \(\kappa\) if pinned, minus the number \(s_i-1\) of same-part neighbors. Thus hub parts have degree \(m\), peripheral parts degree \(m-1\). Every peripheral part of size \(s_i>1\) also contributes a zero-sum eigenspace of multiplicity \(s_i-1\) with eigenvalue \(m\) (unpinned) or \(m+\kappa\) (pinned). Consequently
\[
J_m(S;\kappa)=\operatorname{tr}(Q^{-1})+
\sum_{i\;\text{peripheral part}}
\frac{s_i-1}{m+\kappa\mathbf1_{\{i\;\text{pinned}\}}}.
\]
This identity holds also when \(m=3\), with empty parts omitted. It follows directly from an invariant direct-sum decomposition, not a numerical approximation.

Set \(T=\kappa(m+4)+2m\) and \(U=\kappa(m+2)+2m\), and write \(J_0=J_m(PP_o;\kappa)\). Exact quotient inversion gives the stated formula for \(J_0\), together with the following four differences:
\[
\begin{aligned}
J_m(HP_o;\kappa)-J_0
&=\frac{\kappa[\kappa(m+2)+2m^2+2m+4]}{UT},\\[4pt]
J_m(HH;\kappa)-J_0
&=\frac{2\kappa[\kappa(m+2)+2m^2+2m+4]}{m(\kappa+2)T},\\[4pt]
J_m(HP_s;\kappa)-J_0
&=\frac{\kappa^2(2m^2+7m-2)+\kappa(2m^3+10m^2+2m+4)+2m^3}{2(\kappa+m)T},\\[4pt]
J_m(PP_s;\kappa)-J_0
&=\frac{\kappa^2(m^2+5m+5)+\kappa(m^3+6m^2+8m+2)+m^3+2m^2}{(\kappa+m)T}.
\end{aligned}
\]
Every displayed denominator is positive. For \(m\ge3\) and \(\kappa>0\), every numerator is strictly positive (including \(2m^2+7m-2>0\)). Therefore \(J_m(S;\kappa)>J_0\) for each of the four other orbit types, establishing both global optimality and complete strict equality classification. Every possible two-vertex set belongs to one of these five orbits. \(\square\)

## Verification
The standalone `verify.py` derives the five quotient trace identities symbolically over \(\mathbb Q(m,\kappa)\), verifies their factored differences, and independently constructs full grounded Laplacian matrices. Direct exact-rational full-matrix tests cover \(m\in\{3,4,5,6\}\) at \(\kappa\in\{1/3,1,7/2\}\), comparing every placement orbit with its symbolic formula. The symbolic identities and coefficient-sign argument—not the finite tests—establish the infinite-family theorem.

Run with `python verify.py` using Python 3 and SymPy. This script contains no data-file dependencies.

## Relationship to prior work
Lin, Fardad, and Jovanović introduce the noise-corrupted leader-selection trace-inverse objective and analyze general convex-relaxation methods. Fitch and Leonard obtain general formulas for two noisy leaders in terms of network centralities and solve certain path and cycle cases. Neither inspected result provides the displayed all-gain five-orbit classification for two bridge-joined cliques. A separate graph-theoretic result on zero-forcing polynomials of bridge barbells concerns a different invariant and does not imply the optimization claim.

## Limitations
This is a theorem for balanced unit-weight bridge barbells and two equal finite positive gains. It does not claim a general criterion for arbitrary bottleneck graphs or arbitrary graph weights. The quotient proof assumes nothing about numerical search quality. Although relevant primary full texts and a mathematical findings database were searched, a mathematically equivalent unindexed result may exist; this is an originality risk, not an additional mathematical premise.

## References
1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public version 2013-02-03), especially Sections II–III.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public version 2014-07-07), especially Sections II and V.
3. *Zero forcing polynomial of bridge barbells*, published mathematical finding (2026-10-04), opaque identifier `5431b532d7f2` (overlap comparator on the same graph, different invariant).
