# A spectral volume law and exponential Mahler growth for wheel Lipschitz-free spaces

## Finding
For every integer \(m\ge3\), let \(M_m\) be the vertex set of the unit-edge wheel graph \(K_1*C_m\), with its shortest-path metric and hub \(o\). Let \(P_m\) be the unit ball of the real Lipschitz-free space \(\mathcal F(M_m)\) in hub-anchored molecular coordinates, and let \(Q_m=P_m^\circ\). Put \(\theta=\arctan(3/4)\) and \(W_m=\operatorname{vol}_m(Q_m)\). The polar volume in every such dimension is the absolutely convergent sum
\[
W_m=\sum_{k\in\mathbb Z}\left(\frac1{(\theta+2\pi k)^m}+\frac1{(\pi/2+2\pi k)^m}\right).
\]
For \(|z|<\theta\),
\[
\sum_{m=2}^\infty W_m z^{m-2}=\frac{\tan(z/2)}{z}\left(\frac5{1-3\tan(z/2)}+\frac1{1-\tan(z/2)}\right),
\]
where \(W_2=3\) is a formal trace-square coefficient, not the volume of a wheel with a two-vertex rim. The initial actual volumes \(W_3,W_4,W_5,W_6\) are \(4,6,55/6,283/20\).

Using the previously known primal wheel-volume formula of D'Alì–Delucchi–Michałek, the affine-invariant Mahler product is
\[
\operatorname{vol}_m(P_m)\operatorname{vol}_m(Q_m)
=\frac{\bigl((1+\sqrt3)^m+(1-\sqrt3)^m-2\mathbf1_{2\mid m}\bigr)W_m}{m!}.
\]
Consequently, if \(R_m\) is this product divided by the Hanner value \(4^m/m!\), then
\[
R_m\sim\left(\frac{1+\sqrt3}{4\arctan(3/4)}\right)^m,
\qquad \lim_{m\to\infty}R_m^{1/m}=\frac{1+\sqrt3}{4\arctan(3/4)}>1.
\]
The exponential base is approximately \(1.0614009712788661\). The exact dual volumes, their generating function and the resulting asymptotic are the contributions here; the primal volumes are from prior work.

## Assumptions and scope
All volumes use ordinary Lebesgue measure in the dual pair of hub-anchored coordinates. The primal is the convex hull of the molecules \(\pm e_i\) for hub edges and \(\pm(e_i-e_{i+1})\) for rim edges (cyclic indices). Indeed, for vertices at distance two the normalized difference is an average of two edge molecules along a shortest path. Hence
\[
Q_m=\{x\in[-1,1]^m: |x_i-x_{i+1}|\le1\ (i\bmod m)\}.
\]
The wheel has \(m+1\) vertices and \(\dim\mathcal F(M_m)=m\). The formal coefficient at \(m=2\) is used only in the generating function.

## Proof
**1. Transfer trace.** Let \(K\) be the compact self-adjoint Hilbert–Schmidt operator on \(L^2([-1,1])\) with kernel \(k(x,y)=\mathbf1_{|x-y|\le1}\). The product of the two Hilbert–Schmidt operators \(K\) and \(K^{m-1}\) has trace given by integrating the product of their kernels with reversed variables in the second factor. Iterating the kernel composition and applying Fubini gives, for \(m\ge2\),
\[
\operatorname{Tr}(K^m)=\int_{[-1,1]^m}\prod_{j=1}^m k(x_j,x_{j+1})\,dx,\qquad x_{m+1}=x_1.
\]
This is \(W_m\) for \(m\ge3\). For \(m=2\) the integral is the area of the square \([-1,1]^2\) minus the two triangles where \(|x_1-x_2|>1\), namely \(3\). A nonnegative kernel does not force nonnegative eigenvalues; the trace uses signed powers.

