# The unique smallest non-real-rooted edge-open-packing tree and an exact broom threshold

## Finding

For a finite simple graph \(G\), define its **edge-open-packing polynomial**
\[
E_G(z)=\sum_{S\subseteq E(G)\,\text{edge open packing}}z^{|S|},
\]
where two distinct selected edges are forbidden exactly when a third, distinct edge joins an endpoint of one to an endpoint of the other. Let \(B_d\) be the broom obtained from the star \(K_{1,d}\) by subdividing exactly one edge; thus \(|V(B_d)|=d+2\) and \(d\ge2\).

**Theorem.** For every integer \(d\ge2\),
\[
\boxed{E_{B_d}(z)=(1+z)\big((1+z)^{d-1}+z\big).}
\]
This polynomial has only real zeros **if and only if** \(d\le3\). Among **all finite forests**, the smallest order permitting a non-real zero is six, and the **unique six-vertex forest up to graph isomorphism** with a non-real-rooted edge-open-packing polynomial is \(B_4\), whose polynomial is
\[
\boxed{E_{B_4}(z)=(1+z)(z^3+3z^2+4z+1).}
\]
Thus acyclicity does not force the real-rootedness familiar from matching generating polynomials, even though the first obstruction is a tree.

## Assumptions and scope

Graphs are undirected, finite, simple and labeled when their edge subsets are counted; the polynomial does not depend on the chosen labeling. The empty edge set contributes one. Real-rooted means every complex zero, counting multiplicity, is real. Isolated vertices have no effect on \(E_G\), and the polynomial of a disjoint union is the product of its component polynomials. The family \(B_d\) has a center adjacent to \(d-1\) leaves and to a degree-two vertex attached to one further leaf. The statement about the minimum order ranges over **all forests**, including disconnected forests and isolated vertices, not just brooms.

## Proof

**1. Exact polynomial of the broom.** Denote by \(c\) its high-degree center, by \(b\) the edge from \(c\) to its degree-two neighbor, by \(a_1,\ldots,a_{d-1}\) the other \(d-1\) edges incident with \(c\), and by \(t\) the terminal edge at the degree-two neighbor. The only pairs of conflicting edges are \(\{t,a_i\}\), for \(1\le i\le d-1\): the edge \(b\) connects an endpoint of each, and no other third edge connects endpoints of two selected edges. In particular, \(b\) is compatible with every edge. Every edge-open packing therefore chooses \(b\) freely and then either an arbitrary subset of \(\{a_i\}\) with \(t\) absent, or selects \(t\) and none of the \(a_i\). This proves the displayed factorization.

**2. Exact real-rootedness threshold.** For \(d=2\), the second factor is \(1+2z\), and for \(d=3\) it is \(1+3z+z^2\), whose discriminant is \(5>0\). Hence all zeros are real for \(2\le d\le3\). For \(d\ge4\), put \(m=d-1\ge3\) and let \(Q_m(z)=(1+z)^m+z\). Its first coefficients are
\[
q_0=1,\quad q_1=m+1,\quad q_2=\binom m2,\quad q_3=\binom m3.
\]
If a degree-\(m\) polynomial with nonnegative coefficients has only real zeros, then all its zeros are nonpositive and its binomially normalized coefficient sequence \(q_k/\binom mk\) is log-concave by Newton's inequalities. At position \(k=2\), however,
\[
\left(\frac{q_2}{\binom m2}\right)^2=1
\quad<\quad
\frac{q_1}{\binom m1}\frac{q_3}{\binom m3}
=\frac{m+1}{m}.
\]
Hence \(Q_m\), and therefore \(E_{B_d}\), has non-real zeros for all \(d\ge4\). This establishes the sharp all-parameter threshold without numerical root approximation. For \(d=4\) the cubic factor has discriminant \(-31\), so precisely two of its three zeros are non-real.

**3. Minimal order over all forests.** Direct edge-open-packing enumeration on the complete list of nonisomorphic trees with at most six vertices gives the following factorization census at order six. The six tree shapes and polynomials are indexed by the canonical edge sets in the independent verifier `verify_roots.py`, with vertex labels \(0,\ldots,5\):

