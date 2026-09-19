# Global quadratic Hausdorff stability for the planar fractional-perimeter comparison

## Result

Let \(0<s<1\). There exists a constant \(c_s>0\) such that every planar convex body \(K\subset\mathbb R^2\) with classical perimeter
\[
L=\operatorname{Per}(K),\qquad R=\frac{L}{2\pi},
\]
satisfies
\[
\boxed{
P_s(B_R)-P_s(K)
\ge
c_s R^{-s}\inf_{x\in\mathbb R^2} d_H\!\left(K,x+\overline B_R\right)^2 .
}
\]
Here
\[
P_s(E)=\int_E\int_{\mathbb R^2\setminus E}|x-y|^{-2-s}\,dx\,dy
\]
is the fractional \(s\)-perimeter and \(d_H\) is Hausdorff distance.

Thus the sharp planar inequality saying that the disk maximizes fractional perimeter among sets of fixed classical perimeter has a global quadratic Hausdorff stability estimate within the class of convex bodies.

The power \(2\) is locally optimal. More precisely, there are smooth strictly convex bodies \(K_\varepsilon\) with \(\operatorname{Per}(K_\varepsilon)=2\pi\) such that
\[
\inf_x d_H(K_\varepsilon,x+\overline B_1)=|\varepsilon|
\]
and
\[
0\le P_s(B_1)-P_s(K_\varepsilon)\le C_s\varepsilon^2
\]
for all sufficiently small \(|\varepsilon|\).

## Context

Lin, Yang, Yang, Yuan and Zhang proved the sharp planar comparison
\[
P_s(K)\le P_s(B_1)\left(\frac{\operatorname{Per}(K)}{2\pi}\right)^{2-s}
\]
and, for convex bodies, the exact identity
\[
P_s(K)=\frac{1}{s(1-s)}C_{1-s}(K)
\]
with the chord functional \(C_q\). Their proof uses a fractional Willmore-type quantity \(W_\alpha\), a first-variation formula for \(C_q\) under outer parallel addition, and smooth approximation of convex bodies.

Frank and Ivanisvili subsequently proved the same sharp fixed-classical-perimeter comparison for arbitrary planar finite-perimeter sets. Their result gives the qualitative extremal statement, while the theorem above gives a quantitative global deficit estimate in Hausdorff distance for convex bodies.

A different recent stability theorem of Alberti, Cozzi, Massaccesi and Mirmina concerns the ratio of two fractional perimeters \(P_t/P_s\) with \(0<s<t<1\), locally near a sphere. It does not include the endpoint \(t=1\) considered here and is not a global convex-body estimate.

## Proof

By scaling it is enough to prove the assertion for
\[
\operatorname{Per}(K)=2\pi.
\]
We first assume that \(K\) is \(C^\infty_+\), and later pass to arbitrary convex bodies.

### 1. A quantitative fractional Willmore deficit

Let \(\gamma:\mathbb T_{2\pi}\to\partial K\) be positively oriented and parametrized by arclength. Write
\[
\gamma'(u)=(\cos\theta(u),\sin\theta(u)),
\qquad
\theta(u+2\pi)=\theta(u)+2\pi,
\]
and define the periodic function
\[
g(u)=\theta(u)-u.
\]
For \(w\in(0,2\pi)\), set
\[
X_w(u)=\theta(u+w)-\theta(u).
\]
Strict convexity gives \(0<X_w(u)<2\pi\), while the degree identity gives
\[
\frac1{2\pi}\int_0^{2\pi}X_w(u)\,du=w.
\]

Let
\[
\phi(t)=2\sin(t/2),\qquad
M(w)=\frac1{2\pi}\int_0^{2\pi}\phi(X_w(u))\,du.
\]
The proof of the sharp fractional Willmore inequality gives, for \(0<\alpha<1\),
\[
W_\alpha(K)\ge
\pi\int_0^{2\pi}M(w)^{-\alpha}\,dw,
\]
whereas
\[
W_\alpha(B_1)=
\pi\int_0^{2\pi}\phi(w)^{-\alpha}\,dw.
\]
Indeed, if \(A(u,w)\) and \(R(u,w)\) are the projected tangent increment and chord length used in that proof, then
\[
\int_0^{2\pi}\frac{A}{R}\,du\ge2\pi,
\qquad
\int_0^{2\pi}A\,du
\le 2\pi M(w),
\]
and Hölder's inequality yields
\[
\int_0^{2\pi} A R^{-1-\alpha}\,du\ge2\pi M(w)^{-\alpha}.
\]

