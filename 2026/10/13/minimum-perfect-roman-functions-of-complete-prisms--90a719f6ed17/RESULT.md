# Minimum perfect Roman functions of complete prisms
## Finding
For every integer \(n\ge4\), let
\[
G_n=K_n\square K_2
\]
with clique layers
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and matching edges \(a_i b_i\).

Then
\[
\gamma_R^p(G_n)=4.
\]
Moreover, the minimum perfect Roman dominating functions are exactly the \(n\) functions obtained by choosing one index \(i\), assigning
\[
f(a_i)=f(b_i)=2,
\]
and assigning label \(0\) to every other vertex.

Hence the number of minimum functions is exactly
\[
n.
\]

## Assumptions and scope
A perfect Roman dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex labeled \(0\) is adjacent to exactly one vertex labeled \(2\). Its minimum possible weight is \(\gamma_R^p(G)\).

The theorem is stated for \(n\ge4\). The triangular prism \(K_3\square K_2\) also has minimum weight \(4\), but it has additional minimum functions with only one label \(2\), so the optimizer classification changes at that boundary.

## Proof
Fix an index \(i\). Assign label \(2\) to \(a_i\) and \(b_i\), and label every other vertex \(0\). A zero vertex \(a_j\), with \(j\ne i\), is adjacent to \(a_i\) inside the clique \(A\) and is not adjacent to \(b_i\), because the only cross-layer edge incident with \(a_j\) is \(a_jb_j\). Hence it has exactly one neighbor labeled \(2\). The same argument holds in the layer \(B\). Therefore
\[
\gamma_R^p(G_n)\le4.
\tag{1}
\]

No function of weight at most \(3\) is feasible. A feasible function must contain a label \(2\) whenever a zero exists. Since \(2n\ge8\), every labeling of weight at most \(3\) has a zero. If there is exactly one label \(2\), say at \(a_i\), then every vertex \(b_j\) with \(j\ne i\) is not adjacent to that label \(2\). All such vertices would therefore have to be positive. There are \(n-1\ge3\) of them, which is impossible with at most one remaining unit of weight. Thus weight at most \(3\) cannot occur, and (1) is sharp.

Now let \(f\) have minimum weight \(4\). If \(f\) has exactly one vertex labeled \(2\), say \(a_i\), then all \(n-1\) vertices \(b_j\) with \(j\ne i\) must be positive, because none is adjacent to \(a_i\). But after spending weight \(2\) at \(a_i\), only two units remain, while \(n-1\ge3\). This is impossible.

Hence a minimum function has exactly two vertices labeled \(2\) and no vertices labeled \(1\). The two labels \(2\) cannot lie in the same clique layer: if they were at \(a_i,a_j\), then for \(n\ge4\) any zero vertex \(a_k\) with \(k\notin\{i,j\}\) would be adjacent to both and would have two neighbors labeled \(2\).

Thus the two labels \(2\) have the form \(a_i,b_j\). If \(i\ne j\), then the zero vertex \(a_j\) is adjacent both to \(a_i\) inside \(A\) and to its matched vertex \(b_j\), so it again has two neighbors labeled \(2\). Therefore \(i=j\). Conversely, the matched-pair construction was already proved feasible.

This proves both the value and the complete minimum-function classification.

## Verification
The included checker evaluates the defining perfect-Roman condition directly for every labeling of total weight at most \(4\) for \(4\le n\le12\). It verifies that no labeling of smaller weight is feasible and that every weight-\(4\) optimum is exactly a matched pair labeled \(2\).

## Relationship to prior work
Perfect Roman domination was developed for trees and regular graphs, and later from algorithmic and graph-product viewpoints. The regular-graph paper gives general upper bounds for cubic and higher-regular graphs, but these bounds do not determine the constant value or the equality functions for the \(n\)-regular complete prism.

A 2022 primary paper devoted to Cartesian products treats products of paths and cycles. Its full text explicitly limits the exact constructions to grids, cylinders, and tori, rather than products involving a complete graph. A later Cartesian-product paper proves complexity results for the product setting and gives an upper bound for perfect Italian domination on path/cycle products; its stated scope likewise does not supply the complete-prism theorem above.

Thus the result identifies a dense Cartesian-product family on which the perfect Roman optimum is constant and, more strongly, completely rigid: every optimum consists of the two endpoints of one product-matching edge carrying label \(2\).

## Limitations
The theorem treats complete prisms and minimum functions only; it does not enumerate all perfect Roman functions of every weight.

The finite checker is corroborative only. The arbitrary-order classification follows from the proof.

A differently phrased or non-indexed complete-prism treatment may exist despite the targeted searches.

## References
1. M. A. Henning, W. F. Klostermeyer, “Perfect Roman domination in regular graphs,” Applicable Analysis and Discrete Mathematics 12(1) (2018), 143–152, DOI 10.2298/AADM1801143H.
2. S. Banerjee, J. M. Keil, D. Pradhan, “Perfect Roman domination in graphs,” Theoretical Computer Science 796 (2019), 1–21, DOI 10.1016/j.tcs.2019.08.017.
3. A. Almulhim, A. D. Akwu, B. Al Subaiei, “The Perfect Roman Domination Number of the Cartesian Product of Some Graphs,” Journal of Mathematics (2022), Article 1957027, DOI 10.1155/2022/1957027.
4. A. Almulhim, “Perfect Roman and Perfect Italian Domination of Cartesian Product Graphs,” Scientific Journal of King Faisal University: Basic and Applied Sciences 25(2) (2024), 63–68, DOI 10.37575/b/sci/240037.
