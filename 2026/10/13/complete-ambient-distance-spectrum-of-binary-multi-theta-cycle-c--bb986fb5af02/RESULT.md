# Complete ambient-distance spectrum of binary multi-theta cycle codes

## Finding
Let \(r=2c\ge4\) and \(\ell\ge2\) be integers. The binary cycle code \(C_{r,\ell}\) of the graph consisting of \(r\) internally disjoint paths of length \(\ell\) with common endpoints has length \(r\ell\), dimension \(r-1\), and minimum distance \(2\ell\). Define its *ambient distance polynomial* by
\[
F_{r,\ell}(z)=\sum_{x\in\mathbb F_2^{r\ell}} z^{d(x,C_{r,\ell})},\qquad d(x,C)=\min_{y\in C} d_H(x,y).
\]
The following are closed formulas for every coefficient, at every permitted \(r\) and \(\ell\).

If \(\ell=2s\), put
\[
U_t(z)=2\sum_{d=t}^{s}\binom{2s}{s-d}z^{s-d}\quad(1\le t\le s),\qquad U_{s+1}(z)=0,
\]
\[
B(z)=\binom{2s}{s}z^s+U_1(z).
\]
Then
\[
\boxed{F_{r,2s}(z)=B(z)^r-\frac{U_1(z)^r}{2}+\frac12\sum_{t=1}^{s}z^{2t}\big(U_t(z)^r-U_{t+1}(z)^r\big).}
\]
If \(\ell=2s+1\), put
\[
U_t(z)=2\sum_{d=t}^{s}\binom{2s+1}{s-d}z^{s-d}\quad(0\le t\le s),\qquad U_{s+1}(z)=0.
\]
Then
\[
\boxed{F_{r,2s+1}(z)=\frac{U_0(z)^r}{2}+\frac12\sum_{t=0}^{s}z^{2t+1}\big(U_t(z)^r-U_{t+1}(z)^r\big).}
\]
The fractions combine to integers. The covering radius and exact number of ambient vectors at covering radius (deep holes) are
\[
\begin{array}{c|c|c}
\text{path length}&\text{covering radius}&\text{number of deep holes}\\\hline
2s&rs&\binom{2s}{s}^{r}\\
2s+1&rs+1&2^{r-1}\binom{2s+1}{s}^{r}.
\end{array}
\]
Every deep hole has exactly \(2^{r-1}\) nearest codewords in the even-length case and exactly \(r\) nearest codewords in the odd-length case.

## Assumptions and scope
All graphs are finite, undirected and loopless. The paths have disjoint internal vertices and share only their two endpoints; coordinates are the edges, ordered path by path. All codes and Hamming distances are binary. The \(r\) paths must be an even number, as in the two-isomorphic-book-graph construction; the counting formulas themselves also work for integers \(r\ge3\) without the even restriction. The family agrees, up to coordinate ordering, with the binary codes obtained by a matroid \(2\)-sum of two book graphs along their common book edge: \(r=2c\), \(\ell=n-1\). The four instances identified in the cited construction are \((r,\ell)=(4,2),(6,2),(4,3),(4,4)\).

The code is the repeated single-parity-check code
\[
C_{r,\ell}=\big\{(a_1\mathbf 1_\ell,\ldots,a_r\mathbf 1_\ell):a_i\in\mathbb F_2,\ \textstyle\sum_i a_i=0\big\},
\]
where \(\mathbf 1_\ell\) is the all-ones block. This is an explicit equivalence, not a claim of a previously unknown code construction.

## Proof
At an internal vertex of any path the binary edge-incidence parity equation makes its two incident edges equal. Consequently a cycle-space word is constant on each path. The two common endpoints impose precisely \(\sum_i a_i=0\), giving the stated code, dimension, and minimum distance (at least two complete paths must be selected).

For an ambient word \(x\), let \(w_i\) be the number of ones in its \(i\)-th block. A choice \(a_i\in\{0,1\}\) contributes \(w_i\) errors when \(a_i=0\), or \(\ell-w_i\) when \(a_i=1\). When \(w_i\ne\ell/2\), choose the unique cheaper bit (the *majority bit*) as a baseline. When \(w_i=\ell/2\), either choice ties. The unconstrained minimum distance is \(\sum_i\min(w_i,\ell-w_i)\). If a tie occurs, the overall even-parity condition can be met without increasing the distance. If no tie occurs and the baseline majority bits have odd parity, one must flip an odd number of them; the cheapest way is a single flip with least cost \(\min_i|\ell-2w_i|\). For even baseline parity the unconstrained minimum is already attainable.

