# The order-four integral reconstruction obstruction for Schläfli double-sixes

## Finding
Let \(S\) be a smooth cubic surface over an algebraically closed field of characteristic zero. Let \(\mathcal L\) be its set of \(27\) lines and \(\mathcal D\) its set of \(36\) unordered Schläfli double-sixes. For a double-six \(D\), let \(v_D=\sum_{\ell\in D}e_\ell\) in the formal lattice \(F=\mathbb Z^{\mathcal L}\). Put
\[
 L=\sum_{D\in\mathcal D}\mathbb Z v_D,\qquad
 K=\ker\left(F\longrightarrow\operatorname{Pic}(S)/\mathbb Z[-K_S]\right),
\]
where a basis vector maps to its line's divisor class modulo the anticanonical class. Then \(L\subset K\) and
\[
 \boxed{K/L\cong (\mathbb Z/2\mathbb Z)^{14}\oplus\mathbb Z/4\mathbb Z.}
\]
In particular, \([K:L]=65536\), and \(K\) is the saturation of \(L\) in \(F\). The integer \(27\)-by-\(36\) double-six incidence matrix has Smith normal form
\[
 \boxed{\operatorname{diag}(1^{6},2^{14},4,0^{6})},
\]
with \(6\) zero diagonal positions (and \(9\) further zero columns in its rectangular display). Consequently its cokernel is \(\mathbb Z^6\oplus(\mathbb Z/2\mathbb Z)^{14}\oplus\mathbb Z/4\mathbb Z\). Every formal combination of the \(27\) lines whose divisor class is a multiple of \(-K_S\) becomes an integer sum of double-six vectors after multiplication by \(4\), and the universal multiplier \(4\) is sharp: \(2\) does not suffice.

## Assumptions and scope
The theorem concerns the **formal** integer lattice on geometric lines, not the Picard group itself. Standard cubic-surface geometry identifies \(S\) with the blow-up of six points in general position in \(\mathbb P^2\). Write \(H\) for the pullback of a line and \(E_1,\ldots,E_6\) for exceptional divisors, with intersection matrix \(\operatorname{diag}(1,-1,-1,-1,-1,-1,-1)\). The \(27\) line classes are
\[
 E_i,\quad L_{ij}=H-E_i-E_j\ (i<j),\quad
 C_i=2H-\sum_{j\ne i}E_j.
\]
The anticanonical class is \(-K_S=3H-\sum_iE_i\). All integral computations use the ordering \(E_1,\ldots,E_6\), then \(L_{12},L_{13},\ldots,L_{56}\) in lexicographic order, then \(C_1,\ldots,C_6\). There is no special-moduli or finite-field hypothesis within characteristic zero.

## Proof
**1. Root-theoretic construction.** The \(72\) roots in \((-K_S)^\perp\subset\operatorname{Pic}(S)\) occur in \(36\) opposite pairs. Select representatives
\[
 E_i-E_j\ (i<j),\qquad
 H-E_i-E_j-E_k\ (i<j<k),\qquad
 2H-\sum_iE_i.
\]
For each root \(r\), the \(12\) line classes having \(\ell\cdot r\ne0\) are the double-six corresponding to \(\{r,-r\}\). They consist of six lines with pairing \(+1\) and six with pairing \(-1\). This is the classical root/double-six correspondence. The sum of the twelve line classes is \(4(-K_S)\), as can be checked on the displayed representatives; equivalently, check the standard double-six \(\{E_i,C_i\}\) and use the Weyl group. Hence \(L\subseteq K\).

**2. Saturated rational span.** The classes of the \(27\) lines generate \(\operatorname{Pic}(S)\), since the six \(E_i\) and \(H=L_{12}+E_1+E_2\) generate it. The class \(-K_S\) is primitive. Thus \(\operatorname{Pic}(S)/\mathbb Z[-K_S]\cong\mathbb Z^6\), and \(K\) is a saturated rank-\(21\) sublattice of \(F\). Let \(A\) be the \(27\)-by-\(36\) incidence matrix. Each line belongs to \(16\) double-sixes. Of the \(351\) unordered pairs of lines, \(135\) meet and \(216\) are skew. Meeting pairs lie in \(8\) common double-sixes, skew pairs in \(6\). If \(G\) is the adjacency matrix for meeting of distinct lines and \(J\) is the all-ones matrix, then
\[
 AA^{\mathsf T}=10I+2G+6J.
\]
The meeting graph has adjacency eigenvalues \(10\), \(1\), \(-5\) with multiplicities \(1\), \(20\), \(6\) respectively; the Gram eigenvalues are therefore \(192\), \(12\), \(0\) with the same multiplicities. Hence \(\operatorname{rank}_{\mathbb Q} A=21\) and \(\operatorname{sat}_F(L)=K\).

