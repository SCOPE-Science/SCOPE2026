# Sharp two-point Lebesgue constants and inward optimal nodes on circular arcs

## Finding

For each \(0<\theta<\pi\), let \(K_\theta=\{e^{it}:-\theta\le t\le\theta\}\), and let \(E_\theta=\operatorname{span}_{\mathbb C}\{1,z\}\subset C(K_\theta)\), where \(z(\zeta)=\zeta\). For any two distinct node angles \(-\theta\le u<v\le\theta\), let \(I_{u,v}:C(K_\theta)\to E_\theta\) be the unique complex-linear operator satisfying \((I_{u,v}f)(e^{iu})=f(e^{iu})\) and \((I_{u,v}f)(e^{iv})=f(e^{iv})\). Its norm is the corresponding Lebesgue constant.

**Sharp two-node interpolation theorem.** For every \(0<\theta<\pi\),
\[
\inf_{-\theta\le u<v\le\theta}\|I_{u,v}\|_{C(K_\theta)\to C(K_\theta)}
=\sqrt{1+\sin^2(\theta/2)}.
\]
The infimum is attained at exactly one unordered pair of angles,
\[
\boxed{\{u,v\}=\{-2\arctan(\sin(\theta/2)),\ 2\arctan(\sin(\theta/2))\}.}
\]
Both optimally conditioned nodes lie strictly inside the arc. In contrast, the endpoint-node interpolant has norm
\[
\|I_{-\theta,\theta}\|=\sec(\theta/2)>\sqrt{1+\sin^2(\theta/2)}.
\]
Consequently, the best possible norm is always less than \(\sqrt2\), and approaches \(\sqrt2\) as \(\theta\uparrow\pi\), whereas the endpoint-node norm diverges. As \(\theta\downarrow0\), the optimal norm is \(1+\theta^2/8+O(\theta^4)\).

## Assumptions and scope

The scalar field is complex. The target is the degree-at-most-one analytic polynomial subspace \(E_\theta\), with the supremum norm inherited from the specified closed arc. The input class is **all** complex-valued continuous functions on that arc; no smoothness, analyticity, or probability model is imposed. Exactly two distinct sample nodes are used, and the interpolant is the unique affine complex polynomial matching their values. The minimization is over every pair of nodes on the arc, including asymmetric and endpoint pairs. Only arcs with \(0<\theta<\pi\) are asserted; the two endpoints coincide at \(\theta=\pi\), and the point arc is degenerate at \(\theta=0\).

## Proof

**1. Exact evaluation formula.** The Lagrange basis at \(e^{iu}\) and \(e^{iv}\) is
\[
L_u(z)=\frac{z-e^{iv}}{e^{iu}-e^{iv}},\qquad
L_v(z)=\frac{z-e^{iu}}{e^{iv}-e^{iu}}.
\]
Therefore, for \(t\in[-\theta,\theta]\),
\[
|(I_{u,v}f)(e^{it})|\le\bigl(|L_u(e^{it})|+|L_v(e^{it})|\bigr)\|f\|_\infty.
\]
This bound is sharp at each fixed \(t\): prescribe the two unit-modulus node values with phases making the Lagrange contributions agree, then join those values continuously inside the closed complex unit disk. Hence
\[
\|I_{u,v}\|=\max_{-\theta\le t\le\theta}
\frac{|e^{it}-e^{iu}|+|e^{it}-e^{iv}|}{|e^{iv}-e^{iu}|}.
\tag{1}
\]
No discretization or extremal-function regularity is involved.

**2. The three-interval Lebesgue function.** Set
\[
m=(u+v)/2,\qquad d=(v-u)/4.
\]
Then \(0<d\le\theta/2<\pi/2\) and \(|m|\le\theta-2d\). Elementary chord identities, using the positivity of the relevant half-angle sines, transform the quotient in (1) into
\[
\ell_{m,d}(t)=\begin{cases}
\sin((m-t)/2)/\sin d,&-\theta\le t\le m-2d,\\
\cos((t-m)/2)/\cos d,&m-2d\le t\le m+2d,\\
\sin((t-m)/2)/\sin d,&m+2d\le t\le\theta.
\end{cases}
\tag{2}
\]
In particular, the midpoint \(t=m\) yields \(\|I_{u,v}\|\ge\sec d\). If \(m\ge0\), the test point \(t=m-\theta\) lies in the left exterior interval, giving \(\|I_{u,v}\|\ge\sin(\theta/2)/\sin d\); if \(m\le0\), use \(t=m+\theta\) on the right. Thus for every admissible pair,
\[
\|I_{u,v}\|\ge F_\theta(d):=
\max\left\{\sec d,\frac{\sin(\theta/2)}{\sin d}\right\}.
\tag{3}
\]

