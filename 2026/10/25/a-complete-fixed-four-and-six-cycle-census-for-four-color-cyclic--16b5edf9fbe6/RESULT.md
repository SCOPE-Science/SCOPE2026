# A complete fixed-, four-, and six-cycle census for four-color cyclic competition on bicliques

## Finding
Let \(a,b\geq1\) be integers. In the synchronous four-color cyclic cellular automaton on the labelled complete bipartite graph \(K_{a,b}\), each vertex in color \(c\in\mathbb Z/4\mathbb Z\) changes to \(c+1\pmod4\) if and only if at least one neighbor has that successor color, and otherwise retains \(c\). Put
\[
U_j(n)=\sum_{i=0}^{j}(-1)^i\binom ji(j-i)^n\quad(j=2,3,4;\ n\ge1).
\]
The numbers of **labelled periodic configurations of exact primitive periods** \(1\), \(4\), and \(6\) are, respectively,
\[
\begin{aligned}
P_1(a,b)&=8+4U_2(a)+4U_2(b)+2U_2(a)U_2(b),\\
P_4(a,b)&=2U_2(a)U_2(b)+U_4(a)U_4(b),\\
P_6(a,b)&=4U_3(a)U_3(b).
\end{aligned}
\]
No other primitive periods occur, for any \(a,b\ge1\). The numbers of distinct primitive four- and six-cycles are \(P_4(a,b)/4\) and \(P_6(a,b)/6\). Four-cycles exist exactly when \(a,b\ge2\), and six-cycles exactly when \(a,b\ge3\). The six-cycle family is distinct from the all-advancing four-color rotation. Every initial configuration eventually enters one of the listed periods because the state space is finite.

## Assumptions and scope
The graph is finite, undirected, simple, loopless, with two **labelled** nonempty shores of sizes \(a,b\). Time is integer-valued, updates are simultaneous, and the contact threshold is exactly one. A periodic configuration is counted once as a complete labelled state, not as a cycle modulo time shift or graph symmetries. Surjection numbers \(U_j(n)\) count functions from an \(n\)-element labelled set **onto** a prescribed \(j\)-element color set; they are zero when \(n<j\). The case \(n\ge1\) avoids any \(0^0\) convention.

## Proof
For a configuration write \(S,T\) for its nonempty color supports on the two shores. Define, for nonempty \(T\subseteq\mathbb Z/4\mathbb Z\),
\[
f_T(c)=\begin{cases}c+1\pmod4&c+1\pmod4\in T,\\c&\text{otherwise},\end{cases}
\qquad
\Phi(S,T)=(f_T(S),f_S(T)).
\]
Every labelled state with support pair \((S,T)\) has new support pair \(\Phi(S,T)\); its individual colors advance by the same maps. Hence **all graph sizes** reduce to the \((2^4-1)^2=225\) possible ordered nonempty support pairs. The cardinalities of both supports cannot increase. In particular, on a support cycle they are constant, so every restricted map \(f_T:S\longrightarrow f_T(S)\), and similarly \(f_S:T\longrightarrow f_S(T)\), is a bijection. Therefore every surjective labelled realization of a support cycle is periodic. Its exact period equals the support-cycle length times the order of the induced return permutations on the represented colors: surjectivity prevents a nonidentity color permutation from fixing the labelled realization.

Here is the **complete** periodic-support classification. The third column counts ordered support pairs, not labelled assignments:

| Primitive labelled period | Support sizes \((|S|,|T|)\) | Support pairs | Structural description |
| --- | --- | ---: | --- |
| \(1\) | \((1,1)\) | 8 | Opposite shores are equal or antipodal singleton colors. |
| \(1\) | \((1,2)\) | 4 | One singleton and the corresponding same-parity color pair. |
| \(1\) | \((2,1)\) | 4 | The transpose family. |
| \(1\) | \((2,2)\) | 2 | Both shores are the same parity pair. |
| \(4\) | \((2,2)\) | 2 | Opposite parity pairs, exchanged in a two-step support cycle. |
| \(4\) | \((4,4)\) | 1 | All four colors on both shores; every vertex advances. |
| \(6\) | \((3,3)\) | 4 | \(S=\mathbb Z_4\setminus\{i\}\), \(T=\mathbb Z_4\setminus\{i+2\}\) for \(i\in\mathbb Z_4\). |

For the six-cycle row, one update interchanges \(S,T\); after two updates the three represented colors on each shore undergo a cyclic permutation of order three, proving primitive period six. For the two opposite-parity pairs, two updates interchange the two colors within each shore, giving primitive period four. For full supports every vertex increments, again giving primitive period four. All four fixed-support rows are fixed pointwise.

**Exhaustiveness is a finite exact verification, not sampling.** For each of the 225 nonempty ordered mask pairs, apply the displayed \(\Phi\) repeatedly and detect its eventual directed cycle; the complete resulting cycle table contains exactly the 25 periodic support pairs listed above and no others. The accompanying standalone `verify.py` implements the two finite set-image formulas directly, examines all 225 cases and asserts equality with each coefficient in the table. The proof's reduction is valid for arbitrary \(a,b\); thus the exhaustive finite support calculation certifies the infinite graph family without enumerating infinitely many labelled graphs.

Finally, a prescribed support \(S\) of size \(j\) on a labelled shore of size \(n\) has exactly \(U_j(n)\) realizations, by inclusion-exclusion. Multiplying the two shore counts and summing the table rows yields precisely \(P_1,P_4,P_6\). Each primitive orbit contains as many labelled states as its period. The existence thresholds follow from positivity of \(U_j(n)\) exactly when \(n\ge j\), together with the \((2,2)\) four-cycle row.

## Verification
Run `python3 verify.py` in the directory containing this document and the standalone verifier. It verifies the complete support directed graph and all 25 recurrent support states, then independently enumerates the labelled transition graph for every \(1\le a,b\le4\). Across these 16 profiles it checks 115,600 labelled configurations, including both smallest genuine six-cycle graphs and the full-support four-cycle regime. The expected terminal line is `FOUR_COLOR_BICLIQUE_VERIFY_OK`; the recorded output appears in `verification_output.txt`. The finite support-space proof, not the finite-size labelled-state cross-check, establishes the theorem for every \(a,b\).

## Relationship to prior work
The four-color contact rule is a special case of classical cyclic cellular automata studied by Fisch, Gravner and Griffeath [1] and Durrett and Griffeath [2]. The finite-graph and graphical-defect viewpoints in [3,4] provide context, but the inspected treatments address planar or quasi-crystalline geometries, general three-color graph dynamics, or large-scale propagation; they do not give the ordered-color-support reduction and exact \(K_{a,b}\) four-/six-cycle census here. In particular, the existence of color-wheel spirals or of longer periods in other graphs does not imply these three exact labelled-state formulas.

## Limitations
This classification is for synchronous, contact-threshold-one dynamics with exactly four colors and complete bipartite interaction; it does not assert transient-entry time bounds, basin sizes, a classification for more colors, or uniqueness relative to every unpublished historical source. The 225-state enumeration is exhaustive for the reduced support dynamics; the 115,600 labelled-state checks are corroboration only. The result has not received an independent external audit.

## References
[1] R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39, https://www.stat.cmu.edu/~cshalizi/462/readings/fgg.pdf .

[2] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv submission 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .

[3] C. A. Reiter, *Medley of Spirals from Cyclic Cellular Automata*, preprint, https://webbox.lafayette.edu/~reiterc/mvq/mscca/ms_cca2_pp.pdf .

[4] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, Annals of Applied Probability **28** (2018), 3324–3357, https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
