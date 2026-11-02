# Four-color cyclic dominance on complete split graphs: antipodal activation, exact basins, and a sharp three-step clock

## Finding

For integers \(m,n\ge1\), let \(G_{m,n}=K_m\vee\overline{K_n}\). Under the synchronous four-color cyclic cellular automaton (CCA), every initial coloring reaches either a fixed configuration or a primitive four-cycle within at most three full updates. The bound is sharp exactly when \(n\ge2\); if \(n=1\), the maximum entry time is two for \(m\ge2\) and one for \(m=1\).

Let \(C\subseteq\{0,1,2,3\}\) be the colors initially present in the clique, and let \(I\) be those present in the independent set. A configuration eventually enters a primitive four-cycle **if and only if** one of the following holds:

1. \(|C|=4\);
2. \(|C|=3\) and the missing color belongs to \(I\);
3. \(C\) is one of the antipodal pairs \(\{0,2\},\{1,3\}\), and both colors of its complementary pair belong to \(I\).

All other initial configurations eventually become fixed. In particular, a four-cycle exists exactly when \(m\ge3\), or when \(m=2\) and \(n\ge2\).

Write \(W_j(r)=\sum_{k=0}^{j}(-1)^{j-k}\binom jk k^r\), the number of surjections from \(r\) labeled vertices onto a specified set of \(j\) colors. Thus \(W_2(r)=2^r-2\), \(W_3(r)=3^r-3\cdot2^r+3\), and \(W_4(r)=4^r-4\cdot3^r+6\cdot2^r-4\). Let \(N_{t,p}(m,n)\) be the number of labeled initial colorings whose *first periodic entry* occurs at time \(t\) and whose eventual least period is \(p\). The complete first-entry distribution is

\[
\begin{aligned}
N_{0,1}&=2^{m+n+1},\\
N_{1,1}&=4(2^{m+n}-3\cdot2^n+3^n+1),\\
N_{2,1}&=4\bigl((3^m-2^m)3^n-(2^m-1)(2^n+1)\bigr),\\
N_{3,1}&=4(4^n-2\cdot3^n+2^n)+4(2^m-2)(4^n-3^n-2^n+1),\\
N_{0,4}&=W_4(m)4^n+4W_3(m)(3^n-2^n)+2W_2(m)(2^n-2),\\
N_{1,4}&=4W_3(m)(4^n-2\cdot3^n+2^n)+2W_2(m)(4^n-2\cdot3^n+2).
\end{aligned}
\]

Every other \(N_{t,p}\) equals zero; these six expressions sum to \(4^{m+n}\). In particular, the basin of primitive four-cycles is

\[
B_4(m,n)=W_4(m)4^n+4W_3(m)(4^n-3^n)+2W_2(m)(4^n-2\cdot3^n+2^n),
\]

and the fixed-point basin is \(B_1(m,n)=4^{m+n}-B_4(m,n)\). The number of **distinct primitive four-cycle orbits** is \(N_{0,4}(m,n)/4\); there are exactly \(2^{m+n+1}\) fixed configurations.

For each fixed \(m\ge1\), when the independent-set size tends to infinity under uniformly sampled initial colors,

\[
\Pr(\text{eventual period }4)\longrightarrow 1-\frac{4(2^m-1)}{4^m},
\qquad
\Pr(T=3\mid\text{eventual period }1)\longrightarrow1.
\]

Thus a fixed clique core has a nontrivial, core-size-dependent persistent activity probability, while nearly every trajectory that ultimately freezes takes the full three steps once the independent set is large. If the clique size also tends to infinity, the four-cycle probability tends to one.

## Assumptions and scope

The graph is simple and undirected; the clique has \(m\) labeled vertices and the independent set has \(n\) labeled vertices, with every clique-to-independent edge present. Colors are \(\mathbb Z/4\mathbb Z\). At every synchronous update, a vertex of color \(c\) advances to \(c+1\pmod4\) if and only if **at least one open-neighborhood neighbor** currently has that successor color; otherwise it retains color \(c\). All vertices update simultaneously. The initial state is arbitrary unless probabilities are explicitly stated, in which case vertex colors are i.i.d. uniform. The first periodic entry time \(T\) is the least \(t\ge0\) for which the entire labeled state at time \(t\) lies on its eventual periodic orbit. Counts include all labeled initial states, not graph/color quotient states.

## Proof

**Exact color-cohort reduction.** Two vertices of the same initial color in the same vertex class always have equal future colors: within the independent class their neighborhoods agree, and within the clique they have equal neighborhoods except for themselves and each other; neither exceptional vertex can possess the *successor* of their common current color. Inductively, each originally occupied color cohort evolves as one representative. For any nonempty palette pair \((C,I)\), use four possible cohort representatives per class, marked absent if the initial color did not occur. If their current colors form the sets \(C_t,I_t\), then an occupied clique cohort of color \(c\) advances precisely when its successor lies in \(C_t\cup I_t\), while an independent cohort advances precisely when its successor lies in \(C_t\). These rules hold exactly for every \(m,n\ge1\), including singleton cohorts.

**Exhaustive finite dynamical lemma.** Each initial palette is a nonempty subset of four colors; there are exactly \(15^2=225\) possible ordered palette pairs. The preceding cohort rule is a deterministic transition on a finite set of at most eight tagged cohort colors. Direct complete case analysis gives only the pairs \((T,p)=(0,1),(1,1),(2,1),(3,1),(0,4),(1,4)\). The complete cardinality-stratified certificate is displayed here as six coefficient matrices. The row index is \(|C|=1,2,3,4\), and the column index is \(|I|=1,2,3,4\); each entry is the number of such palette pairs having the indicated \((T,p)\):

