# The symplectic jumping divisor of twisted-cubic restrictions of a uniform rank-nine bundle

## Finding
Let \(V=\mathbb C^6\) with basis \(e_x,e_y,e_z,e_t,e_u,e_v\) and nondegenerate bivector
\[\pi=e_x\wedge e_y-e_z\wedge e_t+e_u\wedge e_v.\]
Set \(W=\ker(\bigwedge^2 V^*\xrightarrow{\langle-,\pi\rangle}\mathbb C)\). Define the rank-nine vector bundle \(E\) on \(\mathbb P(V)\) by the evaluation sequence
\[0\longrightarrow E(-1)\longrightarrow W\otimes\mathcal O_{\mathbb P(V)}\longrightarrow\Omega^1_{\mathbb P(V)}(2)\longrightarrow0.\]
This is the hyperplane-of-Koszul-sections presentation of the uniform non-homogeneous bundle of Denham–Miró-Roig–Schenck [1, Theorem 3.3], with its displayed fourteen-column matrix.

For **every** smooth twisted cubic \(C\subset\mathbb P(V)\), let \(\mathbb P(U)=\langle C\rangle\cong\mathbb P^3\), and put \(A=\operatorname{Ann}(U)\subset V^*\) (a two-plane). Identifying \(C\cong\mathbb P^1\), the complete splitting is
\[
E|_C\cong\begin{cases}
\mathcal O_{\mathbb P^1}(2)^{\oplus6}\oplus\mathcal O_{\mathbb P^1}(1)^{\oplus3},&\pi|_{\wedge^2A}\ne0,\\
\mathcal O_{\mathbb P^1}(3)\oplus\mathcal O_{\mathbb P^1}(2)^{\oplus4}\oplus\mathcal O_{\mathbb P^1}(1)^{\oplus4},&\pi|_{\wedge^2A}=0.
\end{cases}
\]
Both types occur. The exceptional span locus is the seven-dimensional smooth symplectic isotropic Grassmannian \(\operatorname{IG}(2,V^*)\) inside \(\operatorname{Gr}(2,V^*)\cong\operatorname{Gr}(4,V)\); it is a Plücker hyperplane section and thus a divisor. The answer depends only on the linear span of \(C\), not on the parametrization or projective shape of \(C\) within that span.

## Assumptions and scope
The base field is \(\mathbb C\). A smooth twisted cubic means a nondegenerate degree-three rational normal curve in its unique linear span \(\mathbb P^3\subset\mathbb P^5\). All twists \(\mathcal O_C(a)\) in the displayed splitting are intrinsic line bundles of degree \(a\) on \(C\simeq\mathbb P^1\); the ambient hyperplane bundle restricts as \(\mathcal O_{\mathbb P^5}(1)|_C\simeq\mathcal O_C(3)\). The symplectic condition is on the annihilator \(A\) in the dual six-space with alternating form defined by \(\pi\). The assertion concerns smooth twisted cubics and this specific symplectic hyperplane bundle, not arbitrary rational cubics or arbitrary uniformly split bundles.

## Proof
**1. The symplectic quotient sequence.** The exterior-square Euler sequence identifies the kernel of the full Koszul evaluation:
\[0\to\Omega^2_{\mathbb P(V)}(2)\to\bigwedge^2V^*\otimes\mathcal O\to\Omega^1_{\mathbb P(V)}(2)\to0.\]
Taking the hyperplane \(W=\ker\langle-,\pi\rangle\) gives
\[0\to E(-1)\to\Omega^2_{\mathbb P(V)}(2)\xrightarrow{\varphi_\pi}\mathcal O\to0.\tag{1}\]
The right map is surjective: if its fiber vanished at \([v]\in\mathbb P(V)\), the five-dimensional annihilator \(\operatorname{Ann}(v)\subset V^*\) would be isotropic for the nondegenerate alternating form \(\pi\), impossible because the maximal isotropic dimension is three. Thus all terms are vector bundles of the asserted ranks.

