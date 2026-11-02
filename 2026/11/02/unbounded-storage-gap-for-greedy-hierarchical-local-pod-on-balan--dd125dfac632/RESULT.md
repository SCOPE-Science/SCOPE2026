# Unbounded storage gap for greedy hierarchical local POD on balanced path meshes

## Finding

For every dyadic integer \(r=2^d\ge 2\), there exists a binary snapshot matrix on a one-dimensional uniform path mesh, a positive prescribed NRMSE tolerance, and a fixed connected, exactly balanced dyadic row-partition hierarchy for which the size-proportional local POD rank rule of Nuca–Parsani–Dalcin returns the **exact** local ranks, but its one-step storage-decreasing greedy refinement stops at the root. Within the same full hierarchy, the global minimum-cost partition has a storage advantage that grows without bound.

Specifically, for the matrices constructed below, the respective costs under the source paper's algebraic factor-storage measure are

\[
S_{\mathrm{greedy}}=r(2r^3+2r+1),\qquad
S_{\mathrm{optimal}}=2r(r+1)^2,
\]

so that

\[
\frac{S_{\mathrm{greedy}}}{S_{\mathrm{optimal}}}
=\frac{2r^3+2r+1}{2(r+1)^2}\sim r\longrightarrow\infty.
\]

Both representations reconstruct the data *exactly* and both use less factor storage than the uncompressed matrix. The result is an unbounded worst-case ratio for this specified greedy decision rule and hierarchy, **not** a claim about every possible graph-partitioner implementation or about the accuracy guarantee.

## Assumptions and scope

Fix an integer \(d\ge 1\) and set \(r=2^d\), \(b=r^2\), \(n=2r\), and \(m=2rb=2r^3\). Consider a path of \(m\) equal-length, unit-volume cells with one scalar piecewise-constant degree of freedom per cell, and take the discrete mass matrix \(M=I_m\). Thus each connected interval of cells has an identity local mass matrix.

Let \(e_j\) denote standard coordinate vectors in \(\mathbb R^n\) (one-based indexing). Define the row vectors

\[
t_j=e_j+e_{r+j}\qquad(1\le j\le r).
\]

Form \(A\in\{0,1\}^{m\times n}\) by taking \(b\) consecutive copies of each \(t_1,t_2,\ldots,t_r\), followed by the same sequence of \(r\) groups again. Thus \(\operatorname{rank}(A)=r<n\) and the entry range is \(\Delta=1\). Prescribe the strictly positive coefficient-space tolerance \(\varepsilon_{\mathrm{NRMSE}}=1/(4r)\).

Fix the connected, balanced dyadic hierarchy which first divides the two repeated sequences and then bisects each group-aligned interval until its leaves are the \(2r\) homogeneous groups of \(b\) rows. Refinement to individual unit cells is also permitted; it cannot improve the leaf-group cost. Every candidate split separates a contiguous even-length interval into two equal halves. Initially there is one domain and each tentative split has two children.

For an interval containing \(m_k\) rows, its local rank \(p_k\) is the smallest integer at least one with

\[
\sum_{j>p_k}\sigma_j(A_k)^2\le
\lambda_{\min}(M_k)\Delta^2m_kn\varepsilon_{\mathrm{NRMSE}}^2.
\]

The factor-storage cost for that block is \(S(A_k)=(m_k+n+1)p_k\). The greedy procedure retains the parent whenever its storage is no greater than the sum of the costs of its two tentative children. These are precisely the mathematical rank and cost conventions examined; actual partition-encoding overhead is excluded from both sides.

## Proof

**1. Local spectra.** Each row \(t_j\) has squared Euclidean norm \(2\), and vectors with different indices are orthogonal. The root contains each of the \(r\) directions \(2b\) times, so its \(r\) positive squared singular values are exactly \(4b\). Both first-generation children contain each direction \(b\) times, giving \(r\) positive squared singular values \(2b\). Any proper dyadic descendant aligned with group boundaries has \(g\) distinct directions, one group per direction; its \(g\) positive squared singular values are all \(2b\).

The root's allotted squared-error budget is

\[
m n\varepsilon_{\mathrm{NRMSE}}^2
=(2rb)(2r)/(16r^2)=b/4<4b.
\]

At a proper group-aligned node containing \(g\le r\) groups, the allotted budget is

\[
(gb)n\varepsilon_{\mathrm{NRMSE}}^2
=gb/(8r)\le b/8<2b.
\]

In both cases discarding even the smallest positive singular value violates the budget. Therefore every such node selects its exact algebraic rank. For a node of \(h\le b\) identical rows inside a homogeneous group, its sole positive squared singular value is \(2h\), while its allotted budget is \(h/(8r)<2h\), so its selected rank is one. In particular, every representation examined below has reconstruction error zero and hence satisfies the positive NRMSE tolerance.

**2. Greedy root rejection.** Under the storage convention, the unsplit root has cost

\[
S_{\mathrm{root}}=(m+n+1)r=r(2r^3+2r+1).
\]

Its two children both have rank \(r\), so their combined cost is

\[
S_{\mathrm{first\ split}}=r(m+2n+2)
=S_{\mathrm{root}}+r(n+1)>S_{\mathrm{root}}.
\]

The greedy rule therefore refuses the first split and terminates without examining any descendants; its output cost is \(S_{\mathrm{greedy}}=S_{\mathrm{root}}\).

