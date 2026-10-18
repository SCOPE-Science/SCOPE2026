# Sharp endpoint derivatives of the circular Poisson semigroup

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with Haar probability measure \(d\theta/(2\pi)\). Write \(\mathcal P_t=e^{-t|D|}\) for the classical circular Poisson semigroup on \(L^1(\mathbb T)\) and \(L^\infty(\mathbb T)\), so that its Fourier multiplier at frequency \(k\in\mathbb Z\) is \(e^{-t|k|}\). Put \(N_j(t)=\|\partial_t^j\mathcal P_t\|_{L^1\to L^1}=\|\partial_t^j\mathcal P_t\|_{L^\infty\to L^\infty}\), for integers \(j\ge1\) and \(t>0\).

**All-order sharp analytic-semigroup constants.** For each integer \(j\ge1\),
\[
\boxed{\sup_{t>0}t^jN_j(t)=C_j=\frac{4(j-1)!}{\pi}\sum_{m=0}^{\lfloor(j-1)/2\rfloor}\cos^{j+1}\!\left(\frac{(2m+1)\pi}{2(j+1)}\right).}
\]
The inequality \(t^jN_j(t)<C_j\) is strict for every positive \(t\), and equality is approached as \(t\downarrow0\). In particular \(C_1=2/\pi\), \(C_2=3\sqrt3/(2\pi)\), and \(C_3=6/\pi\). For high derivative order,
\[
\boxed{\frac{C_j}{j!}=\frac{2\sqrt{2\pi}}{\pi^2\sqrt j}+O(j^{-1})\qquad(j\to\infty).}
\]

**Finite-time endpoint laws.** Write \(h=\cosh t\), \(s=\sinh t\), and \(z_t=(-h+\sqrt{h^2+8})/2\in(0,1)\). Then
\[
\boxed{N_1(t)=\frac{2}{\pi\sinh t},\qquad N_2(t)=\frac{2\sinh t\sqrt{1-z_t^2}}{\pi(h-z_t)^2}.}
\]
Their small-time corrections have genuinely different orders:
\[
\boxed{\begin{aligned}
tN_1(t)&=\frac2\pi\left(1-\frac{t^2}{6}+O(t^4)\right),\\
t^2N_2(t)&=\frac{3\sqrt3}{2\pi}\left(1-\frac{t^4}{135}+O(t^6)\right).
\end{aligned}}
\]
Thus the second scaled norm has no quadratic finite-circumference correction.

**A third-derivative nodal transition.** Define the cubic
\[
F_h(x)=-hx^3+4(1-h^2)x^2+(4h-h^3)x+4h^2-6.
\]
For \(1<h<2\), it has exactly two roots in \((-1,1)\), one in \((-1,1/h)\) and one in \((1/h,1)\). At \(h=2\), the lower root reaches \(-1\); for \(h>2\), there is exactly one root in \((-1,1)\), situated in \((1/h,1)\). If \(\mathcal Z_t\) denotes these interior roots, the third derivative has the exact norm
\[
\boxed{N_3(t)=\frac2\pi\sum_{x\in\mathcal Z_t}\left|\frac{\sqrt{1-x^2}(2-h^2-hx)}{(h-x)^3}\right|.}
\]
The number of interior zero-angle pairs of the third-derivative convolution kernel therefore changes sharply from two to one at \(t=\operatorname{arcosh}2=\log(2+\sqrt3)\). The transition concerns nodal geometry, not a discontinuity of the norm.

## Assumptions and scope

All statements hold for real and complex \(L^1(\mathbb T)\) and \(L^\infty(\mathbb T)\) functions with the specified normalized Haar measure and the nonnegative generator \(|D|\), whose Fourier eigenvalues are \(|k|\). Operator derivatives are taken at strictly positive time, where the convolution kernels and all parameter derivatives are continuous and integrable. The indices \(j\) are arbitrary positive integers in the all-order assertion; the explicit finite-time formulas concern \(j=1,2,3\). The norm refers to the full input spaces, without imposing a zero-mean constraint or positivity restriction. The result does not assert matching norms for \(1<p<\infty\), nor corresponding constants for higher-dimensional tori.

## Proof

**1. Kernel and endpoint operator norm.** The absolutely convergent Fourier series gives
\[
P(t,\theta)=1+2\sum_{k\ge1}e^{-tk}\cos(k\theta)
=\frac{\sinh t}{\cosh t-\cos\theta}.
\]
The operator \(\partial_t^j\mathcal P_t\) is convolution with \(\partial_t^jP(t,\cdot)\), where convolution is normalized by \(d\theta/(2\pi)\). The sharp \(L^1\) and \(L^\infty\) operator norms both equal the normalized \(L^1\) norm of this signed kernel: the upper bound is Young's inequality, the \(L^1\) lower bound follows by approximate identities, and the \(L^\infty\) lower bound follows by taking the conjugate-sign function at a chosen output point. Evenness reduces this kernel norm to
\[
N_j(t)=\frac1\pi\int_0^\pi|\partial_t^jP(t,\theta)|\,d\theta.
\]