**2. Nonzero spectrum.** Reflection commutes with \(K\), so it suffices to consider even and odd eigenfunctions. A nonzero eigenvalue \(\lambda\) has a continuous eigenfunction representative by its integral equation. Write \(\beta=1/\lambda\). For \(0<x<1\) that equation gives \(\lambda f'(x)=-f(x-1)\); differentiating again using the reflected branch on \((-1,0)\) gives \(f''(x)+\beta^2 f(x)=0\).

In the even case, evaluating at \(0\) and \(1\) gives \(f(0)=2f(1)\). Taking one-sided limits in the derivative equation gives \(f'(0+)=-\beta f(1)\), \(f'(1-)=-\beta f(0)\). Up to scale, \(f(x)=\cos(\beta x)-\tfrac12\sin(\beta x)\) on \([0,1]\). Thus
\[
\cos\beta-\tfrac12\sin\beta=\tfrac12,\qquad
\sin\beta+\tfrac12\cos\beta=1,
\]
so \(\cos\beta=4/5,\ \sin\beta=3/5\), or \(\beta=\theta+2\pi k\). Conversely these values give \(\lambda f'=-f(x-1)\) for the even extension by the angle-subtraction formulas. At \(x=1\), the integral \(\int_0^1 f(y)\,dy=[\sin\beta+(\cos\beta-1)/2]/\beta=1/(2\beta)=\lambda f(1)\). Thus the derivative identity integrates to the eigenvalue equation on \([0,1]\), and evenness extends it to \([-1,1]\).

In the odd case \(f(0)=0\) and \(\lambda f'(x)=f(1-x)\). Up to scale \(f(x)=\sin(\beta x)\) on \([0,1]\). Taking \(x\downarrow0\) gives \(\sin\beta=1\), or \(\beta=\pi/2+2\pi k\). The converse follows from \(\sin(\beta(1-x))=\cos(\beta x)\) and \(\int_0^1 f(y)\,dy=(1-\cos\beta)/\beta=1/\beta=\lambda f(1)\). The two disjoint sequences exhaust the nonzero spectrum and each eigenvalue is simple. The trace of \(K^m\) is the absolutely convergent sum of the corresponding powers for \(m\ge2\), giving the volume formula.

**3. Generating function.** For each \(a\in\{\theta,\pi/2\}\), expand the following normally convergent sum for \(|z|<\theta\):
\[
\sum_{k\in\mathbb Z}\frac1{(a+2\pi k)(a+2\pi k-z)}
=\frac{\cot((a-z)/2)-\cot(a/2)}{2z}.
\]
The equality follows by subtracting the symmetric cotangent partial fractions, and holds by continuity at \(z=0\). Expanding each summand gives \(\sum_{m\ge2}z^{m-2}\sum_k(a+2\pi k)^{-m}\). Substituting \(\cot(\theta/2)=3\) and \(\cot(\pi/4)=1\) and using the cotangent subtraction identity gives the stated generating function. Its first four actual coefficients give the listed volumes.

**4. Mahler product and exponential law.** Theorem 4.24 of D'Alì–Delucchi–Michałek gives the normalized primal wheel volume
\[
A_m=(1+\sqrt3)^m+(1-\sqrt3)^m-2\mathbf1_{2\mid m}.
\]
The anchored coordinate lattice is unimodular, so \(\operatorname{vol}_m(P_m)=A_m/m!\). The polar volume is \(W_m\) in the corresponding dual coordinates, giving the product exactly. The eigenvalue \(\lambda_0=1/\theta\) has strictly greatest absolute value, since \(0<\theta<\pi/2\). The rest are square summable and uniformly bounded in modulus by \(c\lambda_0\) for some \(c<1\); bounding all but two factors in each power by this bound yields \(W_m=\theta^{-m}(1+O(c^m))\). Likewise \(A_m=(1+\sqrt3)^m(1+O(c'^m))\) for some \(c'<1\). This gives the asserted asymptotic and root limit.

To see that the base is strictly greater than one, integrate \(1/(1+s^2)=1-s^2+s^4-s^6/(1+s^2)\) from \(0\) to \(3/4\). It gives \(\theta<3363/5120\). Hence \(4\theta<3363/1280<8/3<1+\sqrt3\), where the last inequality follows from \(3>25/9\).

## Verification
The accompanying `verify.py` evaluates the generating-function coefficients symbolically and compares them with exact Ehrhart volumes in dimensions \(3\) through \(8\). In the latter method, the graph incidence matrix with the hub column deleted, with both edge orientations, is totally unimodular. The right-hand side is integral, so the constraint system gives an integral polytope; the lattice-point count at dilation \(j\) is a polynomial in \(j\) with leading coefficient \(W_m\). Lattice points at dilations \(0\) through \(m\) can be counted by integer transfer matrices; the \(m\)-th forward difference divided by \(m!\) gives \(W_m\). These are finite checks. The spectrum and trace proof establish the all-dimension result.

## Relationship to prior work
The exact primal wheel volume and its parity correction are known from D'Alì, Delucchi and Michałek, *Many faces of symmetric edge polytopes*, Theorem 4.24. Alexander, Fradelizi, García-Lirola and Zvavitch develop the general finite-metric volume-product framework and evaluate the equilateral case. D'Alì, Juhnke-Kubitzke and Koch, Proposition 5.1, provide a general lattice-point/cut correspondence for the polar polytopes. Neither result supplies the closed wheel-polar volume formula above. In the related squared-path family, the same operator yields an open-chain matrix element, rather than the closed-chain trace in the wheel calculation.

## Limitations
These formulas use unit-edge wheel metrics, not arbitrary weighted wheels or general graphs. They concern volume in dual molecular coordinates and an affine-invariant product, not Euclidean-radius or ellipsoid estimates. An equivalent evaluation under other transfer-operator or lattice-point terminology could exist.

## References
1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, Section 4.3 and Theorem 4.24. https://arxiv.org/abs/1910.05193
2. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, Sections 2 and 5. https://arxiv.org/abs/1911.10642
3. A. D'Alì, M. Juhnke-Kubitzke and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933, Section 5 and Proposition 5.1. https://arxiv.org/abs/2307.04933
