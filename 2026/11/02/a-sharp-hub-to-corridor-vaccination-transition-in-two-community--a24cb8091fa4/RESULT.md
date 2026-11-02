# A sharp hub-to-corridor vaccination transition in two-community transmission trees

## Finding

Consider a pair of star-shaped communities linked by a path of length \(L\). In the independent, single-introduction bond-transmission epidemic described below, removing one vertex before the introduction minimizes the expected final number of infections. **Theorem.** For every integer \(s\ge 2\), every integer \(L\ge 2\), and every transmissibility \(0<p<1\), every optimal removal is either one of the two community hubs or a central vertex of the connecting path. Put \(m=\lfloor L/2\rfloor\). If \(2m(L-m)\le s(s-1)\), precisely the two hubs are optimal for all \(0<p<1\). If \(2m(L-m)>s(s-1)\), there is a unique \(p_*\in(1-1/s,1)\) such that exactly the hubs are optimal for \(p<p_*\), the hubs and central spine vertex or vertices tie at \(p=p_*\), and exactly the central spine vertex or vertices are optimal for \(p>p_*\). Here “central” means spine index \(m\) if \(L\) is even, or indices \(m,m+1\) if \(L\) is odd. This classification covers every vertex and every admissible parameter, with no optimization over arbitrary vertex sets left unresolved.

For example, at \(s=3,L=4\) the unique threshold is the root in \((0,1)\) of \(3p^3+4p^2-4p-2=0\), namely \(p_*\approx0.916188398055051\). A hub is better at \(p=1/2\), but the unique middle corridor vertex is better at \(p=49/50\).

## Assumptions and scope

Let \(T_{s,L}\) be the finite simple tree formed from a path with spine vertices \(v_0,v_1,\ldots,v_L\) and an additional \(s\) degree-one leaves attached independently to each endpoint \(v_0,v_L\). Thus \(|V(T_{s,L})|=N=L+1+2s\). The two hubs are \(v_0,v_L\). A single perfect prophylactic intervention deletes one chosen vertex and all incident edges. An imported infectious individual is then placed uniformly among the remaining \(N-1\) vertices. Each of the remaining tree edges independently transmits infection, with common probability \(p\); the final infected set is exactly the open-edge component containing the imported seed. The objective is the expectation of the number of infected vertices, including the seed. Only one vertex is removed; the seed is not chosen before deletion. No assumptions about transmission times are made beyond their edge-level independent transmissibility representation.

For vertices \(x,y\) of the original tree, write \(d(x,y)\) for the number of edges in their unique path, and write \(v\in[x,y]\) if that path contains \(v\), allowing \(x=y=v\). Define
\[
 W(p)=\sum_{x,y\in V(T_{s,L})}p^{d(x,y)},\qquad B_v(p)=\sum_{x,y\in V(T_{s,L}):\,v\in[x,y]}p^{d(x,y)}.
\]
These are finite ordered-pair sums, including diagonals.

## Proof

**1. Exact objective.** In any tree, two surviving vertices \(x,y\) become connected by open edges with probability \(p^{d(x,y)}\). They remain connected after deleting \(v\) exactly when their unique original path avoids \(v\). Averaging the component size over a uniform surviving seed therefore gives
\[
 (N-1)\,\mathbb E_v[|\text{infected}|]=W(p)-B_v(p).
\]
Hence the optimal intervention maximizes \(B_v(p)\). Every leaf is strictly dominated by its adjacent hub: every original path containing that leaf also contains its hub, except the single diagonal leaf-to-itself pair, which has weight \(1\) and is replaced by the hub-to-itself diagonal. The hub lies on further positive-weight paths. Thus only spine vertices can maximize \(B_v\).

**2. Spine scores.** Set \(g_j(p)=\sum_{k=0}^{j}p^k+sp^{j+1}\) for integer \(j\ge0\). Splitting the ordered paths through an interior spine vertex at that vertex gives the exact score
\[
 B_{v_j}(p)=2g_j(p)g_{L-j}(p)-1\quad(1\le j\le L-1).
\]
At either hub, define \(R=pg_{L-1}(p)\). Counting paths between its \(s\) leaves, the hub itself, and the rest of the graph gives
\[
 B_{v_0}(p)=B_{v_L}(p)=1+2sp+2R+s(s-1)p^2+2spR.
\]
These formulas count ordered pairs; the factor \(s(s-1)\) counts ordered distinct leaves on the same hub.

**3. Shape of the interior scores.** For \(0<p<1\), put \(c=1-s(1-p)\). Then
\[
 g_j(p)=\frac{1-cp^{j+1}}{1-p}.
\]
When \(p>1-1/s\), one has \(0<c<1\), and \(j\mapsto\log g_j\), extended to real \(j\ge0\), is strictly concave. Therefore \(g_jg_{L-j}\) increases strictly toward the center and decreases strictly afterward: only the central interior vertices can be best. When \(p<1-1/s\), \(c<0\) and the same logarithm is strictly convex, so the largest interior score occurs at \(j=1\) or \(j=L-1\). At equality, \(c=0\) and all interior scores coincide.

