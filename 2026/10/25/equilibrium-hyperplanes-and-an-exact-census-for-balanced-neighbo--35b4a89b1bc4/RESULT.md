# Equilibrium hyperplanes and an exact census for balanced-neighbor swap games on complete multipartite networks

## Finding
Consider two types of agents occupying every vertex of the equal-part complete multipartite graph \(K_{m,\ldots,m}\), with \(h\ge2\) parts of size \(m\ge2\). Each agent strictly prefers an **open neighborhood** containing one-half agents of the opposite type: utility is \(-|2q-1|\), where \(q\) is the proportion of its neighbors of the opposite type. A swap requires both agents to strictly improve.

Let \(r_i\) be the number of red agents in part \(i\), and let \(R=\sum_{i=1}^{h}r_i\). A profitable swap is available between parts \(i\ne j\), with red moving from \(i\) to \(j\), **if and only if**
\[
r_i-r_j\ge2,\qquad r_i+r_j=2R-(h-1)m.\tag{1}
\]
Swaps within a part and swaps between same-colored agents are never profitable for both. Consequently, a placement is a pure swap equilibrium exactly when no ordered pair satisfies (1). Moreover \(\sum_i r_i^2\) strictly decreases by at least \(2\) under every profitable swap, so every improvement path has at most \(\lfloor hm^2/2\rfloor\) swaps.

For **three parts**, write \(N_m\) for the total number of equilibrium binary colorings (with all vertices labeled), and define
\[
\begin{aligned}
A_m&=\sum_{t=0}^m\binom mt\binom{2m}{2t},\\
B_m&=\sum_{t=0}^m\binom mt^3,\\
J_m&=\sum_{\substack{0\le t\le m\\2t\ne m}}\binom mt^2\binom m{2m-3t},
\end{aligned}
\]
where out-of-range binomial coefficients are zero. Then
\[
\boxed{N_m=2^{3m}-3(A_m-B_m-J_m).}\tag{2}
\]
For uniformly independent red/blue assignments to the \(3m\) vertices,
\[
\boxed{\Pr(\text{not an equilibrium})=\sqrt{\frac3{\pi m}}+O(m^{-1})\quad(m\longrightarrow\infty).}\tag{3}
\]
Thus almost all placements are equilibria even though every sufficiently large instance has many non-equilibrium placements.

## Assumptions and scope
The network is finite, simple, undirected, fully occupied, and complete between parts but edgeless within each part. Equal part sizes are essential to the stated simple criterion. There are exactly two agent types, with arbitrary fixed total number of each. Each agent observes *only its neighbors*, not itself, and has the same strictly symmetric single-peaked utility at a half-and-half neighbor mix, \(u(q)=-|2q-1|\). Swaps may involve any two vertices and occur only if both participating agents strictly gain. The counting results regard vertex colorings, not distinguishable permutations of individual agents of the same type. Equations (2)--(3) concern \(h=3\), while (1) and the convergence bound hold for all integers \(h,m\ge2\).

## Proof
Let \(d=(h-1)m\), \(s=2R-d\), and \(a_i=s-2r_i\). The signed difference between the proportions of red and blue neighbors of a vertex in part \(i\) is \(a_i/d\). The absolute distance of either color's *opposite-color neighborhood proportion* from one-half is therefore \(|a_i|/(2d)\). A red agent in part \(i\) and a blue agent in part \(j\) exchange locations, changing \(r_i\) to \(r_i-1\) and \(r_j\) to \(r_j+1\). Their two strict utility improvements are exactly
\[
|a_j-2|<|a_i|,\qquad |a_i+2|<|a_j|.\tag{4}
\]
Put \(x=r_i-r_j\), so \(a_j=a_i+2x\). If \(x=1\), both comparisons are equalities; if \(x\le0\), squaring the two inequalities imposes incompatible bounds. If \(x\ge2\), squaring and factoring gives
\[
-x-1<a_i<1-x.
\]
Because \(a_i\) is an integer, this means \(a_i=-x\); substituting \(a_i=s-2r_i\) gives \(s=r_i+r_j\). Conversely, for \(x\ge2\) and \(s=r_i+r_j\), both inequalities in (4) hold strictly. These conditions guarantee that a red vertex exists in part \(i\) and a blue vertex exists in part \(j\). Opposite-color swaps within a part leave both agents' neighbor-color proportions unchanged. A same-color swap leaves the coloring unchanged and merely interchanges two agents' old utilities, so it cannot help both. This proves (1).

A profitable red-from-\(i\) to-\(j\) swap changes the integer potential \(\Phi=\sum_k r_k^2\) by
\[
\Phi_{\mathrm{new}}-\Phi_{\mathrm{old}}
=(r_i-1)^2+(r_j+1)^2-r_i^2-r_j^2
=-2(r_i-r_j-1)\le-2.
\]
Since \(0\le\Phi\le hm^2\), no path has more than \(\lfloor hm^2/2\rfloor\) swaps.

