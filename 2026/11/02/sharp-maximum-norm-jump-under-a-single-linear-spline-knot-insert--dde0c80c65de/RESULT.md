# Sharp maximum-norm jump under a single linear-spline knot insertion

## Finding

Let \(0<t<1\). In real \(L^2(0,1)\), let \(P_0\) be the orthogonal projector onto affine functions, and let \(P_t\) be the orthogonal projector onto continuous functions affine on each of \([0,t]\) and \([t,1]\), with no endpoint constraints. Both extend to bounded maps from \(L^\infty(0,1)\) to \(C[0,1]\). The exact, attained difference norm is

\[
\boxed{\|P_t-P_0\|_{L^\infty\to L^\infty}=\frac{12\max\{t,1-t\}}{(1+2t)(3-2t)}.}
\]

The unique minimum over all distinct interior knots occurs at the midpoint, where the norm is \(3/2\). It is strictly decreasing on \((0,1/2]\), strictly increasing on \([1/2,1)\), and has unattained supremum \(4\) as the knot approaches either endpoint. For every \(t\), an essentially bounded input taking only the signs \(\pm1\) attains the norm.

A sharp threshold for exceeding the classical universal bound on an *individual* one-dimensional linear-spline projector is
\[
\|P_t-P_0\|_{\infty\to\infty}>3
\quad\Longleftrightarrow\quad
0<t<1-\frac{\sqrt3}{2}
\ \text{ or }\ 
\frac{\sqrt3}{2}<t<1.
\]

There is a related non-convergence phenomenon even for a fixed smooth input: for \(f(x)=x^2\),
\[
((P_t-P_0)f)(0)=\frac{1-t}{4},\qquad
\lim_{t\downarrow0}\|(P_t-P_0)f\|_\infty=\frac14.
\]
Thus an interior knot that collapses into a boundary need not produce norm convergence of the least-squares fit to the affine fit, even on a fixed quadratic datum.

## Assumptions and scope

All functions and projectors are real. Integrals and inner products are with respect to Lebesgue measure, not empirical or endpoint-weighted measure. \(P_0\) is the projector onto \(\operatorname{span}\{1,x\}\), while \(P_t\) acts on the three-dimensional spline space. Input norms are essential suprema and output norms are ordinary suprema of continuous functions. Endpoint values of the projected functions are well defined. The same statement holds on any compact interval after an affine change of variable, with \(t\) interpreted as the relative knot position.

## Proof

**1. The one-dimensional detail space.** Put \(h_t(x)=(x-t)_+\). The refined spline space is the orthogonal sum of the affine space and the span of \(u_t=h_t-P_0h_t\). Solving the two moment equations \(\int_0^1u_t=\int_0^1xu_t=0\) gives
\[
u_t(x)=\begin{cases}
(1-t)^2\bigl[t-(1+2t)x\bigr],&0\le x\le t,\\
t^2\bigl[(3-2t)x+t-2\bigr],&t\le x\le1.
\end{cases}
\]
Consequently, for every bounded measurable input,
\[
(P_t-P_0)f=\frac{u_t}{\int_0^1u_t^2}\int_0^1f(y)u_t(y)\,dy.
\]
This identity establishes the norm formula \(\|P_t-P_0\|=\|u_t\|_\infty\|u_t\|_1/\|u_t\|_2^2\), with equality for \(f=\operatorname{sgn}u_t\) (arbitrary choices on its two zeroes).

**2. The three norms.** Direct integration gives
\[
\|u_t\|_2^2=\frac{t^3(1-t)^3}{3}.
\]
Its two interior zeroes are \(a_t=t/(1+2t)\) and \(b_t=(2-t)/(3-2t)\). They lie, respectively, in \((0,t)\) and \((t,1)\). As \(u_t\) has integral zero and signs \(+,-,+\), integrating the two positive triangles gives
\[
\|u_t\|_1=\frac{4t^2(1-t)^2}{(1+2t)(3-2t)}.
\]
Since \(u_t\) is affine on each cell, its maximum absolute value is achieved at a knot or endpoint. Its values at the three nodes are
\[
u_t(0)=t(1-t)^2,\quad u_t(t)=-2t^2(1-t)^2,\quad u_t(1)=t^2(1-t).
\]
The middle absolute value is at most the larger endpoint value because \(2\min\{t,1-t\}\le1\). Hence
\[
\|u_t\|_\infty=t(1-t)\max\{t,1-t\}.
\]
Combining all three identities proves the boxed formula and its attainment. The output norm is maximized at \(x=0\) when \(t<1/2\), at \(x=1\) when \(t>1/2\), and at \(x=0,1/2,1\) when \(t=1/2\).

