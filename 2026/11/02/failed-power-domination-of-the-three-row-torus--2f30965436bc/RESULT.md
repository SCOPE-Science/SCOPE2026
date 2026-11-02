# Failed power domination of the three-row torus

## Finding
For every integer \(n\ge3\), the Cartesian-product graph \(T_n=C_3\square C_n\) has failed power domination number
\[
\gamma_{\mathrm{fp}}(T_n)=\left\lfloor\frac n2\right\rfloor.
\]
In particular, every set of at least \(\lfloor n/2\rfloor+1\) initial sensors monitors all vertices, regardless of placement, and this threshold is sharp.

## Assumptions and scope
The graph is finite, simple, and undirected. Write vertices as \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\), \(r\in\{0,1,2\}\), where all three vertices with common first coordinate form a triangle, and consecutive first coordinates are joined in corresponding rows. Let \(N[S]\) be the closed neighborhood of a set \(S\) of initially instrumented vertices. Declare \(N[S]\) monitored; subsequently, any monitored vertex with exactly one unmonitored neighbor forces that neighbor to be monitored. A set failing to monitor the entire graph is a failed power dominating set. Its largest possible size is \(\gamma_{\mathrm{fp}}\). The graph \(C_3\square C_3\) is included; no claim for arbitrary \(C_m\square C_n\) with \(m\ge4\) is made.

## Proof
**Column propagation.** Call the three vertices with common index \(i\) column \(i\). A column containing a sensor is wholly monitored immediately, because it is a triangle. If two adjacent columns become wholly monitored, then in the next column every row can be forced by its already monitored counterpart in a full column: that forcing vertex has its two in-column neighbors and its opposite-column neighbor monitored, leaving only the next-rowwise neighbor possibly unmonitored. Induct in both cyclic directions. Therefore, two adjacent complete columns guarantee monitoring of \(T_n\).

**Forced separation.** Put \(w_i=|S\cap(\{i\}\times\{0,1,2\})|\). A column with three sensors completes both neighboring columns in the initial monitoring stage, so no failed set has such a column. Thus all \(w_i\le2\). Two adjacent sensor-bearing columns also give two adjacent complete columns, hence cannot occur in a failed set.

Suppose two sensor-bearing columns occur at cyclic separation \(d\) in one direction, with \(a\) and \(b\) sensors, respectively, where \(1\le a,b\le2\). If \(d<a+b\), then those two columns alone power dominate the graph. There are only three cases. When \(d=1\), they are adjacent. When \(d=2\), one end column has two sensors. The intervening column begins with at least two monitored rows (from that endpoint), and with the row(s) monitored from the other endpoint. If it has three monitored rows, two adjacent columns are full. Otherwise, a row monitored from *both* endpoints exists; its intervening vertex has three monitored neighbors, except for the one missing in-column row, which it forces, completing the intervening column. When \(d=3\), necessarily \(a=b=2\). The two selected pairs of rows intersect, say in row \(r\). The first intervening column has both rows of the first pair monitored, and row \(r\) is monitored in the second intervening column from the far endpoint. Thus the first intervening vertex in row \(r\) has a full neighboring endpoint column, a monitored horizontal neighbor in the next intervening column, and exactly one unmonitored in-column neighbor, which it forces. This makes two adjacent columns full. In each case, all vertices are ultimately monitored. The preceding reasoning still holds if another route around the cycle contributes additional monitored vertices, since adding monitors cannot prevent forcing.

Consequently, if a failed set has \(k\ge2\) occupied columns, list their positions in cyclic order as \(i_1,\ldots,i_k\), with successive clockwise gaps \(d_j>0\). Every gap satisfies
\[
 d_j\ge w_{i_j}+w_{i_{j+1}},\qquad i_{k+1}=i_1.
\]
Summing gaps gives
\[
 n=\sum_{j=1}^k d_j\ge2\sum_{j=1}^k w_{i_j}=2|S|.
\]
For a failed set occupying exactly one column, its weight is at most two. If \(n=3\) and its weight is two, each of the two other columns initially has the same two rows monitored; those other columns are adjacent in \(C_3\). In either one of them, a monitored vertex in a selected row has exactly the missing third row as its sole unmonitored neighbor. It forces this third row, giving two adjacent full columns, hence full observation. Therefore a single-column failed set also satisfies \(n\ge2|S|\) (trivial when \(|S|\le1\), and if \(|S|=2\) we have \(n\ge4\)). The empty set also satisfies the inequality. Hence \(|S|\le\lfloor n/2\rfloor\) for every failed set.