**2. Exact first and second derivatives.** Set \(x=\cos\theta\), \(h=\cosh t\), \(s=\sinh t\). Direct differentiation yields
\[
\partial_tP=\frac{1-hx}{(h-x)^2},\qquad
\partial_t^2P=\frac{s(x^2+hx-2)}{(h-x)^3}.
\]
For \(t>0\), the first expression changes sign precisely at \(x=1/h\); the second changes sign precisely at \(x=z_t\). Since every derivative of positive order integrates to zero on the circle, its absolute integral equals twice the absolute signed mass on a sign interval. The exact primitives on \([0,\theta]\) are
\[
\int_0^\theta\partial_tP(t,u)\,du=-\frac{\sin\theta}{h-\cos\theta},\qquad
\int_0^\theta\partial_t^2P(t,u)\,du=\frac{s\sin\theta}{(h-\cos\theta)^2}.
\]
Evaluating at the respective sign changes gives the stated formulas. Expanding the explicit radical at \(t=0\) gives the two displayed corrections, including exact vanishing of the quadratic coefficient in \(t^2N_2(t)\); the next coefficient is \(-\sqrt3/(90\pi)\).

**3. Third-derivative transition and sharp norm.** Differentiating again gives
\[
\partial_t^3P(t,\theta)=\frac{F_h(\cos\theta)}{(h-\cos\theta)^4}.
\]
For every \(h>1\), the following exact signs hold:
\[
\begin{aligned}
F_h(1)&=-(h-1)^2(h+2)<0,\\
F_h(1/h)&=3(h^2-1)^2/h^2>0,\\
F_h(-1)&=(h-2)(h+1)^2,\\
F_h(-h)&=-2(h^4-2h^2+3)<0.
\end{aligned}
\]
As \(x\to-\infty\), \(F_h(x)\to+\infty\). The intermediate-value theorem and the fact that the polynomial has degree three place all three distinct real roots. For \(1<h<2\), they occupy \((-\infty,-1)\), \((-1,1/h)\), and \((1/h,1)\). At \(h=2\) the second root is \(-1\); when \(h>2\), they occupy \((-\infty,-h)\), \((-h,-1)\), and \((1/h,1)\). Hence only the stated roots correspond to interior zero angles. A third primitive is
\[
\int_0^\theta\partial_t^3P(t,u)\,du
=\frac{\sin\theta\,[2-h^2-h\cos\theta]}{(h-\cos\theta)^3}.
\]
Its value is zero at both endpoints. The sign intervals alternate, so its total variation on \([0,\pi]\) equals twice the sum of absolute values at its interior critical points. This proves the displayed formula for \(N_3(t)\), including the limiting boundary-root case.

**4. All-order constants by periodization.** Let \(p_t(y)=t/[\pi(t^2+y^2)]\), the Cauchy Poisson density on \(\mathbb R\) with Lebesgue measure. For each \(t>0\) and \(j\ge1\), one has the absolutely convergent periodization identity
\[
\partial_t^jP(t,\theta)=2\pi\sum_{m\in\mathbb Z}\partial_t^jp_t(\theta+2\pi m).
\]
Consequently, the triangle inequality yields \(N_j(t)\le\|\partial_t^jp_t\|_{L^1(\mathbb R)}\). The inequality is **strict** for every \(t>0\): the real-line derivative is an integrable, nonzero signed rational function of total integral zero, and its sign is eventually constant on the positive tail. Choose a real point with sign opposite that tail. At its residue class modulo \(2\pi\), one summand has that sign and infinitely many positive-tail summands have the opposite sign. Continuity makes the cancellation strict on a positive-measure set. On the other hand, homogeneity and the bound
\[
0\le \|\partial_t^jp_t\|_1-N_j(t)
\le2\int_{|y|>\pi}|\partial_t^jp_t(y)|\,dy
\]
show that \(t^jN_j(t)\) approaches the scale-invariant real-line constant as \(t\downarrow0\). Indeed, substitution \(y=tu\) turns the right-hand side after multiplication by \(t^j\) into a tail of an integrable fixed function over \(|u|>\pi/t\).

