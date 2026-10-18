# Exactly forty-eight rank-two theories of binary-coloured directed cycles

## Finding
Let \(\mathcal C\) consist of all finite directed cycles \(C_n\) of length \(n\geq 3\), each vertex coloured either \(0\) or \(1\). The relational language has the directed immediate-successor predicate \(S\), two unary predicates \(P_0,P_1\) partitioning the vertices, and equality; it has no linear order, distinguished origin, or counting quantifiers. Two structures are rank-two equivalent if they satisfy exactly the same first-order sentences of quantifier rank at most \(2\).

**Theorem.** Exactly \(48\) distinct rank-two theories are realized by members of \(\mathcal C\). Each has a representative of length at most \(9\), and \(9\) is optimal: exactly four theories first occur at length \(9\). The distribution of the least possible representative lengths is

| Least length | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| Number of theories | 4 | 6 | 6 | 9 | 10 | 9 | 4 |

Of the \(48\), precisely \(44\) are realized by cycles using **both** colours; the other four are the monochromatic cycles distinguished by colour and by whether their length is \(3\) or at least \(4\). Minimal witnesses for the four length-nine theories, read cyclically, are `000100111`, `000110011`, `000110111`, and `001100111`.

The full rank-two equivalence criterion is the equality of the following explicit cyclic local signatures. For a cyclic word \(w=w_0\cdots w_{n-1}\), with subscripts read modulo \(n\), put \(N_c=|\{i:w_i=c\}|\). For each vertex \(i\), let
\[
 t_i=(w_{i-1},w_i,w_{i+1}),\qquad
 M_i=\{c\in\{0,1\}:N_c-\mathbf 1_{w_{i-1}=c}-\mathbf 1_{w_i=c}-\mathbf 1_{w_{i+1}=c}>0\}.
\]
Then two such cycles have the same rank-two theory **if and only if** their sets \(\{(t_i,M_i):0\leq i<n\}\) coincide. This criterion holds for every cycle length \(n\geq3\), not only the bounded representatives.

## Assumptions and scope
All cycles are simple consistently oriented directed cycles, without loops or reciprocal pairs, and have length at least three. A colouring is a partition into the named predicates \(P_0,P_1\); either colour may be absent. A cyclic word denotes its coloured oriented cycle, and cyclic rotation gives an isomorphic structure, but reversing a word is not generally an isomorphism because the edge orientation is fixed. The logic is unrestricted first-order logic of quantifier rank at most \(2\), not two-variable counting logic \(C^2\). The language contains no successor function symbol, only its binary relational graph.

## Proof
**Step 1: The two-round local invariant.** For any finite structure \(A\) in this vocabulary and vertex \(x\), let \(Q_A(x)\) be the set of complete atomic types \(\operatorname{atp}(x,y)\) as \(y\) ranges over the domain. An atomic type records the colours of both vertices, equality, \(S(x,y)\), and \(S(y,x)\). In the two-round Ehrenfeucht--Fraïssé game, after Spoiler selects \(x\), Duplicator can answer with \(x'\) so as to survive every possible second move in either structure exactly when \(Q_A(x)=Q_B(x')\). Since Spoiler may start in either structure, the two-round theories agree exactly when
\[
\{Q_A(x):x\in A\}=\{Q_B(y):y\in B\}.
\]
This follows directly from the game rule and its quantifier-rank characterization; it does not require a counting quantifier or assume that the number of vertices of any type is preserved.

On a directed cycle of length at least three, for a chosen vertex \(i\) the other vertices fall into its unique predecessor, unique successor, and the vertices adjacent in neither direction; equality supplies the remaining atomic case. The colours of the first three positions are \(t_i\), and the set of colours present among the non-neighbours is exactly \(M_i\). Thus \(Q_A(i)\) is determined by, and determines, \((t_i,M_i)\). This proves the stated all-size criterion.

**Step 2: A finite transition system captures every cyclic word.** The formula for \(M_i\) subtracts at most three occurrences of either colour. Hence it depends on \(N_0,N_1\) only through the two values \(z=\min(N_0,4)\) and \(o=\min(N_1,4)\). It also depends on the set \(T\subseteq\{0,1\}^3\) of length-three factors of \(w\), read around the cycle.