**Sharpness.** Choose one fixed row, say \(r=0\), and place one sensor in columns
\[
 i\in\{0,2,4,\ldots,2\lfloor n/2\rfloor-2\}.
\]
These \(\lfloor n/2\rfloor\) columns are pairwise nonadjacent around the cycle for all \(n\ge3\). Initially, every selected column is fully monitored; every unselected column has precisely its row-zero vertex monitored. This is a proper subset of all vertices. Every monitored row-zero vertex in an unselected column has its two *in-column* neighbors unmonitored, so cannot force. Every monitored vertex in row one or two of a selected column has both its neighboring columns unselected and their corresponding vertices unmonitored, so cannot force. A monitored row-zero vertex in a selected column has all its neighbors already monitored. Thus monitoring stalls immediately and fails. This achieves \(\lfloor n/2\rfloor\), proving the theorem. \(\square\)

## Verification
The standalone C++17 program `verify.cpp` constructs the graph from the definition and independently simulates the closed-neighborhood and unique-neighbor propagation process. It exhaustively checks every subset of all \(3n\) vertices for \(3\le n\le7\), finding maxima \(1,2,2,3,3\) and respectively \(9,18,30,24,63\) maximum failed sets. It tests the explicit stalled construction through \(n=20\), plus small-gap forcing configurations up to \(n=13\). Build using `c++ -std=c++17 -O2 verify.cpp -o verify` and run `./verify`; successful execution ends with `VERIFY_OK`. These finite tests corroborate but do not replace the infinite proof.

## Relationship to prior work
Glasser, Jacob, Lederman, and Radziszowski (2019), Theorem 5.3, determine failed power domination of \(K_k\square P_\ell\), giving \(\lfloor(\ell-1)/2\rfloor\) for \(k=3\). Closing the path into a cycle is not a formal specialization of that theorem; the value differs when \(n\) is even. Byrne, Matthews, Patel, Trivedi, and Winslow (2023), Theorem 5, determine \(\gamma_{\mathrm{fp}}(C_n\square C_n)=n(n-3)\) for \(n\ge4\). Their square-torus case does not include the three-row nonsquare products treated here. Related work on fault-tolerant monitoring of generalized Petersen graphs concerns different graph families. The present theorem addresses one constant-width rectangular torus and provides a cyclic sensor-gap proof.

## Limitations
The result does not classify all maximal failed sets, count them for general \(n\), or determine failed power domination for arbitrary rectangular tori. No assertion of exhaustive literature priority or independent external proof verification is made; an equivalent result in unindexed or other inaccessible literature remains possible. Exhaustive experiments stop at seven columns and do not certify infinite statements by themselves.

## References
1. A. Glasser, B. Jacob, E. Lederman, and S. Radziszowski, *Failed power domination on graphs*, 2019, arXiv:1909.02057, Theorem 5.3. https://arxiv.org/abs/1909.02057
2. I. T. Byrne, G. L. Matthews, N. M. Patel, A. G. Trivedi, and M. A. Winslow, *Failed power domination in grids, cylinders, and tori*, *Involve* 16 (2023), 705–717, doi:10.2140/involve.2023.16.705, Theorem 5. https://personal.math.vt.edu/gmatthews/failed_power_dom.pdf
3. L. Girish and K. Somasundaram, *Bound for the k-Fault-Tolerant Power-Domination Number*, *Symmetry* 16 (2024), 781, doi:10.3390/sym16070781. https://www.mdpi.com/2073-8994/16/7/781
