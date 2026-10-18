# Six agents are the sharp threshold for opinion-diversity reversal of a contact-link effect

## Finding
Let \(G\) be a finite connected, undirected, loopless simple graph of order \(n\). Under asynchronous voter copying, at each step choose a vertex uniformly from \(V(G)\), then choose one of its neighbors uniformly and copy that neighbor's opinion. All updates, including unchanged opinions, count as one step. Initially each vertex chooses independently and uniformly from \(q\) opinion labels. Denote by \(T_q(G)\) the expected number of updates until every vertex has the same opinion.

For \(q=2\) and \(q=3\), adding one missing edge first can have **opposite strict effects** on \(T_q\) at **six vertices**. In particular, on vertices \(\{0,1,2,3,4,5\}\), let
\[
E(G)=\{02,03,04,05,12,13\},\qquad H=G+14.
\]
Here \(ij\) means the undirected edge between vertices \(i\) and \(j\). Exact arithmetic gives
\[
T_2(H)-T_2(G)=\frac{1122656114180194155}{386211260511212369552}>0,
\]
whereas
\[
T_3(H)-T_3(G)=-\frac{28001352030647246132654763802315}{3178404527081395198208684734434114}<0.
\]
Thus the new contact **slows binary consensus** but **speeds three-opinion consensus** under otherwise identical dynamics and uniform independent initial opinions. No such opposite-sign response is possible on fewer than six vertices.

## Assumptions and scope
For each \(q\in\{2,3\}\), every vertex initially samples one of \(q\) exchangeable labels, independently with probability \(1/q\). There is no spontaneous mutation, bias or rewiring after the specified one-time graph modification. The graph remains connected before and after edge insertion. Time is counted in single attempted node updates, *not* rescaled to updates per vertex. A strict sign reversal requires the two changes to have opposite nonzero signs; a zero response is not counted as a reversal.

## Proof
**Finite absorbing chain, reduced exactly by opinion relabeling.** An opinion configuration is completely described, up to relabeling of the \(q\) possible labels, by its set partition \(\pi\) of the vertices into its nonempty same-opinion blocks. Use restricted-growth strings to choose a unique representative of each partition: the first entry is zero, and each succeeding entry is at most one larger than the largest preceding entry. Retain only partitions having at most \(q\) blocks. The one-block partition is absorbing. From a nonabsorbing partition, the transition \(\pi\to\pi'\) associated with vertex \(v\) copying neighbor \(w\) has probability \(1/(n\deg_G(v))\), where \(\pi'\) is the canonical partition obtained by moving \(v\) into the block of \(w\) and removing a block if emptied. Summing probabilities of coincident outcomes constructs a substochastic transition matrix \(Q_{G,q}\) on transient partitions.

A connected graph reaches unanimity almost surely: from any nonconsensus state, there is a finite positive-probability sequence of updates copying an opinion along a spanning tree until all vertices agree. Therefore \(I-Q_{G,q}\) is invertible, and the mean absorption vector \(t\) is the unique solution of
\[
(I-Q_{G,q})t=\mathbf 1.
\]
If \(\pi\) has \(k\) blocks, precisely \((q)_k=q(q-1)\cdots(q-k+1)\) initial labeled opinion assignments produce it. Hence
\[
T_q(G)=\frac{1}{q^n}\sum_{\pi:\,2\le |\pi|\le q}(q)_{|\pi|}\,t(\pi).
\]
This calculation uses rational transition probabilities and an exact rational linear solve, so each result is a rational identity rather than a floating-point estimate.

**Exact six-vertex construction.** Insert the displayed edge sets into the transition construction, separately for \(q=2\) and \(q=3\). On six vertices the reduced transient state spaces have respectively \(31\) and \(121\) set partitions. Fractional Gaussian elimination gives the displayed signed differences. These fractions are generated and checked anew by `verify_multicolor_voter.py`; no rounded comparison is used to determine either sign.

**Exhaustive exclusion below six vertices.** For each \(2\le n\le5\), enumerate all \(2^{\binom n2}\) undirected labeled simple graphs using their binary edge masks. Discard disconnected graphs. Identify isomorphic graphs by enumerating every permutation of the vertex labels, retaining one representative per orbit. Because relabeling preserves voter dynamics and expected times, checking representatives loses no instance. For each representative and each nonedge, compute the exact differences \(\Delta_q=T_q(G+e)-T_q(G)\) for \(q=2,3\) from the rational partition chain. Verify \(\Delta_2\Delta_3\ge0\) identically. The distinct connected-graph representative counts for \(n=3,4,5\) are respectively \(2,6,21\); the corresponding numbers of tested nonedge insertions are \(1,11,80\). There are no nonedges in a connected graph of order two. Across all \(92\) tested edge-marked cases, \(\Delta_2\Delta_3\ge0\); in the single three-vertex case both differences vanish. The self-contained verifier implements the entire graph and partition enumeration and is sufficient to reproduce the finite part of this proof without a graph atlas or floating-point library.

Together, the exact six-vertex witness and the exhaustive smaller-order exclusion prove the claimed sharp threshold.

## Verification
Run `python3 verify_multicolor_voter.py` with a Python 3 standard-library interpreter. It independently enumerates every connected graph isomorphism class up to order five from first principles, tests every missing edge and both opinion counts, and recomputes both six-vertex differences by rational linear systems. A successful execution prints `VERIFIED` and the two signed witness fractions. Finite floating-point experiments alone could not establish the minimum; all decisive checks in this package use exact arithmetic.

## Relationship to prior work
Iwamasa and Masuda (2014) study network effects on consensus times for several binary-opinion update schemes, including node copying, using a different balanced-configuration averaging convention. Their published optimization results do not compare the sign of an identical edge addition under two versus three independent uniform initial opinion labels. Shi, Mucha and Durrett (2013) study multiple opinions on *coevolving* networks with opinion-dependent link rewiring; the present network remains fixed during copying. Finite-graph voter consensus and its connection to coalescing random walks are classical. Neither the update mechanism, exact absorbing-chain method, nor the general possibility of binary edge-addition slowdowns is claimed as new; the contribution is their sharp six-vertex **opinion-diversity sign reversal**.

## Limitations
The sharp minimality statement is only for comparison of \(q=2\) and \(q=3\), with independent *uniform* initial labels and the particular node-update voter model. It does not cover majority/plurality dynamics, synchronous updates, colored initial states conditioned to have balanced counts, adaptive edges, or arbitrary larger opinion alphabets. Complete lower-order enumeration is a finite computer-assisted proof; it is not a classification of all six-vertex witnesses. An equivalent specialization hidden in earlier work may remain undiscovered.

## References
1. Shi, F., Mucha, P. J., and Durrett, R. (2013), *A multi-opinion evolving voter model with infinitely many phase transitions*, arXiv:1303.7434 (initial public posting March 29, 2013); Physical Review E 88, 062818. DOI: 10.1103/PhysRevE.88.062818.
2. Iwamasa, Y., and Masuda, N. (2014), *Networks maximising the consensus time of voter models*, arXiv:1404.6360 (initial public posting April 25, 2014); Physical Review E 90, 012816. DOI: 10.1103/PhysRevE.90.012816.
3. Aldous, D., and Fill, J. A., *Reversible Markov Chains and Random Walks on Graphs*, Chapter 14, Section 3, manuscript (online version): https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S3.html.
