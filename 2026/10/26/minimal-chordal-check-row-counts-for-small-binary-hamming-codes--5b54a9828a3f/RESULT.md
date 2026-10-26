# Minimal chordal check-row counts for small binary Hamming codes

## Finding
For every integer \(r\ge3\), let \(H_r\) be the binary \(r\times(2^r-1)\) parity-check matrix whose columns are all nonzero vectors of \(\mathbb F_2^r\). For any binary parity-check matrix \(A\) with exactly this row space, define its **column primal graph** to have one vertex per code coordinate and an edge between distinct vertices if their columns in \(A\) have a common row containing two ones. Let \(h(r)\) be the minimum number of rows among such matrices whose column primal graph is chordal. Redundant parity-check rows are permitted and counted; matrices must have rank \(r\).

Then
\[
h(3)=3,\quad h(4)=5,\quad h(5)=7,\quad h(6)=9.
\]
In addition, for all larger redundancies the sharp-at-the-base universal lower bounds are
\[
h(r)\ge r+1\quad(r\ge4),\qquad
h(r)\ge r+2\quad(r\ge5),\qquad
h(r)\ge r+3\quad(r\ge6).
\]
Thus a minimum-rank representation of the classical binary Hamming code cannot have chordal primal graph once the redundancy reaches four, and the least extra-row expense is exactly one, two, or three in redundancies four, five, and six, respectively.

## Assumptions and scope
The field is exactly \(\mathbb F_2\); the \(2^r-1\) columns are distinct and nonzero. All parity-check matrices considered define precisely the same code, have row rank \(r\), and may contain dependent or repeated check rows (but no repeated rows are needed by minimizers). A chordal graph has no induced cycle of length at least four. The primal graph is on **variables/columns**, not the bipartite Tanner graph and not a graph on check rows. Row count refers to equations, not the code redundancy \(r\).

## Proof
**Canonical form.** Pick \(r\) independent check rows of any candidate \(A\). Since the columns of \(H_r\) list all nonzero vectors, replacing these rows by the standard coordinate basis merely permutes columns via an invertible linear map on \(\mathbb F_2^r\). Every remaining row is a linear functional \(f\in\mathbb F_2^r\). Therefore, for \(t\) added rows, every possible column primal graph is, up to coordinate permutation, the graph obtained from the standard \(r\) basis rows plus \(t\) arbitrary functionals. If a zero or duplicate functional is included, removing it leaves the same graph; hence all cases with \(t\le2\) are covered by enumerating nonzero distinct functionals in the certificate.

**Unaugmented obstruction.** For \(r\ge4\), the four column labels \(e_1+e_2\), \(e_2+e_3\), \(e_3+e_4\), and \(e_4+e_1\) form an induced four-cycle under the standard basis checks: successive supports intersect and opposite supports do not. Thus \(h(r)>r\) for every \(r\ge4\).

**Exact finite obstructions.** In dimension five, the complete set of \(31\) nonzero candidate extra functionals is checked and every resulting graph is nonchordal. In dimension six, all \(63\) choices of one extra functional and all \(\binom{63}{2}=1953\) unordered pairs are checked, and every resulting graph is nonchordal. The supplied standard-library `check.py` constructs each adjacency relation by exact bit parity and tests chordality by maximum cardinality search with an explicit perfect-elimination-order verification. Its exhaustive loops establish the lower bounds for dimensions five and six; they are finite exhaustive proofs, not extrapolation from sampled graphs. By restricting the induced graph to the \(2^s-1\) columns supported in any fixed set of \(s\) basis coordinates, an \(r\)-dimensional candidate with at most \(t\) extra rows contains an \(s\)-dimensional candidate with at most \(t\) extra rows as an induced subgraph. Since chordality is inherited by induced subgraphs, the dimension-five and dimension-six obstructions extend respectively to every \(r\ge5\) and \(r\ge6\).

**Matching constructions.** Partition the \(r\) basis coordinates into groups of size one or two. For each two-coordinate group \(\{i,j\}\), append one additional check \(e_i+e_j\); keep standard checks for all coordinates. Within each group, two nonzero column projections always share a check containing two ones: the three functionals \(e_i,e_j,e_i+e_j\) cover all pairs of nonzero projections in \(\mathbb F_2^2\). Therefore two columns are adjacent exactly when their sets of nonzero coordinate groups intersect. For \(r=3,4,5,6\), choose respectively \(3,3,3,3\) or fewer groups, for instance groups \((1)(2)(3)\), \((12)(3)(4)\), \((12)(34)(5)\), \((12)(34)(56)\). The graph of intersecting nonempty subsets of a three-element set is chordal: eliminate its three singleton vertices, whose remaining neighborhoods are cliques; the remaining doubletons and the tripleton form a clique. Replacing each subset vertex by a clique of true twins preserves chordality. Hence the constructed primal graphs are chordal with exactly \(r\), \(r+1\), \(r+2\), \(r+3\) rows respectively. This matches the lower bounds and proves every stated equality.

## Verification
Run `python3 check.py` using Python 3.8 or later; expected terminal line: `VERIFY_OK`. The program checks the explicit constructions, the unaugmented obstruction, all \(31\) dimension-five one-row cases, all \(63\) dimension-six one-row cases, and all \(1953\) dimension-six distinct two-row cases. `check_output.txt` contains the actual output from a fresh run. Chordality testing uses maximum cardinality search and verifies the resulting perfect elimination ordering; correctness of this characterization is a standard finite-graph theorem [2]. The analytical canonical-representation and induced-subgraph arguments extend finite tests to the infinite lower-bound ranges.

## Relationship to prior work
The 2026 introduction of chordal parity-check representations [1] motivates minimizing the number of redundant equations needed to make a fixed classical code's primal graph chordal. The result here is an exact representation-cost theorem specifically for classical binary Hamming codes; it is not an improvement to the Gaussian-elimination complexity bounds of [1]. Maximum cardinality search and the chordality test are established algorithms [2], not new algorithms claimed here.

## Limitations
The formula for \(h(r)\) is determined only through \(r=6\); the universal inequalities for larger \(r\) need not be tight. The cost model counts rows and does not optimize row weights, decoding operations, or average complexity. The result does not assert that every redundant-check representation is chordal; adding rows can also destroy chordality. The relevant 2026 source [1] was available at abstract level, but its full text could not be inspected, leaving a residual risk that it contains related examples or a stronger equivalent classification.

## References
[1] Y. Chen, L. Guo, T. Li, and M. Zhu, *Chordal Codes: Code Construction and Efficient Gaussian-Elimination Decoding*, arXiv:2610.17934, first submitted 2026-10-13, https://arxiv.org/abs/2610.17934.

[2] R. E. Tarjan and M. Yannakakis, *Simple Linear-Time Algorithms to Test Chordality of Graphs, Test Acyclicity of Hypergraphs, and Selectively Reduce Acyclic Hypergraphs*, SIAM Journal on Computing 13 (1984), 566–579, https://doi.org/10.1137/0213035.
