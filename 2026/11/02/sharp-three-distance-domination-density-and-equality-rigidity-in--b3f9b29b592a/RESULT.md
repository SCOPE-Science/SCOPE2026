# Sharp three-distance domination density and equality rigidity in two-row grid strips

## Finding
Let \(G_n=C_n\square K_2\) be the labelled circular two-row grid with \(n\ge7\) columns. A three-distance dominating set \(D\) is a vertex set such that every vertex not in \(D\) has at least one member of \(D\) at graph distance **exactly** three. Its minimum size is \(\gamma_3(G_n)\). Then
\[
\gamma_3(G_n)\ge\left\lceil\frac{3n}{7}\right\rceil\qquad(n\ge7).
\]
For every positive multiple \(n\) of seven, equality holds, and there are **exactly fourteen** minimum three-distance dominating sets on the labelled graph. They are the seven cyclic shifts of the repeated seven-column selection word \((0,0,1,0,0,2,2)\) and the seven cyclic shifts of its row-swapped word \((0,0,2,0,0,1,1)\). The digit \(0\) selects no row; \(1\) selects row zero; \(2\) selects row one.

For the open ladder \(H_n=P_n\square K_2\), the exact limiting minimum density is
\[
\lim_{n\to\infty}\frac{\gamma_3(H_n)}{2n}=\frac{3}{14}.
\]

## Assumptions and scope
All graphs are finite, unweighted, undirected and simple. Vertices are \((i,r)\) with column \(i\in\mathbb Z/n\mathbb Z\) for \(G_n\), or \(i\in\{0,\ldots,n-1\}\) for \(H_n\), and row \(r\in\{0,1\}\). The graph is the Cartesian product of the corresponding cycle or path with the single edge. We assume \(n\ge7\), ensuring that in \(G_n\) the vertices at distance three from \((i,r)\) are exactly \((i\pm3,r)\) and \((i\pm2,1-r)\). The selection condition does not constrain a vertex already in \(D\).

## Proof
**Local encoding.** Encode each column by its two-bit mask \(a_i\in\{0,1,2,3\}\), with bit \(r\) indicating whether \((i,r)\in D\). A center column \(a_3\) in a seven-column window \(a_0,\ldots,a_6\) is three-distance dominated if and only if, for each \(r\in\{0,1\}\), at least one of
\[
(a_3)_r,\quad (a_0)_r,\quad (a_6)_r,\quad
(a_1)_{1-r},\quad (a_5)_{1-r}
\]
is one. Here \((a)_r\) denotes the indicated binary digit.

Form the directed graph whose \(4^6=4096\) states are six-column words \(s=(a_0,\ldots,a_5)\). The arc \(s\to t=(a_1,\ldots,a_6)\) is present exactly when the local condition holds, and has weight \(w(s,t)=\operatorname{popcount}(a_3)\), the number of selected vertices in the center column. It has exactly \(15376\) arcs. Every three-distance dominating selection on \(G_n\) corresponds to a length-\(n\) closed walk in this graph, with total arc weight \(|D|\). Conversely, every such closed walk yields a valid labelled cyclic selection. These statements hold for all \(n\ge7\) without requiring the seven-column windows to be disjoint.

**Exact finite potential certificate.** The accompanying file `support/potential.json` explicitly supplies a vector \(p\in\mathbb Z^{4096}\). The independently executable `support/verify.py` enumerates every one of the \(15376\) permitted arcs and establishes the finite inequality
\[
p(t)-p(s)\le 7w(s,t)-3\qquad\text{for every arc }s\to t.
\]
The vector has minimum \(-18\) and maximum \(0\). It can also be reconstructed by initializing all potentials to zero and performing eighteen simultaneous min-plus relaxations from every arc, after which the nineteenth relaxation makes no change. The checker reads the **supplied certificate**, rather than relying on its discovery procedure. Summing the displayed inequality around any closed walk gives
\[
0\le 7|D|-3n,
\]
so \(\gamma_3(G_n)\ge\lceil3n/7\rceil\) for every \(n\ge7\).

