# Thirty-nine primitive quadrilateral systoles on the Paley thirteen-vertex torus

## Finding
Let \(P_{13}\) be the Paley graph on \(\mathbb Z/13\mathbb Z\), with an edge between distinct \(x,y\) if and only if \(y-x\) belongs to the quadratic-residue set \(\{\pm1,\pm3,\pm4\}\). Let \(K=\operatorname{Cl}(P_{13})\) be its ordinary clique complex, with edge length one.

The simple integral-homology one-systole of \(K\) has length exactly four. There are **exactly 39 unoriented simple cycles** attaining it; they are **precisely the 39 induced four-cycles** of \(P_{13}\). Each represents a **primitive, nonzero** element of \(H_1(K;\mathbb Z)\cong\mathbb Z^2\). The full collection is a single orbit under the natural affine subgroup \(\mathbb F_{13}\rtimes(\mathbb F_{13}^{\times})^2\), of order 78.

More precisely, the 39 cycles form three translation orbits of 13 each. In a specified integral basis of \(H_1(K;\mathbb Z)\), their unoriented classes are
\[
\{\pm(0,-1)\},\qquad\{\pm(1,3)\},\qquad\{\pm(1,4)\},
\]
with exactly 13 cycles in each class. These three classes are distinct, and the shortest cycles **generate the entire integral first homology**. In contrast, the other 39 simple four-cycles all have a diagonal edge and are nullhomologous.

## Assumptions and scope
All graph cycles are simple closed edge walks, identified under reversal and cyclic rotation; their length is their number of edges. An integral one-systole is the minimum edge length of a simple cycle whose class in \(H_1(K;\mathbb Z)\) is nonzero. A primitive homology class is one that belongs to an integral basis, equivalently one not divisible by an integer greater than one. Classes of unoriented cycles are recorded up to sign.

The complex is exactly the cyclic torus triangulation \(T_{13,1,3}\) of Datta and Upadhyay. It has face families
\[
\{i,i+1,i+4\},\quad\{i,i+3,i+4\}\qquad (i\in\mathbb Z/13\mathbb Z).
\]
No assertion is made about shortest paths in other metrics, nor about every triangulation of the torus.

## Proof
**1. The flag torus and its integral universal cover.** Every vertex of \(P_{13}\) has six neighbours. Each adjacent pair has two common neighbours; each nonadjacent pair has three. The graph's triangles are exactly the 26 triangles in the two displayed face families, and its vertex links in their resulting complex are six-cycles. No four vertices form a clique. Thus \(K=T_{13,1,3}\), a connected triangulated torus, with face vector \((13,39,26)\). The identification and torus triangulation also follow directly from the cited original definition of \(T_{n,1,k}\).

For explicit integral homology coordinates, consider the simply connected triangular tessellation of \(\mathbb R^2\) with vertices \(\mathbb Z^2\), edges in directions \(\pm e_1\), \(\pm e_2\), and \(\pm(e_1+e_2)\), and triangular faces
\[
\{z,z+e_1,z+e_1+e_2\},\qquad \{z,z+e_2,z+e_1+e_2\}.
\]
The quotient homomorphism on vertices
\[
\phi:\mathbb Z^2\longrightarrow\mathbb Z/13\mathbb Z,\qquad \phi(a,b)=a+3b\pmod{13}
\]
identifies the quotient simplicial complex with \(K\). The deck lattice is
\[
L=\ker\phi=\{(a,b):a+3b\equiv0\pmod{13}\}.
\]
Because the tessellation is simply connected, lifting closed edge walks identifies \(\pi_1(K)\), and hence \(H_1(K;\mathbb Z)\), **integrally** with \(L\). Fix the isomorphism
\[
\Psi:L\xrightarrow{\cong}\mathbb Z^2,\qquad\Psi(a,b)=\left(\frac{a+3b}{13},b\right),
\]
whose inverse is \((p,q)\mapsto(13p-3q,q)\). For an oriented closed walk, sum its six permitted lifted edge increments to obtain its class; reversing orientation changes the sign. Boundary triangles have zero lifted sum, so this identification respects the simplicial relations. It detects nullhomotopy as well as integral homology because the deck group is abelian.

**2. Exhaustive four-cycle count without relying on a search log.** There are 39 edges and 39 nonedges in \(P_{13}\). The common-neighbour parameters are \(\lambda=2\) and \(\mu=3\). Count an unoriented simple four-cycle by choosing either of its two opposite pairs and then its two common neighbours. The exact count is
\[
\frac12\left(39\binom22+39\binom32\right)=78.
\]
No four vertices form a clique, so a four-cycle has at most one diagonal. Each graph edge is the unique diagonal of one four-cycle obtained from its two nonadjacent common neighbours; different edges give different chorded cycles. Exactly 39 four-cycles therefore have a chord, and the other 39 are induced. Every chorded four-cycle bounds the two triangular faces meeting along its diagonal and hence is nullhomologous.

