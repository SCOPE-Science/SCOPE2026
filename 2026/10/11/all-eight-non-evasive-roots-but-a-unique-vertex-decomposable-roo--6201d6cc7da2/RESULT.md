# All eight non-evasive roots but a unique vertex-decomposable root in the minimal non-extendably collapsible ball
## Finding
Let \(B\) be the eight-vertex, twelve-tetrahedron ball of Benedetti--Lutz obtained from the Grünbaum--Sreedharan sphere \(S_{32}\) by deleting the seven tetrahedra listed in their Theorem 2. With the standard recursive definition of non-evasiveness, every one of the eight vertices is an admissible first vertex: for each vertex \(v\), both \(B-v\) and \(\operatorname{lk}_B(v)\) are non-evasive. In contrast, for pure vertex-decomposability exactly one vertex, the published label \(5\), is an admissible first shedding vertex. For every \(v\neq 5\), the deletion \(B-v\) is non-pure because it has maximal triangles as well as tetrahedra; deleting \(5\) leaves a pure three-dimensional complex and both its deletion and link branches are vertex-decomposable.

This gives a sharp first-step separation between two recursive simplification notions on the same canonical ball: non-evasiveness allows every vertex first, whereas pure vertex-decomposability forces the first vertex.

## Assumptions and scope
The complex \(B\) is the labeled ball in Benedetti--Lutz. Their sphere \(S_{32}\) has nineteen tetrahedra, and their Theorem 2 removes exactly seven of them, leaving the twelve tetrahedra reconstructed in `verify.py`. The claim concerns these published labels \(0,1,\ldots,7\).

A nonempty simplex is taken to be non-evasive. A non-simplex \(K\) is non-evasive when some vertex \(v\) has both deletion \(K-v\) and link \(\operatorname{lk}_K(v)\) non-evasive; the empty complex is not used as a successful base case. For pure vertex-decomposability, a simplex is the base case and a first vertex must be a shedding vertex whose deletion has the same pure dimension, whose link has dimension one lower, whose link facets are not deletion facets, and whose two recursive branches are vertex-decomposable.

## Proof
The published nineteen tetrahedra of \(S_{32}\) and the seven tetrahedra removed in Theorem 2 determine \(B\) uniquely. Closing the remaining twelve tetrahedra under faces gives
\[
f(B)=(8,25,30,12).
\]

For non-evasiveness, the recurrence is finite and strictly lowers the number of vertices. The verifier memoizes the truth value of the recurrence on the exact face sets reached from each of the sixteen first child complexes \(B-v\) and \(\operatorname{lk}_B(v)\). All sixteen are non-evasive, so every \(v\in\{0,1,\ldots,7\}\) is an admissible first root.

For vertex-decomposability, examine the maximal faces after deleting each vertex. The deletion profiles, written as “dimension : number of maximal faces”, are
\[
egin{array}{c|c}
v & \text{profile of maximal faces of }B-v\\
\hline
0&(2:3,\ 3:4)\\
1&(2:2,\ 3:4)\\
2&(2:1,\ 3:7)\\
3&(2:1,\ 3:6)\\
4&(2:1,\ 3:7)\\
5&(3:9)\\
6&(2:3,\ 3:5)\\
7&(2:1,\ 3:6).
\end{array}
\]
Thus \(B-v\) is non-pure for every \(v\neq5\), so no such vertex can be a first shedding vertex in the pure vertex-decomposable recursion. For \(v=5\), the deletion is pure three-dimensional and the link is pure two-dimensional; exact recursive checking verifies that both branches are vertex-decomposable and that the shedding condition holds. Hence \(5\) is the unique admissible first vertex for pure vertex-decomposability.

## Verification
Run `python verify.py`. It reconstructs \(B\) from the published \(S_{32}\) tetrahedra and removal list, verifies the face vector, evaluates the standard non-evasive recurrence for every first deletion and link, independently evaluates the pure vertex-decomposable recurrence, and checks all eight deletion-purity profiles. The expected terminal line begins `VERIFY_OK` and reports all eight non-evasive roots and the unique vertex-decomposable root \(5\).

## Relationship to prior work
Benedetti--Lutz prove that \(B\) is vertex-decomposable and non-evasive, and exhibit the valid vertex-deletion sequence \(5,2,4,0,1\). Their statement proves existence of a successful recursive route; it does not assert that every vertex is a valid first non-evasive root, nor that \(5\) is the unique first shedding vertex. Their Theorem 2 simultaneously shows that \(B\) is not extendably collapsible because some elementary collapse sequence reaches the dunce hat. The present dichotomy therefore separates first-step robustness for vertex queries from first-step rigidity for pure vertex-decomposability inside an example already known to be fragile under elementary collapses.

The general theorem that every vertex-decomposable ball is non-evasive also supplies only existence of a non-evasive root and does not imply the eight-root conclusion or the uniqueness of the vertex-decomposable root.

## Limitations
The claim is about one canonical labeled eight-vertex ball and only the first recursive step. It does not classify all later non-evasive decision trees, all vertex-decomposition sequences, or all eight-vertex balls. The originality search can miss unindexed computations or unpublished notes; the Electronic Geometry Models page was not fully retrievable during source inspection, although the complete arXiv full text and the exact tetrahedron lists needed for the claim were inspected.

## References
1. B. Benedetti and F. H. Lutz, *The dunce hat in a minimal non-extendably collapsible 3-ball*, arXiv:0912.3723v1, first public 2009-12-18; Electronic Geometry Models No. 2013.10.001. Primary MSC 57Q05; secondary 57Q15, 57Q35.
2. B. Benedetti and F. H. Lutz, *Knots in collapsible and non-collapsible balls*, Electronic Journal of Combinatorics 20(3), P31 (2013), Section 6 on non-evasiveness and vertex-decomposability.
