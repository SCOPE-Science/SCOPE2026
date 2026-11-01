# Exact period-stratified attraction basins for excitable dynamics on matched cliques

## Finding

Consider the two-clique matching graph \(G_n=K_n\square K_2\), with pairs of vertices \((A_i,B_i)\), \(1\le i\le n\), and \(n\ge2\). Under synchronous three-state threshold-one Greenberg–Hastings excitation, let \(F\) be the global update map. The states are rest \(0\), excited \(1\), refractory \(2\); excited sites become refractory, refractory sites become resting, and a resting site becomes excited exactly when at least one *open-neighborhood* neighbor is excited.

**Theorem.** For every \(n\ge2\), every configuration enters a periodic orbit after at most four updates, and the four-update bound is attained. The only least periods are \(1\), \(3\), and \(4\), with a unique fixed configuration (all zero). Let \(B_p(n)\) count all \(3^{2n}=9^n\) initial labelled states whose eventual orbit has least period \(p\). Then

\[
\begin{aligned}
B_1(n)&=3\cdot4^n+6\cdot3^n-12\cdot2^n+3,\\
B_3(n)&=9^n-9\cdot4^n+18\cdot2^n-9,\\
B_4(n)&=6(4^n-3^n-2^n+1).
\end{aligned}
\]

The numbers of distinct periodic orbits are \(C_1(n)=1\), \(C_4(n)=2^n-2\), and

\[
C_3(n)=\frac{(3^n-3\cdot2^n+3)^2+6(4^n-3\cdot3^n+3\cdot2^n-1)}{3}.
\]

In particular, there are no nontrivial three-cycles at \(n=2\), while \(C_3(n)>0\) for every \(n\ge3\). Under the uniform initial distribution,

\[
\Pr(\text{eventual least period }3)=1-9(4/9)^n+18(2/9)^n-9^{1-n}.
\]

Consequently, although both nonzero orbit types occur for large \(n\), the eventual period is three with probability tending exponentially to one. Among the exponentially rare non-three-period basins, the limiting proportion going to period four is \(2/3\).

## Assumptions and scope

The graph is finite, simple, undirected, labelled and loopless, with two complete \(n\)-vertex shores and precisely the \(n\) edges \(A_iB_i\) between shores. There is no threshold noise, spontaneous excitation, tie rule or sequential update. Every count refers to *all* initial labelled ternary configurations, not only initially recurrent configurations. The first-periodic-entry time of \(x\) is the smallest \(t\ge0\) for which \(F^t(x)\) lies on a periodic orbit. A period-three orbit consists of three distinct configurations; a period-four orbit consists of four.

## Proof

**1. An exact size-independent symbolic reduction.** At matched pair \(i\), write its type \(z_i=(a_i,b_i)\in\{0,1,2\}^2\). There are only nine possible types. Let \(S=\{z_i:1\le i\le n\}\) be their nonempty support, and define Boolean flags \(L=\mathbf1\{(1,b)\in S\}\), \(R=\mathbf1\{(a,1)\in S\}\). For each occupied pair type the update is

\[
T_{L,R}(a,b)=\bigl(\phi(a,L\lor[b=1]),\;\phi(b,R\lor[a=1])\bigr),
\]

where \(\phi(1,h)=2\), \(\phi(2,h)=0\), and \(\phi(0,h)=h\in\{0,1\}\). This follows directly from the update rule: a resting left-hand vertex sees any left-hand excitation in its clique (necessarily at a different vertex because it is resting) or its excited matched right-hand partner, and similarly on the right. Multiplicities of type occurrences do not enter this local rule. Therefore the state trajectory of each original pair type is completely determined by the initial support \(S\), for every \(n\), including when some types occur many times.

For the \(2^9-1=511\) nonempty supports, iterate the explicit function \(T_{L,R}\) simultaneously on one representative of each initially present type. The enclosed complete symbolic checker `verify_support.py` exhausts *every support* (a size-independent finite proof reduction). It verifies for each support that the vector of its original-type images at times \(4\) and \(16\) is identical and that its least period at time \(4\) is in \(\{1,3,4\}\). Hence \(F^{16}=F^4\) holds on **every** labelled \(G_n\) configuration, and the only eventual least periods are \(1\), \(3\), \(4\). No infinite-\(n\) inference from finite-\(n\) enumeration is used here.

The same complete checker gives the following **number of initial type supports**, grouped by their size and eventual least period. It checks the table by exact assertions:

| Number of occupied types \(j\) | Period 1 | Period 3 | Period 4 |
|---:|---:|---:|---:|
|1|9|0|0|
|2|24|0|12|
|3|18|48|18|
|4|3|117|6|
|5|0|126|0|
|6|0|84|0|
|7|0|36|0|
|8|0|9|0|
|9|0|1|0|

**2. Convert support counts into complete attraction-basin counts.** For a specified support with \(j\) distinct pair types, the number of labelled assignments of these types to the \(n\) matching positions, with every type present, is the surjection number

\[
U_j(n)=\sum_{k=0}^j(-1)^{j-k}\binom jk k^n.
\]

This is exactly \(j!\,S(n,j)\), but the explicit inclusion–exclusion sum requires no Stirling-number convention. Multiplying the support table entries by \(U_j(n)\) and summing over \(j\) proves the three displayed expressions for \(B_1(n),B_3(n),B_4(n)\). Their sum is \(9^n\). The same calculation shows that every update enters a periodic orbit within four steps. For sharpness, take at least one matched pair initially in state \((0,1)\) and every other pair in state \((0,0)\). Its original pair-type images evolve through the successive supports

