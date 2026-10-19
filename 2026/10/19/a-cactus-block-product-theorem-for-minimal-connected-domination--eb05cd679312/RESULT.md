# A cactus block-product theorem for minimal connected domination exchanges

## Finding
Let \(G\) be a finite connected simple cactus graph. A *connected dominating set* (CDS) is a nonempty vertex set \(S\) for which \(G[S]\) is connected and every vertex lies in \(S\) or has a neighbor in \(S\). It is *minimal* when no proper subset is a CDS. Define the **minimal-CDS exchange graph** \(J(G)\) to have the inclusion-minimal CDSs as vertices, with an edge when one selected vertex is replaced by one unselected vertex and the resulting set is again an inclusion-minimal CDS.

Suppose \(G\) has at least one cut vertex, and let \(A\) be its set of cut vertices. For each cycle block \(C\), take the maximal cyclic runs of vertices in \(V(C)\setminus A\), of lengths \(\ell_1,\ldots,\ell_r\). Because every cycle block meets \(A\), these runs are ordinary paths, not a single cyclic run. Let \(m_C\) be the number of runs of length one. Define \(\Omega_C\) as follows:

- If \(V(C)\setminus A\) is empty, \(\Omega_C=\{\varnothing\}\).
- Otherwise, \(\Omega_C\) consists of every consecutive two-vertex subset within a noncut run, together with each singleton that constitutes an entire run of length one.

Then **every** inclusion-minimal CDS, and no other set, has the unique form
\[
 S=A\cup\bigcup_{C\text{ a cycle block}}\bigl((V(C)\setminus A)\setminus O_C\bigr),
 \qquad O_C\in\Omega_C.
\]
No degree-one vertex is selected. Thus the complete size enumerator is
\[
 \mathcal M_G(z)=\sum_{S\text{ minimal CDS}}z^{|S|}
 =z^{|A|}\prod_C\left(\sum_{O\in\Omega_C}z^{|V(C)\setminus A|-|O|}\right).
\]
The exchange graph has the *exact* Cartesian-product decomposition
\[
 J(G)\cong\mathop{\square}_{C}J_C,
 \qquad
 J_C=\left(\mathop{\bigsqcup}_{\ell_i\ge2}P_{\ell_i-1}\right)
 \bigsqcup
 \begin{cases}K_{m_C},&m_C>0,\\ \varnothing,&m_C=0,\end{cases}
\]
where \(P_s\) is a path on \(s\) vertices and \(K_s\) is a clique on \(s\) vertices. If the cycle contains no noncut vertex, set \(J_C=K_1\). An empty Cartesian product is \(K_1\).

Consequently, the exact number of connected components is \(\prod_C c_C\), where \(c_C=1\) for a cycle without noncut vertices and otherwise
\[
 c_C=\#\{i:\ell_i\ge2\}+\mathbf1_{\{m_C>0\}}.
\]
Each connected component is a Cartesian product of paths and at most one clique factor from each cycle. In particular, the diameter of such a component is the sum of \(\ell_i-2\) over its chosen path factors plus one for each chosen clique factor of order at least two. Hence its diameter, connectivity, and the full minimal-CDS size distribution follow directly from the cut vertices and cycle-block runs.

The cut-free cases are exact as well: for a bare cycle \(C_n\), \(n\ge3\), the minimal CDSs are the \(n\) complements of consecutive pairs, \(\mathcal M_{C_n}(z)=nz^{n-2}\), and \(J(C_n)\cong C_n\). For the one-vertex graph, \(\mathcal M_G(z)=z\) and \(J(G)=K_1\); for the single edge, \(\mathcal M_G(z)=2z\) and \(J(G)=K_2\). For a tree with at least three vertices, the unique minimal CDS is its set of cut vertices.

## Assumptions and scope
All graphs are finite, undirected, loopless and simple. A cactus is connected and each block is either an edge or a cycle; in particular distinct cycles share at most one vertex. *Minimal* always means inclusion-minimal, not necessarily minimum cardinality. Exchange edges are single token *replacements*, not arbitrary token additions/removals. The polynomial counts labeled vertex subsets of the specified graph, not isomorphism classes. The graph \(J(G)\) includes minimal sets of different sizes as distinct vertices, but a replacement edge always preserves size.

## Proof
**1. Cut-vertex rigidity.** If \(v\) is a cut vertex and \(v\notin S\), connectedness forces \(S\) to lie inside one component of \(G-v\). Vertices in another component have no neighbor in \(S\), contradicting domination. Hence every CDS contains all of \(A\). A degree-one vertex whose neighbor is a cut vertex is never present in a minimal CDS: deleting it preserves both conditions. Every vertex outside \(A\) is either such a leaf or belongs to precisely one cycle block.

**2. Cycle-block locality.** Fix a cycle block \(C\). The block-cut tree ensures that a connected selected set containing all of \(A\) meets \(C\) in a connected induced subgraph: no outside route can connect two distinct vertices of \(C\). A selected subset containing a cut vertex of \(C\) must therefore be the whole cycle or a consecutive path. Thus its omitted vertices form a single consecutive interval of noncut vertices (or the interval is empty). An omitted interval of length at least three has an interior vertex with neither cycle neighbor selected; that noncut vertex has no neighbors outside \(C\), contradicting domination. The omitted interval has length at most two.

