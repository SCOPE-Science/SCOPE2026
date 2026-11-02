# Exact recurrence and basins on the two ten-vertex generalized Petersen graphs

## Finding

There is a sharp change in exceptional primitive excitation periods between the pentagonal prism and the Petersen graph, despite both being cubic graphs on ten vertices. For synchronous three-state Greenberg–Hastings dynamics, \(GP(5,1)\) has genuine seven-period orbits and no eight-period orbit, whereas \(GP(5,2)\) has genuine eight-period orbits and no seven-period orbit. The exact recurrence census is:

| Graph | Period 1 | Period 3 | Period 4 | Period 5 | Period 7 | Period 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \(GP(5,1)\) primitive temporal orbits | 1 | 150 | 80 | 6 | 100 | 0 |
| \(GP(5,2)\) primitive temporal orbits | 1 | 80 | 60 | 30 | 0 | 60 |

The number of initial configurations entering an orbit of each primitive period is:

| Graph | Period 1 | Period 3 | Period 4 | Period 5 | Period 7 | Period 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \(GP(5,1)\) attraction basin sizes | 8409 | 2460 | 38430 | 2190 | 7560 | 0 |
| \(GP(5,2)\) attraction basin sizes | 7839 | 4500 | 9840 | 27270 | 0 | 9600 |

The sharp maximum number of updates before periodic entry is eight on the prism, and six on the Petersen graph. There are exactly 23 and six spatial-automorphism classes of temporal cycles, respectively. By periods \((1,3,4,5,7,8)\), their numbers of geometric classes are \((1,9,6,2,5,0)\) and \((1,2,1,1,0,1)\). All counts distinguish labelled configurations, quotienting by time shifts only when counting primitive temporal orbits.

## Assumptions and scope

For \(k\in\{1,2\}\), define the undirected graph \(GP(5,k)\) on vertices \(u_i,v_i\), \(i\in\mathbb Z/5\mathbb Z\), with edges \(u_i u_{i+1}\), \(v_i v_{i+k}\), and \(u_i v_i\). It has ten vertices and fifteen edges. The case \(k=1\) is the pentagonal prism and \(k=2\) is the Petersen graph. Assign states \(x_v\in\{0,1,2\}\) and update all vertices simultaneously: states one and two advance by \(1\mapsto2\mapsto0\), and a state-zero vertex becomes state one if and only if at least one neighboring vertex currently has state one. The all-zero state is fixed. Define the first periodic entry time \(T(x)\) as the least \(t\ge0\) for which \(F^t(x)\) is periodic, and define the eventual least period \(p(x)\). A primitive temporal orbit is a directed recurrent cycle, with different starting phases identified. A geometric class is an orbit of these temporal orbits under the full graph automorphism group. No statement is made for other generalized Petersen parameters.

## Proof

**Finite exhaustive reduction.** Write each labelled state as the unique base-three integer \(s=\sum_{i=0}^{9}x_i3^i\), with \(u_0,\ldots,u_4,v_0,\ldots,v_4\) in this order. Hence the full state set is exactly \(\{0,\ldots,59048\}\), with no quotienting or symmetry assumptions. The embedded file `verification/check.py` generates the local transition on every state and checks that its entire unsigned little-endian transition array agrees byte-for-byte with `verification/transition_gp51.bin` or `verification/transition_gp52.bin` (one 32-bit destination per state). The implementation explicitly tests the degree-three graph construction and evaluates all three cases of the update rule at every vertex. The generated arrays are complete functions on the finite state set, not samples.

**Functional-graph lemma.** For any finite map \(f\colon S\to S\), iteratively delete every vertex of its directed functional graph having indegree zero. Every removed vertex is transient: it cannot belong to a directed cycle. Conversely, a remaining vertex lies on a cycle: if a noncyclic remaining vertex existed, the finite directed forest of upstream transient vertices would have a vertex of indegree zero. The remaining subgraph is therefore a disjoint union of simple directed cycles. Enumerating these cycles determines all primitive periods and orbit counts. Processing the deleted vertices in reverse removal order gives \(T(x)=1+T(f(x))\) and \(p(x)=p(f(x))\); on cycles \(T=0\). This determines all basin counts and entrance times without assumptions about an eventual cutoff.