**2. Restriction to a twisted cubic.** Fix \(C\) with span \(\mathbb P(U)\). Restricting the Euler sequence to this linear \(\mathbb P^3\) splits off the two conormal directions \(A\), so
\[\Omega^1_{\mathbb P(V)}(1)|_C\cong\Omega^1_{\mathbb P(U)}(1)|_C\oplus (A\otimes\mathcal O_C).\]
Choose homogeneous parameters \([s:t]\) for the rational normal cubic \([s^3:s^2t:st^2:t^3]\). The Euler kernel \(\Omega^1_{\mathbb P(U)}(1)|_C\) has the three independent linear syzygies \((-t,s,0,0)\), \((0,-t,s,0)\), \((0,0,-t,s)\). Thus it is \(\mathcal O_C(-1)^{\oplus3}\), and
\[\Omega^2_{\mathbb P(V)}(2)|_C\cong\mathcal O_C(-2)^{\oplus3}\oplus\mathcal O_C(-1)^{\oplus6}\oplus\mathcal O_C.\tag{2}\]
The map from the last trivial summand in (2) to the right side of (1) is multiplication by the scalar \(\pi|_{\wedge^2 A}\).

**3. Nonisotropic case.** If \(\pi|_{\wedge^2 A}\ne0\), the trivial summand in (2) maps isomorphically to \(\mathcal O_C\). Hence by (1)
\[E(-1)|_C\cong\mathcal O_C(-2)^{\oplus3}\oplus\mathcal O_C(-1)^{\oplus6}.\]
Since \(\mathcal O_{\mathbb P(V)}(1)|_C=\mathcal O_C(3)\), twisting by \(\mathcal O_C(3)\) gives the first formula.

**4. Isotropic case and the only delicate cohomology step.** Suppose \(\pi|_{\wedge^2A}=0\). The trivial summand in (2) maps to zero, so \(h^0(C,E(-1)|_C)=1\). Twist (1) by the intrinsic \(\mathcal O_C(1)\). By (2), the space of sections of its middle term has dimension \(6+2=8\). We claim the map of these sections onto \(H^0(C,\mathcal O_C(1))\) is surjective.

Indeed, the cross term \(\Omega^1_{\mathbb P(U)}(1)|_C\otimes A\cong\mathcal O_C(-1)^{\oplus6}\) maps to \(\mathcal O_C\) by pairing the vectors of \(A\) with the \(U\)-part of \(\pi\). The symplectic isomorphism \(\pi^\sharp:V^*\to V\) sends \(A\) injectively into \(U=\operatorname{Ann}(A)\), because \(A\) is isotropic. Its image is therefore two-dimensional. At any \(p\in C\), with corresponding line \(\ell_p\subset U\), if this cross-term map vanished on the fiber, then \(\pi^\sharp(A)\) would annihilate every covector in \(\operatorname{Ann}_{U^*}(\ell_p)\), forcing \(\pi^\sharp(A)\subset\ell_p\), an impossibility. The six coefficient sections of \(\mathcal O_C(1)\) coming from this cross term therefore have no common zero. Because their degree is one on \(\mathbb P^1\), they necessarily span the two-dimensional space \(H^0(C,\mathcal O_C(1))\). This proves surjectivity and
\[h^0(C,E(-1)|_C\otimes\mathcal O_C(1))=8-2=6.\tag{3}\]
The same equality also holds in the nonisotropic case by the explicit splitting in step 3.

**5. Recovering the complete splitting.** From [1, Theorem 3.3 and Lemma 3.1], \(E\) and \(E^\vee(1)\) are globally generated, its rank is nine, and \(c_1(E)=5\). Every intrinsic splitting degree \(a_i\) of \(E|_C\) therefore satisfies \(0\le a_i\le3\), with \(\sum a_i=15\). Write \(t,s,r,z\) for the multiplicities of degrees \(3,2,1,0\). Then
\[t=h^0(E|_C(-3))\in\{0,1\},\qquad 2t+s=h^0(E|_C(-2))=6,\]
\[3t+2s+r=15,\qquad t+s+r+z=9.\]
The unique solution is \((t,s,r,z)=(0,6,3,0)\) in the nonisotropic case and \((1,4,4,0)\) in the isotropic case. This yields both asserted formulas, for every such curve, without an assumption of general position.

