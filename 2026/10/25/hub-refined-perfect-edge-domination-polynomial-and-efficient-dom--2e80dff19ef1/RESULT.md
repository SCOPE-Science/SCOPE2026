# Hub-refined perfect-edge-domination polynomial and efficient domination of cycle bouquets

## Finding
Let \(B=B(\ell_1,\ldots,\ell_k)\) be the simple graph obtained by identifying one vertex \(c\) of each of \(k\geq2\) pairwise otherwise disjoint cycles of lengths \(\ell_i\geq3\). Put \(n_i=\ell_i-2\), and let \(E_c\) consist of the \(2k\) edges incident with \(c\). An edge set \(P\) is *perfect edge dominating* (PED) if every edge outside \(P\) is adjacent to exactly one edge of \(P\). Define the two-variable enumerator
\[
\mathcal E_B(z,u)=\sum_{P\text{ PED}}z^{|P|}u^{|P\cap E_c|}.
\]

For every integer \(n\geq0\), define
\[
F_n(z)=\sum_{j=0}^{\lfloor(n+1)/3\rfloor}\binom{n-2j+1}{j}z^{n-2j}.
\]
Define the following four explicit local polynomials:
\[
\begin{aligned}
G_1(z)&=z,&G_n(z)&=z^2F_{n-2}(z)\quad(n\geq2),\\
J_1(z)&=1,&J_n(z)&=zF_{n-2}(z)\quad(n\geq2),\\
H_1(z)&=H_2(z)=0,\qquad H_3(z)=z,&H_n(z)&=z^2F_{n-4}(z)\quad(n\geq4).
\end{aligned}
\]
Then the **complete cardinality-and-hub-spoke generating polynomial** is
\[
\boxed{
\mathcal E_B(z,u)=
\prod_{i=1}^kG_{n_i}(z)
+2uz\sum_{i=1}^kJ_{n_i}(z)\prod_{j\ne i}H_{n_j}(z)
+(uz)^{2k}\prod_{i=1}^kF_{n_i}(z).}
\]
In particular, the number of PED sets with exactly \(s\) chosen hub spokes vanishes unless \(s\in\{0,1,2k\}\). The specialization \(\mathcal E_B(z,1)\) enumerates PED sets by cardinality; \(\mathcal E_B(1,1)\) gives their total count.

A *dominating induced matching* (DIM) is a PED set whose edges are pairwise nonadjacent. Let \(\mu(B)\) count DIMs. An additional exact classification is
\[
\boxed{
\mu(B)=
\mathbf1_{\{\ell_i\equiv0\pmod3\ \forall i\}}
+2\sum_{i=1}^k
\mathbf1_{\{\ell_i\equiv0\pmod3,\ \ell_j\equiv2\pmod3\ \forall j\ne i\}}.}
\]
Thus every cycle bouquet with at least two petals has \(0\), \(1\), or \(2\) DIMs; in the last case exactly one petal has length divisible by three and every other petal has length congruent to two modulo three. These formulas include triangular petals and arbitrarily mixed petal lengths.

## Assumptions and scope
All graphs are finite, simple, undirected, and unweighted. Each petal is a specified cycle of length at least three; petals share precisely the single hub \(c\) and share no edges. There are at least two petals. A selected edge has no PED restriction on how many other selected edges it meets; only an *omitted* edge must meet exactly one selected edge. For a DIM, additionally no two selected edges may share an endpoint. Every edge of the graph is either one of the \(2k\) spokes or one of the \(n_i\) internal edges in a petal.

## Proof
**1. Local zero-pair lemma.** Consider a path-like row of \(n\geq0\) internal edge selection bits, where bit 1 denotes a selected edge. Suppose all zero bits must have exactly one neighboring 1 bit, and virtual bits at both ends are 1. For any maximal consecutive run of zeros, the first zero has a 1 on one side, so its other neighbor must be zero; the second zero must then have a 1 on its other side. Hence every zero run has length exactly two. Distinct such pairs are separated by at least one selected edge. Conversely, any binary word built from isolated blocks of two zeros separated by one or more ones (with possible zero pairs at the ends) satisfies the condition. The placements of \(j\) such zero-pairs among \(n\) slots have cardinality \(\binom{n-2j+1}{j}\), obtained by contracting each pair and leaving one mandatory 1 between pairs. The number of selected edges is \(n-2j\), proving the expression for \(F_n(z)\). In particular, \(F_0=1\), \(F_1=z\), \(F_2=z^2+1\); the expression also satisfies \(F_n=zF_{n-1}+zF_{n-3}\) for \(n\geq3\).

**2. Exhaustive hub state split.** Fix a PED set \(P\), and let \(s=|P\cap E_c|\). An omitted spoke shares the hub with each of the \(s\) selected spokes and shares its outer endpoint with just one internal edge. Its number of adjacent selected edges is therefore \(s\) plus either zero or one. If \(s\geq2\), no spoke can be omitted. Thus \(s\) must be \(0\), \(1\), or \(2k\). These possibilities are disjoint and exhaustive.

**3. No selected spokes.** When \(s=0\), both spokes of every petal are omitted. Each must meet exactly one selected edge, so the first and last internal edges of that petal must both be selected. If \(n_i=1\) they coincide and contribute the single monomial \(z\). If \(n_i\geq2\), fixing these two boundary edges to 1 leaves \(n_i-2\) internal edge bits with virtual selected boundary bits, counted by \(z^2F_{n_i-2}(z)\). These are exactly the factors \(G_{n_i}\). Once the spokes are all omitted, different petals have no further adjacent-edge interactions, yielding \(\prod_iG_{n_i}\).

