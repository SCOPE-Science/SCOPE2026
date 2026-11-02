# Exact endpoint stability of two-periodic linear-spline projections

## Finding

Let \(a,b>0\). Put knots \((t_j)_{j\in\mathbb Z}\) on the real line with \(t_0=0\) and successive gaps \(t_{j+1}-t_j=a\) for even \(j\), \(b\) for odd \(j\). Let \(S_{a,b}\subset L^2(\mathbb R)\) be the closed space of continuous, piecewise-affine splines on these knots and \(P_{a,b}\) its orthogonal projector. Its integral kernel is absolutely integrable in the second variable and hence extends the projector to bounded inputs. With \(s=a+b\) and \(p=ab\), the *exact, attained* endpoint norm is
\[
\boxed{\|P_{a,b}\|_{L^\infty\to L^\infty}=\frac{5s^2+12p}{3s^2+4p}.}
\]
Consequently its value lies strictly between \(5/3\) and \(2\); the upper bound \(2\) occurs exactly when \(a=b\), and the lower bound \(5/3\) is approached but never attained as \(a/b\to0\) or \(\infty\). A signed kernel input attaining the norm exists.

For an even number \(2m\ge4\) of alternating gaps \(a,b\) on a circle, let \(P^{\mathrm{cyc}}_{m;a,b}\) be the orthogonal projection onto continuous periodic linear splines. Then
\[
\|P^{\mathrm{cyc}}_{m;a,b}\|_{L^\infty\to L^\infty}<\frac{5s^2+12p}{3s^2+4p},\qquad
\lim_{m\to\infty}\|P^{\mathrm{cyc}}_{m;a,b}\|=\frac{5s^2+12p}{3s^2+4p}.
\]
Therefore the sharp common bound over this complete two-periodic family, including all even cyclic sizes, is \(2\), with no finite-circle equality case.

## Assumptions and scope

All functions and operators are real. The scalar product is Lebesgue \(L^2\) on the line or arclength \(L^2\) on the finite circle; a common positive rescaling of the measure does not change the projector. The term *linear spline* means continuous piecewise polynomial of degree at most one. On the line the spline space is its closed \(L^2\) subspace; bounded inputs are handled through the absolutely convergent integral kernel rather than identifying \(L^\infty\) with \(L^2\). Circle lengths are \(m(a+b)\). The quantity being optimized is the induced essential-supremum norm of this **canonical orthogonal projector**, not a best-approximation constant over all projectors.

## Proof

**1. Hat Gram matrix and reduction to nodes.** Write \(\phi_j\) for the nodal hat function equal to one at \(t_j\) and zero at all other knots. The Gram operator \(G=(\langle\phi_i,\phi_j\rangle)\) has
\[
G_{jj}=s/3,\qquad G_{j,j+1}=G_{j+1,j}=h_j/6,\quad h_{2k}=a,\ h_{2k+1}=b,
\]
with all other entries zero. It is strictly diagonally dominant, positive and invertible on \(\ell^2(\mathbb Z)\), since the sum of off-diagonal entries per row is \(s/6<s/3\). Consequently the kernel at knot \(t_0\) has nodal values \(g_j=(G^{-1})_{0j}\). At an interior evaluation point, the kernel is the same convex combination of the two adjacent nodal kernel rows; convexity of the \(L^1\) norm shows that a maximizing evaluation point may be chosen at a knot. Two-periodic translations and reflection across any knot-adjacent edge interchange the two parity classes, so all knot-row norms agree.

**2. Positive Green recurrence.** The diagonal sign gauge \(v_j=(-1)^jg_j\) turns \(G\) into a strictly diagonally dominant symmetric \(M\)-matrix, so all \(v_j>0\). Put \(x_k=v_{2k}\), \(y_k=v_{2k+1}\). The Green equations are
\[
2s x_k-a y_k-b y_{k-1}=6\mathbf1_{k=0},\qquad
2s y_k-a x_k-b x_{k+1}=0.
\]
Eliminating the odd coordinates gives
\[
(3s^2+2p)x_k-p(x_{k-1}+x_{k+1})=12s\mathbf1_{k=0}.
\]
There is a unique \(\lambda\in(0,1)\) such that \(\lambda+\lambda^{-1}=2+3s^2/p\). Inverting this scalar recurrence yields
\[
 x_k=C\lambda^{|k|},\qquad C=\frac{12s}{p(\lambda^{-1}-\lambda)},\qquad
 y_k=\frac{a x_k+b x_{k+1}}{2s}.
\]
These formulas give absolute summability and justify the integral-kernel extension.

