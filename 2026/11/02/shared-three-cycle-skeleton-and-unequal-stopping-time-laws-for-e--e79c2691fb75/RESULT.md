# Shared three-cycle skeleton and unequal stopping-time laws for excitation on friendship graphs

## Finding

For every integer \(n\ge1\), on the labelled friendship graph \(F_n\) consisting of \(n\) triangles sharing exactly one central vertex, the three-color cyclic cellular automaton (CCA) and three-state Greenberg–Hastings model (GHM) have **exactly the same primitive three-cycle configurations and exactly the same one-step action on those configurations**. Each has precisely \(3^n-1\) primitive three-cycle orbits. Their nonperiodic behavior is sharply different: CCA first enters its eventual cycle within two steps, whereas GHM may require four steps.

For \(t\ge0\), let \(D_{M,t}(n)\) be the number of all \(3^{2n+1}\) labelled initial configurations whose **first** periodic state occurs at update \(t\), under model \(M\). Every entry not displayed below is zero. The following are exact for all \(n\ge1\).

| \(t\) | CCA: \(D_{C,t}(n)\) | GHM: \(D_{G,t}(n)\) |
|---|---|---|
| 0 | \(3\cdot3^n\) | \(3^{n+1}-2\) |
| 1 | \(3\cdot6^n\) | \(6^n+4^n-3^n\) |
| 2 | \(3(9^n-6^n-3^n)\) | \(9^n-3^n+1\) |
| 3 | \(0\) | \(9^n-4^n+1\) |
| 4 | \(0\) | \(9^n-6^n-3^n\) |

Consequently, from uniformly independent initial colors, CCA's first periodic-entry time converges in probability to \(2\), whereas GHM's first periodic-entry time converges in distribution to the uniform law on \(\{2,3,4\}\). Both maxima are attained for every \(n\ge2\); for \(n=1\), the maxima are \(1\) and \(3\), respectively. The map identities are \(C_n^5=C_n^2\) and \(G_n^7=G_n^4\), with the stated sharp thresholds.

Both models also have the same set of initial configurations eventually entering three-cycles, namely those with at least one triangle whose three initial colors are distinct. This common basin criterion is already a consequence of the general cycle-circulation theorem of Gravner–Lyu–Sivakoff [1] and is used here as prior background, **not claimed as new**. The basin contains \(3(9^n-7^n)\) configurations. CCA has three monochromatic fixed points; GHM has the unique all-zero fixed point.

## Assumptions and scope

There are \(2n+1\) distinctly labelled vertices: a center \(o\), and vertices \(u_j,v_j\) for \(1\le j\le n\). Edges are exactly \(ou_j\), \(ov_j\), \(u_jv_j\). States lie in \(\{0,1,2\}\), and updates are simultaneous. Under CCA, state \(a\) advances to \(a+1\pmod3\) precisely when an adjacent state is its successor; otherwise it stays. Under GHM, \(1\mapsto2\mapsto0\) always, and \(0\mapsto1\) if and only if at least one neighbor is in state \(1\). There is no stochastic stimulus. An initial state's first periodic-entry time is the smallest \(t\ge0\) for which its image at \(t\) lies on a periodic orbit; the least period on that orbit is counted microscopically, without quotienting vertex labels.

## Proof

**Exact finite reduction.** Fix the initial central color \(c\in\{0,1,2\}\). Each triangle's two noncentral vertices have one of the nine **ordered** types \((a,b)\in\{0,1,2\}^2\). Let \(S\) be the nonempty set of types represented at least once. There are exactly \(3(2^9-1)=1533\) possible pairs \((c,S)\), independently of \(n\). At any time, all triangles of the same initial type have identical ordered states. Their updates use only their two current colors and the center; the center's next color uses only the **existence** of leaf colors in the union of the represented types. Therefore \((c,S)\), together with the explicitly propagated image of each initially represented type, determines the complete microscopic trajectory of every initial coloring with that support. This is an exact quotient for **every** number of triangles, not a finite-size sampling argument.

For each \((c,S)\) and each model, propagate the center and each represented pair type using the two rules above. The accompanying `verify.py` implements precisely these finite set and pair operations and iterates all 1533 cases. For CCA it verifies equality of the center and every represented pair at updates \(2\) and \(5\); for GHM, at \(4\) and \(7\). It additionally verifies that, for each case, the earliest \(t\) with equality of images at \(t\) and \(t+3\) is between \(0\) and the claimed bound. Equality is checked **for every initial ordered type in the support**, so no permutation or label-level period can be concealed by support collapse.

The resulting exact certificate counts how many support choices \((c,S)\) have a specified first-entry time and support size \(s\) (columns below are \(s=1,\ldots,9\)):

