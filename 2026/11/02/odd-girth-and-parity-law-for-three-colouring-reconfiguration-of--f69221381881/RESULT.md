# Odd-girth and parity law for three-colouring reconfiguration of cycles

## Finding
Let \(n\ge3\). The vertices of \(\mathcal R(C_n)\) are all **labelled** proper vertex \(3\)-colourings of the cycle \(C_n\), and its edges change the colour at precisely one vertex. Colours are elements of \(\mathbb Z/3\mathbb Z\). For each colouring, put \(s_i=+1\) if \(c_{i+1}-c_i\equiv1\pmod3\), and \(s_i=-1\) otherwise, with indices modulo \(n\). Let \(p\) be the number of plus signs and \(W=2p-n\).

**Theorem.** The integer \(W\) is divisible by \(3\) and preserved by every recolouring. For each \(0\le p\le n\) satisfying \(3\mid(2p-n)\), the corresponding sector \(\mathcal R_{n,p}\) exists, and there are no other sectors. If \(p=0\) or \(p=n\), this sector comprises three isolated vertices. If \(0<p<n\), it is connected and
\[
|V(\mathcal R_{n,p})|=3\binom np,\qquad
|E(\mathcal R_{n,p})|=3n\binom{n-2}{p-1}.
\]
For even \(n\), every such nontrivial sector is bipartite with chromatic number \(2\). For odd \(n\), its **odd girth is exactly \(3n\)**, and **every edge lies on a simple odd cycle of that minimum length**; its chromatic number is \(3\). Moreover, for all \(n\),
\[
\mathcal R_{n,p}\cong C_{3n}\quad\text{if }\min(p,n-p)=1,
\]
and otherwise its ordinary girth equals \(4\). In particular, the nonlazy single-site reconfiguration walk on every nontrivial sector has period \(2\) for even \(n\) and period \(1\) for odd \(n\).

## Assumptions and scope
All indices, vertex labels and all three colour names are retained, not quotiented by graph automorphisms or colour permutations. Adjacency permits exactly one legal recolouring; there are no holding loops. A walk's length is its number of recolourings. The girth is the minimum length of a simple cycle and odd girth the minimum length of a simple odd cycle; bipartite graphs have no odd girth. The cases \(n=3\) and \(p\in\{0,n\}\) are included with the isolated-vertex convention. The ordinary-girth statement for mixed sectors has two disjoint cases as above, and no girth is assigned to an isolated sector.

## Proof
**1. Sign sectors and counts.** Closing the colours around the cycle forces \(\sum_i s_i=2p-n\equiv0\pmod3\). Conversely, any such sign word and any of the three choices for \(c_0\) produce exactly one proper colouring, giving \(3\binom np\) states. The only possible recolouring at site \(i\) occurs when \(s_{i-1}\ne s_i\), and it interchanges those two signs. Thus \(p\) is invariant. If every sign is the same, no move is possible. A mixed sign word has at least one sign boundary and hence at least one legal edge. For the edge count, there are \(2n\binom{n-2}{p-1}\) ordered choices of a sign word and a sign-changing adjacent pair. Multiplying by three initial colours and dividing by two for the ends of each undirected exchange yields \(3n\binom{n-2}{p-1}\).

**2. Twisted integer height cover.** Fix \(p\) with \(0<p<n\) and \(3\mid W\). A lifted state is an integer sequence \(H=(h_i)_{i\in\mathbb Z}\) satisfying
\[
h_{i+n}=h_i+W,\qquad h_i\equiv i\pmod2,\qquad |h_{i+1}-h_i|=1.
\]
Its colouring is \(c_i=h_i\bmod3\). Conversely, start from an admissible colour and choose the unique congruence class \(h_0\bmod6\) that is even and agrees with \(c_0\bmod3\), then use the prescribed \(\pm1\) increments. Thus every proper colouring in the sector has precisely the lifts \(H+6t\), \(t\in\mathbb Z\). The congruence \(3\mid W\) ensures cyclic colouring closure. A legal recolouring corresponds exactly to raising by \(2\) a local valley, or lowering by \(2\) a local peak, in this twisted height profile. The neighboring heights at the wrap are \(h_{-1}=h_{n-1}-W\) and \(h_n=h_0+W\).

**3. Monotone interpolation lemma.** Suppose two lifted profiles \(H\) and \(T\) share the same \(W\) and satisfy \(H\le T\) pointwise. If they are different, some coordinate has \(T_i-H_i\ge2\). If \(i\) is not a valley of \(H\), select a neighboring coordinate \(j\) strictly lower in the twisted profile. As \(T\) has unit slopes,
\[
T_j-H_j\ge (T_i-1)-(H_i-1)=T_i-H_i\ge2.
\]
Continue descending. A strictly descending path cannot turn back. Since the periodic sign sequence contains both signs, it reaches a valley after fewer than \(n\) steps, rather than descending indefinitely around the cycle. Raising that valley by \(2\) preserves the unit slopes and the pointwise upper bound \(T\). Iteration reaches \(T\) in exactly \(\frac12\sum_{i=0}^{n-1}(T_i-H_i)\) legal moves. For arbitrary two profiles of equal twist, their coordinatewise minimum is another valid twisted unit-slope profile: it retains prescribed alternating parities, and its adjacent differences are odd and at most one in absolute value. Using the lemma twice, any two lifts of the given winding are connected, so the finite sector is connected.

