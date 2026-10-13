# Cyclic-stabilizer polygon criterion for Clifford mixtures under tilted qubit dephasing

## Finding

**Theorem (exact Clifford-mixture criterion).** Let \(u\in\mathbb R^3\) be a unit vector, let \(R\in SO(3)\), and let \(0\le p\le1\). Denote by \(U_R\) any qubit unitary whose Bloch rotation is \(R\), and define
\[
\mathcal E_{p,u,R}(\rho)=(1-p)U_R\rho U_R^\dagger+p\,(u\cdot\sigma)U_R\rho U_R^\dagger(u\cdot\sigma).
\]
Let \(\mathcal C\subset SO(3)\) be the group of 24 determinant-one signed permutation matrices, representing single-qubit Clifford conjugations. Set \(v=R^\top u\), \(\lambda=1-2p\), and \(\mathcal C_{u,v}=\{C\in\mathcal C:Cv=u\}\).

If \(\mathcal C_{u,v}\) is empty, the channel is not a convex combination of Clifford unitary channels. Otherwise select any \(C_0\in\mathcal C_{u,v}\), let \(K=C_0^\top R\), and choose any unit vector \(a\perp v\). Put \(b=v\times a\) and
\[
z=\lambda\bigl(a^\top K a+i\,b^\top K a\bigr),\qquad h=|\{H\in\mathcal C:Hv=v\}|.
\]
The matrix \(K\) fixes \(v\); thus \(z=\lambda e^{i\delta}\), where \(\delta\) is its oriented rotation angle about \(v\). One always has \(h\in\{1,2,3,4\}\), and the **necessary and sufficient** condition is
\[
\boxed{\quad\mathcal E_{p,u,R}\in\operatorname{conv}\{\operatorname{Ad}_U:U\text{ is a single-qubit Clifford}\}\quad\Longleftrightarrow\quad z\in\operatorname{conv}\{e^{2\pi i j/h}:0\le j<h\}.\quad}
\]
In purely real inequalities the right side is:

- \(h=1\): \(z=1\).
- \(h=2\): \(\Im z=0\) and \(|\Re z|\le1\).
- \(h=3\): \(\Re z\ge-\tfrac12\) and \(\Re z+\sqrt3|\Im z|\le1\).
- \(h=4\): \(|\Re z|+|\Im z|\le1\).

The stabilizer orders correspond respectively to a generic axis, a face-diagonal axis, a body-diagonal axis, and a coordinate axis of the Bloch-sphere cube. Changing \(C_0\) multiplies \(z\) by an \(h\)-th root of unity and cannot change membership. No exception is excluded at \(p=0\), \(p=\frac12\), or \(p=1\).

**Corollary (strict tilted-axis exclusion for a non-Clifford phase gate).** Suppose \(R=R_z(\vartheta)\) with \(\vartheta\notin\frac\pi2\mathbb Z\) and \(0<p<1\). Then
\[
\boxed{\mathcal E_{p,u,R}\text{ is a Clifford-unitary mixture}\quad\Longleftrightarrow\quad u=\pm(0,0,1),\quad |1-2p|(|\cos\vartheta|+|\sin\vartheta|)\le1.}
\]
In particular, every genuinely tilted dephasing axis has **no** Clifford-only unitary unraveling at any strictly intermediate error probability. The endpoint \(p=1\) must not be included in this exclusion: special tilted axes can compose with the phase gate to give a Clifford unitary.

**Corollary (threefold body-diagonal transition).** For \(R=I\) and \(u=(1,1,1)/\sqrt3\), the channel is a Clifford-unitary mixture exactly when \(0\le p\le\frac34\). By contrast, if \(u\) is any face-diagonal or coordinate axis, \(R=I\) produces a Clifford-unitary mixture for every \(0\le p\le1\).

## Assumptions and scope

The channel is the **unmodified**, trace-preserving, random-unitary qubit channel specified above; the noise is conjugation by one fixed Hermitian involution \(u\cdot\sigma\) with probability \(p\), **after** the unitary \(U_R\). A Clifford-only unraveling means a finite probability distribution of **unitary** Clifford gates whose channels average to exactly \(\mathcal E_{p,u,R}\), with arbitrary global phases disregarded. Nonunitary stabilizer instruments, changes to the physical channel such as twirling, and approximate decompositions are not included. All directions are physical unit vectors, and all angle conditions use real radians.

## Proof

**1. Bloch action and pure-direction rigidity.** The Bloch matrix is
\[
M=(\lambda I_3+(1-\lambda)uu^\top)R,\qquad \lambda=1-2p.
\]
Consequently \(Mv=u\) for \(v=R^\top u\). Suppose \(M=\sum_j t_j C_j\) with \(t_j>0\), \(\sum_jt_j=1\), and \(C_j\in\mathcal C\). Each \(C_jv\) has norm one, and \(u=\sum_jt_jC_jv\) also has norm one. Equality in the strict Euclidean triangle inequality forces \(C_jv=u\) for every positive-weight summand. Thus every contributing matrix belongs to \(\mathcal C_{u,v}\). In particular, an empty such set proves impossibility. This is the pure-state rigidity mechanism also used in Lemma 7 of Fioroni–Ferrari–Tirrito.

**2. One cyclic coset.** If \(C_0v=u\), the set of allowed Clifford matrices is exactly \(C_0H_v\), where \(H_v=\{H\in\mathcal C:Hv=v\}\). Any rotation fixing the oriented vector \(v\) acts as a planar rotation on \(v^\perp\); hence \(H_v\) is a finite cyclic subgroup of \(SO(2)\). Its possible orders are \(1,2,3,4\): a signed-permutation rotation axis of order greater than one is either a face diagonal (a half-turn), a body diagonal (a third-turn), or a coordinate axis (a quarter-turn). Those descriptions also prove that every listed order occurs.

