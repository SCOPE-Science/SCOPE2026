# Parity law for Euclidean roundness of the regular-simplex central kernel
## Finding
Let
\[
S_n=\operatorname{conv}\{v_0,\ldots,v_n\}\subset\mathbb R^n,
\qquad n\ge2,
\]
be a regular simplex of Euclidean circumradius \(1\), centered at its centroid, and let
\[
K_n=S_n\cap(-S_n).
\tag{1}
\]
Then
\[
\boxed{r(K_n)=\frac1n}
\tag{2}
\]
and
\[
\boxed{
R(K_n)=
\begin{cases}
\displaystyle\frac1{\sqrt n},&n\text{ odd},\\[5pt]
\displaystyle\frac1{\sqrt{n+1}},&n\text{ even}.
\end{cases}}
\tag{3}
\]
Thus the Euclidean roundness ratio is
\[
\boxed{
\frac{R(K_n)}{r(K_n)}=
\begin{cases}
\sqrt n,&n\text{ odd},\\[3pt]
\displaystyle\frac{n}{\sqrt{n+1}},&n\text{ even}.
\end{cases}}
\tag{4}
\]

The farthest points are also explicit. Define
\[
y_i=n\,v_i\cdot x.
\tag{5}
\]
For odd \(n\), equality in (3) occurs exactly when the \(n+1\) numbers \(y_i\) are equally split between \(+1\) and \(-1\). For even \(n\), equality occurs exactly when one \(y_i\) is \(0\) and the other \(n\) entries are equally split between \(+1\) and \(-1\). Hence the numbers of farthest points are, respectively,
\[
\binom{n+1}{(n+1)/2}
\quad\text{and}\quad
(n+1)\binom{n}{n/2}.
\tag{6}
\]

## Assumptions and scope
The regular simplex is normalized by
\[
\lVert v_i\rVert=1,
\qquad
v_i\cdot v_j=-\frac1n\quad(i\ne j),
\qquad
\sum_{i=0}^n v_i=0.
\tag{7}
\]
The body \(K_n\) in (1) is the centered intersection of a regular simplex with its reflection. This is the regular-simplex instance of the centrally symmetric kernel appearing in the classical Fáry--Rédei symmetry problem and in Brannen's projection-body discussion.

The theorem concerns Euclidean inradius, circumradius, diameter, and the full farthest-point set of this canonical symmetric kernel. It does not re-evaluate its volume and does not address Brannen's projection-body maximization conjecture.

## Proof
For every \(x\in\mathbb R^n\), the barycentric coordinate of \(x\) at the vertex \(v_i\) is
\[
\lambda_i(x)=\frac{1+n\,v_i\cdot x}{n+1}.
\tag{8}
\]
Indeed, (8) takes the value \(1\) at \(v_i\), the value \(0\) at every other vertex, and the coordinates sum to \(1\). Consequently
\[
x\in S_n
\quad\Longleftrightarrow\quad
v_i\cdot x\ge-\frac1n
\quad(0\le i\le n).
\]
Applying the same criterion to \(-x\) gives
\[
K_n
=
\left\{x:\left|v_i\cdot x\right|\le\frac1n
\text{ for every }i\right\}.
\tag{9}
\]
Since every \(v_i\) is a unit normal, all supporting hyperplanes in (9) have distance \(1/n\) from the origin. The body is centrally symmetric, so its largest inscribed Euclidean ball can be centered at the origin: if \(c+rB_2^n\subset K_n\), then also \(-c+rB_2^n\subset K_n\), and convexity yields \(rB_2^n\subset K_n\). Therefore (9) proves (2).

The regular-simplex vectors form a tight frame:
\[
\sum_{i=0}^n v_i v_i^{\mathsf T}
=
\frac{n+1}{n}I_n.
\tag{10}
\]
Set \(y_i=n\,v_i\cdot x\). Equations (7), (9), and (10) give
\[
\sum_{i=0}^n y_i=0,
\qquad
|y_i|\le1,
\qquad
\lVert x\rVert^2
=
\frac1{n(n+1)}\sum_{i=0}^n y_i^2.
\tag{11}
\]
Conversely, every vector \(y\) satisfying \(\sum_i y_i=0\) is obtained from a unique \(x\), because the map in (5) is an injective linear map between two \(n\)-dimensional spaces. Thus the circumradius problem is exactly
\[
\max\left\{
\sum_{i=0}^n y_i^2:
-1\le y_i\le1,
\ \sum_{i=0}^n y_i=0
\right\}.
\tag{12}
\]

