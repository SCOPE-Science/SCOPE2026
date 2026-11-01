# The exterior-square homology representation of the \(\mathrm{PG}(2,3)\) cap complex

## Finding
Let \(P=\mathrm{PG}(2,3)\) be the thirteen-point projective plane over \(\mathbf F_3\). Form the cap simplicial complex \(K\) on its points: a finite subset is a simplex exactly when no three of its points are collinear. Let \(G=\mathrm{PGL}_3(\mathbf F_3)\) act by projective collineations, and let \(U=\ker(\mathbf Q^P\xrightarrow{\mathrm{sum}}\mathbf Q)\) be the twelve-dimensional augmentation representation. Then

\[\widetilde H_i(K;\mathbf Q)=0\quad(i\ne3),\qquad \widetilde H_3(K;\mathbf Q)\cong_G\bigwedge^2U,\qquad\dim\widetilde H_3(K;\mathbf Q)=66.\]

In particular, writing \(f(g)=|\{p\in P:g(p)=p\}|\), for every \(g\in G\) we have

\[\operatorname{tr}(g\mid\widetilde H_3(K;\mathbf Q))=\frac{(f(g)-1)^2-(f(g^2)-1)}2,\qquad\dim\widetilde H_3(K;\mathbf Q)^G=0.\]

This is a complete **rational equivariant refinement** of the numerical homology of this same cap complex, which was already known. It is not a new claim about integral homology.

## Assumptions and scope
The vertices are the one-dimensional subspaces of \(\mathbf F_3^3\). A representative is uniquely normalized so that its first nonzero coordinate is 1. A triple is collinear precisely when its representative columns have determinant zero in \(\mathbf F_3\). Faces contain no forbidden triple. Orient every face by increasing index in the lexicographically ordered vertex set; these orientation choices specify the integer matrices and signed permutation traces in the verifier. All homology in the statement uses coefficients \(\mathbf Q\), and \(G\) is the order-5616 projective **linear** group, not an unspecified larger group.

## Proof
**1. Faces and low-dimensional homology.** There are 13 points, and exactly 52 collinear triples because 13 lines each contain four points, so \(13\binom43=52\). Every triple not collinear is a face. Every four-cap is maximal: any five points in a projective plane of order three contain three collinear points. The exact face vector in dimensions 0 through 3 is \((13,78,234,234)\), with no higher faces. The complex has the full complete-graph one-skeleton and is connected. For each collinear triple, a fourth point off its line exists, and its three edges to the triple provide three noncollinear triangles filling the missing triangle boundary. Therefore *all* complete-graph cycle boundaries are in the image of \(\partial_2\), so \(\operatorname{rank}_{\mathbf Q}\partial_2=\binom{13}{2}-13+1=66\). Thus \(\ker\partial_2\) has dimension \(234-66=168\).

**2. Exact top boundary rank.** The 234 oriented four-cap tetrahedra give an integer \(234\times234\) matrix \(\partial_3\). The standalone program `VERIFY.py` reconstructs that matrix directly from the determinant criterion, and elementary column elimination modulo 101 gives rank 168 (repeated independently modulo 1009). A nonzero minor over a prime field is nonzero over \(\mathbf Q\), so \(\operatorname{rank}_{\mathbf Q}\partial_3\ge168\). Since \(\partial_2\partial_3=0\), its image lies in the 168-dimensional kernel of \(\partial_2\); hence equality holds. Thus reduced rational Betti numbers in degrees 0,1,2,3 are \((0,0,0,66)\), with no higher faces.

**3. The full character.** A projective-linear transformation is represented uniquely by an invertible \(3\times3\) matrix over \(\mathbf F_3\) scaled to have its first nonzero entry equal 1. There are \((27-1)(27-3)(27-9)/2=5616\) such matrices. The verifier enumerates all of them and asserts that their induced point permutations are distinct. For a simplex stabilized setwise by \(g\), its contribution to the trace of \(g\) on the oriented chain group is the sign of the permutation of its vertices. Consequently the reduced Lefschetz trace is

