# Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques

## Finding

Let \(K_{a,b}\) have two nonempty, individually labelled vertex shores of sizes \(a,b\ge1\). Consider simultaneous three-color cyclic successor-contact dynamics (CCA) and the three-state Greenberg–Hastings model (GHM), both at contact threshold one. For a configuration \(x\), let \(p_C(x)\) and \(p_H(x)\) be the least eventual periods for the respective maps, and let \(T_C(x)\), \(T_H(x)\) be their first periodic-entry times.

**Period-basin coincidence:** For every \(a,b\ge1\) and every labelled initial configuration \(x\),
\[
p_C(x)=p_H(x)\in\{1,3,4\}.
\]
Write \(A,B\subseteq\{0,1,2\}\) for the two initial occupied-color sets. The common eventual period is exactly
\[
p(x)=\begin{cases}
3,&|A|=|B|=3,\\
4,&|A|,|B|\ge2,\quad A\cup B=\{0,1,2\},\quad (|A|,|B|)\ne(3,3),\\
1,&\text{otherwise}.
\end{cases}
\]

**New exact GHM transient census:** Define
\[
\alpha=2^a-2,\quad\beta=2^b-2,\quad
\rho=3^a-3\cdot2^a+3,\quad\sigma=3^b-3\cdot2^b+3.
\]
Every nonzero row of the full GHM first-entry/least-period census is

| \((T_H,p_H)\) | Number of labelled initial configurations |
|---|---|
| \((0,1)\) | \(1\) |
| \((0,3)\) | \(\rho\sigma\) |
| \((0,4)\) | \(2\alpha\beta\) |
| \((1,1)\) | \(3+2(\alpha+\beta)+\alpha\beta\) |
| \((1,4)\) | \(2\alpha\beta+\alpha\sigma+\rho\beta\) |
| \((2,1)\) | \(3+3(\alpha+\beta)+\alpha\beta+\rho+\sigma\) |
| \((2,4)\) | \(2\alpha\beta+\alpha\sigma+\rho\beta\) |
| \((3,1)\) | \(2+2(\alpha+\beta)+\alpha\beta+\rho+\sigma\) |
| \((3,4)\) | \(\alpha\sigma+\rho\beta\) |
| \((4,1)\) | \(2(\alpha+\beta)+\rho+\sigma\) |

All omitted classes are empty. Consequently \(H^{16}=H^4\) for the GHM global update \(H\), with sharp maximal transient time four whenever \(\max(a,b)\ge2\). The numbers of GHM primitive orbits of periods one, three and four are respectively
\[
1,\quad\frac{\rho\sigma}{3},\quad\frac{\alpha\beta}{2}.
\]
The previously available CCA biclique census has three fixed points, \(\rho\sigma/3\) primitive three-orbits and \(3\alpha\beta/2\) primitive four-orbits, with maximum transient two. Thus equal eventual-period basins coexist with unequal orbit multiplicities and transient depths. In fact the periodic-three configurations and transitions coincide for the two rules, and each GHM primitive four-cycle is also a CCA primitive four-cycle with the same transitions.

The common total numbers of initial configurations ending in periods one, three and four are, respectively,
\[
\begin{aligned}
B_1&=9+9(\alpha+\beta)+3\alpha\beta+3(\rho+\sigma),\\
B_3&=\rho\sigma,\\
B_4&=6\alpha\beta+3(\alpha\sigma+\rho\beta).
\end{aligned}
\]
In particular, these three basin totals sum to \(3^{a+b}\), and their equality is **pointwise**, not merely equality in distribution under random initial colors.

## Assumptions and scope

Both shores are nonempty and every edge between them is present; there are no edges within either shore. All vertices update simultaneously, and configurations are counted with individually labelled sites (no quotient by graph automorphisms). CCA updates color \(c\) to \(c+1\pmod3\) exactly when a neighbor of that successor color exists, otherwise keeping \(c\). GHM updates \(1\mapsto2\mapsto0\), and updates \(0\mapsto1\) if an excited (color-one) neighbor exists, otherwise retaining zero. The term *eventual least period* refers to the minimum positive period of the ultimate periodic orbit; \(T\) is the smallest nonnegative time for which the whole labelled configuration is periodic.

## Proof

**Exact 49-support factor.** Encode each nonempty occupied-color set by its bit mask \(m(S)=\sum_{c\in S}2^c\in\{1,\ldots,7\}\). If the two supports are \(A,B\), all vertices on one shore see precisely the colors \(B\) on the other. Define \(f_B(c)\) by the local rule, so the next support pair is exactly
\[
(A,B)\longmapsto (\{f_B(c):c\in A\},\{f_A(d):d\in B\}).
\]
The code file `verification.py` implements the two local rules independently, and `support_certificate.csv` displays **all 49** initial support pairs, their two successors, support preperiods, support-cycle lengths and the common eventual microscopic least period. These 49 cases exhaust the possible support dynamics for *every* shore size. They can also be checked directly from the displayed local rule without any asymptotic or sampling step.

