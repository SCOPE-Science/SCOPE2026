# The Morse complex of the Wagner graph \(M_8\) is a wedge of \(147\) six-spheres
## Finding
For the Wagner graph \(M_8\), with vertex set \(\mathbb Z/8\mathbb Z\), cycle edges \(\{i,i+1\}\) and opposite edges \(\{i,i+4\}\), the Morse complex of acyclic discrete vector fields satisfies \(\mathcal M(M_8)\simeq \bigvee^{147} S^6\).

## Assumptions and scope
The Wagner graph \(M_8\) has vertices \(0,1,\ldots,7\), the eight cycle edges \(\{i,i+1\pmod 8\}\), and the four opposite edges \(\{i,i+4\}\) for \(0\le i<4\). The Morse complex \(\mathcal M(M_8)\) has primitive vertex-edge pairs as vertices and acyclic discrete vector fields as simplices. For graphs these simplices are rooted forests, each selected tree component being oriented toward its unique root.

## Proof
There are \(24\) primitive pairs. Exhaustive rooted-forest enumeration gives \(23{,}804\) nonempty simplices with face vector
\[
(24,240,1296,4084,7520,7504,3136).
\]
These coefficients, preceded by \(1\), agree with \(\det(I+tL)\).

A staged element matching uses the order stored in `certificate.json`. Directly orienting all \(125{,}280\) Hasse covers and reversing the matched covers gives an acyclic directed graph. The matching has \(11{,}818\) pairs and leaves one critical \(0\)-simplex, ten critical \(5\)-simplices, and \(157\) critical \(6\)-simplices. Thus Forman theory gives a CW model with exactly those cells.

The signed gradient-path boundary \(C_6\to C_5\) is a \(10\times157\) integer matrix. Columns \(2,13,22,58,59,64,65,67,73,79\) form a \(10\times10\) minor of determinant \(-1\). Hence the boundary is surjective over \(\mathbb Z\), so \(H_5=0\), and its kernel is free of rank \(147\). The CW model is \(4\)-connected because its \(4\)-skeleton is a point. Hurewicz gives \(\pi_5=0\), so it is \(5\)-connected, and then \(\pi_6\cong H_6\cong\mathbb Z^{147}\). A map from \(\bigvee^{147}S^6\) representing a basis of \(\pi_6\) is a homology isomorphism, hence a homotopy equivalence by the simply connected Whitehead theorem.

## Verification
Run `python verify.py`. The verifier rebuilds all rooted forests, checks closure, reconstructs all Hasse covers, verifies acyclicity of the complete matched Hasse orientation, rebuilds the signed Morse boundary, and evaluates the unit minor by the fraction-free Bareiss determinant. It also computes the full simplicial boundary ranks over \(\mathbf F_2\), \(\mathbf F_3\), and \(\mathbf F_5\); each gives Betti vector \((1,0,0,0,0,0,147)\).

## Relationship to prior work
Donovan, Lin, and Scoville compute exact Morse-complex homotopy types for selected graph families such as caterpillar and related tree constructions, not the Wagner graph. Scoville and Zaremsky define the same Morse complex, stress that precise homotopy types are difficult, and prove general connectivity bounds rather than this graph-specific type. Donovan and Scoville later treat tree, path, extended-star, cycle-related, and matching/generalized-complex families; the Wagner graph is not among the listed families. Database searches covered both “Wagner graph” and “Möbius ladder \(M_8\)” and the aliases “Morse complex,” “complex of discrete Morse functions,” and “rooted forest complex.” The closest Wagner record concerns a different total \(3\)-cut complex, and a nearby cube record concerns a different graph and only mod-\(2\) homology.

## Limitations
The claim concerns only the ordinary Morse complex of this explicitly defined eight-vertex graph. It gives no formula for larger Möbius ladders, all cubic graphs, or generalized Morse complexes. An independently existing computation in an unindexed source remains a residual literature risk.

## References
1. C. Donovan, M. Lin, and N. A. Scoville, “On the homotopy and strong homotopy type of complexes of discrete Morse functions,” arXiv:1909.11440, first public version 2019-09-25.
2. N. A. Scoville and M. C. B. Zaremsky, “Higher connectivity of the Morse complex,” arXiv:2004.10481, first public version 2020-04-22.
3. C. Donovan and N. A. Scoville, “Star clusters in the matching, Morse, and generalized complex of discrete Morse functions,” *New York Journal of Mathematics* 29 (2023), 1393–1412.
