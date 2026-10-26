# Sharp Lipschitz endpoint errors of Legendre and Chebyshev spectral projections

## Finding
Let \(L_n\) and \(C_n\) be the degree-at-most-\(n\) orthogonal projections on \([-1,1]\) for the uniform and first-kind Chebyshev weights, respectively, where \(n\ge0\). Define their sharp right-endpoint errors on real functions of Lipschitz constant at most one by
\[
\mathcal E_n^{L}=\sup_{\operatorname{Lip}(f)\le1}|f(1)-(L_nf)(1)|,\quad
\mathcal E_n^{C}=\sup_{\operatorname{Lip}(f)\le1}|f(1)-(C_nf)(1)|.
\]
With standard Legendre polynomials \(P_j(1)=1\), Jacobi polynomials \(P_n^{(0,1)}(1)=1\), and \(D_n(u)=1+2\sum_{k=1}^n\cos(ku)\), **both sharp constants for every degree** are
\[
\boxed{\mathcal E_n^{L}=\frac12\int_{-1}^{1}|P_n(t)+P_{n+1}(t)|\,dt
=\frac12\int_{-1}^{1}(1+t)|P_n^{(0,1)}(t)|\,dt},
\]
\[
\boxed{\mathcal E_n^{C}=\frac1\pi\int_0^\pi\sin u\left|(\pi-u)-2\sum_{k=1}^n\frac{\sin(ku)}k\right|\,du}.
\]
The sharp endpoint constants have **different decay exponents** and explicit optimal coefficients:
\[
\boxed{\lim_{n\to\infty}\sqrt n\,\mathcal E_n^L=\sqrt{\frac2\pi},\qquad
\lim_{n\to\infty}n\,\mathcal E_n^C=\frac8{\pi^2}.}
\]
For every degree, each finite sharp constant is attained by a piecewise smooth real Lipschitz function with derivative of magnitude one almost everywhere. The same constants hold at the left endpoint by reflection. In particular, the sharp endpoint error for Chebyshev projection is asymptotically of smaller order than that for Legendre projection, for an identical Lipschitz input class.

## Assumptions and scope
A function is real-valued and has Lipschitz constant at most one with respect to ordinary Euclidean distance on \([-1,1]\). Its values are unrestricted up to additive constants. The Legendre projection uses \(\int_{-1}^{1}fg\,dt\). The Chebyshev projection uses \(\int_{-1}^{1}fg\,(1-t^2)^{-1/2}\,dt\). Both include constants. No assumption of differentiability beyond the almost-everywhere derivative guaranteed by Lipschitz continuity is made. The statements concern evaluation at the two endpoints, **not** a sharp uniform-in-position error bound.

