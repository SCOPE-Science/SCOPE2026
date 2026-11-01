# Linear orbit loss and quadratic delayed waves in matching-defected cliques

## Finding
Let \(n\ge5\), let \(M\) be an arbitrary matching of size \(k\) in \(K_n\), and assume \(1\le k\le\lfloor n/2\rfloor\) and \(n-k\ge4\). On \(G=K_n\setminus M\), run synchronous three-color cyclic cellular automata: at each step a vertex in color \(c\in\mathbb Z/3\mathbb Z\) advances to \(c+1\) if and only if some *adjacent* vertex already has color \(c+1\). Let \(T(x)\) be the first time the full labelled coloring becomes periodic, and \(p(x)\) its eventual primitive temporal period. The complete six-class census is

\[
\begin{array}{c|c}
(T,p)&\#\{x:(T(x),p(x))=(T,p)\}\\\hline
(0,1)&3\\
(0,3)&3^n-3\cdot2^n+3-6k(2^{n-2}-1)\\
(1,1)&3\cdot2^n-6-6k\\
(1,3)&6k(2^{n-2}-2k)\\
(2,1)&12k\\
(2,3)&12k(k-1)
\end{array}
\]

Every orbit enters a fixed point or a primitive three-cycle by time two, and the bound two is sharp for every admitted \(k\). Thus \(F^5=F^2\). In particular, the number of distinct primitive three-cycle orbits is
\[
Q_3=3^{n-1}-2^n+1-2k(2^{n-2}-1),
\]
while exactly \(3(2^n-1)+6k\) labelled initial configurations eventually become monochromatic. Relative to the complete graph, deleting \(k\) disjoint edges removes precisely \(2k(2^{n-2}-1)\) primitive three-cycle orbits but adds only \(6k\) consensus-basin states. The count of initial configurations first entering a primitive three-cycle at time two is \(12k(k-1)\): the delayed interactions are quadratic in the number of deleted edges although orbit loss and consensus change are linear.

## Assumptions and scope
The graphs are finite, undirected, loopless, labelled, and the deleted edges share no endpoints. The condition \(n-k\ge4\) supplies at least four complete-multipartite parts (the deleted pairs and the remaining singleton vertices); two-shore graphs are excluded. A temporal three-cycle consists of three distinct labelled full-color configurations. A basin count refers to initial configurations, not to the number of eventual orbits. The dynamics is successor-contact CCA, not Greenberg–Hastings excitation or an asynchronous rule. All statements concern every initial coloring, not a typical-state approximation.

## Proof
**Local blocking rule.** Each vertex has at most one nonneighbor other than itself: its partner in the deleted matching, if any. For a coloring using all three colors, a vertex \(v\) of color \(i\) fails to advance if and only if its matched partner \(w\) is the *unique* vertex of color \(i+1\). There can be at most one such blocked vertex: if color \(j\) is unique at a vertex paired to a vertex of color \(j-1\), the only other candidate singleton colors \(j-1\) and \(j+1\) cannot simultaneously satisfy their required partner-color conditions. Without a blocked vertex, every vertex advances, so the state is already in a primitive three-cycle.

**States with one or two colors.** Three monochromatic colorings are fixed. For a state with exactly two colors, choose the unique cyclic orientation \(\{i,i+1\}\). All color-\(i+1\) vertices remain still, and all color-\(i\) vertices advance, except possibly a vertex paired with the *unique* color-\(i+1\) vertex. With no exception, consensus occurs at time one. With that exception, all vertices other than the blocked one have color \(i+1\) after one update; since \(n\ge5\), the blocked vertex sees another color-\(i+1\) neighbor and joins consensus at time two. These exceptional initial states have exactly \(6k\) choices: three cyclic color orientations, one deleted pair and two endpoint orientations. Exactly-two-color assignments number \(3(2^n-2)\), giving \((T,p)=(1,1)\) count \(3\cdot2^n-6-6k\) and an initial \(6k\) contribution to \((2,1)\).

**States with three colors.** Write the unique initial blocked pair, when it exists, as \(v=i\), \(w=i+1\), with \(w\) the unique vertex of color \(i+1\). Apart from these vertices, all \(n-2\) others have color \(i\) or \(i+2\); at least one has color \(i+2\). Let \(r\) be the number of color-\(i\) vertices other than \(v\), and \(s=n-2-r\ge1\). An initial blocked pair has \(6k(2^{n-2}-1)\) possible colorings, since two distinct blocked pairs cannot occur. Every other onto-three-coloring is immediately periodic; inclusion–exclusion counts all onto-three-colorings as \(3^n-3\cdot2^n+3\).

