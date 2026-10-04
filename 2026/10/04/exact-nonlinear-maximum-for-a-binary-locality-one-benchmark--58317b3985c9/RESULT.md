# Exact nonlinear maximum for a binary locality-one benchmark
## Finding
Let \(M_{\max}(2,9,3,1,2)\) be the maximum size of a binary code \(C\subseteq\mathbb F_2^9\) with global minimum Hamming distance at least \(3\) and all-symbol \((1,2)\)-locality in the following local-distance sense: for each coordinate \(i\), there is one helper coordinate \(j\ne i\) such that the projection \(C|_{\{i,j\}}\) has minimum distance at least \(2\). Then
\[
M_{\max}(2,9,3,1,2)=8.
\]
Thus the eight-word construction reported for this parameter is already optimal even when nonlinear codes are allowed.

## Assumptions and scope
The alphabet is \(\mathbb F_2\). Hamming distance is used globally and on every selected recovery view. A projected code with fewer than two distinct words is assigned minimum distance \(0\), matching the convention in the motivating definition. No linearity, disjoint-repair-group assumption, or a priori partition of the coordinates is assumed.

## Proof
An explicit code of size \(8\) is
\[
C_0=\{(a,a,b,b,c,c,d,d,d):a,b,d\in\mathbb F_2,\ c=a+b\}.
\]
Within each of the coordinate classes \(\{1,2\}\), \(\{3,4\}\), \(\{5,6\}\), and \(\{7,8,9\}\), any coordinate can use another coordinate in the same class as its helper. Each such two-coordinate projection is \(\{00,11\}\), so its minimum distance is \(2\). If two codewords differ only in \(d\), their distance is \(3\); if \(d\) is unchanged, the parity condition on \((a,b,c)\) forces at least two of those three class bits to change, contributing distance at least \(4\). Hence \(d(C_0)=3\), proving \(M_{\max}(2,9,3,1,2)\ge8\).

For the upper bound, it is enough to consider a code \(C\) with at least two words. For each coordinate \(i\), locality supplies a helper \(j\) such that \(C|_{\{i,j\}}\) has minimum distance at least \(2\). Over the binary alphabet, any set of at least two length-two words with minimum distance \(2\) is contained in either \(\{00,11\}\) or \(\{01,10\}\). Therefore there is a constant \(\varepsilon_{ij}\in\mathbb F_2\) such that
\[
x_j=x_i+\varepsilon_{ij}\qquad\text{for every }x\in C.
\]
Define coordinates \(i\sim j\) when their coordinate functions on \(C\) differ by a fixed binary constant. This is an equivalence relation. The locality condition shows that every equivalence class has size at least \(2\). Moreover, no coordinate is constant on \(C\): if \(x_i\) were constant, then a two-coordinate projection containing \(i\) could not have two distinct words at distance \(2\).

Choose one representative from each equivalence class. If the class sizes are \(w_1,\ldots,w_m\), then \(w_s\ge2\), \(\sum_s w_s=9\), and the representative map embeds \(C\) into \(\mathbb F_2^m\). For two codewords, their original Hamming distance is exactly the weighted Hamming distance
\[
d_w(u,v)=\sum_{s:u_s\ne v_s}w_s.
\]
Thus \(m\le4\). If \(m\le3\), injectivity immediately gives \(|C|\le2^3=8\).

It remains to consider \(m=4\). Since four integers at least \(2\) sum to \(9\), the class-size multiset is \(\{2,2,2,3\}\). Order the representative coordinates so that the weight \(3\) coordinate is fourth. Split the compressed code according to the fourth bit. Inside either slice, changing exactly one of the first three bits would have weighted distance \(2<3\), so each slice is a binary length-three code of ordinary minimum distance at least \(2\). Pairing the vertices of \(\mathbb F_2^3\) along one coordinate shows that such a code has at most \(4\) words. There are two slices, hence \(|C|\le4+4=8\). Together with the construction, this proves the claim.

## Verification
The standalone verifier `verify.py` reconstructs \(C_0\), checks its size, global minimum distance, and every locality condition directly. For the upper-bound reduction, it enumerates every integer partition of \(9\) into class sizes at least \(2\), and then exhaustively enumerates every subset of the corresponding binary quotient cube to compute the largest weighted-distance-\(3\) code. The maxima by class-size partition are
\[
(2,2,2,3):8,\ (2,2,5):4,\ (2,3,4):4,\ (2,7):2,\ (3,3,3):8,\ (3,6):4,\ (4,5):4,\ (9):2.
\]
The global maximum is \(8\), and the script terminates with `VERIFY_OK`. The exhaustive computation verifies only the finite quotient problem; the reduction from locality to equivalence classes is proved above and is not inferred from the computation.

## Relationship to prior work
Kang and Xiong's 2026 three-block linear-programming paper defines the same all-symbol local-distance locality without assuming linearity and tabulates the parameter \((q,n,d,r,\delta)=(2,9,3,1,2)\). Their certified bounds give an eight-word construction and the upper bound \(64/5\), so the exact nonlinear maximum is not determined there. Their paper states seven exact maximum code sizes, and this row is not among them. Li, Wei, and Xiong's earlier 2026 moment-based LP likewise provides general bounds for nonlinear locally recoverable codes but does not state this exact value. A published research record on residual three-block LRC cases determines neighboring exact maxima, including a different binary locality-one parameter with local distance \(3\), but does not cover the present length-nine, local-distance-two tuple.

The proof here uses the especially rigid binary locality-one condition: every selected recovery pair forces its two coordinate functions to agree up to complement, so arbitrary overlapping recovery views collapse to equivalence classes and a small weighted quotient code. The exact value is therefore stronger than the cited \(64/5\) bound at this benchmark.

## Limitations
The theorem concerns only the binary parameter \((n,d,r,\delta)=(9,3,1,2)\). The equivalence-class reduction extends to other binary locality-one parameters, but no broader exact formula is claimed here. The argument does not address alphabets larger than two, where a two-coordinate local code of distance two need not force the same binary complement relation. The exact value has not been independently audited.

## References
1. M.-H. Kang and M. Xiong, *Linear Programming Bounds for Locally Recovery Codes II*, arXiv:2609.16044v1, 2026. In particular, Definition II.1 and Table V.1.
2. S. Li, H. Wei, and M. Xiong, *Moment-based linear programming bounds for locally recoverable codes*, arXiv:2608.05758v1, 2026.