| Tree | Edge-open-packing polynomial | Real-rooted? |
|---|---|---|
| \(P_6\) | \((1+2z)(1+3z+z^2)\) | yes |
| three-arm spider of arm lengths \((1,1,3)\) | \((1+2z)(1+3z+z^2)\) | yes |
| double star with three edges at each center | \((1+z)(1+4z+2z^2)\) | yes |
| three-arm spider of arm lengths \((1,2,2)\) | \(1+5z+6z^2+z^3\) | yes |
| \(B_4\) | \((1+z)(1+4z+3z^2+z^3)\) | **no** |
| \(K_{1,5}\) | \((1+z)^5\) | yes |

The distinct cubic \(z^3+6z^2+5z+1\) has discriminant \(49>0\), hence three distinct real roots; as all its coefficients are positive, its roots are negative. Every other affirmative entry factors into powers of linear factors and quadratics with positive discriminant. For five vertices, the three trees have polynomials \((1+2z)^2\), \((1+z)(1+3z+z^2)\), and \((1+z)^4\), respectively. For orders one through four, direct enumeration gives paths or stars, each having real-rooted polynomial. As every disconnected forest is a product of tree factors, every forest with at most five vertices has a real-rooted polynomial; at six vertices any disconnected forest has components of at most five vertices and is also real-rooted. Among the six connected six-vertex shapes, only \(B_4\) fails. This completes the minimality and uniqueness proof.

## Verification

The standalone Python standard-library verifier `verify_roots.py` exhaustively enumerates all selected-edge subsets for canonical representatives of every unlabeled tree through six vertices (one, one, one, two, three and six classes by order). For each representative, it computes the coefficient vector **from the edge-open-packing conflict definition** and checks the asserted factorizations. The program independently enumerates the broom formula for \(2\le d\le9\) and checks the Newton-inequality witness for \(4\le d\le100\). It also evaluates the exact cubic discriminants and the real-rootedness of the listed lower-order cases through rational-arithmetic sign checks. The retained output is `verification_roots_output.txt`.

The exhaustive finite tests are not a proof for all \(d\); that is supplied by the factored form and the all-parameter Newton inequality. The finite minimality assertion relies on the complete enumeration of the six unlabeled six-vertex trees and three unlabeled five-vertex trees, for which the full coefficient data are given and independently reproduced.

## Relationship to prior work

Chelladurai, Kalimuthu, and Soundararajan, *Edge open packing sets in graphs* (2022), introduced the packing invariant and obtained scalar bounds and family values. Brešar and Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1 (first public 2024-03-01), developed maximum-cardinality algorithms for trees. Brešar, Dravec, Hedžet, and Samadi, arXiv:2406.04020 (2024), compared the maximum edge-open-packing and induced-matching parameters, also pointing out that edge-open packing is not ordinary open packing in the line graph. These inspected works do not present a real-zero obstruction or a minimal-order classification for the full edge-open-packing counting polynomial.

The broom polynomial may be recognized as the independence polynomial of a star with an isolated vertex, but **this is used as a derivation**, not claimed to be a new formula about ordinary independence polynomials. The new graph-theoretic assertion concerns the exact edge-open-packing polynomial and the unique smallest acyclic obstruction, with a sharp infinite broom threshold. General weighted counting results for bounded-treewidth graphs imply computability of this polynomial but do not imply the claimed location and classification of its zeros. Unindexed equivalent work remains a bibliographic risk.

## Limitations

This is not a theorem classifying real-rootedness on every forest, nor does it assert that non-real-rootedness implies nonunimodality. It gives an exact all-parameter threshold for one natural broom family and the sharp global smallest forest obstruction. Distinguishing roots by approximate numerics alone would not prove the claims; the actual proof uses Newton's inequalities, exact factorization and an exhaustive small-tree classification. Independent mathematical validation and exhaustive bibliographic priority verification remain unperformed.

## References

1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research **56** (2022), 3765–3776. DOI: `10.1051/ro/2022171`; open text: `https://www.numdam.org/item/10.1051/ro/2022171.pdf`.
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1, first posted 2024-03-01; full text: `https://arxiv.org/pdf/2403.00750`.
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (2024); full text: `https://arxiv.org/pdf/2406.04020`.
4. Classical Newton inequalities for the elementary symmetric functions of nonnegative real numbers, as applied to coefficient sequences of real-rooted polynomials.
