# Positive quartic reduction at the one-dimensional mixed-norm Strichartz threshold
## Finding
At the unresolved one-dimensional threshold \((q,r)=(5,10)\), let \(g_0(x)=e^{-x^2/2}\) and
\[
h_n(x)=\frac{H_n(x)e^{-x^2/2}}{\sqrt{2^n n!}},
\]
where \(H_n\) is the physicists' Hermite polynomial. Let \(d_{5,10}\) denote the \(5\)-homogeneous deficit of Gonçalves, Negro and Oliveira e Silva, and put
\[
B=\frac12\left\|e^{-iT(H+1)/2}g_0\right\|_{L_T^5L_X^{10}(( -\pi,\pi)\times\mathbb R)}^5
=\pi\left(\frac{\pi}{5}\right)^{1/4}.
\]
For every fixed \(a\in\mathbb C\),
\[
B^{-1}d_{5,10}[g_0+\varepsilon h_3+\varepsilon^2 a h_6]
=\frac{6}{625}\left(77|a|^2-74\sqrt5\,\operatorname{Re}a+210\right)\varepsilon^4+O_a(\varepsilon^5).
\]
The coefficient has the exact completion of squares
\[
77|a|^2-74\sqrt5\,\operatorname{Re}a+210
=77\left(\left(\operatorname{Re}a-\frac{37\sqrt5}{77}\right)^2+(\operatorname{Im}a)^2\right)+\frac{9325}{77},
\]
so its unique minimum occurs at \(a=37\sqrt5/77\), and the normalized minimum is
\[
\frac{2238}{1925}>0.
\]
Moreover, for a general second-order Hermite correction orthogonal to the Gaussian tangent space and to \(h_3\), time-frequency selection shows that only its \(h_6\) coefficient can enter the cubic coupling with two copies of \(h_3\). The source proves that at the threshold the Hessian is positive semidefinite on the tangent-orthogonal space and that its kernel is exactly the complex line spanned by \(h_3\). Therefore every other second-order Hermite mode contributes a nonnegative Hessian term. No second-order tangent-orthogonal correction can remove the positive reduced quartic coefficient.

## Assumptions and scope
The spatial dimension is \(d=1\). Schrödinger admissibility \(2/q+1/r=1/2\) and the source threshold \(r=10\) give \(q=5\). The Hermite normalization is exactly the one used in arXiv:2609.11644v1, so \(\|h_n\|_2^2=\sqrt\pi\) for every \(n\). The number-operator evolution satisfies \(e^{-iT(H+1)/2}h_n=e^{inT}h_n\).

The statement is a reduced fourth-order result. It establishes positivity after optimization over the complete second-order stable correction, but it does not assert that Gaussians are full local maximizers at the threshold. Such a conclusion would require control of higher-order remainders uniformly in an infinite-dimensional neighborhood.

## Proof
The lens-transform formula in the source gives
\[
d_{5,10}[f]=\frac12\frac{\|Ug_0\|_{L_T^5L_X^{10}}^5}{\|g_0\|_2^5}\|f\|_2^5-\frac12\|Uf\|_{L_T^5L_X^{10}}^5,
\]
with \(U=e^{-iT(H+1)/2}\) and \(T\in(-\pi,\pi)\). Since \(|Ug_0|=g_0\), the factor \(B\) above is exactly half of the Gaussian spacetime term.