**3. Exact row integration.** Adjacent coefficients \(g_j,g_{j+1}\) have opposite signs. For positive \(u,v\), the absolute integral of the linear interpolant between \(u\) and \(-v\) over an interval of length \(h\) is
\[
\frac h2\frac{u^2+v^2}{u+v}.
\]
Set \(\alpha=(a+b\lambda)/(2s)\) and \(\beta=(a\lambda+b)/(2s)\). Summing the right-hand and left-hand geometric tails, respectively, gives
\[
\|P_{a,b}\|=\frac{C}{2(1-\lambda)}\left[
 a\frac{1+\alpha^2}{1+\alpha}
 +b\frac{\alpha^2+\lambda^2}{\alpha+\lambda}
 +a\frac{\lambda^2+\beta^2}{\lambda+\beta}
 +b\frac{1+\beta^2}{1+\beta}\right].
\]
Substitute the definitions of \(\alpha,\beta,C\), combine fractions, and use \(p\lambda^2-(3s^2+2p)\lambda+p=0\). The right side reduces **identically** to \((5s^2+12p)/(3s^2+4p)\). `verify.py` reproduces this polynomial remainder identity symbolically; the displayed recurrence and geometric sums establish it for all positive \(a,b\). Taking the input \(f(y)=\operatorname{sgn}K(t_0,y)\) realizes the absolute kernel-row integral. (Its value at isolated zero crossings is irrelevant.)

**4. Sharp contrast dependence.** Put \(u=p/s^2\). For positive \(a,b\), \(0<u\le1/4\), with equality precisely for \(a=b\); the norm is \((5+12u)/(3+4u)\), whose derivative is \(16/(3+4u)^2>0\). Its endpoint values give the claimed sharp interval.

**5. Finite circles and strict periodization loss.** For \(2m\ge4\), the finite cyclic Gram inverse is obtained by periodizing the exponentially decaying infinite inverse along indices modulo \(2m\). Accordingly each cyclic knot kernel is the periodized line kernel. The triangle inequality for its absolute integral yields \(\|P^{\mathrm{cyc}}_{m;a,b}\|\le\|P_{a,b}\|\). Strictness follows already for the two translates of the edge \([t_0,t_1]\): the infinite kernel on the original edge crosses zero at fractional position \(1/(1+\alpha)\), whereas its translate from edge indexed \(-2m\) crosses zero at \(1/(1+\beta/\lambda)\). The latter is strictly smaller, because \(\beta/\lambda-\alpha=b(1-\lambda^2)/(2s\lambda)>0\). On the open interval between these two crossings, the two summands have opposite signs, so the integral triangle inequality is strict. The same strictness holds at every cyclic knot by symmetry, and convexity excludes a larger interior norm. Finally geometric decay and periodization show the cyclic kernels converge in row \(L^1\) to the infinite kernel as \(m\to\infty\), proving the asserted limit.

## Verification

Running `python verify.py` with SymPy checks the rational-function identity by reducing its numerator modulo \(p\lambda^2-(3s^2+2p)\lambda+p\). Separately, the program builds and inverts **finite periodic Gram matrices over exact rational arithmetic**, computes every knot-row absolute integral directly from its inverse, and checks equality across nodes and strictness against the closed envelope for 49 profiles: seven positive mesh ratios and all circle half-sizes \(2\le m\le8\). The same calculations verify exact examples \(2\) (balanced), \(69/35\) (ratio \(1:2\)), and \(173/91\) (ratio \(1:4\)). These finite tests are not substitutes for the infinite recurrence and periodization arguments.

## Relationship to prior work

Shadrin proved uniform \(L^\infty\) boundedness of orthogonal spline projectors independently of the knot sequence. The periodic extension and almost-everywhere convergence for general periodic splines appear in Passenbrunner's 2016 preprint; its Theorem 1.4 is a uniform inequality rather than the present two-periodic exact ratio law. Passenbrunner--Shadrin establish inverse-Gram decay for arbitrary partitions, without the present exact specialization. Oswald records the classical sharp general one-dimensional linear-spline upper bound \(3\), which is distinct from the sharp bound \(2\) within alternating meshes. Uniform-mesh periodic norms are a known special case; novelty is asserted only for the full nonuniform two-periodic formula, the strict cyclic inequality and the sharp contrast law.

## Limitations

The result is restricted to real continuous linear splines on exact two-periodic positive knot gaps and even-length periodic rings; it does not establish a sharp constant for arbitrary nonperiodic gaps, higher-order splines, boundary intervals, or nonorthogonal projectors. This is a claim of mathematical derivation, not a claim of exhaustive bibliographic priority; unpublished or older specialist computations of two-periodic spline kernels remain possible.

## References

- M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720 (first public 2016-08-24), especially Theorems 1.3 and 1.4 and Sections 3--5.
- M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824 (2013), especially Theorems 1.1 and 1.2.
- P. Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573 (2006), Introduction.
- A. Shadrin, *The \(L^\infty\)-norm of the \(L^2\)-spline projector is bounded independently of the knot sequence: a proof of de Boor's conjecture*, Acta Mathematica 187 (2001), 59--137.