For a linear word of length at least two, store a state \((a,b,p,q,z,o,T)\), where \(a,b\) are its first two letters, \(p,q\) its last two letters, \(z,o\) its counts of zero and one capped at four, and \(T\) is its set of internal contiguous length-three factors. The four length-two words yield four initial states, each with \(T=\varnothing\). Appending letter \(c\in\{0,1\}\) gives exactly
\[
(a,b,p,q,z,o,T)\longmapsto
(a,b,q,c,\min(4,z+\mathbf 1_{c=0}),\min(4,o+\mathbf 1_{c=1}),T\cup\{(p,q,c)\}).
\]
To close a word of length at least three into a cycle, adjoin the two wraparound factors \((p,q,a)\) and \((q,a,b)\) to \(T\). For every resulting factor \((u,v,w)\), compute the non-neighbour colour mask using \(z,o\), thereby obtaining its complete rank-two signature. These operations are exact consequences of the definitions.

**Step 3: Exhaustive closure certificate.** Applying both append operations from all four initial states until closure produces **exactly \(758\)** states. Each reachable state has a shortest linear-word witness of length at most \(15\). The transition-system proof is exhaustive because every word starts with one of the four seeds and each further letter follows the stated transition. It does not infer a global theorem merely from testing words of bounded length.

Closing the reachable states represented by length-three-or-longer words produces **exactly \(48\)** distinct local signatures. Breadth-first exploration assigns the least word length to each state, and minimizing again over the states with any particular signature gives the displayed length distribution. Four signatures require length \(9\) and admit precisely the four listed witnesses as shortest examples from the catalogue. A separate direct enumeration of all binary words through length \(15\), testing the actual two-round atomic-pair profiles, reproduces \(48\), the length distribution, and the state-closure count. Thus every cycle, however long, has the same rank-two theory as some cycle of length at most \(9\), whereas the four exhibited theories cannot have shorter representatives.

The supporting table `theory_catalogue.tsv` lists all \(48\) signatures with their shortest representatives. To reproduce the calculation with Python's standard library, execute `python verify_cycle_rank2.py` and `python verify_cycle_bruteforce.py` in a directory containing the accompanying files.

## Verification
The first program computes the exact reachable-state closure and reads off every possible cyclic rank-two signature. It prints `STATES 758`, `RANK2_THEORIES 48`, the representative-length distribution, and the four sharp witnesses. The second implementation enumerates all binary words through length \(15\), forms actual atomic-pair profile sets in the two-round game, and checks that these agree bijectively with the explicit local signatures. It independently reconstructs all \(758\) linear summary states by brute force and checks closure under both possible appended letters. Recorded outputs are `closure_output.txt` and `direct_output.txt`.

The finite calculation certifies the exact class count because the proof supplies a complete finite transition system and verifies closure. The direct word enumeration alone would **not** certify absence of new theories at larger lengths; its role is cross-checking. No assertion is made about higher quantifier ranks, arbitrary directed graphs, or counting logics.

## Relationship to prior work
Brown and Hoshino (2007) establish an all-rank Ehrenfeucht--Fraïssé classification for **uncoloured undirected** paths and cycles. Their cycle theorem has no named colours or directed-successor relation and does not tabulate the present \(48\) rank-two classes or the optimal nine-vertex bound. Weis and Immerman (2009) classify two-variable logic over **linearly ordered** words, including a successor predicate, using rankers. An oriented cycle in the present signature has no linear order or endpoints and includes the wraparound successor edge. Their structural results motivate this question but do not state the particular cyclic quotient or its exact enumeration.

The two-round game characterization itself is classical. What is asserted here as the contribution is the exact complete finite theory spectrum for the binary-coloured directed-cycle family, its intrinsic local signature, and the sharp shortest-representative bound, not the general Ehrenfeucht--Fraïssé theorem or the binary-word encoding.

## Limitations
The calculation is a classification only of rank-two theories inside the stated class of coloured oriented cycles. Equality of rank-two theories is not graph isomorphism and does not preserve cycle length. The assertion that this exact \(48\)-class census is not covered by inspected sources remains subject to possible earlier specialist tabulations or derivations not found in the searches.

## References
1. Jason Brown and Richard Hoshino, “The Ehrenfeucht--Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* 83 (2007), 193–212, published 2007-04-30. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. Philipp Weis and Neil Immerman, “Structure Theorem and Strict Alternation Hierarchy for FO2 on Words,” first publicly available as ECCC TR07-008 on 2007-01-18; later in *Logical Methods in Computer Science* 5(3:3) (2009), arXiv:0907.0616. https://eccc.weizmann.ac.il/report/2007/008/ ; https://lmcs.episciences.org/1159/pdf