Write
\[
P_3(x)=\frac{h_3(x)}{g_0(x)}=\frac{2x^3-3x}{\sqrt3},
\]
and
\[
P_6(x)=\frac{h_6(x)}{g_0(x)}=\frac{64x^6-480x^4+720x^2-120}{96\sqrt5}.
\]
Normalize spatial integration by the probability density proportional to \(e^{-5x^2}\), and denote the resulting expectation by \(\mathbb E_5\). Direct Gaussian moments give
\[
\mathbb E_5(P_3^2)=\frac15,\qquad
\mathbb E_5(P_3^4)=\frac{249}{3125},
\]
\[
\mathbb E_5(P_6)=-\frac{16\sqrt5}{125},\qquad
\mathbb E_5(P_6^2)=\frac{2841}{15625},\qquad
\mathbb E_5(P_3^2P_6)=\frac{22\sqrt5}{15625}.
\]
For
\[
f_{\varepsilon,a}=g_0+\varepsilon h_3+\varepsilon^2 a h_6,
\]
one has
\[
\frac{Uf_{\varepsilon,a}}{g_0}=1+\varepsilon e^{3iT}P_3+\varepsilon^2a e^{6iT}P_6.
\]
Expanding the tenth power in the spatial integral, then the square root corresponding to \(q/r=1/2\), and finally averaging over a full \(T\)-period yields
\[
\frac{\|Uf_{\varepsilon,a}\|_{L_T^5L_X^{10}}^5}{\|Ug_0\|_{L_T^5L_X^{10}}^5}
=1+\frac52\varepsilon^2+rac{8804|a|^2+3552\sqrt5\,\operatorname{Re}a-705}{5000}\varepsilon^4+O_a(\varepsilon^5).
\]
Orthogonality of the Hermite functions gives
\[
\left(\frac{\|f_{\varepsilon,a}\|_2}{\|g_0\|_2}\right)^5
=(1+\varepsilon^2+|a|^2\varepsilon^4)^{5/2}
=1+\frac52\varepsilon^2+\left(\frac52|a|^2+\frac{15}{8}\right)\varepsilon^4+O_a(\varepsilon^6).
\]
Subtracting produces the displayed quartic polynomial and its positive minimum.

It remains to identify the complete second-order coupling. If a stable Hermite mode \(h_n\) occurs in the \(\varepsilon^2\) correction, then the cubic term involving two factors from the kernel mode \(h_3\) has time frequencies of the form \(\pm3\pm3\pm n\). A zero time frequency is possible only for \(n=0\) or \(n=6\). The \(n=0\) direction belongs to the Gaussian tangent space, so the only stable resonant correction is \(h_6\). All nonresonant stable modes have no cubic coupling and enter at this order only through the threshold Hessian. Remark 3.2 of the source proves that this Hessian is positive semidefinite on the tangent-orthogonal space with kernel exactly \(\operatorname{span}_{\mathbb C}\{h_3\}\). This proves the reduced statement.

## Verification
The accompanying standard-library checker recomputes the exact Gaussian moments from rational polynomial arithmetic and verifies the quartic coefficients, the completing-square identity, and the minimum \(2238/1925\). Its replay output is included separately. The computation is auxiliary: the proof is the exact Taylor and frequency-selection argument above.

## Relationship to prior work
Gonçalves, Negro and Oliveira e Silva identify \(r=10\) as the one-dimensional stability threshold, prove that the threshold Hessian is positive semidefinite with one-dimensional complex kernel generated by the third Hermite mode, and explicitly state that the threshold case is not resolved because higher-order Fréchet derivatives would be needed. Their paper does not compute the fourth-order reduced coefficient above.

Gonçalves and Negro treat the diagonal paraboloid restriction problem; in one dimension this corresponds to the diagonal Schrödinger pair \((q,r)=(6,6)\), not the mixed critical pair \((5,10)\). Carneiro's sharp even diagonal Strichartz inequalities likewise do not imply the present mixed-norm threshold calculation. The numerical study of Valenzuela, Freire and Muñoz supplies evidence for Gaussian extremizers at many conjectural one-dimensional pairs but does not provide this exact analytic quartic reduction.

## Limitations
The result does not prove full local maximality at \((q,r)=(5,10)\). It controls the first nonzero Lyapunov--Schmidt coefficient after the quadratic degeneracy and rules out cancellation by any second-order stable Hermite correction. A full threshold theorem would additionally require a uniform higher-order expansion or an equivalent infinite-dimensional center-manifold argument.

The originality search found no statement equivalent to the exact coefficient or its optimized value, but database search cannot prove absence from all literature. The principal residual risk is an equivalent unpublished or poorly indexed higher-variation computation.

## References
1. F. Gonçalves, G. Negro, D. Oliveira e Silva, “Gaussians Do Not Always Maximize Mixed-Norm Strichartz Inequalities for the Schrödinger Equation,” arXiv:2609.11644v1, 10 September 2026.
2. F. Gonçalves, G. Negro, “Local maximizers of adjoint Fourier restriction estimates for the cone, paraboloid and sphere,” arXiv:2003.11955v2; Analysis & PDE 15 (2022), 1097–1130.
3. E. Carneiro, “A sharp inequality for the Strichartz norm,” arXiv:0809.4054v1.
4. N. Valenzuela, R. Freire, C. Muñoz, “Neural Discovery of Strichartz Extremizers,” arXiv:2605.04918v1, 6 May 2026.
