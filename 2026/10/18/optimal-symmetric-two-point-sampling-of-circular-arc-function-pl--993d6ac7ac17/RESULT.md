# Optimal symmetric two-point sampling of circular-arc function planes

## Finding
For every \(0<\theta<\pi\), symmetric samples at two points of the circular arc determine the coefficients of every affine analytic polynomial, but their reconstruction norm depends sharply on their placement. The unique optimally conditioned symmetric pair occurs at
\[s_\theta=2\arctan\bigl(\sin(\theta/2)\bigr),\]
and the exact optimal inverse norm, at **every matrix level**, equals
\[\inf_{0<s\le\theta}\|U_{\theta,s}\|_{\mathrm{cb}}=\sqrt{1+\sin^2(\theta/2)}.\]
More precisely, the complete norm profile is
\[\boxed{\|U_{\theta,s}\|=\|U_{\theta,s}\|_{\mathrm{cb}}=\max\!\left\{\sec(s/2),\sec((\theta-s)/2),\frac{\sin(\theta/2)}{\sin(s/2)}\right\}.}\]
The two opposite polynomials \(1+z\) and \(1-z\) simultaneously saturate the optimal bound. In contrast, using the two arc endpoints costs \(\sec(\theta/2)\), which diverges as \(\theta\uparrow\pi\), whereas the optimally symmetric two-node constant tends to \(\sqrt2\).

## Assumptions and scope
Let \(K_\theta=\{e^{it}: -\theta\le t\le\theta\}\), and let \(E_\theta=\operatorname{span}_{\mathbb C}\{1,z\}\subset C(K_\theta)\), where \(z(\zeta)=\zeta\). Fix \(0<\theta<\pi\) and \(0<s\le\theta\). Define
\[R_{\theta,s}(a+bz)=(a+be^{-is},\,a+be^{is})\in\ell_\infty^2.\]
The two evaluation points are distinct, so \(R_{\theta,s}\) is injective. Give its range \(F_{\theta,s}\) the operator-space structure inherited from \(\ell_\infty^2\), and give \(E_\theta\) the structure inherited from \(C(K_\theta)\). Write \(U_{\theta,s}:F_{\theta,s}\to E_\theta\) for the inverse of \(R_{\theta,s}\). The operator \(R_{\theta,s}\) has ordinary and complete norm one. Optimization is restricted to the **symmetric** evaluation pair; this statement does not solve the unrestricted two-point node-placement problem.

## Proof
**1. Reduction to balanced scalar polynomials.** Let \(p(z)=a+bz\), not identically zero. Put \(H=|a|^2+|b|^2>0\), \(r=2|a||b|/H\in[0,1]\), and choose \(\eta\in[-\pi,\pi]\) such that \(|p(e^{it})|^2=H(1+r\cos(t-\eta))\). Define \(A=\max_{|t|\le\theta}\cos(t-\eta)\) and \(B=\max_{t\in\{-s,s\}}\cos(t-\eta)\). Because sample nodes belong to the arc, \(A\ge B\). Consequently
\[\frac{\|p\|_{C(K_\theta)}^2}{\|R_{\theta,s}p\|_{\ell_\infty^2}^2}=\frac{1+rA}{1+rB}\]
is nondecreasing in \(r\in[0,1]\). The worst case can therefore be taken with \(|a|=|b|\), or \(r=1\). If \(r=1\) and the denominator vanished then both distinct sampled points would be the unique antipode of the same point, impossible. Thus every displayed ratio is well-defined.

**2. Exact phase maximization.** By reflection take \(0\le\eta\le\pi\). At \(r=1\), \(|p(e^{it})|\) is a positive constant times \(\cos(d(t,\eta)/2)\), where \(d\) denotes shortest circular angular distance. The closest sampling point to \(\eta\) is \(s\), and the closest arc point is \(\eta\) for \(\eta\le\theta\), or the endpoint \(\theta\) otherwise. Hence the ratio equals
\[Q(\eta)=\begin{cases}\sec(|\eta-s|/2),&0\le\eta\le\theta,\\[2pt]\dfrac{\cos((\eta-\theta)/2)}{\cos((\eta-s)/2)},&\theta\le\eta\le\pi.\end{cases}\]
On \([0,\theta]\) the maximum is \(\max\{\sec(s/2),\sec((\theta-s)/2)\}\). For \(\theta\le\eta\le\pi\), the logarithmic derivative of \(Q\) is
\[\frac12\left[\tan((\eta-s)/2)-\tan((\eta-\theta)/2)\right]\ge0,\]
strict unless \(s=\theta\). The maximum on that interval is \(Q(\pi)=\sin(\theta/2)/\sin(s/2)\). This proves the exact scalar formula.

