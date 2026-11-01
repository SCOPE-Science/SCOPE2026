# A universal parity correction in primitive two-cycles of leaf-decorated rings

## Finding

Let \(n\ge3\) and \(r\ge1\) be integers. Form the labelled simple graph \(S_{n,r}\) from a cycle \(C_n\) by attaching exactly \(r\) distinct degree-one leaves to each cycle vertex. Apply ordinary synchronous degree-threshold parallel chip-firing without a sink. A vertex fires one chip along each incident edge precisely when it currently has at least its degree in chips.

For a primitive period-two orbit, write \(s_i\in\{0,1\}\) for whether cycle vertex \(i\) fires in either selected temporal phase. The number \(b\) of cyclic core edges with \(s_i\ne s_{i+1}\) is independent of which of the two phases was chosen, and is even. Define the labelled-orbit interface enumerator
\[
P_{n,r}(z)=\sum_{\substack{\mathcal O\text{ primitive}\\|\mathcal O|=2}}z^{b(\mathcal O)}.
\]
Let
\[
T_r(z)=\begin{pmatrix}r&(r+1)z\\r+1&(r+2)z\end{pmatrix}.
\]
Then the exact polynomial identity is
\[
\boxed{P_{n,r}(z)=\frac12\left(\operatorname{tr}(T_r(z)^n)+\operatorname{tr}(T_r(-z)^n)\right).}
\]
Consequently, the number of distinct primitive two-cycle orbits is
\[
\boxed{N_{n,r}=P_{n,r}(1)=\frac{\left(r+1+\sqrt{(r+1)^2+1}\right)^n+\left(r+1-\sqrt{(r+1)^2+1}\right)^n}{2}+(-1)^n.}
\]
The alternating correction \((-1)^n\) is **exact and independent of the number of leaves**. Every binary firing-phase assignment to the core is realizable. The extremal polynomial coefficients are \([z^0]P_{n,r}(z)=r^n\); for even \(n\), \([z^n]P_{n,r}(z)=(r+2)^n\); for odd \(n\), \([z^{n-1}]P_{n,r}(z)=n(r+1)^2(r+2)^{n-2}\). For one leaf per core vertex, the initial totals are \(N_{3,1}=37\), \(N_{4,1}=162\), \(N_{5,1}=681\), and \(N_{6,1}=2890\).

## Assumptions and scope

All vertex labels are distinguished. Orbits are identified only under temporal rotation (the two states of a primitive two-cycle), not under graph rotations, reflections, or interchange of leaves. Configurations have arbitrary nonnegative integral chip counts, not merely bounded initial heights. The fixed graph is connected, loopless and undirected. The polynomial is indexed by disagreement edges in the two-phase **core firing** pattern, not by total chip count. Only primitive period-two orbits are enumerated; other primitive periods and basins are outside the theorem.

## Proof

For a finite connected simple graph \(G\), write \(d_v\) for the degree, \(h_v\) for a chip height, and \(f_v\in\{0,1\}\) for firing during the first round. If the state returns after two rounds, the vector of two-round firing counts has zero graph Laplacian. By connectedness and the maximum principle it is constant. For a primitive two-cycle the constant cannot be zero (nobody fires in either round) or two (everybody fires in both rounds), since either would make the state fixed. Thus every vertex fires once in the two rounds, and the second-phase firing pattern is \(1-f_v\).