**4. Shortest nontrivial odd loops.** Any closed walk of length \(L\) in the finite sector lifts to a path from \(H\) to \(H+6t\) for some integer \(t\). Each step changes exactly one height by \(\pm2\), hence
\[
L\ge3n|t|,\qquad L\equiv3nt\pmod2.
\]
The congruence follows by considering the parity of \(\frac12\sum_i(h_i-H_i)\), which reverses at every step. For even \(n\), every closed walk has even length, proving bipartiteness. For odd \(n\), an odd closed walk requires an odd nonzero \(t\), hence \(L\ge3n\).

On the other hand, take any lift \(H\). The monotone lemma applied to \(H\le H+6\) yields a path of exactly \(3n\) valley-raises. Its projected endpoints are identical. No two **internal** projected states coincide: if profiles on the monotone path project to the same colouring, their height difference is \(6t\) at every coordinate, requiring at least \(3n\) steps for nonzero \(t\). Thus the projection is a simple cycle of length \(3n\). Moreover, for any specified reconfiguration edge, orient its lift as one upward valley-raise \(H\to H'\). Since \(H'\le H+6\), complete the prescribed move by the monotone lemma from \(H'\) to \(H+6\). This constructs a simple cycle of length \(3n\) through that edge. Therefore odd girth is exactly \(3n\) for odd \(n\). Since \(c\mapsto\sum_{i=0}^{n-1}c_i\bmod3\) is a proper \(3\)-colouring of the recolouring graph, the chromatic number is exactly \(3\) in the odd case, and exactly \(2\) in the even nontrivial case.

**5. Ordinary girth.** If \(\min(p,n-p)=1\), there is exactly one sign of the minority type, so each state has precisely two legal recolourings. The sector is finite and connected by Step 3; hence it is the single cycle \(C_{3n}\). Otherwise \(p,n-p\ge2\). In the sign word formed by a block of \(p\) plus signs followed by \(n-p\) minus signs, the two sign boundaries correspond to nonadjacent cycle vertices. Their two recolourings commute, forming a four-cycle. No triangle exists: any odd closed walk of length less than \(3n\) is forbidden by Step 4 (even \(n\) has no odd closed walk at all). Consequently the ordinary girth is exactly four.

## Verification
The standalone file `verify_direct.py` enumerates all proper labelled colourings of \(C_n\) and every legal recolouring from the definition for \(3\le n\le11\). It independently groups by winding, verifies all vertex/edge counts and components, and checks odd-girth and four-cycle predictions. Execute `python3 verify_direct.py`.

The separately implemented `verify_sign_lift.cpp` enumerates binary sign sequences and their three colour lifts for \(3\le n\le16\), constructs every legal switch, checks connected components, and tests a monotone \(3n\)-move lift from each individual mixed-sector sign sequence. Compile using `g++ -std=c++17 -O2 verify_sign_lift.cpp -o verify_sign_lift`, then execute `./verify_sign_lift`. The independent implementations cover different encodings and are corroboration only; Steps 1–5 establish all \(n\).

## Relationship to prior work
The winding obstruction and ordinary recolouring connectivity questions were developed by Cereceda, van den Heuvel and Johnson in their July 2006 report *Mixing 3-colourings in Bipartite Graphs*. That paper already proves that an oriented cycle's weight is constant under recolouring, develops integer height moves for zero-weight bipartite colourings, and classifies globally mixing bipartite graphs. Those tools and facts are **not claimed as new** here. Their later *Finding Paths Between 3-Colourings* and Johnson et al.'s 2014 *Finding Shortest Paths between Graph Colourings* give general recolouring connectivity and, in the latter, a shortest-path algorithm for every pair of three-colourings. The present claim is different: the sharp **minimum length of a nontrivial closed odd walk**, existence of shortest odd cycles through **every edge**, parity of each nontrivial winding sector, and the exact ordinary girth, all as uniform functions of the underlying cycle length. A shortest path between a vertex and itself is zero and does not by itself state these holonomy-sensitive graph invariants.

## Limitations
This result concerns only cycles and exactly three named vertex colours, with single-site legal recolouring and no holding loops. It does not establish new general shortest-path algorithms or a mixing-time bound. Earlier height-function and winding lemmas are explicitly prior work. An equivalent odd-girth computation may occur under different terminology (for example exclusion dynamics or Potts-model state graphs); the 2007 preprint on paths was located but its complete primary PDF was not accessible for comparison, so a residual originality risk remains.

## References
1. L. Cereceda, J. van den Heuvel, M. Johnson, *Mixing 3-colourings in Bipartite Graphs*, LSE-CDAM-2006-08, July 2006; accessible text: https://www.yumpu.com/en/document/view/38771252/mixing-3-colourings-in-bipartite-graphs-department-of-mathematics .
2. L. Cereceda, J. van den Heuvel, M. Johnson, *Finding Paths Between 3-Colourings*, LSE-CDAM-2007-31, December 2007; indexed preprint: https://matthewjohnsondurham.github.io/papers/cdam-2007-31.pdf ; Journal of Graph Theory 67 (2011), 69–82, first published online 16 December 2010.
3. M. Johnson, D. Kratsch, S. Kratsch, V. Patel, D. Paulusma, *Finding Shortest Paths between Graph Colourings*, arXiv:1403.6347v1, first submitted 25 March 2014: https://arxiv.org/abs/1403.6347 .
4. M. Wrochna, *Homomorphism reconfiguration via homotopy*, arXiv:1408.2812 (2014), for a distinct general homotopy approach.
