# Parity transitions and an optimal strong odd-coloring census of gear graphs

## Finding
For an integer \(n\ge3\), let \(G_n\) be the gear graph with one hub \(h\), rim vertices \(v_0,\ldots,v_{n-1}\), and subdivision vertices \(w_0,\ldots,w_{n-1}\). Its edges are \(hv_i\), \(v_iw_i\), and \(w_iv_{i+1}\), with indices taken modulo \(n\). It is the wheel with every rim edge subdivided once. A **strong odd coloring** is a proper vertex coloring in which each color used in an open neighborhood occurs there an odd number of times.

**Theorem.** For every integer \(n\ge3\), the strong odd chromatic number is
\[
\chi_{\mathrm{so}}(G_n)=
\begin{cases}
3,&n\equiv2\pmod4,\\
5,&n\equiv0\pmod4,\\
6,&n=5,\\
4,&n\text{ odd and }n\ne5.
\end{cases}
\]
Every strong odd coloring belongs to exactly one of two modes: all subdivision vertices have the hub color, or none does. In the second mode, consecutive subdivision vertices have distinct colors.

Let \(N_n\) be the number of strong odd colorings with the minimum number of *named* colors \(1,\ldots,\chi_{\mathrm{so}}(G_n)\), where the graph vertices are fixed and named. Every such coloring uses all the colors. For \(n\equiv2\pmod4\), \(N_n=6\). For \(n=5\), \(N_5=49{,}680\). For odd \(n\ne5\), put \(S_0=3\), \(S_1=0\), \(S_2=-2\), and
\[
S_{r+3}=-S_{r+1}-2S_r\quad(r\ge0).
\]
Then
\[
N_n=2^n-2-3S_n+24\mathbf1_{3\mid n}.
\]
In particular, \(N_3=48\), \(N_7=168\), and \(N_9=552\).

For \(n\equiv0\pmod4\), there is also an exact constant-size matrix formula for \(N_n\). Put \(m=4\) and work in the finite group algebra
\[
\mathcal R_m=\mathbb Z[x_1,\ldots,x_m]/(x_1^2-1,\ldots,x_m^2-1).
\]
Write \(\langle F\rangle_m\) for the coefficient of \(x_1\cdots x_m\) in the unique squarefree representative of \(F\in\mathcal R_m\). Define the \(m\times m\) matrix \(A_m\), indexed by \(a,b\in[m]\), by \((A_m)_{a,b}=\mathbf1_{a\ne b}x_b\). Define the \(m(m-1)\times m(m-1)\) matrix \(B_m\), indexed by ordered pairs \((a,u)\) with \(a\ne u\), by
\[
(B_m)_{(a,u),(b,v)}
=\mathbf1_{a\ne b}\mathbf1_{u\ne b}\mathbf1_{u\ne v}x_b.
\]
(The row and column state conditions also require \(a\ne u\) and \(b\ne v\).) Then the exact enumerator is
\[
\boxed{N_n=5\left\langle\operatorname{tr}(A_4^n)+\operatorname{tr}(B_4^n)\right\rangle_4}\qquad(4\mid n).
\]
Thus \(N_4=360\), \(N_8=37{,}920\), and \(N_{12}=10{,}670{,}760\). These are exact integer matrix expressions for every such \(n\), not extrapolations from experiments.

## Assumptions and scope
All graphs are finite, undirected, and simple. The rim length satisfies \(n\ge3\). The edges and labels above specify the gear graph completely; in particular, the hub is **not** adjacent to subdivision vertices. Color names matter in \(N_n\); automorphism orbits are not being counted. A color occurs strongly oddly at a vertex precisely when its positive multiplicity among the neighbors is odd. There is no restriction on the number of times a color appears outside the neighborhoods under discussion.

## Proof
**1. Local-mode dichotomy.** Write the hub color as \(0\), and let \(a_i\) and \(b_i\) denote the colors of \(v_i\) and \(w_i\), respectively. Properness at the hub gives \(a_i\ne0\). At \(w_i\), degree two forces \(a_i\ne a_{i+1}\). At \(v_i\), the open neighborhood has color multiset \(\{0,b_{i-1},b_i\}\). Its positive color multiplicities are all odd exactly when either \(b_{i-1}=b_i=0\), or \(b_{i-1}\ne0\), \(b_i\ne0\), and \(b_{i-1}\ne b_i\). In particular a zero/nonzero boundary is impossible, and cyclic connectivity forces either all \(b_i=0\) (mode A), or all \(b_i\ne0\) with consecutive values different (mode B). In mode B, properness also forces \(b_i\notin\{a_i,a_{i+1}\}\). Conversely, these local constraints, together with the hub condition below, imply strong oddness at every vertex.

