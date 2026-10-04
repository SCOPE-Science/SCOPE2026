# A \(7A_1+3A_3\) Hessian quartic at the exceptional \(3A_1\) cubic parameters
## Finding
Let \(\rho\in\mathbb C\) satisfy
\[
9\rho^2-14\rho+9=0,
\]
and let
\[
f_\rho=x_4(x_2^2-x_1x_3)+x_2^2\bigl(x_1-(1+\rho)x_2+\rho x_3\bigr).
\]
Write \(H_\rho(x)=\operatorname{Hess}(f_\rho)(x)\) and
\[
Y_\rho=V\!\left(\det H_\rho\right)\subset\mathbb P^3.
\]
Then \(Y_\rho\) has exactly ten singular points. Seven are rational double points of type \(A_1\) and three are rational double points of type \(A_3\).

More precisely, the rank-at-most-two degeneracy scheme of \(H_\rho\) has length ten but support seven. It is the disjoint union of four reduced points
\[
Q_1=(-\rho:0:1:0),\quad Q_2=(0:1:0:0),\quad Q_3=(0:0:1:-\rho),\quad Q_4=(1:0:0:-1)
\]
and three curvilinear length-two schemes supported at
\[
P_1=(\rho:x_0:1:0),\qquad P_2=(0:x_0:1:\rho),\qquad P_3=(1:y_0:0:1),
\]
where
\[
x_0=\frac{3(\rho+1)}8,\qquad y_0=\frac{23}{24}-\frac{3\rho}{8}.
\]
The three points \(P_i\) are exactly the \(A_3\) singularities. The four points \(Q_i\), together with the three nodes
\[
E_1=(1:0:0:0),\qquad E_3=(0:0:1:0),\qquad E_4=(0:0:0:1)
\]
of the cubic surface \(V(f_\rho)\), are exactly the seven \(A_1\) singularities of \(Y_\rho\).

Thus the collision of the ten generic rank-two Hessian points on the exceptional parameter divisor does not merely reduce the support from ten to seven: each of the three colliding pairs upgrades an ordinary Hessian node to an \(A_3\) singularity, while the three nodes of the cubic itself contribute three additional ordinary nodes of the Hessian quartic.

## Assumptions and scope
Everything is over \(\mathbb C\). The parameter equation has two roots, neither equal to \(0\) or \(1\), so the displayed cubic remains in the \(3A_1\) normal-form family. The statement concerns the projective Hessian quartic and the scheme cut out by the \(3\times3\) minors of its Hessian matrix. It does not classify nearby deformations, global resolutions, or the Néron--Severi lattice.

Seigal--Sukarto give this normal form and prove that the \(3\times3\)-minor ideal decomposes into four reduced points and three degree-two pieces. They identify \(9\rho^2-14\rho+9=0\) as precisely the parameter condition under which those ten generic points cease to be distinct, while the cubic remains of type \(3A_1\). The result here starts from that published decomposition and determines the scheme collision and the complete analytic singularity basket of the Hessian quartic at the exceptional parameters.

## Proof
Set
\[
\Delta(\rho)=9\rho^2-14\rho+9.
\]
The three degree-two pieces in the published decomposition are parameterized by
\[
(\rho:x:1:0),\qquad(0:x:1:\rho),\qquad(1:y:0:1),
\]
with
\[
4x^2-3(\rho+1)x+2\rho=0,
\qquad
4\rho y^2-3(\rho+1)y+2=0.
\]
Both discriminants equal \(\Delta(\rho)\). Hence, on \(\Delta(\rho)=0\), the first two quadratics have the double root \(x_0=3(\rho+1)/8\), while the third has the double root \(y_0=3(\rho+1)/(8\rho)=23/24-3\rho/8\). Their leading coefficients are nonzero, so each defines a curvilinear length-two subscheme. Together with the four reduced points \(Q_i\), the rank-at-most-two degeneracy scheme therefore has length \(4+3\cdot2=10\) and support seven.

Every rank-at-most-two point of the symmetric \(4\times4\) matrix \(H_\rho(x)\) is singular on \(Y_\rho\), because its adjugate vanishes. It remains to determine possible singular points where \(H_\rho(x)\) has rank three. Let \(k\) span the kernel of such a matrix. Since \(H_\rho(x)\) is symmetric, its adjugate has the form \(c kk^{\mathsf T}\) with \(c\ne0\). If \(T\) denotes the constant symmetric third-derivative tensor of the cubic, then for every tangent direction \(v\),
\[
\mathrm d(\det H_\rho)_x(v)
 =c\,k^{\mathsf T}H_\rho(v)k
 =c\,T(k,k,v).
\]
For a homogeneous cubic, \(T(k,k,v)=2\,\mathrm df_\rho|_k(v)\). Thus a rank-three point of \(Y_\rho\) can be singular only if \([k]\) is a singular point of \(V(f_\rho)\). The normal form has exactly the three nodes \(E_1,E_3,E_4\). Directly solving \(H_\rho(x)E_i=0\) gives a unique projective solution \(x=E_i\) for each \(i\). Therefore the singular locus of \(Y_\rho\) consists exactly of the seven rank-drop support points plus \(E_1,E_3,E_4\), hence exactly ten points.

