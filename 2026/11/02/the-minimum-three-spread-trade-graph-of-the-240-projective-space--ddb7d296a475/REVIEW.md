# Independent mathematical audit

## correctness

PASS

The geometric encoding is consistent: distinct label triples yield disjoint spreads exactly when their intersection has size one (triples in a common 4-side share a split at intersection size two; disjoint triples can instead lie on complementary sides). In a packing the seven triples thus meet pairwise once. The degree identities sum d_x=21, sum binom(d_x,2)=21 and d_x<=3 force seven degrees 3 and one 0. Every pair of used labels lies on a unique triple, giving a Fano system. On the same seven labels two different Steiner systems cannot differ in at most three blocks: a removed abc needs three distinct replacement blocks for ab, bc and ca. Then conservation of point degrees requires each of a,b,c to occur once more in the other removed blocks, impossible for two blocks each meeting abc at most once. On different supports at most four blocks can be common, because exactly three contain the label lost from the first support. Swapping the omitted label with that lost label fixes the four possible common blocks; the same-support argument forces uniqueness of that neighbor. The star transpositions on a fixed reference omitted label generate S8 on the cosets, and the even Fano stabilizer makes parity well defined. Independently written coordinate exact covers gave 35 lines, 56 spreads and 240 packings; all 28680 pair comparisons gave common-spread counts (13560,8400,5040,840,840) for k=0 through 4 and zero higher. The independent eight-label construction checked all star images and parity over 40320 permutations. BFS from all 240 roots gave (1,7,42,105,77,8). Thus the graph is connected with diameter five, 840 edges, and two parity classes of 120. Bipartiteness and at most one common neighbor per vertex pair exclude cycles shorter than six, and the independent check exhibited a six-cycle. This is exhaustive for PG(3,2), not an extrapolation.

## originality

PASS

The 56 spreads, 240 packings, Fano encoding, S8 action, even stabilizer and two 120-element parity classes are documented prior inputs. The supported distinct claim is the identification of minimum whole-spread trades with the unused-label moves together with their precise metric and girth. The closest inspected action and graph results use a different length/order or adjacency relation, and do not furnish these invariants.

## value

PASS

Local reconfiguration of a classical line parallelism is a natural question: the minimum number of entire spreads that can change, which minimal changes are legal, and how many steps they take to reach any parallelism. The star characterization and exact layers answer these questions for the full space and give a usable distance benchmark. This is not a re-enumeration of the known 240 packings or a change of notation for the known disjointness graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
