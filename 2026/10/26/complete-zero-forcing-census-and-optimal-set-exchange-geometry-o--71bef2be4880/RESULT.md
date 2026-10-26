# Complete zero-forcing census and optimal-set exchange geometry of the Grötzsch graph

## Finding
For the eleven-vertex Grötzsch graph \(G=\mu(C_5)\), the Mycielskian of a five-cycle, the ordinary zero-forcing number is \(Z(G)=5\), and its **complete zero-forcing polynomial** is
\[
\mathcal Z(G;z)=175z^5+370z^6+320z^7+165z^8+55z^9+11z^{10}+z^{11}.
\]
Here the coefficient of \(z^k\) counts all \(k\)-element zero-forcing starting sets. The \(175\) optimum sets fall into exactly \(19\) symmetry classes under the full dihedral automorphism group: \(16\) classes of size \(10\) and \(3\) of size \(5\). Their parallel propagation-round distribution is \(55\) requiring three rounds, \(100\) requiring four rounds, and \(20\) requiring five rounds.

Join two optimum sets when they differ by exchanging exactly one selected vertex for one unselected vertex while remaining optimum. This *token-jump exchange graph* has \(175\) vertices, \(1180\) edges, is connected, has radius \(4\) and diameter \(5\); its eccentricity counts are \(30\) at four and \(145\) at five. The exact unordered-pair shortest-distance counts for distances \(1,2,3,4,5\) are respectively \((1180,4780,6445,2610,210)\).

## Assumptions and scope
Number the original cycle vertices \(u_0,\ldots,u_4\) by indices \(0,\ldots,4\), their shadow copies \(v_0,\ldots,v_4\) by \(5,\ldots,9\), and the apex \(w\) by \(10\). Indices on each cycle are read modulo five. The twenty simple undirected edges are \(u_i u_{i+1}\), \(v_i u_{i-1}\), \(v_i u_{i+1}\), and \(wv_i\), for each \(i\in\{0,1,2,3,4\}\). This gives the standard 11-vertex, 20-edge Mycielskian \(\mu(C_5)\).

For a selected set \(B\subseteq V(G)\), call its vertices blue. At each round, every blue vertex with exactly one white neighbor forces that neighbor blue, with all enabled forces computed from the preceding round's coloring. The set \(B\) is zero forcing exactly when repeated rounds blue all \(11\) vertices. Its propagation time is the least number of such parallel rounds required. The polynomial above includes *all* selected subsets, not just optimum ones. Token jumping allows replacement by any unselected vertex; it is not token sliding along an edge.

## Proof
The graph and each selected subset are encoded without isomorphism assumptions. For \(0\leq m<2^{11}\), interpret bit \(i\) of \(m\) as membership of vertex \(i\) in the initial blue set. Let \(N(i)\) be the neighbor bit mask determined by the edge formula above, and \(b\) the current blue mask. For each blue vertex \(i\), compute \(q_i=N(i)\mathbin{\&}\mathord{\sim}b\), with complements understood inside the 11-bit universe. The force from \(i\) exists exactly when \(q_i\) has one set bit. Form the bitwise union \(f(b)\) of all these singletons. Replace \(b\) by \(b\mathbin{|}f(b)\) until no new bit is set. The process is monotone and each successful step increases the number of blue vertices, so it always terminates in at most \(11\) steps; its terminal mask is the unique closure independently of the order of single permitted forces.

The accompanying standalone `verify.py` exhausts all \(2048\) masks, checks each mask with both parallel forcing and a separately programmed sequential single-force closure, and tallies success by mask cardinality. Its exactly reproduced success-count vector, in cardinality order \(0\) through \(11\), is
\[
(0,0,0,0,0,175,370,320,165,55,11,1).
\]
There are no successful sets of size smaller than five, while there are \(175\) of size five; this proves the minimum and the full polynomial without making an inference from sampling or only enumerating some cardinalities.

The full symmetry group is \(D_5\) of order ten: the apex is the only degree-five vertex, the five shadows have degree three, and the five original vertices have degree four. Any graph automorphism therefore preserves these classes and restricts to an automorphism of the original five-cycle; that determines its action on the shadows, and all ten cycle rotations/reflections preserve the listed edge set. The verifier builds those ten permutations, verifies that they preserve all twenty edges, and partitions the \(175\) minimum masks into precisely \(19\) orbits. The attached `orbit_types.csv` lists a representative, the size and propagation time of each orbit, giving a complete classification: every optimum mask is a dihedral translate of exactly one representative in that file.

Two size-five masks are exchange adjacent exactly when their symmetric difference has cardinality two. Independently constructing such edges by (i) scanning all unordered pairs of minimum masks and (ii) explicitly deleting and inserting one vertex gives the same \(1180\) edges. Breadth-first search starting from each of the \(175\) vertices yields a distance to every other vertex (hence connectedness) and gives the asserted eccentricities and distance counts. In particular \(1180+4780+6445+2610+210=\binom{175}{2}\), so every unordered pair is accounted for.

## Verification
Run `python3 verify.py` from a Python 3 standard-library environment; no additional packages or external datasets are required. The program rebuilds the 20 edges, verifies triangle-freeness and chromatic number four by exhaustive coloring, checks both zero-forcing implementations on all 2048 initial states, reconstructs symmetry orbits and the exchange graph, and checks every shortest-path distance and both handshaking and unordered-pair identities. It outputs `VERIFY_OK` followed by the computed statistics and all 19 orbit representatives. The attached `orbit_types.csv` contains these representatives with zero-based vertex labels.

## Relationship to prior work
Hogben, Huynh, Kingsley, Meyer, Walker and Young (first public arXiv version 15 October 2014) introduce and study propagation-time distributions for minimum zero-forcing sets, but do not tabulate this Grötzsch graph's complete 2048-state census. Boyer and collaborators (arXiv, 26 January 2018) define the zero-forcing polynomial and derive formulas for familiar families including cycles, wheels and threshold graphs; their inspected text does not treat Mycielskians or identify the present polynomial. Rameh's 2021 paper on zero-forcing number and maximum nullity of some Mycielski constructions is directly plausible prior work for the *scalar* optimum size, but only bibliographic/abstract material was accessible; the value \(Z(G)=5\) is therefore not presented as an independently established historical first. The claimed new content is the complete size distribution together with the 19-fold symmetry classification and exact optimum-set exchange metric. None of the inspected sources or available related records was found to imply that package of statements.

## Limitations
This is a single exact finite graph computation, not a theorem for all Mycielskians; the proof is exhaustive and reproducible but does not provide a short symbolic description of each of the 175 sets beyond the listed symmetry generators and orbit representatives. The absence of a covering result in inspected literature or indexes cannot establish global novelty. A relevant 2021 Mycielski-construction article and possibly unindexed enumerations were not fully inspected and remain originality risks. The optimum-set exchange graph uses token jumping, not token sliding. No independent review or independent audit is claimed.

## References
1. L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker and M. Young, *Propagation time for zero forcing on a graph*, arXiv:1410.4191v1, 15 October 2014. https://arxiv.org/abs/1410.4191
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, 26 January 2018. https://arxiv.org/abs/1801.08910
3. Z. Rameh, *The zero forcing number of Which Mycielski construction ...*, 2021 bibliographic record, https://sid.ir/paper/953698/en (full text not inspected).
4. *Grötzsch graph*, Wolfram MathWorld, https://mathworld.wolfram.com/GroetzschGraph.html (canonical object description; publication date not used for archive eligibility).