Suppose \(\ell=2s\). Each non-tied block has a uniquely determined majority bit, deviation \(d=|w_i-s|\in\{1,\ldots,s\}\), minimum block cost \(s-d\), and multiplicity \(\binom{2s}{s-d}\) for each majority-bit value. The tied blocks have weight \(s\), multiplicity \(\binom{2s}{s}\), and no parity penalty. Thus \(B(z)^r\) counts all unconstrained minimum-cost baselines. The all-non-tie subcollection is \(U_1(z)^r\); exactly half of its words have odd majority parity, because complementing the first block interchanges the parities without changing its deviation. The subcollection whose minimum deviation is exactly \(t\) has polynomial \(U_t(z)^r-U_{t+1}(z)^r\). Add the correction \(2t\) to its odd-parity half to obtain the first boxed identity.

Suppose \(\ell=2s+1\). No block ties. Its deviation parameter \(d\in\{0,\ldots,s\}\) gives minority cost \(s-d\), majority-bit flip cost \(2d+1\), and multiplicity \(\binom{2s+1}{s-d}\) for either majority-bit value. Exactly half of ambient words at each deviation tuple have odd majority parity. The minimum deviation is exactly \(t\) on the difference \(U_t(z)^r-U_{t+1}(z)^r\), proving the second boxed identity.

For even \(\ell\), the distance is never more than \(rs\), since \(s\) is the maximum minority cost. An all-tie ambient word has distance exactly \(rs\). If any block is non-tied and another is tied, its baseline cost is already strictly below \(rs\). If no blocks tie and the smallest deviation is \(t\ge1\), the distance is at most \(rs-rt+2t<rs\) since \(r\ge4\). Hence the deep holes are precisely the \(\binom{2s}{s}^r\) all-tie words, each having exactly \(2^{r-1}\) even-parity closest block assignments.

For odd \(\ell\), an odd-majority ambient word with deviation zero in every block has distance \(rs+1\). If any deviation is positive while the minimum is zero, the distance drops; if the minimum deviation is \(t\ge1\), distance is at most \(rs-rt+2t+1<rs+1\). Even-majority words have distance at most \(rs\). Thus precisely the odd-parity all-zero-deviation words are deepest; they number \(2^{r-1}\binom{2s+1}{s}^r\). Exactly one majority assignment must be flipped to achieve parity with minimum added cost \(1\), and there are \(r\) choices. This proves both the radius and nearest-codeword multiplicity assertions.

## Verification
The standalone pure-Python script `verify.py` constructs the actual graph and independently enumerates its binary incidence-kernel codewords. It then enumerates ambient words and directly computes distances to the codewords, without invoking the displayed formulas to obtain the observed distributions. It checks all ambient vectors for \((r,\ell)=(4,2),(6,2),(4,3),(4,4),(4,5)\), including the number of nearest codewords of every deep hole. The output ends with `VERIFY_OK` when all assertions succeed. It also checks polynomial total mass, zero-shell size and deep-hole leading coefficients for five larger pairs. These computations test finite instances; the displayed argument, not enumeration, proves the formulas for all parameters.

For the four named code instances, the observed pairs (radius, number of deep holes) are \((4,16)\), \((6,64)\), \((5,648)\), and \((8,1296)\), respectively.

## Relationship to prior work
Barbosa, Marquezino and La Guardia (arXiv:2610.04617v1, 3 October 2026, Section 3.2) construct the code family by two-summing book graphs, prove the parameters and present four examples. The code construction and those parameters are not new here. Solé and Zaslavsky (1993) study covering radii of graph cycle codes using minimum \(T\)-joins, and Ribeiro and Cardell (arXiv:2608.26457, 2026) study ordinary weight distributions and generalized support weights of single-parity-check *product* codes. The result above concerns the distribution of the **distance of every ambient word** to this particular repeated parity code, with exact extreme-shell multiplicities and nearest-codeword ties; ordinary codeword weight enumerators do not determine this distribution in general. The closest older cycle-code article was available here only through its abstract; equivalent statements hidden in its full text or other literature remain a novelty risk.

## Limitations
The theorem is binary and covers equal-length parallel paths; it does not address arbitrary graph cycle codes, unequal path lengths, or quantum CSS distances. It is a self-review, not an independent audit. The existence of earlier equivalent formulations of some or all of the ambient spectrum has not been ruled out by database searches. No independent literature priority or machine proof is asserted.

## References
1. A. S. Barbosa, F. de L. Marquezino, G. G. La Guardia, *New Methods for Constructing Classical and Quantum Codes from Graphs and Matroids*, arXiv:2610.04617v1 (first posted 2026-10-03), Section 3.2, https://arxiv.org/html/2610.04617v1.
2. P. Solé and T. Zaslavsky, *The covering radius of the cycle code of a graph*, Discrete Applied Mathematics **45** (1993), 63–70, DOI:10.1016/0166-218X(93)90140-J.
3. M. M. A. Ribeiro and S. D. Cardell, *Weight Distributions of Single Parity-Check Product Codes via Character Sums*, arXiv:2608.26457 (first posted 2026-08-26).
