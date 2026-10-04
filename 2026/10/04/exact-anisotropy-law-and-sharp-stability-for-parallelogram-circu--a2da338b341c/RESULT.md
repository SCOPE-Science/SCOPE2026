# Exact anisotropy law and sharp stability for parallelogram circumellipses
## Finding
Let \(Q\) be a nondegenerate Euclidean parallelogram and \(E_0\) its minimum-area ellipse through the four vertices. Every circumellipse \(E\) of \(Q\) has the same center as \(Q\). Write
\[
E=\{x:(x-o)^T H(x-o)\le 1\},\qquad
E_0=\{x:(x-o)^T H_0(x-o)\le 1\},
\]
with \(H,H_0\) positive definite. If \(\lambda_{\max}\ge \lambda_{\min}>0\) are the generalized eigenvalues of the pair \((H,H_0)\), define the affine-invariant half-log anisotropy
\[
\delta=\frac12\log\!\left(\frac{\lambda_{\max}}{\lambda_{\min}}\right).
\]
Then the entire circumellipse pencil obeys the exact identity
\[
\boxed{\ \frac{\operatorname{area}(E)}{\operatorname{area}(Q)}=\frac{\pi}{2}\cosh\delta\ }.
\]
Equivalently,
\[
\frac{\operatorname{area}(E)}{\operatorname{area}(Q)}-\frac{\pi}{2}
=\pi\sinh^2\!\left(\frac{\delta}{2}\right)
\ge \frac{\pi}{4}\delta^2.
\]
The coefficient \(\pi/4\) is optimal. Thus the classical minimum-area theorem for parallelogram circumellipses has a complete exact stability profile, with area excess itself serving as an invertible coordinate on the quotient pencil:
\[
\delta=\operatorname{arcosh}\!\left(\frac{2\operatorname{area}(E)}{\pi\operatorname{area}(Q)}\right).
\]

## Assumptions and scope
The parallelogram is nondegenerate. A circumellipse means a nondegenerate ellipse whose boundary contains all four vertices. The generalized eigenvalues are those of \(H_0^{-1}H\), equivalently of the symmetric positive definite matrix \(H_0^{-1/2}HH_0^{-1/2}\). The quantity \(\delta\) is unchanged by invertible affine changes of coordinates. The statement concerns ellipses through the vertices, not minimum-volume ellipses merely containing the parallelogram.

## Proof
Translate the center of \(Q\) to the origin. Its vertices can be written \(p,q,-p,-q\), where \(p,q\) are linearly independent. If a general conic through these four points has equation \(x^T Hx+b^Tx+c=0\), subtracting the equations at \(p\) and \(-p\), and then at \(q\) and \(-q\), gives \(b^Tp=b^Tq=0\). Hence \(b=0\): every circumellipse is centered at the parallelogram center.

Let \(P=[p\ q]\). In coordinates \(y=P^{-1}x\), the vertices become \(\pm e_1,\pm e_2\), and a centered ellipse through them has a unique normalized quadratic form
\[
y^T K_cy\le1,\qquad K_c=\begin{pmatrix}1&c\\c&1\end{pmatrix},\qquad |c|<1.
\]
Indeed, the two vertex conditions force both diagonal entries to equal \(1\), while positive definiteness is exactly \(|c|<1\). Thus this single parameter is the complete pencil.

The parallelogram in these coordinates has area \(2\). Since \(\det K_c=1-c^2\), the ellipse has area \(\pi/\sqrt{1-c^2}\), so
\[
\frac{\operatorname{area}(E)}{\operatorname{area}(Q)}
=\frac{\pi}{2\sqrt{1-c^2}}.
\]
This is minimized uniquely at \(c=0\). Hence \(E_0\) corresponds to \(K_0=I\). Relative to \(H_0\), the generalized eigenvalues are therefore \(1+|c|\) and \(1-|c|\), so
\[
\delta=\frac12\log\frac{1+|c|}{1-|c|}=\operatorname{artanh}|c|.
\]
Because \(\sqrt{1-c^2}=\operatorname{sech}\delta\), substitution gives the boxed identity.

Finally,
\[
\frac{\pi}{2}(\cosh\delta-1)=\pi\sinh^2(\delta/2)\ge \frac{\pi}{4}\delta^2,
\]
using \(\sinh t\ge t\) for \(t\ge0\). The inequality is strict for \(\delta>0\). Since \(\sinh^2(\delta/2)/\delta^2\to1/4\) as \(\delta\to0\), no coefficient larger than \(\pi/4\) can hold globally.

## Verification
A deterministic checker samples nonsingular affine images of the model parallelogram and parameters \(c\in(-1,1)\). It verifies the four vertex incidences, direct determinant area, generalized-eigenvalue anisotropy, exact \(\cosh\) law, affine invariance, and the sharp quadratic lower bound. The proof itself is symbolic and does not depend on finite sampling.

## Relationship to prior work
Horwitz proved existence and uniqueness of a minimum-area circumellipse for a general convex quadrilateral; the first public version located here is arXiv:0707.2092, submitted 13 July 2007. Li, Wang, Shen and Dai later stated for parallelograms that the minimum occurs when the diagonals are conjugate diameters and that the minimum area is \(\pi/2\) times the parallelogram area (DOI: 10.1515/math-2017-0117, Theorems 4–5). Classical conic geometry also identifies conjugate-diameter parallelograms as maximum-area parallelograms inscribed in a fixed ellipse.

The result here keeps the full pencil rather than only its minimizer: it identifies the affine-invariant generalized-eigenvalue coordinate \(\delta\), gives the exact \(\cosh\) area profile, its exact inverse, and the globally sharp quadratic stability coefficient. Targeted database and literature searches located the classical extremal statements but no statement of this exact anisotropy law or its sharp stability consequence. A 2024 monograph by Horwitz has a section titled “Area Inequality” for circumscribed ellipses of parallelograms; only publisher-level description and contents were available for inspection here, so overlap with that section remains a specific residual risk.

## Limitations
No claim is made that the classical minimum \(\pi/2\), the conjugate-diameter characterization, or uniqueness of the minimizing circumellipse is new. The originality claim is limited to the exact affine-invariant \(\cosh\) profile and the resulting sharp stability/inverse formulas. The 2024 monograph section noted above was not available in full text during this check, so exact-formula overlap there cannot be excluded. Independent review has not been performed.

## References
1. A. Horwitz, “Ellipses of minimal area and of minimal eccentricity circumscribed about a convex quadrilateral,” arXiv:0707.2092 (first version 13 July 2007); Australian Journal of Mathematical Analysis and Applications 7 (2010), Article 8.
2. J. H. Li, Z. Q. Wang, Y. X. Shen, and Z. Y. Dai, “Does any convex quadrilateral have circumscribed ellipses?”, Open Mathematics (2017), DOI: 10.1515/math-2017-0117.
3. A. Horwitz, *Ellipses Inscribed in, and Circumscribed about, Quadrilaterals*, Chapman & Hall/CRC, 2024, ISBN 9781032622590.
4. “Conic Sections,” *Encyclopaedia Britannica*, 9th edition, classical discussion of conjugate diameters and maximal inscribed parallelograms.