\[\widetilde L(g)=-1+\sum_{d=0}^{3}(-1)^d\sum_{\substack{F\in K,\;\dim F=d\\gF=F}}\operatorname{sgn}(g\mid F).\]

As the only nonzero rational reduced homology is in odd degree three, \(\operatorname{tr}(g\mid\widetilde H_3)=-\widetilde L(g)\). On the other hand, \(\chi_U(g)=f(g)-1\), and for any characteristic-zero representation \(V\), \(\chi_{\wedge^2 V}(g)=[\chi_V(g)^2-\chi_V(g^2)]/2\). The checker evaluates *both* expressions for each of the 5616 group elements and verifies equality, grouped into the eight occurring permutation-cycle types. Therefore the finite-dimensional rational representations are isomorphic by the character theorem for finite groups. The weighted sum of their character over all group elements vanishes, proving the final invariant-dimension assertion.

The eight cycle types, multiplicities, and common character values are respectively: \(1^{13}\): \((1,66)\); \(1^5 2^4\): \((117,2)\); \(1^4 3^3\): \((104,3)\); \(1^2 2\,3\,6\): \((936,-1)\); \(1\,2^2\,4^2\): \((702,-2)\); \(1\,3^4\): \((624,0)\); \(1\,4\,8\): \((1404,0)\); and \(13\): \((1728,1)\). The class sizes sum to 5616 and the class-size-weighted character values sum to zero.

## Verification
Run `python3 VERIFY.py` from a directory containing the standalone supplied verifier. It requires Python 3 with standard library only, makes no external calls, constructs all faces, checks modular ranks, enumerates the complete group and its signed Lefschetz traces, and must end with `FULL_CHARACTER_EQUALITY_OK`, `GLOBAL_INVARIANTS 0`, and `VERIFY_OK`. The accompanying `VERIFY_OUTPUT.txt` records one actual run. The finite verification is *exhaustive* for the stated finite projective plane and group; it is not extrapolated to other fields or dimensions. The conceptual upper rank bound and character-theoretic implication are proved above, rather than inferred from a failed computational search.

## Relationship to prior work
The same thirteen-point cap complex has previously had its *nonequivariant* integral homology determined, including a rank-66 third group and lower torsion. That established calculation is not reproduced or claimed as new here; its maximal-four-cap orbit does not determine the action on the 66-dimensional homology kernel. The contribution here is the complete \(\mathrm{PGL}_3(\mathbf F_3)\)-character and the exterior-square isomorphism. Csorba's results concern edge-subdivision independence complexes and Alexander duality, and Tsukuda's concern independence complexes of incidence graphs of hypergraphs; neither identifies this cap-complex homology module. Work on projective-plane line-facet complexes and classical classifications of arcs addresses different constructions or combinatorial counts. These comparisons do not constitute a proof of uniqueness in all literature.

## Limitations
Only rational equivariant homology is classified, for the single classical plane of order three. The verifier's modular boundary-rank computation establishes rational rank, not the integer Smith normal form; this claim does not deduce absence of torsion, describe the integral homology representation, establish homotopy type, or extend uniformly to other projective planes. Equivalent descriptions in unindexed geometric/topological literature cannot be excluded by database searches alone.

## References
- P. Csorba, *Subdivision Yields Alexander Duality on Independence Complexes*, Electronic Journal of Combinatorics 16(2), R11 (2009), DOI: 10.37236/77, first publicly dated 2009-05-12. Primary full text inspected for structural comparison.
- S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12(1) (2017), DOI: 10.55016/ojs/cdm.v12i1.62277. Primary full text inspected; later background, not the archive-dating source.
- M. Superdock, *Simplicial complexes from finite projective planes and colored configurations*, arXiv:2110.12314 (2021), public full text inspected. The simplicial complexes arise from line facets rather than the cap criterion.
- S. Ball, *Multiple Blocking Sets and Arcs in Finite Planes*, Journal of the London Mathematical Society 54 (1996), DOI: 10.1112/jlms/54.3.581. Geometric-arc context; only abstract-level material compared.