Fix
\[
I=[\pi/2,3\pi/2].
\]
Since \(\phi\) is strictly concave on \((0,2\pi)\), compactness gives an absolute \(c_0>0\) such that for all \(w\in I\) and \(x\in[0,2\pi]\),
\[
\phi(w)+\phi'(w)(x-w)-\phi(x)\ge c_0(x-w)^2.
\]
Averaging in \(u\), using the mean identity for \(X_w\), gives
\[
\phi(w)-M(w)
\ge
\frac{c_0}{2\pi}
\int_0^{2\pi}|g(u+w)-g(u)|^2\,du.
\]
Since \(0<M(w)\le\phi(w)\le2\),
\[
M(w)^{-\alpha}-\phi(w)^{-\alpha}
\ge
\alpha\,2^{-\alpha-1}\,[\phi(w)-M(w)].
\]
Consequently,
\[
W_\alpha(K)-W_\alpha(B_1)
\ge
c_\alpha
\int_I\frac1{2\pi}
\int_0^{2\pi}|g(u+w)-g(u)|^2\,du\,dw.
\]
The interval \(I\) has a Fourier spectral gap: for every nonzero integer \(k\),
\[
\int_I|e^{ikw}-1|^2\,dw\ge m_0>0.
\]
Hence
\[
\boxed{
W_\alpha(K)-W_\alpha(B_1)
\ge
\kappa_\alpha
\inf_{c\in\mathbb R}
\int_0^{2\pi}|\theta(u)-u-c|^2\,du
}
\tag{1}
\]
for some \(\kappa_\alpha>0\).

### 2. Outer parallel bodies transfer the deficit to the chord functional

Write the boundary using the tangent-angle variable \(\beta\). Let
\[
\rho(\beta)=\frac{ds}{d\beta}>0
\]
be the radius of curvature, so that
\[
\int_0^{2\pi}\rho(\beta)\,d\beta=2\pi.
\]
Define
\[
F(\beta)=\int_0^\beta(\rho(t)-1)\,dt
\]
and
\[
J(K)=
\inf_{b\in\mathbb R}
\int_0^{2\pi}|F(\beta)-b|^2\,d\beta.
\]

For \(r\ge0\), put
\[
K_r=K+r\overline B_1,
\qquad
\widetilde K_r=\frac{K_r}{1+r}.
\]
The curvature radius of \(\widetilde K_r\) is
\[
\widetilde\rho_r(\beta)=\frac{\rho(\beta)+r}{1+r},
\]
and its normalized arclength is
\[
\widetilde s_r(\beta)
=
\beta+\frac{F(\beta)}{1+r}.
\]
Therefore the quantity on the right of (1), applied to \(\widetilde K_r\), equals
\[
\frac1{(1+r)^3}
\inf_b
\int_0^{2\pi}|F(\beta)-b|^2[\rho(\beta)+r]\,d\beta.
\]
For \(1\le r\le2\) this is bounded below by \(J(K)/27\). Using the scaling
\[
W_s(\lambda K)=\lambda^{1-s}W_s(K),
\]
(1) with \(\alpha=s\) gives
\[
W_s(K_r)-W_s(B_{1+r})
\ge
\frac{\kappa_s}{27}J(K),
\qquad 1\le r\le2.
\tag{2}
\]

Set \(q=1-s\) and
\[
H(r)=C_q(K_r)-C_q(B_{1+r}).
\]
The sharp convex chord inequality implies \(H(r)\le0\). The first-variation identity
\[
\frac{d}{dr}C_q(K+rB_1)=2qW_{1-q}(K+rB_1)
\]
applied at every \(r\) and (2) imply
\[
H'(r)\ge\frac{2q\kappa_s}{27}J(K),
\qquad 1\le r\le2.
\]
Since \(H(0)\le H(1)\le H(2)\le0\),
\[
C_q(B_1)-C_q(K)
=-H(0)
\ge H(2)-H(1)
\ge\frac{2q\kappa_s}{27}J(K).
\]
For convex bodies,
\[
P_s(K)=\frac{C_{1-s}(K)}{s(1-s)},
\]
and hence
\[
\boxed{
P_s(B_1)-P_s(K)\ge c_s J(K).
}
\tag{3}
\]

### 3. The angular defect controls Hausdorff distance

Let \(h(\beta)\) be the support function of \(K\). Since
\[
\rho=h+h'',
\]
and \(\operatorname{Per}(K)=2\pi\), the zeroth Fourier coefficient of \(h\) is \(1\). Translation changes only the Fourier modes \(k=\pm1\). For \(|k|\ge2\),
\[
\rho_k=(1-k^2)h_k,
\qquad
F_k=\frac{\rho_k}{ik}.
\]
Thus
\[
J(K)
=
2\pi
\sum_{|k|\ge2}
\frac{(k^2-1)^2}{k^2}|h_k|^2.
\]
Moreover
\[
\frac{(k^2-1)^2/k^2}{1+k^2}\ge\frac9{20},
\qquad |k|\ge2.
\]
After translating \(K\) to remove its first Fourier modes,
\[
J(K)\ge c\|h-1\|_{H^1(\mathbb S^1)}^2
\ge c'\|h-1\|_\infty^2.
\]
For convex bodies, the uniform distance between support functions is the Hausdorff distance. Hence
\[
\boxed{
J(K)\ge
c'\inf_{x\in\mathbb R^2}
d_H(K,x+\overline B_1)^2.
}
\tag{4}
\]
Combining (3) and (4) proves the normalized theorem.

