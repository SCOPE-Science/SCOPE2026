# Exact crown-network equilibria for the two-level public-goods response rule

## Finding

**Theorem.** For any integers \(r\ge2\) and \(n\ge r+2\), take the crown graph \(\mathrm{Cr}_n=K_{n,n}\setminus M_n\), with matched nonedges \(\{u_i,v_i\}\), \(1\le i\le n\). Each vertex makes a binary decision and strictly prefers action \(1\) exactly when it has \(0\) or \(r\) active neighbors; otherwise it strictly prefers action \(0\). The full set of labeled pure Nash equilibria consists precisely of the following disjoint families:

1. **Polarized:** one whole bipartition class chooses \(1\), the other \(0\) (two profiles).
2. **Matched:** \(u_i\) and \(v_i\) simultaneously choose \(1\) on precisely \(t\) matched indices, and choose \(0\) elsewhere, where \(t=1\) or \(t=r+1\) (respectively \(n\) and \(\binom n{r+1}\) profiles).
3. **Complementary resonance:** only if \(n=2r\), for each matched index exactly one of \(u_i,v_i\) chooses \(1\), with precisely \(r\) active vertices in each bipartition class (\(\binom{2r}r\) profiles).

Consequently their exact number is
\[
E(n,r)=2+n+\binom n{r+1}+\mathbf 1_{\{n=2r\}}\binom{2r}r.
\]
Under the same rule on the complete bipartite graph \(K_{n,n}\) (before deleting the matching), there are exactly two equilibria. Thus deleting one perfect matching from this dense graph introduces \(n+\binom n{r+1}\) extra equilibria, plus \(\binom{2r}r\) at the unique resonance \(n=2r\). In the crown graph, the action-count generating polynomial is
\[
P_{n,r}(z)=n z^2+\binom n{r+1}z^{2r+2}+\left(2+\mathbf 1_{\{n=2r\}}\binom{2r}r\right)z^n.
\]

## Assumptions and scope

The graph has two **labeled** bipartition classes \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\). Every \(u_i\) is adjacent to all \(v_j\) except \(v_i\), with no within-class edges. An action profile is a vector \(x_i=s(u_i)\in\{0,1\}\), \(y_i=s(v_i)\in\{0,1\}\). The homogeneous strict best-response rule is \(T(k)=\mathbf1_{\{k\in\{0,r\}\}}\) for every nonnegative integer \(k\). There are no ties. A pure Nash equilibrium means every vertex plays \(T\) of its number of active **open-neighborhood** vertices. The asserted infinite-family classification requires \(r\ge2\) and \(n\ge r+2\); the cases \(r=1\) and smaller graphs are not claimed.

## Proof

Put \(X=\sum_{i=1}^n x_i\) and \(Y=\sum_{i=1}^n y_i\). Because the matched partner alone is excluded, every equilibrium satisfies exactly
\[
x_i=\mathbf1_{\{Y-y_i\in\{0,r\}\}},\qquad
y_i=\mathbf1_{\{X-x_i\in\{0,r\}\}}\quad (1\le i\le n).
\]
Classify each matched pair by its two actions. A pair of type \((0,0)\) requires \(X,Y\notin\{0,r\}\). A pair of type \((1,1)\) requires \(X,Y\in\{1,r+1\}\). A pair of type \((0,1)\) requires \(X\in\{0,r\}\) and \(Y-1\notin\{0,r\}\). A pair of type \((1,0)\) requires \(Y\in\{0,r\}\) and \(X-1\notin\{0,r\}\). These conditions are necessary and sufficient by the displayed best-response equations.

