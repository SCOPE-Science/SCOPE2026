# Exact two-coset Poisson Gabor frame bounds and optimal frequency staggering

## Finding

Fix a width \(w>0\) and a staggering parameter \(0<\delta<1\). Define
\[
g_w(t)=\frac{1}{t^2+w^2},\qquad
\Lambda_\delta=\mathbb Z\cup(\mathbb Z+\delta),
\]
and consider the collection
\[
\mathcal G_{w,\delta}
=\{e^{2\pi i m t}g_w(t-n):n\in\mathbb Z,\ m\in\Lambda_\delta\}
\]
in \(L^2(\mathbb R,dt)\), with the two frequency cosets counted once each. Write \(a=\pi w\) and \(d=\min\{\delta,1-\delta\}\). Then the collection is a frame for every specified \(w,\delta\), with **exact optimal squared frame bounds**
\[
\boxed{A(w,\delta)=\frac{2\pi^2}{w^2}\operatorname{sech}^2(a)\sinh^2(ad),}
\]
\[
\boxed{B(w,\delta)=\frac{\pi^2}{w^2}\operatorname{csch}^2(a)
 [\cosh^2(a)+\cosh^2(a(1-2\delta))].}
\]
Both \(A(w,\delta)\) and \(B(w,\delta)\) are symmetric under \(\delta\mapsto1-\delta\). Among all staggering parameters \(0<\delta<1\), the **unique** optimal choice \(\delta=1/2\) simultaneously maximizes the sharp lower bound, minimizes the sharp upper bound, and minimizes the condition number \(B/A\). As \(\delta\downarrow0\),
\[
A(w,\delta)=2\pi^4\operatorname{sech}^2(\pi w)\delta^2+O_w(\delta^4),
\quad
B(w,\delta)\longrightarrow\frac{2\pi^2}{w^2}\coth^2(\pi w).
\]
Thus coalescence of the two frequency cosets causes an exact quadratic loss in stable reconstruction.

## Assumptions and scope

There is no restriction on \(w\) beyond positivity or on \(\delta\) beyond \(0<\delta<1\). Modulations use \(e^{2\pi i m t}\), translations are by integers, and \(g_w\) is not normalized to unit norm. By optimal frame bounds we mean the largest \(A\) and smallest \(B\) satisfying
\[
A\|f\|_2^2\le\sum_{n\in\mathbb Z}\sum_{m\in\Lambda_\delta}
|\langle f,e^{2\pi i m(\cdot)}g_w(\cdot-n)\rangle|^2
\le B\|f\|_2^2
\]
for every \(f\in L^2(\mathbb R)\). The theorem concerns the two-coset *nonlattice* system; \(\delta=1/2\) is the one parameter at which the union becomes the regular half-frequency lattice.

## Proof

**1. Unitary Zak reduction.** For Schwartz \(f\), set
\[
(Zf)(x,\omega)=\sum_{n\in\mathbb Z}f(x+n)e^{-2\pi i n\omega},
\quad 0\le x,\omega<1.
\]
It extends by density to a unitary transformation from \(L^2(\mathbb R)\) to \(L^2([0,1)^2)\). Parseval on the fundamental square shows that the critical lattice \(\{M_mT_n g:m,n\in\mathbb Z\}\) has frame operator equal to multiplication by \(|Zg|^2\). A second frequency coset corresponds, up to phases of modulus one, to the window \(M_\delta g\), with \(|Z(M_\delta g)(x,\omega)|^2=|Zg(x,\omega-\delta)|^2\). Therefore the operator for the union is multiplication by
\[
S_\delta(x,\omega)=|Zg_w(x,\omega)|^2+
|Zg_w(x,\{\omega-\delta\})|^2,
\]
where \(\{\cdot\}\) is the fractional part. Its essential minimum and maximum are the optimal bounds. Since \(g_w\) has sufficient decay, the resulting symbol is continuous on the Zak torus, so these extrema are attained.

**2. Exact fiber and monotonicity in translation phase.** With the Fourier convention \(\widehat g(\xi)=\int_{\mathbb R}g(t)e^{-2\pi i\xi t}dt\), one has \(\widehat g_w(\xi)=\pi w^{-1}e^{-2\pi w|\xi|}\). Poisson summation, applied for \(0\le\omega<1\), gives
\[
Zg_w(x,\omega)=\frac{\pi}{w}e^{2\pi i x\omega}
\left(\frac{u}{1-rz}+\frac{v}{z-r}\right),
\quad z=e^{2\pi i x},\quad r=e^{-2a},
\quad u=e^{-2a\omega},\quad v=e^{-2a(1-\omega)}.
\]
Both \(p=u-rv\) and \(q=v-ru\) are nonnegative; they are not simultaneously zero. With \(c=\cos(2\pi x)\), direct simplification yields
\[
|Zg_w(x,\omega)|^2=\frac{\pi^2}{w^2}
\frac{p^2+q^2+2pq c}{(1+r^2-2rc)^2}.
\]
Its derivative with respect to \(c\) is strictly positive: after multiplying by the positive cube of the denominator, the numerator is
\[
2pq(1+r^2-2rc)+4r(p^2+q^2+2pqc)>0.
\]
Hence every summand of \(S_\delta\) is minimized when \(x=1/2\), and maximized when \(x=0\). This reduces both global extrema to one-dimensional angular problems. Evaluating the preceding formula at these two phases gives
\[
|Zg_w(1/2,\omega)|^2=\frac{\pi^2}{w^2}
\operatorname{sech}^2(a)\sinh^2(2a(\omega-1/2)),
\]
\[
|Zg_w(0,\omega)|^2=\frac{\pi^2}{w^2}
\operatorname{csch}^2(a)\cosh^2(2a(\omega-1/2)).
\]

