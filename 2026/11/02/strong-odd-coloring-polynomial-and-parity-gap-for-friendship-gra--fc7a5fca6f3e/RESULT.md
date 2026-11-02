# Strong odd-coloring polynomial and parity gap for friendship graphs

## Finding

Let \(F_m\) be the labelled friendship graph consisting of \(m\ge1\) triangles sharing one central vertex \(h\). In triangle \(i\), the other two vertices are individually distinguished as \(a_i\) and \(b_i\), and vertices from different triangles have no edge except through \(h\). A *strong odd coloring* is a proper vertex coloring in which every color appears either zero or an odd number of times in the open neighborhood of each vertex. For an integer \(q\ge1\), let \(P_m(q)\) count all strong odd colorings \(V(F_m)\to\{1,\ldots,q\}\); palette colors are named, and need not all be used.

Define, for integers \(m\ge1\) and \(k\ge2\),
\[
H_m(k)=\frac1{2^k}\sum_{j=0}^k(-1)^j\binom{k}{j}\bigl((k-2j)^2-k\bigr)^m.
\]
Then \(H_m(k)\) is a nonnegative integer, and **the complete strong odd-coloring polynomial** is
\[
\boxed{P_m(q)=q\sum_{k=2}^{\min(q-1,2m)}\binom{q-1}{k}H_m(k).}
\]
An upper summation bound less than two means an empty sum. As a function of \(q\), this is a polynomial in the binomial basis.

Its sharp chromatic and optimal-multiplicity consequences are
\[
\boxed{\chi_{\mathrm{so}}(F_m)=
\begin{cases}3,&m\text{ odd},\\5,&m\text{ even},\end{cases}}
\qquad
\boxed{P_m(\chi_{\mathrm{so}}(F_m))=
\begin{cases}
3\cdot2^m,&m\text{ odd},\\
\dfrac58\bigl(12^m+3\cdot4^m\bigr),&m\text{ even}.
\end{cases}}
\]
In particular, even a two-triangle friendship graph requires five strong odd colors, despite having ordinary chromatic number three. The counts concern labelled vertices and named colors, with no quotient by automorphisms.

## Assumptions and scope

All graphs are finite, simple and undirected. The index \(m\) counts triangles, not vertices; \(F_m\) has \(2m+1\) vertices and \(3m\) edges. All triangles share precisely the central vertex, and vertices \(a_i,b_i\) are distinct within each labelled triangle. A proper coloring assigns different colors to the endpoints of every edge. The strong odd condition is imposed for every vertex \(v\) and every color \(c\): its multiplicity in \(N(v)\) belongs to \(\{0,1,3,5,\ldots\}\). No lists, weights, edge colors, or graph-isomorphism identification are involved.

## Proof

**1. Local reduction.** Properness forces the color of \(h\) to differ from every peripheral color. In each triangle the colors of \(a_i,b_i\) must be distinct. Every noncentral vertex has exactly two neighbors, its triangle-mate and \(h\); those neighbors have distinct colors and hence each occurs exactly once. Thus the strong odd condition at every noncentral vertex is automatic for proper colorings. It remains precisely the demand that each noncentral color appearing anywhere among the \(2m\) peripheral vertices appears an odd number of times.

**2. Active-color enumeration.** Fix the color of \(h\) in \(q\) ways. Let \(k\) be the number of distinct colors used by the peripheral vertices. Choose them from the remaining \(q-1\) in \(\binom{q-1}{k}\) ways. Each triangle contributes an ordered pair \((c(a_i),c(b_i))\) of unequal colors among these \(k\) colors. The condition at \(h\) says that every one of the chosen \(k\) colors has an odd occurrence count; in particular, all are genuinely active. Since the total occurrence count is \(2m\), necessarily \(k\le2m\).

For every \(k\)-component sign vector \(\varepsilon\in\{+1,-1\}^k\), the indicator that an occurrence count \(d_c\) is odd is \((1-(-1)^{d_c})/2\). Expanding the product of these indicators and summing over all ordered unequal pairs in all \(m\) triangles gives the exact count
\[
\frac1{2^k}\sum_{\varepsilon\in\{+1,-1\}^k}
\Bigl(\prod_{c=1}^k\varepsilon_c\Bigr)
\left(\sum_{a\ne b}\varepsilon_a\varepsilon_b\right)^m.
\]
This is nonnegative and integral because it counts actual assignments. For a sign vector with exactly \(j\) negative coordinates,
\[
\sum_{a\ne b}\varepsilon_a\varepsilon_b
=\left(\sum_{a=1}^k\varepsilon_a\right)^2-k
=(k-2j)^2-k,
\]
and its product of signs is \((-1)^j\). Grouping sign vectors by \(j\) proves that their total count equals \(H_m(k)\). Summing over the chosen central and active colors gives the displayed formula for \(P_m(q)\). No finite-case extrapolation is used.

