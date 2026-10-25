# Sharp gyration and midpoint rigidity for equilateral equiangular spatial hexagons

## Finding
Let \(P=(P_0,\ldots,P_5)\) be a closed spatial six-gon with unit edges and the same interior bond angle \(\theta\) at every vertex, with \(0<\theta<2\pi/3\). The vertex radius of gyration is maximized **uniquely up to all Euclidean isometries** by the chair conformation. In particular,
\[
R_g^2(P)\le \sin^2(\theta/2)+\frac14.
\]
The full deficit is exactly the dispersion of the midpoints of the three long diagonals:
\[
\sin^2(\theta/2)+\frac14-R_g^2(P)
=\frac1{18}\sum_{0\le i<j\le2}\|M_i-M_j\|^2,
\qquad M_i=\frac12(P_i+P_{i+3}).
\]
Consequently a deficit at most \(\varepsilon\) forces all opposite-chord midpoint separations to be at most \(\sqrt{18\varepsilon}\). For the ideal tetrahedral angle \(\arccos(-1/3)\), the sharp squared gyration is \(11/12\) in unit-side normalization.

## Assumptions and scope
Indices are taken modulo six, and intersections of nonadjacent sides are permitted. The bond angle is the angle \(\angle P_{i-1}P_iP_{i+1}\). Set
\[
\overline P=\frac16\sum_{i=0}^5P_i,\qquad
R_g^2(P)=\frac16\sum_{i=0}^5\|P_i-\overline P\|^2.
\]
No oriented-embedding or self-avoidance restriction is imposed. Congruence includes reflections. The result is a global extremum over **all** spatial conformations obeying the six length and six bond-angle constraints; it does not assert that the maximizer minimizes molecular energy.

## Proof
**Universal six-point identity.** For an arbitrary six-tuple of points in Euclidean space, put
\[
C_1=\sum_{i=0}^5\|P_i-P_{i+1}\|^2,\qquad
C_2=\sum_{i=0}^5\|P_i-P_{i+2}\|^2,\qquad
D=\sum_{i=0}^2\|P_i-P_{i+3}\|^2.
\]
The standard centroid identity gives \(36R_g^2=C_1+C_2+D\). For four points \(a,b,c,d\), the parallelogram expansion
\[
4\left\|\frac{a+c}{2}-\frac{b+d}{2}\right\|^2
=\|a-b\|^2+\|a-d\|^2+\|c-b\|^2+\|c-d\|^2-\|a-c\|^2-\|b-d\|^2
\]
holds by direct expansion of inner products. Apply it to each pair among the opposite chords \((P_0,P_3)\), \((P_1,P_4)\), \((P_2,P_5)\), and sum. Every edge and every length-two diagonal appears once, while every long diagonal appears twice. Therefore
\[
4\sum_{0\le i<j\le2}\|M_i-M_j\|^2=C_1+C_2-2D.
\]
Solving for \(D\) gives the **general identity**
\[
\boxed{R_g^2=\frac{C_1+C_2}{24}-\frac1{18}\sum_{0\le i<j\le2}\|M_i-M_j\|^2.}
\]
When successive sides are unit and bond angles all equal \(\theta\), the cosine law gives every two-step chord squared equal to \(4\sin^2(\theta/2)\). Thus \(C_1=6\) and \(C_2=24\sin^2(\theta/2)\), proving the stated identity and bound. Equality means \(M_0=M_1=M_2\), or equivalently all three opposite pairs share one center of symmetry.

**Sharpness and equality rigidity.** Put \(z=4\sin^2(\theta/2)\), so \(0<z<3\). Let \(a,b,c\in\mathbb R^3\) have the Gram matrix
\[
G(z)=\frac14\begin{pmatrix}
1+z&z-1&1-z\\
z-1&1+z&z-1\\
1-z&z-1&1+z
\end{pmatrix}.
\]
Its eigenvalues are \(z/2,z/2,(3-z)/4\), hence it is positive definite for the whole stated range. Such vectors exist. Define the closed chair polygon
\[
(P_0,P_1,P_2,P_3,P_4,P_5)=(a,b,c,-a,-b,-c).
\]
The Gram entries imply all six side lengths are one and all six two-step chord lengths squared are \(z\), which by the cosine law is exactly the prescribed bond angle. Its three opposite midpoints all equal zero, so it attains the bound.

Conversely, any equality polygon is centrally symmetric. Translate the common midpoint to the origin and write its vertices in the displayed opposite-pair form. Unit side lengths and two-step chord lengths force the three squared lengths of \(a,b,c\) and their three pairwise inner products to be exactly the displayed Gram matrix. Equality of Gram matrices implies congruence by an orthogonal map, even when reflections are allowed. Thus there is exactly one full-Euclidean congruence class of maximizers, namely the chair. The quantitative statement follows immediately by retaining the nonnegative midpoint terms in the exact deficit formula.

## Verification
The accompanying standalone Python script reproduces the centroid–midpoint identity on five thousand independently generated six-tuples, constructs chairs for ninety-nine bond angles throughout the open range, checks the six unit edges and six angle constraints, verifies attainment, and independently factorizes the Gram characteristic polynomial. The algebraic proof above, rather than any finite sample, establishes the full theorem. Run \(\texttt{python3 hexagon_gyration_checker.py}\) with Python, NumPy and SymPy installed.

## Relationship to prior work
Crippen (1992) describes fixed-bond-length/fixed-angle cyclohexane configuration spaces using metric matrices and identifies the isolated chair versus a boat pseudorotation family. O'Hara (2011, first public preprint dated 25 May 2011) gives a complete all-angle conformational classification, including special small-angle configurations. Those works concern the **space of configurations**, not this sharp optimization of the centroid-based gyration metric or the exact opposite-chord-midpoint deficit. The present inequality holds simultaneously on all the classes they identify, without requiring their case-by-case parameterizations.

## Limitations
The statement assumes six labeled vertices, equal unit edge lengths, common bond angle, and ordinary Euclidean distance; no self-avoidance or force-field energy enters. The bond-angle endpoints are excluded from the uniqueness statement. The midpoint dispersion bounds midpoint separation, not directly the full vertexwise distance to a congruent chair. Historical priority is subject to independent literature review; the cited earlier configuration-space classifications are not claimed novel. This proof has not undergone independent mathematical validation.

## References
- G. M. Crippen, *Exploring the conformation space of cycloalkanes by linearized embedding*, Journal of Computational Chemistry **13** (1992), 351–361, doi:10.1002/jcc.540130308.
- J. O'Hara, *The configuration space of equilateral and equiangular hexagons*, arXiv:1105.5046v1 (first public 25 May 2011), subsequently Osaka Journal of Mathematics **50** (2013), 477–489.
