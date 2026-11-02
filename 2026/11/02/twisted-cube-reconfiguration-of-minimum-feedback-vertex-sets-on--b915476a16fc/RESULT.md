# Twisted-cube reconfiguration of minimum feedback vertex sets on odd prisms

## Finding
For every integer \(k\ge2\), put \(n=2k+1\) and consider the odd prism \(P_n=C_n\square K_2\). All minimum feedback vertex sets of \(P_n\) are classified explicitly, and their one-vertex-exchange graph has a cyclic twisted-cube presentation. It has \(n2^k\) vertices, is connected, bipartite and \((k+1)\)-regular, has \(n2^{k-1}(k+1)\) edges, and has exactly
\[
 n2^{k-2}\left(\binom{k-1}{2}+2(k-2)\right)
\]
unoriented simple four-cycles. The principal contribution is the complete configuration and exchange structure, not the previously established minimum feedback-set cardinality or general connectivity.

## Assumptions and scope
The graph \(P_n\) has vertices \((i,a)\) for \(i\in\mathbb Z_n\), \(a\in\{0,1\}\). Its edges are the two cycles \((i,a)(i+1,a)\) and the rungs \((i,0)(i,1)\), with first coordinates modulo \(n\). A feedback vertex set (FVS) \(S\) is a subset for which \(P_n-S\) is acyclic; a minimum FVS has least cardinality. The exchange graph \(\mathcal R_n\) has minimum FVSs as vertices and connects sets whose symmetric difference has exactly two elements (one removal, one addition). All claims are for the infinite family of odd integers \(n\ge5\); no assertion is made for even prisms.

## Proof
**Step 1: optimal column supports.** Every two consecutive columns form a four-cycle, so the columns meeting an FVS form a vertex cover of the base \(C_n\). For \(n=2k+1\), this forces at least \(k+1\) selected columns, hence \(|S|\ge k+1\). Each minimum-size vertex cover of the odd base cycle has exactly one pair of consecutive occupied columns. Indeed its complement is an independent set of size \(k\), whose cyclic gaps contain two vertices in precisely one place and one vertex in all other gaps. With \(i\) the initial column of the unique consecutive pair, the occupied columns are exactly
\[
 C_i=\{i,i+1,i+3,i+5,\ldots,i+(2k-1)\}\pmod n.
\]
The \(n\) choices of \(i\) are distinct.

**Step 2: layers and acyclicity.** If \(|S|=k+1\), it contains exactly one vertex of each column in \(C_i\). The prism has \(3n=6k+3\) edges and is cubic. On deleting \(S\), the \(3k+1\) retained vertices induce \(3k+e(P_n[S])\) edges. An acyclic graph on \(3k+1\) vertices has at most \(3k\) edges, so every minimum FVS is independent. The only pair of potentially adjacent selected vertices lies in columns \(i,i+1\); thus their selected levels must be opposite.

Conversely, suppose one vertex is selected in each column of \(C_i\), with opposite levels in the consecutive pair. The \(k\) remaining columns \(i+2,i+4,\ldots,i+2k\) contain both retained levels and their rungs. Between consecutive such columns, the sole retained vertex in the intervening selected column links the two rungs. The retained vertex in each of the two special columns \(i,i+1\) attaches to a different end of this chain; their opposite retained levels ensure there is no edge between them. Therefore the induced complement is connected, and by the preceding edge count it is a tree. This proves sufficiency and shows every optimal FVS leaves an induced tree. There are two layer choices in the special pair and two independently at each of the \(k-1\) other occupied columns: exactly \(n2^k\) optimum sets.

**Step 3: exact exchange coordinates.** Write \((i,v_1,\ldots,v_k)\) for the FVS whose selected levels in the ordered columns \(i,i+1,i+3,i+5,\ldots,i+2k-1\) are respectively \(v_1,1-v_1,v_2,v_3,\ldots,v_k\). Exchanging vertices without changing the occupied columns must flip the selected level in a single column. Such a flip is admissible precisely at one of the nonconsecutive occupied columns: it changes coordinate \(v_j\) for one \(2\le j\le k\). The only distinct minimum base-cycle covers differing in one column from \(C_i\) are \(C_{i+2}\) and \(C_{i-2}\). In the forward direction, the removed column is \(i+1\) and the introduced column is \(i+2\). Its new selected level must oppose the selected level \(v_2\) in column \(i+3\). Thus the forward exchange is the bijection
\[
 (i,v_1,v_2,\ldots,v_k)\longleftrightarrow(i+2,1-v_2,v_3,\ldots,v_k,v_1).
\]
The backward exchange is its inverse, whose bit map is \((v_1,\ldots,v_k)\mapsto(v_k,1-v_1,v_2,\ldots,v_{k-1})\). No other exchange is possible. Each state has exactly \(k-1\) within-fiber and two cross-fiber neighbors.