**3. Symmetric pairs attain the exact lower envelope.** When \(m=0\), the middle branch of (2) has maximum \(\sec d\). On both exterior intervals, the argument of the sine lies in \([d,\theta/2]\subset(0,\pi/2)\), where sine is increasing. Their maximum is therefore \(\sin(\theta/2)/\sin d\). Consequently
\[
\|I_{-2d,2d}\|=F_\theta(d)\qquad(0<d\le\theta/2).
\tag{4}
\]

**4. Exact minimax and rigidity.** On \((0,\theta/2]\), \(d\mapsto\sec d\) is strictly increasing and \(d\mapsto\sin(\theta/2)/\sin d\) is strictly decreasing. They cross exactly at
\[
\tan d_*=\sin(\theta/2),\qquad d_*=\arctan(\sin(\theta/2)).
\]
This crossing is admissible and interior, since \(\arctan(\sin x)<x\) for \(0<x<\pi/2\). Equations (3)–(4) show that the minimum equals \(F_\theta(d_*)=\sec d_*=\sqrt{1+\sin^2(\theta/2)}\). Strict monotonicity forces \(d=d_*\) for any minimizer.

It remains to exclude asymmetric nodes at this separation. If \(m>0\), choose \(0<\varepsilon<\min\{m,\pi-\theta\}\). Then \(t=m-\theta-\varepsilon\in[-\theta,m-2d_*]\), so (2) gives
\[
\ell_{m,d_*}(t)=\frac{\sin((\theta+\varepsilon)/2)}{\sin d_*}>
\frac{\sin(\theta/2)}{\sin d_*}=F_\theta(d_*).
\]
If \(m<0\), the reflected choice \(t=m+\theta+\varepsilon\), with \(0<\varepsilon<\min\{-m,\pi-\theta\}\), gives the same strict inequality. Thus \(m=0\) is necessary, proving uniqueness of the unordered node pair. Finally, (4) at \(d=\theta/2\) gives the stated endpoint norm. The limiting statements follow from the exact formulas by continuity and Taylor expansion.

## Verification

The proof above establishes the result for every real parameter in the claimed open interval and every continuous complex input function. The independent implementations in `arc_two_node_checker.py` evaluate (1) by complex chord arithmetic, compare it to (3), test 250 fixed-seed node pairs at each of six distinct angles, verify the optimized node norms and endpoint-node norms, and check the asymmetry obstruction. The checker passed **4,539 deterministic finite diagnostic assertions** in the supplied package. These diagnostics corroborate the algebra but are not an exhaustive search or an infinite-dimensional proof. To reproduce: execute `python3 arc_two_node_checker.py` with a Python 3 standard library; no external dependencies are required.

## Relationship to prior work

Ray (arXiv:2610.04608v1, publicly posted 2026-10-03) introduced this exact circular-arc function-space family in the study of unique operator-space structures and proved isometric-geometry results. The text inspected in its introduction and main results does not contain this two-node interpolation minimax or an equivalent sampling-norm statement. The new assertion concerns optimal reconstruction from arbitrary continuous data, rather than operator-space uniqueness or Euclidean distortion.

Chui and Zhong (arXiv:2209.07101) study growth and adaptation of interpolation Lebesgue constants on more general complex arcs for increasing interpolation degree. The inspected introduction and principal stated results concern asymptotic degree growth, not the exact fixed-degree-one node minimax for a circular subarc. Nevskii (arXiv:2405.01254) studies minimal real-affine interpolation-projector norms on full-dimensional convex bodies with \(n+1\) real nodes; that setting does not directly imply a sharp two-**complex**-node projector on a nonconvex circular arc. The usual inequality relating interpolation error to the Lebesgue constant is classical and is not presented as a new result here.

## Limitations

The theorem optimizes the norm among **two-node Lagrange interpolation projectors** only; it does not claim minimal norm over every bounded linear projection from \(C(K_\theta)\) onto \(E_\theta\), nor among noisy or randomized nonlinear recovery methods. The stated sharp formula applies only to the first-degree complex polynomial subspace and to centered circular arcs of length less than a full circle. No new general high-degree interpolation theorem is asserted. Older interpolation theory might include this exact special case under different language; publication priority is subject to independent expert review. No independent validation or audit has occurred.

## References

1. S. K. Ray, *Unique operator space structures on a family of two dimensional Banach spaces*, arXiv:2610.04608v1 (2026-10-03), https://arxiv.org/html/2610.04608v1.
2. C. K. Chui and L. Zhong, *Order of uniform approximation by polynomial interpolation in the complex plane and beyond*, arXiv:2209.07101 (2022), https://arxiv.org/abs/2209.07101.
3. M. Nevskii, *Optimal Lagrange Interpolation Projectors and Legendre Polynomials*, arXiv:2405.01254 (2024), https://arxiv.org/abs/2405.01254.
