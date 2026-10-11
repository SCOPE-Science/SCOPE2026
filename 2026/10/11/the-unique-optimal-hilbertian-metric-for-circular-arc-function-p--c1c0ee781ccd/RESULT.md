# The unique optimal Hilbertian metric for circular-arc function planes freezes at a semicircle

## Finding
For each \(0<\theta<\pi\), put \(K_\theta=\{e^{it}:|t|\le\theta\}\), and give \(E_\theta=\operatorname{span}_{\mathbb C}\{1,z\}\subset C(K_\theta)\) the norm
\[
N_\theta(a,b)=\max_{|t|\le\theta}|a+be^{it}|.
\]
Define \(\rho_\theta=\max\{\cos\theta,0\}\) and the positive definite Hermitian quadratic form
\[
H_\theta(a,b)^2=|a|^2+|b|^2+2\rho_\theta\operatorname{Re}(a\overline b).
\]
Then \(H_\theta\le N_\theta\le\sqrt2 H_\theta\) pointwise, both constants are attained by nonzero vectors, and **every** complex-linear isomorphism from this plane to a complex Hilbert plane has distortion at least \(\sqrt2\). More precisely, for every positive definite Hermitian form \(Q\),
\[
\frac{\sup_{x\ne0}N_\theta(x)/\sqrt{Q(x)}}{\inf_{x\ne0}N_\theta(x)/\sqrt{Q(x)}}\ge\sqrt2,
\]
with equality **if and only if** \(Q=cH_\theta^2\) for some positive real \(c\).

Thus the unique optimal Hilbertian quadratic form, up to scale, depends nontrivially on \(\theta\) for \(0<\theta<\pi/2\), but is exactly \(|a|^2+|b|^2\) for the entire interval \(\pi/2\le\theta<\pi\). The transition angle is sharp. This explicitly determines the metric, not merely the already-known Banach–Mazur distance.

## Assumptions and scope
All spaces and isomorphisms are **complex**. The parameter satisfies \(0<\theta<\pi\); no claim is made at the degenerate arc \(\theta=0\). A Hilbertian quadratic form means a positive definite complex Hermitian form; its square root defines a Hilbert norm. The optimum runs over **all** such forms, including ones with complex off-diagonal terms. Scalar multiples represent the same distortion. The arcs and norms coincide with those introduced in the cited 2026 preprint.

## Proof
Write \(s=\theta/2\), \(c=\cos s\), \(h=\sin s\), \(u=a+b\), and \(v=a-b\). As
\[
a+be^{it}=e^{it/2}\bigl(u\cos(t/2)-iv\sin(t/2)\bigr),
\]
we have the equivalent norm
\[
F_s(u,v)=\max_{|r|\le s}|u\cos r-iv\sin r|.
\]
The involution \((u,v)\mapsto(u,-v)\) preserves this norm. Set \(q_y(u,v)=|u|^2+y|v|^2\) for \(y>0\).

**Exact diagonal extremal ratios.** Directly,
\[
M_s(y):=\sup_{(u,v)\ne(0,0)}\frac{F_s(u,v)^2}{q_y(u,v)}=\max\{1,c^2+h^2/y\}.
\]
Indeed, for each fixed \(r\), the squared dual norm of \((\cos r,-i\sin r)\) with respect to \(q_y\) is \(\cos^2r+\sin^2r/y\); taking the supremum for \(|r|\le s\) gives the formula. Moreover, the values at \(r=0\) and the average of the squares at \(r=\pm s\) imply
\[
F_s(u,v)^2\ge\max\{|u|^2,c^2|u|^2+h^2|v|^2\}.
\]
For \(u,v\) with the same complex phase, equality holds in this lower bound. Minimization over the ratio \(|v|^2/|u|^2\in[0,\infty]\), including the limiting axis, therefore yields
\[
m_s(y):=\inf_{(u,v)\ne(0,0)}\frac{F_s(u,v)^2}{q_y(u,v)}=\min\{1/(1+y),h^2/y\}.
\]
(The two candidate minima are achieved by \((u,v)=(1,1)\) and \((0,1)\).)

**Optimization of diagonal forms.** Let \(b=h^2/c^2=\tan^2s\). The squared distortion is exactly \(M_s(y)/m_s(y)\). If \(b\le1\), it decreases strictly to \(y=b\) and increases strictly thereafter: for \(y\le b\) it equals \(1+c^2y+h^2/y\), for \(b\le y\le1\) it equals \(1+c^2y/h^2\), and for \(y\ge1\) it equals \(y/h^2\). If \(b\ge1\), it decreases strictly up to \(y=1\), then increases strictly: on \(y\le1\) it is \(1+c^2y+h^2/y\), on \(1\le y\le b\) it is \(1+y\), and on \(y\ge b\) it is \(y/h^2\). Therefore its unique minimizer is
\[
y_* =\min\{\tan^2s,1\},\qquad M_s(y_*)/m_s(y_*)=2.
\]
Scaling the diagonal form to have minimum ratio one gives
\[
Q_s(u,v)=\begin{cases}c^2|u|^2+h^2|v|^2,&0<s\le\pi/4,\\(|u|^2+|v|^2)/2,&\pi/4\le s<\pi/2.\end{cases}
\]
The two formulae agree at the junction. In the original coordinates, \(Q_s=H_\theta^2\), and \(\inf F_s^2/Q_s=1\), \(\sup F_s^2/Q_s=2\).