**3. Primitive coordinates.** In the quotient \(\operatorname{Pic}(S)/\mathbb Z[-K_S]\), eliminate \(E_6\) using \(E_6=3H-\sum_{i=1}^{5}E_i\). The six line classes \(E_1,\ldots,E_5,L_{12}\) map to an integral basis (determinant \(-1\)). Therefore the projection of \(K\) to the remaining \(21\) line coordinates is an isomorphism onto \(\mathbb Z^{21}\). Denote the resulting \(21\)-by-\(36\) matrix by \(B\); its retained zero-based row indices in the ordering above are \(5,7,8,\ldots,26\). Sort the \(36\) double-six supports lexicographically by their increasing lists of zero-based line indices, and index their columns \(0,\ldots,35\).

**4. Sharp integral certificate.** Exact reduction modulo \(2\) yields \(\operatorname{rank}_{\mathbb F_2}(B)=6\). The square minor using **all \(21\) rows** and columns
\[
 (1,3,5,6,9,10,13,14,16,17,18,19,20,22,23,26,27,29,30,33,35)
\]
has exact determinant \(-65536=-2^{16}\). Finally the primitive row covector
\[
 w=(1,0,0,0,-1,0,0,0,-1,0,0,-1,0,-1,-1,-1,-1,-1,-1,-1,0)
\]
satisfies \(wB=(-4,-4,\ldots,-4)\). Thus reduction of \(w\) modulo \(4\) induces a surjection \(\mathbb Z^{21}/\operatorname{im}(B)\twoheadrightarrow\mathbb Z/4\mathbb Z\). Since the mod-\(2\) rank is \(6\), exactly \(15\) of the \(21\) nonzero Smith factors are even, forcing the index to be at least \(2^{15}\); the order-four quotient forces a second factor of \(2\), so the index is at least \(2^{16}\). The displayed nonzero minor gives the opposite bound. Hence the index is exactly \(2^{16}\), and the only possible Smith factors are \(1^6,2^{14},4\). This proves all assertions.

## Verification
Run `python3 verify_double_sixes.py` using Python \(3\) and its standard library only. The program enumerates the \(36\) roots (up to sign) and the \(27\) exceptional classes; reconstructs each double-six from the intersection pairing; independently checks all column class sums, incidence valencies, pair-intersection counts, and the primitive quotient basis; computes the mod-\(2\) rank by exact bit elimination; and evaluates the displayed minor by fraction-free integer Bareiss elimination. It also checks \(wB=-4\) for every one of the \(36\) columns. The output terminates in `VERIFY_OK`. These are exhaustive calculations on a fixed finite matrix; the passage to all smooth cubic surfaces is justified by the uniform blow-up/incidence classification in the proof, not by sampling particular surfaces.

## Relationship to prior work
Schläfli's double-sixes, the \(27\) line classes, and their identification with opposite \(E_6\)-roots are classical. Dolgachev–Kapranov (1993, §0) describe the double-six geometry and its Schur quadrics. Alexeev–Donagi–Farkas–Izadi–Ortega (2015, §2) give explicit root and exceptional-vector coordinates for the \(36\) double-sixes in the context of Prym–Tyurin geometry. Arap–Varley (2012, Lemma 2.5) discuss the rational span of the distinct **tritangent triple** vectors, which is a related \(21\)-dimensional space but not an integral classification of the \(36\) **double-six** twelve-line vectors. Marquand (2022, Appendix B) uses double-six root data for intersections of twisted cubics and lattice theory, but the inspected material does not compute the present formal incidence-lattice quotient. The new determination is the integral saturation defect and sharp exponent, not the classical configurations or rational ranks.

## Limitations
No claim is made about actual torsion of \(\operatorname{Pic}(S)\), arithmetic Galois modules, line-bundle relations, or all possible integral \(E_6\)-incidence modules. Although related primary sections and database records were checked, an equivalent historical Smith calculation in finite-geometry, coding-theory, or older cubic-surface literature cannot be ruled out without further independent review. Independent scientific audit has not been performed.

## References
1. I. Dolgachev and M. Kapranov, *Schur quadrics, cubic surfaces and rank 2 vector bundles over the projective plane*, arXiv:alg-geom/9304005 (first posted 1993-04-13), especially §0.
2. V. Alexeev, R. Donagi, G. Farkas, E. Izadi, and A. Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, arXiv:1507.05710 (first posted 2015-07-21), §2.
3. M. Arap and R. Varley, *On algebraic equivalences among the twenty-seven Abel-Prym curves on a generic abelian five-fold*, arXiv:1206.6517 (first posted 2012-06-27), Lemma 2.5.
4. L. Marquand, *Cubic fourfolds with an involution*, arXiv:2202.13213 (first posted 2022-02), Appendix B.
