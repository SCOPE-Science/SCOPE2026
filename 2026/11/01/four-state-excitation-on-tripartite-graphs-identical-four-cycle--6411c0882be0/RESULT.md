# Four-state excitation on tripartite graphs: identical four-cycle orbits, different transients, and exact extinction

## Finding
For all positive integers \(a,b,c\), let \(G=K_{a,b,c}\) be the labelled loopless complete tripartite graph with three specified nonempty independent shores. Let \(F\) be synchronous threshold-one four-state Greenberg–Hastings excitation: an active or refractory vertex advances \(1\to2\to3\to0\), while a resting vertex advances \(0\to1\) exactly when it has an excited (color-\(1\)) neighbor, and otherwise remains resting. Let \(C\) be the four-color cyclic successor-contact automaton, under which a vertex advances \(h\to h+1\pmod4\) exactly when it has a neighbor of successor color.

The following statements hold simultaneously.

1. Every configuration satisfies \(F^{10}=F^6\); its first periodic-entry time is at most six. The sharp bound is five on \(K_{1,1,1}\) and six for every other positive shore-size triple. The only least periods under \(F\) are one and four, with the all-resting configuration its unique fixed point. A four-cycle exists exactly when at least one shore contains two vertices.
2. The set of **entire labelled primitive four-cycle configurations** for \(F\) equals that for \(C\). Moreover, the two maps agree at every such configuration, so their primitive four-cycle orbits, including the phase-to-phase transitions, coincide. Their off-cycle transients and other fixed configurations need not agree. The previously established four-cycle counting polynomial for \(C\) therefore also counts the four-cycles of \(F\); equality of these two graph dynamics on their four-cycle attractors is the additional assertion here.
3. Define \(U_j(n)=\sum_{h=0}^{j}(-1)^h\binom jh(j-h)^n\), the number of surjections from \(n\) labelled vertices onto \(j\) specified colors. For a sorted triple \((i,j,k)\), define
\[
M_{ijk}(a,b,c)=\sum_{(u,v,w)\in\operatorname{Perm}(i,j,k)}U_u(a)U_v(b)U_w(c),
\]
where \(\operatorname{Perm}(i,j,k)\) means the set of **distinct** permutations. With the finite coefficient table below, the total periodic-state count and the complete all-resting attraction-basin cardinality are
\[
P(a,b,c)=\sum_{i\le j\le k}p_{ijk}M_{ijk}(a,b,c),\qquad
E(a,b,c)=\sum_{i\le j\le k}e_{ijk}M_{ijk}(a,b,c).
\]
Thus the exact number of primitive four-cycle orbits is \((P(a,b,c)-1)/4\), and precisely \(E(a,b,c)\) of the \(4^{a+b+c}\) initial states eventually become entirely resting.

| Support sizes \((i,j,k)\) | Periodic coefficient \(p_{ijk}\) | Extinction coefficient \(e_{ijk}\) |
|:--|--:|--:|
| \(1,1,1\) | 1 | 64 |
| \(1,1,2\) | 4 | 88 |
| \(1,1,3\) | 0 | 52 |
| \(1,1,4\) | 0 | 12 |
| \(1,2,2\) | 16 | 98 |
| \(1,2,3\) | 8 | 44 |
| \(1,2,4\) | 0 | 7 |
| \(1,3,3\) | 12 | 12 |
| \(1,3,4\) | 4 | 0 |
| \(1,4,4\) | 4 | 0 |
| \(2,2,2\) | 42 | 108 |
| \(2,2,3\) | 32 | 42 |
| \(2,2,4\) | 6 | 4 |
| \(2,3,3\) | 36 | 12 |
| \(2,3,4\) | 12 | 0 |
| \(2,4,4\) | 6 | 0 |
| \(3,3,3\) | 36 | 4 |
| \(3,3,4\) | 12 | 0 |
| \(3,4,4\) | 4 | 0 |
| \(4,4,4\) | 1 | 0 |

For example, \(P(1,1,2)=9\), giving two primitive four-cycle orbits, while \(E(1,1,2)=240\) of the \(256\) initial states become all-resting. On \(K_{2,2,2}\), there are \(138\) primitive four-cycle orbits and \(2632\) extinguishing initial states.

