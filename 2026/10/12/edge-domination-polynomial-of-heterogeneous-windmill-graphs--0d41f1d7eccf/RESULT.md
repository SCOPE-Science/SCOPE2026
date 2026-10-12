# Edge-domination polynomial of heterogeneous windmill graphs

## Finding
Let \(r\ge2\), let \(m_1,\ldots,m_r\) be arbitrary positive integers, and form the heterogeneous windmill
\[
W=K_1\vee(K_{m_1}\cup\cdots\cup K_{m_r}),
\]
with hub \(c\) and mutually disjoint clique blades \(B_i\) of sizes \(m_i\). An edge dominating set is an edge set \(F\) such that each edge of \(W\) shares an endpoint with an edge of \(F\) (possibly itself). Its edge-domination polynomial is \(D_e(W;x)=\sum_{F\text{ edge dominating}}x^{|F|}\).

For positive \(m\) and \(\epsilon\in\{0,1\}\), define the integer polynomials
\[
A_m(x)=\sum_{j=0}^{m}(-1)^j\binom mj(1+x)^{\binom{m-j}{2}},
\]
\[
T_m^{(\epsilon)}(x)=\sum_{t=0}^{1}\binom mt
\sum_{j=0}^{m-t}(-1)^j\binom{m-t}{j}
(1+x)^{\binom{m-t-j}{2}+\epsilon(m-t-j)}.
\]
Then the **complete edge-domination polynomial** is
\[
\boxed{D_e(W;x)=\prod_{i=1}^{r}T_{m_i}^{(1)}(x)
-\prod_{i=1}^{r}T_{m_i}^{(0)}(x)+\prod_{i=1}^{r}A_{m_i}(x).}
\tag{1}
\]
In particular, if \(L=\sum_i\lfloor m_i/2\rfloor\), then the edge-domination number satisfies
\[
\boxed{\gamma_e(W)=\begin{cases}
L,&\text{some blade size is even},\\
L+1,&\text{all blade sizes are odd}.
\end{cases}}
\tag{2}
\]
The coefficient of the first nonzero term also has the following closed form, classifying and counting *all* optimum edge sets, not merely minimum maximal matchings. Let \((-1)!!=0!!=1\) and \(d!!=d(d-2)(d-4)\cdots\) for positive integers \(d\). For even \(m\ge2\), set
\[
p_m=(m-1)!!,\qquad
 e_m=\begin{cases}0,&m=2,\\m(m-1)\binom{m-2}{2}(m-5)!!,&m\ge4,\end{cases}
\qquad q_m=m(m-1)(m-3)!!.
\]
For odd \(m\ge1\), set
\[
t_m=m(m-2)!!,
\]
\[
\begin{aligned}
u_m={}&m(m-2)!!+m(m-1)(m-2)!!\\
&+\mathbf1_{m\ge5}m(m-1)(m-2)\binom{m-3}{2}(m-6)!!\\
&+\mathbf1_{m\ge3}m\binom{m-1}{2}(m-4)!!.
\end{aligned}
\]
With \(E=\{i:m_i\text{ even}\}\) and \(O=\{i:m_i\text{ odd}\}\), if \(E\ne\varnothing\), the number of optimum edge dominating sets is
\[
\boxed{N_{\min}=\Big(\prod_{i\in O}t_{m_i}\Big)
\left[\prod_{i\in E}(p_{m_i}+e_{m_i}+q_{m_i})
-\prod_{i\in E}(p_{m_i}+e_{m_i})\right]
+\mathbf1_{O=\varnothing}\prod_{i\in E}p_{m_i}.}
\tag{3}
\]
If all blade sizes are odd, it is
\[
\boxed{N_{\min}=\sum_{i=1}^r u_{m_i}\prod_{j\ne i}t_{m_j}.}
\tag{4}
\]
For ordinary friendship graphs, with every \(m_i=2\), these specialize to \(D_e(W;x)=((1+x)^3-1)^r\), \(\gamma_e(W)=r\), and \(N_{\min}=3^r\). For stars, with every \(m_i=1\), they give \(D_e(W;x)=(1+x)^r-1\), \(\gamma_e(W)=1\), and \(N_{\min}=r\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The hub is a single universal vertex and the rim is a disjoint union of nonempty cliques, with arbitrary and not necessarily equal blade sizes. The symbol \(\gamma_e\) denotes the smallest size of an **edge dominating** set, not vertex domination or vertex-edge domination; selected edges need not form a matching. In formulas (1)–(4), \(r\) is any integer at least two and each \(m_i\) is any integer at least one. Products over the empty set equal one.

## Proof
**Zero-selected-degree lemma.** For any edge set \(F\), let \(Z(F)\) be the vertices incident to no edge of \(F\). A graph edge is undominated by \(F\) precisely when *both* its endpoints belong to \(Z(F)\); hence \(F\) is edge dominating if and only if \(Z(F)\) is an independent set of \(W\). In this windmill, if the hub is incident with some selected spoke, the uncovered rim vertices must number at most one in each blade. If the hub has no selected spoke, then the hub belongs to \(Z(F)\), so every rim vertex must be incident with a selected internal edge. These two cases are disjoint.

**Enumerators.** In the hub-uncovered case, no spokes may be selected; a clique on \(m\) rim vertices must have no zero-selected-degree vertex. Inclusion-exclusion over prescribed isolated vertices gives \(A_m(x)\). In the hub-covered case, first allow all potential spokes and require *at most one* isolated rim vertex per clique: select the exact isolated set of size \(t\in\{0,1\}\), forbid all edges incident with it, and use inclusion-exclusion over the remaining vertices. For \(m-t-j\) unrestricted vertices the allowed internal edges number \(\binom{m-t-j}{2}\) and the allowed spokes number \(m-t-j\), yielding \(T_m^{(1)}(x)\). This product also includes configurations with **no spoke at all**; those are exactly counted by the corresponding \(T_m^{(0)}(x)\) product and must be subtracted. Adding back the distinct hub-uncovered configurations counted by \(\prod A_{m_i}\) yields (1). Every edge set is counted once, since its actual isolated rim set is uniquely determined.

**Smallest cardinality.** Suppose at least one spoke is selected. In a blade of size \(m\), at least \(m-1\) rim vertices must be incident with selected edges. An internal edge covers at most two rim vertices, whereas a spoke covers just one. Consequently that blade uses at least \(\lfloor m/2\rfloor\) edges. If \(m\) is odd and equality holds, every selected local edge must be an internal matching edge: one spoke would reduce the maximum number of covered rim vertices below \(m-1\). Thus equality at total \(L\) with the hub covered is possible if and only if some blade has even size. It is constructible by choosing in that even blade one spoke and a matching on all but the spoke's rim endpoint and one other rim vertex; choose an internal matching covering all but one rim vertex in every odd blade and permissible minimum local patterns in all remaining even blades. If instead the hub is uncovered, every rim vertex in each blade must be covered with internal edges, needing at least \(\sum_i\lceil m_i/2\rceil\). When all blade sizes are odd this is \(L+r>L+1\), whereas adding one spoke and suitable internal matching to one odd blade, and minimum internal matchings on all others, constructs a dominating edge set of size \(L+1\). These observations prove (2), including singleton blades.

**Classification and counts at equality.** If \(m=2s\) is even, precisely \(s\) local edges covering at least \(m-1\) rim vertices have exactly three possible disjoint types: (P) all internal edges are a perfect matching, counted by \(p_m\); (E) all edges are internal with exactly one repeated rim endpoint, equivalently one two-edge path and \(s-2\) independent edges, leaving one rim isolated, counted by \(e_m\); or (Q) exactly one spoke and \(s-1\) independent internal edges, with their rim endpoints pairwise distinct and one rim isolated, counted by \(q_m\). The stated binomial and double-factorial expressions count the labeled choices directly. If \(m=2s+1\) is odd, precisely \(s\) local edges covering at least \(m-1\) rim vertices must be disjoint internal matching edges with one rim isolated, giving \(t_m\).

For an odd blade with one *extra* local edge (\(s+1\) total) that contains at least one spoke, the number of selected spokes is at most two: with \(k\) spokes one can cover no more than \(2(s+1)-k\) rim vertices, and at least \(2s\) must be covered. With one spoke, either all rim vertices are covered by otherwise disjoint edges (first term of \(u_m\)); or exactly one rim vertex is isolated, and the single repeated rim incidence is shared between the spoke and one internal edge (second term), or between two internal edges forming a two-edge path (third term). With two spokes, all selected edges cover pairwise distinct rim vertices and exactly one is isolated (fourth term). These are exhaustive, mutually exclusive, and counted by the displayed expressions for \(u_m\).

If an even blade exists, the total minimum size is \(L\): every odd blade must be a \(t_m\)-type local matching, every even blade is P/E/Q, and either at least one Q supplies the required spoke, or there are no spokes and **every blade is even and every blade is P**. Counting those disjoint possibilities proves (3). If every blade is odd, the total minimum is \(L+1\), every minimum set must have a spoke, and precisely one blade carries one extra edge and one of the \(u_m\) local types while every other blade has the \(t_m\) type. Summing the distinct choices of exceptional blade proves (4).

## Verification
The standalone Python 3 checker `verify_edge_windmill.py` builds the polynomials from the displayed inclusion-exclusion formulas using integer arithmetic. Independently, it enumerates every subset of the actual edge set, tests the edge-domination condition directly via incidence bitmasks, and compares each cardinality coefficient and the closed optimum count. The recorded finite run reports:

`VERIFY_OK local_sizes=1..7 exhaustive_tuples=58 brute_edge_subsets=572252 dominated_sets=475022 algebraic_tuples=2..5 blades max_size=5 max_edges=19`

The finite check is not used to infer validity for unbounded blade sizes: equations (1)–(4) are established by the preceding combinatorial proof. To reproduce, run `python3 verify_edge_windmill.py` with the supplied standalone file and Python 3's standard library.

## Relationship to prior work
General edge-domination and line-graph equivalences, NP-hardness, and exact algorithms are known; see van Rooij and Bodlaender, *Exact Algorithms for Edge Domination* (2011 public version). Alaeiyan and Mohammadian's *Graph Polynomials* (2011) provides general binary-programming coefficient extraction, but not the explicit heterogeneous windmill product identity or the parity-sensitive minimum multiplicities. The published edge-domination-polynomial paper by Chaluvaraju and Chaitra (2016) describes general properties and coefficient tables for paths and cycles; its full text was not inspected, so exact completeness of this comparison is not claimed. Gupta's 2026 work states the already known **scalar** saturation number for homogeneous friendship graphs; no novelty is asserted for that scalar special case. A 2023 paper on *connected vertex-edge* domination of friendship graphs studies a different hybrid vertex-edge parameter, not sets of selected edges dominating edges. The polynomial here specializes to homogeneous windmills and stars, but the claimed contribution is the exact full enumerator and all optimum edge-set multiplicities for arbitrary heterogeneous clique blades.

## Limitations
These are exact combinatorial formulas for the specified clique-bouquet graph family, not formulas for arbitrary block graphs. The polynomial counts all edge dominating sets, including nonmatchings; it does not count solely inclusion-minimal sets or minimal maximal matchings. Full texts of some plausibly related older and the 2016 coefficient paper were not accessible, leaving a literature-coverage risk despite the explicit comparisons. The finite verifier is only a reproducibility stress test; the proof supplies the infinite-parameter justification.

## References
1. J. M. M. van Rooij and H. L. Bodlaender, “Exact Algorithms for Edge Domination,” *Algorithmica* 64 (2012), 535–563, first public online 2011-07-06, DOI: 10.1007/s00453-011-9546-x.
2. M. Alaeiyan and S. Mohammadian, “Graph Polynomials,” *International Scholarly Research Notices* (2011), article 193560, first public online 2011-08-25, DOI: 10.5402/2011/193560.
3. B. Chaluvaraju and V. Chaitra, “On coefficients of edge domination polynomial of a graph,” *Journal of Discrete Mathematical Sciences and Cryptography* 19 (2016), 413–423, DOI: 10.1080/09720529.2015.1107974.
4. J. D. Horton and K. Kilakos, “Minimum Edge Dominating Sets,” *SIAM Journal on Discrete Mathematics*, DOI: 10.1137/0406030.
5. V. S. Radhika, R. Roselin Suhi, and D. Jangiti, “Connected Vertex-Edge Dominating Sets and Connected Vertex-Edge Domination Polynomials of Friendship \(F_n\),” *Journal of Advanced Zoology* 44 (2023), DOI: 10.17762/jaz.v44i3.1677.
6. C. Gupta, “The saturation number is not bounded by the harmonic index,” arXiv:2606.15761 (2026), friendship-graph scalar comparison.
