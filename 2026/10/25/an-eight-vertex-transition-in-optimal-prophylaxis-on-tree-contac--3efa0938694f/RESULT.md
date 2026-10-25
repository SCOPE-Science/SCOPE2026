# An eight-vertex transition in optimal prophylaxis on tree contact networks

## Finding
Fix a finite tree \(T\) with \(n\ge2\) vertices. Preemptively immunize exactly one vertex \(v\), remove that vertex and its incident contact edges, and choose the initially infected vertex uniformly among the remaining \(n-1\) vertices. Each surviving edge independently transmits infection with probability \(p\in(0,1)\), and the final outbreak is the component of the initial vertex among the transmitting edges. Write \(R_T(v;p)\) for the expected final outbreak size.

**Theorem.** For every tree of order at most seven there exists a *single* immunization vertex that minimizes \(R_T(v;p)\) simultaneously for all \(0<p<1\). Eight is the smallest order where such a probability-independent optimal vertex need not exist. At order eight, consider the tree with edge set
\[
\{\{1,0\},\{1,2\},\{0,5\},\{2,3\},\{2,4\},\{5,6\},\{6,7\}\}.
\]
Its optimal vertex is \(2\) for \(0<p<\alpha\), and \(1\) for \(\alpha<p<1\), where \(\alpha\) is the unique root in \((0,1)\) of
\[
\alpha^3+\alpha^2-1=0.
\]
At \(p=\alpha\), both vertices \(1\) and \(2\) are optimal. The threshold lies strictly between \(3/4\) and \(4/5\).

## Assumptions and scope
The epidemic is the independent-bond percolation outbreak model, not the general continuous-time SIR process with potentially correlated outgoing transmissions. Immunization removes a vertex completely *before* selecting the source. The source is uniform among the \(n-1\) remaining vertices, not drawn from the original \(n\) with vaccinated seeds allowed. The policy objective is expected total infected vertices, including the initial source, and is normalized by \(n-1\). All trees are simple, finite, undirected, unweighted and unlabelled for the minimum-order census.

## Proof
After deleting \(v\), two vertices \(x,y\) in the same remaining component are connected by open edges exactly when every edge on their unique path is open. Hence their connectivity probability is \(p^{d_T(x,y)}\). It follows that
\[
(n-1)R_T(v;p)=F_v(p):=\sum_{C\in\operatorname{comp}(T-v)}\ \sum_{x,y\in C}p^{d_T(x,y)}.
\]
Ordered pairs are counted, including \(x=y\); therefore the constant coefficient of every \(F_v\) is \(n-1\). This identity is valid for every real \(0\le p\le1\).

For the eight-vertex witness, direct enumeration of distance pairs in the two forests gives
\[
F_2(p)=7+8p+6p^2+4p^3+2p^4,
\qquad F_1(p)=7+10p+6p^2+2p^3.
\]
Consequently
\[
F_2(p)-F_1(p)=2p(p^3+p^2-1).
\]
The cubic is strictly increasing on \((0,1)\), negative at \(3/4\), and positive at \(4/5\), so there is exactly one transition. To establish these vertices' global optimality rather than only a pairwise comparison, the verification program compares every other vertex's \(F_v\) against both \(F_1\) and \(F_2\) using exact sign certificates: for each other vertex, at least one of \(F_v-F_1\) and \(F_v-F_2\) is nonnegative throughout \((0,1)\). Therefore no third vertex can improve on their pointwise minimum.

For orders \(2\) through \(7\), the supplied exhaustive certificate recursively produces all unlabelled trees: begin with the unique two-vertex tree; for each tree of order \(j\), attach a leaf to every existing vertex and discard duplicates only by explicit graph isomorphism. Every \((j+1)\)-vertex tree arises because every tree has a leaf, so deleting a leaf reduces it to an order-\(j\) tree. The generated class counts are \(1,1,2,3,6,11\) at orders \(2,3,4,5,6,7\). For every generated tree, the checker constructs all exact integer distance polynomials \(F_v\) and finds at least one vertex \(v_*\) such that \(F_v-F_{v_*}\ge0\) for all competitors and all \(p\in(0,1)\). It certifies this using exact rational factorization and real-root counting: every nonzero comparison is nonnegative at \(p=1/2\) and has no zero in the open interval. This finite enumeration establishes the lower bound without numerical sampling or extrapolation. The explicit eight-vertex witness establishes sharpness.

## Verification
Run `python verify.py` with the Python packages listed in `requirements.txt`. The standard output is deterministic JSON and agrees with `certificate.json` when whitespace and key order are ignored. The checker performs \(141\) comparison tests, generates the \(23\) unlabelled trees of order eight for independent count consistency, verifies all potential immunization targets in the witness, and independently recomputes the two witness expectations by enumerating every retained-edge subset in each deleted-vertex forest at \(p=1/2,3/4,9/10\). The latter tests do not replace the all-probability polynomial proof. The finite classification relies on the supplied exhaustive enumeration and exact root-count algorithm; no closed-form structural characterization of all optimal vertices for arbitrary tree orders is claimed.

## Relationship to prior work
Newman's network epidemic/percolation formulation provides the infection model, including the interpretation of the final outbreak as a connected open-edge cluster; it does not supply this optimization transition or its minimum tree order. Holme's study explicitly treats vaccination importance and exact small-network calculations, but uses a continuous-time exponential-infection/recovery SIR model and investigates graphs through seven vertices, whereas the present result is the homogeneous independent-bond tree case with an eight-vertex sharp threshold. The conclusion concerns a changing *optimal immunization target*, not the distinct source-seeding optimization problem.

## Limitations
The theorem does not assert a universal optimal immunization node for arbitrary trees or general contact graphs. It does not apply without modification to correlated edge transmissions, time-dependent infection hazards, nonuniform or specified sources, incomplete vaccine efficacy, immunization after outbreak initiation, or multiple vaccinees. The eight-vertex threshold is for the stated independent-bond and uniform-source objective; it is not a bound for every epidemic model. A matching bibliographic result may exist under another centrality or reliability formulation, and independent literature review is still needed.

## References
1. M. E. J. Newman, *The spread of epidemic disease on networks*, arXiv:cond-mat/0205009, first submitted 2002-04-30; *Physical Review E* 66, 016128 (2002), https://doi.org/10.1103/PhysRevE.66.016128.
2. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (first submitted 2017-08-22), *Physical Review E* 96, 062305 (2017), https://doi.org/10.1103/PhysRevE.96.062305.
3. F. Takeuchi and K. Yamamoto, *Effectiveness of realistic vaccination strategies for contact networks of various degree distributions*, *Journal of Theoretical Biology* 243, 39–47 (2006), https://doi.org/10.1016/j.jtbi.2006.05.033.
