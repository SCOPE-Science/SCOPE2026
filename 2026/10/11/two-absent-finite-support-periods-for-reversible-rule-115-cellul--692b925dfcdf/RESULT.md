# Two absent finite-support periods for reversible rule-115 cellular automata

## Finding

Let \(F\) be the reversible, second-order, binary cellular automaton on \((\{0,1\}^{\mathbb Z})^2\) induced by elementary rule 115. Let \(\mathcal F\) be the configurations for which **both** time layers have finite support. Its fixed-point sets satisfy the exact equalities

\[
\operatorname{Fix}(F^9)\cap\mathcal F
=\operatorname{Fix}(F^3)\cap\mathcal F,
\qquad
\operatorname{Fix}(F^{18})\cap\mathcal F
=\operatorname{Fix}(F^6)\cap\mathcal F.
\]

Consequently, **neither \(9\) nor \(18\) is a least period of a finite-support configuration**. These are exactly the two small-period gaps highlighted in Section 7 of the motivating paper, rather than an arbitrary finite range. The result concerns bi-infinite spatial configurations with finite support, not arbitrary infinite-support or spatially periodic configurations.

## Assumptions and scope

All additions and products in the following local rule are in \(\mathbb F_2\). Write the current row at integer time \(t\) as \(x_t\in\mathbb F_2^{\mathbb Z}\). The state is the pair \((x_{t-1},x_t)\), and rule 115 gives

\[
x_{t+1}(i)=x_{t-1}(i)+1+x_t(i)
+x_t(i-1)x_t(i)\bigl(1+x_t(i+1)\bigr)
\quad(i\in\mathbb Z).
\]

This is the truth-table identity \(f_{115}(a,b,c)=1+b+ab(1+c)\). The automaton is reversible because the preceding row is recovered from the current and subsequent rows using the same formula. A configuration has finite support if \(x_{-1}(i)=x_0(i)=0\) outside some finite spatial interval. \(\operatorname{Fix}(F^p)\) denotes the set of states fixed by the \(p\)-fold iterate; the displayed equalities quantify over **every** finite-support state, without any support-size bound.

## Proof

**1. Exact temporal-column reduction.** Fix a multiple \(p\) of \(3\) and an \(F^p\)-fixed configuration. Reversibility makes its bi-infinite time orbit \(p\)-periodic. Encode the time trace of spatial site \(i\) as a binary word \(b^{(i)}=(x_t(i))_{t\in\mathbb Z/p\mathbb Z}\). For adjacent columns \(a,b,c\), the local equation is equivalent, for every \(t\in\mathbb Z/p\mathbb Z\), to

\[
Q_t(b):=b_{t-1}+b_{t+1}
=1+b_t+a_tb_t(1+c_t).
\tag{1}
\]

In particular, a possible center column \(b\) must obey \(b_t=0\Longrightarrow Q_t(b)=1\). Define \(\mathcal S_p\) as **all** words satisfying this implication. Define the finite directed graph \(G_p\) on ordered pairs \((a,b)\in\mathcal S_p^2\), with \((a,b)\to(b,c)\) precisely when (1) holds in every time position. This is an exact equivalence: a bi-infinite path in \(G_p\) determines, and is determined by, a spatial configuration with time period dividing \(p\).

**2. Finite support is a rooted-return condition.** Starting with two finite-support time layers, finite propagation of the radius-one rule guarantees that for all \(0\le t<p\) the time trace agrees outside a finite spatial interval with the homogeneous zero-initial-data orbit. Its temporal column \(B_p\) has \((B_p)_t=1\) exactly when \(t\equiv1\pmod3\). Consequently, the corresponding bi-infinite spatial graph path equals the vertex \(v_p=(B_p,B_p)\) on both far tails. Conversely, any finite graph path from \(v_p\) back to \(v_p\), extended by the constant root path, gives a valid time-\(p\)-periodic trajectory with finite support at times \(-1\) and \(0\). The vertices that can occur on these paths are exactly

\[
C_p=\operatorname{Reach}_{G_p}(v_p)
\cap\operatorname{CoReach}_{G_p}(v_p).
\tag{2}
\]

