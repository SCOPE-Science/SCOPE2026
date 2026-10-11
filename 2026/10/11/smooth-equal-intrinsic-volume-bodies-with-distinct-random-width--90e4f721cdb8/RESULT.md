# Smooth equal-intrinsic-volume bodies with distinct random-width laws
## Finding
There exists \(\varepsilon_0>0\) such that for every \(0<|\varepsilon|<\varepsilon_0\), the two origin-symmetric \(C^\infty\), strictly convex bodies in \(\mathbb R^3\) with support functions \[h_f(u)=1+\varepsilon f(u),\qquad h_g(u)=1+\varepsilon g(u),\] where for \(u=(x,y,z)\in S^2\), \[f(u)=y^4-6y^2z^2+z^4,\] and \[g(u)=\frac{2\sqrt7}{7}\big[(y^4-6y^2z^2+z^4)-(x^4-6x^2z^2+z^4)\big],\] have exactly the same volume, surface area, and mean width, but have different random-width distributions for a uniform direction \(U\in S^2\). In fact their common mean width is \(2\), their common surface area and volume are respectively \[4\pi-\frac{256\pi}{35}\varepsilon^2\qquad\text{and}\qquad \frac{4\pi}{3}-\frac{256\pi}{35}\varepsilon^2,\] while the fourth centered moments of width differ because \[\mathbb E f(U)^4=\frac{4096}{36465},\qquad \mathbb E g(U)^4=\frac{241664}{2501499},\qquad \mathbb E f(U)^4-\mathbb E g(U)^4=\frac{65536}{4169165}>0.\]

This gives an explicit smooth, strictly convex, centrally symmetric three-dimensional pair with all three nontrivial intrinsic volumes equal but with unequal scalar random-width laws. The construction addresses the width half of the smooth three-dimensional strengthening left open after the polyhedral/prismatic counterexamples in Abas's recent work.

## Assumptions and scope
Let \(\sigma\) be spherical area measure on \(S^2\), and let \(U\) be uniform on \(S^2\). For a smooth function \(q\) on \(S^2\), write
\[A_q=\nabla^2_{S^2}q+qI.\]
Define
\[\varepsilon_0=\min\left\{\|f\|_\infty^{-1},\|g\|_\infty^{-1},\|A_f\|_{\mathrm{{op}},\infty}^{-1},\|A_g\|_{\mathrm{{op}},\infty}^{-1}\right\}.\]
For every \(0<|\varepsilon|<\varepsilon_0\), both \(h_f\) and \(h_g\) are positive and satisfy \(\nabla^2 h+hI\succ0\), so they are support functions of origin-containing \(C^\infty\) strictly convex bodies. Because \(f\) and \(g\) are even, the bodies are origin-symmetric.

The claim is only about the random-width law. It does not prove that the corresponding random-brightness laws are different, so it does not settle the simultaneous smooth width-and-brightness strengthening in full.

## Proof
Both \(f\) and \(g\) are restrictions of homogeneous harmonic quartics, hence
\[\Delta_{S^2}q=-20q\]
for \(q=f,g\), and \(\int_{S^2}q\,d\sigma=0\). Set \(A=A_q\). Then
\[\operatorname{{tr}}A=\Delta q+2q=-18q.\]
On \(S^2\), Bochner's identity gives
\[\int_{S^2}|\nabla^2q|^2\,d\sigma=380\int_{S^2}q^2\,d\sigma.\]
Therefore
\[\int_{S^2}|A|^2\,d\sigma=342\int_{S^2}q^2\,d\sigma,\]
and, because \(A\) is a \(2\times2\) symmetric tensor,
\[\int_{S^2}\det A\,d\sigma=\frac12\int_{S^2}\big[(\operatorname{{tr}}A)^2-|A|^2\big]\,d\sigma=-9\int_{S^2}q^2\,d\sigma.\]

For the cubic term, multiply the Bochner identity by \(q\). Since
\[\int_{S^2}q|\nabla q|^2\,d\sigma=10\int_{S^2}q^3\,d\sigma,\]
one obtains
\[\int_{S^2}q|\nabla^2q|^2\,d\sigma=90\int_{S^2}q^3\,d\sigma.\]
Thus
\[\int_{S^2}q|A|^2\,d\sigma=52\int_{S^2}q^3\,d\sigma,\]
and hence
\[\int_{S^2}q\det A\,d\sigma=136\int_{S^2}q^3\,d\sigma.\]

