# A cubic residue-class defect in affine projection on polygonal boundaries

## Finding
For every integer \(n\ge3\), let \(P_n\subset\mathbb R^2\) be the regular \(n\)-gon with vertices \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), and put normalized **arclength**, not area or vertex-counting measure, on its boundary. Let \(\mathcal P_n\) be the \(L^2(\partial P_n)\)-orthogonal projector onto restrictions of real affine functions. Define
\[
h=\frac{2\pi}{n},\qquad k=\frac6{2+\cos h},\qquad J=\left\lceil\frac n3\right\rceil,
\]
\[
a=1+k\cos((J-1)h),\qquad b=-1-k\cos(Jh).
\]
Then \(a,b>0\), and its sharp endpoint operator norms are
\[
\boxed{\|\mathcal P_n\|_{L^1\to L^1}=\|\mathcal P_n\|_{L^\infty\to L^\infty}
=1+\frac2n\left[-(n-2J+1)+k\frac{\sin((J-\tfrac12)h)}{\sin(h/2)}-\frac{ab}{a+b}\right].}
\]
Each boundary vertex, and no nonvertex boundary point, is a norm-maximizing evaluation location. At a chosen vertex \(v\), a sharp \(L^\infty\) input is the sign of \(1+k v\cdot y\), with signs arbitrary only at its zero set.

Let \(\Lambda_\circ=\frac13+\frac{2\sqrt3}{\pi}\). As \(n\to\infty\), with an error bounded uniformly over all three residue classes,
\[
\boxed{\|\mathcal P_n\|_{\infty\to\infty}=\Lambda_\circ+
\frac{2\pi\sqrt3}{3n^2}+\frac{8\pi^2}{81n^3}\varepsilon_n+O(n^{-4}),\quad
\varepsilon_n=\begin{cases}0&n\equiv0\pmod3,\\-1&n\equiv1\pmod3,\\1&n\equiv2\pmod3.\end{cases}}
\]
In particular, the leading polygonal defect is positive, while its cubic correction remembers \(n\bmod3\). The first three simple benchmarks are \(\|\mathcal P_3\|=16/9\), \(\|\mathcal P_4\|=5/3\), and \(\|\mathcal P_6\|=277/180\). These norms are induced endpoint norms, not the Hilbert-space norm (which is one).

## Assumptions and scope
Each polygon has unit circumradius and its own normalized one-dimensional arclength probability measure \(\mu_n\), equally weighted across its \(n\) edges. Edge endpoints are measure-zero and shared without duplicate mass. The projector acts on real or complex functions; in the complex case use affine coordinate functions with complex coefficients. Its integral kernel and norm are the same. The data are arbitrary bounded measurable functions; no positivity of the data is assumed. The assertion concerns the entire boundary, not the filled polygon, not solely the vertices, and not the discrete cyclic Fourier projector.

## Proof
**1. Reproducing kernel.** On an edge, write \(y=(1-t)v_j+tv_{j+1}\), \(0\le t\le1\). Rotational symmetry gives \(\int y\,d\mu_n=0\) and \(\int yy^{\mathsf T}\,d\mu_n=\sigma_n^2 I_2\). Integrating \(\|y\|^2\) along any edge yields \((2+\cos h)/3\), so \(\sigma_n^2=(2+\cos h)/6\). The reproducing kernel is therefore
\[
K_n(x,y)=1+kx\cdot y,\qquad k=\sigma_n^{-2}=\frac6{2+\cos h}.
\]
This proves the stated normalization and symmetry, including the equality of the \(L^1\) and \(L^\infty\) operator norms by duality.

**2. Localization and sharpness.** For fixed \(x\), \(\|K_n(x,\cdot)\|_{L^1(\mu_n)}\) is convex in \(x\). Every boundary point is a convex combination of its two incident vertices, hence the maximum occurs at a vertex; symmetry makes all vertex values equal. For the strict form, kernels evaluated at adjacent vertices have opposite signs on a set of positive arclength (their distinct negative caps have different endpoints). Equality in the triangle inequality is therefore strict for any interior point of an edge. The kernel-sign input at any maximizing vertex attains the \(L^\infty\) norm. The symmetric kernel implies the same \(L^1\) induced norm (its \(L^1\) extremum need not be attained by an \(L^1\) function).

**3. Exact finite formula.** At \(v_0\), the kernel endpoint values along edge \((v_j,v_{j+1})\) are \(q_j=1+k\cos(jh)\) and \(q_{j+1}\), with indices modulo \(n\). The sequence is strictly negative precisely at \(J\le j\le n-J\). Indeed \(Jh\ge2\pi/3\) and \(k>2\) imply \(q_J<0\). For \(n\ge4\), \(h\le\pi/2\) and \((J-1)h\le2\pi/3-h/3\); the inequality
\[
\cos(2\pi/3-h/3)+\frac{2+\cos h}{6}>0
\]
follows from \(2\sin(2\pi/3-h/6)\sin(h/6)>(1-\cos h)/6\). One elementary bound is \(2\sin(2\pi/3-h/6)\sin(h/6)\ge\sqrt3 h/(3\pi)>h^2/12\ge(1-\cos h)/6\) on this range. The case \(n=3\) follows directly. Monotonicity of cosine on the first half-circle and symmetry give all remaining signs. Consequently \(a=q_{J-1}>0\), \(b=-q_J>0\).