## Proof
**1. Exact Legendre kernel.** The endpoint reproducing kernel is
\[
K_n^L(1,t)=\frac12\sum_{k=0}^{n}(2k+1)P_k(t).
\]
Because \((2k+1)P_k=(P_{k+1}-P_{k-1})'\) for \(k\ge1\), telescoping and \(P_j(-1)=(-1)^j\) give, including \(n=0\),
\[
\int_{-1}^{s}K_n^L(1,t)\,dt=\frac{P_n(s)+P_{n+1}(s)}2.
\]
Writing \(f(t)=f(1)-\int_t^1f'(s)\,ds\) and applying Fubini shows
\[
f(1)-(L_nf)(1)=\frac12\int_{-1}^{1}f'(s)[P_n(s)+P_{n+1}(s)]\,ds.
\]
The inequality \(|f'|\le1\) is sharp: choose \(f'(s)=\operatorname{sgn}(P_n(s)+P_{n+1}(s))\) almost everywhere. The classical contiguous identity \(P_n+P_{n+1}=(1+t)P_n^{(0,1)}\) yields the claimed Jacobi expression.

**2. Exact Chebyshev kernel.** On substituting \(t=\cos u\), Chebyshev projection at \(1\) becomes
\[
(C_nf)(1)=\frac1\pi\int_0^\pi D_n(u)f(\cos u)\,du.
\]
Since \(\int_0^\pi D_n(u)\,du=\pi\), expressing \(f(\cos u)-f(1)\) as an integral of \(-f'(\cos v)\sin v\) and swapping integrations gives
\[
f(1)-(C_nf)(1)=\int_0^\pi f'(\cos v)\sin v\,H_n(v)\,dv,
\quad H_n(v)=\frac1\pi\int_v^\pi D_n(u)\,du.
\]
Consequently
\[
H_n(v)=\frac{(\pi-v)-2\sum_{k=1}^n\sin(kv)/k}{\pi}.
\]
The sharp upper bound is attained by taking \(f'(\cos v)=\operatorname{sgn}H_n(v)\) almost everywhere. This measurable derivative defines a Lipschitz function by integration; the change of variable is legitimate at both endpoints.

**3. Legendre asymptotic and its constant.** Write \(t=\cos\theta\) in the Jacobi formula. The standard fixed-parameter Jacobi Darboux asymptotic on every compact subinterval of \((0,\pi)\) is
\[
P_n^{(0,1)}(\cos\theta)
=\frac{\cos((n+1)\theta-\pi/4)+o(1)}{\sqrt{\pi n}\,[\sin(\theta/2)]^{1/2}[\cos(\theta/2)]^{3/2}}.
\]
The standard global fixed-parameter Jacobi bound, for all \(n\ge1\) and \(0<\theta<\pi\), is \( |P_n^{(0,1)}(\cos\theta)|\le Cn^{-1/2}(\sin(\theta/2)+n^{-1})^{-1/2}(\cos(\theta/2)+n^{-1})^{-3/2}\). After multiplying by \(\sqrt n(1+\cos\theta)\sin\theta\), this is dominated by an integrable multiple of \([\sin(\theta/2)]^{1/2}[\cos(\theta/2)]^{3/2}\). Hence the two endpoint regions contribute arbitrarily little uniformly and one may pass to the averaged oscillatory limit \(|\cos((n+1)\theta-\pi/4)|\rightharpoonup2/\pi\) in the weighted integral. Therefore
\[
\lim_{n\to\infty}\sqrt n\,\mathcal E_n^L
=\frac4{\pi\sqrt\pi}\int_0^\pi[\sin(\theta/2)]^{1/2}[\cos(\theta/2)]^{3/2}\,d\theta.
\]
The integral is \(B(3/4,5/4)=\pi\sqrt2/4\), yielding \(\sqrt{2/\pi}\).

**4. Chebyshev asymptotic and its constant.** For \(0<u<\pi\), the classical sine-series identity gives
\[
A_n(u):=(\pi-u)-2\sum_{k=1}^{n}\frac{\sin(ku)}k
=2\sum_{k=n+1}^{\infty}\frac{\sin(ku)}k.
\]
Abel summation, twice applied to the coefficient sequence, yields uniformly for \(0<u\le\pi\)
\[
A_n(u)=\frac{\cos((n+1/2)u)}{(n+1)\sin(u/2)}
+O\!\left(\frac{1}{(n+1)^2\sin^2(u/2)}\right).
\]
The same Dirichlet estimate gives \(|A_n(u)|\le C\min\{1,((n+1)\sin(u/2))^{-1}\}\). Split the absolute-integral at \(u=n^{-1/2}\). The small interval contributes \(O(n^{-3/2})\) after the factor \(\sin u\); the integrated remainder over the other interval is \(O((\log n)/n^2)\). It follows that
\[
\mathcal E_n^C=\frac{2}{\pi(n+1)}\int_0^\pi\cos(u/2)|\cos((n+1/2)u)|\,du+o(n^{-1}).
\]
Oscillatory averaging gives \(\int_0^\pi\cos(u/2)|\cos((n+1/2)u)|\,du\to4/\pi\). Hence \(n\mathcal E_n^C\to8/\pi^2\). The integrals are sharp at every finite degree by the derivative-sign construction, so both limits describe **optimal**, not merely admissible, coefficients.

## Verification
The accompanying `verify.py` recomputes both finite-degree error integrals independently using classical polynomial routines and numerical quadrature; it also checks the convergence of their rescaled values toward \(\sqrt{2/\pi}\) and \(8/\pi^2\) at selected degrees. These finite computations are consistency checks only. The infinite-dimensional sharpness and asymptotic statements follow from the preceding exact kernel identities and analytic estimates, not from numerical extrapolation. For example, at degree \(2\) the Legendre value is exactly \(24\sqrt6/125\), obtained by integrating between the two zeros of \(P_2^{(0,1)}\).

## Relationship to prior work
The derivation uses classical Legendre/Jacobi polynomial identities and the Peano-kernel principle. Kuijlaars–McLaughlin–Van Assche–Vanlessen (arXiv:math/0111252) and Deaño–Huybrechs–Opsomer (arXiv:1502.07191) develop strong Jacobi asymptotics used here as background; their examined texts do not formulate the present pair of sharp Lipschitz endpoint projection errors. Wang (arXiv:2001.01985) studies rates of Legendre projection on analytic and bounded-variation derivative classes and states general Peano-kernel error representations, but does not evaluate the present Lipschitz-unit-ball endpoint norm or establish the Chebyshev/Legendre sharp-rate separation. The kernel-norm/transport-duality reduction is classical; the asserted contribution is the **joint exact all-degree norm identities, sharp extremizers, and evaluated asymptotic comparison**, not an invention of that general principle.

## Limitations
No sharp maximum over all spatial points is claimed. There is no assertion that one projection dominates the other at every finite degree. The comparison is asymptotic. Possible older, unindexed evaluations of these special kernel integrals remain an originality risk. The asymptotic proof invokes standard Jacobi endpoint estimates; the numerical script does not certify those classical analytic estimates.

## References
1. A. B. J. Kuijlaars, K. T.-R. McLaughlin, W. Van Assche, M. Vanlessen, *The Riemann–Hilbert approach to strong asymptotics for orthogonal polynomials on [-1,1]*, first public 2001-11-23, https://arxiv.org/abs/math/0111252.
2. A. Deaño, D. Huybrechs, P. Opsomer, *Construction and implementation of asymptotic expansions for Jacobi-type orthogonal polynomials*, first public 2015-02-25, https://arxiv.org/abs/1502.07191.
3. H. Wang, *How much faster does the best polynomial approximation converge than Legendre projection?*, https://arxiv.org/abs/2001.01985.
4. G. Szegő, *Orthogonal Polynomials*, fourth edition, AMS Colloquium Publications, 1975, Ch. VIII (classical Jacobi asymptotics).