**3. Exhaustive finite graph lemma.** Equation (1) admits a short exact enumeration, independently reproducible using the attached `verify.py`. For each period, enumerate every \(p\)-bit word satisfying the displayed implication, all possible directed successors and predecessors of every reachable pair, and then intersect the two reachable sets. The complete counts are:

| \(p\) | \(|\mathcal S_p|\) | forward vertices | forward edges | backward vertices | backward edges | \(|C_p|\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(3\) | 4 | 4 | 7 | 9 | 21 | 3 |
| \(6\) | 10 | 46 | 121 | 45 | 159 | 27 |
| \(9\) | 31 | 40 | 52 | 63 | 102 | 3 |
| \(18\) | 973 | 5500 | 8590 | 8235 | 17484 | 27 |

Here an edge count counts all directed edges from the visited vertices, including edges to previously visited vertices. The enumeration also determines the graph components themselves: \(C_9\) is the triple temporal repetition of \(C_3\), and \(C_{18}\) is the triple repetition of \(C_6\). Precisely, if \(\ell_k\) repeats a length-\(k\) temporal word three times, then

\[
C_9=\{(\ell_3(a),\ell_3(b)):(a,b)\in C_3\},
\quad
C_{18}=\{(\ell_6(a),\ell_6(b)):(a,b)\in C_6\}.
\tag{3}
\]

Both identities are checked **as equal sets of vertex labels**, not merely by cardinalities. A transparent exhaustive algorithm and independent candidate-generation cross-check appear in `verify.py`. Its predecessor and successor traversals examine every eligible temporal column, so they are full finite-graph enumerations, not bounded searches through spatial initial conditions.

**4. Deduction.** Every spatial temporal column of an \(F^9\)-fixed finite configuration lies in a vertex of \(C_9\), hence by (3) has period dividing \(3\). Its entire pair of spatial rows therefore repeats after three updates: \(F^3z=z\). The analogous reasoning with \(C_{18}\) shows \(F^6z=z\) whenever \(F^{18}z=z\) and \(z\in\mathcal F\). Reverse inclusions follow from divisibility of exponents. Both asserted identities are proved.

## Verification

With a standard Python 3 interpreter, run `python3 verify.py` alongside this document. The program enumerates all temporal center words (up to \(2^{18}\) candidates), constructs the exact forward and reverse root-reachable subgraphs, and verifies the two repetition identities. It uses two logically equivalent but independently implemented successor-generation methods: exhaustive tests of every candidate column and a necessary-and-sufficient bit-mask sieve. It checks the rule-115 truth table explicitly and compares the bitwise formula against all triples of admissible length-nine temporal words.

The script also checks finite-support examples: a single occupied site in both time layers has least period \(3\); two adjacent occupied sites in the current layer, with the preceding layer zero, have least period \(6\). Thus the equalities do not arise from empty or trivial fixed sets. No floating-point arithmetic, probabilistic sampling, timeout inference, or finite spatial-support cutoff is involved.

## Relationship to prior work

Formenti and Kamilya establish that all finite-support configurations of this reversible rule have periods divisible by \(3\), and they introduce a merge construction for periods. Their Section 7 explicitly reports a temporal period \(9\) found only for infinite-support configurations and identifies period \(18\) as a computationally inaccessible gap. Their published results do not assert the two fixed-set equalities proved here. The temporal-column graph is a finite-state symbolic-dynamics reduction; the distinction between known general techniques and the particular exhaustive rooted-component calculation is intentional.

## Limitations

Only the exact powers \(9\) and \(18\) are classified here, with comparison to \(3\) and \(6\); no claim is made for all multiples of \(3\) or all temporal periods. The result is restricted to binary rule 115 in the reversible second-order update and to finite-support two-layer initial states. It does not exclude period \(9\) on infinite-support configurations, which the motivating paper reports. Its finite-graph lemma is reproducible from the included code but has not undergone independent scientific validation.

## References

Formenti, Enrico, and Supreeti Kamilya. *The Curious Case of Reversible Elementary Second Order Cellular Automaton 115*. arXiv:2606.13159v1, first posted 2026-06-11; EPTCS 445 (2026), 95–103. https://arxiv.org/html/2606.13159v1 ; https://doi.org/10.4204/EPTCS.445.12 . Relevant portions: §§2–4 for the rule and background, §5 for merged periods, §§6–7 for the exact open gaps.