**3. Complete symmetry classification of the induced cycles.** The affine transformations \(x\mapsto bx+t\), where \(t\in\mathbb F_{13}\) and \(b\in\{1,3,4,9,10,12\}\), preserve the graph and all its triangles. Apply them to the oriented four-cycle \(A=(0,1,2,3)\). Multipliers differing by sign produce the same translation orbit of unoriented cycles. Multipliers represented by \(1,3,4\) produce three distinct translation orbits, each of size 13, since the resulting edge-difference multisets have respectively three edges of step magnitude \(1,3,4\). Thus the affine orbit of \(A\) has 39 members. All are induced (the two potential diagonals have difference \(\pm2\) for \(A\)), so it exhausts all 39 induced cycles.

Convenient oriented representatives of the three translation orbits are
\[
A=(0,1,2,3),\qquad B=(0,1,5,9),\qquad C=(0,3,6,9).
\]
Their lifted edge-increment sums in \(L\) are, respectively,
\[
(3,-1),\qquad(4,3),\qquad(1,4).
\]
Applying \(\Psi\) gives
\[
[A]=(0,-1),\qquad[B]=(1,3),\qquad[C]=(1,4).
\]
The integral relation is \([B]=[A]+[C]\), since \((3,-1)+(1,4)=(4,3)\). Therefore the three unoriented classes are exactly those in the Finding. Their nonzero status proves every induced four-cycle essential. The determinant of \([A]=(0,-1)\) and \([C]=(1,4)\) is \(+1\), so these two classes form an integral basis; all three classes are primitive. Translations preserve the lifted net increment. Multiplication by three cycles the three unoriented directions, and the affine group is transitive on all 39 cycles.

**4. Minimality.** The graph has no loops or repeated-edge two-cycles, and all 26 simple three-cycles are faces. Every integral simplicial one-cycle decomposes as an integral sum of oriented simple edge cycles, so an essential one-cycle requires an essential simple cycle. The preceding essential four-cycles therefore realize the sharp integral one-systolic length four, and the classification is complete.

## Verification
Run `python3 verify.py` (only the standard library is required). It independently constructs the Paley graph and the torus face set, checks both common-neighbour parameters, all vertex links and absence of higher cliques, and exhaustively enumerates all simple three- and four-cycles. The program checks all six translation orbits of four-cycles and their winding coordinates, detects exactly 39 chorded null cycles and 39 induced essential cycles, checks the order-78 affine orbit, and confirms an integral determinant of one for the two displayed generators. The exact successful output is embedded in `verification_output.txt`.

The computational enumeration concerns a fixed finite 13-vertex graph and **is exhaustive**, not an extrapolation to an infinite family. The integral deck-lattice argument independently supplies the topological meaning of the winding coordinates. All required executable files are included in this package.

## Relationship to prior work
Datta and Upadhyay introduced \(T_{n,1,k}\), proved its torus topology and cyclic symmetry, and identified the two thirteen-vertex degree-regular torus triangulations. Brehm and Kühnel supplied a general classification of equivelar torus maps as triangular-lattice quotients, including the order-thirteen chiral example and its rotational symmetry. Those structural results are premises here; the claimed result is the **complete four-edge homological-systole carrier count, primitive-class spectrum, and integral generation statement**.

The published results *An exact flag criterion for the cyclic weakly regular torus family* and *A one-direction systolic shell in the cyclic torus family* concern, respectively, flagness in a parameter family and homological systoles only for \(n\ge17\). The first identifies the order-thirteen model as the first flag member of that family; the second explicitly does not include the thirteen-vertex case. Their conclusions do not give the present three-direction order-thirteen systolic census. Closest related work on the regular nine-vertex torus concerns a distinct triangulation and shorter triangular systoles.

## Limitations
The theorem is specific to the Paley-thirteen flag triangulation. It does not classify longer noncontractible cycles, other equivelar maps, or geometric-length systoles in continuously varying flat metrics. The order-thirteen surface and its lattice quotient are established prior work. The originality assessment depends on the accessible primary literature and record searches; a different notation or unindexed classification of these exact shortest cycles remains possible. There is no independent audit claim.

## References
1. Basudeb Datta and Ashish Kumar Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433v1, first public 2004-03-25. https://arxiv.org/abs/math/0403433
2. Ulrich Brehm and Wolfgang Kühnel, *Equivelar maps on the torus*, Stuttgart Mathematical Preprint 2006/013 (2006), subsequently European Journal of Combinatorics 29 (2008), 1843–1861. https://www.f08.uni-stuttgart.de/.content/media/downloads/Mathematik/mathematische_berichte/2006/2006-013.pdf
3. *An exact flag criterion for the cyclic weakly regular torus family* (public research record, 2026-10-11).
4. *A one-direction systolic shell in the cyclic torus family* (public research record, 2026-10-11).