For \(h=3\), denote by \(E_{ij}\) the event that the unordered pair of parts \(\{i,j\}\) admits some profitable swap. By (1), with \(k\) the third part, this is precisely
\[
r_i+r_j+2r_k=2m,\qquad |r_i-r_j|\ge2.\tag{5}
\]
For independent fair vertex colors, the counts \(r_1,r_2,r_3\) are independent \(\operatorname{Bin}(m,1/2)\) variables. Fixing \(r_k=m-t\), Vandermonde's identity shows that the number of vertex colorings satisfying the equality in (5) is \(A_m\); those additionally satisfying \(r_i=r_j\) number \(B_m\). Since the equality forces \(r_i-r_j\) even, excluding \(r_i=r_j\) is exactly the condition \(|r_i-r_j|\ge2\). Hence \(|E_{ij}|=A_m-B_m\).

Two distinct pair events, say \(E_{12}\) and \(E_{13}\), force \(r_2=r_3=t\) and \(r_1=2m-3t\); their strict inequalities hold exactly when \(2t\ne m\). This overlap has \(J_m\) vertex colorings. All three pair events cannot occur together: the pairwise equalities would force \(r_1=r_2=r_3\), contradicting the strict count differences. Inclusion--exclusion over the three pairs yields (2).

For (3), \(r_i+r_j\) has law \(U\sim\operatorname{Bin}(2m,1/2)\), independent of \(V=r_k\sim\operatorname{Bin}(m,1/2)\). The equality in (5) is \(U+2V=2m\); this integer-valued sum has mean \(2m\), variance \(3m/2\), and lattice span one. The lattice local central limit theorem gives
\[
\Pr(U+2V=2m)=\frac1{\sqrt{3\pi m}}+O(m^{-1}).
\]
The excluded equality event \(r_i=r_j\) imposes a second independent binomial constraint and has probability \(O(m^{-1})\), using the bound \(\max_t\Pr(\operatorname{Bin}(m,1/2)=t)=O(m^{-1/2})\). The same bound shows that the intersection of two distinct pair events has probability \(O(m^{-1})\): for a shared-index pair, the constraints set \(r_j=r_k=t\) and determine \(r_i=2m-3t\); sum the resulting products of three binomial point masses. As the triple intersection is empty, inclusion--exclusion gives \(3/\sqrt{3\pi m}+O(m^{-1})\), which is (3).

## Verification
The standalone `verify_swap.py` independently evaluates open-neighborhood utilities after each potential swap rather than reusing (4). It exhaustively checked every binary coloring for \((h,m)=(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(5,2)\), totaling \(42{,}816\) configurations and \(1{,}468{,}544\) oriented cross-part red-to-blue swap cases. All direct utilities agreed with (1). For three-part graphs, independent weighted profile enumeration agreed with (2), giving \(N_2=52\), \(N_3=458\), \(N_4=3196\), and \(N_5=28568\). These are finite checks; the results for arbitrary sizes follow from the proof.

## Relationship to prior work
Bilò, Bilò, Lenzner and Molitor (2022, arXiv:2204.12599, originally available April 26, 2022) develop a symmetric single-peaked swap Schelling model and prove convergence on almost-regular graphs. Crucially, their neighborhood fraction **includes the agent itself** (Section 1, model definition). The present open-neighborhood convention is not covered by that formula, and the contribution here is the exact profitable-swap hyperplane, the complete equilibrium census for three equal parts, and the asymptotic equilibrium frequency, not the established general idea of finite-improvement potentials. In fact, adding self-inclusion changes incentives on these networks: with the symmetric half peak, each cross-part swap would exchange the two absolute-deviation utilities, making bilateral strict improvement impossible.

Kreisel, Boehmer, Froese and Niedermeier (arXiv:2105.06561) investigate complexity and robustness for a monotone same-type preference, not the symmetric balanced-neighbor utility considered here. The jump-game study of Friedrich, Lenzner, Molitor and Seifert (arXiv:2302.12107) permits moves to vacant vertices rather than mutually beneficial swaps in a fully occupied graph. The formal comparisons do not imply novelty outside the inspected literature; no assertion of uniqueness is made.

## Limitations
The classification assumes equal part sizes, binary agent types, fully occupied complete multipartite networks, open neighborhoods, symmetric distance-to-one-half utility, and mutual *strict* benefit. Heterogeneous part sizes, asymmetric peaks, closed neighborhoods, strategic unilateral jumps, or more than two types may behave differently. The asymptotic concerns uniformly independently assigned colors (hence a random number of red agents), not a fixed-composition conditional distribution. The survey of literature cannot exclude an equivalent theorem in unindexed work; no independent audit has been performed.

## References
- D. Bilò, V. Bilò, P. Lenzner, L. Molitor. *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*. arXiv:2204.12599, initially posted 2022-04-26. https://arxiv.org/abs/2204.12599
- L. Kreisel, N. Boehmer, V. Froese, R. Niedermeier. *Equilibria in Schelling Games: Computational Hardness and Robustness*. arXiv:2105.06561, initially posted 2021-05-13. https://arxiv.org/abs/2105.06561
- T. Friedrich, P. Lenzner, L. Molitor, L. Seifert. *Single-Peaked Jump Schelling Games*. arXiv:2302.12107, initially posted 2023-02-23. https://arxiv.org/abs/2302.12107