**3. Exact minimum palette.** Every \(F_m\) contains a triangle, so \(\chi_{\mathrm{so}}(F_m)\ge3\). If \(q=3\), each peripheral pair must use the two colors distinct from the central one, so both colors occur exactly \(m\) times. Thus the condition holds exactly for odd \(m\), in which case \(P_m(3)=3\cdot2^m\).

Suppose \(m\) is even. Since the total number \(2m\) of peripheral occurrences is even, the number \(k\) of odd active color multiplicities must be even. With \(q\le4\), only \(k=2\) is possible; then each of the two colors must occur once in every triangle, hence \(m\) times, contradicting oddness. Hence \(\chi_{\mathrm{so}}(F_m)\ge5\). Conversely, when \(m\ge2\) is even, put four distinct colors on the four peripheral vertices of the first two triangles, and put the same ordered pair on each subsequent pair of triangles. All four peripheral color multiplicities remain odd, so five total colors suffice.

**4. Exact optimal counts for even \(m\).** At \(q=5\), the only possible active count is \(k=4\), because \(k=2\) is impossible for even \(m\). For \(k=4\), group signs with zero, one, two, three, or four negatives. The possible ordered-pair character sums are respectively \(12,0,-4,0,12\), with binomial multiplicities \(1,4,6,4,1\). It follows that
\[
H_m(4)=\frac{2\cdot12^m+6\cdot(-4)^m}{16}
=\frac{12^m+3\cdot4^m}{8}
\quad(m\text{ even}).
\]
There are five choices of the central color and only one choice of all four remaining active colors. Hence \(P_m(5)=5H_m(4)\), establishing the claimed optimal-multiplicity formula.

## Verification

A standalone standard-library Python program, `verify_friendship.py`, accompanies this result. It independently constructs each graph and directly checks properness and the neighborhood odd-multiplicity rule for \(1\le m\le3\) and \(1\le q\le6\). Separately, a parity-state dynamic program counts allowed ordered peripheral pairs for \(1\le m\le8\) and \(1\le q\le7\) and compares them with the closed character-sum formula. The script also checks the chromatic and optimal-count corollaries in those ranges; it exits nonzero on disagreement. Representative values are \(P_2(5)=120\), \(P_3(3)=24\), \(P_4(5)=13440\), and \(P_5(3)=96\). The universal proof is the character expansion above, not the bounded checks.

## Relationship to prior work

Strong odd coloring was introduced by Kwon and Park (arXiv:2401.11653), who studied sparse graphs and degree bounds. Caro, Petruševski, Škrekovski and Tuza (arXiv:2410.02336) developed planar, tree, unicyclic and product results. Manattu, Vinay and Lakshmanan (arXiv:2602.03259, first public version 2026-02-03) study strong odd chromatic numbers of wheel-type joins and certain one-point unions, motivating a precise census for a different natural one-point union, the friendship family. Their stated one-point-union theorem concerns unions of \(C_n\vee\overline{K_2}\), not this family. The present theorem counts *all* colorings on an arbitrary named palette and gives optimal multiplicities, not just a chromatic bound. A sign-character projection is a standard enumerative method; originality is asserted for this specific graph-coloring identity and its parity consequences, not for the projection technique.

## Limitations

This theorem is restricted to friendship graphs made from identical triangles meeting in one hub. It does not prove formulas for arbitrary clique windmills, heterogeneous bouquets, general block graphs, or list colorings. It does not count equivalence classes modulo color permutations or graph symmetries. Mathematical correctness follows from the included argument and checks; historical novelty is subject to the risk of previously unlocated broader results, and no independent mathematical audit has been performed.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (first version 2024-01-22). https://arxiv.org/abs/2401.11653
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336 (first version 2024-10-03). https://arxiv.org/abs/2410.02336
3. A. J. Manattu, A. Vinay and A. Lakshmanan S, *On a conjecture about the strong odd chromatic number of planar graphs*, arXiv:2602.03259 (first version 2026-02-03). https://arxiv.org/abs/2602.03259
