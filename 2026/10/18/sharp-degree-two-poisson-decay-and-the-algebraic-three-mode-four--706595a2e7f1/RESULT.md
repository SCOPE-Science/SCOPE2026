# Sharp degree-two Poisson decay and the algebraic three-mode fourth-moment barrier

## Finding
Let \(\mathbb T\) carry probability-normalized Haar measure, and let \(P_r\) be the harmonic Poisson operator with Fourier multiplier \(r^{|k|}\), for \(0<r<1\). For \(N\ge1\), let \(\mathcal V_N\) denote the complex trigonometric polynomials having zero constant coefficient and Fourier degrees between \(-N\) and \(N\). Then the **sharp bandwidth dichotomy** is
\[
\sup_{0\ne f\in\mathcal V_N}\frac{\|P_rf\|_4}{r\|f\|_4}=1\quad\text{for }N=1,2,
\qquad
\sup_{0\ne f\in\mathcal V_N}\frac{\|P_rf\|_4}{r\|f\|_4}>1\quad\text{for all }N\ge3,
\]
for **every** radius \(0<r<1\). Indeed the first assertion holds with \(L^4\) replaced by any \(L^p\) with \(1\le p\le\infty\). A single rational-coefficient cubic
\[
f_0(\zeta)=\zeta^{-1}+\zeta-\tfrac1{10}\zeta^3
\]
violates the proposed normalized \(L^4\) decay at *every* radius.

There is also an **exact sharp size** of the first three-mode obstruction. On the natural minimal resonant space \(\mathcal W=\operatorname{span}\{\zeta^{-1},\zeta,\zeta^3\}\), define
\[
K=\lim_{r\downarrow0}\sup_{0\ne f\in\mathcal W}\frac{\|P_rf\|_4}{r\|f\|_4}.
\]
Let \(u_*\) be the unique positive root of
\[
6u^6+50u^5+156u^4+202u^3+110u^2+14u-1=0.
\]
Put \(y_*=\sqrt{u_*}\) and
\[
x_*=y_*\frac{2u_*^3+2u_*^2-9u_*-2}{4u_*^3+20u_*^2+2u_*-1},
\quad N_*=x_*^4+4x_*^2+1,
\quad D_*=N_*+y_*^4+4(1+x_*^2)y_*^2-4x_*y_*.
\]
Then
\[
\boxed{K=\left(\frac{N_*}{D_*}\right)^{1/4}=1.027443983453088780\ldots.}
\]
Every maximizer of the limiting quotient is, up to nonzero complex scalar and rotation of the circle, exactly \(x_*\zeta^{-1}+\zeta-y_*\zeta^3\). The finite-radius operator norm on \(\mathcal W\) equals \(K+O(r^2)\) as \(r\downarrow0\). No formula for the full finite-radius optimum is claimed.

## Assumptions and scope
All functions and norms are complex-valued, with \(\|f\|_p=(\int_{\mathbb T}|f|^p\,dm)^{1/p}\) and normalized Haar measure. A trigonometric polynomial has degree at most \(N\) if its Fourier coefficients vanish outside \([-N,N]\). The mean-zero condition is the absence of the zero-frequency coefficient; the input need not have modulus one. The first theorem concerns **stronger \(L^4\)-to-\(L^4\) decay**, *not* the open complex \(L^\infty_0\)-to-\(L^4\) Poisson Schwarz inequality. The three-mode limit is an operator norm restricted to \(\mathcal W\), not the unrestricted norm.

## Proof
**1. The degree-two inequality.** Write a mean-zero polynomial of degree at most two as \(f=g_1+g_2\), where \(g_j\) has frequencies \(\pm j\). Then \(P_rf/r=g_1+rg_2\). The half-turn sends \(g_1(-\zeta)=-g_1(\zeta)\), while \(g_2(-\zeta)=g_2(\zeta)\). For \(p\ge1\), the real-variable function \(t\mapsto\|g_1+t g_2\|_p\) is even by the half-turn and convex by the triangle inequality. Hence it is nondecreasing on \([0,\infty)\), and \(\|P_rf\|_p/r\le\|f\|_p\). Equality occurs at every radius for \(f(\zeta)=\zeta\). This covers degree one as well.

