# Exact VC dimension and linear online shattering gap for matching-covered ladders

## Finding
Let \(L_n=P_2\mathbin{\square}P_n\) be the ordinary two-row, \(n\)-column ladder, \(n\ge1\), and let \(\mathcal P_n\) be the set of incidence vectors of *all* its perfect matchings, with a Boolean query at an edge reporting whether that edge occurs. Then
\[
|\mathcal P_n|=F_{n+1},\qquad \operatorname{VCdim}(\mathcal P_n)=\left\lfloor\frac n2\right\rfloor,
\]
where \(F_1=F_2=1\) are Fibonacci numbers. In addition,
\[
\operatorname{Ldim}(\mathcal P_{11})=7,
\qquad \operatorname{VCdim}(\mathcal P_{11})=5.
\]
For every integer \(m\ge1\),
\[
\operatorname{Ldim}(\mathcal P_{11m})\ge7m,
\quad \operatorname{VCdim}(\mathcal P_{11m})=\left\lfloor\frac{11m}{2}\right\rfloor,
\quad \operatorname{Ldim}-\operatorname{VCdim}\ge\left\lceil\frac{3m}{2}\right\rceil.
\]
For \(n\ge2\), these are the perfect-matchings classes of ordinary planar, bipartite, two-vertex-connected, maximum-degree-three ladders; **each edge** lies in some perfect matching. Thus the unbounded static-versus-adaptive gap occurs with no forbidden matching edges or separating bridges.

## Assumptions and scope
All graphs are finite and simple. The two rows have vertices \(t_i,b_i\), for \(1\le i\le n\). The edges are vertical rungs \(v_i=t_ib_i\) and horizontal edges \(t_it_{i+1},b_ib_{i+1}\) for \(1\le i<n\). The concept set consists of all perfect matchings, not arbitrary matchings. VC dimension uses a fixed set of distinct edge queries. Littlestone dimension is the greatest depth of a fully branching binary tree of edge queries with a consistent perfect matching at each leaf. Query outcomes are \(0\) (absent) and \(1\) (present). Repeated queries cannot increase either dimension. The exceptional \(n=1\) ladder has one perfect matching, so both dimensions are zero.

## Proof
**Matching structure.** For a cut immediately after column \(i\), count matched edges crossing from the first \(2i\) vertices to the rest. The count is even because every vertex in the prefix has one matched edge. There are only two edges crossing this cut, so either both or neither cross. Consequently each perfect matching is uniquely a tiling of the column path by a one-column *rung* tile or a two-column tile consisting of both horizontal edges. A two-column tile starting at \(i\) is called a dimer at \(i\). The tiling recurrence gives \(|\mathcal P_n|=F_{n+1}\), with the stated Fibonacci initialization. The top and bottom horizontal edges at the same cut are therefore equivalent Boolean queries.

**VC lower bound.** Query the top horizontal edges spanning the pairwise disjoint column pairs \((1,2),(3,4),\ldots\). Any prescribed binary labeling is achieved by tiling each two-column pair either with its horizontal dimer (value one) or with two vertical rungs (value zero), and using a rung on a remaining last column if \(n\) is odd. Thus \(\operatorname{VCdim}\ge\lfloor n/2\rfloor\).

**VC upper bound.** Suppose a set \(S\) of edge queries is shattered. Because equivalent top and bottom horizontal queries cannot both lie in \(S\), write \(S=H\sqcup V\), where \(H\) comprises \(h\) distinct horizontal-cut queries and \(V\) comprises \(v\) rung queries. Shattering the all-one labeling forces the cuts in \(H\) to be pairwise nonadjacent: their dimers occupy disjoint two-column intervals. It also forces all rungs in \(V\) to lie outside those occupied columns. Fix the \(h\) horizontal queries to value one. Remove their \(2h\) occupied columns and write \(R\) for the remaining \(N=n-2h\) columns. Within \(R\), all \(v\) queried rungs can still realize every labeling.

Partition their columns into \(V_{\mathrm{even}}\) and \(V_{\mathrm{odd}}\) according to the parity of the original column index. Consider the labeling in which the rung queries in \(V_{\mathrm{even}}\) are zero and all rung queries in \(V_{\mathrm{odd}}\) are one. Every even queried column must then belong to a horizontal dimer: it cannot pair with a different even column, and it cannot pair with a queried odd column, whose rung is present. Thus the disjoint horizontal dimers provide an injection from \(V_{\mathrm{even}}\) into the unqueried odd columns of \(R\). Apply the reverse labeling to obtain an injection from \(V_{\mathrm{odd}}\) into the unqueried even columns of \(R\). These two target sets are disjoint, so the injections combine to show that \(R\) has at least \(v\) unqueried columns, or \(2v\le N\). It follows that
\[
|S|=h+v\le h+\frac{n-2h}{2}=\frac n2,
\]
proving the claimed exact VC dimension.