Put \(m=n+1\). A maximizer in (12) must be a vertex of the cube section, because the squared Euclidean norm is strictly convex. At a vertex of
\[
[-1,1]^m\cap\left\{\sum_i y_i=0\right\},
\]
all but at most one coordinate lie in \(\{\pm1\}\).

If \(n\) is odd, then \(m\) is even. The section contains cube vertices: choose exactly \(m/2\) plus signs and \(m/2\) minus signs. Hence the maximum in (12) is \(m=n+1\), and every maximizer has exactly that sign pattern. Equation (11) gives
\[
R(K_n)^2=\frac{n+1}{n(n+1)}=\frac1n.
\]

If \(n\) is even, then \(m\) is odd. At an extreme point, the sum of the \(m-1=n\) saturated coordinates is an even integer. The remaining coordinate lies in \([-1,1]\) and cancels that sum, so the saturated coordinates must sum to \(0\) and the remaining coordinate is \(0\). Therefore the maximum in (12) is \(m-1=n\), with exactly the pattern stated after (5). Equation (11) gives
\[
R(K_n)^2=\frac{n}{n(n+1)}=\frac1{n+1}.
\]
This proves (3), (4), and the classification and counts in (6). Since \(K_n=-K_n\), its Euclidean diameter is also exactly \(2R(K_n)\).

## Verification
The bundled `verify.py` constructs the standard regular simplex in the zero-sum hyperplane, verifies the Gram and tight-frame identities, enumerates every vertex of the central cube section for dimensions \(2\) through \(10\), and checks the exact parity formulas and farthest-point counts.

The finite enumeration is only a regression check. The all-dimensional result is proved by the cube-section extreme-point argument in (12).

## Relationship to prior work
Fáry and Rédei introduced the centrally symmetric kernel problem for convex bodies. Brannen later uses, for a regular simplex \(S\) centered at the origin, the body
\[
S^s=S\cap(-S)
\]
as the largest centrally symmetric subset of the simplex and proposes it as the candidate extremizer for an upper projection-body inequality among centrally symmetric convex bodies. His calculation concerns its volume and projection body, not its Euclidean inradius, circumradius, diameter, or parity-dependent farthest-point structure.

A later treatment of projection-body volumes revisits Brannen's conjectural framework under primary MSC \(52A40\), but does not state the radius formulas (2)--(4). Related regular-simplex section results concern hyperplane sections rather than the intersection with the reflected simplex.

Targeted searches under “central kernel,” “largest centrally symmetric subset,” “regular simplex intersection with its negative,” “inradius,” “circumradius,” “Euclidean radius,” “cube section,” and parity formulations did not locate an implication-equivalent published statement.

## Limitations
The formulas depend on the regular Euclidean metric. An arbitrary affine simplex has an affinely equivalent central kernel, but Euclidean inradius and circumradius are not affine invariants.

The result does not compute the maximum-volume symmetry ratio, which is classical, and does not prove either of Brannen's projection-body conjectures.

The central cube-section model is classical enough that an equivalent radius computation may exist in unindexed polytope or hypersimplex literature. That is the main residual originality risk.

## References
1. N. S. Brannen, *Volumes of projection bodies*, *Mathematika* 43 (1996), 255--264. DOI: 10.1112/S002557930001175X.
2. I. Fáry and L. Rédei, *Der zentralsymmetrische Kern und die zentralsymmetrische Hülle von konvexen Körpern*, *Mathematische Annalen* 122 (1950), 205--220.
3. M. Moszyńska and T. Żukowski, *On G-pseudo-centres of convex bodies*, *Glasnik Matematički* 33(53) (1998), 251--265.
4. C. Saroglou, *Volumes of projection bodies of some classes of convex bodies*, *Mathematika* 57 (2011), 329--339. DOI: 10.1112/S0025579311001860.
