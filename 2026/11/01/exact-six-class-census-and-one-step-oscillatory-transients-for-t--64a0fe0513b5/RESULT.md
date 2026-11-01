# Exact six-class census and one-step oscillatory transients for three-color cyclic dynamics on bicliques

## Finding

Let \(K_{a,b}\) be the labelled complete bipartite graph with nonempty distinguished shores of sizes \(a,b\ge1\). Apply the synchronous three-color cyclic cellular automaton: a vertex in color \(c\in\mathbb Z/3\mathbb Z\) advances to \(c+1\) if and only if at least one neighbor already has color \(c+1\); otherwise it retains color \(c\). Let \(T\) be the first time the **entire labelled configuration** is periodic, and \(p\) its eventual least period. Write
\[
U_m=2^m-2,\qquad R_m=3^m-3\cdot2^m+3.
\]
The complete initial-state census, for all positive integers \(a,b\), is

| \((T,p)\) | Number of labelled initial configurations |
|---|---|
| \((0,1)\) | \(3\) |
| \((0,3)\) | \(R_aR_b\) |
| \((0,4)\) | \(6U_aU_b\) |
| \((1,1)\) | \(6+3(U_a+U_b+U_aU_b)\) |
| \((1,4)\) | \(3(U_aR_b+R_aU_b)\) |
| \((2,1)\) | \(6(U_a+U_b)+3(R_a+R_b)\) |

No other pair \((T,p)\) occurs. In particular, every state is periodic after at most two updates, and
\[
F^{14}=F^2.
\]
The two-update bound is sharp whenever \(\max(a,b)\ge2\). Primitive period-three and period-four orbits are present precisely when \(\min(a,b)\ge3\) and \(\min(a,b)\ge2\), respectively. Their exact numbers of distinct **orbits** are
\[
N_3=\frac{R_aR_b}{3},\qquad N_4=\frac{3U_aU_b}{2}.
\]
For independent uniform initial colors and \(\min(a,b)\to\infty\), the probability of already lying in a three-cycle tends to one. More sharply,
\[
\Pr\!\left(T=1,\ p=4\mid (T,p)\ne(0,3)\right)\longrightarrow1.
\]
Thus almost every exceptional initial configuration (outside the immediate three-cycle population) passes through exactly one nonperiodic step and then enters a four-cycle.

## Assumptions and scope

Shore vertices are individually labelled; the graph is simple, undirected, connected, and has no loops. The color set is exactly \(\{0,1,2\}\) modulo three. All updates are simultaneous and use colors from the immediately preceding time. A configuration's least period is the least positive \(p\) satisfying \(F^p(x)=x\); \(T\) is the smallest nonnegative time at which \(F^T(x)\) is periodic. Counts concern all \(3^{a+b}\) labelled initial configurations. Both shores must be nonempty; the star cases are included. No randomness is needed for the finite formulas, only for the final probabilistic asymptotic statement.

## Proof

**Support reduction.** Encode a nonempty subset \(S\subseteq\{0,1,2\}\) by the bit mask \(m(S)=\sum_{c\in S}2^c\), an integer from one through seven. Let \(A\) and \(B\) be the masks of colors present on the left and right shores. For any support mask \(B\), define
\[
\phi_B(c)=\begin{cases}c+1\pmod{3},&c+1\pmod{3}\in B,\\c,&\text{otherwise}.\end{cases}
\]
Because every vertex sees exactly the opposite shore, the next support pair is
\[
H(A,B)=\left(m(\{\phi_B(c):c\in A\}),\;m(\{\phi_A(d):d\in B\})\right).
\]
This is an exact factor of the labelled dynamics, not a probabilistic approximation.

**Complete recurrent-support classification.** Applying this displayed rule to all \(7\times7=49\) nonempty mask pairs yields a finite exhaustive classification. The recurrent support states are the three fixed pairs \((1,1),(2,2),(4,4)\), the fixed pair \((7,7)\), and three support two-cycles
\[
(3,5)\leftrightarrow(5,3),\quad
(3,6)\leftrightarrow(6,3),\quad
(5,6)\leftrightarrow(6,5).
\]
Every other support pair enters one of these cycles in one or two steps. The complete transition table, including all forty-nine images and the first periodic-entry time, is in `support_transition_table.csv`; it is directly reconstructed by `verify_cca_biclique.py`.

If both supports are the same singleton, every vertex is fixed. At \((7,7)\), each vertex sees its successor and therefore all vertices advance by one at every update, making the labelled configuration a primitive three-cycle. On the representative support pair \((A,B)=(3,5)\), the colors on the left are \(\{0,1\}\) and those on the right are \(\{0,2\}\). Directly applying the displayed local rule twice swaps \(0\leftrightarrow1\) on the left and \(0\leftrightarrow2\) on the right. The other five recurrent support phases follow by the global cyclic permutation of colors or one update of this representative. Hence on every displayed support two-cycle the two-step labelled update interchanges the two represented colors **within each shore**; both colors actually occur in each shore. Therefore the first return of the labelled configuration occurs after four updates, never after two. The same conclusion holds upon entering these supports from another pair: the labelled state is immediately periodic once the recurrent support is reached. Since no other support pair is on a cycle, the support entry time equals the labelled configuration's first periodic-entry time. This proves the six possible \((T,p)\) classes and the uniform two-update bound.

