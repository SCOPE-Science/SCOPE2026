# Positive square points of \(\ell_\infty^n\) are exactly cube-face centers
## Finding
For every integer \(n\ge 1\), the positive square points of \(\ell_\infty^n\) are exactly
\[
\{-1,0,1\}^n\setminus\{0\}.
\]
Thus the positive square locus consists precisely of the centers of the nonempty proper faces of the \(n\)-cube and has cardinality \(3^n-1\).

Here a point \(x\in S_X\) is called a positive square point if, for every \(f\in S_{X^*}\) with \(f(x)\ge 0\) and every \(\varepsilon>0\), there exists \(y\in S_X\) with \(f(y)>1-\varepsilon\) and \(\|x+y\|>2-\varepsilon\).

## Assumptions and scope
The scalar field is real, \(X=\ell_\infty^n\), and \(n\ge1\) is finite. We identify \(X^*=\ell_1^n\). No smoothness, strict convexity, or asymptotic assumption is used.

The conclusion is specific to finite-dimensional cubes. It does not assert the analogous statement for an infinite-dimensional \(\ell_\infty(\Gamma)\), whose dual contains non-coordinate functionals.

## Proof
First note a compactness reduction. In any finite-dimensional Banach space, for fixed \(x\in S_X\) and \(f\in S_{X^*}\), the pair \((x,f)\) is good exactly when there is \(y\in S_X\) such that
\[
f(y)=1\qquad\text{and}\qquad \|x+y\|=2.
\]
Indeed, an exact witness gives the defining inequalities for every \(\varepsilon>0\). Conversely, from witnesses for \(\varepsilon=1/m\), compactness of \(S_X\) gives a convergent subsequence, and its limit satisfies both equalities.

Now take \(X=\ell_\infty^n\) and write \(f=(a_1,\ldots,a_n)\in S_{\ell_1^n}\). A vector \(y\in B_{\ell_\infty^n}\) satisfies \(f(y)=1\) exactly when
\[
y_i=\operatorname{sgn}(a_i)\quad\text{for every }i\text{ with }a_i\ne0,
\]
while coordinates with \(a_i=0\) are free in \([-1,1]\). Also, for \(x,y\in B_{\ell_\infty^n}\),
\[
\|x+y\|_\infty=2
\]
holds exactly when some coordinate \(i\) satisfies \(|x_i|=|y_i|=1\) and \(x_i=y_i\).

Suppose first that \(x\in\{-1,0,1\}^n\setminus\{0\}\), and let
\[
A=\{i:x_i\ne0\}=\{i:|x_i|=1\}.
\]
Fix \(f\in S_{\ell_1^n}\) with \(f(x)\ge0\). If \(a_i=0\) for some \(i\in A\), choose a norming vector \(y\) for \(f\) and set the free coordinate \(y_i=x_i\); then \(f(y)=1\) and \(\|x+y\|_\infty=2\). Otherwise every \(a_i\) with \(i\in A\) is nonzero. If every one of those coefficients had sign opposite to \(x_i\), then
\[
f(x)=-\sum_{i\in A}|a_i|<0,
\]
contrary to the hypothesis. Hence some \(i\in A\) has \(\operatorname{sgn}(a_i)=x_i\). Every norming vector \(y\) for \(f\) then satisfies \(y_i=x_i\), again giving \(\|x+y\|_\infty=2\). Thus \(x\) is a positive square point.

Conversely, suppose \(x\in S_{\ell_\infty^n}\) has a coordinate \(j\) with
\[
0<|x_j|<1.
\]
Let \(A=\{i:|x_i|=1\}\), which is nonempty. Choose
\[
0<\delta<\frac{|x_j|}{1+|x_j|}.
\]
Define \(f=(a_i)\in\ell_1^n\) by distributing total mass \(\delta\) equally over \(A\) with signs opposite to \(x_i\), putting the remaining mass \(1-\delta\) on coordinate \(j\) with the sign of \(x_j\), and setting every other coefficient to zero. Explicitly,
\[
a_i=-\frac{\delta}{|A|}x_i\quad(i\in A),\qquad
a_j=(1-\delta)\operatorname{sgn}(x_j).
\]
Then \(\|f\|_1=1\) and
\[
f(x)=-\delta+(1-\delta)|x_j|>0.
\]
If \(f(y)=1\), the norming-face description forces \(y_i=-x_i\) for every \(i\in A\), while \(y_j=\operatorname{sgn}(x_j)\). Therefore the saturated coordinates cancel, and every unsaturated coordinate \(k\notin A\) obeys
\[
|x_k+y_k|\le |x_k|+1<2.
\]
Hence \(\|x+y\|_\infty<2\) for every norming vector \(y\) of \(f\). By the compactness reduction, \((x,f)\) is not good, so \(x\) is not a positive square point.

Thus the positive square points are exactly the nonzero vectors with all coordinates in \(\{-1,0,1\}\). Such a vector is the center of the unique proper cube face obtained by fixing its nonzero coordinates to their signs, and every nonempty proper face has exactly one such center. The count is therefore \(3^n-1\).

## Verification
The proof is symbolic and exhaustive. Its only finite-dimensional compactness input is that a sequence of approximate witnesses has a convergent subsequence in the unit sphere. The norming face of an \(\ell_1^n\) functional on the cube is described coordinatewise, and the obstruction functional in the converse has exact \(\ell_1\)-norm one and strictly positive value on \(x\).

For \(n=1\), the theorem gives the two sphere points. For \(n=2\), it gives the four vertices and four edge midpoints, including the point \((1,0)\) used in the motivating source. No finite enumeration is used as a substitute for the proof.

## Relationship to prior work
Langemets introduced positive and negative square points while proving that the negative square points are exactly the Daugavet points. In the same paper, Example 3.4 shows that \((1,0)\in\ell_\infty^2\) is a positive square point which is neither a \(\Delta\)-point nor a \(\nabla\)-point. The paper does not classify the positive square points of \(\ell_\infty^n\), nor does it identify them with cube-face centers.

The present result completes that canonical finite-dimensional model in every dimension. It is not implied by the operator-level equivalence between the global signed-square Daugavet properties and the Daugavet property: finite-dimensional cubes do not have the Daugavet property, while they still contain the finite positive-square locus classified here.

## Limitations
The result concerns the newly introduced positive square point condition only. It gives no classification of \(\Delta\)-points or \(\nabla\)-points, and it does not extend automatically to infinite-dimensional \(\ell_\infty(\Gamma)\). It also does not provide a stability theorem for approximate positive-square points.

## References
1. J. Langemets, “Characterizing the Daugavet property by squares of rank-one operators,” arXiv:2609.27693v1, 2026.
2. T. A. Abrahamsen, R. Haller, V. Lima, and K. Pirk, “Delta- and Daugavet points in Banach spaces,” Proc. Edinb. Math. Soc. 63 (2020), 475–496.
3. R. Haller, J. Langemets, Y. Perreau, and T. Veeorg, “Unconditional bases and Daugavet renormings,” J. Funct. Anal. 286 (2024), Article 110421.
