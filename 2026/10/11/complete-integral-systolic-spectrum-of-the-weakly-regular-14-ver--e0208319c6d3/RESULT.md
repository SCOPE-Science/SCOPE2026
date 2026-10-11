# Complete integral systolic spectrum of the weakly regular 14-vertex Klein bottle
## Finding
Let \(K=Q_{7,2}\) be the 14-vertex triangulation on \(\mathbb Z/14\mathbb Z\) whose facets are
\[
\{i,i+1,i+2\}\quad\text{and}\quad\{i,i+2,i+8\},\qquad i\in\mathbb Z/14\mathbb Z.
\]
Then \(K\) is flag and
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]
Among the 77 unoriented simple four-edge cycles in the one-skeleton, exactly 35 have nonzero integral homology. These 35 cycles are exactly the simple edge cycles of minimum nonzero integral-homology length. Exactly 21 represent the unique nonzero torsion class, while exactly 14 have primitive infinite-order class.

Under addition by one on the vertex labels, these 35 cycles form three orbits. A 14-element torsion orbit is represented by \((0,1,7,6)\), a 7-element torsion orbit is represented by \((0,1,7,8)\), and a 14-element primitive orbit is represented by \((0,2,4,6)\).
## Assumptions and scope
The object is the labeled cyclic complex \(Q_{7,2}\) from the Datta--Upadhyay family. Their construction states that \(Q_{7,2}\) triangulates the Klein bottle and is weakly regular. The statement here concerns simple cycles in the one-skeleton and their classes in integral first homology. It does not classify longer cycles, arbitrary singular cycles, or all 14-vertex flag triangulations of the Klein bottle.
## Proof
The published facet formula gives 14 vertices, 42 edges, and 28 triangular facets. Direct clique enumeration shows that the 28 graph triangles are exactly the 28 facets and that the one-skeleton has no 4-clique. Hence every clique is a simplex and \(K\) is flag.

Collapse the path spanning tree \(0-1-\cdots-13\). The 29 remaining oriented edges generate the cycle group after contraction, and the 28 triangle boundaries give a \(28\times29\) integral relation matrix \(R\). At least one maximal minor of \(R\) is nonzero, so \(R\) has rank 28 over \(\mathbb Q\). The greatest common divisor of all 29 maximal minors is 2. Therefore the presentation has one free generator and torsion of order 2, so
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]
The signed maximal cofactors, divided by 2, form a primitive integer vector annihilated by every row of \(R\); pairing a cycle with this vector gives its coordinate on the free quotient. Modulo 2, the relation matrix has rank 27, so the quotient has dimension 2. A four-cycle with zero free coordinate is the nonzero torsion class exactly when its mod-two residue is nonzero.

Exhaustive simple-cycle enumeration finds 28 three-cycles and 77 four-cycles. Every three-cycle is a facet boundary, so no simple cycle of length three has nonzero homology. Of the four-cycles, 42 have zero free coordinate and zero mod-two residue, 21 have zero free coordinate but nonzero mod-two residue, and 14 have free coordinate of absolute value 1. Thus the latter 35 cycles are precisely the simple integral-homology systoles; the 21 zero-free-coordinate cycles are the unique nonzero torsion class, and the 14 remaining cycles are primitive infinite-order classes.

Finally, translating vertices modulo 14 and identifying a cycle up to reversal and cyclic reparametrization partitions the 35 cycles into the three stated orbits of sizes 14, 7, and 14. The first two orbits have zero free coordinate and nonzero mod-two residue, while the third has free coordinate of absolute value 1.
## Verification
The accompanying `verify.py` reconstructs \(K\) only from the published facet formula. It checks the face vector, manifold edge incidences, flagness, the integral determinantal calculation, the mod-two rank, all simple cycles of lengths three and four, their homology classification, and the three translation orbits. Its successful terminal line is:

`VERIFY_OK f=14,42,28 flag=yes H1=Z+Z/2 cycles4=77 essential4=35 torsion4=21 primitive4=14 orbits=14T,7T,14P systole=4`
## Relationship to prior work
Datta and Upadhyay define \(Q_{2m+1,2}\), prove that these complexes triangulate the Klein bottle, and prove weak regularity by cyclic translation. For the 14-vertex degree-regular Klein-bottle cases in their classification, \(Q_{7,2}\) is the only weakly regular one. Their paper does not state the flag property or the complete shortest integral-homology cycle spectrum above.

Later work on flag triangulations reports at least 28 non-isomorphic 14-vertex flag triangulations of the Klein bottle and treats induced four-cycles as structurally important. The inspected text does not identify \(Q_{7,2}\) with one of those examples and does not state the 77/35/21/14 cycle counts or the three translation orbits.
## Limitations
The proof is an exact finite calculation for this labeled triangulation. It does not prove that 14 vertices is globally minimal for a flag triangulation of the Klein bottle; the cited flag-triangulation work describes that value as computationally suggested rather than proved. It also does not classify non-simple or longer representatives of the same homology classes. A residual originality risk remains that an older or unindexed computation may contain some of these finite counts.
## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433v1, submitted 2004-03-25. Example 6 gives the facet formula and weak regularity; Theorem 6 identifies \(Q_{7,2}\) among the 14-vertex Klein-bottle triangulations.
2. C. Bibby, A. Odesky, M. Wang, S. Wang, Z. Zhang, and H. Zheng, *Minimal flag triangulations of lower-dimensional manifolds*, arXiv:1909.03303v1, submitted 2019-09-07. Example 3.3 reports at least 28 non-isomorphic 14-vertex flag Klein-bottle triangulations.