**Exact eleven-column adaptive dimension.** The Fibonacci count gives \(|\mathcal P_{11}|=F_{12}=144\). A complete binary mistake tree of depth \(d\) must have \(2^d\) distinct terminal concepts, so \(\operatorname{Ldim}(\mathcal P_{11})\le\lfloor\log_2 144\rfloor=7\). The included `ladder11_tree.json` is a fully explicit depth-seven tree. It contains \(127\) internal nodes, \(128\) leaf witnesses, and only queries `v1`–`v11` and `h1`–`h10` (where `h` denotes the top horizontal edge). Each leaf gives a bitmask of dimer starts. The independent `verify_witness.py` reconstructs all perfect matchings directly from the \(22\)-vertex graph, checks each of the \(127\) splits, the distinctness and consistency of all \(128\) leaf witnesses, and the common depth seven. This finite certificate proves the matching lower bound and hence equality.

**Linear gap on ordinary connected ladders.** Partition the \(11m\) columns into \(m\) consecutive blocks of length \(11\). Restrict to the subfamily of matchings having no horizontal dimer crossing a block boundary. This subfamily is the independent Cartesian product of \(m\) copies of \(\mathcal P_{11}\); it sits inside the *full* matching family \(\mathcal P_{11m}\), in which boundary-crossing dimers remain available. Query the blocks one at a time, using the full depth-seven mistake tree in each block. For any binary answer path, independent leaf witnesses concatenate to a perfect matching of the full ladder. This yields a depth-\(7m\) shattered tree and establishes the lower bound; the exact VC formula supplies the gap. Finally, every ladder edge belongs to a perfect matching: rungs occur in the all-rung matching, and each horizontal edge belongs to a dimer across its columns together with rungs elsewhere. For \(n\ge2\), the ladder's outer perimeter is a spanning cycle, proving two-vertex-connectivity.

## Verification
Requires Python 3 only. Place `ladder11_tree.json`, `verify_witness.py`, and `finite_recurrence.py` in one directory and execute:

```bash
python3 verify_witness.py
python3 finite_recurrence.py
```

The first program enumerates the \(144\) graph-theoretic perfect matchings independently of the dimer generator, reconstructs their edge signatures, and verifies every terminal constraint and node of the supplied tree. It returns `LADDER11_TREE_CERTIFICATE_PASS` with \(127\) internal nodes, \(128\) distinct leaves, and depth \(7\). The second implements a separate exact minimax recurrence over finite version spaces for column counts \(1\) to \(11\); its Littlestone sequence is \((0,1,1,2,3,3,4,5,5,6,7)\). These computations are exhaustive finite certificates for the eleven-column statement, not a substitute for the all-\(n\) VC proof or product lower bound.

## Relationship to prior work
The static VC dimension and adaptive Littlestone dimension are standard learning-theoretic invariants. Ghazi, Golowich, Kumar, and Manurangsi (2020) study generic closure bounds under Boolean aggregation, while Manurangsi (2023) studies computational hardness for explicitly represented concept classes. Their results do not imply the specified ladder classifications. Standard domino-tiling/Fibonacci facts supply the counting context. Tratnik and Ye (2017) prove cubical-embedding and Clar-polynomial identities for resonance graphs whose vertices are perfect matchings; Lam and Zhang (2003), as credited there, establish distributive-lattice structure for the resonance graph of matching-covered plane bipartite graphs. Those invariants and their graph objects differ from fixed/adaptive queries of whether *an original ladder edge* belongs to an unknown matching. The present depth-seven adaptive witness and global edge-query classification are not stated in the inspected theorems. A previously accessible construction gives an adaptive gap using separate five-column ladder blocks joined by edges excluded from every matching; that construction does not yield the present all-edge-feasible, two-vertex-connected ladder result. Literature comparisons did not locate a publication asserting the same full statement; this is not a proof of absolute historical priority.

## Limitations
The exact Littlestone dimension is established here for the eleven-column ladder, not for arbitrary width. For widths divisible by eleven, only the stated *lower bound* on the Littlestone dimension is claimed; no matching upper bound is asserted. The graph result is about ordinary two-row ladders and full perfect-matching concept classes, not arbitrary planar matching-covered graphs. The eleven-column assertion relies on an explicitly replayable finite certificate rather than a short closed-form depth formula. Independent scientific validation and a comprehensive priority audit remain outstanding.

## References
- B. Ghazi, N. Golowich, R. Kumar, and P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668, first publicly submitted 2020-07-07. https://arxiv.org/abs/2007.03668
- N. Tratnik and D. Ye, *Resonance Graphs and Perfect Matchings of Graphs on Surfaces*, arXiv:1710.00761, first publicly submitted 2017-10-02. https://arxiv.org/abs/1710.00761
- P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, ITCS 2023, published 2023-02-01, doi:10.4230/LIPIcs.ITCS.2023.85. https://doi.org/10.4230/LIPIcs.ITCS.2023.85