\[
\{(0,0),(0,1)\}\to\{(0,1),(1,2)\}\to\{(1,2),(2,0)\}\to\{(2,0),(0,0)\}\to\{(0,0)\}.
\]

The first periodic configuration is reached at time \(4\), for every \(n\ge2\).

**3. Classify recurrent states.** The checker identifies precisely one fixed-point support, \(\{(0,0)\}\), so the all-zero state is the unique fixed point. It identifies exactly four period-four periodic supports:

\[
\begin{aligned}
&\{(0,1),(0,2)\},\quad\{(0,0),(1,2)\},\\
&\{(1,0),(2,0)\},\quad\{(0,0),(2,1)\}.
\end{aligned}
\]

These are the successive four phases of one family of orbits. In the first phase the left shore is entirely resting, while the right shore has both colors \(1\) and \(2\). A nonempty proper subset of matching positions determines which right-hand sites are excited; every such subset yields one distinct period-four orbit, giving \(C_4(n)=2^n-2\). This four-cycle count is a specialization of an earlier rook-graph period-four classification, and is not asserted to be new.

For every period-three periodic support, the complete nine-type check additionally verifies that every occupied site color increments by one modulo three at each step. Conversely, any coloring in which every site has a neighbor with the next cyclic color advances by one at every tick and forms a period-three orbit. On a clique containing all three colors, this condition is automatic. Neither clique can be monochromatic; two cliques both using exactly two colors cannot both satisfy the condition, since the matching requirements for the color lacking its successor contradict one another. Thus either **both** cliques use all three colors or **exactly one** clique uses two colors and the other uses all three.

In the first case, each clique has \(3^n-3\cdot2^n+3\) surjective three-colorings, so there are \((3^n-3\cdot2^n+3)^2\) periodic configurations. In the second, choose the deficient clique (two choices), its missing color (three choices), and the nonempty set of \(r\) positions with the color whose successor is missing. Their matched partners are forced to have the missing color. The remaining \(n-r\) matched partners must contain each of the other two colors at least once, giving

\[
6\sum_{r=1}^{n-2}\binom nr\left(3^{n-r}-2\cdot2^{n-r}+1\right)
=6(4^n-3\cdot3^n+3\cdot2^n-1).
\]

Every nonfixed period-three orbit contains three configurations. Dividing their total by three gives \(C_3(n)\) as displayed. The two nonfixed recurrence classes together with the support reduction exhaust all attractors.

**4. Concentration.** Direct division of the exact \(B_3(n)\) expression by \(9^n\) gives the displayed probability. Since \(B_1(n)\sim3\cdot4^n\) and \(B_4(n)\sim6\cdot4^n\), the limiting conditional non-three-period mass ratio is \(1:2\).

## Verification

`verify_support.py` runs the complete symbolic proof check for every one of the 511 nonempty type supports, asserts the 9-row table, the identity \(F^{16}=F^4\), the exact recurrent-support shapes and the basin formulas, and compares two expressions for the period-three recurrent-state census. Its output is included in `support_output.txt`.

`verify_direct.cpp` separately implements each vertex's original neighborhood update, without using the support reduction. It exhaustively enumerates every one of the \(9^n\) initial configurations for \(2\le n\le6\), checks the four-update bound and all derived formulas, and reports entrance-time distributions. Its output is included in `direct_output.txt`. Exact commands and results appear in `VERIFICATION.md`. Finite-size checks corroborate the all-size symbolic reduction but are not substituted for it.

## Relationship to prior work

Durrett and Griffeath (1993) define and study Greenberg–Hastings excitation in spatially extended lattice automata, focusing on spiral waves and threshold-range scaling. Doba (2018) proves general qualitative convergence and cycle-density criteria for three-state Greenberg–Hastings dynamics on finite connected graphs. Those general criteria are acknowledged; this theorem supplies exact all-starting-state *counts*, a uniform four-step transient bound, and a matched-clique orbit census not stated in those works.

A previously recorded theorem for Greenberg–Hastings dynamics on arbitrary rook graphs \(K_a\square K_b\) classifies primitive four-cycles and gives \((2^a-2)(2^b-2)/2\) of them. Its specialization to \(b=2\) already yields the period-four orbit count \(2^n-2\); that part is explicitly not claimed as new. The new contribution is the complete eventual-period basin stratification, sharp first-periodic-entry bound, and period-three orbit count for \(K_n\square K_2\).

## Limitations

The result concerns only the deterministic three-state, threshold-one rule on the labelled two-shore matching graph, not higher-state excitation, threshold-two excitation, random updates, other Cartesian factors, or individual attraction basins of each separate nonfixed orbit. The support table is an exhaustive finite symbolic certificate on nine pair types, and must be replayed from the enclosed code to verify the crucial nonstandard step. Independently reproducing every finite direct simulation alone would not establish the all-\(n\) theorem. Potential unindexed earlier exact basin formulas remain a historical priority risk. Independent expert auditing has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics **2** (1993), 183–208; arXiv:patt-sol/9303002 (first submission March 22, 1993), DOI 10.1080/10586458.1993.10504277. Author-hosted full text: https://sites.math.duke.edu/~rtd/reprints/paper79.pdf.
2. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126, DOI 10.25088/ComplexSystems.27.2.101; full text: https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.
3. Earlier recorded rook-graph primitive-four-cycle classification, opaque record identifier `2bb2b82d-5fac-4a5f-85a4-c319fd71a351` (scientific comparison limited to its stated claim).