For balanced shores with size \(n\to\infty\), a uniformly sampled four-color initial state obeys the sharp rare-extinction asymptotic
\[
\Pr(\mathrm{extinction})=4(27/64)^n\bigl(1+O((2/3)^n)\bigr).
\]
The leading term arises from exactly four initially occupied-support triples containing three colors on each shore that eventually extinguish; no support triple with all four colors on each shore extinguishes.

## Assumptions and scope
All vertices are labelled and the three shores are specified, nonempty and independent, with all edges between different shores. Both maps update **simultaneously** using neighbors only (no loops). A primitive period is the least positive *temporal* period of the full microscopic configuration, not that of its three shore-support sets. The first periodic-entry time is the least \(t\ge0\) for which the state at time \(t\) is periodic. The extinction basin comprises initial configurations whose orbit eventually becomes all color zero; it includes the single fixed point. There is no assumption of initially distinct colors or balanced shores except in the final asymptotic statement.

## Proof
**Exact finite support-and-representative reduction.** For each shore \(i\in\{1,2,3\}\), write \(A_i\subseteq\{0,1,2,3\}\) for its nonempty occupied-color set. A resting vertex on shore \(i\) is excited exactly when color \(1\) belongs to at least one of the other two shore supports. Consequently the complete Greenberg–Hastings successor is specified by the map
\[
h_i(z;A_1,A_2,A_3)=\begin{cases}
1,&z=0\text{ and }1\in A_j\cup A_k,\\
0,&z=0\text{ and }1\notin A_j\cup A_k,\\
z+1\pmod4,&z\in\{1,2,3\},
\end{cases}
\]
with \(\{i,j,k\}=\{1,2,3\}\), followed by \(A_i'=\{h_i(z;A):z\in A_i\}\). For \(C\), the corresponding map is \(z\mapsto z+1\pmod4\) if its successor lies in \(A_j\cup A_k\), and \(z\mapsto z\) otherwise. The crucial observation is that neither update depends on the *multiplicities* of colors within a shore. All vertices starting on the same shore with the same color follow identical histories. Thus it suffices to retain one individually labelled representative for each initially present color, including cases in which representatives later coalesce. Every possible initial configuration is represented by exactly one of \((2^4-1)^3=3375\) nonempty ordered shore-support triples and its original representatives. This reduction is exact for arbitrary positive shore sizes.

**Complete bounded certificate and uniform transient.** The included source file `gh4_tripartite_verify.py` explicitly iterates the stated maps through all \(3375\) support triples, while carrying every initial representative through ten steps. It checks, for each original representative, equality at steps six and ten. Therefore \(F^{10}=F^6\) as an identity on the **full**, not merely support-set, state space; this supplies the infinite-size proof, with the finite enumeration as the exhaustive bounded lemma. The first \(F^4\)-return times of the representative triples have exact histogram \((620,248,658,739,641,391,78)\) at times \(0,1,2,3,4,5,6\), respectively, proving the uniform cutoff. For \(K_{1,1,1}\), initial colors \((0),(1),(3)\) have first periodic entry at time five. For \(K_{1,1,2}\), the initial shore words \((0),(3),(1,2)\) extinguish exactly at time six. Duplicating color classes preserves every representative history and extends the latter sharpness example to all other shore sizes.

**True primitive cycles and inter-model coincidence.** Exactly \(620\) of the \(3375\) representative states are \(F^4\)-fixed initially. Of them only the support triple \((\{0\},\{0\},\{0\})\) is \(F\)-fixed; the certificate explicitly excludes two-step returns for every other initially recurrent representative triple. Hence their least period is four. The same certificate independently iterates \(C\) for every possible initial support triple, verifies its three-step eventual four-periodicity, and checks that the primitive-four membership tests agree for \(F\) and \(C\) on all \(3375\) cases. The two maps' immediate microscopic successors also agree on each of the \(619\) common primitive-four representative triples. Identical-support color copies evolve identically, so this proves that the entire labelled primitive-four configuration sets and their induced transitions agree for **every** shore size. The positive coefficient at support sizes \((1,1,2)\) proves the stated existence threshold; \((1,1,1)\) is the sole reachable support-size triple when all shores are singletons and has no four-cycle.

**Orbit and extinction counting.** For a prescribed occupied-color support of size \(j\) on a shore of size \(n\), inclusion–exclusion gives exactly \(U_j(n)\) microscopic assignments. Exhaustive classification yields the \(620\) initially periodic support triples and exactly \(1442\) triples whose tags have become all zero by time six. Grouping each class by sorted shore-support cardinalities gives the respective \(p_{ijk}\) and \(e_{ijk}\) coefficients shown above. Multiplying surjection counts and summing over distinct assignments of each sorted support size proves \(P\) and \(E\) exactly. Every nontrivial periodic orbit contains exactly four states, proving the orbit divisor. Since \(U_j(n)=j^n+O((j-1)^n)\) for fixed \(j\), the extinction table's unique largest exponential base on balanced shores is \(3\cdot3\cdot3=27\), from its coefficient \(e_{333}=4\). Every remaining extinction monomial has product base at most \(18\). Thus \(E(n,n,n)=4\cdot27^n(1+O((2/3)^n))\), and division by \(4^{3n}=64^n\) yields the stated asymptotic.

## Verification
Run `python3 gh4_tripartite_verify.py` using Python 3.8 or later and no third-party modules. This exhaustive certificate checks all \(3375\) support triples, all tagged representatives, the full-state iterate identity, all possible least-period conditions, both exact coefficient tables, and equality of the four-cycle sets and one-step maps between the two update rules. It separately simulates all \(353600\) labelled microscopic initial configurations across eight graph sizes from \(K_{1,1,1}\) through \(K_{3,3,3}\) and compares independent vertex-wise dynamics with the inclusion–exclusion formulas. The accompanying `gh4_tripartite_verify.out` is the actual successful checker output, terminating in `GH4_TRIPARTITE_VERIFY_OK`. Direct tests at bounded graph sizes are cross-checks, not the justification for the all-size theorem; that justification is the exact finite representative reduction.

## Relationship to prior work
Durrett and Griffeath introduced and analyzed generalized excitable cellular automata and lattice-scale wave dynamics in a public 1993 preprint [1]. Fisch and Gravner's full 1995 article [2] supplies the multicolor Greenberg–Hastings definition, analyses stable periodic objects, and studies **one-dimensional** infinite lattices, not complete tripartite labelled graphs. Gravner, Lyu and Sivakoff [3] study **three** colors on arbitrary graphs; their update concepts agree in that three-color specialization, but their theorem does not imply the present four-color six-step identity and all-state extinction census.

Two existing exact finite-family results are essential comparisons: the complete-bipartite four-state Greenberg–Hastings extinction and six-step entry classification [4], and the four-color *cyclic-contact* complete-tripartite period-four orbit census [5]. The period-four counting polynomial displayed above is numerically **identical to the already reported periodic-four polynomial in [5]** and is not claimed as a previously unknown numerical polynomial. The new inter-model result is that the corresponding **entire microscopic period-four states and phase-to-phase transitions** are common to the different maps, despite distinct transients and fixed states. In particular, [5] has a three-step universal entry cutoff, whereas the Greenberg–Hastings cutoff here is sharply six. Neither [4] (only two shores) nor [5] (different local update, no Greenberg–Hastings basin) determines the \(E(a,b,c)\) extinction polynomial or its rare-event exponent.

## Limitations
The graph family and four-state threshold-one synchronous update are essential; no theorem is asserted for arbitrary graphs, other numbers of colors, stochastic excitation, or asynchronous schedules. The equality concerns only primitive four-cycle states and their induced transitions, not all fixed or transient states. The source analysis cannot exclude an unindexed historical equivalent. The full text of the 1993 public preprint was not accessible through the attempted public HTML/PDF routes; its available abstract was used only for model genealogy, not for a whole-document novelty claim. The accessible 1995 full article was inspected for relevant definitions, objects and principal theorems. Verification is a finite exact certificate plus a reduction proof, not an independent external audit.

## References
[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first public 1993-03-22. https://arxiv.org/abs/patt-sol/9303002

[2] R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348. https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf

[3] J. Gravner, H. Lyu and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320, first public 2016-10-24. https://arxiv.org/abs/1610.07320

[4] Prior mathematical finding, *Exact extinction basins and six-step entry for four-state Greenberg–Hastings dynamics on bicliques*, identifier `aaefced5-8ffc-48ba-898f-3ad35f981f25`.

[5] Prior mathematical finding, *Sharp three-step period collapse and exact orbit counts for four-color cyclic dynamics on tripartite graphs*, identifier `a56bc883-e0df-4bd1-b2ee-cc23f563bed1`.
