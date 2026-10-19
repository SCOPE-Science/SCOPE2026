# Exact fixed-point and opinion-balance spectrum of strict majority on prism networks

## Finding

Let \(P_n=C_n\square K_2\) be the triangular or larger prism graph, with \(n\ge 3\) and \(2n\) labeled vertices. Under binary synchronous strict-neighbor-majority dynamics, a coloring is *fixed* if every vertex already has the color shared by at least two of its three neighbors. In particular, the fixed states coincide under deterministic and random majority tie-breaking, because all vertices have odd degree.

**Classification.** Every fixed coloring is in exactly one of two classes:

1. The two layer-separated states, in which all \(n\) vertices in one cycle have one color and every vertex in the other cycle has the other color.
2. The column-synchronized states, in which each rung has two vertices of the same color and the associated cyclic binary word of length \(n\) has no isolated letter (all maximal cyclic monochromatic runs have length at least two).

Let \(N_n(m)\) be the number of fixed colorings with exactly \(m\) blue vertices, for \(0\le m\le 2n\). Define, for integers \(1\le k\le n-1\),
\[
B_n(k)=\sum_{r=1}^{\min(\lfloor k/2\rfloor,\lfloor(n-k)/2\rfloor)}
\frac nr\binom{k-r-1}{r-1}\binom{n-k-r-1}{r-1},
\]
with an empty sum interpreted as zero. Then the **complete fixed-point opinion-balance spectrum** is
\[
\boxed{N_n(m)=\mathbf 1_{\{m=0\}}+\mathbf 1_{\{m=2n\}}
+2\mathbf 1_{\{m=n\}}+\sum_{k=1}^{n-1}\mathbf 1_{\{m=2k\}}B_n(k).}
\]
In particular, the total number \(F_n=\sum_{m=0}^{2n}N_n(m)\) is exactly
\[
\boxed{F_n=2+L_n+2\cos(n\pi/3),}
\]
where \(L_n=((1+\sqrt5)/2)^n+((1-\sqrt5)/2)^n\) is the \(n\)-th Lucas number. Thus \(F_n\sim ((1+\sqrt5)/2)^n\), and the exponential fixed-state entropy per vertex is \(\tfrac12\log((1+\sqrt5)/2)\).

The smallest nonzero number of blue vertices in a fixed coloring is \(3\) when \(n=3\), and \(4\) for every \(n\ge4\). For \(n\ge5\), exactly \(n\) fixed colorings contain precisely four blue vertices.

## Assumptions and scope

The graph is simple, undirected, unweighted, and has vertex set \(\{(i,a):i\in\mathbb Z/n\mathbb Z,\ a\in\{0,1\}\}\). The neighbors of \((i,a)\) are \((i-1,a)\), \((i+1,a)\), and \((i,1-a)\). The two allowed opinions are labelled blue and white; vertices are individually labelled, rather than counted modulo rotation or color exchange. A fixed coloring is an absorbing singleton state under synchronous majority with arbitrary tie handling, which is irrelevant on these degree-three graphs. No assertion is made about attraction basins or the probability of reaching any fixed state from random initial conditions.

## Proof

**1. A mismatched rung forces global layer separation.** Suppose at least one column \(i\) has different colors at its two endpoints, say blue on the upper cycle and white on the lower. The vertical neighbor of either endpoint is opposite, so that vertex needs *both* horizontal neighbors to have its own color to satisfy strict majority among three neighbors. Hence columns \(i-1\) and \(i+1\) must have the same ordered blue-white pattern as column \(i\). Iteration around the connected cycle forces the same ordered pattern on every column. Conversely, either global layer-separated configuration is fixed, since each vertex has its two horizontal neighbors of the same color. There are exactly two of these configurations.

**2. All remaining fixed states have non-isolated synchronized runs.** If no rung is mismatched, both endpoints of column \(i\) have a common opinion \(x_i\). Each endpoint has one same-colored vertical neighbor. It retains its color under strict majority precisely when at least one of the two horizontal neighbors has opinion \(x_i\). This fails precisely when \(x_{i-1}=x_{i+1}\ne x_i\). Accordingly, synchronized fixed states correspond bijectively to labeled cyclic binary words without singleton monochromatic runs.

**3. Exact counts by opinion balance.** Consider such a cyclic word with \(k\) blue columns and \(n-k\) white columns, both positive. It has \(r\) alternating blue runs and \(r\) white runs, each of length at least two, so \(1\le r\le\min(\lfloor k/2\rfloor,\lfloor(n-k)/2\rfloor)\). The blue run lengths are a composition of \(k\) into \(r\) parts at least two, of which there are \(\binom{k-r-1}{r-1}\); independently the white lengths have \(\binom{n-k-r-1}{r-1}\) choices. Designate the starting column of one blue run: there are \(n\) choices for its labeled location. Each resulting labeled cyclic word is thereby counted exactly \(r\) times, once per blue-run start, giving the formula for \(B_n(k)\). The all-white and all-blue synchronized words contribute one each. Synchronized words with \(k\) blue columns have exactly \(2k\) blue vertices, while each of the two layer-separated states has exactly \(n\) blue vertices. Combining these disjoint classes proves the displayed spectrum.

