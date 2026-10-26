# Unique optimal two-sample norming of complex circular-arc function planes

## Finding
For every \(0<\theta<\pi\), let \(K_\theta=\{e^{it}:-\theta\le t\le\theta\}\) and let \(E_\theta=\operatorname{span}_{\mathbb C}\{1,z\}\subset C(K_\theta)\), with the uniform norm. For distinct sampling angles \(-\theta\le u<v\le\theta\), define the smallest norming constant
\[
\Lambda_\theta(u,v)=\sup_{0\ne f\in E_\theta}\frac{\|f\|_{C(K_\theta)}}{\max\{|f(e^{iu})|,|f(e^{iv})|\}}.
\]
Write \(x=(v-u)/4\) and \(m=(u+v)/2\). The *entire* two-node profile is
\[
\boxed{\displaystyle \Lambda_\theta(u,v)=\max\left\{\frac1{\cos x},\frac{\sin\bigl(\min\{(\theta+|m|)/2,\pi/2\}\bigr)}{\sin x}\right\}.}
\]
Consequently, the exact optimal two-evaluation norming constant is
\[
\boxed{\displaystyle C_\theta:=\min_{-\theta\le u<v\le\theta}\Lambda_\theta(u,v)=\sqrt{1+\sin^2(\theta/2)}.}
\]
The **unique optimal ordered pair** is
\[
\boxed{\displaystyle (u,v)=(-a_\theta,a_\theta),\qquad a_\theta=2\arctan(\sin(\theta/2)).}
\]
The function \(\theta\mapsto C_\theta\) is strictly increasing from the limiting value \(1\) to the limiting value \(\sqrt2\), and therefore recovers the arc aperture from the best two-sample constant in this canonical function representation. In marked contrast, using the two **arc endpoints** gives the inferior constant \(\Lambda_\theta(-\theta,\theta)=\sec(\theta/2)\), which diverges as \(\theta\uparrow\pi\) even though the optimal constant stays below \(\sqrt2\).

## Assumptions and scope
The scalars, linear combinations, samples and norms are complex. The parameter \(\theta\) ranges over the open interval \((0,\pi)\). The two nodes must lie on the specified arc and must be distinct. The interpolation maps below are induced by ordinary point evaluations, not by arbitrary elements of the Banach dual. The exact constant measures the smallest inverse norm of a two-point sampling map \(E_\theta\to\ell_\infty^2\) with its forward norm fixed at one. It is not asserted to equal the unrestricted Banach–Mazur distance from \(E_\theta\) to \(\ell_\infty^2\).

## Proof
**1. Exact evaluation norm.** The two values of \(f(z)=b_0+b_1z\) at distinct \(e^{iu},e^{iv}\) may be prescribed as arbitrary complex numbers \(w_u,w_v\). The Lagrange representation is
\[
f(e^{it})=\frac{e^{it}-e^{iv}}{e^{iu}-e^{iv}}\,w_u+\frac{e^{it}-e^{iu}}{e^{iv}-e^{iu}}\,w_v.
\]
For a fixed \(t\), the supremum over \(\max\{|w_u|,|w_v|\}\le1\) equals the sum of the absolute values of the two coefficients: choose the two sample phases to align both summands. Taking the supremum over \(t\) and interchanging the two suprema (both are over Cartesian products) gives
\[
\Lambda_\theta(u,v)=\sup_{|t|\le\theta}\frac{\bigl|\sin((t-u)/2)\bigr|+\bigl|\sin((t-v)/2)\bigr|}{\sin((v-u)/2)}.
\]
In particular, the denominator is strictly positive since \(0<v-u\le2\theta<2\pi\).

**2. Exact angular maximization.** Put \(x=(v-u)/4\in(0,\theta/2]\), \(m=(u+v)/2\), so the nodes are \(m-2x,m+2x\). On the interval between the two nodes the sine terms have opposite signs; their sum is \(2\sin x\cos((t-m)/2)\), and the denominator is \(\sin(2x)=2\sin x\cos x\). The maximum there is exactly \(1/\cos x\), attained at \(t=m\).

Outside the node interval the two sine terms have the same sign because all argument differences lie strictly between \(-2\pi\) and \(2\pi\). Their sum is \(2\cos x\,|\sin((t-m)/2)|\). Division by \(\sin(2x)\) yields \(|\sin((t-m)/2)|/\sin x\). Of the two exterior intervals, the farther arc endpoint is at angular distance \(\theta+|m|\) from the midpoint. The largest sine magnitude obtainable there equals \(\sin(\min\{(\theta+|m|)/2,\pi/2\})\): either the endpoint is reached before angular distance \(\pi\), or the exterior interval contains a point at distance \(\pi\). The opposite exterior interval cannot give a larger value. Combining the interior and exterior suprema proves the displayed exact two-node formula. The statement includes all endpoint cases, including \(u=-\theta\) or \(v=\theta\).