For \(h=1+\varepsilon q\), the curvature-radius tensor is \(I+\varepsilon A\). In dimension three the surface area and volume are
\[S(K_q)=\int_{S^2}\det(I+\varepsilon A)\,d\sigma,\]
\[V(K_q)=\frac13\int_{S^2}(1+\varepsilon q)\det(I+\varepsilon A)\,d\sigma.\]
Because the determinant is exactly quadratic in \(\varepsilon\), the preceding identities give the exact formulas
\[S(K_q)=4\pi-9\varepsilon^2\int_{S^2}q^2\,d\sigma,\]
\[V(K_q)=\frac{4\pi}{3}-9\varepsilon^2\int_{S^2}q^2\,d\sigma+\frac{136}{3}\varepsilon^3\int_{S^2}q^3\,d\sigma.\]
The mean width is exactly \(2\), since \(q\) has spherical mean zero and the body is centrally symmetric.

For the explicit quartics, the standard sphere-moment formula
\[\mathbb E[X^{2a}Y^{2b}Z^{2c}]=\frac{(2a-1)!!(2b-1)!!(2c-1)!!}{(2a+2b+2c+1)!!}\]
for uniform \((X,Y,Z)\in S^2\) yields
\[\mathbb E f(U)^2=\mathbb E g(U)^2=\frac{64}{315}.\]
Moreover \(\mathbb E f(U)^3=0\): rotation by \(\pi/4\) in the \((y,z)\)-plane sends \(f\) to \(-f\). Also \(\mathbb E g(U)^3=0\): swapping \(x\) and \(y\) sends \(g\) to \(-g\). Consequently the two bodies have exactly equal surface area and volume, and substituting \(\int q^2\,d\sigma=4\pi(64/315)\) gives the displayed common values.

Finally, for an origin-symmetric body \(w_K(u)=2h_K(u)\). Thus equality of the two random-width laws would force equality of every centered width moment. But direct exact integration gives
\[\mathbb E f(U)^4=\frac{4096}{36465},\qquad \mathbb E g(U)^4=\frac{241664}{2501499},\]
with difference \(65536/4169165>0\). Therefore the random-width laws are different for every nonzero admissible \(\varepsilon\).

## Verification
The included `verify.py` uses only the Python standard library. It represents the quartics exactly as rational monomial dictionaries, checks that the unscaled harmonic polynomials have zero Euclidean Laplacian, evaluates all sphere moments by the exact double-factorial formula, verifies the equal quadratic moments and zero cubic moments, and reproduces the two distinct fourth moments and their positive difference. It also checks the exact common coefficients in the surface-area and volume formulas. The script is a finite symbolic check of the explicit polynomial arithmetic; the universal support-function and curvature argument is proved above rather than inferred from computation.

## Relationship to prior work
Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* (arXiv:2609.26202v1), proves that equal intrinsic volumes do not determine width or brightness laws in dimension three using centrally symmetric right prisms. Its introduction explicitly notes that the spatial witnesses are not smooth strictly convex bodies and that the corresponding smooth three-dimensional strengthening remains open. The present construction gives a smooth strictly convex near-spherical pair for the width law, while making no claim about brightness.

Finch's earlier work on width distributions of regular polyhedra (arXiv:1110.0671) develops nontrivial higher width moments for specific polyhedra but does not compare smooth bodies with equal volume, surface area, and mean width. Standard support-function identities and the area-measure formula are classical; the new content is the explicit matched degree-four pair and the exact separation of their random-width laws.

## Limitations
The argument proves only that the scalar width laws differ. It does not show that the brightness laws of this same pair differ, and therefore does not resolve the full simultaneous smooth strengthening posed by the recent source. The admissible interval is given by a rigorous positive-curvature threshold \(\varepsilon_0\), but its numerical sharp value is not optimized. A poorly indexed earlier smooth counterexample using a different support-function construction remains a residual originality risk.

## References
1. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1, first public 2026-08-10, primary MSC 52A22.
2. Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671.
3. Rolf Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, second expanded edition, Cambridge University Press, 2014.
