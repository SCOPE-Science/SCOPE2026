# Threshold-partition enumerators and the odd-cycle obstruction at maximum degree two

## Finding

For every finite, nonempty, simple graph \(G\) of maximum degree at most two, let \(W_2(G)\) be the number of maps \(f:V(G)\to\{1,2\}\) for which each color class induces a **threshold graph**. Empty classes are permitted. Let \(\tau(G)\) be the minimum number of nonempty induced-threshold classes partitioning \(V(G)\).

There is an explicit four-state formula for \(W_2(G)\) in terms of the connected path and cycle components of \(G\). Use the truncated commutative ring \(R=\mathbb Z[x,y]/(x^2,y^2)\); for \(Q\in R\), write \(\Sigma Q\) for the sum of its four coefficients in the basis \(1,x,y,xy\). Associate to a connected component \(H\) the following polynomial:

\[
F_{P_n}(x,y)=\begin{cases}
2,&n=1,\\
2+x+y,&n=2,\\
2+(2n-3)(x+y)+2(n-3)^2xy,&n\ge3,
\end{cases}
\]

and

\[
F_{C_n}(x,y)=\begin{cases}
4(x+y),&n=3,\\
2\mathbf 1_{\{2\mid n\}}+n(x+y)+n(n-3)xy,&n\ge4.
\end{cases}
\]

Then, with multiplicities when components are isomorphic,

\[
\boxed{W_2(G)=\Sigma\left(\prod_{H\text{ a component of }G}F_H(x,y)\right),\quad\text{product taken in }R.}
\]

In particular, for the individual path and cycle families,

\[
W_2(P_n)=2n^2-8n+14\quad(n\ge3),
\]
\[
W_2(C_3)=8,\qquad W_2(C_n)=n(n-1)+2\mathbf1_{\{2\mid n\}}\quad(n\ge4).
\]

Let \(o(G)\) be the number of odd-cycle components (triangles included). The exact threshold-partition chromatic number is

\[
\boxed{\tau(G)=\begin{cases}
1,&G\text{ itself is threshold},\\
3,&o(G)\ge3,\\
2,&\text{otherwise}.
\end{cases}}
\]

For this graph class, \(G\) itself is threshold precisely when it has at most one component containing an edge, that component being \(P_2\), \(P_3\), or \(C_3\); the edgeless case is also allowed. Thus both quantities are computable from the list of components using \(O(|V(G)|)\) component-level arithmetic operations; this is not a claim of linear bit complexity for the potentially large integer output.

Equivalently, by assigning red to edges and blue to nonedges of the complete graph on \(V(G)\), these are the exact two-named-color acyclic alternating colorings and the alternating chromatic number for this restricted complete two-edge-colored family.

## Assumptions and scope

All graphs are finite, nonempty, undirected and simple; \(\Delta(G)\le2\). Each component is a path \(P_n\), \(n\ge1\), or a cycle \(C_n\), \(n\ge3\), with specified (distinguishable) vertices. A threshold graph is equivalently a graph with no induced \(P_4\), \(C_4\), or \(2K_2\). A color class may be empty when counting maps into the named palette \(\{1,2\}\); the invariant \(\tau(G)\) instead counts only nonempty classes. If one elects to include the empty graph, its natural separate conventions are \(W_2(\varnothing)=1\) and \(\tau(\varnothing)=0\).

The four polynomial terms record, respectively, whether colors \(1\) and \(2\) induce zero or one connected component containing an edge **inside the original connected component**. The equations \(x^2=y^2=0\) discard assignments in which a given named color has edge-containing components in two different connected components of \(G\). No probability or independence assumption is used.

## Proof

**1. Threshold structure at degree two.** In an induced subgraph of a graph of maximum degree at most two, any connected component with at least four vertices is a path or cycle and contains an induced \(P_4\) or \(C_4\). Two distinct components each containing an edge yield an induced \(2K_2\). Conversely, a graph formed from isolates together with at most one component isomorphic to \(P_2\), \(P_3\), or \(C_3\) contains none of the three forbidden induced subgraphs. Thus these, and only these, are the induced threshold graphs of maximum degree at most two.

For a fixed binary vertex coloring of a path or cycle, the monochromatic connected components are its monochromatic runs (with the sole exceptional case of an entirely monochromatic triangle). Consequently each named color may have at most one run of length two or three; all its other runs must have length one. Call a run of length two or three a *defect*, since it creates the unique edge-containing component of that color. An entirely monochromatic triangle counts as one defect; an entirely monochromatic cycle of length at least four is invalid.

**2. Paths.** There are exactly two defect-free binary words of each positive path length: the two alternating words. If exactly color \(1\) has a defect, its one long run has length two or three, while all other runs have length one. The number with length two is \(n-1\); the number with length three is \(n-2\), interpreting a negative count as zero. Therefore the coefficient of \(x\), and symmetrically of \(y\), is \(2n-3\) for \(n\ge2\).

For a word having one defect of each color, take its total number of runs to be \(k\ge2\). For a specified ordered pair of defect lengths, their total excess beyond singleton length is \(d\in\{2,3,4\}\), so \(k=n-d\). Among the two alternating choices for the first run color, the number of ways to choose one run of each color is \(2\lfloor k^2/4\rfloor\). There is one choice of defect-length pair for \(d=2\), two for \(d=3\), and one for \(d=4\). Hence for \(n\ge3\) the coefficient of \(xy\) is

\[
2\left\lfloor\frac{(n-2)^2}{4}\right\rfloor+
4\left\lfloor\frac{(n-3)^2}{4}\right\rfloor+
2\left\lfloor\frac{(n-4)^2}{4}\right\rfloor
=2(n-3)^2.
\]