**Equality and exhaustive structural rigidity.** The seven-column word \((0,0,1,0,0,2,2)\) has three selected vertices and satisfies every cyclic local constraint. Repeating it when \(7\mid n\) attains \(|D|=3n/7\). The checker independently constructs the directed subgraph of *tight* arcs, those with equality in the potential inequality. It verifies \(3583\) tight arcs and, using a complete strongly-connected-component decomposition, exactly two cyclic components, each a directed simple cycle of length seven. All remaining strongly connected components are acyclic singletons. When \(|D|=3n/7\), every arc of its closed walk must be tight, because all individual slacks are nonnegative integers and sum to zero. Thus its walk must lie in one of those two seven-cycles. They are the seven rotations of the displayed word and the seven rotations of its row swap. This proves exactly fourteen labelled minimum sets, without quotienting by automorphisms.

**Open ladder density.** For \(n\ge7\), every pair at distance three in \(H_n\) remains at distance three when the ends are joined to form \(G_n\). Therefore a three-distance dominating set of \(H_n\) also dominates \(G_n\), and \(\gamma_3(H_n)\ge3n/7\). Conversely restrict the infinite periodic seven-column word to \(n\) columns, then select both vertices in each of the first and last three columns. Every vertex outside these boundary strips retains its periodic exact-distance-three witness inside \(H_n\). This uses at most \(3\lceil n/7\rceil+12\le3n/7+15\) vertices. Hence \(3n/7\le\gamma_3(H_n)\le3n/7+15\), and dividing by \(2n\) proves the asserted limit.

## Verification
Run `python3 support/verify.py` with Python 3 and no nonstandard dependencies. The checker reads `support/potential.json`, checks all states/arcs and all potential inequalities, computes all strongly connected components of the tight subgraph, and checks the periodic witnesses. A distinct check builds the original prism graph and independently calculates shortest-path distances for circumferences seven through ten. Finally, complete labelled-set enumeration for circumferences seven through nine yields minimum sizes \(3,4,5\), with respectively \(14,36,72\) minimum sets. Only the first value is asserted as a closed-form extremal multiplicity; the larger brute-force cases corroborate the graph/automaton correspondence. All arithmetic in the certificate is exact integer arithmetic; no finite sampling is extrapolated to prove the infinite claim.

## Relationship to prior work
Das, Das, and Sadhukhan (2026, arXiv:2607.29648v1) introduced the general exact-distance-grid density question and give two-dimensional asymptotic bounds, including for distance three. Their results concern square grids and a two-dimensional limit; they do not state this fixed-height-two sharp density or equality classification. Hassan et al. (2024) define exactly the same distance-three domination condition and prove broad extremal characterizations, but do not analyze circular ladders. Bouznif et al. (arXiv:1708.00758v1) develop a broad finite-state method for identifying/locating-dominating codes on small-height strips; this methodological precedent is acknowledged, but its reported codes impose different covering/separation conditions and it does not state the \(3/14\) density or fourteen-pattern rigidity. The new assertion is the **exact invariant and extremal classification**, not the existence of finite-state methods.

## Limitations
No closed formula is claimed for \(\gamma_3(G_n)\) when \(7\nmid n\), and the number of minimum sets outside multiples of seven is not classified. The result is only for distance exactly three and grid height two; it does not resolve the two-dimensional square-grid distance-three density or higher strip heights. Priority was assessed against accessible mathematical records and full texts but has not undergone independent exhaustive literature review. The finite certificate requires executing/rechecking the supplied bounded verification program; no independent human audit is claimed.

## References
1. S. Das, S. Das, and A. Sadhukhan, *Exact-Distance Domination in Grid Graphs*, arXiv:2607.29648v1 (first posted 2026-07-31), https://arxiv.org/abs/2607.29648.
2. J. A. Hassan et al., *3-Distance Domination Numbers of Some Graphs*, International Journal of Mathematics and Computer Science **19** (2024), 981–986, https://future-in-tech.net/19.4/R-JavierHassan.pdf.
3. M. Bouznif, J. Darlay, J. Moncel, and M. Preissmann, *Exact values for three domination-like problems in circular and infinite grid graphs of small height*, arXiv:1708.00758v1, https://arxiv.org/abs/1708.00758.