**2. A cubic failure at every radius.** For \(f_0=\zeta^{-1}+\zeta-\varepsilon\zeta^3\) with \(\varepsilon=1/10\), set \(t=r^2\). Fourier convolution, or Parseval applied to the squared modulus of the quadratic polynomial \(1+w-\varepsilon t w^2\) with \(w=\zeta^2\), gives
\[
\frac{\|P_rf_0\|_4^4}{r^4}=6-4\varepsilon t+8\varepsilon^2t^2+\varepsilon^4t^4,
\quad\|f_0\|_4^4=6-4\varepsilon+8\varepsilon^2+\varepsilon^4.
\]
The difference is
\[
(1-t)\left[4\varepsilon-8\varepsilon^2(1+t)-\varepsilon^4(1+t+t^2+t^3)\right].
\]
For \(0<t<1\), its bracket is at least \(4\varepsilon-16\varepsilon^2-4\varepsilon^4=599/2500>0\). Thus \(\|P_rf_0\|_4>r\|f_0\|_4\) for every radius. Every \(\mathcal V_N\) with \(N\ge3\) contains this cubic, completing the bandwidth classification.

**3. Exact fourth moment on the resonant space.** Multiplying \(f=a\zeta^{-1}+b\zeta+c\zeta^3\) by \(\zeta\) and using \(w=\zeta^2\) does not change the distribution of its modulus. Parseval yields
\[
\|f\|_4^4=(|a|^2+|b|^2+|c|^2)^2
 +2|b\bar a+c\bar b|^2+2|c\bar a|^2.
\]
The limiting normalized Poisson image is \(a\zeta^{-1}+b\zeta\), with fourth power \(N_0=(|a|^2+|b|^2)^2+2|a b|^2\). Expanding the preceding expression shows its only phase-dependent term is \(4\operatorname{Re}(ac\bar b^{\,2})\). For fixed nonzero coefficient magnitudes the quotient is largest precisely when that real part is \(-|a||c||b|^2\). Inputs with any zero coefficient have quotient at most one, while step 2 gives examples above one. Thus all optimizers have nonzero coefficients and the antialigned phase condition. Removing overall scale and circle-rotation phase reduces them to
\[
f=x\zeta^{-1}+\zeta-y\zeta^3,\qquad x,y>0.
\]
The fourth-power quotient becomes \(N/D\), where
\[
N=x^4+4x^2+1,\qquad
D=N+y^4+4(1+x^2)y^2-4xy.
\]
The normalized coefficient space is compact and every boundary point where one of \(a,b,c\) vanishes gives a quotient at most one. Therefore a maximum greater than one occurs in the interior, and must satisfy
\[
 y^3+2(1+x^2)y-x=0,
\quad
(\partial_x D)N-D(\partial_x N)=0.
\]
Exact polynomial elimination of \(x\) from these two equations gives the *necessary* relation
\[
6y^{12}+50y^{10}+156y^8+202y^6+110y^4+14y^2-1=0,
\]
and the linear subresultant relation
\[
x(4y^6+20y^4+2y^2-1)+y(-2y^6-2y^4+9y^2+2)=0.
\]
The degree-six polynomial in \(u=y^2\) has strictly positive derivative for \(u>0\) and negative value at zero, so it has exactly one positive root. Exact rational evaluations bracket it between \(49/1000\) and \(51/1000\). On that interval the coefficient of \(x\) in the subresultant is strictly negative and therefore nonzero. The subresultant hence fixes \(x\) uniquely by the displayed formula. Since an interior maximizer exists, these necessary conditions identify it uniquely; no assertion that an arbitrary root of the elimination equations is automatically optimal is needed. Substitution yields the stated algebraic constant and the complete coefficient-phase extremizer orbit.

