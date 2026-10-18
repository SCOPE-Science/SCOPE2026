# A spectral volume law and exponential Mahler growth for wheel Lipschitz-free spaces

## Finding
For every integer \(m\ge3\), let \(M_m\) be the vertex set of the unit-edge wheel graph \(K_1*C_m\), with its shortest-path metric; write \(o\) for the hub. Let \(P_m\) be the unit ball of the real Lipschitz-free space \(\mathcal F(M_m)\) in hub-anchored molecular coordinates, and let \(Q_m=P_m^\circ\). Put \(\theta=\arctan(3/4)\) and \(W_m=\operatorname{vol}_m(Q_m)\). Then the following absolutely convergent series evaluates the polar volume in **every** dimension:
\[
W_m=\sum_{k\in\mathbb Z}\left(\frac1{(\theta+2\pi k)^m}+\frac1{(\pi/2+2\pi k)^m}\right).
\]
Moreover, for \(|z|<\theta\),
\[
\sum_{m=2}^\infty W_m z^{m-2}=\frac{\tan(z/2)}{z}\left(\frac5{1-3\tan(z/2)}+\frac1{1-\tan(z/2)}\right),
\]
where the constant term \(W_2=3\) is a formal trace-square coefficient, not the volume of a wheel with a two-vertex rim. The initial actual volumes \(W_3,W_4,W_5,W_6\) are \(4,6,55/6,283/20\).

Using the **previously known** primal wheel-volume formula of D'Alì–Delucchi–Michałek, the affine-invariant Mahler product is
\[
\operatorname{vol}_m(P_m)\operatorname{vol}_m(Q_m)
=\frac{\bigl((1+\sqrt3)^m+(1-\sqrt3)^m-2\mathbf1_{2\mid m}\bigr)W_m}{m!}.
\]
Consequently, if \(R_m\) is this product divided by the Hanner value \(4^m/m!\), then
\[
R_m\sim\left(\frac{1+\sqrt3}{4\arctan(3/4)}\right)^m,
\qquad \lim_{m\to\infty}R_m^{1/m}=\frac{1+\sqrt3}{4\arctan(3/4)}>1.
\]
The exponential base is approximately \(1.0614009712788661\). The new claims are the exact **dual** volumes, their generating function, and the resulting exact volume-product asymptotic; the primal volumes are explicitly attributed to prior work.

## Assumptions and scope
All volumes use ordinary Lebesgue measure in the dual pair of hub-anchored coordinates \((x_1,\ldots,x_m)\), in which the primal molecules are \(\pm e_i\) for hub edges and \(\pm(e_i-e_{i+1})\) for rim edges (cyclic indices). Hence
\[
Q_m=\left\{x\in[-1,1]^m:\ |x_i-x_{i+1}|\le1\quad(i\bmod m)\right\}.
\]
The wheel has \(m+1\) vertices, and \(\dim \mathcal F(M_m)=m\). All results hold for every integer \(m\ge3\) without genericity, positivity, or parity conditions beyond unit edge lengths. The formal coefficient at \(m=2\) is used only in the generating function.

## Proof
**1. Transfer trace.** Define a compact self-adjoint Hilbert–Schmidt integral operator on \(L^2([-1,1])\) by
\[
(Kf)(x)=\int_{-1}^1 \mathbf 1_{|x-y|\le1}\,f(y)\,dy.
\]
For every \(m\ge3\), cyclic Fubini integration and the trace formula for positive integer powers of a Hilbert–Schmidt integral operator give
\[
W_m=\int_{[-1,1]^m}\prod_{j=1}^m\mathbf1_{|x_j-x_{j+1}|\le1}\,dx
=\operatorname{Tr}(K^m),\qquad x_{m+1}=x_1.
\]
Although the kernel is nonnegative, \(K\) itself need not have nonnegative eigenvalues; this formula uses signed powers of the real eigenvalues. Powers \(K^m\) with \(m\ge2\) are trace-class.

