# Sharp three-knot periodic linear-spline projection bound

## Finding

Let a circle have three distinct cyclic knots separated by arcs of arbitrary lengths \(a,b,c>0\). Let \(S_{a,b,c}\) consist of continuous functions that are affine on each arc, and let \(P_{a,b,c}:L^2\to S_{a,b,c}\) be the unweighted orthogonal projection for arclength measure. For every choice of positive arc lengths,
\[
\boxed{\|P_{a,b,c}\|_{L^\infty\to L^\infty}<\frac73.}
\]
The constant is sharp over all three-knot circles:
\[
\boxed{\sup_{a,b,c>0}\|P_{a,b,c}\|_{L^\infty\to L^\infty}=\frac73,}
\]
and no positive triple attains this supremum. In fact, the norm tends to \(7/3\) along the hierarchically collapsing mesh \((a,b,c)=(\varepsilon^2,1,\varepsilon)\) as \(\varepsilon\downarrow0\). The three equally spaced arcs instead yield the exact norm \(16/9\).

## Assumptions and scope

The circle circumference is \(a+b+c\), and length scaling leaves the operator norm unchanged. All three arc lengths are strictly positive. Inputs are real or complex essentially bounded functions with respect to arclength; the projector has the same sharp endpoint norm in both cases. The range uses ordinary continuous, periodic, piecewise-affine hat splines without weights or endpoint boundary conditions. No assertion is made here about circles with four or more knots or higher-order splines.

## Proof

**Kernel reduction.** Label the knot vertices \(0,1,2\), with directed arc lengths \(a:0\to1\), \(b:1\to2\), \(c:2\to0\), and let \(\phi_j\) be the nodal hat functions. The Gram matrix is
\[
G=\frac16\begin{pmatrix}
2(a+c)&a&c\\ a&2(a+b)&b\\ c&b&2(b+c)
\end{pmatrix}.
\]
It is positive definite because the three hats are linearly independent. The reproducing kernel is \(K(x,y)=\phi(x)^{\mathsf T}G^{-1}\phi(y)\). The exact operator norm equals \(\sup_x\int|K(x,y)|\,dy\): for each fixed \(x\), its sign is a norming bounded input. Since \(K(x,\cdot)\) is affine in \(x\) between consecutive knots, its integral absolute value is convex there. Therefore the supremum over \(x\) is attained at some knot. Cyclic relabeling reduces the required bound to knot \(0\) for arbitrary positive \(a,b,c\).

Define
\[
D=(a+b+c)(ab+ac+bc),\quad
A=4ab+4ac+3b^2+4bc,\quad
X=2a(b+c)-bc,\quad Y=2c(a+b)-ab.
\]
The three nodal values of \(K(0,\cdot)\) are exactly \((A,-X,-Y)/D\). Also \(K\) reproduces constants, so \(\int K(0,y)\,dy=1\). Write \(Q\) for the integral of the negative part of this kernel. Its absolute integral is \(1+2Q\). On an arc of length \(h\), a linear function with endpoint values \(u>0>v\) has negative-area integral \(hv^2/[2(u-v)]\); when both endpoint values are negative, this area is \(-h(u+v)/2\). These formulas also apply by continuity when an endpoint is zero.

**Case 1: \(X,Y\ge0\).** The nodal signs are positive, nonpositive, nonpositive. Direct integration yields
\[
Q=\frac1{2D}\left(\frac{aX^2}{A+X}+b(X+Y)+\frac{cY^2}{A+Y}\right).
\]
Using \(A+X=3(2a+b)(b+c)\) and \(A+Y=3(a+b)(b+2c)\), exact reduction gives
\[
\frac23-Q=\frac{R(a,b,c)}{6(a+b)(2a+b)(b+c)(b+2c)(ab+ac+bc)},
\]
where
\[
\begin{aligned}
R={}&8a^3c^3+20ba^2c^2(a+c)
 +2b^2ac(8a^2+17ac+8c^2)\\
&+4b^3(a+c)(a^2+4ac+c^2)
 +2b^4(3a^2+2ac+3c^2)+b^5(a+c).
\end{aligned}
\]
Every displayed summand and each denominator factor is strictly positive. Hence \(Q<2/3\).