**3. Local minimality.** If noncut vertices are available and no vertex is omitted, removing one gives a still-connected dominating set. If exactly one noncut vertex \(u\) is omitted and one of its cycle neighbors is also noncut, deleting that neighbor enlarges the omitted interval to a legal length-two interval. Hence such a set is not minimal. If the omitted interval is a consecutive noncut pair, deleting any other selected noncut vertex either disconnects the selected cycle path or creates an undominated interior vertex. If the omitted interval is a singleton whose two cycle neighbors are cut vertices, deleting any other selected noncut vertex disconnects the selected cycle path. All cut vertices are forced by step 1. Thus precisely the options \(\Omega_C\) give minimal sets; choices on distinct cycle blocks are independent through the forced cut vertices. This proves the classification and the product enumerator.

**4. Exchange structure.** Two distinct local omission choices of equal size have symmetric difference of cardinality two exactly when they are consecutive edges in the *same* noncut run, or two different isolated singleton runs. The former choices make a path \(P_{\ell-1}\) in a run of length \(\ell\); the latter make \(K_{m_C}\). A pair-omission and an isolated singleton have different sizes and cannot be joined by a replacement. Since distinct cycle blocks have disjoint noncut vertices and each distinct local choice changes at least two vertices, one global replacement changes exactly one cycle-block choice. This proves the Cartesian-product isomorphism and the formulas for component counts and diameters.

**5. Exceptional cut-free graphs.** A connected cactus with no cut vertex is a single vertex, a single edge, or a cycle. Direct domination on a cycle requires omission of at most two consecutive vertices; inclusion-minimality forces omission of exactly two. Their edge sets overlap in one vertex precisely for adjacent edges of the original cycle, giving \(J(C_n)\cong C_n\). The remaining tiny cases and trees follow directly.

## Verification
The accompanying standalone Python program `verify_cactus.py` uses only the standard library. It compares the structural formula with independent exhaustive subset enumeration, direct connectivity and domination tests, the size polynomial, and the complete exchange-edge graph on all 103 connected unlabeled cactus graphs through seven vertices. It additionally checks 180 deterministically generated glued-cycle/bridge cacti of up to thirteen vertices. The two explicit ten-vertex examples check a connected \(P_4\square P_3\) exchange graph with twelve configurations and seventeen edges, and a disconnected \(P_2\sqcup P_2\) exchange graph with four configurations and two edges. Run `python3 verify_cactus.py`; expected terminal marker: `VERIFY_OK`. These finite tests are independent sanity checks of the symbolic proof, not substitutes for it.

## Relationship to prior work
Golovach, Heggernes and Kratsch (2015) initiated systematic enumeration of inclusion-minimal connected dominating sets and proved general bounds for several graph classes, but did not give this cactus block-run enumerator or its exchange-graph factorization. Lokshtanov and collaborators (2020) studied connected-dominating-set reconfiguration under *token addition/removal* with a size bound, a different state space and move rule from the exchange graph of inclusion-minimal states here. Abu-Khzam and collaborators (2022) gave general enumeration algorithms for two-degenerate and arbitrary graphs; a general algorithm does not itself imply this local closed form or the exact component isomorphisms. Gupta, Acharya and Jain (2016) considered **two-point set domination** of cacti, a different quantifier condition, not connected domination of the selected set. Brimkov, Mikesell and Smith (2017) proved block-decomposition and cactus algorithms for **connected power domination**, a weaker dynamic observation rule than ordinary connected domination; their minimum-cardinality algorithm does not classify the inclusion-minimal ordinary CDSs or their exchange edges. The standard correspondence with spanning trees having many leaves concerns cardinality optimisation; the full inclusion-minimal exchange classification is not a stated consequence of the cited results.

## Limitations
The formula assumes cactus block structure. It need not hold when distinct cycles share an edge or in a general outerplanar graph. Exchange connectivity concerns only inclusion-minimal states and single replacements; it does not decide connectivity of the broader bounded-capacity addition/removal reconfiguration graph. Published work not indexed by the searches may contain an equivalent reformulation. No external independent scientific validation is claimed.

## References
1. P. A. Golovach, P. Heggernes, D. Kratsch, *Enumerating Minimal Connected Dominating Sets in Graphs of Bounded Chordality*, IPEC 2015, 307–318, DOI: 10.4230/LIPIcs.IPEC.2015.307 (public 2015-11-19).
2. D. Lokshtanov, A. E. Mouawad, F. Panolan, S. Siebertz, *On the Parameterized Complexity of Reconfiguration of Connected Dominating Sets*, IPEC 2020, Article 24, DOI: 10.4230/LIPIcs.IPEC.2020.24.
3. F. N. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, K. Mann, *Enumerating Minimal Connected Dominating Sets*, ESA 2022, Article 1, DOI: 10.4230/LIPIcs.ESA.2022.1.
4. P. Gupta, M. Acharya, D. Jain, *2-Point Set Domination Number of a Cactus*, Gulf Journal of Mathematics 4 (2016), 80–89, DOI: 10.56947/gjom.v4i3.76.
5. B. Brimkov, D. Mikesell, L. Smith, *Connected power domination in graphs*, arXiv:1712.02388v1 (public 2017-12-06); DOI: 10.1007/s10878-019-00380-7.
