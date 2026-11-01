# Area-calibrated width-moment tomography of parallelograms, with sharp inverse slope

## Finding
For a nondegenerate Euclidean parallelogram \(K\), let \(P\) be its perimeter, \(A\) its area, and \(W(U)\) its orthogonal projection length onto a Haar-uniform unoriented line \(U\). **The three scalar measurements \((P,A,\mathbb E W^2)\) determine \(K\) up to Euclidean congruence.** No directional labels or maximum-width measurement are required.

More precisely, put \(S=P/2\), \(\delta=4A/S^2\), and \(\nu=\mathbb E W^2\). Suppose \(0<\delta<1\). Among all parallelograms with these fixed \(P,A\), the unique minimum of \(\nu\) is attained by the rectangle, and the unique maximum by the rhombus. For all such bodies the side-length product \(t\) belongs to \([A,S^2/4]\), and \(\nu=F_{S,A}(t)\) is strictly increasing and strictly concave. If \(A\le t_1<t_2\le S^2/4\), then
\[
 c(\delta)(t_2-t_1)\le F_{S,A}(t_2)-F_{S,A}(t_1)
 \le\left(\frac4\pi-1\right)(t_2-t_1),
\]
where the **optimal, positive lower slope** is
\[
 c(\delta)=\frac2\pi\left(\delta+
 \frac{\pi/2-\arcsin\delta}{\sqrt{1-\delta^2}}\right)-1>0.
\]
Both slope constants are optimal for each fixed \(0<\delta<1\), in the sense of limits of differences for distinct admissible parallelograms. If \(\delta=1\), the sole admissible body is a square, up to congruence.

## Assumptions and scope
A nondegenerate parallelogram is a Minkowski sum of two nonzero nonparallel segments. Write their lengths as \(a,b>0\) and the acute angle between their unoriented supporting lines as \(\theta\in(0,\pi/2]\). Replacing one generating vector by its negative changes the parametrization but not the body up to translation; therefore \(\theta\) and unordered \(\{a,b\}\) parameterize congruence classes.

Then \(P=2(a+b)\), \(A=ab\sin\theta\), \(t=ab\), \(S=a+b\), and the feasible interval is exactly \(A\le t\le S^2/4\). Conversely every \(t\) in this interval occurs: take \(a,b\) as the two positive roots of \(z^2-Sz+t=0\) and \(\theta=\arcsin(A/t)\). Its endpoints correspond to a rectangle (\(\theta=\pi/2\)) and to a rhombus (\(a=b\)). The nontrivial interval requires \(0<A<S^2/4\).

For any unit vector \(u\), \(W(u)\) is the length of the orthogonal shadow of \(K\) on the line it spans. The normalization is \(\mathbb E f(W)=\pi^{-1}\int_0^\pi f(W((\cos\varphi,\sin\varphi)))\,d\varphi\). Thus \(\mathbb E W=2S/\pi\), so the same conclusions hold for its variance \(\operatorname{Var}(W)=\nu-4S^2/\pi^2\) at fixed perimeter.

## Proof
Choose edge directions \(v=a(1,0)\), \(w=b(\cos\theta,\sin\theta)\). The support function of a Minkowski sum of segments gives
\[
 W(\varphi)=a|\cos\varphi|+b|\cos(\varphi-\theta)|.
\]
Splitting the angular integral at the zeroes of the two cosines gives
\[
 \mathbb E|\cos\varphi|^2=\frac12,\qquad
 g(\theta):=\mathbb E(|\cos\varphi\cos(\varphi-\theta)|)
 =\frac{\sin\theta+(\pi/2-\theta)\cos\theta}{\pi}.
\]
Consequently
\[
 \nu=\frac{a^2+b^2}{2}+2ab g(\theta)
 =\frac{S^2}{2}+t\bigl(2g(\theta)-1\bigr),
 \qquad \theta=\arcsin(A/t).
\]
Set \(F_{S,A}(t)\) equal to this last expression. For \(t>A\) we have \(\theta'(t)=-\tan\theta/t\) and \(g'(\theta)=-(\pi/2-\theta)\sin\theta/\pi\). Therefore
\[
 F'_{S,A}(t)=H(\theta),\qquad
 H(\theta)=\frac2\pi\left[\sin\theta+
 \frac{\pi/2-\theta}{\cos\theta}\right]-1.
\]
The apparent singularity at \(\theta=\pi/2\) is removable, and \(H(\pi/2)=4/\pi-1\). Also \(H(0)=0\). A direct derivative calculation yields
\[
 H'(\theta)=\frac{2\sin\theta}{\pi\cos^2\theta}
 \left(\frac\pi2-\theta-\sin\theta\cos\theta\right)>0
 \quad(0<\theta<\pi/2).
\]
Indeed the term in parentheses is zero at \(\pi/2\), and its derivative is \(-2\cos^2\theta<0\). Thus \(H\) is positive and strictly increasing throughout the permitted angular interval.

