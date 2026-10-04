# An exact 8+6 angle-bisector split for the 14-real QL² configuration
## Finding
Consider the \(QL^2\) constituent in the mixed degeneration used for the 144-real-circle construction of Brysiewicz. The fixed conic is
\[
Q_1:\;20x^2-5y^2+1=0,
\]
and the two limiting lines are
\[
\ell_1=-1601x+1000y+\frac{134133}{500}=0,
\qquad
\ell_2=-2261x+1000y+\frac{1788717}{1000}=0.
\]
Set
\[
N_1=3563201,\qquad N_2=6112121.
\]

The 14 real circles tangent to \(Q_1,\ell_1,\ell_2\) split exactly as follows:
\[
8
\]
belong to the angle-bisector family
\[
\frac{\ell_1}{\sqrt{N_1}}=\frac{\ell_2}{\sqrt{N_2}},
\]
and
\[
6
\]
belong to the other family
\[
\frac{\ell_1}{\sqrt{N_1}}=-\frac{\ell_2}{\sqrt{N_2}}.
\]
Each family has complex enumerative degree \(8\). Hence the first family is totally real, while the second has exactly one nonreal conjugate pair.

## Assumptions and scope
The notation comes from the mixed degeneration in Brysiewicz, *144 real circles tangent to three conics*. There the irreducible conic is
\[
Q_1(x,y)=20x^2-5y^2+1,
\]
and the two other conics degenerate to the double lines
\[
L_1=y-\frac{2399}{1000}-\frac{1601}{1000}\left(x-\frac{833}{500}\right),
\]
\[
L_2=y-\frac{3857}{1000}-\frac{2261}{1000}\left(x-\frac{2497}{1000}\right).
\]
Multiplying by \(1000\) gives the \(\ell_1,\ell_2\) above. Their squared normal lengths are \(N_1\) and \(N_2\).

A nonzero-radius Euclidean circle tangent to both nonparallel lines has its center on exactly one of the two Euclidean angle bisectors. If \(q\) is its signed distance from \(\ell_1=0\), then its squared radius is \(q^2\).

The source establishes that this particular \(QL^2\) problem has exactly 14 real solutions. The claim here refines that total by determining the exact distribution between the two angle-bisector families.

## Proof
For a sign \(\sigma\in\{+1,-1\}\), impose
\[
\ell_1(X,Y)=q\sqrt{N_1},
\qquad
\ell_2(X,Y)=\sigma q\sqrt{N_2}.
\]
Because the two lines are nonparallel, this system has a unique solution
\[
(X_\sigma(q),Y_\sigma(q))
\]
affine-linear in \(q\), with coefficients in
\[
K=\mathbf Q\!\left(\sqrt{N_1},\sqrt{N_2}\right).
\]
The corresponding circle is
\[
C_{\sigma,q}:
(x-X_\sigma(q))^2+(y-Y_\sigma(q))^2=q^2.
\]

Write \(M_Q\) and \(M_{\sigma,q}\) for the symmetric \(3\times3\) matrices of \(Q_1\) and \(C_{\sigma,q}\). A necessary condition for the two smooth conics to be tangent is that the cubic
\[
P_{\sigma,q}(\lambda)=\det(M_Q+\lambda M_{\sigma,q})
\]
have a repeated root. Therefore every \(QL^2\) solution in branch \(\sigma\) is a zero of
\[
\Delta_\sigma(q)=\operatorname{disc}_\lambda P_{\sigma,q}(\lambda).
\]

Exact symbolic elimination over \(K\) gives
\[
\deg_q\Delta_+=\deg_q\Delta_-=8,
\]
with both polynomials squarefree and with \(q=0\) excluded. Exact Sturm root counting in the real embedding determined by the positive square roots gives
\[
\#\{q\in\mathbf R:\Delta_+(q)=0\}=8,
\]
and
\[
\#\{q\in\mathbf R:\Delta_-(q)=0\}=6.
\]
Thus there are at most \(8+6=14\) real tangent circles across the two angle-bisector families.

Brysiewicz independently establishes that the same \(QL^2\) configuration has exactly 14 real solutions. Every such real circle has nonzero radius, is tangent to the two nonparallel lines, and therefore belongs to exactly one of the two angle-bisector families. Since the exact discriminant count supplies only 14 real parameter values in total, all of them must be realized by the 14 real \(QL^2\) circles. Consequently the branch counts are exactly
\[
8\quad\text{and}\quad6.
\]

Because each branch has degree \(8\), the minus branch has precisely two nonreal roots; its coefficients are real, so these form one conjugate pair. This proves the claim.

## Verification
The accompanying `verify.py` reconstructs the two angle-bisector parametrizations from the exact rational line equations, forms the circle matrices, computes the determinant-pencil discriminants symbolically, and performs exact real-root counting over
\[
\mathbf Q\!\left(\sqrt{3563201},\sqrt{6112121}\right).
\]
It verifies that both discriminants are squarefree of degree \(8\), that neither has \(q=0\) as a root, and that their exact real-root counts are \(8\) and \(6\).

The replay output ends in `VERIFY_OK`. No floating-point root count is used for the accepted claim.

## Relationship to prior work
Brysiewicz records that the mixed-degeneration \(QL^2\) constituent has complex count \(16\), gives a configuration with \(14\) real solutions, and notes that the maximal real count for \(QL^2\) remains open. The paper tabulates only the total \(14\) for this constituent.

The present refinement separates those 14 solutions according to the canonical decomposition of circles tangent to two lines into the two Euclidean angle-bisector families. One branch is already totally real, while the entire two-solution deficit from the complex count lies on the other branch.

Targeted searches for the source identifier, the \(QL^2\) constituent, the angle-bisector decomposition, and an \(8+6\) split located no statement of this refinement.

## Limitations
This result does not determine the maximal possible real count for the general \(QL^2\) problem. In particular, it does not prove that \(16\) real solutions are impossible or construct a \(16\)-real configuration.

The argument uses the published fact that the specified limiting configuration has exactly 14 real \(QL^2\) circles. The new exact computation determines how those circles are distributed between the two angle-bisector branches; it does not independently recertify the source's tangency points.

## References
1. T. Brysiewicz, *144 real circles tangent to three conics*, arXiv:2609.01521v1, 2026.
2. S. Fiorelli Vilmart, *Étude de cercles tangents à des coniques*, doctoral thesis, Université de Genève, 2009.
