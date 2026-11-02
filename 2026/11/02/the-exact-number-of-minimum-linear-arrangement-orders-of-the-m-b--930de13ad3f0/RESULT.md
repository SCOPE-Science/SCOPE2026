# The exact number of minimum-linear-arrangement orders of the Möbius ladder

## Finding

For every integer \(n\ge4\), the cubic Möbius ladder \(M_{2n}\) has **exactly** \(n4^n\) minimum-linear-arrangement vertex orders, with all \(2n\) vertices individually distinguished. The minimum value is \(9n-8\). Every optimal order simultaneously realizes the smallest possible edge boundary at **every** prefix size.

Moreover, all optimal orders admit a complete structural characterization: the first four vertices form a square on two adjacent antipodal pairs; their even prefixes at all intermediate sizes \(4,6,\ldots,2n-4\) are consecutive blocks of whole antipodal pairs; and the last four vertices form the square complementary to the last such block. Within each initial and terminal square, the constrained internal order has sixteen choices; each intermediate two-vertex extension has four choices. Thus the number is \(n\cdot16\cdot4^{n-4}\cdot16=n4^n\).

The minimum edge-boundary numbers and the width-five construction are treated as known background, not as independent novelties [1]. The new assertion is the complete classification and **multiplicity** of all orders optimizing total edge length, rather than a single layout or its optimal objective value.

## Assumptions and scope

Write \(V=\mathbb Z/(2n)\), with distinct vertices represented by \(0,1,\ldots,2n-1\). The undirected edge set consists of the \(2n\) cycle edges \(\{i,i+1\}\), indices modulo \(2n\), together with the \(n\) antipodal edges \(\{i,i+n\}\), for \(0\le i<n\). Here \(n\ge4\) is arbitrary; the six-vertex degenerate boundary case is excluded. A layout is a bijection \(\pi:V\longrightarrow\{1,\ldots,2n\}\), without identifying dihedral symmetries or reverse orders. The objective is \(\operatorname{LA}(\pi)=\sum_{uv\in E}|\pi(u)-\pi(v)|\).

For \(S\subseteq V\), let \(b(S)\) be its edge boundary size. If \(S_k=\{v:\pi(v)\le k\}\), then \(\operatorname{LA}(\pi)=\sum_{k=1}^{2n-1}b(S_k)\). A *rung column* is one antipodal pair \(\{i,i+n\}\), identified with \(i\in\mathbb Z/n\). A block of consecutive rung columns is a cyclic interval in \(\mathbb Z/n\), taken with both vertices of each column.

## Proof

**1. A cut identity and extremizers.** For a nonempty proper \(S\subset V\), let \(r(S)\) be the number of circular runs of vertices of \(S\) on the Hamiltonian \(2n\)-cycle, and let \(u(S)\) count antipodal edges with exactly one endpoint in \(S\). Then
\[
b(S)=2r(S)+u(S).
\]
Each cycle run contributes precisely two escaping cycle edges; the remaining boundary edges are exactly the \(u(S)\) antipodal rungs.

If \(r(S)=1\), then \(S\) is a cyclic interval of size \(k\) and \(u(S)=\min(k,2n-k)\): for \(k\le n\), every member's antipode lies outside; for \(k\ge n\), the same reasoning applies to its complementary interval. If \(r(S)\ge3\), then \(b(S)\ge6\). If \(r(S)=2\), the boundary is at least four; equality holds exactly when \(u(S)=0\), i.e. \(S\) is a union of complete antipodal pairs. Such an invariant \(S\) has two cycle runs if and only if its selected columns form a single proper cyclic interval in \(\mathbb Z/n\). Consequently, **for every even size \(k\) with \(4\le k\le2n-4\)**, the sets with boundary four are precisely the consecutive complete-rung blocks.

Because the graph is cubic, \(b(S)=3|S|-2|E(S)|\), so the boundary and \(|S|\) have the same parity. The preceding run arguments and their complements show that the minimum boundary at any size \(1\le k\le2n-1\) is
\[
\beta(k)=\begin{cases}
3,&\min(k,2n-k)=1,\\
4,&k\text{ even},\\
5,&k\text{ odd and }3\le k\le2n-3.
\end{cases}
\]
Indeed, for even \(k\ge4\) consecutive rung blocks give four; for size two an edge gives four; and selecting full consecutive rungs followed by one adjacent vertex gives five at odd sizes. Complementation handles the far end. The paired order \(0,n,1,n+1,\ldots,n-1,2n-1\) realizes every value \(\beta(k)\). Its sum is \(9n-8\), and no layout can be shorter, since each prefix contributes at least its size-constrained minimum. Moreover, equality of the total sum occurs **if and only if** every prefix has boundary \(\beta(k)\).

**2. Initial four vertices.** Every minimizing layout has \(b(S_4)=4\), hence by the equality classification \(S_4\) comprises two consecutive rung columns. There are exactly \(n\) choices of this square. An optimal initial two-prefix must have boundary four; within the square this means the first two vertices form one of its four edges, with either orientation (eight choices). Either of the remaining two vertices can be third: each three-vertex subset of this square has boundary five (the complement of a corner in the induced four-cycle is a length-two path). Therefore there are exactly \(4\cdot2\cdot2=16\) possible internal orders of the first four.

