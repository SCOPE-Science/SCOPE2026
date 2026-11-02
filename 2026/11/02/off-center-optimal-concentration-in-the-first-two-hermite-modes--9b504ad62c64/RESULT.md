# Off-center optimal concentration in the first two Hermite modes

## Finding
Let the normalized first two Hermite functions be
\[
h_0(t)=\pi^{-1/4}e^{-t^2/2},\qquad h_1(t)=\sqrt{2}\,t h_0(t).
\]
For \(L>0\), \(a\in\mathbb R\), and the two-dimensional space \(E=\operatorname{span}\{h_0,h_1\}\), put
\[
G_L(a)_{jk}=\int_{a-L}^{a+L}h_j(t)h_k(t)\,dt,\qquad F_L(a)=\lambda_{\max}(G_L(a)).
\]
Equivalently, \(F_L(a)=\sup_{f\in E,\,\|f\|_2=1}\int_{a-L}^{a+L}|f(t)|^2\,dt\).

**Theorem.** For every \(L>0\), \(F_L\) is even, \(F_L(a)\to0\) at infinity, and
\[
F_L''(0)=\frac{4L}{\sqrt\pi}e^{-L^2}>0.
\]
Thus the centered window is a strict local minimum and is never globally optimal; at least one maximizing center lies on each open half-line. For all sufficiently small \(L>0\), the only global maximizing centers are \(\pm a_L\), with
\[
a_L=\frac{1}{\sqrt2}-\frac{\sqrt2}{180}L^4+O(L^6).
\]
The sharp optimal concentration satisfies
\[
\sup_{a\in\mathbb R}F_L(a)=\frac{4L}{\sqrt{\pi e}}
\left(1-\frac{L^2}{2}+\frac{41L^4}{180}+O(L^6)\right),
\qquad \lim_{L\downarrow0}\frac{\sup_aF_L(a)}{F_L(0)}=\frac2{\sqrt e}.
\]
In particular, there is an exact cancellation of the would-be quadratic shift of the narrow-window maximizing center.

## Assumptions and scope
The two Hermite functions are real and orthonormal in \(L^2(\mathbb R,dt)\). The interval length is exactly \(2L\); the free variable \(a\) is its center. Eigenvalues are those of the displayed \(2\times2\) real symmetric Gram matrix, and the supremum allows complex coefficients in \(E\). The local-minimum statement covers **every finite positive** \(L\). Global uniqueness is asserted only for sufficiently small \(L\), with no explicit uniform cutoff.