**3. The optimal cut of the complete hierarchy.** Consider a group-aligned node strictly below the root that contains \(g\ge2\) distinct groups. Its rank equals \(g\), so retaining it costs \(g(gb+n+1)\). Splitting it into two equal group-aligned children produces a total cost of

\[
2\cdot\frac g2\left(\frac g2 b+n+1\right)
=g\left(\frac g2 b+n+1\right),
\]

which is strictly smaller by \(g^2b/2\). Repeating such refinements strictly decreases the cost until every leaf is one homogeneous group. Once inside a homogeneous group, every descendant still has rank one; replacing the group by multiple pieces strictly increases storage by \(n+1\) per additional piece. Hence a complete optimal cut within each child of the root consists of its \(r\) individual homogeneous groups.

The sum over all \(2r\) homogeneous groups is

\[
S_{\mathrm{fine}}=2r(b+n+1)=2r(r+1)^2.
\]

A complete rooted dyadic cut either retains the root or chooses a cut separately in both children. Thus its optimal cost is the smaller of \(S_{\mathrm{root}}\) and \(S_{\mathrm{fine}}\). Their difference is

\[
S_{\mathrm{root}}-S_{\mathrm{fine}}
=r\bigl(2r^3-2r^2-2r-1\bigr)>0
\qquad(r\ge2).
\]

Therefore the fine partition is the *global cost minimum within the specified complete dyadic hierarchy*.

**4. Divergence and nontrivial compression.** Dividing the exact costs gives the stated ratio, which is asymptotic to \(r\). Meanwhile, the raw matrix contains \(mn=4r^4\) scalar entries, and

\[
\frac{S_{\mathrm{root}}}{mn}
=\frac12+\frac{1}{2r^2}+\frac{1}{4r^3}<1
\qquad(r\ge2).
\]

Thus even the greedy root representation genuinely compresses the matrix, while the optimal hierarchy cut compresses much further. This proves the claim for every dyadic \(r\), and in particular proves that no dimension-independent storage approximation ratio exists for the stated greedy rule.

## Verification

The standalone standard-library Python script `verify.py` materializes exact matrix Gram matrices at small dyadic sizes; computes the exact integer singular-value multiplicities from repeated orthogonal row directions; checks the strictly positive NRMSE budget against the least nonzero squared singular value at every hierarchy node; and uses a full dynamic-programming recursion to verify the global tree optimum independently of the closed-form argument. It also checks root refusal, zero-error rank selection, and actual compression relative to the raw matrix.

Run `python3 verify.py`. Its deterministic execution completes **3,550 exact assertions**. Checked dyadic sizes include \(r=2,4,8,16,32,64\), with concrete Gram matrices constructed at the three smallest sizes. These finite tests support but do not replace the proof for all \(r=2^d\).

## Relationship to prior work

Nuca, Parsani and Dalcin [1], particularly their equations (25)–(26), Section 4, and Remark 4.2, define the local rank criterion and storage-decreasing hierarchical rule used here. They explicitly acknowledge that an immediately nonprofitable split can conceal beneficial deeper refinement, and they do **not** claim global optimum of the greedy search. The contribution here is a quantitative, arbitrarily large **worst-case** storage ratio despite a positive prescribed error tolerance, exact local POD reconstructions, legitimate balanced connected splits, and real compression by both outputs. The qualitative observation itself is prior work, not a novelty claim.

Shamrai [2] examines low-rank compression of clusters of matrices formed by concatenation and evaluates merge strategies under error constraints; that is a different optimization problem from the present size-proportional, local-rank, path-mesh top-down bisection. The abstract of Ehrlacher, Grigori, Lombardi and Song [3] concerns adaptive hierarchical subtensor compression and is thematically related. Full text of [3] was not available for an exhaustive implication comparison, so historical priority should be treated as provisional.

## Limitations

The theorem concerns a deliberately constructed binary snapshot family and a prescribed admissible balanced-bisection hierarchy with one initial domain, not the exact sequence generated by any named graph-partitioner software. The original method allows other initial partitions, partitioners, and tuning choices which can avoid this particular trap. The bound concerns factor-entry storage only, omitting partition metadata, and does not challenge the source method's NRMSE certificate or assert a failure of its practical numerical experiments. It makes no inference about finite-precision compression. A closely related full specialist manuscript remains an unresolved historical-priority risk; independent mathematical validation has not been performed.

## References

[1] R. Nuca, M. Parsani and L. Dalcin, *Adaptive Local Proper Orthogonal Decomposition via Graph Partitioning and Provable Error-Bounded Lossy Compression for Parametric Series in Finite-Dimensional Function Spaces*, arXiv:2610.31375v1 (first posted 2026-10-22), https://arxiv.org/html/2610.31375v1.

[2] M. Shamrai, *Concatenated Matrix SVD: Compression Bounds, Incremental Approximation, and Error-Constrained Clustering*, arXiv:2601.11626v2 (2026), https://arxiv.org/html/2601.11626v2.

[3] V. Ehrlacher, L. Grigori, D. Lombardi and H. Song, *Adaptive Hierarchical Subtensor Partitioning for Tensor Compression*, SIAM Journal on Scientific Computing (2021), https://doi.org/10.1137/19M128689X (abstract available; complete text unavailable in this review).
