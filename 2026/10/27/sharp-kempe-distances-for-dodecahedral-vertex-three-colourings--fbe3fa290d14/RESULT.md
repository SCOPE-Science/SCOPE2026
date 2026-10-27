# Sharp Kempe distances for dodecahedral vertex three-colourings

## Finding
For the dodecahedral graph \(D=GP(10,2)\), form the undirected simple Kempe reconfiguration graph on proper vertex three-colourings, joining two distinct colourings when one is obtained from the other by interchanging two colours on a maximal connected bicoloured component. There are two natural versions: the labelled-colour graph \(K_{\mathrm{lab}}\) and its graph \(K_{\mathrm{orb}}\) after identifying global permutations of the three colour names. Both are connected and have these exact values:

| Invariant | Labelled colours \(K_{\mathrm{lab}}\) | Palette orbits \(K_{\mathrm{orb}}\) |
| --- | ---: | ---: |
| States | 7200 | 1200 |
| Undirected edges | 36120 | 5360 |
| Radius | 7 | 6 |
| Diameter | 8 | 7 |

The labelled degree distribution is \(6960\) states of degree \(10\) and \(240\) of degree \(11\). Its eccentricity distribution is \(5280\) states of eccentricity \(7\) and \(1920\) of eccentricity \(8\). The palette-orbit degree distribution is \(140,1020,20,20\) states of respective degrees \(8,9,10,11\); its eccentricity distribution is \(460\) states of eccentricity \(6\) and \(740\) of eccentricity \(7\). These numbers give a complete exact finite computation, not an asymptotic claim.

## Assumptions and scope
The graph \(GP(10,2)\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with all undirected edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). It is the ordinary twenty-vertex dodecahedral graph. A proper vertex three-colouring is a map \(c:V(D)\to\{0,1,2\}\) assigning distinct colours to adjacent vertices. Every such colouring uses all three colours since \(D\) contains an odd cycle; hence the global \(S_3\) action is free. A Kempe component is an entire connected component in the induced subgraph on vertices of two specified colours, not an arbitrary connected bicoloured set. Each move swaps those two colours on precisely one Kempe component. For both state graphs multiple moves with the same endpoints count as one edge, and quotient loops are omitted. Shortest-path distances use these undirected simple state graphs.

## Proof
The accompanying standard C++17 program `verify.cpp` is a finite exhaustive certificate for the stated exact values. Its completeness and correctness can be checked from the following invariants.

First it constructs all thirty edges using the given modular definition and verifies degree three at all twenty vertices. In `generate`, vertex indices are processed in order; at each vertex the recursion chooses every permitted existing colour or introduces the next previously unused colour, rejecting an assignment only if a previously assigned neighbour has the same colour. Thus every proper colouring appears exactly once up to relabelling of colours by order of first occurrence, and no invalid colouring appears. All canonical leaves use precisely three colours. Exhausting this recursion produces \(1200\) canonical representatives. Applying the six permutations in \(S_3\) to every representative produces exactly \(7200\) distinct labelled proper colourings, since no nonidentity colour permutation can fix a colouring using all three colours.

Second, for each colouring the procedure `kempe_moves` iterates through each of the three unordered colour pairs, runs graph traversal to identify **every** connected component of the two-colour induced subgraph, and swaps the two colours on that complete component. These and only these are permitted single Kempe moves. `make_graph` matches every resulting colouring to the exhaustive state list (or canonicalizes it for the palette quotient), rejects missing states, deduplicates neighbours and checks symmetry of all edges. Consequently its adjacency list is exactly the required reconfiguration graph, not a sampled subgraph. Degrees and edge totals follow by summing these complete adjacency lists and halving the directed arc count.

Finally, for each of the \(7200\) labelled and \(1200\) quotient starting states, `analyze` runs breadth-first search on its complete finite graph. Breadth-first search computes shortest path distance because every move has unit cost. Every search reaches every state, establishing connectivity. Its maximum distance is precisely the starting state's eccentricity. Histograms of these exhaustive maxima give the eccentricity multiplicities above; their minimum and maximum yield, respectively, each radius and diameter. The program contains exact assertions for each count and prints `VERIFY_OK` if and only if every assertion succeeds. Therefore all displayed values are proved by exhaustive finite computation with explicitly auditable enumeration and graph algorithms.

## Verification
From this directory, compile and run the included independent-of-external-packages source with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify.cpp -o verify && ./verify`. A successful run ends in `VERIFY_OK` and prints both full metric profiles. A separate Python implementation constructed the graph independently using a standard graph library and reproduced the state and metric distributions; the packaged C++ program does not use this library or any precomputed data. Runtime/memory depend on the compiler and hardware, but the source fixes all finite loops and assertions.

## Relationship to prior work
Feghali, Johnson and Paulusma (2015, arXiv:1503.03430, Theorem 1) prove that three-colourings of cubic graphs other than two exceptional graphs form one Kempe class. That theorem implies **connectivity** here but does not imply the exact shortest-path radius, diameter, degree distribution or eccentricity spectrum for this specific graph; the present finite calculation refines the qualitative theorem. Bonamy and collaborators (2020) investigate shortest Kempe-change sequences and algorithmic complexity, with methods and results for paths and stars, not the dodecahedral graph's metric census. The labelled and global-colour-unlabelled formulations are distinguished: a quotient can shorten paths, as the different measured diameters show. The computation is for **vertex** colourings and is not interchangeable with edge-colouring Kempe results. Published database and semantic record searches revealed no target-specific exact census, but a negative search result is not proof of novelty.

## Limitations
This is a result for one fixed finite graph, not a theorem for all cubic graphs and not an independent formal proof assistant certification. The numerical claims are exact conditional on the explicitly given standard finite algorithm, and the supplied code provides the complete finite calculation, not an infinite extrapolation. The originality comparison is bounded by accessible/indexed literature; an unpublished or unindexed equivalent computation cannot be ruled out. Independent audit has not been performed.

## References
1. C. Feghali, M. Johnson and D. Paulusma, *Kempe Equivalence of Colourings of Cubic Graphs*, arXiv:1503.03430 (first public version March 11, 2015), https://arxiv.org/abs/1503.03430 .
2. M. Bonamy et al., *Shortest Reconfiguration of Colorings Under Kempe Changes*, STACS 2020, Article 35, doi:10.4230/LIPIcs.STACS.2020.35, https://drops.dagstuhl.de/storage/00lipics/lipics-vol154-stacs2020/LIPIcs.STACS.2020.35/LIPIcs.STACS.2020.35.pdf .
