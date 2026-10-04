# Equivalent Hilbert norms have intrinsic distance exactly three times the log distance
## Finding
Let \(H\) be a nonzero real Hilbert space and let \(p,q\) be equivalent Hilbert norms on the same underlying vector space. Then \([p]\) and \([q]\) belong to the same intrinsic part of the cone \(\mathcal N(H)\) of equivalent norms, and
\[
d_{\mathcal N(H)}([p],[q])=3d_{\log}([p],[q]).
\]
More precisely, use the inner product inducing \(p\). There is a unique bounded positive invertible self-adjoint operator \(A\) such that
\[
q(x)^2=\langle Ax,x\rangle_p.
\]
Write \(m=\inf\sigma(A)>0\) and \(M=\sup\sigma(A)<\infty\). Then
\[
m_{\log}(q/p)=\sqrt m,\qquad M_{\log}(q/p)=\sqrt M,
\]
and the triangular defects \(\Delta_r(x,y)=r(x)+r(y)-r(x+y)\) satisfy the sharp comparison
\[
\frac{m}{\sqrt M}\,\Delta_p(x,y)\le \Delta_q(x,y)\le \frac{M}{\sqrt m}\,\Delta_p(x,y)
\]
for all \(x,y\in H\). Both constants are optimal, so
\[
m_{\log}(\Delta_q/\Delta_p)=\frac{m}{\sqrt M},\qquad M_{\log}(\Delta_q/\Delta_p)=\frac{M}{\sqrt m}.
\]

## Assumptions and scope
The result concerns real Hilbert spaces of arbitrary dimension, finite or infinite, and Hilbert norms that are equivalent on the same underlying vector space. The intrinsic metric is the Hilbert projective metric induced by the cone \(\mathcal N(H)\cup\{0\}\), in the sense introduced in arXiv:2609.28922v1. If \(M=m\), then \(q\) is a positive scalar multiple of \(p\), so both projective distances are zero and the formula is immediate. The proof below treats \(M>m\); the scalar case is its degenerate endpoint.

## Proof
Fix the inner product inducing \(p\), and write \(q(x)^2=\langle Ax,x\rangle_p\) with \(A\) positive, bounded, self-adjoint and invertible. The spectral bounds give
\[
mp(x)^2\le q(x)^2\le Mp(x)^2,
\]
hence the optimal pointwise comparison constants are \(\sqrt m\) and \(\sqrt M\).

For nonzero \(x,y\), put \(u=x/p(x)\), \(v=y/p(y)\),
\[
a_u=\langle Au,u\rangle_p,\qquad a_v=\langle Av,v\rangle_p.
\]
Rationalizing the triangular defect of a Hilbert norm gives
\[
\Delta_p(x,y)=\frac{2p(x)p(y)(1-\langle u,v\rangle_p)}{p(x)+p(y)+p(x+y)}
\]
and
\[
\Delta_q(x,y)=\frac{2p(x)p(y)(\sqrt{a_ua_v}-\langle Au,v\rangle_p)}{q(x)+q(y)+q(x+y)}.
\]
Pairs with \(\Delta_p(x,y)=0\) lie on the same positive ray, and then \(\Delta_q(x,y)=0\) as well, so only \(\Delta_p(x,y)>0\) needs consideration.

Set \(B=A-mI\ge0\). By Cauchy--Schwarz for the positive form induced by \(B\),
\[
\langle Bu,v\rangle_p\le \sqrt{\langle Bu,u\rangle_p\langle Bv,v\rangle_p}.
\]
For nonnegative \(s,t\),
\[
\sqrt{(m+s)(m+t)}\ge m+\sqrt{st},
\]
so, with \(s=a_u-m\) and \(t=a_v-m\),
\[
\sqrt{a_ua_v}-\langle Au,v\rangle_p\ge m(1-\langle u,v\rangle_p).
\]
For the opposite inequality set \(C=MI-A\ge0\). Again Cauchy--Schwarz gives
\[
\langle Cu,v\rangle_p\le\sqrt{(M-a_u)(M-a_v)},
\]
and the two-dimensional Cauchy--Schwarz inequality gives
\[
\sqrt{(M-a_u)(M-a_v)}+\sqrt{a_ua_v}\le M.
\]
Therefore
\[
\sqrt{a_ua_v}-\langle Au,v\rangle_p\le M(1-\langle u,v\rangle_p).
\]
Finally,
\[
\sqrt m\,[p(x)+p(y)+p(x+y)]\le q(x)+q(y)+q(x+y)\le \sqrt M\,[p(x)+p(y)+p(x+y)].
\]
Combining the last three displays yields
\[
\frac{m}{\sqrt M}\Delta_p(x,y)\le\Delta_q(x,y)\le\frac{M}{\sqrt m}\Delta_p(x,y).
\]

