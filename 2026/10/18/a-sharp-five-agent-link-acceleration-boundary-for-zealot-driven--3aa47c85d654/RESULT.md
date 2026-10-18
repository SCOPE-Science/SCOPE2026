# A sharp five-agent link-acceleration boundary for zealot-driven voter dynamics

## Finding
On a finite connected simple undirected graph \(G=(V,E)\), one committed positive-opinion vertex \(r\) does not update, and all other vertices initially hold the negative opinion. Each noncommitted vertex has an independent rate-one exponential clock; at a ring it uniformly chooses one of its graph neighbors and copies that neighbor's opinion. Define the expected cumulative negative-opinion person-time by
\[
\mathcal D(G,r)=\mathbb E\!\left[\int_0^\infty\sum_{i\in V\setminus\{r\}}\mathbf1_{\{X_i(t)=0\}}\,dt\right].
\]
This is **not** the expected time until unanimous agreement.

**Sharp finite-order bound.** For every connected graph with at most four vertices, adding any missing edge \(uv\), with \(u,v\ne r\), strictly **increases** \(\mathcal D\). Five vertices suffice for the opposite effect. Take
\[
V=\{0,1,2,3,4\},\qquad r=0,\qquad E=\{01,04,12,23\}.
\]
Inserting the edge \(24\) changes the exact expected cumulative dissent from \(23\) to \(21\). Thus the new social link speeds cumulative conversion by two expected dissent-person-time units. This phenomenon persists at every vertex order at least five, by adding arbitrary extra leaves adjacent only to the committed vertex in both networks.

**Exact link-response law.** Let \(L\) be the root-deleted combinatorial Laplacian (its diagonal entries retain the full graph degrees); let \(d\) be the nonroot degree vector; and set \(P=L^{-1}\), \(h=Pd\), \(z=P\mathbf1\). For a missing nonroot link \(uv\), let \(b=e_u-e_v\) and \(R=b^TPb\). Then
\[
\mathcal D(G+uv,r)-\mathcal D(G,r)
=z_u+z_v-\frac{(z_u-z_v)(h_u-h_v+P_{uu}-P_{vv})}{1+R}.
\]
The formula applies to every connected finite graph, and its sign is a precise criterion for whether one proposed peer link accelerates or delays cumulative alignment.

## Assumptions and scope
All graphs are finite, loopless, undirected, unweighted, and connected. The single distinguished vertex remains permanently in opinion one. Every other vertex starts in opinion zero and independently updates at rate exactly one; each update selects a graph neighbor uniformly. The proposed added edge is absent and joins **two nonroot vertices**. When no such edge exists, the lower-order assertion has an empty quantifier. Units are physical time, not discrete global-update steps. A nonroot vertex can change its opinion repeatedly before absorption.

The rooted Laplacian \(L\) is positive definite: for each nonzero real vector \(y\) on nonroot vertices, \(y^TLy\) equals the sum of squared differences across nonroot edges plus squared nonroot values across root-neighbor edges; connectivity forces this sum positive. Hence the inverse and all displayed expressions exist.

## Proof
**1. Integrated first moments.** Write \(q_i(t)=\Pr[X_i(t)=0]\) for each nonroot vertex, with \(q_r(t)=0\). Conditioning on the next clock ring gives
\[
\dot q_i(t)=-q_i(t)+\frac1{d_i}\sum_{j\sim i}q_j(t),\qquad q_i(0)=1.
\]
In vector notation \(\dot q=-D^{-1}Lq\), with \(D=\operatorname{diag}(d)\). This is an absorbing finite irreducible-to-root random-walk subgenerator; its eigenvalues have strictly negative real parts, because \(D^{-1/2}LD^{-1/2}\) is positive definite. Thus \(a=\int_0^\infty q(t)\,dt\) is finite. Integrating the differential equation yields \(La=d\), so \(a=L^{-1}d=h\). Fubini/Tonelli now gives \(\mathcal D(G,r)=\mathbf1^Th\). Equivalently, \(h_i\) is the discrete-step simple-random-walk mean hitting time of \(r\) from \(i\).