**Complete certificate evaluation.** `verification/check.py` applies this lemma to all \(59049\) states for each graph and obtains exactly the two tables above. The periodic-state totals are \(1501\) and \(1111\), respectively, and each basin table sums to \(59049\). The full matrix \(\#\{x:T(x)=t,p(x)=q\}\) for every occurring pair is in `verification/python_results.json`. It has maximum nonzero \(t\) equal to eight for the prism and six for the Petersen graph. Two sharp witnesses, encoded in the same base-three convention, have initial decimal states \(1181\) and \(1423\), respectively. Their full preperiodic paths are included in `verification/python_results.json` and directly checked against the transition arrays. Primitive period-seven and period-eight witnesses are included there as complete state traces as well.

**Spatial symmetry quotient.** The checker enumerates all graph automorphisms by exhaustive backtracking through adjacency-preserving bijections of the ten vertices. These groups have orders \(20\) and \(120\). It applies every permutation to the entire temporal orbit, not merely to one fixed phase, and partitions the temporal cycles by resulting group orbits. For \(GP(5,1)\), the orbit-size partitions by periods \(1,3,4,5,7\) are respectively \((1)\), \((10,10,10,20,20,20,20,20,20)\), \((10,10,10,10,20,20)\), \((2,4)\), and \((20,20,20,20,20)\). For \(GP(5,2)\), the partitions by periods \(1,3,4,5,8\) are \((1)\), \((20,60)\), \((60)\), \((30)\), and \((60)\). Their sizes sum to the primitive-orbit totals in the table and give 23 versus six geometric classes.

**Independent reconstruction.** `verification/check_independent.cpp` constructs the same two graphs and local rule independently, then traverses every trajectory via three-color depth-first functional-graph marking rather than indegree peeling. Its raw orbit, basin and first-entry counts in `verification/independent_results.txt` agree exactly with the Python classification, including the sharp entry times and absence of any additional period. The complete finite enumeration and two structurally different graph algorithms provide reproducible exact proof of the stated finite claims.

## Verification

From the directory containing the embedded `verification` folder, run `python3 verification/check.py`. It recalculates both complete maps, checks the binary transition arrays and JSON certificate, enumerates automorphisms, and reports the period and basin tables. Run `g++ -std=c++17 -O2 verification/check_independent.cpp -o independent_check` followed by `./independent_check`; compare the output with `verification/independent_results.txt` for the independently reconstructed counts. The two transition arrays contain exactly \(59049\) little-endian 32-bit integers each. The text and JSON certificates are plain UTF-8. Neither program needs randomness, numerical approximation, or a special graph library.

## Relationship to prior work

Gravner, Lyu and Sivakoff (2016), especially Theorem 3, characterize synchronization and long-run excitation rate on general graphs via a circulation form. That general theorem is acknowledged and is consistent with the extinction basins here, but it does not state the primitive-period multiplicities, all individual basin sizes, sharp first-entry cutoffs or geometric class partitions for these particular cubic graphs. Fisch and Gravner (1995) concern one-dimensional excitable arrays rather than this two-graph atlas. Standard Petersen-graph cycle tables concern cycles *in the graph*, not temporal cycles of the nonlinear update. No claim of first discovery of excitable waves or of the general synchronization criterion is made.

## Limitations

This is a complete exact finite-state classification for \(GP(5,1)\) and \(GP(5,2)\) only. It is not an infinite-family theorem for \(GP(n,k)\); the numerical contrast does not prove a monotonic relationship between girth, degree or symmetry and period. The primitive-cycle and basin assertions are proved by exhaustive finite calculation with reproducible complete transition certificates, not by a short symbolic closed formula. Search-based priority checks cannot eliminate the risk of an equivalent historical or unindexed computation. Independent external audit has not been performed.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first arXiv version 2016-10-24, arXiv:1610.07320v1, https://arxiv.org/abs/1610.07320. Theorem 3 and Sections 3–4.
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348, https://www.complex-systems.com/abstracts/v09_i05_a01/.
3. A. E. Brouwer, *Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html, standard graph-theoretic structure and simple-cycle inventory.