The cases \(P_1,P_2\) have no way to place two defects and are given separately. This proves the displayed path factors.

**3. Cycles.** For \(n\ge4\), a defect-free cyclic binary word exists exactly when \(n\) is even; the two alternating words give its coefficient \(2\). With one defect of color \(1\) and none of color \(2\), the unique exceptional run has length two when \(n\) is odd and length three when \(n\) is even; choosing its first vertex gives precisely \(n\) words. The same count applies to color \(2\).

For one defect of each color, write \(e_1,e_2\in\{1,2\}\) for their excess lengths over one vertex. There must be \(2k=n-e_1-e_2\ge2\) cyclic runs, \(k\) of each color. For fixed admissible \((e_1,e_2)\), count a boundary among the \(n\) cyclic edges, two possible colors of the subsequent run, and one of the \(k\) runs of each color to be long. Each word is counted at its \(2k\) boundaries, giving \(n\cdot2\cdot k^2/(2k)=nk\) words. For even \(n\ge6\), the admissible excess pairs are \((1,1)\) and \((2,2)\); for \(n=4\), only \((1,1)\) is admissible; for odd \(n\ge5\), the pairs are \((1,2)\) and \((2,1)\). The total in all cases is \(n(n-3)\). The triangle is exceptional: each of its eight binary words has exactly one active defect color, with four choices for which words activate each color. This proves every cycle factor.

**4. Disjoint components.** Every global map has a unique restriction to each component \(H\). By step 1, its color classes are threshold if and only if among these restrictions at most one component has a color-\(1\) defect and at most one has a color-\(2\) defect, and all restrictions are locally valid. Multiplying the factors and imposing \(x^2=y^2=0\) retains exactly these possibilities. Summing their four coefficients counts all admissible maps exactly once and proves the product formula.

**5. Number of classes.** A one-class partition exists exactly when \(G\) itself has the form in step 1. If \(o(G)\ge3\), then every binary map on each odd cycle has a monochromatic edge, since a proper binary coloring of an odd cycle is impossible. The associated defect must be assigned to one of only two colors, so the pigeonhole principle forces some color to have edge-components in at least two disconnected odd cycles. Hence no two-class threshold partition exists. Conversely, if at most two odd-cycle components exist, use a proper alternating binary coloring on every path and even cycle. On each odd cycle choose a binary word having a unique two-vertex monochromatic run (or an allowed two-vertex run on a triangle), placing its defect in a different named color when two odd-cycle components exist. The resulting two classes induce threshold graphs. Finally every graph of maximum degree at most two admits a proper three-coloring, whose independent color classes are threshold. This proves the trichotomy. All constructions are explicit and the component formulas are arithmetically evaluable in a linear number of component operations.

## Verification

The accompanying standalone \(\texttt{verify.py}\) reconstructs paths, cycles, and disjoint unions from their edges, independently enumerates every map into two named colors, and recognizes threshold color classes by searching for all forbidden induced four-vertex graphs \(P_4,C_4,2K_2\). It compares this direct test against the four-coefficient formulas for all paths of orders one through fourteen, all cycles of orders three through fourteen, and 134 disconnected unions up to ten vertices. It also checks the closed individual-family counts through order one thousand and the odd-cycle feasibility rule on selected unions. It returns \(\texttt{VERIFY_OK}\). These finite checks do not prove the all-order statement; steps 1–5 do.

## Relationship to prior work

Bang-Jensen, Bessy and Reinald (arXiv:2610.32954, first publicly posted 2026-10-23, Section 1 and Section 4, Corollary 4.2) establish hardness of partitioning a general graph into two induced threshold graphs and its equivalence to alternating two-edge-color acyclicity. Their paper does not state the present complete degree-two family classification, exact two-color enumeration, or truncated component factorization.

Dorbec, Montassier and Ochem (doi:10.1002/jgt.21724) examine partitioning into cographs and stars; the abstract-level comparison concerns the weaker \(P_4\)-free class, not the simultaneous \(P_4,C_4,2K_2\)-free class or its binary enumeration. Demange, Ekim and de Werra (doi:10.1016/j.ejor.2007.09.018) studied partition-colouring in applications and are cited as earlier hardness work. Only a bibliographic/abstract-level comparison was possible for these two older works. The formula also differs from previously recorded complete-multipartite threshold-class enumerations: paths of order at least four and odd cycles of order at least five lie outside that graph family, and its generating function has a different hypothesis.

## Limitations

This result is restricted to maximum degree at most two and exactly two named classes for the enumeration; it does not count all proper \(k\)-class threshold partitions at arbitrary \(k\) or treat graphs with vertices of degree at least three. Full historical priority cannot be certified from the searches and source access reported here, and independent mathematical review has not occurred. In particular, an equivalent formula under a different coloring vocabulary is a residual bibliographic risk. The proof is combinatorial, not dependent on extrapolating finite outputs.

## References

1. J. Bang-Jensen, S. Bessy and A. Reinald, *Acyclic 2-edge-coloured graphs: polynomial-time linkages and colouring hardness*, arXiv:2610.32954v1 (2026-10-23), https://arxiv.org/html/2610.32954v1.
2. P. Dorbec, M. Montassier and P. Ochem, *Vertex Partitions of Graphs into Cographs and Stars*, Journal of Graph Theory 75 (2014), 75–90, doi:10.1002/jgt.21724.
3. M. Demange, T. Ekim and D. de Werra, *A tutorial on the use of graph coloring for some problems in robotics*, European Journal of Operational Research 192 (2009), 41–55, doi:10.1016/j.ejor.2007.09.018.