**Recurrent microscopic periods.** For CCA, the recurrent support pairs are the fixed singleton pairs \((1,1),(2,2),(4,4)\), the fixed full-palette pair \((7,7)\), and three support two-cycles \((3,5)\leftrightarrow(5,3)\), \((3,6)\leftrightarrow(6,3)\), \((5,6)\leftrightarrow(6,5)\). For GHM, the recurrent support pairs are \((1,1)\), \((7,7)\) and \((3,5)\leftrightarrow(5,3)\). Every GHM support pair enters this set within four steps; every CCA support pair enters its recurrent set within two.

At \((7,7)\), every site advances at every step in *both* models, yielding exact period three. At a recurrent two-cycle of supports, the two-step update interchanges the two present colors *within each shore*: at \((3,5)\), the left shore swaps colors zero and one after two updates, and the right shore swaps zero and two. Both colors actually occur, so the labelled orbit has exact period four, never two. Cyclic color rotation gives the other CCA two-cycles; the GHM two-cycle is the displayed representative. At a fixed singleton support pair the labelled state is fixed. Since the local update restricted to every recurrent support is a bijection on the represented colors, **every** labelled configuration having that recurrent support is periodic. A nonrecurrent support precludes a periodic labelled state. Hence microscopic first-periodic-entry time equals support entry time, and the microscopic least period is as stated.

**Pointwise equality.** The 49 support cases classify the eventual period in either model solely by the displayed cardinality-and-union criterion. Equivalently, the period-three class consists of the unique full/full support pair; the period-four class consists of the six ordered pairs of *different* two-color supports and the six ordered pairs in which one shore uses two colors and the other all three. All remaining 36 support pairs reach fixed points in either model. This establishes pointwise equality of ultimate periods. Although the classification can be recovered from the 49-row table, the 49 cases are a *finite proof*, rather than a finite sample of arbitrary graph sizes.

**Exact counting and transient bound.** For any prescribed set of \(k\) colors on \(m\) labelled vertices, the number of maps onto that set is \(\sum_{j=0}^k(-1)^j\binom{k}{j}(k-j)^m\). For \(k=1,2,3\) these numbers are \(1,2^m-2,3^m-3\cdot2^m+3\). Summing these products over the GHM support pairs with each \((T,p)\) label in the 49-row certificate gives each of the ten displayed polynomial counts. Summing only by least period gives \(B_1,B_3,B_4\), independently of the model. The 49-case maximum GHM support-entry depth is four; the depth-four support pairs include one singleton and one two-color palette, realizable whenever at least one shore has at least two vertices. Each recurrent microscopic period divides 12, so \(H^{4+12}=H^4\). The fixed-point and orbit counts follow by dividing the number of periodic labelled states by their least period, with \(\alpha\beta/2\) an integer since \(2^m-2\) is even. Finally, the two models use identical local maps on the full/full support and on both phases of the GHM support two-cycle, establishing the claimed common recurrent transitions.

## Verification

Run `python3 verification.py` in the directory containing `support_certificate.csv`. The checker independently recomputes all 49 support transitions and orbit classifications, compares exact microscopic trajectories with support predictions on 145,440 labelled initial configurations across shore sizes through nine total vertices, and verifies the ten-class and six-class formula groups by support weighting for 800 additional model-and-size cases (shore sizes one through twenty). The observed terminal output is recorded in `verification_output.txt` and ends in `BICLIQUE_THREE_COLOR_VERIFY_OK`. The all-size result rests on the explicit finite-state support reduction and exact onto-map counting, not on extrapolation from microscopic tests.

## Relationship to prior work

Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, publicly posted 2016-10-24 as arXiv:1610.07320, defines both three-color rules and proves a general synchronization-versus-oscillation criterion (Theorem 3), with a diameter bound on synchronizing states. This provides important qualitative context, **not** the ten-class GHM orbit/entry census or pointwise equality of least eventual periods with CCA. A prior exact CCA biclique census (research identifier `64a0fe05-13b5-4052-a816-81f6ace14c3e`) gives its six-class transient table and primitive orbit counts; those CCA formulas are explicitly prior work here. The contribution assessed here is the GHM census and the unexpectedly identical eventual-period partition under two distinct updates, accompanied by different transient depths and four-cycle counts. Other graph rules, including inhibitory firefly and threshold-two excitation, use different updates and do not imply the present comparison.

## Limitations

The classification is restricted to three colors, threshold one, the complete bipartite interaction graph and synchronous updates. It does not claim equality of transient times, actual ultimate orbit identities for all configurations, or analogous behavior on arbitrary graphs. The recurrent three-cycle configurations agree for both models; most period-four basins reach different orbits. Published work may imply related qualitative convergence statements through broader general results; an unindexed exact GHM biclique enumeration cannot be excluded without independent literature audit. No independent audit has been performed.

## References

1. J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (first version publicly submitted 2016-10-24), subsequently *Annals of Applied Probability* 28 (2018), 3324–3357; https://arxiv.org/abs/1610.07320 ; lawful author PDF https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
2. J. M. Greenberg, S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523; https://doi.org/10.1137/0134040 .
3. Previously established exact six-class census for three-color cyclic dynamics on labelled bicliques, scientific identifier `64a0fe05-13b5-4052-a816-81f6ace14c3e` (prior unpublished mathematical statement; used for scientific overlap comparison, not claimed here).
