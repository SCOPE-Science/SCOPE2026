# Six independent direction classes and the orientation obstruction of quadrangle moduli

## Finding
Let \(\mathcal Q\) be the eight-dimensional Nash manifold of labeled quadrangles defined by Olberding and Walker, and let \(G=\operatorname{Sim}^{+}(\mathbb R^2)\), the group of orientation-preserving Euclidean similarities. The quotient \(B=\mathcal Q/G\) is a smooth Nash manifold of dimension four. For each of the six unordered edges \(e=\{i,j\}\) of the complete graph on four vertices, there is a canonical real line bundle \(\bar\lambda_e\to B\) of normal directions. Put \(u_e=w_1(\bar\lambda_e)\in H^1(B;\mathbb F_2)\). Then
\[
w_1(TB)=\sum_{e}u_e,
\qquad
\dim_{\mathbb F_2}\operatorname{span}\{u_e:e\in E(K_4)\}=6.
\]
In fact, six explicit loops \(\gamma_e\) satisfy \(\langle u_f,[\gamma_e]\rangle=\delta_{ef}\). Consequently \(\dim_{\mathbb F_2}H^1(B;\mathbb F_2)\ge6\) and \(B\) is nonorientable. Upstairs, the six pulled-back direction classes are likewise independent and \(w_1(T\mathcal Q)\) is their sum.

## Assumptions and scope
A labeled quadrangle is a tuple of vertices \(v_1,v_2,v_3,v_4\in\mathbb R^2\) and a projective normal line \(\ell_{ij}\in\mathbb{RP}^1\) for each \(1\le i<j\le4\), such that a representative normal \(n_{ij}\) obeys \(n_{ij}\cdot(v_i-v_j)=0\) and at least three of the resulting six affine lines extend the sides of a nondegenerate triangle. Vertices may coincide in pairs. Let \(A=(\mathbb R^2)^4\times(\mathbb{RP}^1)^6\) and let \(\lambda_{ij}\) be the pullback from the \(ij\)-th \(\mathbb{RP}^1\) of the tautological real line bundle. The connected four-dimensional group \(G\) acts freely and properly on \(\mathcal Q\), as established in the cited initiating article. Its natural linear action on normal vectors makes every \(\lambda_{ij}|_{\mathcal Q}\) equivariant, and hence it descends to \(\bar\lambda_{ij}\) on \(B\). All characteristic classes and cohomology are with \(\mathbb F_2\)-coefficients.

## Proof
**The incidence normal bundle.** On the ambient manifold \(A\), the \(ij\)-th incidence equation \(n_{ij}\cdot(v_i-v_j)=0\) is a globally defined section of \(\lambda_{ij}^{\vee}\): replacing a representative of the projective normal by its negative changes the scalar component accordingly. Therefore the six equations assemble into a section of
\[
E=\bigoplus_{1\le i<j\le4}\lambda_{ij}^{\vee}.
\]
The local Jacobian of this section has constant rank six along \(\mathcal Q\), by the explicit incidence-gradient argument of Olberding--Walker, Lemma 3.1. The nondegenerate-triangle condition is open. Thus on \(\mathcal Q\) there is an exact sequence of real vector bundles
\[
0\longrightarrow T\mathcal Q\longrightarrow TA|_{\mathcal Q}\longrightarrow E|_{\mathcal Q}\longrightarrow0.
\]
Each \(\mathbb{RP}^1\) factor is an oriented circle and each \(\mathbb R^2\) factor is oriented, so \(TA\) is orientable. The Whitney formula, \(w_1(\lambda_{ij}^{\vee})=w_1(\lambda_{ij})\), and additivity of the first class give
\[
w_1(T\mathcal Q)=\sum_{i<j}w_1(\lambda_{ij}|_{\mathcal Q}).
\]