As \(t\) increases, \(\theta=\arcsin(A/t)\) strictly decreases. It follows that \(F'_{S,A}>0\) and \(F'_{S,A}\) is strictly decreasing, proving strict increase and strict concavity. The minimum and maximum derivative values are respectively \(H(\arcsin\delta)=c(\delta)\) and \(H(\pi/2)=4/\pi-1\). Integrating these bounds proves the two-sided slope inequality. For fixed \(\delta\in(0,1)\), let the two parameters coalesce at \(S^2/4\) or at \(A\) to see that neither constant can be improved. The endpoint derivatives exist from within the closed feasible interval.

The extremal second moments are explicit:
\[
 \nu_{\mathrm{rect}}=\frac{S^2}{2}+A\left(\frac2\pi-1\right),
\]
\[
 \nu_{\mathrm{rhomb}}=\frac{S^2}{2}
 +\frac{S^2}{4}\left[
 \frac2\pi\left(\delta+(\pi/2-\arcsin\delta)\sqrt{1-\delta^2}\right)-1\right].
\]
Strict monotonicity gives strict separation unless \(\delta=1\). Finally, for given measurements \((P,A,\nu)\), solve the unique scalar equation \(F_{S,A}(t)=\nu\), then recover
\[
 \{a,b\}=\left\{\frac{S+\sqrt{S^2-4t}}2,
 \frac{S-\sqrt{S^2-4t}}2\right\},\qquad
 \theta=\arcsin(A/t).
\]
This recovers the complete congruence class. The optimal lower slope bounds error in the recovered side-product \(t\); extracting individual side lengths has the unavoidable square-root behavior at the rhombus endpoint.

## Verification
The accompanying standalone standard-library program `verify.py` checks the analytic second-moment formula against direct angular quadrature on 400 reproducibly seeded nondegenerate parallelograms. It also checks the derivative bounds and inverse scalar reconstruction on these examples, as well as near-endpoint lower-slope limits for 15 fixed-area/perimeter families. It reports `VERIFY_OK 1215`. The complete continuum and best constants are proved above, independently of this finite test.

## Relationship to prior work
Martirosyan and Sargsyan (first publicly submitted May 23, 2026, arXiv:2605.24616v1) show that a triple of chord-power integrals determines a triangle and motivate the problem of shape recovery from a few scalar integral-geometric measurements. Their class is triangles and their data are chord integrals; they do not provide the parallelogram area-plus-width-moment inversion.

A publicly accessible mathematical finding, *Three unlabeled width statistics reconstruct a parallelogram with sharp stability* (October 11, 2026), already proves an inverse theorem using **mean width, mean-square width, and maximum width**. Its exact general parallelogram moment formula is used above with credit. The new data replace *maximum width* by *area* and yield a different one-parameter inversion, a fixed-area/perimeter rectangle-to-rhombus variance envelope, and a sharp lower derivative depending only on the normalized area. The earlier three-statistic result does not imply the present three-statistic result, because the third measurements differ and the displayed moment formula alone does not establish the needed fixed-area monotonicity.

Kim, Yaskin and Zvavitch (arXiv:1512.07289v1, especially Section 3) study the complete unlabeled distribution of projection measurements and nonidentifiability for broader body classes. Their full-text positive and negative statements do not assert this specific three-scalar classification. Finch (arXiv:1110.0671) computes width moments of regular polyhedra; those examples are not area-calibrated nonorthogonal parallelogram tomography. The mean-width/perimeter formula is classical and not claimed new.

## Limitations
The theorem assumes exact full-direction second moments, not finite-sample estimates. Uniform inverse conditioning necessarily deteriorates as normalized area \(\delta\to0\); the sharp constant tends to zero. Although the side-product inversion is Lipschitz at fixed \(P,A\), individual sorted side lengths need not be Lipschitz at equal sides. These conclusions do not extend without additional work to arbitrary quadrilaterals or general convex bodies. Independent priority verification and independent mathematical audit are not supplied.

## References
1. M. Martirosyan and R. Sargsyan, *A Closed Form for the Chord-Power Integral I2 of a Triangle*, arXiv:2605.24616v1, submitted May 23, 2026. https://arxiv.org/abs/2605.24616.
2. *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, publicly available mathematical finding, October 11, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-unlabeled-width-statistics-reconstruct-a-parallelogram-wit--dcfda0360928 (particularly RESULT.md).
3. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, December 22, 2015, Section 3. https://arxiv.org/abs/1512.07289.
4. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, October 4, 2011. https://arxiv.org/abs/1110.0671.
