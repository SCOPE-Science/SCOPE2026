# Projective stabilizer of the unique free two-conic three-line arrangement
## Finding
Let \(\mathcal{CL}_7\subset\mathbb P^2_{\mathbb C}\) be the corrected Dimca–Pokora arrangement
\[
(x^2+y^2-z^2)(x^2+y^2-4z^2)(x-z)
\left(y+\frac{\sqrt3}{3}x+\frac{2\sqrt3}{3}z\right)
\left(y-\frac{\sqrt3}{3}x-\frac{2\sqrt3}{3}z\right)=0.
\]
Its full projective automorphism group is
\[
\operatorname{Aut}_{\mathbb P^2}(\mathcal{CL}_7)\cong D_3\cong S_3.
\]
The group has order \(6\), fixes the two conic components individually, and acts faithfully as the full permutation group on the three line components. Its eight singular points form exactly three orbits: three line–inner-conic tacnodes, three ordinary triple points on the outer conic, and two conic–conic tacnodes at infinity. The order-three subgroup fixes each infinite tacnode, whereas each reflection swaps the two.

## Assumptions and scope
The base field is \(\mathbb C\), and “projective automorphism” means an element of \(\operatorname{PGL}_3(\mathbb C)\) preserving the reduced divisor \(\mathcal{CL}_7\). The equation is the corrected equation published by Dimca and Pokora. Their classification proves that this configuration is unique up to projective transformation among free arrangements of two smooth conics and three lines with five tacnodes and three ordinary triple points. The claim here concerns the stabilizer of that unique projective class and its action on the singular set; it does not assert a new freeness classification.

For exact arithmetic, put \(Y=\sqrt3\,y\). The components then become
\[
C_1:3x^2+Y^2-3z^2=0,\qquad C_2:3x^2+Y^2-12z^2=0,
\]
with lines
\[
L_1:x-z=0,\qquad L_2:x+Y+2z=0,\qquad L_3:-x+Y-2z=0.
\]

## Proof
A projective automorphism preserves component degree, so it permutes the two conics and separately permutes the three lines. The conics are intrinsically distinguishable inside the divisor: each of the three lines is tangent to \(C_1\), whereas each is secant to \(C_2\). Therefore every projective automorphism fixes \(C_1\) and \(C_2\) individually.

The three tangency points on \(C_1\) are
\[
[1:0:1],\qquad [1:3:-2],\qquad [1:-3:-2]
\]
in \((x,Y,z)\)-coordinates. Restriction to \(C_1\cong\mathbb P^1\) gives a homomorphism from the projective stabilizer to the permutation group of these three points. Its kernel is trivial: an automorphism of \(\mathbb P^1\) fixing three points is the identity, and a projective transformation of \(\mathbb P^2\) fixing a nondegenerate conic pointwise is scalar. Hence
\[
\operatorname{Aut}_{\mathbb P^2}(\mathcal{CL}_7)\hookrightarrow S_3.
\]

The upper bound is attained. In \((x,Y,z)\)-coordinates define
\[
R=\begin{pmatrix}-\frac12&-\frac12&0\\[2pt]\frac32&-\frac12&0\\0&0&1\end{pmatrix},
\qquad
S=\begin{pmatrix}1&0&0\\0&-1&0\\0&0&1\end{pmatrix}.
\]
Both preserve \(C_1\) and \(C_2\). Direct substitution gives
\[
L_1\circ R=-\frac12L_2,\qquad L_2\circ R=-L_3,\qquad L_3\circ R=2L_1,
\]
and \(S\) fixes \(L_1\) while interchanging \(L_2\) and \(L_3\) up to scalar. Moreover \(R^3=S^2=1\) and \(SRS=R^{-1}\). Thus \(R\) and \(S\) generate a subgroup \(D_3\) of order \(6\). The injection above forces this subgroup to be the full projective automorphism group.

The singular orbits follow directly. The three points above are the simple tangencies of the line components with \(C_1\), so they are tacnodes and form one orbit. The three line-line vertices
\[
[-2:0:1],\qquad [1:-3:1],\qquad [1:3:1]
\]
lie on \(C_2\); the three branches there have distinct tangents, so they are ordinary triple points, again one orbit. Finally, \(C_2-C_1=-9z^2\), so the two conics meet only at
\[
[1:i:0],\qquad [1:-i:0]
\]
in the original \((x,y,z)\)-coordinates, each with intersection multiplicity \(2\), hence as conic–conic tacnodes. The rotation \(R\) fixes each of these two projective points, while \(S\) swaps them. The pairwise Bézout count is exhausted by five tacnodes and three triple points:
\[
4+12+3=19=5\cdot2+3\cdot3,
\]
so there are no additional singular points.

## Verification
The accompanying exact-arithmetic script `artifacts/verify.py` checks the dihedral relations, preservation of both conics, permutation of all three line equations, tangency at the three finite tacnodes, transitivity on the two size-three singular orbits, the ordinary-triple transversality tests, the two conic intersections at infinity, and the complete Bézout count. It uses only Python’s standard library and returns `VERIFY_OK`.

## Relationship to prior work
Dimca and Pokora classify the relevant free conic-line arrangements and prove that the case with two conics, three lines, five tacnodes and three ordinary triple points has a unique projective-equivalence class. They normalize the two conics to concentric circles and deduce that the associated triangle is equilateral with outer radius twice the inner radius. Their corrected publication supplies the equation used here. The source does not determine the full projective stabilizer or its singular-orbit decomposition. The new point is therefore the exact stabilizer of the unique class, not the already-known equilateral realization or freeness.

## Limitations
The result concerns only the corrected \(\mathcal{CL}_7\) projective-equivalence class over \(\mathbb C\). It does not classify automorphism groups of other free or nearly free conic-line arrangements, and it does not address automorphisms of the complement that fail to extend to \(\mathbb P^2\). The literature search found no published computation of this stabilizer, but an obscure source using different notation could still exist.

## References
A. Dimca and P. Pokora, “On conic-line arrangements with nodes, tacnodes, and ordinary triple points,” Journal of Algebraic Combinatorics 56 (2022), 403–424; arXiv:2111.12349; DOI: 10.1007/s10801-022-01116-3.

A. Dimca and P. Pokora, “Correction: On conic-line arrangements with nodes, tacnodes, and ordinary triple points,” Journal of Algebraic Combinatorics 56 (2022), 1339; DOI: 10.1007/s10801-022-01151-0.