**Counting.** For a specified support of cardinality \(k\) on a labelled shore of size \(m\), the number of configurations realizing exactly that support is the onto-function count
\[
S_k(m)=\sum_{j=0}^k(-1)^j\binom kj(k-j)^m.
\]
Specifically \(S_1(m)=1\), \(S_2(m)=U_m\), and \(S_3(m)=R_m\). Directly grouping the forty-nine support pairs gives the following numbers of pairs by support-size pair \((|A|,|B|)\):

| \((T,p)\) | \((1,1)\) | \((1,2)\) | \((2,1)\) | \((2,2)\) | \((1,3)\) | \((3,1)\) | \((2,3)\) | \((3,2)\) | \((3,3)\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \((0,1)\) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| \((0,3)\) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| \((0,4)\) | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 |
| \((1,1)\) | 6 | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| \((1,4)\) | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 |
| \((2,1)\) | 0 | 6 | 6 | 0 | 3 | 3 | 0 | 0 | 0 |

Each row is weighted by \(S_{|A|}(a)S_{|B|}(b)\), giving exactly the six formulas in the finding. Their sum is \(3^{a+b}\). Since the recurrent labelled configurations of period three or four split into disjoint orbits of sizes three or four, dividing \(R_aR_b\) by three and \(6U_aU_b\) by four proves the orbit counts. The latter is integral because \(U_m\) is even for every \(m\ge1\). The \((2,1)\) row is nonempty exactly when at least one shore has at least two vertices, establishing sharpness.

**Exceptional-state concentration.** Let \(E\) denote the complement of the immediately periodic three-cycle states. The census yields
\[
\#E=3^{a+b}-R_aR_b,
\]
and the number in the one-update four-cycle class is \(3(U_aR_b+R_aU_b)\). Their difference simplifies exactly to
\[
3^{a+b}-R_aR_b-3(U_aR_b+R_aU_b)
=3(R_a+R_b)+9(2^a-1)(2^b-1).
\]
As \(\min(a,b)\to\infty\), the right-hand side is negligible compared with the denominator \(3^{a+b}-R_aR_b\): the denominator grows on the scale of \(2^a3^b+3^a2^b\), while the error is bounded by a constant multiple of \(3^a+3^b+2^{a+b}\). The displayed conditional probability therefore tends to one. Also \(R_m/3^m\to1\), proving the unconditional concentration in period three.

## Verification

The standalone standard-library script `verify_cca_biclique.py` independently simulates the full labelled synchronous update on every three-color configuration for all shore pairs \((a,b)\) with \(1\le a,b\le5\) and \(a+b\le9\), covering 72,720 labelled configurations. It compares exact first periodic-entry times and least periods to the support-map predictions. Separately, it enumerates all forty-nine support pairs, checks the cardinality table, and verifies the closed count formulas for every one of 196 shore-size pairs with \(1\le a,b\le14\). Recorded output is in `verification_output.txt`, ending `CCA_BICLIQUE_EXACT_VERIFY_OK`. The proof for arbitrary shore sizes is the finite support classification plus inclusion-exclusion; finite-size simulations corroborate, rather than substitute for, that proof.

## Relationship to prior work

Gravner, Lyu, and Sivakoff's public preprint of October 24, 2016 defines the same three-color cyclic rule and proves that, on finite connected graphs, synchronization is equivalent to an irrotational color-difference form; its Theorem 3(i) already bounds synchronization time by graph diameter. Consequently, the fact that **synchronizing** configurations on \(K_{a,b}\) do so by time two is prior-covered and is not claimed independently as new. The paper also establishes a general activity criterion for oscillating configurations. The present census instead resolves all labelled configurations into six exact transient-time and least-period classes, computes both primitive orbit populations, and gives the conditional concentration law. These quantitative and phase-entry assertions were not found in the inspected source or mathematical-record searches. Related three-color inhibitory firefly dynamics on bicliques uses a different update rule and has different transient oscillatory behavior; its results do not imply this census.

## Limitations

The theorem applies to exactly three colors and the contact threshold of one on complete bipartite graphs, not to general multipartite graphs, non-complete bipartite graphs, asynchronous updates, or threshold-two dynamics. It counts configurations and primitive recurrent orbits, not the individual basin size of every orbit. A previous unindexed equivalent classification cannot be excluded. The general synchronization-within-diameter principle and qualitative oscillation criteria are existing results, not separate original claims here.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first public arXiv posting October 24, 2016, arXiv:1610.07320, https://arxiv.org/abs/1610.07320 (definition of cyclic dynamics; Theorem 3; finite-graph discussion).
2. R. Fisch, J. Gravner, D. Griffeath, *Cyclic cellular automata in two dimensions* (1991), cited for the historical cyclic-excitation setting. The present classification concerns a different graph family.