**3. Sharp optimization.** Set \(s=\sin(\theta/2)\in(0,1)\). Since \(\theta+|m|\ge\theta\), the exact formula gives the universal lower bound
\[
\Lambda_\theta(u,v)\ge\max\{\sec x,s/\sin x\}.
\]
On \(0<x\le\theta/2<\pi/2\), the first term increases strictly and the second decreases strictly. They meet at the unique point \(x_*=\arctan s\), since the equality is \(\tan x=s\). This point is feasible: \(x_*<\theta/2\), because \(\tan(\theta/2)>\sin(\theta/2)\). Their common value is \(\sqrt{1+s^2}\). Hence no pair of points has a smaller norming constant.

At the symmetric pair \(u=-2x_*,v=2x_*\) we have \(m=0\), so the exact formula gives \(\Lambda_\theta(-2x_*,2x_*)=\max\{\sec x_*,s/\sin x_*\}=\sqrt{1+s^2}\). This proves existence and sharpness.

**4. Unique optimizer.** Strict monotonicity of the two lower-bound terms forces \(x=x_*\) for every minimizing pair. If \(m\ne0\), then \(\sin(\min\{(\theta+|m|)/2,\pi/2\})>s\), because \(0<\theta<\pi\) and the capped sine is strictly increasing until its cap. The exterior term in the exact formula is then strictly larger than \(s/\sin x_*\), contradicting minimality. Thus \(m=0\); the two samples are precisely the stated pair. Finally, \(s\) increases strictly with \(\theta\), so \(C_\theta\) does also, and its endpoint limits are \(1\) and \(\sqrt2\).

## Verification
All identities above hold for every real \(0<\theta<\pi\), without discretization or numerical assumptions. The standalone `check_sampling.py` evaluates the exact closed formula and a direct Lagrange-coefficient expression on deterministic finite grids at eight apertures, and tests 2,400 pseudorandom admissible node pairs against the proposed global bound. Its expected success marker is `CIRCULAR_ARC_SAMPLING_CHECK_OK`. These finite tests corroborate normalization, but cannot establish the all-parameter theorem; that conclusion follows from the four analytic steps above.

## Relationship to prior work
Samya Kumar Ray, *Unique operator space structures on a family of two dimensional Banach spaces* (arXiv:2610.04608v1, posted 2026-10-03), introduces precisely \(E_\theta\), proves uniqueness of its operator-space structure and nonisometry of these planes, and proves that no \(E_\theta\) is isometric to \(\ell_\infty^2\) (Proposition 2). The exact two-evaluation norming constant, its full two-node profile, and the unique optimal locations do not appear in that full text. They provide a quantitative sampling analogue of the qualitative nonisometry observation, not an alternative proof of the operator-space result.

The published study *The unique optimal Hilbertian metric for circular-arc function planes freezes at a semicircle* concerns the optimal Hermitian quadratic norm and the Hilbertian Banach–Mazur distance to \(\ell_2^2\), not the inverse norms of the two evaluation maps into \(\ell_\infty^2\). Its Hilbertian result does not determine the two-sample constant or its optimizers. General Lebesgue-constant literature, including B. A. Ibrahimoglu's survey, treats polynomial interpolation and optimal sampling over real intervals, rather than this complex circular-arc two-point profile; the elementary Lagrange representation itself is standard and not claimed to be new. A 2018 disk-interpolation study treats real bivariate polynomial spaces on the *filled disk*, requiring three nodes for linear interpolation, so it does not imply the present complex two-node circular-arc formula.

## Limitations
The theorem concerns only two point evaluations of complex affine functions on a single proper arc; it does not optimize over arbitrary invertible linear maps into \(\ell_\infty^2\), more than two nodes, higher polynomial degrees, or disjoint arcs. Although the specified literature comparison did not identify the same exact profile, possible older formulations of the degree-one complex Lebesgue constant on arcs remain a priority risk. Exhaustive historical priority is not established.

## References
1. Samya Kumar Ray, *Unique operator space structures on a family of two dimensional Banach spaces*, arXiv:2610.04608v1, first public 2026-10-03, https://arxiv.org/html/2610.04608v1.
2. *The unique optimal Hilbertian metric for circular-arc function planes freezes at a semicircle*, published-finding corpus published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-unique-optimal-hilbertian-metric-for-circular-arc-function-p--c1c0ee781ccd.
3. B. A. Ibrahimoglu, *Lebesgue functions and Lebesgue constants in polynomial interpolation*, Journal of Inequalities and Applications 2016, article 93, https://doi.org/10.1186/s13660-016-1030-3.
4. *On the computation of sets of points with low Lebesgue constant on the unit disk*, Journal of Computational and Applied Mathematics (2018), https://doi.org/10.1016/j.cam.2018.06.051.