**6. Geometry of the jumping locus.** The annihilator map identifies four-planes \(U\subset V\) with two-planes \(A\subset V^*\). The exceptional condition \(\pi|_{\wedge^2 A}=0\) is the usual symplectic isotropy Plücker equation. Its zero locus \(\operatorname{IG}(2,6)\) is a smooth nonempty hyperplane section of \(\operatorname{Gr}(2,6)\), of dimension seven rather than eight. For example, \(\mathbb P(\langle e_x,e_y,e_z,e_t\rangle)\) has nonisotropic annihilator, while \(\mathbb P(\langle e_x,e_y,e_z,e_u\rangle)\) has isotropic annihilator. Either projective three-space contains smooth twisted cubics. This proves both occurrences and the exact jump divisor.

## Verification
The standalone `verify.py` checks the fourteen signed Koszul columns from [1], their Euler identities, and the two cohomology dimensions for the fifteen coordinate four-planes using exact rational Gaussian elimination. It finds three nonisotropic coordinate planes with section dimensions \((0,6)\) and twelve isotropic coordinate planes with dimensions \((1,6)\) for \((h^0(E|_C(-3)),h^0(E|_C(-2)))\). These are finite consistency checks, **not** the proof for the infinite family; that is the vector-bundle argument above. An additional independent check of the linear syzygy space finds fourteen linear global syzygies and evaluation rank nine at a coordinate point, consistent with the globally generated premise and symplectic transitivity.

## Relationship to prior work
Denham, Miró-Roig and Schenck [1] exhibit the fourteen Koszul sections and prove that the resulting rank-nine bundle is globally generated, uniform on every projective line, and non-homogeneous; their paper does not determine restriction types on twisted cubics. Landsberg and Manivel [2, §6.2] describe the related symplectic rank-nine constant-rank matrix construction and its homogeneous symmetry under the symplectic group. In fact the bundle defined there as a quotient of \(\bigwedge^2 Q\) by the symplectic section is the dual twist \(E^\vee(1)\), as follows by dualizing (1); thus it is essential to compare that source, not regard it as unrelated. Its results describe the rank-nine bundle and symplectic structure but do not state the present two twisted-cubic splitting formulas or the codimension-one jumping criterion. Fantechi and Miró-Roig [3] give general moduli theory of generalized syzygy bundles, without this curve-restriction classification.

Previously recorded investigations of the same hyperplane bundle deal with a rank-four bivector's jumping lines and with restrictions to projective planes. Neither determines the restriction to a nondegenerate twisted cubic, which spans a projective three-space; the present jumping divisor is the symplectic isotropic two-plane Grassmannian rather than the Lagrangian three-plane Grassmannian. The result is a specific new curve-restriction invariant, not a claim that the underlying symplectic construction is new.

## Limitations
The theorem concerns complex smooth rational normal cubics and the symplectic hyperplane bundle. It does not classify singular rational cubics, higher-degree curves, other deformations of the bundle, or restrictions over positive characteristic. The jumping locus is asserted for the spanning four-plane and as a set of smooth curves above that span, not as a newly analyzed nonreduced Hilbert-scheme determinantal structure. Independent audit has not been performed. Since existing general symplectic bundle descriptions could conceivably have unstated consequences for twisted cubics, the absence of an exact published classification remains a qualified literature conclusion, not a uniqueness theorem.

## References
[1] G. Denham, R. M. Miró-Roig, H. Schenck, *Uniform non-homogeneous vector bundles: A counterexample to the conjecture of Drézet and Ballico-Ellia*, arXiv:2610.20208v1 (first public 2026-10-14), especially §3, Theorem 3.3, Lemma 3.1 and the printed matrix: https://arxiv.org/pdf/2610.20208.

[2] J. M. Landsberg, L. Manivel, *Equivariant spaces of matrices of constant rank*, arXiv:2212.04228v1 (2022), especially §6.2, Lemma 21, Proposition 22 and the explicit symplectic fourteen-by-fourteen matrix: https://arxiv.org/pdf/2212.04228.

[3] B. Fantechi, R. M. Miró-Roig, *Moduli of generalized syzygy bundles*, arXiv:2306.04317v1 (2023), especially Introduction and the definition of generalized syzygy bundles: https://arxiv.org/pdf/2306.04317.