It remains to classify their analytic types. Write \(h_\rho=\det(H_\rho)/4\). At \(P_1\), in the affine chart \(x_3=1\) with
\[
x_1=\rho+u,\qquad x_2=x_0+v,\qquad x_4=w,
\]
the quadratic part is
\[
\frac{\rho}{2}(u-w)(u+w).
\]
It has corank one with kernel coordinate \(v\). Solving the two transverse critical equations formally through cubic order and substituting back gives a one-variable reduced germ whose first nonzero term is
\[
8\rho\,v^4.
\]
Since \(\rho\ne0\), the splitting lemma gives type \(A_3\). The same calculation at \(P_2\) again gives reduced fourth-order coefficient \(8\rho\). At \(P_3\), after choosing the kernel coordinate along \(x_2\), the quadratic part is
\[
-\frac{9\rho u^2+(9\rho-14)w^2}{18},
\]
and the reduced fourth-order coefficient is again \(8\rho\). Hence all three \(P_i\) are \(A_3\).

At each \(Q_i\), the quadratic part of the local equation is nondegenerate. Exact determinants of the corresponding quadratic Hessians are, respectively,
\[
-\frac{8(476\rho-1035)}{729},\quad
-\frac{32(14\rho-9)}9,\quad
-\frac{8(476\rho-1035)}{729},\quad
-8.
\]
Neither linear factor can vanish simultaneously with \(\Delta(\rho)\), so these four points are \(A_1\). At \(E_1,E_3,E_4\), the local quadratic forms are nondegenerate as well; representatives are
\[
u^2-vw,
\qquad
-\frac{9\rho uw+(9-14\rho)v^2}{9},
\qquad
-uw+v^2,
\]
with nonzero quadratic Hessian determinants. Hence the three additional singular points are also \(A_1\). This proves the basket \(7A_1+3A_3\).

## Verification
The accompanying exact symbolic checker `verify.py` works in \(\mathbb Q[\rho]/(9\rho^2-14\rho+9)\). It reconstructs \(f_\rho\), its Hessian matrix, and the Hessian quartic; verifies the two double-root identities; checks all \(3\times3\) minors at the seven rank-drop support points; computes the corank-one quadratic forms and splitting-lemma fourth-order coefficients at the three \(P_i\); checks nondegeneracy at the four \(Q_i\) and the three cubic nodes; and verifies that the kernel-incidence equations at the three cubic nodes have unique projective solutions. Its terminal output is `VERIFY_OK`. The complete replay output is included in `verification_output.txt`.

The checker verifies the new local and exhaustion calculations. The published decomposition of the full \(3\times3\)-minor ideal is used as a literature premise rather than recomputed from a primary decomposition package.

## Relationship to prior work
Seigal--Sukarto identify the same \(3A_1\) family, the four fixed points and three degree-two pieces of the Hessian rank-drop scheme, and the exceptional condition \(9\rho^2-14\rho+9=0\). They state that the ten points are then not distinct and that the cubic remains of type \(3A_1\). They do not determine the resulting length-two scheme structure, the singularity types of the Hessian quartic, or the three additional rank-three Hessian singularities. Their results on the Salmon invariant also place these exceptional cubics on the rank-greater-than-five Hessian discriminant; that rank consequence is prior context, not part of the originality claim here.

Dardanelli--van Geemen study Hessians of cubic surfaces and the non-Sylvester strata, including general singular cubics, but their treatment does not give this exceptional \(3A_1\) local basket. Koike studies Hessian K3 surfaces of non-Sylvester type and gives a singularity analysis for a general non-Sylvester family on its smooth parameter locus; it likewise does not identify the present three-pair collision or a \(7A_1+3A_3\) quartic.

Targeted published-record searches for the exact \(3A_1\) Hessian-discriminant condition, non-Sylvester three-nodal Hessians, and a \(7A_1+3A_3\) Hessian quartic produced no statement implying this result. The closest retrieved records concerned unrelated Hessian calculations or unrelated surface singularities.

## Limitations
The proof relies on the published primary decomposition of the \(3\times3\)-minor ideal for the \(3A_1\) family. The new checker independently verifies the special-point incidence and local analytic calculations but does not recompute that entire primary decomposition from scratch. The claim is over \(\mathbb C\) and is specific to the two roots of \(9\rho^2-14\rho+9\). No assertion is made about the minimal resolution lattice, monodromy of the degeneration, or whether an older classification under different coordinates records an equivalent ADE basket. That last possibility remains the principal originality risk.

## References
1. Anna Seigal and Eunice Sukarto, *Ranks and Singularities of Cubic Surfaces*, arXiv:1909.12538, first posted 2019-09-27. See the \(3A_1\) normal form, the rank-five decomposition condition, and the Hessian-discriminant example in Sections 3--4.
2. Elisa Dardanelli and Bert van Geemen, *Hessians and the moduli space of cubic surfaces*, arXiv:math/0409322.
3. Kenji Koike, *Hessian K3 surfaces of non-Sylvester type*, arXiv:1006.3617.
