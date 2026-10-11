# Cyclic symmetry on Heawood independence homology
## Finding
Let \(H\) be the Heawood graph realized as the point-line incidence graph of the Fano plane, and let \(r\) be the order-seven automorphism sending point \(p_i\) to \(p_{i+1}\) and line \(\ell_i\) to \(\ell_{i+1}\), with indices modulo \(7\). Then, as a \(\mathbb Q[C_7]\)-module, \(H_3(\operatorname{Ind}(H);\mathbb Q)\cong \ker(\mathbb Q[C_7]\xrightarrow{\sum}\mathbb Q)\cong\mathbb Q(\zeta_7)\). Equivalently, the character on \(1,r,\ldots,r^6\) is \((6,-1,-1,-1,-1,-1,-1)\).

## Assumptions and scope
Let \(H\) have point vertices \(p_0,\ldots,p_6\) and line vertices \(\ell_0,\ldots,\ell_6\), with indices modulo \(7\), and put \(p_i\sim\ell_j\) exactly when \(i-j\in\{0,1,3\}\). This is the standard Fano-plane incidence realization of the Heawood graph. Let \(r(p_i)=p_{i+1}\) and \(r(\ell_i)=\ell_{i+1}\). The claim concerns the induced action of the cyclic subgroup \(C_7=\langle r\rangle\) on rational homology. It does not determine the integral \(\mathbb Z[C_7]\)-module or the representation of the full automorphism group.

## Proof
The independence complex \(\operatorname{Ind}(H)\) consists of all independent vertex sets of \(H\). Exhaustive enumeration gives \(457\) nonempty faces and face vector
\[
(14,70,154,147,56,14,2).
\]
A staged vertex-toggle matching on the complete face poset has \(225\) matched pairs. Direct verification on all \(1568\) Hasse covers shows that the reversed-matched-edge orientation is acyclic. Exactly one critical \(0\)-simplex and six critical \(3\)-simplices remain. Forman's discrete Morse theorem therefore gives
\[
\operatorname{Ind}(H)\simeq\bigvee^6 S^3,
\]
so reduced rational homology vanishes outside degree \(3\) and \(\dim H_3=6\).

For each \(k=0,\ldots,6\), compute the signed trace of \(r^k\) on every simplicial chain group. For \(k=0\), the alternating chain trace is the Euler characteristic \(-5\), hence the Lefschetz number is \(-5\). For every \(1\le k\le6\), the only nonempty simplices fixed setwise by \(r^k\) are the seven point vertices taken together and the seven line vertices taken together. Each is a \(6\)-simplex, and the induced seven-cycle has sign \(+1\). Thus the Lefschetz number is \(2\). Since only \(H_0\) and \(H_3\) are nonzero and \(r^k\) acts trivially on \(H_0\), the Hopf trace formula gives
\[
\operatorname{tr}(r^k\mid H_3)=1-L(r^k),
\]
which yields the character \((6,-1,-1,-1,-1,-1,-1)\).

This is the regular character of \(C_7\) minus the trivial character. Hence the rational representation is the augmentation ideal of \(\mathbb Q[C_7]\). Because \(7\) is prime, that augmentation ideal is the irreducible cyclotomic representation \(\mathbb Q[x]/(1+x+\cdots+x^6)\cong\mathbb Q(\zeta_7)\), proving the claim.

## Verification
The standalone `verify.py` reconstructs the graph from the incidence rule, confirms that \(r\) has order \(7\) and preserves every edge, enumerates all independent faces, rebuilds the staged matching, checks every Hasse cover and acyclicity, and independently computes all seven signed chain traces. It returns the face vector above, \(225\) matching pairs, critical vector \((c_0,c_3)=(1,6)\), Lefschetz vector \((-5,2,2,2,2,2,2)\), and the asserted degree-three character. The supplied `certificate.json` records these finite invariants.

## Relationship to prior work
Matsushita and Wakatsuki develop independence-complex topology in primary MSC \(55P10\) and determine homotopy types for a grid-graph family; their paper supplies the topology setting but does not treat the Heawood graph or an equivariant homology representation. Perarnau and Perkins give the exact Heawood independence polynomial, whose coefficients reproduce the face vector used here, but their result is enumerative rather than an induced homology-action computation. Flapan, Lawrence, and Wilson study symmetry groups of spatial embeddings of the Heawood graph; the accessible abstract and metadata concern graph symmetries in \(S^3\), not the action on independence-complex homology. A same-object nonequivariant homotopy computation \(\operatorname{Ind}(H)\simeq\bigvee^6S^3\) was also compared during the literature check; that statement fixes the rank of \(H_3\) but does not determine the \(C_7\)-module structure.

## Limitations
The result is only for the canonical order-seven Fano translation subgroup and rational coefficients. It does not compute the full \(336\)-element automorphism-group representation, an integral lattice classification, or equivariant attaching data beyond the induced homology character. The literature comparison was targeted rather than exhaustive; one symmetry article could only be inspected through its abstract and bibliographic metadata because its full page was temporarily unavailable.

## References
1. T. Matsushita and S. Wakatsuki, *Independence complexes of (n×6)-grid graphs*, arXiv:2207.10363v1, first public 2022-07-21; primary MSC 55P10.
2. G. Perarnau and W. Perkins, *Counting independent sets in cubic graphs of given girth*, Journal of Combinatorial Theory, Series B 133 (2018), 211–242, DOI 10.1016/j.jctb.2018.04.009.
3. E. Flapan, B. Lawrence, and R. Wilson, *Topological Symmetry Groups of the Heawood Graph*, Symmetry 12 (2020), 546, DOI 10.3390/sym12040546.