**3. Exact frequency extrema.** Consider the two intervals \(0\le\omega<\delta\) and \(\delta\le\omega<1\). In the first interval, the arguments \(\omega-1/2\) and \(\{\omega-\delta\}-1/2\) are separated by \(1-\delta\), and in the second they are separated by \(\delta\). Both \(y\mapsto\sinh^2(2ay)\) and \(y\mapsto\cosh^2(2ay)\) are strictly convex. For a pair of arguments at fixed separation and symmetric available domain, the sum of the \(\sinh^2\)-terms is minimized at their midpoint; its value is twice \(\sinh^2\) evaluated at half that separation. Choosing the shorter separation \(d\) gives the global minimum
\[
\min_{x,\omega}S_\delta(x,\omega)
=\frac{2\pi^2}{w^2}\operatorname{sech}^2(a)\sinh^2(ad).
\]
A minimizing fiber is \((x,\omega)=(1/2,(1+\delta)/2)\) for \(\delta\le1/2\), and \((1/2,\delta/2)\) for \(\delta\ge1/2\); at equality both descriptions give minimizing fibers. Each sum of \(\cosh^2\)-terms is strictly convex, so its maximum on the closure of either interval occurs at an endpoint. Evaluating at \(\omega=0\) or \(\omega=\delta\) yields
\[
\max_{x,\omega}S_\delta(x,\omega)
=\frac{\pi^2}{w^2}\operatorname{csch}^2(a)
[\cosh^2(a)+\cosh^2(a(1-2\delta))].
\]
The upper bound is attained at \((0,0)\) and \((0,\delta)\). Both exact constants are positive and finite.

**4. Optimal staggering and degeneration.** On \(0<\delta\le1/2\), \(d=\delta\), so \(\sinh^2(ad)\) is strictly increasing. On the same interval, \(\cosh^2(a(1-2\delta))\) is strictly decreasing. Symmetry gives strict reversal on the second half of the parameter interval, proving all uniqueness assertions, including the ratio \(B/A\). Taylor's formula \(\sinh(ad)=ad+O_w(\delta^3)\) proves the quadratic asymptotic; continuity proves the upper-limit statement.

## Verification

The standalone standard-library checker `verify.py` computes the closed Zak fibers, compares the predicted extrema against every point of finite angular grids, compares them with independently truncated bilateral lattice sums, and checks the \(\delta=1/2\) reduction to the classical frequency-half lattice. Its observed output is:

`CHECK_OK: exact Zak extremal fibers, numeric grid, direct sums, and balanced-lattice limit`

These numerical tests are corroborative; the inequalities for all parameters follow from the explicit positive derivative and strict convexity argument above.

## Relationship to prior work

The recent full-text study of de Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor (first posted 2026-08-05) characterizes frame *existence* for continuous integrable totally positive windows over rectangular lattices. The present rational window has only polynomial decay and is not within that class; moreover the frequency set is nonlattice for \(\delta\ne1/2\), and the present claim is about exact sharp constants and their optimizer. Belov, Kulikov, and Lyubarskii's earlier full-text rational-window study concerns frame sets for rectangular lattices and certain sampling constructions, not the sharp two-frequency-coset spectral profile. Ghosh's 2026-09-16 paper treats a different even rational window and primarily lattice frame/non-frame regions; only its accessible abstract could be checked here.

Previously established exact integer-factor Poisson Gabor bounds include the regular frequency-half lattice, corresponding to the single parameter \(\delta=1/2\). The formulas here agree there exactly but determine the entire nonlattice staggering family, its unique optimal spacing, and the sharp quadratic coalescence constant. Classical unitary Zak diagonalization and the Fourier transform of the Poisson window are used, not claimed as novel.

## Limitations

The result applies to unit translation spacing, two unit-frequency cosets, and the unscaled rational window specified above; it does not determine bounds for arbitrary irregular frequency sets, arbitrary shifts of translations, or other rational windows. The checked literature may omit an earlier equivalent formula in the extensive Zak-transform/frame-bound literature. Independent validation and exhaustive historical-priority confirmation have not been performed.

## References

1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1, first posted 2026-08-05. https://arxiv.org/abs/2608.04992
2. Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959v1, first posted 2021-03-16; *Inventiones mathematicae* 231 (2023), 431–466. https://doi.org/10.1007/s00222-022-01151-8
3. R. Ghosh, *Gabor Frame Regions and Non-Frame Obstructions for an even Rational Window*, arXiv:2609.19232v1, first posted 2026-09-16. https://arxiv.org/abs/2609.19232