**Step 4: connectivity and bipartition.** Denote the forward bit map by \(T\). One has \(T^k(v)=\mathbf1-v\), hence \(T^{2k}=\mathrm{id}\) and \(T^n=T\) because \(n=2k+1\). Forward moves around the base \(n\)-cycle return to the original fiber and act by \(T\). Within each fiber, independent flips allow free changes to \(v_2,\ldots,v_k\), and a full base tour can change \(v_1\) as well, by first choosing \(v_2\) appropriately. This connects every state in one fiber, and the forward links reach every fiber because \(\gcd(2,n)=1\). Every permitted move changes parity of \(\sum_jv_j\): an internal move flips one bit, and \(T\) complements exactly one input bit. Therefore the graph is connected and bipartite. Counting its constant degree gives \(n2^{k-1}(k+1)\) edges.

**Step 5: simple four-cycles.** The fiber indices form a base \(n\)-cycle under the step \(i\mapsto i+2\), and every edge between successive fibers belongs to a bijective matching. Since \(n\ge5\), a four-cycle projects either entirely to one fiber or to a two-edge backtrack in the base; a walk using four cross-fiber edges cannot give four distinct lifted vertices because the matching at a backtrack is inverse to itself. Each vertex lies in \(\binom{k-1}{2}\) within-fiber squares, indexed by pairs of different internal bit flips. A square using two successive fibers has two within-fiber edges and two crossing edges: an internal bit flip must carry under the crossing map to another internal bit flip. For the forward crossing, exactly \(k-2\) flips (coordinates \(3,\ldots,k\)) have this property; for the backward crossing there are also \(k-2\) (coordinates \(2,\ldots,k-1\)). These describe all further squares. Summing square incidences over \(n2^k\) vertices and dividing by four gives
\[
 c_4(\mathcal R_n)=n2^{k-2}\left(\binom{k-1}{2}+2(k-2)\right).
\]
In particular \(c_4(\mathcal R_5)=0\). No unproved asymptotic or higher-cycle assertion is used.

## Verification
The standalone program `verify_prism_direct.py` constructs the prism's labeled adjacency and checks all \(\binom{2n}{k+1}\) sets of the minimum cardinality for \(n=5,7,9,11,13\), rejecting induced cycles by union-find. From the enumerated solutions, it independently constructs all legal vertex exchanges, checks regularity and connectivity, and counts four-cycles. It also verifies the special adjacent-pair description of every optimum set. It prints `PRISM_DIRECT_EXHAUSTIVE_PASS`.

The standalone program `verify_prism_coordinates.py` independently constructs the abstract bit-transfer graph without using the prism graph or forest tests. For \(n=5,7,9,11,13,15,17\), it checks undirectedness, degree, connectivity, parity bipartition and exact four-cycle count. It also verifies the inverse transfer and base-tour monodromy. It prints `PRISM_SYMBOLIC_TRANSFER_PASS`. Both require only the Python 3 standard library. Finite tests are corroboration; the infinite assertion follows from the five proof steps above.

## Relationship to prior work
Bau's 2007 survey defines the decycling problem, describes the induced-forest complement relation and provides general cubic lower bounds. Chiang, Huang and Yeh (2014 online; 2016 journal), and Wei and Li (2013), establish minimum FVS cardinalities for generalized Petersen graphs, a family containing prisms. The optimum cardinality is not new here. Bousquet, Hommelsheim, Kobayashi, Mühlenthaler and Suzuki (2023), Theorem 2, show all equally sized feedback vertex sets of any \(K_{3,3}\)-minor-free subcubic graph can be reconfigured; therefore connectedness alone is also covered. This theorem instead determines **every** minimum solution, its explicit global exchange graph, and the exact regularity and four-cycle census. Neither the minimum-size statement nor the general connectivity theorem supplies those results.

## Limitations
The classification is limited to odd prisms of base length at least five, with token-jumping (one arbitrary vertex removed and another inserted). It does not characterize shortest paths, larger cycle counts, or even prisms. The published abstract of Chiang–Huang–Yeh was available, but its 18-page full text could not be inspected, so possible incidental counting or configuration analysis there remains a priority risk. Alternate formulations under maximum induced trees, decycling sets, and reconfiguration of induced forests are further plausible historical risks. The result has undergone self-review only; independent audit has not been performed.

## References
- Sheng Bau, *The Decycling Number of Graphs*, arXiv:math/0703544v1 (first public 2007-03-19), https://arxiv.org/abs/math/0703544.
- C.-Y. Chiang, W.-T. Huang, H.-G. Yeh, *Dynamic monopolies and feedback vertex sets in cycle permutation graphs, generalized Petersen graphs and torus cordalis*, Journal of Combinatorial Optimization 31 (2016), 815–832, doi:10.1007/s10878-014-9790-5.
- Wei and Li, *Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs*, Acta Mathematica Sinica (Chinese Series) 56 (2013), 211–216, doi:10.12386/A2013sxxb0022.
- N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler, A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science 979 (2023), 114188, doi:10.1016/j.tcs.2023.114188.