**Case 2: \(X<0\).** The inequality \(2a(b+c)<bc\) implies \(a<c/2\), and therefore \(Y=2c(a+b)-ab>0\). The nodal signs are positive, positive, negative. The negative portion lies in arcs \(b,c\). Integrating and using \(Y-X=3b(c-a)\) yields
\[
Q=\frac{Y^2(b+c)}{6(c-a)(a+b)(b+2c)(ab+ac+bc)}.
\]
Put \(z=bc/a-2(b+c)>0\), so \(a=bc/[2(b+c)+z]\). Algebraic simplification produces
\[
\frac23-Q=
\frac{T(b,c,z)}{6(b+2c)(b+2c+z)(2b+3c+z)(3b+3c+z)},
\]
with
\[
\begin{aligned}
T={}&6(b+c)(b+2c)^2(b+3c)\\
&+(b+2c)(11b^2+49bc+42c^2)z\\
&+4(b^2+7bc+8c^2)z^2+4cz^3.
\end{aligned}
\]
All coefficients and factors are strictly positive, so again \(Q<2/3\).

**Case 3: \(Y<0\).** Interchanging \(a\) and \(c\) reduces this case to Case 2. Indeed, then \(X>0\). The cases exhaust all positive triples, including equality boundaries, so the operator norm is always strictly less than \(7/3\).

**Sharpness.** Set \(a=\varepsilon^2\), \(b=1\), \(c=\varepsilon\) with sufficiently small \(\varepsilon>0\). Here \(X=\varepsilon(2\varepsilon^2+2\varepsilon-1)<0\) and \(Y=\varepsilon(2\varepsilon^2-\varepsilon+2)>0\). The Case 2 formula gives
\[
\lim_{\varepsilon\downarrow0}Q=\frac23,
\quad
\lim_{\varepsilon\downarrow0}\int|K(0,y)|\,dy=\frac73.
\]
The universal upper bound forces the full norm to have the same limit. Strict positivity in the two algebraic certificates proves nonattainment for every fixed positive mesh. At \(a=b=c\), direct inversion yields the row \((5,-1,-1)/(3a)\), whose absolute integral is \(16/9\).

## Verification

The accompanying standalone script `check.py` reconstructs the inverse Gram matrix, checks the polynomial positivity identities symbolically, evaluates the absolute-affine-kernel formula independently at 2,187 rational knot/vertex instances, checks all three sign regimes, and verifies the exact \(\varepsilon\downarrow0\) limit. These finite checks are supplementary: the strict universal inequality and the limiting sharpness follow from the displayed symbolic identities and elementary integration for every admissible real positive triple. Run with `python check.py` in an environment containing SymPy.

## Relationship to prior work

Passenbrunner's *Orthogonal projectors onto spaces of periodic splines* (first public arXiv version dated 2016-08-24, arXiv:1608.06720) proves degree-dependent uniform boundedness for arbitrary periodic knots (Theorem 1.4), but its theorem does not specify the exact three-knot constant or a nonattaining extremal mesh. Passenbrunner and Shadrin's 2013 arXiv:1308.4824 concerns convergence and inverse Gram-matrix estimates for nonperiodic splines. Kayumov's 2004 arXiv:math/0408418 discusses the broader mesh-independent constant \(3\) for second-order spline projectors on intervals, which is weaker than the sharp three-knot periodic constant above. A uniform three-knot computation and a four-knot alternating-mesh calculation concern restricted families and do not determine the all-mesh three-knot envelope.

## Limitations

This is an exact statement only for continuous linear splines with exactly three distinct knots on one circle and unweighted arclength. It gives the sharp supremum over positive length triples, not an explicit single closed formula for the maximum of the three nodal norms on every mesh (although the proof provides a finite exact evaluation procedure). The supremum requires a degenerating family; no positive length triple attains it. A complete search of unpublished or unindexed historical computations is not established, so priority and independent verification remain open.

## References

1. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720, first posted 2016-08-24; Sections 1.2–3, especially Theorem 1.4. https://arxiv.org/abs/1608.06720
2. M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824, first posted 2013-08-22; Sections 1, 4–5. https://arxiv.org/abs/1308.4824
3. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first posted 2004-08-30; abstract and Introduction. https://arxiv.org/abs/math/0408418