**Case I: some pair has equal actions.** Since \(r\ge2\), the sets \(\{0,r\}\) and \(\{1,r+1\}\) are disjoint. Either equal-action type is incompatible with either unequal-action type, using the conditions on \(X\) or \(Y\). Therefore every pair has equal actions. With \(t\) pairs of type \((1,1)\), we have \(X=Y=t\). All-zero is impossible because its vertices have zero active neighbors and should choose \(1\). All-one is impossible since an active vertex then sees \(n-1\ge r+1\) active neighbors. Hence \(0<t<n\). The active pairs require \(t-1\in\{0,r\}\), so \(t=1\) or \(t=r+1\); each is strictly between \(0\) and \(n\) by \(n\ge r+2\). The inactive pairs require \(t\notin\{0,r\}\), which both values satisfy as \(r\ge2\). Conversely, every such choice solves the equations. The respective counts are \(\binom n1=n\) and \(\binom n{r+1}\).

**Case II: all pairs have unequal actions.** Then \(x_i+y_i=1\) for every index, so \(X+Y=n\). If all pairs are of the same unequal-action type, they give one of the two polarized profiles. The active class sees zero active neighbors; each inactive vertex sees \(n-1\), which is neither \(0\) nor \(r\). Thus both are equilibria.

If both unequal-action types occur, each has an active vertex and an inactive vertex. Their conditions imply \(X,Y\in\{0,r\}\). Since both totals are positive, \(X=Y=r\) and necessarily \(n=2r\). Conversely, when \(n=2r\), any choice of precisely \(r\) indices with \(x_i=1,y_i=0\) and the complementary \(r\) indices with \(x_i=0,y_i=1\) works: all active vertices see exactly \(r\) active neighbors, and all inactive vertices see \(r-1\notin\{0,r\}\) since \(r\ge2\). The number is \(\binom{2r}r\). This exhausts the possibilities and proves the count and polynomial.

**Comparison with the undeleted graph.** On \(K_{n,n}\), the best response of every vertex in a bipartition class is identical because its active-neighbor count is the opposite class's total. Every equilibrium must therefore be uniform on each part; their active totals are \(0\) or \(n\). Since \(n\ge r+2\), \(T(0)=1\) and \(T(n)=0\). Exactly the two polarized profiles satisfy both classes' responses. Subtracting their count gives the stated matching-deletion increase. \(\square\)

## Verification

The accompanying standalone `verify.py` constructs the graph's open neighborhoods directly and checks every binary profile for all \(n=4,\ldots,8\) and every \(2\le r\le n-2\). It independently generates the classified configurations and tests set equality, not only cardinality. The same checker independently sums all four matched-pair-type multinomial configurations for \(4\le n\le30\) and \(2\le r\le n-2\), and checks the formula. It also restores the missing edges and verifies exactly two equilibria for the complete bipartite graph in the directly enumerated cases.

The local execution returned `VERIFIED`: 407,808 individual profiles for 15 parameter pairs, and 378 separate four-type exact counts. The proof above, not these finite checks, covers all admissible integers.

## Relationship to prior work

Klimm and Stahlberg (2023) establish NP-completeness of equilibrium existence on **general** undirected graphs for precisely the family of homogeneous nonmonotone "picky" best-response patterns, which includes \(T(k)=\mathbf1_{\{k\in\{0,r\}\}}\). Their reduction analyzes gadget constructions and does not state an exact all-size crown-graph equilibrium count. Gilboa (2023/2024) proves the general finite nonmonotone complexity dichotomy; Gilboa and Nisan (2022) analyze other strict best-response patterns and a general algorithmic framework. General NP-hardness does not imply the exact spectrum on the fixed highly symmetric graph family. The present count is a graph-family-specific consequence derived independently by pair-type classification; no generic complexity theorem is claimed.

## Limitations

This is an exact mathematical result within a homogeneous strict two-level best-response model, not an empirical behavioral claim. It does not classify arbitrary graphs, other response patterns, heterogeneous preferences, mixed equilibria, or the excluded low-parameter ranges. Public-literature searches cannot establish publication priority conclusively; unpublished or specialist precedent may exist. Computational verification is finite and is not an independent external audit.

## References

- M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849, first posted January 27, 2023. https://arxiv.org/abs/2301.11849
- M. Gilboa, *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580, first posted January 27, 2023. https://arxiv.org/abs/2301.11580
- M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238, first posted July 9, 2022. https://arxiv.org/abs/2207.04238