**No off-diagonal form can improve or tie differently.** Suppose an arbitrary positive Hermitian \(Q\) has distortion \(\sqrt2\). Multiply \(Q\) by a positive scalar so that \(Q\le F_s^2\le2Q\). Averaging this inequality with its image under \((u,v)\mapsto(u,-v)\) shows the diagonal part of \(Q\) also has distortion at most \(\sqrt2\). By the unique diagonal minimizer and the sharp ratios of \(Q_s\), this diagonal part is exactly \(Q_s\), not merely proportional to it. Hence
\[
Q(u,v)=Q_s(u,v)+2\operatorname{Re}(\gamma u\overline v)
\]
for some \(\gamma\in\mathbb C\). At the two vectors \((u,v)=(1,1),(1,-1)\), we have \(F_s^2=Q_s=1\); the lower inequality \(Q\le F_s^2\) forces \(\operatorname{Re}\gamma=0\). If \(s\le\pi/4\), use the two vectors \((1,i\cot s)\) and \((1,-i\cot s)\): at each, \(F_s^2=2Q_s\), attained at an arc endpoint. If \(s\ge\pi/4\), instead use \((1,i)\) and \((1,-i)\): at each, \(F_s^2=2Q_s\), attained at \(r=\pm\pi/4\). In both cases the upper inequality \(F_s^2\le2Q\) forces \(\operatorname{Im}\gamma=0\). Hence \(Q=Q_s\) after normalization, proving full uniqueness and optimality.

Finally, \(Q_s=c^2|a+b|^2+h^2|a-b|^2\) before the threshold, which is \(|a|^2+|b|^2+2\cos\theta\operatorname{Re}(a\overline b)\). After the threshold, \(Q_s=(|a+b|^2+|a-b|^2)/2=|a|^2+|b|^2\). Since \(\cos\theta\) is strictly decreasing until \(\pi/2\), the claimed sharp metric-freezing transition follows.

## Verification
The identities for \(M_s(y)\) and \(m_s(y)\) can be checked independently by fixed-angle weighted Cauchy–Schwarz and by one-variable minimization. All equality vectors are given explicitly in the proof. The standalone file `verify_arc.py` tests the claimed bounds and contact vectors at five angles on both sides of the transition, along with deterministic complex-coordinate samples; execution ends with `ARC_HILBERT_FINITE_CHECK_OK`. The finite checker is supplementary and does **not** establish the all-parameter or uniqueness assertions, which follow from the analytic proof.

## Relationship to prior work
Ray, *Unique operator space structures on a family of two dimensional Banach spaces* (arXiv:2610.04608v1, first posted 2026-10-03), introduces this exact family and establishes operator-space uniqueness and pairwise nonisometry. Arias–Figiel–Johnson–Schechtman, *Banach spaces with the 2-summing property* (arXiv:math/9403206v1; published 1995), prove in Corollary 2.8 that every complex two-dimensional subspace of a \(C(K)\)-space containing a unimodular function has the 2-summing property. Their general maximal-distance theorem therefore already yields \(d_{\mathrm{BM}}(E_\theta,\ell_2^2)=\sqrt2\), and their discussion of Maurey's distance-ellipsoid theorem can yield abstract uniqueness of an optimizer in complex dimension two. **Neither result is claimed as new.** The present contribution is the explicit unique optimizing quadratic form, its sharp semicircle phase boundary, and its constancy for all longer proper arcs. Related published exact-distance computations for real Lorentz and Cesàro planes concern different norms and do not imply this parameterized complex-arc optimizer.

## Limitations
The theorem concerns only these two-dimensional complex circular-arc function spaces and Hilbertian (Hermitian) renormings. It does not give a stability modulus for near-optimal forms or classify arbitrary higher-dimensional function systems. The complete text of Ray's 2026 preprint was not accessible for the literature comparison; its abstract was read, so possible implicit coverage of the exact quadratic form remains a specific originality risk requiring a separate full-text comparison.

## References
1. Samya Kumar Ray, *Unique operator space structures on a family of two dimensional Banach spaces*, arXiv:2610.04608v1 (2026-10-03), https://arxiv.org/abs/2610.04608.
2. A. Arias, T. Figiel, W. B. Johnson, G. Schechtman, *Banach spaces with the 2-summing property*, arXiv:math/9403206v1 (1994); *Transactions of the American Mathematical Society* 347 (1995), 3835–3857, https://doi.org/10.1090/S0002-9947-1995-1303114-X.