**3. Knot minimax and endpoint limits.** Symmetry under \(x\mapsto1-x\) reduces minimization to \(0<t\le1/2\). There the norm equals \(12(1-t)/(3+4t-4t^2)\), whose derivative is
\[
-\frac{12(4t^2-8t+7)}{(1+2t)^2(3-2t)^2}<0.
\]
It follows that the midpoint is the unique minimizer, with value \(3/2\). Direct evaluation gives both endpoint limits equal to \(4\); neither endpoint is within the stated domain. For \(0<t\le1/2\), solving \(12(1-t)/(3+4t-4t^2)>3\) gives \(4t^2-8t+1>0\), or \(t<1-\sqrt3/2\). Reflection gives the other branch of the displayed threshold.

**4. Fixed smooth-data obstruction.** Direct integration yields
\[
\int_0^1x^2u_t(x)\,dx=\frac{t^2(1-t)^2}{12}.
\]
Substitution into the rank-one formula, using \(u_t(0)=t(1-t)^2\), shows \(((P_t-P_0)x^2)(0)=(1-t)/4\). For \(0<t\le1/2\), the first endpoint is an output maximizer, so the full norm on this datum equals \((1-t)/4\). This establishes the nonzero limit.

## Verification

The attached standalone `verify.py` uses exact symbolic integration to check the two orthogonality moments, the three norm expressions and the quadratic-data identity. Independently, it constructs the three-hat finite-element mass matrix and affine Gram inverse, calculates the refined-minus-coarse kernel at all knot pairs, integrates the absolute kernel exactly on each cell for rational knot positions, and checks the resulting row norms against the closed formula. It completes 905 exact-rational assertions, in addition to the symbolic integration identities. This finite cross-check does not replace the proof for every real \(0<t<1\).

## Relationship to prior work

Gawlik and Lew (2014 preprint, 2015 journal) study closeness of projectors onto nearby finite-element spaces under regularity and mesh assumptions; the inspected text concerns function-dependent convergence estimates rather than this exact operator-norm law for a single collapsing knot. Oswald (2006) surveys one-dimensional uniform boundedness of individual spline projections and proves a higher-dimensional instability result; neither the general individual-projector bound nor that higher-dimensional construction determines this difference norm. Dickopf and Krause (2014) study primarily non-nested transfer operators and numerical \(L^2\)/\(H^1\) performance, not the present nested one-knot endpoint formula. The residual \(u_t\) can also be viewed as a first nonuniform Franklin detail function; earlier Franklin-system calculations may contain an equivalent identity, and priority is not claimed as conclusively established.

## Limitations

The result assumes exactly one inserted interior knot, full endpoint freedom and unweighted \(L^2\) projection on one interval. It does not determine changes caused by a knot insertion in a larger pre-existing mesh, arbitrary density weights, discontinuous splines, or higher polynomial degrees. The supremum \(4\) is a limit over \(t\), not an operator norm attained at a degenerate endpoint knot. The extremizing input \(\operatorname{sgn}u_t\) is an \(L^\infty\) function; continuously varying approximants can approach the same norm but need not attain it.

## References

- E. S. Gawlik and A. J. Lew, *Supercloseness of Orthogonal Projections onto Nearby Finite Element Spaces*, arXiv:1408.4104, first posted 2014-08-18; ESAIM: M2AN 49 (2015), 559–576. https://arxiv.org/abs/1408.4104
- P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573, first posted 2006-11-19. https://arxiv.org/abs/math/0611573
- T. Dickopf and R. Krause, *Evaluating Local Approximations of the \(L^2\)-Orthogonal Projection Between Non-Nested Finite Element Spaces*, Numer. Math. Theor. Meth. Appl. 7 (2014), 288–316; DOI:10.4208/nmtma.2014.1218nm. https://www.global-sci.com/nmtma/article/view/14057