**2. Edge insertion.** A new nonroot edge \(uv\) increases the two affected degrees by one; its grounded Laplacian update is \(L'=L+bb^T\), where \(b=e_u-e_v\), while \(d'=d+e_u+e_v\). Sherman–Morrison gives
\[
(L')^{-1}=P-\frac{Pb\,b^TP}{1+b^TPb}.
\]
Inserting this into \(\mathbf1^T(L')^{-1}d'-\mathbf1^TPd\), using symmetry of \(P\) and \(b^TP(e_u+e_v)=P_{uu}-P_{vv}\), produces exactly the response law in the Finding section. Its denominator is strictly greater than one.

**3. Complete small-order obstruction.** The standalone checker enumerates every labeled graph on each vertex set of orders two, three, and four, retaining only connected graphs; for each graph it uses every possible root and every missing nonroot edge. All calculations are exact rational Gaussian elimination on \(Lh=d\). There are respectively \(2\), \(12\), and \(152\) connected graph/root pairs, yielding respectively zero, three, and \(168\) eligible edge insertions. Every one of the \(171\) nonvacuous changes is strictly positive; their minimum is \(2\). Exhaustive enumeration of this explicitly finite domain proves the lower bound; no inference from small numerical samples to higher orders is used.

**4. Sharp witness and unbounded family.** On the displayed five-vertex graph, the integrated dissent times for vertices \(1,2,3,4\) before insertion are exactly \((5,8,9,1)\), and after insertion exactly \((4,6,7,4)\). Their sums are \(23\) and \(21\). Independently, the attached checker solves the complete \(2^4\)-configuration continuous-time voter chain for the expected integrated dissent, obtaining the same values. Attaching \(k\ge0\) additional leaves directly to root \(0\), in both graphs, does not alter the update rules at any of the original four nonroot vertices: only the root's degree changes and it never updates. Each new leaf copies the permanently positive root at rate one, contributing exactly one to cumulative dissent. Both totals therefore rise by \(k\), retaining the strict change of \(-2\) for all \(k\).

## Verification
Run `python3 verify.py` with a standard Python 3 installation. Its sole output is a compact sorted-key JSON object; it must agree byte-for-byte with `certificate.json` (allowing the final newline). It uses `fractions.Fraction`, enumerates all labeled connected simple graphs through four vertices and their rooted eligible insertions, and separately evaluates the five-vertex witness by solving a full transient continuous-time Markov-chain reward system. The complete finite census comprises \(171\) eligible root/link cases; it is exhaustive because all \(2^{\binom n2}\) labeled edge masks are traversed at each order \(2\le n\le4\). The general edge-response identity and indefinite leaf extension are proven algebraically, not established by computational sampling.

## Relationship to prior work
A single opinion-biased voter in an infinite lattice and its spatial relaxation were investigated by Mobilia (2003), and finite populations with immutable zealots by Mobilia, Petersen, and Redner (2007). Masuda (2014/2015) studied network opinion control and stationary vote share with zealots. Brede, Restocchi, and Stein (2018) investigated finite-horizon strategic control allocations and transient vote shares; their control-placement and finite-horizon objective do not state the fixed single-zealot **integral over the entire transient**, a sharp five-agent link-addition cutoff, or the graph-level formula here.

A different graph-edge insertion problem, Kemeny's constant, is studied by Kirkland and Zeng (2016) and Kirkland, Li, McAlister, and Zhang (2023). Kemeny's constant averages hitting times over a **stationary-random target**, whereas the present observable sums hitting times to **one fixed absorbing target**, and alters the transitions at both endpoints of a newly added nonroot link. Neither identity nor nonmonotonicity for one observable implies this precise result for the other. The underlying random-walk linear systems and Sherman–Morrison identity are classical ingredients, not claimed as independently new.

## Limitations
This is a fixed-zealot, uniform-neighbor, rate-one-updating model. Changing the clock normalization to one global update per unit time rescales the objective and numerical values. Edge insertion incident to the committed vertex is excluded. No claim is made for consensus absorption time, competing committed opinions, nonlinear social influence, biased copying, directed graphs, or arbitrary weighted edges. The finite lower-bound certificate is a complete enumeration through four vertices, not an enumeration of all larger graphs. Despite direct comparisons with relevant mathematical literature, an unlocated equivalent earlier result under root-hitting-time or network intervention terminology remains possible, and independent bibliographic validation has not been performed.

## References
1. M. Mobilia, *Does a Single Zealot Affect an Infinite Group of Voters?*, arXiv:cond-mat/0304670, original public version 30 April 2003. https://arxiv.org/abs/cond-mat/0304670
2. M. Mobilia, A. Petersen, and S. Redner, *On the Role of Zealotry in the Voter Model*, arXiv:0706.2892 (2007). https://arxiv.org/abs/0706.2892
3. N. Masuda, *Opinion Control in Complex Networks*, arXiv:1412.2170 (2014); New Journal of Physics 17, 033031 (2015). https://arxiv.org/abs/1412.2170
4. M. Brede, V. Restocchi, and S. Stein, *Effects of Time Horizons on Influence Maximization in the Voter Dynamics*, Journal of Complex Networks 7 (2019), 445–468; first published 30 October 2018. https://doi.org/10.1093/comnet/cny027
5. S. Kirkland and Z. Zeng, *Kemeny's Constant and an Analogue of Braess' Paradox for Trees*, Electronic Journal of Linear Algebra 31 (2016). https://doi.org/10.13001/1081-3810.3222
6. S. Kirkland, Y. Li, J. McAlister, and X. Zhang, *Edge Addition and the Change in Kemeny's Constant*, arXiv:2306.04005 (2023). https://arxiv.org/abs/2306.04005
