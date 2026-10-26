# Exact endpoint stability for alternating-knot linear spline projections

## Finding

Fix real numbers \(a,b>0\). On the real line take the bi-infinite knot sequence \(t_{2k}=k(a+b)\), \(t_{2k+1}=k(a+b)+a\), for every \(k\in\mathbb Z\). Let \(V_{a,b}\subset L^2(\mathbb R)\) be the closed space of continuous functions affine on every knot interval, and let \(P_{a,b}\) be its orthogonal \(L^2\) projection, extended by its absolutely integrable kernel to \(L^1\) and \(L^\infty\).

The sharp endpoint operator norms are
\[
\boxed{\|P_{a,b}\|_{L^1\to L^1}=\|P_{a,b}\|_{L^\infty\to L^\infty}=\Lambda(a,b)
=\frac{5a^2+22ab+5b^2}{3a^2+10ab+3b^2}
=2-\frac{(a-b)^2}{(3a+b)(a+3b)}.}
\]
Consequently, writing \(\eta=|a-b|/(a+b)\),
\[
\Lambda(a,b)=2-\frac{\eta^2}{4-\eta^2},\qquad \frac53<\Lambda(a,b)\le2.
\]
Equality \(\Lambda=2\) holds precisely at equal spacing; \(\Lambda\) strictly decreases with \(\eta\), and its unattained infimum over positive spacings is \(5/3\), approached when the mesh ratio tends to zero or infinity.

There is a finite-periodic consequence: for every integer \(m\ge2\), form the circle of circumference \(m(a+b)\) with its \(2m\) consecutive knot intervals alternating between \(a\) and \(b\). If \(P^{\mathrm{per}}_{m;a,b}\) is the orthogonal projection onto the continuous piecewise-affine periodic splines, then
\[
\boxed{\|P^{\mathrm{per}}_{m;a,b}\|_{L^1\to L^1}
=\|P^{\mathrm{per}}_{m;a,b}\|_{L^\infty\to L^\infty}\le\Lambda(a,b),\quad
\lim_{m\to\infty}\|P^{\mathrm{per}}_{m;a,b}\|=\Lambda(a,b).}
\]
Thus the displayed rational constant is also the **exact best uniform endpoint stability constant over all numbers of two-cell repeats**. No exact formula for each finite \(m\) is asserted.

## Assumptions and scope

The function spaces use Lebesgue measure, not a discrete knot measure. Functions may be real or complex. The projection kernel is the continuous hat-basis reproducing kernel. The \(L^\infty\) domain of the extended operator is all essentially bounded measurable functions; its restriction to \(L^2\cap L^\infty\) has the same sharp norm. The finite-circle spaces are genuine periodic \(L^2\) spline spaces, not interpolation spaces. Only strictly positive alternating lengths are considered; zero length is a limiting degeneration, not an admissible knot interval.

## Proof

**1. Gram operator and resolvent.** Let \(\phi_j\) be the nodal hat at \(t_j\) and \(h_{2k}=a\), \(h_{2k+1}=b\). The Gram matrix \(\mathsf G=(\langle\phi_i,\phi_j\rangle)\), as an operator on \(\ell^2(\mathbb Z)\), has \(6\mathsf G=J\) with diagonal \(2(a+b)\), and off-diagonals \(J_{j,j+1}=J_{j+1,j}=h_j\). Since \(2(a+b)>a+b\), the symmetric band matrix \(J\) is boundedly invertible. Conjugating by signs \((-1)^j\) makes its off-diagonals negative and its inverse entrywise positive (Neumann series after diagonal scaling). Its inverse entries decay geometrically, so the associated integral projection kernel is absolutely integrable in either variable.

Set \(S=a+b\), \(c=3a^2+8ab+3b^2\), \(d=2ab\), \(F=\sqrt{c^2-d^2}\), and \(\rho=d/(c+F)\in(0,1)\). In the even/odd Bloch representation, the signed Gram matrix has symbol
\[
\begin{pmatrix}2S&-a-be^{-i\theta}\\-a-be^{i\theta}&2S\end{pmatrix},
\quad \det=c-d\cos\theta.
\]
The Fourier coefficients of its reciprocal determinant are \(\rho^{|k|}/F\). Consequently, if \(g_j=(-1)^j(J^{-1})_{0j}>0\), then for all integers \(k\),
\[
\begin{aligned}
g_{2k}&=D\rho^{|k|},\\
g_{2k+1}&=\begin{cases}E\rho^k,&k\ge0,\\H\rho^{-k-1},&k\le-1,\end{cases}\\
D&=\frac{2S}{F},\qquad E=\frac{a+b\rho}{F},\qquad H=\frac{b+a\rho}{F}.
\end{aligned}
\]
In particular, the \(L^2\) projector has a continuous kernel \(K\) with \(K(t_0,t_j)=6(-1)^j g_j\). Its restriction to each knot interval is affine in the second argument.

