# A dihedral-to-Klein-four monodromy divisor for mixed elliptic surfaces

## Finding
For every complex rational elliptic surface of six-double-fibre type \((4,2)\) satisfying the assumptions below, its degree-four rational \(j\)-map has geometric monodromy group \(D_4\) (order eight), except on the explicit polar divisor \(\mathfrak p(P,Q)=0\), where the map becomes Galois with group \(V_4\). On the divisor the map has three branch values of partition \((2,2)\), whereas outside it has four values of partitions \((2,2),(2,2),(2,1,1),(2,1,1)\). The divisor is nonempty and proper among the allowed models.

## Assumptions and scope
Work over \(\mathbb C\). Adopt the six-singular-fibre Weierstrass normal form from Ciliberto–Grassi–Miranda–Verra–Zanardini, Section 4.1: \(y^2=x^3+A(t)x+B(t)\), \(B=AQ\), \(A=(P^2-27Q^2)/4\), with binary quadratic forms \(P,Q\). Require that \(P\) and \(Q\) both have two distinct zeros, share no zero, and \(P^2-27Q^2\) has four simple zeros. Thus the six singular fibres are exactly four type-II fibres (zeros of \(A\)) and two type-\(I_2\) fibres (zeros of \(P\)); this is a nonempty open subfamily, not the entire possibly degenerate parameter space.

In an affine coordinate let \(P=a t^2+bt+c\) and \(Q=d t^2+et+f\), and define \(\mathfrak p(P,Q)=be-2(af+cd)\). Vanishing is intrinsic: this is the polarization of the quadratic discriminant and scales under a change of base coordinates; changing signs/scales of \(P\) and \(Q\) also preserves its zero set. Let \(D_4\) mean the dihedral group of order eight and \(V_4=C_2\times C_2\). Monodromy means the permutation group of a degree-four map of complex projective lines, not the elliptic-fibre homology monodromy.

## Proof
**Step 1 (factor the invariant).** The discriminant of the Weierstrass cubic is \(4A^3+27B^2=A^2(4A+27Q^2)=A^2P^2\). Therefore, as rational functions,
\[
 j(t)=1728\frac{4A^3}{4A^3+27B^2}=1728\left(1-27\left(\frac{Q(t)}{P(t)}\right)^2\right).
\]
Write \(z=Q/P\) and \(h(z)=1728(1-27z^2)\). Both \(z:\mathbb P^1_t\to\mathbb P^1_z\) and \(h:\mathbb P^1_z\to\mathbb P^1_j\) have degree two. By the coprimality assumption, \(j=h\circ z\) has degree four.

**Step 2 (calculate branch sets).** The two critical values \(z_1,z_2\) of the map \(z=Q/P\) are exactly the simple zeros in \(z\) of the quadratic \(\Delta(z)=\operatorname{disc}_t(Q-zP)\). Expanding gives
\[
 \Delta(z)=(b^2-4ac)z^2+[4(af+cd)-2be]z+(e^2-4df).
\]
Since \(P\) and \(Q\) have simple zeros, the two distinct critical values are finite and nonzero. The four distinct roots of \(P^2-27Q^2\) moreover exclude \(z_i=\pm 1/\sqrt{27}\). The branch points of \(h\) are \(0,\infty\). Hence the branch values of \(j\) are \(1728,\infty,h(z_1),h(z_2)\); the last two coincide precisely when \(z_1=-z_2\), equivalently when the linear coefficient of \(\Delta\) vanishes, i.e. \(\mathfrak p(P,Q)=0\).

**Step 3 (geometric monodromy).** Consider function fields \(K=\mathbb C(j)\subset L=\mathbb C(z)\subset M=\mathbb C(t)\). Both steps are quadratic. The involution of \(L/K\) sends \(z\mapsto-z\). The double cover \(M/L\) is branched at the two-point set \(S=\{z_1,z_2\}\). Its conjugate under \(z\mapsto-z\) is branched over \(-S\). If \(S\ne-S\), the two distinct quadratic extensions over \(L\) are independent; their compositum has group \(C_2\times C_2\) over \(L\), and the involution of \(L/K\) interchanges the two factors. The Galois closure over \(K\) therefore has group \((C_2\times C_2)\rtimes C_2\cong D_4\), acting transitively on four sheets.

If \(S=-S\), the unique quadratic extension of \(\mathbb C(z)\) branched at \(S\) is preserved under the involution \(z\mapsto-z\); hence \(M/K\) is Galois of degree four. In this case its branch values are exactly \(1728,\infty,h(z_1)\). Each has two points of local degree two (because neither \(z_i\) equals \(0\) or \(\infty\)). Every nontrivial inertia subgroup has order two, excluding a cyclic quartic Galois group; hence the group is \(V_4\). Off the divisor the two values \(h(z_i)\) are distinct, each contributes a single simple ramification, while \(1728,\infty\) each have two simple ramification points, proving the asserted four branch partitions.

**Step 4 (proper nonempty jump divisor).** For \(P=t^2+1\), \(Q=t^2-1\), the hypotheses hold and \(\mathfrak p(P,Q)=0\). Here \(j\) is invariant under the commuting involutions \(t\mapsto-t\) and \(t\mapsto1/t\), visibly realizing \(V_4\). For \(P=t^2+1\), \(Q=t^2+t+2\), the hypotheses also hold, but \(\mathfrak p(P,Q)=-6\ne0\), so the monodromy is \(D_4\). Thus the jump divisor is genuine.

## Verification
A standalone SymPy checker supplied as `verify_mixed_jmap.py` checks the symbolic \(j\)-factorization, the quadratic critical-value discriminant, the two examples' squarefreeness and coprimality, and both explicit involutions on the exceptional example. These are algebraic consistency checks; the infinite statement follows from the function-field argument in the proof. Reproduce using `python verify_mixed_jmap.py` with SymPy installed. The checker does not prove originality, and finite examples alone do not establish the universal claim.

## Relationship to prior work
Ciliberto–Grassi–Miranda–Verra–Zanardini, *Rational elliptic surfaces with six singular double fibres* (arXiv:2602.11725v1), Section 4.1, supply the Weierstrass normal form and the two-dimensional moduli family. They do not identify the dihedral monodromy and its precise Klein-four jump divisor in the inspected 30-page paper. Classical quadratic-cover and Galois-closure theory explains why a composition of two double covers is at most dihedral; the contribution here is the sharp intrinsic polar equation and complete branching/monodromy stratification **for this elliptic-surface family**. Shaska's *The invariant ring of degree-four rational maps on the projective line* (arXiv:2608.23321) studies general degree-four-map invariants, not specifically these Weierstrass maps in the available abstract; its full text could not be inspected, so any stronger comparison remains a priority risk.

## Limitations
The claim concerns the \(j\)-map as a covering of projective lines, not automorphisms of the elliptic surface or the monodromy of the elliptic fibres. It applies only when \(P,Q\) and \(P^2-27Q^2\) have the specified simple-root properties. No claim is made for degenerations outside that locus. The standard covering theory and the published normal form are prior mathematics; independent priority verification remains unperformed.

## References
- C. Ciliberto, A. Grassi, R. Miranda, A. Verra, A. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725v1 (2026-02-12), Section 4.1, https://www.math.colostate.edu/~miranda/preprints/2602.11725v1.pdf .
- T. Shaska, *The invariant ring of degree-four rational maps on the projective line*, arXiv:2608.23321 (2026-08-24), https://arxiv.org/abs/2608.23321 (abstract inspected; full text unavailable).