**2. Entire nonzero spectrum.** Reflection \(x\mapsto-x\) commutes with \(K\), so every nonzero eigenspace decomposes into even and odd functions. For an eigenpair \(Kf=\lambda f\), \(\lambda\ne0\), differentiation for \(0<x<1\) gives \(\lambda f'(x)=-f(x-1)\) and, after a second differentiation, \(f''(x)+\lambda^{-2}f(x)=0\). Write \(\alpha=1/\lambda\).

For even \(f\), the eigenvalue equation at \(x=0,1\) gives \(f(0)=2f(1)\), while the differentiated equation gives \(f'(0)=-\alpha f(1)\) and \(f'(1)=-\alpha f(0)\). Up to scale, on \([0,1]\),
\[
f(x)=\cos(\alpha x)-\tfrac12\sin(\alpha x).
\]
The two boundary equations at \(x=1\) require
\[
\cos\alpha-\tfrac12\sin\alpha=\tfrac12,
\qquad \sin\alpha+\tfrac12\cos\alpha=1.
\]
Their unique trigonometric solution is \(\cos\alpha=4/5\), \(\sin\alpha=3/5\). Thus \(\alpha=\theta+2\pi k\), \(k\in\mathbb Z\). These functions, extended evenly, directly satisfy the integral eigenvalue equation, including its value at \(x=1\).

For odd \(f\), \(f(0)=0\) and \(\lambda f'(x)=f(1-x)\) on \([0,1]\). Thus \(f(x)\) is a multiple of \(\sin(\alpha x)\); evaluating at \(x=0\) gives \(\sin\alpha=1\), so \(\alpha=\pi/2+2\pi k\), \(k\in\mathbb Z\). These odd functions also satisfy the entire integral equation. Since the compact self-adjoint spectral theorem accounts for all nonzero eigenvalues, the displayed two sequences exhaust the nonzero spectrum, with one-dimensional eigenspaces. Taking \(\operatorname{Tr}(K^m)\) proves the volume series. Both sums converge absolutely for \(m\ge2\).

**3. Closed generating function.** For \(a\notin2\pi\mathbb Z\) and \(|z|\) below the distance from \(a\) to that lattice, classical symmetric cotangent partial fractions (or differentiation of the uniformly convergent squared-reciprocal series) give
\[
\sum_{k\in\mathbb Z}\frac1{(a+2\pi k)(a+2\pi k-z)}
=\frac{\cot((a-z)/2)-\cot(a/2)}{2z}.
\]
The left side equals \(\sum_{m\ge2} z^{m-2}\sum_k(a+2\pi k)^{-m}\). Since \(\cot(\theta/2)=3\), \(\cot(\pi/4)=1\), the subtraction identity for cotangent transforms this into the two terms \(5\tan(z/2)/(z(1-3\tan(z/2)))\) and \(\tan(z/2)/(z(1-\tan(z/2)))\). Their sum is the generating function.

**4. Mahler product and exponential law.** Theorem 4.24 of D'Alì–Delucchi–Michałek gives the normalized primal wheel volume
\[
A_m=(1+\sqrt3)^m+(1-\sqrt3)^m-2\mathbf1_{2\mid m}.
\]
The anchored coordinate lattice is unimodular, so \(\operatorname{vol}_m(P_m)=A_m/m!\). The polar volume is \(W_m\) in the corresponding dual coordinates, giving the product exactly. The spectral term \(\lambda_0=1/\theta\) has strictly greater absolute value than every other eigenvalue, since \(0<\theta<\pi/2\); the squared-summability of the remaining eigenvalues implies \(W_m=\theta^{-m}(1+O(c^m))\) for some \(0<c<1\). Likewise \(A_m=(1+\sqrt3)^m(1+O(c'^m))\) for some \(0<c'<1\). Hence the claimed asymptotic. Finally, \(\theta=\arctan(3/4)<3/4\) and \(1+\sqrt3>3\), proving the exponential base strictly exceeds one.

## Verification
The standalone file `verify.py` evaluates the generating-function coefficients symbolically and, independently, counts lattice points in integer dilates of \(Q_m\) using exact transfer matrices. Because the defining constraint matrix is a directed graph incidence matrix (totally unimodular) with integral right-hand side, \(Q_m\) is integral. Its Ehrhart polynomial has degree \(m\) and leading coefficient \(W_m\). Exact \(m\)-th forward differences of integer counts therefore recover \(m!W_m\). This checks the spectral coefficients independently for \(3\le m\le8\), as well as the primal-volume combination and strict normalized gain for those cases. It does not constitute an infinite-dimensional computational proof; the spectral argument above proves the all-\(m\) theorem.

## Relationship to prior work
The exact primal wheel volume and its parity correction are **known** from D'Alì, Delucchi, Michałek, *Many faces of symmetric edge polytopes*, Theorem 4.24. Alexander, Fradelizi, García-Lirola, Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, develops the general finite-metric volume-product framework and evaluates the equilateral case, not the wheel polar volumes. D'Alì, Juhnke-Kubitzke, Koch, *On a generalization of symmetric edge polytopes to regular matroids*, Proposition 5.1, provides a general lattice-point/cut correspondence for polar polytopes, but does not evaluate these wheel volumes or the spectral/Mahler asymptotics. In a different but related metric family, dual volumes for squared paths arise from an **open-chain** matrix element of the same transfer operator; the wheel requires a **closed-chain trace**, which has a distinct spectrum-level answer.

## Limitations
These are exact mathematical results for unit-edge wheel metrics, not for arbitrary weighted wheels or general graphs. They concern volume in dual molecular coordinates and an affine-invariant product, not Euclidean-radius or ellipsoid estimates. Independent scientific validation has not been performed. An equivalent evaluation under different transfer-operator or lattice-point terminology could exist in literature not identified by the source comparisons.

## References
1. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first public 2019-10-11), especially Section 4.3 and Theorem 4.24. https://arxiv.org/abs/1910.05193
2. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (2019), especially Sections 2 and 5. https://arxiv.org/abs/1911.10642
3. A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933 (2023), especially Section 5 and Proposition 5.1. https://arxiv.org/abs/2307.04933