The signed kernel integrates to one. Its negative portion consists of all complete interior edges between negative vertices plus exactly two crossing-edge triangles. Summing their negative areas yields
\[
\int_{\partial P_n}(-K_n(v_0,y))_+\,d\mu_n(y)
=\frac1n\left[\sum_{j=J}^{n-J}(-q_j)-\frac{ab}{a+b}\right].
\]
The correction \(ab/(a+b)\) is **both** crossing-edge deficits, not an omitted endpoint contribution. The cosine progression satisfies
\[
\sum_{j=J}^{n-J}(-q_j)=-(n-2J+1)+k\frac{\sin((J-\tfrac12)h)}{\sin(h/2)}.
\]
Because \(\int K_n=1\), its absolute integral is one plus twice its negative integral. This proves the exact formula.

**4. Third-order residue law.** Put \(d=J-n/3\), which is \(0,2/3,1/3\) for \(n\equiv0,1,2\pmod3\), respectively; let \(h=2\pi/n\). Taylor expansion with these three fixed values gives, with \(S=\sum_{j=J}^{n-J}(-q_j)\) and \(R=ab/(a+b)\),
\[
S=\frac{2\sqrt3-2\pi/3}{h}+\sqrt3(-d^2+d+\tfrac16)h
+\left(\tfrac{d^3}{3}-\tfrac{d^2}{2}-\tfrac d6+\tfrac16\right)h^2+O(h^3),
\]
\[
R=\sqrt3(d-d^2)h+(\tfrac16-\tfrac d3)h^2+O(h^3).
\]
Here \(a+b\asymp h\), including when \(d=0\), so the quotient admits the displayed expansion without division by a vanishing leading coefficient. Since \(\|\mathcal P_n\|=1+(h/\pi)(S-R)\), subtraction gives
\[
\|\mathcal P_n\|=\frac13+\frac{2\sqrt3}{\pi}+\frac{\sqrt3 h^2}{6\pi}
+\frac{d(2d-1)(d-1)h^3}{6\pi}+O(h^4).
\]
Substituting the three values of \(d\) and \(h=2\pi/n\) completes the proof. Uniformity follows because there are only three fixed values of \(d\).

## Verification
Run `python verify.py` with Python 3, NumPy and SymPy. It independently forms Gram moments from edge integrals and inverts the Gram matrix, checks the exact formula against direct absolute-linear-edge integration for \(3\le n\le1000\), verifies the sign interval, checks rational values at three orders, and symbolically verifies the three cubic Taylor coefficients. A successful run emits `PASS 3065 assertion groups`. The finite checks are corroboration; the exact identities and the infinite asymptotic statement follow from the preceding analytical proof.

## Relationship to prior work
Hangelbroek, Narcowich, Sun and Ward (2010) develop \(L^p\) stability of least-squares projectors from smooth-manifold kernel spaces, including symmetric \(L^1\)/\(L^\infty\) bounds. They do not evaluate the present finite-dimensional affine projector on polygonal **arclength** or its arithmetic defect. Anderson, Ash, Jones, Rider and Saffari (2007) develop idempotent trigonometric-polynomial theory and Dirichlet kernels on the continuous circle; they do not treat polygon-boundary least squares.

The published result *Exact three-frequency Fourier projection norm on every cyclic group* gives the sampled vertex average of \(1+2\cos(2\pi j/n)\) and its arithmetic dependence on \(n\bmod3\). Its underlying measure is normalized **counting measure on the vertices**. Here the measure is **continuous arclength on polygon edges**, the coefficient is \(k=6/(2+\cos h)\), and each zero-crossing produces a triangular correction. Thus the sampled formula does not imply this norm or its cubic defect. For example, on orders divisible by three, the sampled norm has *negative* leading defect \(-2\pi\sqrt3/(3n^2)\), while the polygon-boundary defect is *positive* \(+2\pi\sqrt3/(3n^2)\). Related area-measure affine projections on filled polygons likewise concern a different operator and limit.

## Limitations
The result gives exact endpoint norms for affine projectors only, on regular polygonal perimeters with equal arclength density, not for general polygons, polynomial degrees above one, or higher dimensions. The \(n^{-3}\) residue effect does not imply monotonicity of the finite sequence. The public literature comparison is not an exhaustive historical priority certification; older numerical-analysis or boundary approximation literature under different terminology could contain equivalent identities.

## References
1. B. Anderson, J. M. Ash, R. Jones, D. G. Rider, B. Saffari, *Exponential sums with coefficients 0 or 1 and concentrated \(L^p\) norms*, arXiv:0705.0636v1 (first posted 2007-05-04). https://arxiv.org/abs/0705.0636
2. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424v1 (first posted 2010-05-13). https://arxiv.org/abs/1005.2424
3. *Exact three-frequency Fourier projection norm on every cyclic group*, published mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242
