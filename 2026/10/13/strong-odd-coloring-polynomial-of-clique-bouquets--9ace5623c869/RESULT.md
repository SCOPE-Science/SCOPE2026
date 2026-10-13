# Strong-odd coloring polynomial of clique bouquets
## Finding
Let \(t\ge2\) and \(s_1,\ldots,s_t\ge1\). A **clique bouquet** is the graph
\[
B(s_1,\ldots,s_t)=K_1\vee(K_{s_1}\sqcup\cdots\sqcup K_{s_t}).
\]
Its central vertex is adjacent to every noncentral vertex; the \(t\) noncentral cliques are the **blades**. The empty graph between blades is intentional. Let \(F_B(q)\) denote the number of proper strong-odd colorings with colors drawn from \(\{1,\ldots,q\}\); the palette colors are named and need not all be used.

Put
\[
S=\sum_{i=1}^t s_i,
\qquad
K_{k,s}(j)=\sum_{h=0}^{s}(-1)^h\binom{j}{h}\binom{k-j}{s-h},
\]
where a binomial coefficient vanishes if its lower argument is outside its natural range.

**The full coloring polynomial** is
\[
\boxed{F_B(q)=q\sum_{k=1}^{\min\{q-1,S\}}\binom{q-1}{k}
\frac{\prod_{i=1}^t s_i!}{2^k}
\sum_{j=0}^{k}(-1)^j\binom{k}{j}\prod_{i=1}^t K_{k,s_i}(j).}
\tag{1}
\]
This expression counts every feasible coloring for every positive integer \(q\), not just optimum colorings. Every summand is an integer after the full signed sum and the factorial prefactor are taken together.

**The uniform clique-bouquet optimum** is
\[
\boxed{
\chi_{\mathrm{so}}(K_1\vee tK_s)=
\begin{cases}
s+1,&\text{if }t\text{ is odd},\\[2pt]
1+2\left\lceil\dfrac{ts}{2(t-1)}\right\rceil,&\text{if }t\text{ is even}.
\end{cases}}
\tag{2}
\]
For example, a friendship graph with \(t\ge2\) triangular blades has strong-odd chromatic number \(3\) when \(t\) is odd and \(5\) when \(t\) is even.

## Assumptions and scope
All graphs are finite and simple, and all cliques have positive order. For a graph with no isolated vertices, a vertex coloring \(c\) is **strong odd** when it is proper and, for each vertex \(v\), every color appearing in the open neighborhood \(N(v)\) appears there an odd number of times. The strong-odd chromatic number \(\chi_{\mathrm{so}}\) is the minimum number of colors in such a coloring. The theorem assumes \(t\ge2\); the polynomial expression is also meaningful for a single clique blade, but that case is not needed for the structural comparison.

The color-counting convention counts proper maps into a labeled palette and is distinct from counting partitions into unlabeled color classes. Unused palette colors are permitted.

## Proof
**Reduction to odd column sums.** In any proper coloring, the hub uses a color distinct from every blade color, and every individual blade uses pairwise distinct colors. Every noncentral vertex sees the hub and all other vertices in its own blade. Those neighbor colors are all different, so the strong-odd requirement is automatically met at every noncentral vertex. The hub sees all noncentral vertices; its strong-odd requirement holds exactly when **each peripheral color that is used appears in an odd number of distinct blades**. Thus feasible colorings are equivalent to injections of a set of colors into the ordered vertices of each blade, with all nonzero total color multiplicities odd.

**Exact enumeration.** Choose the hub color in \(q\) ways. Fix a number \(k\) of distinct peripheral colors, then choose that color set in \(\binom{q-1}{k}\) ways. The peripheral assignment enumerator on this fixed set is
\[
H(x_1,\ldots,x_k)
=\left(\prod_{i=1}^t s_i!\right)
\prod_{i=1}^t e_{s_i}(x_1,\ldots,x_k),
\]
where \(e_r\) is the elementary symmetric polynomial of degree \(r\). To see the factorial, each unordered choice of \(s_i\) colors for blade \(i\) can be bijectively assigned to its \(s_i\) labeled vertices in \(s_i!\) ways.

For any monomial in the \(k\) variables, the discrete parity projector
\[
\frac{1}{2^k}
\sum_{\epsilon\in\{-1,1\}^k}
\left(\prod_{a=1}^k\epsilon_a\right)
H(\epsilon_1,\ldots,\epsilon_k)
\]
retains that monomial precisely when each exponent is **odd** and otherwise annihilates it. Odd exponents are necessarily positive, so exactly the fixed \(k\) colors occur. If exactly \(j\) signs are negative, then
\[
e_{s_i}(\epsilon_1,\ldots,\epsilon_k)
=\sum_{h=0}^{s_i}(-1)^h\binom{j}{h}\binom{k-j}{s_i-h}
=K_{k,s_i}(j).
\]
There are \(\binom{k}{j}\) such signs, whose projector weight is \((-1)^j\). Grouping by \(j\), then summing over \(k\), proves (1). In particular, the signed expression has the required integer interpretation.

**Uniform optimum, odd number of blades.** Every blade is a clique of order \(s\), and the hub has its own color, so \(\chi_{\mathrm{so}}\ge s+1\). If \(t\) is odd, use the same \(s\) peripheral colors once in each blade and a separate hub color. Each peripheral color occurs exactly \(t\) times at the hub, an odd number; all other open neighborhoods are automatically valid. Therefore \(\chi_{\mathrm{so}}=s+1\).