To evaluate this constant, differentiate
\[
p_t(y)=\frac1\pi\operatorname{Re}(t+iy)^{-1},\qquad
\partial_t^jp_t(y)=\frac{(-1)^jj!}{\pi}\operatorname{Re}(t+iy)^{-j-1}.
\]
After \(y=t\tan u\),
\[
C_j=\frac{j!}{\pi}\int_{-\pi/2}^{\pi/2}\cos^{j-1}u\,|\cos((j+1)u)|\,du.
\]
The identity
\[
\frac{d}{du}[\cos^ju\sin(ju)]=j\cos^{j-1}u\cos((j+1)u)
\]
reduces the absolute integral to total variation. Its positive-angle critical points are exactly \(u_m=(2m+1)\pi/[2(j+1)]\), for \(m=0,\ldots,\lfloor(j-1)/2\rfloor\), and \(|\cos^ju_m\sin(ju_m)|=\cos^{j+1}u_m\). The variation equals twice the sum of those heights on the positive half-interval, and the integrand is even. This proves the finite trigonometric sum and strict finite-time inequality.

**5. Growth at high differentiation order.** In the last integral put \(w_j(u)=\cos^{j-1}u\). The periodic function \(|\cos v|\) has an absolutely summable cosine Fourier series with mean \(2/\pi\), and the remaining coefficients decay quadratically. For \(j\ge2\), integration by parts and the total variation bound \(\int_{-\pi/2}^{\pi/2}|w_j'(u)|\,du=2\) give an \(O(j^{-1})\) bound for all nonconstant Fourier contributions combined. The constant contribution is
\[
\frac2\pi\int_{-\pi/2}^{\pi/2}w_j(u)\,du
=\frac{2\sqrt\pi}{\pi}\frac{\Gamma(j/2)}{\Gamma((j+1)/2)}
=\frac{2\sqrt{2\pi}}{\pi\sqrt j}+O(j^{-3/2}).
\]
Multiplying by the outer factor \(1/\pi\) gives the claimed \(C_j/j!\) expansion.

## Verification

The accompanying `checker.py` requires Python 3.9 or later together with `sympy` and `mpmath`. From the directory containing this file, run `python checker.py`. It checks the symbolic first three derivatives, the cubic sign identities, piecewise high-precision integral norms for the first three derivatives at multiple times spanning the nodal transition, the all-order trigonometric constants for twelve differentiation orders, representative strict bounds, and the small-time series cancellation. A successful run prints its exact assertion count. These are finite consistency tests; the proof above establishes statements for all specified real times and positive integral orders.

## Relationship to prior work

Chen, Xu and Yin's 2012 paper studies circular Poisson means and Littlewood–Paley theory on quantum tori, including the classical torus. Xiong, Xu and Yin's 2015 preprint treats time derivatives of circular Poisson and heat semigroups in Besov/Triebel–Lizorkin descriptions; specifically §3.3 gives multiplier derivatives and equivalence estimates rather than these sharp \(L^1\) and \(L^\infty\) time-derivative norms, third-order sign-transition law, or all-order constants. Batty and collaborators' Besov-calculus paper gives bounds for holomorphic half-plane functions and discusses the real-line Poisson extension, but the explicit constants there govern a different holomorphic derivative problem. Searches of mathematical research records and published literature did not locate the exact combined theorem. This absence is evidence for a distinct statement, not a certification of historical priority.

## Limitations

This is a theorem about a specific one-dimensional periodic convolution semigroup with the given normalization. The claim excludes general diffusion semigroups, vector-valued endpoint extensions, higher-dimensional tori, and interior \(L^p\) operator norms. Sharp constants refer to the supremum over positive time and are not attained at any finite time. Historical equivalence under another name cannot be ruled out; independent bibliographic and mathematical review is outstanding. The checker provides finite cross-checks, not computer-assisted certification of the analytical arguments.

## References

- Z. Chen, Q. Xu and Z. Yin, *Harmonic analysis on quantum tori*, arXiv:1206.3358 (first posted 2012-06-15), especially the circular Poisson semigroup and §8 on Hardy spaces. https://arxiv.org/abs/1206.3358
- X. Xiong, Q. Xu and Z. Yin, *Sobolev, Besov and Triebel-Lizorkin spaces on quantum tori*, arXiv:1507.01789 (first posted 2015-07-07), especially §3.3 on Poisson and heat semigroup derivatives. https://arxiv.org/abs/1507.01789
- C. Batty, A. Gomilko and Y. Tomilov, *A Besov algebra calculus for generators of operator semigroups and related norm-estimates*, published online 2019-11-12 (volume dated 2021), DOI:10.1007/s00208-019-01924-2, §2 for half-plane Poisson and holomorphic derivative bounds. https://doi.org/10.1007/s00208-019-01924-2