### 4. Approximation and scaling

Every planar convex body is a Hausdorff limit of \(C^\infty_+\) planar convex bodies. Under Hausdorff convergence of convex bodies, both classical perimeter and \(C_q\) are continuous. Normalize the approximants to perimeter \(2\pi\), apply the preceding estimate, and pass to the limit. The Hausdorff asymmetry
\[
K\mapsto \inf_x d_H(K,x+\overline B_1)
\]
is continuous under Hausdorff convergence.

Finally, if \(R=\operatorname{Per}(K)/(2\pi)\), apply the normalized result to \(R^{-1}K\). Since
\[
P_s(\lambda E)=\lambda^{2-s}P_s(E),
\qquad
d_H(\lambda K,\lambda L)=\lambda d_H(K,L),
\]
the general inequality is
\[
P_s(B_R)-P_s(K)
\ge
c_sR^{-s}\inf_x d_H(K,x+\overline B_R)^2.
\]

## Local optimality of the quadratic power

For \(|\varepsilon|<1/3\), let \(K_\varepsilon\) be the convex body with support function
\[
h_\varepsilon(\theta)=1+\varepsilon\cos(2\theta).
\]
Its radius of curvature is
\[
h_\varepsilon+h_\varepsilon''
=
1-3\varepsilon\cos(2\theta)>0,
\]
and
\[
\operatorname{Per}(K_\varepsilon)=2\pi.
\]
Because \(h_\varepsilon\) is \(\pi\)-periodic, \(K_\varepsilon\) is centrally symmetric. For any translation term
\[
\ell_x(\theta)=x\cdot(\cos\theta,\sin\theta),
\]
the values at \(\theta\) and \(\theta+\pi\) imply
\[
\|\varepsilon\cos2\theta-\ell_x(\theta)\|_\infty\ge|\varepsilon|,
\]
while \(x=0\) attains equality. Therefore
\[
\inf_xd_H(K_\varepsilon,x+\overline B_1)=|\varepsilon|.
\]

The support-function perturbation expansion for the chord functional gives
\[
C_q(K_{\varepsilon,\psi})
=
C_q(B_1)
+
\varepsilon\,c_q\int_0^{2\pi}\psi
+
O(\varepsilon^2).
\]
For \(\psi(\theta)=\cos2\theta\), the linear term vanishes. Since \(P_s=C_{1-s}/[s(1-s)]\) on convex bodies,
\[
P_s(B_1)-P_s(K_\varepsilon)=O_s(\varepsilon^2).
\]
Thus no estimate with the same Hausdorff asymmetry and a power strictly smaller than \(2\) can hold uniformly near the disk.

## Significance

The qualitative fixed-perimeter theorem determines the unique extremal shape. The present estimate additionally controls geometric closeness to that shape from the analytic deficit, globally over all planar convex bodies. The mechanism is not a compactness-only argument: a quantitative Jensen gap in the tangent-angle proof is transferred through outer parallel bodies and then converted to Hausdorff distance by the support-function Fourier spectrum.

The endpoint is complementary to recent local stability results comparing two genuinely fractional perimeters \(0<s<t<1\): here the upper-order quantity is the classical perimeter \(t=1\), the estimate is global within convex bodies, and the controlled geometry is translation-invariant Hausdorff distance.

## Limitations

- The theorem is restricted to planar convex bodies. It does not provide Hausdorff stability for arbitrary finite-perimeter sets.
- The constant \(c_s\) is not optimized, and no uniform behavior as \(s\to0^+\) or \(s\to1^-\) is claimed.
- The quadratic exponent is shown to be locally optimal, but the extremizers for the quantitative deficit at finite distance are not classified.
- No higher-dimensional analogue is claimed.
- Originality is asserted only to the best of our knowledge.

## References

1. X. Lin, D. Yang, S. Yang, W. Yuan, Y. Zhang, *A Sharp Planar Fractional Isoperimetric Inequality*, arXiv:2609.19052 (2026).
2. R. L. Frank, P. Ivanisvili, *Sharp comparison between the perimeter and its fractional analogue in two dimensions*, arXiv:2609.14513 (2026).
3. G. Alberti, G. Cozzi, A. Massaccesi, J. Mirmina, *Stability of the ball in isoperimetric inequalities between two fractional perimeters*, arXiv:2605.07543 (2026).
4. F. Giannetti, G. Stefani, *On the monotonicity of non-local perimeter of convex bodies*, Topological Methods in Nonlinear Analysis (2024), DOI: 10.12775/TMNA.2024.019.