**3. Reduction to a polygon.** Since \(Rv=C_0v=u\), the matrix \(K=C_0^\top R\) fixes \(v\). Direct calculation gives
\[
C_0^\top M=\lambda K+(1-\lambda)vv^\top=vv^\top+\lambda K(I_3-vv^\top).
\]
Relative to the right-handed orthonormal basis \((a,b,v)\), the matrix has a scalar \(1\) along \(v\) and the planar block \(\lambda R_2(\delta)\). Each \(H\in H_v\) has blocks \(1\) and \(R_2(2\pi j/h)\) for one integer \(j\in\{0,\ldots,h-1\}\). The equation \(C_0^\top M=\sum_jt_jH_j\) is therefore equivalent to the two real scalar equations that make \(\lambda e^{i\delta}\) a convex combination of the \(h\)-th roots of unity. This proves both directions, including explicit existence through barycentric polygon weights whenever the criterion holds. The four displayed inequality systems are the elementary half-space or segment descriptions of these polygons.

**4. Independence of the coset representative.** Another choice is \(C_0'=C_0H_s\) with \(H_s\in H_v\), so \((C_0')^\top R=H_s^\top K\); its complex planar coefficient differs by an \(h\)-th root of unity. The regular polygon is invariant under such multiplication. Independence of the transverse basis follows because all matrices involved are planar rotations commuting on \(v^\perp\).

**5. Non-Clifford phase rotations.** If \(0<p<1\), then \(|\lambda|<1\), so the point polygon \(h=1\) cannot contain \(z\). Therefore \(v\) is one of the finitely many coordinate, face-diagonal, or body-diagonal symmetry axes; the existence of \(C_0\) forces \(u\) to be a symmetry axis of the same type. For any fixed nonzero third coordinate, the possible azimuthal angles of axes in each of these three orbits differ by multiples of \(\pi/2\). The same statement holds for nonvertical axes with third coordinate zero. Because \(u=R_z(\vartheta)v\), a rotation \(\vartheta\notin\frac\pi2\mathbb Z\) cannot match such two axes unless both equal \(\pm e_z\). For \(u=\pm e_z\) choose \(C_0=I\), yielding \(h=4\) and \(z=\lambda e^{i\vartheta}\); the diamond inequalities give the stated equivalence. This argument does not apply to \(p=1\), when \(|\lambda|=1\) permits isolated generic-axis Clifford compositions.

**6. Threefold boundary.** For \(R=I\) the choice \(C_0=I\) gives \(z=1-2p\). On the real axis the triangle for \(h=3\) is the interval \([-\tfrac12,1]\). This is precisely \(p\le\frac34\). The \(h=2\) segment and \(h=4\) square contain every real \(z\in[-1,1]\), proving the remaining assertion.

## Verification

Run `python3 artifacts/verify_polygon.py` after installing the two packages listed in `requirements.txt`. The verifier enumerates all 24 determinant-one signed permutation matrices. On 88 finite cases covering generic and all three special axis types, phase-rotated axes, negative \(\lambda\), and endpoint probabilities, it independently tests membership of the **full 24-vertex polytope** by linear programming and compares this decision to the four exact polygon conditions. It prints `VERIFY_OK 88 LP-vs-polygon cases; 24 Clifford rotations`. These numerical checks are reproducibility aids; no finite list proves the universal theorem, which follows from the foregoing argument.

## Relationship to prior work

Fioroni, Ferrari, and Tirrito (arXiv:2609.16160v1, Section IV C and Appendix C) developed the tilted-dephasing channel, proved the **pure-direction rigidity** and circle-moment reduction, and solved the cost optimization numerically for generic angles; these facts are prior results, not contributions claimed here. Their reported aligned-axis classical region is also prior. The distinction here is the finite Clifford subgroup reduction yielding a complete **if-and-only-if** polygon classification for arbitrary rotation and arbitrary axis, plus the exact generic-angle exclusion and threefold threshold. Virmani–Huelga–Plenio previously obtained exact dephasing thresholds for diagonal non-Clifford gates by the stabilizer octahedron; those aligned thresholds are included here only as an explicitly prior-known limiting case. Buhrman and coauthors developed the full Clifford rotation polytope for depolarizing-noise thresholds; their general polytope membership formulation is not itself a classification of the purity-preserving tilted-dephasing section by stabilizer order.

## Limitations

This result determines **existence**, not a general nonzero minimum average non-Clifford cost, and does not classify nonunitary stabilizer-operation decompositions. Even a Clifford-only unitary decomposition for a single qubit channel does not on its own prove a hardware fault-tolerance threshold or an arbitrary-circuit runtime bound. The full-rotation theorem covers one noise axis and one preceding qubit unitary; it does not cover general nonunital or time-dependent channels. Originality remains subject to the possibility of a differently indexed exact face characterization of the known Clifford polytope.

## References

1. L. Fioroni, F. Ferrari, E. Tirrito, *Noise-induced classical phases in optimally-unraveled random quantum circuits*, arXiv:2609.16160v1 (first public 2026-09-14), Section IV C and Appendix C. https://arxiv.org/abs/2609.16160
2. S. Virmani, S. F. Huelga, M. B. Plenio, *Classical simulability, entanglement breaking, and quantum computation thresholds*, arXiv:quant-ph/0408076 (2004), Section IV, especially Lemmas 1–2. https://arxiv.org/abs/quant-ph/0408076
3. H. Buhrman, R. Cleve, M. Laurent, N. Linden, A. Schrijver, F. Unger, *New Limits on Fault-Tolerant Quantum Computation*, FOCS (2006), Sections 2.3 and 3. https://ir.cwi.nl/pub/12635/12635D.pdf