**4. Exactly one selected spoke.** Let that spoke belong to petal \(i\), and orient this petal so its first spoke is selected and its other spoke is omitted. Every omitted spoke already meets the unique selected hub spoke; therefore the internal edge next to each omitted spoke must be unselected. In petal \(i\), this forces the last internal edge to zero. For \(n_i=1\), that is the only internal edge; the local factor is 1. For \(n_i\geq2\), its preceding internal edge must be selected to dominate the omitted last edge; the remaining \(n_i-2\) internal bits are counted by \(F_{n_i-2}\) with the appropriate selected virtual boundaries. The local factor is \(J_{n_i}\). In each other petal \(j\), *both* boundary internal edges must be omitted. For \(n_j\leq2\), no valid choice exists; for \(n_j=3\), only \(010\) is valid; for \(n_j\geq4\), the second and penultimate internal edges are both selected, leaving a word counted by \(F_{n_j-4}\). This is \(H_{n_j}\). The factor 2 is the choice of which spoke in petal \(i\) is selected, and the selected spoke contributes \(uz\). Summing over the unique selected-spoke petal proves the middle summand.

**5. All spokes selected.** When \(s=2k\), none of the spokes impose a PED condition. Each omitted internal edge must have exactly one selected adjacent edge, with both virtual boundary spokes selected. Thus the internal edge words in petal \(i\) are independently enumerated by \(F_{n_i}\). The \(2k\) selected spokes contribute \((uz)^{2k}\), yielding the last summand. Together with Steps 3--4 this proves the polynomial identity for all quantified parameters.

**6. Dominating induced matchings.** A DIM cannot have two selected spokes, so the case \(s=2k\) is impossible because \(k\geq2\). If \(s=0\), every petal has selected first and last internal edges and cannot contain adjacent selected internal edges. The unique possible bit pattern is \(1,0,0,1,0,0,\ldots,0,0,1\); it exists if and only if \(n_i\equiv1\pmod3\), equivalently \(\ell_i\equiv0\pmod3\). This gives exactly one DIM when every petal length is divisible by three.

If \(s=1\), the chosen spoke excludes its neighboring internal edge. Following the domination and nonadjacency conditions around its petal forces the unique periodic pattern \(0,0,1,0,0,1,\ldots,0\) on its internal edges, possible if and only if \(n_i\equiv1\pmod3\), equivalently \(\ell_i\equiv0\pmod3\). In every other petal, the two internal boundary edges are omitted, and nonadjacency forces the unique pattern \(0,1,0,0,1,0,\ldots,0,1,0\), possible if and only if \(n_j\equiv0\pmod3\), equivalently \(\ell_j\equiv2\pmod3\). Each eligible chosen petal permits exactly two choices of the selected spoke. With at least two petals, at most one petal can satisfy the chosen-petal condition, and the \(s=0\) and \(s=1\) cases cannot both occur. This proves the asserted formula and its range \(\{0,1,2\}\).

## Verification
The self-contained `verify.py` script constructs every simple cycle bouquet for all ordered tuples of 2--4 petal lengths in \(\{3,4,5,6,7\}\) with at most 15 total edges. It independently enumerates every subset of its edge set, directly checks the defining perfect-edge-domination condition, and independently checks whether each PED set is a matching. It compares the bivariate coefficient table and the DIM count with the two closed formulas. The executed script checked 132 bouquet tuples, 1,679 PED sets, and 30 DIMs. All comparisons succeeded; its recorded output begins `VERIFY_OK`. These finite checks corroborate, but do not prove, the unrestricted quantified statements established in the preceding argument.

Run using `python3 verify.py` from the extracted document directory. No external packages or datasets are required.

## Relationship to prior work
Grippo, Lin, Moyano and Vera (2026), arXiv:2607.03894v1, introduce a linear-time algorithm for **total counts** of perfect edge dominating sets and dominating induced matchings on generalized series-parallel graphs. Cycle bouquets belong to that more general class, so the previously known algorithm already calculates both *unrefined total counts* on each fixed instance. That coverage is explicitly acknowledged. The present result gives a *closed* independent-petal product expression for all cardinality coefficients, also recording the number of selected hub spokes, together with an exact congruence criterion and sharp 0/1/2 DIM count. The cited paper's algorithm is not claimed to be unknown, and this result does not improve its worst-case complexity. The earlier P6-free counting algorithm of Grippo, Lin and Vera (2025/2026), arXiv:2509.04598, likewise does not state this hub-refined expression. The 2002 paper of Lu, Ko and Tang established structural and weighted optimization methods on generalized series-parallel graphs; its full publisher text was not available for the final comparison.

## Limitations
The formula is for **single-hub bouquets**, not for general cactus graphs or arbitrary generalized series-parallel graphs. Counting all PED sets and DIMs in this family was already algorithmically tractable by the 2026 GSP framework; only the explicit bivariate refinement, factorization, and exact residue classification are assessed here. A formal symbolic-weight specialization of that framework could potentially yield an equivalent enumerator, and unindexed literature might contain these formulas. Independence or publication priority has not been externally certified. The supplied finite checker cannot verify arbitrarily large instances; the proofs provide the infinite claims. No independent audit has been performed.

## References
1. L. N. Grippo, M. C. Lin, V. Moyano, and C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1, initially public 2026-07-04; especially Sections 2, 4 and 5. https://arxiv.org/abs/2607.03894
2. L. N. Grippo, M. C. Lin, and C. Vera, *Perfect Edge Domination in P6-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, arXiv:2509.04598v1, initially public 2025-09-04 (revised v2 2026-03-05); Sections 2 and 6. https://arxiv.org/abs/2509.04598
3. C.-L. Lu, M.-T. Ko, and C. Y. Tang, *Perfect edge domination and efficient edge domination in graphs*, Discrete Applied Mathematics 119 (2002), 227–250. https://doi.org/10.1016/S0166-218X(01)00198-6
