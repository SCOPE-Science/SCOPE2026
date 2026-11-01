# Six-step synchronization and polynomially rare four-cycles for firefly dynamics on cocktail-party graphs

## Finding
For every integer \(n\ge3\), let \(H_n=K_{2n}\setminus M_n\) be the cocktail-party graph formed by deleting a fixed perfect matching from the complete graph. Consider the synchronous three-color inhibitory firefly cellular automaton: colors \(0\to1\to2\to0\) advance at each update, except a color-\(2\) vertex holds at \(2\) when some adjacent vertex has color \(1\).

**Theorem.** Every initial labelled configuration on \(H_n\) is either already on a primitive four-cycle or reaches a synchronized primitive three-cycle within at most **six** updates. The only primitive four-cycle configurations are those for which exactly one deleted-edge pair has unordered colors \(\{0,2\}\), exactly one *different* deleted-edge pair has unordered colors \(\{1,2\}\), and all other pairs have colors \(\{2,2\}\). Such configurations have no strictly transient predecessors. There are exactly \(4n(n-1)\) of them, forming exactly \(n(n-1)\) distinct primitive temporal four-cycle orbits. The all-equal three-cycle is the unique primitive three-cycle orbit, and no other periodic orbits exist. The maximal first-entry time into a periodic orbit is exactly six.

Let \(N_t(n)\) denote the number of initially labelled colorings that **first synchronize** at update \(t\). The complete first-synchronization census is
\[
\begin{aligned}
N_0(n)&=3,\\
N_1(n)&=N_3(n)=4^n-2n-2,\\
N_2(n)&=9^n-(6n+8)4^{n-1}+4n^2+1,\\
N_4(n)&=2n,\\
N_5(n)&=4n4^{n-1}-4n^2+2n,\\
N_6(n)&=2n4^{n-1}-4n(n-1).
\end{aligned}
\]
In particular, \(\sum_{t=0}^6N_t(n)+4n(n-1)=9^n\). There are no first-synchronization times larger than six. Under independent uniform initial colors, the probability of an asynchronous four-cycle is exactly \(4n(n-1)/9^n\), while the probability of first synchronization at update two tends to one exponentially fast as \(n\to\infty\).

## Assumptions and scope
Vertices are labelled \(1,\ldots,2n\), with the removed edges joining the distinct pairs \((1,2),(3,4),\ldots,(2n-1,2n)\). Thus two vertices are adjacent precisely when they belong to different removed-edge pairs. Updates are simultaneous. An initial configuration is first synchronized at time \(t\) if its image after exactly \(t\) updates is constant and none of the preceding configurations is constant. Once constant, it cycles through the three uniform colors. In the exceptional class the configuration is periodic from time zero; no synchronization time is assigned to it. A primitive temporal orbit is not quotiented by graph automorphisms.

## Proof
**1. An exact six-type reduction.** Each removed-edge pair has one of the unordered color types \(00,01,02,11,12,22\). For each type \(ab\), let \(m_{ab}\) be its exact multiplicity and \(c_{ab}=\min(2,m_{ab})\). Put \(\beta=\min(2,c_{01}+2c_{11}+c_{12})\); this equals the total number of blinking vertices, capped at two. A color-\(2\) vertex sees every blinking vertex except a possible blinking partner, so its update depends only on whether \(\beta=0\), \(\beta=1\), or \(\beta=2\), and on its partner's color.

The unordered-pair update table, in the order \(00,01,02,11,12,22\), is

| \(\beta\) | \(00\) | \(01\) | \(02\) | \(11\) | \(12\) | \(22\) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| \(0\) | \(11\) | \(12\) | \(01\) | \(22\) | \(02\) | \(00\) |
| \(1\) | \(11\) | \(12\) | \(12\) | \(22\) | \(02\) | \(22\) |
| \(2\) | \(11\) | \(12\) | \(12\) | \(22\) | \(22\) | \(22\) |

For each output type the new exact multiplicity is a sum of input multiplicities. Since \(\min(2,x+y)=\min(2,\min(2,x)+\min(2,y))\) for nonnegative integers, the next capped six-vector depends only on the current capped six-vector. In particular the reduction is exact for every \(n\), not an approximation by a small graph.

**2. Exhaustive finite-state lemma and sharpness.** The standalone `check_symbolic.py` enumerates every capped vector in \(\{0,1,2\}^6\) representing at least two deleted-edge pairs: all \(3^6-7=722\) cases. It uses precisely the displayed transition table. For each vector, within six iterations it reaches either (a) a pure uniform-pair type \(00\), \(11\), or \(22\), or (b) the exceptional vector with exactly one \(02\) pair, exactly one \(12\) pair, and only \(22\) pairs otherwise. The checker also exhaustively establishes that case (b) can occur only at time zero. Its assertions test the full transition system, rather than extrapolating from finitely many graph sizes. In case (a) all vertices are synchronized, because every pair has the same repeated color; in case (b) see the following explicit calculation. The initial coloring with exactly one color-\(2\) vertex and all other vertices color \(0\) first synchronizes after six updates, for every \(n\ge3\), proving sharpness. This is also directly confirmed by the exact \(N_6(n)>0\) formula.