**4. Low-transmissibility hub dominance.** Direct subtraction yields
\[
 \frac{B_{v_1}(p)-B_{v_0}(p)}p=-2(s-1)-s(s-1)p+2\sum_{k=1}^{L-2}p^k+2sp^{L-1}=H_{s,L}(p),
\]
with an empty sum for \(L=2\). In ascending powers of \(p\), the nonzero coefficients of \(H_{s,L}\) have at most one sign change, from negative to positive: its constant term is \(-2(s-1)\), the coefficient of \(p\) is \(2-s(s-1)\) for \(L\ge3\), all later coefficients are positive; for \(L=2\) this assertion follows directly from its linear expression. By Descartes' rule, it has at most one positive zero, and any positive zero changes its sign from negative to positive. At \(t=1-1/s\), a geometric-series evaluation gives \(H_{s,L}(t)=-s(s-1)t<0\). Consequently \(H_{s,L}(p)<0\) for \(0<p\le t\). Together with the shape in Step 3, this proves that the hubs strictly dominate all interior vertices throughout this range.

**5. Unique high-transmissibility transition.** Let \(m=\lfloor L/2\rfloor\), and define the polynomial
\[
 D_{s,L}(p)=\frac{B_{v_m}(p)-B_{v_0}(p)}p.
\]
The following list of coefficients is obtained by multiplying the two finite geometric sums in Step 2 and subtracting the hub expression; \(c_k\) is the coefficient of \(p^k\):

For \(L=2\), \((c_0,c_1)=(-2(s-1),\,s(3-s))\). For \(L=3\), \((c_0,c_1,c_2)=(-2(s-1),\,-s^2+s+2,\,2s)\). For \(L\ge4\),
\[
 c_0=-2(s-1),\quad c_1=4-s^2-s,\quad c_k=2(k+1-s)\quad(2\le k<m).
\]
When \(L=2m+1\) is odd, \(c_m=2m\) and \(c_k=2(s+L-1-k)\) for \(m+1\le k\le L-1\). When \(L=2m\) is even, \(c_k=2(s+L-1-k)\) for \(m\le k\le L-1\). All ranges with lower bound above upper bound are empty.

In every case the coefficient list, read in ascending order and omitting zeros, has at most one sign change, negative to positive. This follows because \(c_0<0\), \(c_1\le0\) when \(L\ge4\), \(2(k+1-s)\) is increasing in \(k\), and every trailing coefficient is strictly positive. The two exceptional lists satisfy the same assertion directly. Descartes' rule thus gives at most one positive root. At \(p=1\), every pair through a vertex contributes one, and direct component-size counting yields
\[
 D_{s,L}(1)=2m(L-m)-s(s-1).
\]
Since \(D_{s,L}(0)=-2(s-1)<0\), if the displayed value is positive, a unique positive root lies in \((0,1)\), with opposite strict signs on either side. Step 4 forces that root to exceed \(t\). If that value is zero or negative, the same one-sign-change property excludes positive values for all \(0<p<1\) (a zero at \(p=1\) is outside the parameter range). The interior-shape result then proves exactly the stated global optimality and all equality cases.

## Verification

The standalone Python 3/SymPy checker in `checks/check.py` enumerates every vertex and ordered path independently in sample trees, evaluates all path weights with exact rational arithmetic, and compares against both formula families. It additionally verifies the proposed polynomial coefficient formulas and \(p=1\) boundary identities for \(2\le s\le7\), \(2\le L\le10\), and checks the \(s=3,L=4\) threshold polynomial and optimal-vertex witnesses at \(p=1/2\) and \(p=49/50\). The saved script reported 3,564 exact-rational/path and symbolic assertions. The arbitrary-parameter theorem rests on the preceding analytical argument, not on finite enumeration.

## Relationship to prior work

The standard bond-percolation representation of a finite independent-transmission epidemic motivates the exact ordered-pair objective. Hadidjojo and Cheong (2011) optimize graph partitioning in an estimated infection network; Gong and collaborators (2013) compare community-focused immunization heuristics; Altarelli and collaborators (2013) use message passing to select influential or protective interventions; Morone and Makse (2015) examine optimal percolation and the dismantling of large components. Those problems differ from the complete closed-form optimum for uniform single-seed expected infections on every member of this symmetric tree family, including the all-parameter hub-versus-corridor threshold. General published tree-centrality or network-immunization results may subsume a specialization; historical priority therefore remains provisional.

## Limitations

The theorem assumes a tree, identical community sizes, identical edge transmissibility, one uniformly selected introduction after one perfectly effective removal, and maximization of expected *finite* outbreak size rather than giant-component collapse, outbreak probability, epidemic duration, or outcomes from multiple simultaneous introductions. Its vaccination language is a mathematical graph intervention, not a clinical recommendation. Endpoint cases \(p=0\) and \(p=1\) are excluded: at \(p=0\) every vertex deletion leads to an outbreak of size one, while at \(p=1\) additional boundary ties may occur. The independently enumerating checker is illustrative finite corroboration, not a proof of the universal quantifiers; no independent audit has been performed.

## References

1. Hadidjojo, J., and Cheong, S. A. (2011). Equal Graph Partitioning on Estimated Infection Network as an Effective Epidemic Mitigation Measure. *PLoS ONE* 6(7), e22124. First public date 2011-07-22. https://doi.org/10.1371/journal.pone.0022124
2. Altarelli, F., Braunstein, A., Dall'Asta, L., and Zecchina, R. (2013). Containing epidemic outbreaks by message-passing techniques. arXiv:1309.2805v1, first public date 2013-09-11. https://arxiv.org/abs/1309.2805
3. Gong, K., Tang, M., Hui, P. M., Zhang, H. F., Younghae, D., and Lai, Y. C. (2013). An Efficient Immunization Strategy for Community Networks. *PLoS ONE* 8(12), e83489. https://doi.org/10.1371/journal.pone.0083489
4. Morone, F., and Makse, H. A. (2015). Influence maximization in complex networks through optimal percolation. arXiv:1506.08326. https://arxiv.org/abs/1506.08326