\[
\begin{array}{c|c}
(T,p)&(a_{ij}^{T,p})_{i,j=1}^4\\\hline
(0,1)&\begin{pmatrix}8&4&0&0\\4&2&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}\\
(1,1)&\begin{pmatrix}8&8&4&0\\8&4&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}\\
(2,1)&\begin{pmatrix}0&8&4&0\\12&20&8&0\\12&12&4&0\\0&0&0&0\end{pmatrix}\\
(3,1)&\begin{pmatrix}0&4&8&4\\0&8&12&4\\0&0&0&0\\0&0&0&0\end{pmatrix}\\
(0,4)&\begin{pmatrix}0&0&0&0\\0&2&0&0\\4&8&4&0\\4&6&4&1\end{pmatrix}\\
(1,4)&\begin{pmatrix}0&0&0&0\\0&0&4&2\\0&4&8&4\\0&0&0&0\end{pmatrix}.
\end{array}
\]

The matrices total \(225\) support pairs. The file `support_certificate.py` is a short, standalone, exhaustive verifier of the cohort map, first-entry times, periods, and all six matrices. Because the quotient follows **every initial color cohort**, not merely the current support sets, this verifies the actual labeled configuration period and does not confuse a fixed support set with a fixed colored configuration. Inspection of the \(55\) four-cycle palette pairs proves precisely the three structural activation cases in the statement.

**Counting all sizes.** Each fixed palette pair of cardinalities \((i,j)\) admits exactly \(W_i(m)W_j(n)\) labeled initial colorings. Hence \(N_{t,p}(m,n)=\sum_{i,j=1}^4a_{ij}^{T,p}W_i(m)W_j(n)\). Substituting the four elementary surjection polynomials into the displayed six matrices gives the six formulas in the Finding section. In particular, summing the four-cycle rows by clique support gives the compact expression for \(B_4\): full clique palette, the four triple palettes exposed to their missing color, and the two antipodal pairs exposed to both complements. The \((0,4)\) row counts the periodic states, and division by four counts distinct primitive orbits. The \((0,1)\) row simplifies to \(2^{m+n+1}\). For \(n\ge2\), the \((3,1)\) row is positive, establishing sharpness; for \(n=1\) its polynomial vanishes, and the remaining rows give the asserted smaller maxima. These identities are exact for **all** positive integers \(m,n\), not inferred from finite samples.

**Asymptotic limit.** Divide the formula for \(B_4(m,n)\) by \(4^{m+n}\) and hold \(m\) fixed. The terms with \(3^n\) and \(2^n\) vanish, leaving \([W_4(m)+4W_3(m)+2W_2(m)]/4^m=1-4(2^m-1)/4^m\). The fixed-basin size and the third-entry fixed count each have leading term \(4(2^m-1)4^n\); their ratio therefore tends to one. Finally the displayed formula for \(B_4\) shows \(B_4/4^{m+n}\to1\) if both \(m,n\to\infty\).

## Verification

Run `python3 support_certificate.py` to enumerate every one of the \(225\) support pairs and reproduce the six matrices. That program additionally evaluates the surjection identities for \(144\) parameter pairs as a check; the matrix derivation proves the formulas for arbitrary sizes. Compile `direct_check.cpp` with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic direct_check.cpp -o direct_check`, then run `./direct_check`: it directly evolves \(463{,}760\) labeled configurations across twenty positive-size graph pairs, without using the cohort update in its transition rule. The captured outputs `support_certificate.log` and `direct_check.log` are supplied. The two checks agree on periods, first-entry bounds, fixed states, cycle basins, and sharp third-entry counts.

## Relationship to prior work

Cyclic cellular automata and graph-based excitable media are established models. Gravner, Lyu and Sivakoff (arXiv:1610.07320v1, 24 October 2016), Section 2 and Section 6.1, establish and discuss **three-color** graph dynamics and explicitly distinguish the four-color case as lacking the same tournament expansion; their results do not specify the four-color split-graph first-entry or basin counts. Bello and Sivakoff (arXiv:2108.06404v1, 13 August 2021), Section 1, study **infinite regular trees with contact threshold at least two**, not threshold-one split graphs. Both comparisons were made from accessible complete HTML manuscripts, not abstract snippets. More general complete-tripartite four-color orbit results do not directly supply the exact first-entry distribution for the complete-split family with arbitrarily many clique singleton parts; the \(m=2\) subclass is a complete-tripartite specialization and is not independently presented as a new coarse period phenomenon. The new assertion is the support-palette mechanism, the six complete entry shells, and their sharp two-parameter probability limits.

## Limitations

The conclusions require the stated synchronous, threshold-one, open-neighborhood update, exactly four colors, and a complete split graph. They do not assert corresponding bounds for arbitrary graphs, more colors, higher thresholds, asynchronous updating, or perturbed joins. Prior-art searches and close-result comparisons cannot establish global historical uniqueness; an unindexed equivalent split-graph enumeration remains a residual risk. No independent mathematical audit has been performed.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016-10-24), https://arxiv.org/html/1610.07320v1 .
2. J. Bello, D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404v1 (2021-08-13), https://arxiv.org/html/2108.06404v1 .