**3. The exceptional primitive orbit.** A pair with \(02\) and a different pair with \(12\), surrounded by \(22\), has exactly one blinker. The two mixed types exchange on each update while all \(22\) pairs remain \(22\). Within two steps, each of the two mixed pairs reverses its ordered colors, and after four steps the entire labelled configuration returns. It does not return after two steps; hence its least period is four. Choosing its two distinct distinguished pairs, and independently orienting each mixed pair, gives \(n(n-1)\cdot2\cdot2=4n(n-1)\) periodic states and \(n(n-1)\) temporal orbits.

**4. Exact generating-function census.** Assign weights \(w_{00}=w_{11}=w_{22}=1\) and \(w_{01}=w_{02}=w_{12}=2\), the numbers of ordered colorings of one pair of each type. For a capped multiplicity \(0\), \(1\), or \(2\), the exponential generating functions for labelled pairs are respectively \(1\), \(wz\), and \(e^{wz}-1-wz\). Therefore summing their products over the 722 capped vectors and assigning each to its exact first-entry outcome yields a generating function for each outcome for all \(n\) simultaneously.

Write \(y=e^z\). The complete verified outcome generating functions are
\[
\begin{aligned}
G_{3,0}&=3(y-z-1),\\
G_{3,1}=G_{3,3}&=y^4-2yz-2y+1,\\
G_{3,2}&=y^9-6y^4z-2y^4+4yz^2+4yz+y,\\
G_{3,4}&=2z(y-1),\\
G_{3,5}&=4y^4z-4yz^2-2yz-2z,\\
G_{3,6}&=2y^4z-4yz^2-2z,\\
G_{4,0}&=4yz^2.
\end{aligned}
\]
Here \(G_{p,t}\) counts initial configurations of eventual primitive period \(p\) entering their recurrent class at time \(t\). Their sum is \(e^{9z}-1-9z\), representing every labelled state on \(n\ge2\) pairs. Since \(n![z^n](z^ke^{rz})=n(n-1)\cdots(n-k+1)r^{n-k}\) when \(n\ge k\), the displayed exact formulas for \(N_t(n)\) and the four-cycle count follow. The formulas are valid on the stated \(n\ge3\) domain.

## Verification
The file `check_symbolic.py` implements the exact capped transition and integer-polynomial arithmetic without external packages. It fully enumerates 722 admissible capped vectors, asserts the six-step dichotomy and absence of nontrivial preperiodic points feeding the exceptional orbit, proves eight generating-function polynomial identities by coefficient comparison in independent formal variables \(y,z\), and verifies their labelled coefficients for 19 widths from \(n=2\) through \(n=20\). It prints `SYMBOLIC_PASS` when every assertion holds.

The independent `check_direct.cpp` uses the full labelled graph adjacency relation, not the capped update, and directly evolves all \(\sum_{n=2}^6 9^n=597861\) labelled configurations on graph sizes \(2n=4,6,8,10,12\). It checks first synchronization times, labelled exceptional cycles and all exact counts. It prints `DIRECT_PASS`. The archived executable output files record successful replay. The universal theorem follows from the exact capped-state reduction and exhaustive symbolic certificate, not from extrapolation of the direct graph tests.

## Relationship to prior work
Hanbaek Lyu introduced this discrete inhibitory firefly rule in *Synchronization of finite-state pulse-coupled oscillators* (first publicly available 2014-07-04; arXiv:1407.1103). The inspected full-text preprint defines the rule on general graphs, establishes synchrony principles for paths and trees, and mentions non-synchronizing cliques; it gives no cocktail-party graph classification. The follow-up *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees* (arXiv:1610.00837, first publicly available 2016-10-04) studies tree-network synchronization and transient complexity, not the complete multipartite family with pair parts. Results for bipartite and crown graph firefly models concern different adjacency graphs; the former has substantial asynchronous basins and the latter can exhibit distinct periodic phenomena. Their general descriptions and exact statements do not imply the above complete enumeration on \(K_{2,2,\ldots,2}\).

A three-state Greenberg–Hastings *excitation* process on the same cocktail-party graph is also distinct: refractory state updates automatically, unlike the inhibitory holding rule used here. Its results therefore do not imply those of the present firefly map. The previously known definition of the rule and its general finite-state eventual periodicity are not claimed as new.

## Limitations
The result concerns only three-color synchronous inhibitory dynamics on cocktail-party graphs with at least three removed matched pairs, with the stated labelled-state counting convention. It does not assert analogous rigidity for other color numbers, arbitrary missing-edge patterns or asynchronous updates. The finite-state proof is implemented in transparent executable code rather than as a fully handwritten 722-case table; independent human or machine verification of the certificate remains desirable. A literature search cannot exclude all unindexed equivalent work. No independent scientific audit has been performed.

## References
1. H. Lyu, *Synchronization of finite-state pulse-coupled oscillators*, arXiv:1407.1103 (initial public posting 2014-07-04; full text version 3, 2015-03-30). https://arxiv.org/abs/1407.1103
2. H. Lyu, *Time complexity of Synchronization of discrete pulse-coupled oscillators on trees*, arXiv:1610.00837 (initial public posting 2016-10-04; consulted later full-text version). https://arxiv.org/abs/1610.00837
