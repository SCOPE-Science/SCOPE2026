# A cycle-word model for three-edge Kempe changes on prism graphs

## Finding
Let \(P_n=C_n\square K_2\), \(n\ge3\), be the ordinary prism with upper vertices \(u_i\), lower vertices \(v_i\), and indices in \(\mathbb Z/n\mathbb Z\). Fix the colours \(1,2,3\) on \(u_0u_1,u_{n-1}u_0,u_0v_0\), respectively. Vertices of \(\mathcal K_n\) are proper three-edge-colourings satisfying this normalization; a move interchanges two colours on one complete alternating cycle not meeting \(u_0\).

Let \(\mathcal W_n\) consist of words \(x=(x_0,\ldots,x_{n-1})\in\{1,2,3\}^n\) satisfying \(x_0=1\), \(x_{n-1}=2\), and \(x_i\ne x_{i+1}\) cyclically. Form a graph on these words: choose a letter \(c\in\{1,2,3\}\), and choose one connected component \(I\) of the cyclic positions with \(x_i\ne c\), with \(0,n-1\notin I\). Replace each \(x_i\) in \(I\) by the third colour, exchanging the other two letters. Join the original and resulting words. Call this graph \(\mathcal W_n^*\).

**Theorem.** For odd \(n\ge3\), \(\mathcal K_n\cong\mathcal W_n^*\). For even \(n\ge4\), \(\mathcal K_n\) is obtained from \(\mathcal W_n^*\) by attaching one leaf to the alternating word \((1,2,1,2,\ldots,1,2)\). Moreover, \(\mathcal K_3\) is a singleton, \(\mathcal K_4\cong K_{1,3}\), and for **every** \(n\ge5\), \(\mathcal K_n\) has odd girth exactly \(5\). The theorem describes *all individual adjacencies* and does not merely count states or degrees.

## Assumptions and scope
All graphs are finite, simple, undirected. The prism has two cycles of length \(n\) connected by the \(n\) rungs. Named colours are distinguished, and the three incident edge colours at \(u_0\) are fixed. An edge-Kempe move switches the two colours along an entire connected alternating cycle, not an arbitrary subpath. The odd girth is the least odd cycle length (infinite when no odd cycle exists). The XOR notation \(a\oplus b\) treats colour labels \(1,2,3\) as the three nonzero members of \(\mathbb F_2^2\), so \(1\oplus2=3\).

## Proof
**1. Face-coordinate bijection.** Embed the prism on a sphere with top face \(T\), bottom face \(B\), and side faces \(F_i\) between adjacent rungs. For a proper named three-edge-colouring, regard the colour of an edge as a nonzero vector in \(\mathbb F_2^2\). Three distinct nonzero vectors sum to zero at every cubic vertex. Thus the edge vectors form a flow, and on the sphere uniquely integrate to face potentials after fixing the potential of \(T\) as zero. Explicitly, the vector on an edge is the XOR of the potentials of its two incident faces.

Write \(x_i\) for the potential of \(F_i\) and \(b\) for that of \(B\). The edge colours on upper rim \(u_iu_{i+1}\), lower rim \(v_iv_{i+1}\), and rung \(u_iv_i\) are respectively
\[
x_i,\qquad x_i\oplus b,\qquad x_{i-1}\oplus x_i.
\]
Every such edge colour must be nonzero; hence \(x_i\ne0\), \(x_i\ne x_{i-1}\), and \(x_i\ne b\). Conversely these inequalities make the three colours at every vertex the three different nonzero vectors, proving the converse. The fixed upper vertex conditions force \(x_0=1\), \(x_{n-1}=2\). If \(b=0\), precisely the words of \(\mathcal W_n\) occur. If \(b\ne0\), then \(x_i\) avoids \(0\) and \(b\), leaving exactly two alternating symbols; cyclic alternation forces even \(n\). Since the first and last letters are \(1,2\), necessarily \(b=3\) and \(x=(1,2,1,2,\ldots,1,2)\). This proves the asserted state bijection, including the unique exceptional even state.

