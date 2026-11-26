# Exact exchange distances between minimum super dominating sets of crown graphs

## Finding

Let \(\operatorname{Cr}_n\) be the labeled crown graph with shores \(\{a_i:i\in[n]\}\) and \(\{b_i:i\in[n]\}\), and edges \(a_i b_j\) exactly when \(i\ne j\). A super dominating set \(D\) is a set for which each vertex outside \(D\) has a neighbor in \(D\) adjacent to no other vertex outside \(D\). A token jump replaces one member of \(D\) by one vertex outside \(D\); a token slide additionally requires those two vertices to be adjacent in \(\operatorname{Cr}_n\). In both reconfiguration graphs, only minimum super dominating sets are states.

For \(n\ge4\), each minimum set is encoded by the disjoint two-subsets \(U,W\subseteq[n]\) indexing its omissions on the two respective shores. There are \(N_n=6\binom n4\) states. For \(n=4\) the token-jump graph has six isolated states. For \(n\ge5\) it is connected and \(4(n-4)\)-regular, and its distance is
\[
d((U,W),(U',W'))=4-|U\cap U'|-|W\cap W'|+
\mathbf1_{\{U\cup W=U'\cup W',\ (U,W)\ne(U',W')\}}.
\]
Its diameter is five, and the unique state at distance five from \((U,W)\) is \((W,U)\). The shell polynomial from any fixed state is
\[
\begin{aligned}
P_n(t)={}&1+4(n-4)t+(n-4)(5n-17)t^2+2(n-3)(n^2-8n+18)t^3\\
&+\frac{(n-4)(n-3)(n^2-7n+18)}4t^4+t^5.
\end{aligned}
\]
Consequently the ordered-pair distance polynomial is \(N_nP_n(t)\). The token-sliding graph has no edges, for any \(n\ge4\). The exact distances isolate a reconfiguration cost invisible to the number of mismatched occupied positions: with unchanged support, some token must use a vacancy as a buffer.

## Proof

**State space (known counting input).** If a shore has omissions indexed by \(U\), the omitted neighbors of \(b_j\) on that shore have indices \(U\setminus\{j\}\). Three or more omissions on one shore would therefore make witnessing on that shore impossible. With two omissions, the witnesses must be the two opposite-shore vertices at the same indices as those omissions, each witnessing the other index. Hence the simultaneous maximum of four omissions is attained exactly when the shores each omit two and the index sets are disjoint. Such pairs exist for \(n\ge4\), and their number is \(\binom n2\binom{n-2}{2}=N_n\).

**Moves and distance.** Use colors \(1,2\) for omission at an index on the respective shore and color \(0\) for an index unused by either shore. A token jump must preserve each shore's number of omissions. Within one shore it exchanges a colored index with any index of color \(0\) and no other moves are possible. This gives isolation for \(n=4\) and degree \(4(n-4)\) otherwise. A token slide crosses shores and necessarily changes the number of omissions on each, so it is impossible.

For a fixed target, write \(b=4-|U\cap U'|-|W\cap W'|\). Each of the \(b\) initially occupied positions of wrong color must become vacant before reaching the target. One move vacates only one position. This gives the lower bound \(b\). For every wrong index put a directed edge, labeled by that index, from its initial color to its target color. The multigraph is balanced because both colorings have the same multiplicities.

If the occupied unions differ, the edges meet color \(0\); any nontrivial component not meeting \(0\) would have to contain both \(1,2\), impossible with only two nonzero colors and one of them already in the component of \(0\). There is therefore an Euler circuit through all nontrivial edges starting at \(0\). Read this circuit, splitting it at repeated visits to \(0\). In each segment the first edge labels a vacant index needing the first nonzero color. Move the token from the index labeling the next edge into this vacancy; it fills the target color and leaves a vacancy at its old index. Iterate along the segment until the last vacated index is one whose target color is zero. Each edge with nonzero tail was used for exactly one move, for a total of \(b\) moves.

If the occupied unions agree but there is a mismatch, the edge multigraph is a nontrivial balanced graph on the two nonzero colors. For \(n\ge5\), use any index that is vacant in both states. Move the first mismatched token into that buffer, leaving its old position vacant, then traverse a cyclic order of the remaining edges of an Euler circuit to fill successive vacancies with the required colors. The buffered token fills the last vacancy. This takes \(b+1\) moves. The first move of any solution has to fill an initially vacant index that is also vacant in the target, so a move vacating one such position must be added to the \(b\) distinct initially occupied vacatings. This proves the extra unit. If source equals target the distance is zero. The resulting formula proves connectivity and gives distance five only for two pairs on the same union with no same-color matches, namely the full swap.

**Shell coefficients.** Fix the four initially colored positions and let \(s=4-b\) be the number of same-color matches. For \(r=0,1,2,3,4\), sum \(\binom{s}{r}\) over all targets. Requiring a specified subset of \(r\) matches, including \(a\) on shore one, leaves \(2-a\) and \(2-r+a\) positions of the two colors to be assigned disjointly among \(n-r\) positions. Thus the five binomial moments, in order, are
\[
N_n,\quad 2(n-1)(n-2)(n-3),\quad 5(n-2)(n-3),\quad 4(n-3),\quad 1.
\]
Binomial inversion counts the exact matches and hence gives shells in the baseline distance \(b\). Among the six targets on the same support there are the source, four partial swaps (baseline two), and one full swap (baseline four). Accordingly the correction to the baseline polynomial is \(4(t^3-t^2)+(t^5-t^4)\). Substituting the moments yields the displayed polynomial. Permuting indices simultaneously on the two shores acts transitively on the state space, so multiplying by \(N_n\) counts ordered pairs.

## Relationship to prior work

The all-cardinality classification and enumeration are known in the Resultary record [*All super dominating sets of crown graphs*](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-all-super-dominating-sets-of-crown-graphs--9d11a0d9ad56) and follow more generally from [*Super domination polynomial of bicliques with a deleted matching*](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-super-domination-polynomial-of-bicliques-with-a-deleted-matching--5607c6d03173). The state space is recalled only as an input. The contribution here is the distance formula, its complete shell distribution and antipode, and the contrast with sliding. Yamanaka et al., [*Swapping Colored Tokens on Graphs*](https://arxiv.org/abs/1803.06816), permit direct swaps between both occupied colors on a complete host; those moves are forbidden here. Related crown-graph results for minimum connected dominating or minimum zero-forcing sets use pairs of unequal two-subsets rather than disjoint two-subsets. The result does not determine the exchange metric for the latter models, nonminimum sets, or other super domination families; it does not assert global publication priority.

## Reproducibility

`verify_crown_superdom.py` tests the state-space description against the witness definition on all subsets of crowns with \(4\le n\le8\), and checks the token-jump distance against breadth-first search for \(4\le n\le10\). The witness rule, circuit argument and binomial moments above establish the claims for all orders in scope.