| Model and \(t\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CCA 0 | 9 | 9 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| CCA 1 | 18 | 45 | 60 | 45 | 18 | 3 | 0 | 0 | 0 |
| CCA 2 | 0 | 54 | 189 | 333 | 360 | 249 | 108 | 27 | 3 |
| GHM 0 | 7 | 9 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| GHM 1 | 7 | 18 | 23 | 16 | 6 | 1 | 0 | 0 | 0 |
| GHM 2 | 7 | 33 | 83 | 126 | 126 | 84 | 36 | 9 | 1 |
| GHM 3 | 6 | 30 | 80 | 125 | 126 | 84 | 36 | 9 | 1 |
| GHM 4 | 0 | 18 | 63 | 111 | 120 | 83 | 36 | 9 | 1 |

The table is fully reproducible from the small exhaustive verifier, which uses only ordinary integer operations and enumerates the finite reduction in its entirety. It is also checked separately by direct vertex-neighborhood simulation for every labelled state of sizes \(1\) through \(5\), totaling \(199287\) initial states per model across those sizes.

**Exact counting for arbitrary size.** An initial sequence of \(n\) labelled ordered pair types has support exactly a prescribed \(s\)-element subset in
\[
U_s(n)=\sum_{j=0}^s(-1)^j\binom{s}{j}(s-j)^n
\]
ways, by inclusion–exclusion. Multiplying the \(s\)-th column of each table row by \(U_s(n)\) and summing \(s=1,\ldots,9\) yields the five displayed power-sum formulas. Their sum is \(3\cdot9^n=3^{2n+1}\) in each model. This proves the exact first-entry distribution for every \(n\ge1\), not only tested values.

**Shared recurrent three-cycles.** For a fixed central color \(c\), a microscopic configuration on a primitive three-cycle has, in every petal, one of exactly three ordered pair types:
\[
(c+1,c+2),\quad(c+2,c+1),\quad(c+2,c+2)\pmod3,
\]
with at least one of the first two. The finite reduction verifies necessity; sufficiency is immediate by applying either update rule to these three types: every vertex advances by one color, and the pattern rotates after three updates. Thus the periodic-three configuration sets and their maps coincide, and there are \(3(3^n-1)\) such microscopic configurations, hence \(3^n-1\) primitive three-cycles. The one-cycle fixed-point counts follow from the update definitions. The finite certificate further verifies that the eventual period equals three precisely when some initial petal together with the center uses all three colors. This is consistent with, and independently predicted at basin level by, the prior circulation theorem [1].

**Sharpness and limiting laws.** The certificate supplies cases first entering at time two for CCA and time four for GHM with support size two, hence realizable for all \(n\ge2\) by repeating one type. At \(n=1\), the table gives the smaller exact maxima. Divide all counts by \(3\cdot9^n\); the stated asymptotic laws follow directly because every other exponential base in the entries is less than nine.

## Verification

`verify.py` is a self-contained exact Python certificate. It enumerates \(1533\) distinct initial support cases per model, checks the full labelled-type orbit identities and the entire table, and independently simulates the actual graph at all \(199287\) labelled initial configurations for each model across \(n=1,\ldots,5\). It confirms shared period-three states and their update maps, the catalyst criterion, period counts, and all stopping-time formulas. The included `verify_output.txt` records a successful execution. The exhaustive finite symbolic check, rather than the small-graph simulation, supplies the all-size statement.

## Relationship to prior work

Gravner–Lyu–Sivakoff [1], Theorem 3, characterizes whether three-color CCA or GHM on a finite connected graph synchronizes by zero circulation around initial cycles; it gives synchronization by graph diameter when circulation vanishes. For a friendship graph, this **already implies** the common oscillation-basin criterion and its probability \(1-(7/9)^n\). These facts are not offered as independently original. Their Theorem 5 also supplies a related upper bound for synchronization probability. Their result does not tabulate first-periodic-entry times, distinguish their exact law in the two models, or count the shared primitive three-cycle configurations on friendship graphs. Doba [2] independently gives a general cycle-density criterion for GHM's eventual behavior, with a walk description of excitation times, but does not provide the friendship-graph finite-time histogram or cross-model correspondence. The new contribution is the **explicit, sharp, all-size microscopic first-entry census and the contrasting limiting distributions**, together with an exact recurrent-set census.

## Limitations

The results require exactly three states, synchronous threshold-one neighbor contact, and a bouquet of triangles with one common central vertex. General connected graphs, other cycle lengths, refractory lengths, asynchronous rules, and higher thresholds are not classified. The finite certificate is exhaustive over all nine ordered pair types and all their supports; it is not a proof about arbitrary other graphs. The originality comparison does not exclude an unindexed historical treatment or an equivalent specialization of more general excitation-time formulas. No independent audit has been performed.

## References

[1] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first posted 2016-10-24. https://arxiv.org/abs/1610.07320 . Relevant: equations (1)–(2), Theorems 3 and 5, and proof of Theorem 3.

[2] N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, DOI:10.25088/ComplexSystems.27.2.101. Relevant: Sections 2, 5–7 and concluding remarks. https://content.wolfram.com/uploads/sites/13/2018/09/27-2-1.pdf .