After one step, in the blocked case, \(v\) has color \(i\), \(w\) has color \(i+2\), the \(r\) other former color-\(i\) vertices have color \(i+1\), and all \(s\) original color-\(i+2\) vertices have color \(i\). If \(r=0\), the next update reaches consensus at color \(i\); this contributes another \(6k\) to \((2,1)\). If \(r\ge1\), all three colors remain. The only possible blocker at the new state occurs when \(r=1\) and the sole other original color-\(i\) vertex \(u\) is paired with an original color-\(i+2\) vertex \(z\). If this second blocker is absent, every vertex now advances at every subsequent step, hence \((T,p)=(1,3)\).

If the second blocker exists, the original colors on two distinct deleted pairs are \((i,i+1)\) and \((i,i+2)\), with every remaining vertex color \(i+2\). The number of these assignments is \(3\cdot(2k)\cdot2(k-1)=12k(k-1)\). After the first update, \(z\) is the only blocker. After the second update, exactly two vertices have color \(i\), exactly \(n-3\) vertices have color \(i+1\), and exactly one vertex has color \(i+2\). The singleton color-\(i+2\) vertex is paired with a color-\(i\) vertex, not its predecessor color \(i+1\); the color-\(i\) class has two vertices, and \(n-3\ge2\). Consequently no vertex is blocked, every subsequent update is a global color increment, and these \(12k(k-1)\) states have \((T,p)=(2,3)\). Subtracting the \(r=0\) and two-blocker cases from the first-blocker count leaves \(6k(2^{n-2}-2k)\) cases of \((1,3)\). All six classes are now disjoint and exhaustive, proving the theorem and exact sharpness.

**Orbit and basin counts.** Every primitive three-cycle consists of three periodic configurations, so the \((0,3)\) row divided by three gives \(Q_3\). The consensus basin is the sum of rows with eventual period one, namely \(3+(3\cdot2^n-6-6k)+12k=3(2^n-1)+6k\). For the complete graph the analogous counts are \(3^{n-1}-2^n+1\) three-cycle orbits and \(3(2^n-1)\) consensus-basin states, yielding the stated perturbation differences. For any allowed \(k\), the \((2,1)\) row is positive, so two steps are necessary in the worst case.

## Verification
Two standalone programs are provided: `verify_matching_structure.py` independently classifies states from the unique blocking-pair events, and `verify_matching_exhaustive.cpp` directly implements the neighbor-contact rule without using that classification. The first checked all \(498{,}096\) labelled states across \(30\) graph parameters up to \(n=10\); the second checked all \(1{,}560{,}978\) labelled states across \(36\) graph parameters up to \(n=11\). Both reproduced every six-class count and the iterate identity. See `verification_matching_structure.txt` and `verification_matching_exhaustive.txt`. The infinite family is proved by the blocking-pair argument above, not inferred from finite enumeration.

## Relationship to prior work
Gravner, Lyu and Sivakoff (2016) introduced the finite-graph synchronization criterion for three-color cyclic cellular automata via cycle integrals; in particular, their Theorem 3 gives synchronization by graph diameter when it occurs. That qualitative result does not provide the present labelled six-class counts, the linear response of recurrent-orbit counts to *multiple disjoint edge removals*, or the quadratic two-step delayed-wave class. A previously obtained exact treatment of complete tripartite graphs covers the boundary with three parts, and an eventual-period identity for complete multipartite graphs covers the qualitative period restriction; neither is claimed as new here. We deliberately restrict to at least four parts to keep the present new quantitative domain distinct. No new general synchronization criterion is asserted.

## Limitations
The result does not classify individual attraction-basin sizes for the separate three-cycle orbits, nor does it extend to arbitrary edge deletions with shared endpoints, general numbers of colors, or the two-shore case. The theorem has a self-contained analytic proof, but the historical novelty comparison is not an exhaustive theorem that no unknown earlier calculation exists. Numerical checks cover the stated finite sizes only; they are corroboration rather than a substitute for the family-level proof.

## References
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, publicly submitted 24 October 2016, especially Theorem 3 and Section 4. https://arxiv.org/abs/1610.07320 .