**3. Interior extensions.** Suppose an optimal prefix of size \(2t\) is a consecutive block of \(t\) complete columns with \(2\le t\le n-3\). To reach an optimal prefix of size \(2t+2\), the next entire column must be the left or right adjacent column: all other full-rung additions would split the column interval and have boundary at least six. These are two choices. The two new vertices can enter in either order, because either single added vertex gives the required odd-prefix boundary five (it has exactly one neighbor in the current block). Thus each two-vertex extension has four choices. Exactly \(n-4\) such extensions bring a four-vertex optimal prefix to size \(2n-4\). When \(n=4\), this stage is empty.

**4. Final four vertices.** The complementary four vertices form two consecutive rung columns, hence induce a square. The boundary at size \(2n-3\) is five regardless of which one of these four vertices enters next. The boundary at size \(2n-2\) is four exactly when the last two unplaced vertices form an edge. To count the final orders, choose the first added vertex in four ways, then choose the second added vertex in exactly two ways that leave an edge, and arrange the remaining two vertices in either order. This yields \(4\cdot2\cdot2=16\) terminal orders. No choices are repeated because the four-vertex prefix and its intermediate blocks are uniquely recoverable from the permutation.

Multiplying the independent stages yields
\[
\#\{\pi:\operatorname{LA}(\pi)=9n-8\}
=n\cdot16\cdot4^{n-4}\cdot16=n4^n.
\]
Each constructed order meets the prefix minima, so this is both a lower and an upper count. This completes the proof for all integers \(n\ge4\).

## Verification

The standalone Python scripts `verify_direct.py` and `verify_structure.py` require only Python 3. Both have been executed after being written. `verify_direct.py` evaluates every edge boundary independently by looping over all edges of every subset and counts all optimum prefix chains by dynamic programming for \(n=4,5,6,7,8,9\). It returns respectively \(1024,5120,24576,114688,524288,2359296\), and minimum objective values \(28,37,46,55,64,73\). `verify_structure.py` uses an independent cycle-run/rung-count formula, checks its equality classification over every proper subset for those same cases, and checks the sixteen initial/final square permutations by independent permutation enumeration. These are finite corroborations; the all-parameter result follows from the argument above.

Run in the directory containing these files:

```sh
python3 verify_direct.py
python3 verify_structure.py
```

## Relationship to prior work

Greeni and Rajasingh [1], in the accessible complete article (especially Lemma 8 and the section on the cutwidth algorithm), give the complete minimum induced-edge counts for each subset size and construct the consecutive-rung ordering proving cutwidth five. Their Lemma 8 also implies the displayed \(\beta(k)\) and hence the minimum sum \(9n-8\), by the standard cut-sum identity; **none of these are asserted to be new**. They do **not** classify all equality subsets at all intermediate sizes or count the number of optimal total-length permutations. The extra equality-set classification is what makes the exact \(n4^n\) count possible.

Rajasingh, Manuel, Arockiaraj and Rajan [2] study edge isoperimetry and embedding for different circulant graphs; their proved construction has consecutive generator sets \(\{1,\ldots,j\}\), not the antipodal generator set \(\{1,n\}\). Cygan and collaborators [3] establish general cutwidth algorithms, not the present optimizer count. McSorley [4] discusses counting structures in Möbius ladders, but the full article was not accessible during this comparison; the generic abstract does not resolve whether any enumeration of optimal layouts appears therein.

## Limitations

The theorem concerns *minimum total edge length* layouts, not all layouts attaining cutwidth five: those optimizer sets need not coincide. Orders are counted with all vertices individually distinguished, without division by graph symmetries. The statement excludes the case \(n=3\). Its originality remains qualified by the unavailable full text of McSorley [4] and potentially unindexed enumerations of graph layouts; database search alone cannot certify priority. The primary literature already supplies the size-wise minimum-cut values and the width-five construction; these facts should not be attributed to this theorem. No independent external audit has been performed.

## References

1. A. Berin Greeni and I. Rajasingh, *Cutwidth of Certain Classes of Circulant Networks*, International Journal of Pure and Applied Mathematics **109** (2016), 81–88, https://acadpubl.eu/jsi/2016-109-si/6/11/11.pdf , doi:10.12732/ijpam.v109i6.11.
2. I. Rajasingh, P. Manuel, M. Arockiaraj and B. Rajan, *Embeddings of Circulant Networks*, Journal of Combinatorial Optimization **26** (2013), 135–151, doi:10.1007/s10878-011-9443-x.
3. M. Cygan, D. Lokshtanov, M. Pilipczuk, M. Pilipczuk and S. Saurabh, *On Cutwidth Parameterized by Vertex Cover*, Algorithmica **68** (2014), 940–953; publicly posted November 8, 2012, doi:10.1007/s00453-012-9707-6.
4. J. P. McSorley, *Counting Structures in the Möbius Ladder*, Discrete Mathematics **184** (1998), 137–164, doi:10.1016/S0012-365X(97)00086-1.