At \(h\), the neighborhood is the sequence \(a_0,\ldots,a_{n-1}\). Thus each color appearing among the \(a_i\) must occur an odd number of times. Since the \(a_i\) properly color the ordinary cycle \(C_n\), each color class has at most \(\lfloor n/2\rfloor\) vertices.

**2. Exact minimum palettes.** The rim needs at least two colors, hence the whole graph needs at least three. If \(n\) is even, the number of nonempty odd rim color classes is even. Two colors can properly color \(C_n\) only by alternating, giving two classes of size \(n/2\); these classes are odd exactly if \(n\equiv2\pmod4\). Consequently \(n\equiv0\pmod4\) requires at least four rim colors and hence at least five colors overall. If \(n\) is odd, the number of nonempty odd rim color classes is odd. At least three are needed to properly color an odd cycle. For \(n=5\), using three would force class sizes \((3,1,1)\) in some order, contradicting the independence bound \(2\). The rim therefore needs at least five colors at \(n=5\), giving a global lower bound of six. At other odd orders the lower bound is four.

All these lower bounds are realized in mode A by coloring every \(w_i\) with the hub color. Valid cyclic rim words are as follows, with distinct symbols representing distinct nonhub colors: for \(n\equiv2\pmod4\), alternate \(1,2\); for \(n=3\), use \(1,2,3\); for \(n=5\), use \(1,2,3,4,5\); for \(n=7\), use \(1,2,1,2,1,2,3\); for \(n=9\), use \(1,2,3,1,2,3,1,2,3\); and for \(n=4\), use \(1,2,3,4\). In any valid cyclic word, replace an adjacent pair \(a,b\) by \(a,b,a,b,a,b\). This adds exactly four vertices while keeping properness and adding two occurrences of each of the two colors, hence preserves odd class sizes. The seeds cover all claimed residue classes. This establishes the formula for \(\chi_{\mathrm{so}}(G_n)\).

**3. Counting for a minimal palette.** The preceding lower-bound arguments show that in a minimum coloring all \(m=\chi_{\mathrm{so}}(G_n)-1\) nonhub colors must occur on the rim, each an odd number of times. The hub has \(m+1\) independent choices of color. By the local dichotomy, the remaining possibilities split disjointly into modes A and B.

For \(n\equiv2\pmod4\), \(m=2\); the rim alternates in exactly two ways, while mode B is impossible because each \(w_i\) would need a third nonhub color distinct from the two incident rim colors. Thus \(N_n=3\cdot2=6\).

For odd \(n\ne5\), \(m=3\). In mode A, let \(D_n\) be the number of proper three-colorings of \(C_n\) in which all three named colors occur oddly. With \(\epsilon=(-1,1,1)\), form
\[
T=\begin{pmatrix}0&1&1\\-1&0&1\\-1&1&0\end{pmatrix},\qquad S_n=\operatorname{tr}(T^n).
\]
The characteristic polynomial of \(T\) is \(\lambda^3+\lambda+2\), giving the displayed recurrence and initial values. Character orthogonality on the three color-class parity bits gives, for odd \(n\),
\[
D_n=\frac{2^n-2-3S_n}{4}.
\]
Indeed, the signed proper-cycle trace with no negative sign is \(2^n-2\); the all-negative trace is its negative; and the three one-negative traces are \(S_n\), with the three two-negative traces equal to \(-S_n\). Weighting signs by their products and averaging over eight choices yields the formula.

In mode B with exactly three nonhub colors, each \(b_i\) is forced to be the third color outside \(\{a_i,a_{i+1}\}\). The condition \(b_{i-1}\ne b_i\) is equivalent to \(a_{i-1}\ne a_{i+1}\). Hence the rim is a proper three-coloring of \(C_n^2\), which exists exactly when \(3\mid n\), in which case it has exactly six named colorings: adjacent triple distinctness propagates a period-three pattern around the cycle. Thus \(N_n=4(D_n+6\mathbf1_{3\mid n})\), as asserted.