**4. Closed total count.** For a synchronized cyclic word, mark the cycle edge between columns \(i\) and \(i+1\) exactly when the colors differ. The marked edges have no common endpoints, because singleton runs are forbidden, and their total number is even, because color switches around a cycle have even parity. Conversely, an even-cardinality matching of cycle edges and a choice of initial column color determine one synchronized fixed coloring; the opposite initial color gives the other. Let \(I(C_n,z)\) be the matching generating polynomial of cycle *edge* sets, equivalently the independence polynomial of the line graph \(C_n\), again a cycle. The number of synchronized fixed states is
\[
2\sum_{r\ \mathrm{even}}[z^r]I(C_n,z)=I(C_n,1)+I(C_n,-1).
\]
Using the elementary two-state transfer matrix \(T_z=\begin{pmatrix}1&z\\1&0\end{pmatrix}\), one has \(I(C_n,z)=\operatorname{tr}(T_z^n)\) for every \(n\ge3\). The eigenvalues of \(T_z\) solve \(\lambda^2-\lambda-z=0\). At \(z=1\) their powers sum to the Lucas number \(L_n\); at \(z=-1\) they are \(e^{\pm i\pi/3}\), whose powers sum to \(2\cos(n\pi/3)\). Adding the two layer-separated states gives the total formula. The second characteristic root at \(z=1\) has modulus less than one, and the cosine correction is bounded, proving the asymptotic.

**5. Sharp smallest persistent color group.** A synchronized nonmonochromatic coloring must contain at least two consecutive blue columns, hence at least four blue vertices. A layer-separated coloring has exactly \(n\) blue vertices. Therefore the smallest positive blue count is \(\min(4,n)\), attained by the separated states for \(n=3\) and by two adjacent blue columns for every \(n\ge4\). When \(n\ge5\), every fixed coloring with four blue vertices must have a single pair of adjacent blue columns, since layer separation has \(n\ne4\) blue vertices; the pair can start at any of the \(n\) labeled columns.

## Verification

A standalone Python 3 program, `verification.py`, independently enumerates all \(2^{2n}\) binary configurations for each \(3\le n\le9\), directly tests strict-majority inequalities at all vertices, and compares the complete blue-count histogram with the run-composition formula and Lucas/cosine total. It also compares the two exact formulas for every \(3\le n\le200\). Running `python3 verification.py` passed \(40688\) formula comparisons, including exhaustive finite-state enumerations. These computational checks are supplemental; the proof above applies to all integer \(n\ge3\).

## Relationship to prior work

Zehmakan (2023; journal version 2024) proves that random majority dynamics on a simple cycle has precisely two fixed colorings, whereas deterministic majority with keep-your-color ties has exponentially many; Theorem 2.8 analyzes no-isolated-color words on the cycle and its appendix describes a doubling construction that preserves synchronized majority trajectories. The current result instead classifies **all** fixed states of the distinct, cubic, vertex-transitive prism, including ruling out partially mismatched rungs, and determines their exact total and blue-opinion composition counts. The previous cycle analysis supplies a natural comparative motivation but does not state these prism-specific conclusions.

Arkhipov (2024) identifies fixed majority states on odd-regular graphs with internal partitions and studies random-regular trajectories experimentally; the prism fixed-state and opinion-balance enumerations are not among its results. The new result can equivalently be read as an exact count, by side sizes, of internal partitions of cubic prism graphs. The underlying finite-state transfer and run-composition methods are classical; originality is asserted only for their prism-specific classification and exact spectrum, subject to literature-priority limitations.

## Limitations

The theorem concerns only *fixed* states, not period-two configurations, probability of convergence, finite-time stabilization, noisy update rules, or nonuniform edge weights. Counts distinguish labeled individuals and distinguish both colors. General statements about arbitrary cubic vertex-transitive networks do not follow. The equivalence to internal cuts and the cycle no-isolated-run characterization are prior knowledge. A logically equivalent enumeration in the broader literature on Ising metastability, internal partitions or binary cellular automata cannot be excluded by the inspected searches; independent literature and proof review remain outstanding.

## References

1. A. N. Zehmakan, “Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes,” arXiv:2302.06760v1 (first public 14 February 2023), and *AAMAS 2023*. Full text: https://arxiv.org/abs/2302.06760 . Cycle stable-coloring theorem, stable-state experiments, Appendix A.
2. A. N. Zehmakan, “Majority opinion diffusion: when tie-breaking rule matters,” *Autonomous Agents and Multi-Agent Systems* **38**, article 21 (20 May 2024), DOI: 10.1007/s10458-024-09651-y. Journal full text: https://link.springer.com/article/10.1007/s10458-024-09651-y . Theorems 2.7–2.8, Sections 5.3 and 6, Appendix.
3. P. Arkhipov, “Majority Dynamics and Internal Partitions of Random Regular Graphs: Experimental Results,” arXiv:2406.07026v1 (11 June 2024). Public full text: https://arxiv.org/html/2406.07026v1 . Sections 1 and 3.