## Proof
Write \(u=a+L\), \(v=a-L\), and set \(p=G_{00}\), \(q=G_{11}\), \(b=G_{01}\). Elementary integration gives the exact expressions
\[
\begin{aligned}
p&=\tfrac12\bigl(\operatorname{erf}(u)-\operatorname{erf}(v)\bigr),\\
q&=p+\frac{v e^{-v^2}-u e^{-u^2}}{\sqrt\pi},\\
b&=\frac{e^{-v^2}-e^{-u^2}}{\sqrt{2\pi}},\\
F_L(a)&=\frac{p+q+\sqrt{(p-q)^2+4b^2}}2.
\end{aligned}
\]
Parity of the Hermite functions implies \(F_L(-a)=F_L(a)\). For fixed \(L\), all entries of \(G_L(a)\) tend to zero as \(|a|\to\infty\), so its largest eigenvalue also vanishes there. At the center,
\[
p(0)=\operatorname{erf}(L),\quad b(0)=0,\quad p(0)-q(0)=\frac{2L e^{-L^2}}{\sqrt\pi}>0.
\]
Hence the maximal eigenvalue is locally simple. Differentiating the displayed entries gives
\[
p''(0)=-\frac{4L e^{-L^2}}{\sqrt\pi},\qquad
b'(0)=\frac{2\sqrt2 L e^{-L^2}}{\sqrt\pi}.
\]
The standard simple-eigenvalue expansion of the two-by-two matrix at \(a=0\) then yields
\[
F_L''(0)=p''(0)+\frac{2b'(0)^2}{p(0)-q(0)}
=\frac{4L e^{-L^2}}{\sqrt\pi}>0.
\]
Thus \(a=0\) cannot maximize. Existence of a global maximizer follows from continuity, positivity, and decay at infinity; evenness supplies a maximizing center on each side.

For the sharp narrow-window expansion, define the column
\[
V(a)=\pi^{-1/4}e^{-a^2/2}\begin{pmatrix}1\\\sqrt2\,a\end{pmatrix},
\qquad S(a)=V(a)V(a)^T.
\]
Taylor expansion of the interval average, uniformly with as many derivatives as required on any compact \(a\)-set, is
\[
\frac{G_L(a)}{2L}=S(a)+\frac{L^2}{6}S''(a)+\frac{L^4}{120}S^{(4)}(a)+O(L^6).
\]
Set \(U=V^TV\) and \(W=(-V_2,V_1)^T\). Since \(S\) has simple positive eigenvalue \(U\) and other eigenvalue zero, elementary second-order spectral perturbation gives
\[
\frac{F_L(a)}{2L}=U(a)+L^2 A_2(a)+L^4 A_4(a)+O(L^6),
\]
where
\[
\begin{aligned}
U&=\frac{(1+2a^2)e^{-a^2}}{\sqrt\pi},\\
A_2&=\frac{V^TS''V}{6U},\\
A_4&=\frac{V^TS^{(4)}V}{120U}+
\frac{(W^TS''V)^2}{36U^3}.
\end{aligned}
\]
These formulas follow by projecting onto the normalized directions \(V/\sqrt U\) and \(W/\sqrt U\) and retaining the off-diagonal second-order contribution. Direct differentiation, with \(a_0=1/\sqrt2\), gives the exact data
\[
\begin{array}{c|c}
\text{quantity}&\text{value at }a_0\\\hline
U&2/\sqrt{\pi e}\\
U'&0\\
U''&-4/\sqrt{\pi e}\\
A_2&-1/\sqrt{\pi e}\\
A_2'&0\\
A_4&41/(90\sqrt{\pi e})\\
A_4'&-\sqrt2/(45\sqrt{\pi e})
\end{array}
\]
The \(O(L^6)\) remainder is analytic in \(L^2\) on a compact neighborhood of \(a_0\) and remains \(O(L^6)\) after any fixed number of \(a\)-derivatives.

The leading profile \(U\) has precisely two strict global maxima, at \(a=\pm a_0\), with \(U''(\pm a_0)<0\). Moreover, the inequality
\[
\frac{F_L(a)}{2L}\le\sup_{|t-a|\le L} (|h_0(t)|^2+|h_1(t)|^2)
\]
shows Gaussian-uniform tail decay for \(0<L\le1\). Consequently every global maximizer converges to one of \(\pm a_0\) as \(L\downarrow0\). Uniform \(C^2\) convergence to \(U\) and its strict local concavity imply a unique stationary/global maximizing center near each of them for all sufficiently small \(L\). The implicit function theorem produces the positive branch \(a_L\). Because \(A_2'(a_0)=0\), solving the derivative equation at fourth order gives
\[
a_L-a_0=-\frac{A_4'(a_0)}{U''(a_0)}L^4+O(L^6)
=-\frac{\sqrt2}{180}L^4+O(L^6).
\]
Substitution into the eigenvalue expansion yields the three-term optimal concentration formula, since the optimizer displacement changes its value only at higher order. Finally, \(F_L(0)=\operatorname{erf}(L)\sim2L/\sqrt\pi\) gives the ratio \(2/\sqrt e\). This completes the proof.

## Verification
The accompanying standalone script `hermite_interval_check.py` verifies the exact Gram entries by independent numerical quadrature, the all-width curvature identity for six radii, evenness, strict improvement under nonzero translation, and the asymptotic optimizer and sharp-value coefficients for four small radii. It completed 100 deterministic high-precision checks using `mpmath` at 65 decimal digits. The proof of the continuum statements is the analytic argument above, not finite testing. Reproduce with `python hermite_interval_check.py` using `mpmath`.

## Relationship to prior work
The 2023 polyanalytic Fock-kernel analysis of Lee-Guzmán, Maximenko, Ramos-Vazquez, and Sánchez-Nungaray identifies the Hermite-matrix fibers for horizontally invariant localization operators (especially its Proposition 10.4); it motivates studying the spectral supremum of a Gaussian/Hermite matrix over translations. Earlier work on horizontal-symbol Toeplitz operator algebras and matrix representations (Sánchez-Nungaray et al., 2018; Arroyo Neri et al., 2021) develops the general representation, not the present first-two-mode interval optimization and quartic maximizing-center law. Floettmann's 2022 discussion of coherent Hermite–Gaussian superpositions concerns propagation and transverse beam moments rather than optimal interval mass. No claim is made that the Hermite normalization or underlying matrix representation is new.

## Limitations
The theorem is confined to the span of the first two **normalized** Hermite functions and interval masks. It establishes existence of noncentral maximizers at every positive width but does not classify all maximizers for arbitrary widths. The three-term asymptotic is only for small widths and has no explicit quantified universal error constant. Historical priority requires external independent assessment; no independent mathematical validation or formal proof certification is claimed.

## References
1. E. Lee-Guzmán, E. A. Maximenko, G. Ramos-Vazquez, A. Sánchez-Nungaray, *Horizontal Fourier transform of the polyanalytic Fock kernel*, arXiv:2309.03410v1 (first submitted 2023-09-07), especially Proposition 10.4 and Remark 10.5. https://arxiv.org/abs/2309.03410
2. A. Sánchez-Nungaray, C. González-Flores, R. R. López-Martínez, J. L. Arroyo-Neri, *Toeplitz Operators with Horizontal Symbols Acting on the Poly-Fock Spaces*, Journal of Function Spaces 2018, article 8031259. https://doi.org/10.1155/2018/8031259
3. J. L. Arroyo Neri, A. Sánchez-Nungaray, M. Hernández Marroquin, R. R. López-Martínez, *Toeplitz Operators with Lagrangian Invariant Symbols Acting on the Poly-Fock Space of* \(\mathbb C^n\), Journal of Function Spaces 2021, article 9919243, Section 3. https://doi.org/10.1155/2021/9919243
4. K. Floettmann, *Coherent superposition of orthogonal Hermite–Gauss modes*, Optics Communications (2022), manuscript https://bib-pubdb1.desy.de/record/459328/files/1-s2.0-S0030401821007860-main.pdf