**2. Exact row integral.** For positive \(u,v\), let \(\mathcal J(u,v)=(u^2+v^2)/(2(u+v))\), the integral over the unit interval of the modulus of the affine function joining \(u\) and \(-v\). Adjacent nodal values of \(K(t_0,\cdot)\) have opposite signs. Summing the four types of knot interval and their geometric tails gives
\[
\int_\mathbb R|K(t_0,y)|\,dy
=\frac6{1-\rho}\left[
 a\mathcal J(D,E)+b\mathcal J(E,\rho D)
 +b\mathcal J(D,H)+a\mathcal J(H,\rho D)\right]. \tag{1}
\]
The identity \(d\rho^2-2c\rho+d=0\), together with \(F=c-d\rho\), simplifies (1) exactly to
\[
\frac{5a^2+22ab+5b^2}{(3a+b)(a+3b)}.\tag{2}
\]
For reproducibility, the accompanying exact-arithmetic checker clears all rational denominators in (1) minus (2) and checks that the numerator is divisible by \(d\rho^2-2c\rho+d\). This checks the critical algebraic cancellation, not merely its decimal values.

**3. Global and attained norm.** For fixed \(y\), the function \(x\mapsto K(x,y)\) is affine between knots. Hence \(x\mapsto\int|K(x,y)|\,dy\) is convex on each knot interval and is bounded by the larger of its endpoint values. Translation by \(a+b\), and reflection \(x\mapsto a-x\), take all knots to one another and preserve the mesh; all nodal absolute row integrals therefore equal (2). This proves the sharp \(L^\infty\) bound. The choice \(f(y)=\operatorname{sgn}\overline{K(t_0,y)}\) gives equality for the bounded integral-kernel extension; its compactly supported truncations give the same supremum over \(L^2\cap L^\infty\). Symmetry of \(K\) and Tonelli's theorem give the equal sharp \(L^1\) norm. Positivity of \(a,b\) and direct differentiation of \(\eta^2/(4-\eta^2)\) yield the strict contrast dependence and boundary limits.

**4. Finite periodic meshes.** Let \(T=m(a+b)\). The periodic knot Gram operator is the quotient of the bi-infinite Gram operator by the shift of \(2m\) indices. Absolute summability of the inverse rows proves that the finite periodic projection kernel is the periodization
\[
K_m(x,y)=\sum_{k\in\mathbb Z}K(x,y+kT),\qquad 0\le x,y<T.
\]
The triangle inequality therefore yields \(\int_0^T|K_m(x,y)|dy\le\int_\mathbb R|K(x,y)|dy\le\Lambda(a,b)\). Conversely, at the knot \(x=t_0\), the exponential decay of the inverse Gram rows makes the periodization error tend to zero in \(L^1\) as \(m\to\infty\). Hence the finite-circle endpoint norms converge to (2), proving that the uniform bound is sharp.

## Verification

Run `python CHECKER.py` with Python 3 and SymPy 1.12 or later. The checker performs an exact polynomial-remainder proof of the cancellation in (1), forms the periodic Gram matrices for positive rational spacings, inverts them over exact rational arithmetic, integrates each signed affine kernel row exactly, checks row symmetry and the predicted sharp upper bounds, and checks the finite-period convergence numerically using exact-rational differences. Its finite examples do not prove the universal theorems; Steps 1–4 above do.

## Relationship to prior work

Ciesielski's classical one-dimensional uniform \(L^\infty\) bound of \(3\) for linear-spline least-squares projections is recalled in Oswald's 2006 preprint, whose main new theorem concerns failure of dimension-independent bounds in higher dimensions. Passenbrunner's 2016 preprint develops \(L^\infty\) stability for periodic orthogonal spline projections with arbitrary knots and addresses bi-infinite knot sequences. These sources provide the qualitative stability setting, not the rational two-spacing endpoint profile (2) or the exact sharp uniform-in-repeat envelope. The result here concerns orthogonal projection, not cardinal spline interpolation. A related 2012 paper of Oswald on \(L^\infty\) bounds for linear spline spaces was accessible only in abstract form, leaving a literature-comparison risk; its full text has not been established to exclude an equivalent calculation.

## Limitations

The theorem is limited to continuous degree-one splines with exactly alternating positive lengths; it asserts neither an optimal bound over all nonuniform meshes nor a comparable law for higher-degree splines. The finite-circle bound is optimal as a supremum over repeat counts, not asserted to be attained for any given finite count. The novelty assessment is based on the inspected accessible primary papers and searches; inaccessible or unindexed equivalent presentations could affect historical priority. Independent validation has not occurred.

## References

1. P. Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573, first posted 2006-11-19; complete HTML text inspected, especially Introduction and Sections 2–3. https://arxiv.org/abs/math/0611573
2. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720, first posted 2016-08-24; complete HTML text inspected, especially Sections 1, 3, and 5. https://arxiv.org/html/1608.06720v2
3. P. Oswald, *\(L^\infty\)-Bounds for the \(L^2\)-Projection onto Linear Spline Spaces*, 2012, DOI:10.1007/978-1-4614-4565-4_24; abstract inspected, full text not obtained. https://doi.org/10.1007/978-1-4614-4565-4_24