It remains to prove optimality. Assume \(M>m\). For every sufficiently small \(\varepsilon>0\), the spectral subspaces of \(A\) corresponding to \([M-\varepsilon,M]\) and \([m,m+\varepsilon]\) are nonzero and orthogonal. Choose unit vectors \(u_\varepsilon,v_\varepsilon\) in these subspaces and write
\[
\alpha_\varepsilon=\langle Au_\varepsilon,u_\varepsilon\rangle_p,\qquad
\beta_\varepsilon=\langle Av_\varepsilon,v_\varepsilon\rangle_p.
\]
Then \(\langle Au_\varepsilon,v_\varepsilon\rangle_p=0\), \(\alpha_\varepsilon\to M\), and \(\beta_\varepsilon\to m\) along a sequence \(\varepsilon\downarrow0\). For fixed \(\varepsilon\), Taylor expansion at \(t=0\) gives
\[
\Delta_p(u_\varepsilon,u_\varepsilon+t v_\varepsilon)=\frac14t^2+O(t^4),
\]
\[
\Delta_q(u_\varepsilon,u_\varepsilon+t v_\varepsilon)=\frac{\beta_\varepsilon}{4\sqrt{\alpha_\varepsilon}}t^2+O(t^4).
\]
Hence the defect ratio approaches \(\beta_\varepsilon/\sqrt{\alpha_\varepsilon}\), and then \(m/\sqrt M\) as \(\varepsilon\downarrow0\). Swapping the low- and high-spectral vectors yields the limiting ratio \(M/\sqrt m\). Thus the comparison constants are sharp.

Acosta-Portilla's intrinsic-part criterion now places \(p\) and \(q\) in the same part. His metric formula gives
\[
d_{\mathcal N(H)}([p],[q])=
\log\frac{\max\{\sqrt M,M/\sqrt m\}}{\min\{\sqrt m,m/\sqrt M\}}
=\frac32\log\frac{M}{m}.
\]
Since
\[
d_{\log}([p],[q])=\log\frac{\sqrt M}{\sqrt m}=\frac12\log\frac{M}{m},
\]
the claimed factor \(3\) follows.

## Verification
The proof is symbolic. The only nonstandard inputs are the intrinsic-part criterion and intrinsic-distance formula of arXiv:2609.28922v1. The spectral-subspace sharpness argument uses the standard spectral theorem for bounded self-adjoint operators. As a finite-dimensional sanity check, random positive definite matrices in dimensions \(2,3,5\) numerically produced triangular-defect ratios inside the predicted interval; that experiment is not used as proof.

## Relationship to prior work
Acosta-Portilla introduces the triangular-defect criterion and the intrinsic metric formula, and computes a specific two-dimensional family
\[
p(x,y)=\sqrt{x^2+y^2},\qquad q(x,y)=\sqrt{ax^2+y^2}
\]
for \(a>1\), obtaining \(d_{\mathcal N}([p],[q])=3d_{\log}([p],[q])\). The result here proves that this factor is not a peculiarity of that diagonal two-dimensional example: it holds for every pair of equivalent Hilbert norms in every real Hilbert dimension, including infinite dimension, with exact defect constants determined solely by the spectral endpoints of the relative positive operator.

Searches for the arbitrary-Hilbertian statement, for the exact constants \(m/\sqrt M\) and \(M/\sqrt m\), and for a condition-number formulation did not locate a covering statement. Classical Hilbert-projective metrics on positive-definite operators concern a different ambient cone and do not imply the triangular-defect metric identity proved here.

## Limitations
The theorem is restricted to Hilbertian renormings. It does not claim that non-Hilbert equivalent norms lie in the same intrinsic part, and the source gives examples where they do not. The result uses only the extreme spectral values \(m\) and \(M\); it does not describe geodesics or curvature of the Hilbertian subcone. The source preprint is recent, so an equivalent statement may exist in literature not exposed by the searches performed.

## References
1. J. R. Acosta-Portilla, *Intrinsic Hilbert metrics on cones of equivalent norms*, arXiv:2609.28922v1, 2026. In particular Theorem 4.6, Theorem 5.2, and Example 5.6.
2. Standard spectral theorem for bounded self-adjoint operators on a real Hilbert space.