**2. Full move correspondence.** A switch on a complete alternating cycle with colours \(a,b\) has missing colour \(c=a\oplus b\). Its planar boundary separates two regions of faces; changing every face potential on the region not containing \(T\) by XOR \(c\) changes exactly the edges of the cycle, swapping \(a,b\) and preserving other edges. Conversely such a face-potential flip describes the switch uniquely. With bottom potential \(b=0\), when a side face bears \(c\), every maximal contiguous run \(I\) of side faces whose letters differ from \(c\) is enclosed by one \(a,b\)-alternating cycle (the two rims over the run and its bounding rungs). Every alternating \(a,b\) cycle arises this way. It meets \(u_0\) precisely when its run meets position \(0\) or \(n-1\); otherwise its face flip exchanges the letters \(a,b\) exactly on \(I\). This is the definition of adjacency in \(\mathcal W_n^*\).

If no side face has letter \(c\), the word alternates the other two letters, so \(n\) is even. The \(a,b\)-alternating subgraph has two cycles, the upper and lower rims; the upper meets \(u_0\) and the lower does not. Switching the lower rim changes the bottom potential from \(0\) to \(c=3\), thereby reaching the exceptional state. Conversely in the exceptional state, the only Kempe cycle avoiding \(u_0\) is this lower rim; the alternating cycles for the other two pairs pass through \(u_0\). The exceptional state is therefore a leaf, proving the isomorphism for all \(n\).

**3. Odd girth.** The general triangle-exclusion result for edge-Kempe reconfiguration graphs (Belcastro–Haas 2017, Proposition 2.1) applies to \(\mathcal K_n\) as an induced subgraph, so no triangle occurs. For odd \(n=5+2k\), the following cyclically ordered five words, with the common prefix \((12)^k\), give a five-cycle:
\[
12132,\ 12312,\ 13212,\ 13232,\ 13132.
\]
For even \(n=6+2k\), the five suffixes are
\[
121212,\ 121232,\ 123232,\ 123132,\ 121312.
\]
For either five-tuple, each consecutive transition (including last to first) is exactly one allowed full maximal component swap as specified in the theorem. Adding one extra initial \(12\) leaves these swaps legal: each changed component lies away from the word endpoints and is bounded by occurrences of the missing letter, so its component status survives the added prefix. This establishes explicit five-cycles for every \(n\ge5\). The small models yield one vertex at \(n=3\), and a claw at \(n=4\). Hence the asserted sharp odd-girth phase is proved.

## Verification
Run `python verify_reduction.py` and `python verify_odd_cycles.py` in the directory containing the included `verify_direct.py`. The first code independently enumerates all named proper edge-colourings and their genuine full alternating-cycle Kempe switches, then checks a *bijection of vertices and equality of complete neighbor sets* with the face-word model for every \(3\le n\le12\). It reports `PRISM_CYCLE_REDUCTION_PASS`. The second verifies the five stated vertices and all five moves after every padding for \(5\le n\le60\), reporting `FIVE_CYCLE_ALL_TESTED_5_TO_60_PASS`. These finite checks corroborate but do not replace the all-parameter proof above.

## Relationship to prior work
Belcastro–Haas (2012) established the unique edge-Kempe equivalence class for prism graphs. Belcastro–Haas (2017), Proposition 2.1, proved triangle-freeness generally, and on page 213 observed that the exact general structure of vertex-fixed Kempe graphs for ordinary prisms was natural to conjecture but lacked a proof; the same paper proves a different hypercube-with-leaves result for *crossed* prisms. Prior numerical results for the ordinary prism's fixed-vertex graph determine its **degree sequence and exceptional leaf**, but do not determine all pairs of adjacent states, the word-rewrite model, or five-cycles for every size; none of those earlier numerical counts is claimed as novel here. Goedgebeur–Östergård (2021) analyze Kempe equivalence classes rather than this explicit adjacency model.

## Limitations
The result concerns named *three-edge* colourings of the **ordinary** prism with one fixed vertex, not vertex recolouring, crossed prisms, more than three edge colours, or arbitrary cubic graphs. It does not establish a sharp all-size diameter, mixing time, or a new degree-enumeration theorem. An equivalent unpublished historical word construction cannot be ruled out by accessible searches alone; no independent scholarly audit has been performed.

## References
- S. M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730 (first publicly submitted 2012-09-08), https://arxiv.org/abs/1209.1730 .
- S. M. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, *Australasian Journal of Combinatorics* **69** (2017), 197–214, https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf .
- J. Goedgebeur and P. R. J. Östergård, *Switching 3-Edge-Colorings of Cubic Graphs*, arXiv:2105.01363 (2021), https://arxiv.org/abs/2105.01363 .