For \(n=5\), the five nonhub rim colors each occur once, giving \(5!\) possible words after fixing the hub. Each permits one mode-A coloring. By relabeling, the number of mode-B words is the same as for the rim word \(1,2,3,4,5\). Set \(L_i=[5]\setminus\{i,i+1\}\), indices modulo five. A mode-B word consists of \(b_i\in L_i\) with \(b_{i-1}\ne b_i\). Inclusion-exclusion over the five potential equalities \(b_{i-1}=b_i\) gives unsigned sums \(243,270,105,10,0,0\) for equality-edge subsets of cardinality \(0,1,2,3,4,5\), respectively. Therefore there are exactly \(243-270+105-10=68\) mode-B choices per rim word. In total \(N_5=6\cdot5!\cdot(1+68)=49{,}680\).

**4. Uniform exact transfer count.** For any minimal palette with \(m\) nonhub colors, mode A is enumerated by length-\(n\) closed walks in \(A_m\): each transition chooses the next rim color \(b\), gives it weight \(x_b\), and forces neighboring rim colors to differ. For mode B, the state \((a,u)\) means that the current rim vertex has color \(a\) and the immediately following subdivision vertex has color \(u\). A transition to \((b,v)\) enforces \(a\ne b\), \(u\ne b\), and \(u\ne v\); the state restrictions enforce \(a\ne u\) and \(b\ne v\). This is exactly the mode-B local condition proved in step 1. A length-\(n\) closed walk therefore corresponds bijectively to an admissible named cyclic coloring, with product monomial recording every rim color multiplicity. In \(\mathcal R_m\), the squarefree monomial \(x_1\cdots x_m\) occurs exactly when every rim-color count is odd. Taking its coefficient and multiplying by the choice of hub color yields the stated formula for \(N_n\) when \(4\mid n\), as well as a uniform exact formula at all orders.

## Verification
The accompanying standalone `verify.py` implements the group-algebra parity transfer count by dynamic programming on closed walks. Independently, it enumerates rim words, admissible subdivision words, and checks properness and odd multiplicities in the *actual gear graph* for orders \(3\le n\le7\) at the asserted minimum palettes. The two counts agree and give respectively \(48,360,49{,}680,6,168\) at \(n=3,4,5,6,7\). Its independent inclusion-exclusion routine reproduces the \(68\) five-rim mode-B words; the recurrence formula and transfer count agree at all odd orders \(3\le n\le39\), except the separately handled order five. The transfer check also confirms all minimum palettes through \(n=12\), and additional even families. The entire infinite statement follows from the proof above, not these finite experiments. Run `python3 verify.py` in the directory containing that file.

## Relationship to prior work
Kwon and Park introduced strong odd coloring and established sparse-graph bounds [1]. Caro, Petruševski, Škrekovski, and Tuza studied general graph classes and products [2]. Manattu, Vinay, and Lakshmanan determined the strong odd chromatic number of wheels, using odd color-class conditions together with the **distance-two** constraint on their unsubdivided rims [3]. Subdividing every rim edge produces the bipartite gear graph, where rim vertices instead require only adjacent distinctness, and where the subdivision vertices have the exact two-mode dichotomy above. The wheel value and wheel optimum-count results therefore do not imply the gear classification or the new matrix census. The graph family itself is standard [4].

## Limitations
No formula is claimed here for nonoptimal palettes, graph automorphism orbits, list coloring, or generalized Jahangir graphs other than \(G_n\). The formula for the \(4\mid n\) named optimal-coloring counts is an explicit fixed-size group-algebra matrix trace rather than an expanded constant-coefficient scalar recurrence. Although searches of published mathematical records and source texts uncovered no prior identical gear result, indexing is incomplete; an unnoticed specialized coloring result remains a priority risk. The self-review is not independent confirmation.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, first public version 22 January 2024, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, first public version 3 October 2024, https://arxiv.org/abs/2410.02336.
3. A. J. Manattu, A. Vinay, and A. Lakshmanan S, *On a conjecture about the strong odd chromatic number of planar graphs*, arXiv:2602.03259, first public version 3 February 2026, https://arxiv.org/abs/2602.03259.
4. E. W. Weisstein, *Gear Graph*, MathWorld, https://mathworld.wolfram.com/GearGraph.html.