**Descent of the determinant line.** Similarities act on the normal representatives by the inverse transpose of their linear part, so \(E\) and the incidence map above are equivariant. The action of connected \(G\) preserves the orientation of the ambient tangent bundle. Its adjoint action also preserves the orientation of the Lie algebra \(\mathfrak g\), since a connected group has positive adjoint determinant. Hence the equivariant determinant exact sequences for the incidence map and the principal bundle \(\mathcal Q\to B\) show
\[
\det(TB)\simeq\bigotimes_{i<j}\bar\lambda_{ij}
\]
as orientation line bundles (equivalently, after tensoring by canonically orientable lines). Thus \(w_1(TB)=\sum_{i<j}u_{ij}\). This argument takes place equivariantly and does not infer a characteristic class downstairs merely from equality of pullbacks.

**Six dual collision loops.** Fix an unordered edge \(e=\{i,j\}\), and write its complementary vertices as \(k,l\). Place \(v_i=v_j=(0,0)\), \(v_k=(1,0)\), \(v_l=(0,1)\). For every side other than \(e\), use the unique joining line through the two distinct relevant vertex positions. These five lines do not vary. The lines corresponding to \(ik\), \(il\), and \(kl\) form a nondegenerate triangle independently of the missing side. Because the incidence equation for \(e\) is automatic at \(v_i=v_j\), allow its normal line \(\ell_e\) to traverse once around \(\mathbb{RP}^1\). This produces a closed embedded circle in \(\mathcal Q\), and its image \(\gamma_e\) is a closed loop in \(B\). On that circle the bundle \(\lambda_e\) is the Möbius tautological line and the other five \(\lambda_f\) are constant. Pulling back the descended classes through the circle and its quotient map yields
\[
\langle u_f,[\gamma_e]\rangle=
\begin{cases}1&f=e,\\0&f\ne e.\end{cases}
\]
These six evaluations form the identity matrix. Therefore the six classes are independent, both on \(B\) and on \(\mathcal Q\). In particular their sum evaluates to one on each \(\gamma_e\); it is nonzero, making \(B\) and \(\mathcal Q\) nonorientable. \(\square\)

## Verification
The incidence-bundle construction has rank six because it uses the six separate projective normal factors; its zero section is regular on the nondegenerate-triangle open subset by the explicit rank proof in the source. For every collision loop the three fixed vertices form a genuine triangle, so rotating the free side never leaves \(\mathcal Q\), even when that side coincides with another side. The tautological bundle restricted to one complete rotation of \(\mathbb{RP}^1\) has first Stiefel--Whitney evaluation one, whereas the five fixed-direction bundles evaluate to zero. These six exact evaluations establish independence without numerical experiments. The quotient argument uses the connected oriented similarity group, not its disconnected extension including reflections.

## Relationship to prior work
Olberding and Walker construct \(\mathcal Q\), prove regularity of its incidence equations (Lemma 3.1), and show that free proper similarity quotients are Nash manifolds (Section 3). Their treatment develops the form, aspect and sphericity invariants but does not derive the orientation class or independent cohomology classes calculated here. Martin's graph picture spaces use the same point--line incidence type over projective geometry, but his results describe algebraic irreducible components, defining equations, and Cohen--Macaulay phenomena, not the mod-two characteristic class of this real Nash quotient. The characteristic-class and collision-loop arguments here are separate calculations relying on the stated manifold foundations.

## Limitations
Only the six-dimensional subspace of \(H^1(B;\mathbb F_2)\) generated by the direction lines is determined. The full cohomology ring, the exact first Betti number, integral torsion, and the topology of other similarity quotients are not classified. The orientation calculation concerns \(\operatorname{Sim}^{+}(\mathbb R^2)\), not the disconnected full similarity group. Prior literature might contain an implicit incidence-bundle version of this argument; the cited geometric sources do not state this specific quotient computation.

## References
1. B. Olberding and E. A. Walker, *The Nash manifold of four-point configurations modulo similarity subgroups*, arXiv:2610.02087v1 (first public 2026-10-01), especially Definition 2.1, Lemma 3.1, and Section 3.
2. J. L. Martin, *Geometry of graph varieties*, arXiv:math/0302089v1 (2003), *Transactions of the American Mathematical Society* 355, 4151–4169. Background on point--line incidence spaces.