Let \(k_v=\#\{u\sim v:f_u\ne f_v\}\), the number of opposite-phase neighbors. If \(f_v=1\), the vertex loses \(k_v\) chips in the first round and must change from firing to waiting, hence
\[
d_v\le h_v\le d_v+k_v-1.
\]
If \(f_v=0\), it gains \(k_v\) chips and must change from waiting to firing, hence
\[
d_v-k_v\le h_v\le d_v-1.
\]
Both intervals have exactly \(k_v\) nonnegative integers; they are empty when \(k_v=0\). Conversely, every collection of independent choices from these intervals flips all firing bits after one round, and returns to the identical chip configuration after two rounds because each vertex has then sent and received exactly its degree. Therefore the number of first-phase chip configurations with prescribed firing vector is \(\prod_v k_v\), and each primitive two-cycle contributes precisely two phase configurations.

In \(S_{n,r}\), every degree-one leaf must fire in the phase opposite to its cycle neighbor; its allowable chip height is unique. For a binary core word \(s=(s_1,\ldots,s_n)\), set \(e_i=1\) if \(s_i\ne s_{i+1}\) and \(e_i=0\) otherwise, with cyclic indices. The cycle vertex \(i\) has exactly \(k_i=r+e_{i-1}+e_i\) opposite-phase neighbors. Thus its chip-height choices contribute the factor \(r+e_{i-1}+e_i\). Since \(r\ge1\), every binary core word is feasible.

Cyclic binary core words correspond two-to-one to edge words \((e_1,\ldots,e_n)\) having even sum; the two core words differ by complementation. Dividing by two for temporal phase rotation yields exactly
\[
P_{n,r}(z)=\sum_{\substack{e\in\{0,1\}^n\\\sum_i e_i\text{ even}}}z^{\sum_i e_i}\prod_{i=1}^n(r+e_{i-1}+e_i).
\]
The transfer matrix \(T_r(z)\), whose entry from previous edge bit \(a\) to next bit \(b\) is \((r+a+b)z^b\), has trace power equal to the unrestricted sum over cyclic edge words. The even-parity projector \((1+(-1)^{\sum e_i})/2\) proves the boxed polynomial identity.

At \(z=1\), \(T_r(1)\) has trace \(2(r+1)\), determinant \(-1\), and eigenvalues \(r+1\pm\sqrt{(r+1)^2+1}\). In contrast, \(T_r(-1)\) has trace \(-2\) and determinant \(1\), so both eigenvalues equal \(-1\) (diagonalizability is unnecessary to compute the trace of its powers). Consequently \(\operatorname{tr}(T_r(-1)^n)=2(-1)^n\), giving the second boxed identity. The extremal coefficients follow by enumerating, respectively, zero, all, or all but one of the cyclic edge bits equal to one.

## Verification

Run `python3 verify_sunlet.py` with standard Python 3; no third-party modules or downloaded data are required. The checker uses two distinct constructions: explicit chip updates on all states with \(0\le h_v<2d_v\), and independent enumeration of even-parity boundary words. It checks the full interface histogram for parameter pairs \((n,r)=(3,1),(4,1),(5,1),(3,2),(4,2),(3,3)\), covering exactly 1,864,640 bounded vertex-level states. It separately checks the phase-product formula and the integer trace identity for additional lengths through \(30\) and leaf multiplicities through \(15\). The successful recorded output ends in `SUNLET_PRIMITIVE_TWO_CYCLE_VERIFY_OK`.

The finite checks are consistency evidence, not a substitute for the exact proof for all \(n,r\). Their bounded state restriction is exhaustive for two-cycles, since the proved local intervals force \(h_v\le2d_v-1\).

## Relationship to prior work

Dall'Asta's one-dimensional deterministic fixed-energy sandpile treats the **undecorated** cycle (degree two) and identifies its periodic regimes. The general two-round equal-firing-count criterion and confinement principles are established in Jiang (2010), and their use here is not claimed as new. Scully, Jiang and Zhang analyze permissible firing words and the removal of tree-like appendages; the relevant leaf-removal statement does not enumerate microscopic chip allocations on uniformly leaf-decorated rings.

The distinct contribution is the complete interface-resolved orbit polynomial for all positive leaf multiplicities, together with the explicit closed orbit count and the leaf-multiplicity-independent parity correction. In particular, attaching leaves can change the exponential count of distinct chip-realized primitive two-cycles even though the core remains a single cycle. For comparison only, the undecorated \(r=0\) specialization has growth constant \(1+\sqrt2\), whereas \(r=1\) has \(2+\sqrt5\). Neither this theorem nor these counts follow as an explicit numerical specialization of the cited period-length or firing-word statements without the present chip-height enumeration and transfer calculation.

## Limitations

No claim is made for periods other than two, for transient attraction basins, for unlabeled graph-isomorphism orbit counts, or for sinks/dissipation. Published descriptions of early chip-firing work are broader than the exact sources inspected here; in particular, the original 1992 Bitar–Goles article was not fully available for text comparison. A historical equivalent expressed with different graph notation or via a general weighted partition function remains a residual originality risk.

## References

- L. Dall'Asta, *Exact solution of the one-dimensional deterministic Fixed-Energy Sandpile*, first arXiv submission 2006-01-12, https://arxiv.org/abs/cond-mat/0601267 .
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, first arXiv submission 2010-03-04, https://arxiv.org/abs/1003.0943 .
- T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, first arXiv submission 2012-11-29, https://arxiv.org/abs/1211.6786 ; see also the full-text precursor https://dmtcs.episciences.org/articles/2421/download .
- J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300, https://doi.org/10.1016/0304-3975(92)90316-8 .