**3. The minimizing symmetric nodes.** The functions \(\sec(s/2)\) and \(\sin(\theta/2)/\sin(s/2)\) are strictly increasing and strictly decreasing, respectively, on \((0,\theta]\). They meet exactly at
\[\tan(s/2)=\sin(\theta/2),\qquad s=s_\theta.\]
Since \(\sin(\theta/2)\ge\tan(\theta/4)\) for \(0<\theta<\pi\), we have \(s_\theta\ge\theta/2\), and therefore the remaining term \(\sec((\theta-s_\theta)/2)\) does not exceed \(\sec(s_\theta/2)\). For every other \(s\), one of the first and third terms is strictly larger than their common value at \(s_\theta\). The minimum is unique, and evaluating the trigonometric identity yields
\[\sec(s_\theta/2)=\sqrt{1+\sin^2(\theta/2)}.\]
The balanced polynomial \(1+z\) witnesses \(\sec(s/2)\), while \(1-z\) witnesses \(\sin(\theta/2)/\sin(s/2)\); at the optimal parameter both witness the same exact norm.

**4. No matrix-level penalty.** Let \(A,B\in M_n(\mathbb C)\). For unit vectors \(\xi,\eta\in\mathbb C^n\), apply the scalar inequality to the affine polynomial \(\langle(A+zB)\xi,\eta\rangle\). It gives
\[\sup_{|t|\le\theta}|\langle(A+e^{it}B)\xi,\eta\rangle|\le\|U_{\theta,s}\|\max_{\sigma\in\{-s,s\}}\|A+e^{i\sigma}B\|.\]
Taking suprema over both unit vectors and the arc yields exactly \(\|U_{\theta,s}^{(n)}\|\le\|U_{\theta,s}\|\), for all \(n\ge1\). The reverse inequality follows by \(n=1\). Thus the ordinary and completely bounded norms coincide.

## Verification
The accompanying `verify.py` uses only the Python standard library and tests the piecewise phase maximization on deterministic angular grids, the unique balancing equation, and the two extremizing polynomials over seven arc widths and several distinct sampling locations. Run `python verify.py`. Its finite checks are diagnostic: the preceding monotonicity and scalar-to-matrix argument supply the exact proof for every admissible parameter and every matrix size.

## Relationship to prior work
Ray (arXiv:2610.04608v1, 2026) introduces these particular two-dimensional function planes, proves their unique operator-space structures, and proves that different arc widths yield nonisometric planes. Ray does not state a two-point sampling-conditioning theorem. Tikhonov and Yuditskii (arXiv:1809.09726v2) solve sharp Remez inequalities and pointwise extremal problems for polynomials bounded on positive-length arcs; their degree-one full-circle endpoint is relevant background, but it does not supply the exact optimal conditioning of **two isolated symmetric evaluations** on an entire arc. Pinasco and Venuti (arXiv:2608.27618) concern polynomial meshes on compact real sets; only the public abstract was accessible for comparison. No priority claim is made for the underlying elementary cosine identities.

## Limitations
Optimality is proved only among reflection-symmetric pairs; arbitrary asymmetric node choices, higher-degree polynomial spaces, and more than two sampling nodes are not classified. The algebraic parameter law assumes \(0<\theta<\pi\); statements at the endpoint \(\theta=\pi\) follow only as limits. Published priority for the exact symmetric norming constant remains subject to specialist verification, especially in the classical theory of discrete polynomial meshes. Independent validation has not been performed.

## References
1. S. K. Ray, *Unique operator space structures on a family of two dimensional Banach spaces*, arXiv:2610.04608v1 (October 3, 2026), https://arxiv.org/html/2610.04608v1.
2. S. Tikhonov and P. Yuditskii, *Sharp Remez inequality*, arXiv:1809.09726v2 (2018), https://arxiv.org/pdf/1809.09726.
3. D. Pinasco and M. V. Venuti, *Optimal polynomial meshes beyond geometric boundary regularity via Green sublevels*, arXiv:2608.27618 (2026), https://arxiv.org/abs/2608.27618.