**4. Norm limit.** On the finite-dimensional space \(\mathcal W\), the operators \(r^{-1}P_r\) converge in operator norm to the projection \(Qf=a\zeta^{-1}+b\zeta\), and their difference is exactly \(r^2 c\zeta^3\). Consequently the corresponding operator norms differ by \(O(r^2)\). The preceding maximization is exactly \(\|Q\|_{\mathcal W\cap L^4\to L^4}\), proving the sharp limit.

## Verification
The standalone file `verify.py` recomputes the Fourier fourth-moment polynomial, the two stationary conditions, their exact polynomial resultant and linear subresultant, the rational bracket isolating the positive root, and the strict all-radius rational margin. It uses symbolic exact arithmetic and high-precision root evaluation only to print the decimal illustration. Running `python3 verify.py` completes with `VERIFY_OK`. The analytic proof of global optimality uses compactness and uniqueness of positive algebraic stationary data rather than a finite search; no experiment is extrapolated to infinitely many Fourier modes.

## Relationship to prior work
Kovalev's 2026 Poisson Schwarz-contractivity theorem establishes \(\|P_rf\|_3\le r\|f\|_\infty\) for mean-zero complex boundary data and formulates the outstanding \(L^\infty_0\to L^4\) endpoint conjecture. It does **not** assert an \(L^4\to L^4\) inequality. The present result identifies exactly where the *stronger intermediate \(L^4\) spectral-gap strategy* first fails among all centered bounded-degree harmonic polynomials; it quantifies that first failure with a sharp algebraic amplification and unique extremizers. The endpoint conjecture itself is neither proved nor disproved.

The published fourth-moment Fourier-section obstruction for the third symmetric partial sum concerns \(S_3\colon L^\infty_0\to L^4\), not the radial Poisson multiplier, the bandlimited \(L^4\)-decay threshold, or this restricted sharp algebraic projection norm. A published exact finite-radius formula for a special odd unimodular Poisson witness likewise concerns \(L^\infty\)-normalized endpoint decay of a different input family, not \(L^4\)-normalized spectral-gap decay. The distinction is mathematical: the source inequalities compare the image to a *boundary supremum*, whereas the present counterexample compares it to the *boundary fourth norm*. Older functional-analytic inequalities about \(L^p\) Poisson semigroups may still contain equivalent special cases; exhaustive historical priority is not asserted.

## Limitations
The classification is for complex mean-zero trigonometric polynomials of bounded degree and probability-normalized \(L^4\) norms; the positive half actually holds for every \(p\ge1\). The sharp constant is a **small-radius limit on a three-character subspace**, not an exact all-radius operator norm on that subspace, and not the unrestricted operator norm. It is greater than one but does not contradict the conjectured complex Poisson \(L^\infty_0\to L^4\) Schwarz bound. The originality assessment is limited to examined sources and accessible searches; independent validation has not been performed.

## References
1. L. V. Kovalev, *Schwarz-contractivity of the Poisson operator*, arXiv:2609.28938v1, first posted 2026-09-24, Sections 1 and 4–5. https://arxiv.org/abs/2609.28938
2. *Mean-zero fourth-moment obstruction for the third symmetric Fourier cutoff* (2026), published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mean-zero-fourth-moment-obstruction-for-the-third-symmetric-four--c478f3ae3a29
3. *Exact endpoint deficit for the canonical complex Poisson obstruction family* (2026), published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-endpoint-deficit-for-the-canonical-complex-poisson-obstruc--87cdbe275635
4. L. V. Kovalev and X. Yang, *Near-isometric duality of Hardy norms with applications to harmonic mappings*, J. Math. Anal. Appl. 487 (2020), Paper No. 124040; arXiv:2001.09465. (Earlier small-radius \(L^\infty\)-normalized first-harmonic inequality.)