**Uniform optimum, even number of blades.** Let \(t\) be even, and suppose \(k\) peripheral colors are used. Their multiplicities in the \(t\) blades are positive odd numbers, each at most \(t-1\). Since the total is \(ts\), the number \(k\) must be even and satisfies
\[
k(t-1)\ge ts.
\]
Hence the number of colors, including the hub color, is at least
\[
1+2\left\lceil\frac{ts}{2(t-1)}\right\rceil.
\tag{3}
\]

For sharpness put \(k=2\lceil ts/(2(t-1))\rceil\). It is the least even integer at least \(ts/(t-1)\), and the even integer \(ts\) bounds it above: \(k\le ts\le k(t-1)\). Thus integers \(a_1,\ldots,a_k\) exist with
\[
0\le a_j\le\frac{t-2}{2},
\qquad
\sum_{j=1}^k a_j=\frac{ts-k}{2}.
\]
Choose prospective peripheral color multiplicities
\[
d_j=1+2a_j,
\qquad 1\le d_j\le t-1,
\qquad\sum_jd_j=ts.
\]
Construct a binary \(t\)-by-\(k\) incidence matrix with column \(j\) containing exactly \(d_j\) ones, for instance by initially placing the ones in the first \(d_j\) rows. Its average row sum is \(s\). Whenever a row has more ones than another by at least two, it contains a one in some column where the smaller row has zero. Move that one to the smaller row. This keeps every column sum and every entry binary, while strictly decreasing the sum of squared row sums. Because the average row sum is the integer \(s\), the process terminates only when every row has sum exactly \(s\). Assign to each blade exactly the \(s\) colors indicated by its row. Colors are distinct within blades, and each occurs exactly \(d_j\), an odd number of times over all blades. With a separate hub color this yields a strong-odd coloring with \(k+1\) colors, meeting (3) and proving (2).

## Verification
The attached standalone program `verify.py` constructs each clique bouquet directly from its adjacency lists and evaluates the definition vertex by vertex. Separately, it evaluates formula (1) using integer binomial sums, and it constructs every uniform coloring used in the upper-bound proof.

Across \(23\) heterogeneous or uniform blade-size lists and palettes of up to six colors, its direct enumeration checks \(151{,}311\) hub-normalized proper assignments in \(138\) comparisons and agrees with the exact signed count in every case. It independently tests \(570\) uniform instances, \(2\le t\le20\) and \(1\le s\le30\), verifying the incidence-matrix construction, minimum-color identity, and vanishing of the full polynomial at one fewer color. Full output is bundled in `verify_output.txt`.

These finite computations corroborate but do not replace the unrestricted algebraic count and balancing proof.

## Relationship to prior work
Kwon and Park's initial study of strong-odd coloring (arXiv:2401.11653, first posted 22 January 2024) defines the same proper coloring condition with odd multiplicity for every color in every nonempty open neighborhood. Caro, Petruševski, Škrekovski and Tuza (arXiv:2410.02336v1, posted 3 October 2024) study structural bounds and graph families including claw-free graphs, trees, cycles, planar graphs, and graph products. Their claw-free result addresses, among other graphs, the two-blade clique bouquet; it does not determine the complete counting polynomial for arbitrary clique bouquets, and the nontrivial many-blade families with at least three blades contain an induced claw at the hub.

Manattu, Vinay, and Lakshmanan (arXiv:2602.03259v1, 2026) study particular joins involving cycles and one-point unions, distinct from a bouquet of arbitrarily sized cliques. Pradhan, Sharma, and Verma (arXiv:2610.01441v1, 1 October 2026) announce a linear-time algorithm to compute an optimal strong-odd coloring on block graphs, a superclass of clique bouquets. The available abstract does not announce a complete named-palette coloring polynomial. The full text of that potentially relevant source was not retrievable during comparison, which remains an explicit originality risk.

The present statement independently counts **all** proper strong-odd colorings on arbitrary clique bouquets and derives a closed parity-sensitive optimum for uniform blades. Related exact results for ordinary odd coloring and general-position polynomials use different coloring conditions or different invariants and do not imply the parity-incidence count.

## Limitations
Equation (1) is a finite signed binomial sum rather than a product factorization. It is exact for all positive integers \(q\), and is not claimed to give a polynomial-time evaluation in every input-encoding model.

The closed chromatic formula (2) assumes equal blade sizes. For unequal blade sizes, the exact coloring polynomial (1) applies, but no separate compact general minimization formula is asserted.

The block-graph optimization algorithm announced in 2026 was inspected at the abstract level only, because the accessible PDF and HTML endpoints failed. That access gap prevents a full comparison of its internal reductions with the uniform chromatic corollary, although the announced optimization result does not imply the complete polynomial enumeration.

Searches cannot rule out non-indexed equivalent formulas, and finite enumeration does not establish the infinite theorem.

## References
1. O. Kwon and E. Park, “Strong odd coloring of sparse graphs,” arXiv:2401.11653v1, first public 22 January 2024, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, “On strong odd colorings of graphs,” arXiv:2410.02336v1, 3 October 2024, https://arxiv.org/abs/2410.02336.
3. A. J. Manattu, A. Vinay, and A. Lakshmanan S., “On a conjecture about the strong odd chromatic number of planar graphs,” arXiv:2602.03259v1, 2026, https://arxiv.org/abs/2602.03259.
4. D. Pradhan, V. Sharma, and S. Verma, “On the Classical and Parameterized Complexity of Strong Odd Coloring,” arXiv:2610.01441v1, 1 October 2026, https://arxiv.org/abs/2610.01441. Abstract inspected; full text unavailable during the comparison.
