# Sharp smoothness staircase and gradient susceptibility of a cat-driven Möbius response

## Finding
Consider the cat-driven Möbius map of Chigarev, Kazakov and Pikovsky in the zero-drift, zero-phase regime. Its attracting graph has a well-defined first-order response to forcing. The response has **exact and sharp Sobolev and integer differentiability thresholds**, a Fibonacci Fourier spectrum and an explicit diverging gradient susceptibility.

Write \(\lambda=(3+\sqrt5)/2\), \(r=(1-\varepsilon)/(1+\varepsilon)\), and \(\varepsilon_m=(\lambda^m-1)/(\lambda^m+1)\). For every \(\varepsilon\in(0,1)\), every real \(s\ge0\), and every integer \(m\ge0\),
\[
h_\varepsilon\in H^s(\mathbb T^2)\ \Longleftrightarrow\ r\lambda^s<1,
\qquad
h_\varepsilon\in C^m(\mathbb T^2)\ \Longleftrightarrow\ \varepsilon>\varepsilon_m.
\]
The endpoint is excluded. In particular, \(h_\varepsilon\) is continuously differentiable exactly when \(\varepsilon>1/\sqrt5\), and in that range
\[
\|\partial_s h_\varepsilon\|_\infty
=\frac{2\pi}{1-3r+r^2}
=\frac{2\pi(1+\varepsilon)^2}{5\varepsilon^2-1}.
\]
This exact susceptibility diverges as \(\varepsilon\downarrow1/\sqrt5\).

## Assumptions and scope
Take \(u=(t,s)\in\mathbb T^2=\mathbb R^2/\mathbb Z^2\), the cat automorphism \(A(u)=(2t+s,t+s)\bmod1\), and \(0<\varepsilon<1\). The circle skew map is
\[
 (u,x)\longmapsto
 \bigl(Au,\ M_\varepsilon(x)+\mu\sin(2\pi t)\bmod1\bigr),
\qquad
 M_\varepsilon(x)=x-\frac1\pi\arctan\frac{\varepsilon\sin(2\pi x)}{1+\varepsilon\cos(2\pi x)}.
\]
The arctangent is its principal continuous branch; its denominator is everywhere positive. The forcing amplitude \(\mu\) is real and sufficiently close to zero, with the permitted neighborhood possibly dependent on \(\varepsilon\). The attracting graph \(X_\mu:\mathbb T^2\to\mathbb R\) is the unique **small continuous lift** satisfying \(X_\mu(Au)=M_\varepsilon(X_\mu(u))+\mu\sin(2\pi t)\). Define the response by the uniform derivative \(h_\varepsilon=\left.\partial_\mu X_\mu\right|_{\mu=0}\in C^0(\mathbb T^2)\).

The Sobolev space \(H^s\) uses the standard periodic Fourier norm \(\sum_{k\in\mathbb Z^2}(1+4\pi^2|k|^2)^s|\widehat h(k)|^2\). \(C^m\) means continuous partial derivatives through order \(m\), including integer endpoints.

## Proof
**1. Local graph and response.** Direct differentiation of the Möbius map at the fixed point gives \(M_\varepsilon(0)=0\) and \(M'_\varepsilon(0)=r\in(0,1)\). Choose a small interval around zero on which \(|M'_\varepsilon|\le\kappa<1\). For sufficiently small \(|\mu|\), the graph transform
\[
(\mathcal T_\mu g)(u)=M_\varepsilon(g(A^{-1}u))+\mu\sin(2\pi[A^{-1}u]_1)
\]
is a contraction of a closed sup-norm ball into itself. It has a unique fixed point \(X_\mu\), with \(X_0=0\). Its parameter derivative exists in the uniform norm by the contraction fixed-point equation (or the Banach-space implicit-function theorem). Differentiating yields
\[
h_\varepsilon(Au)=r h_\varepsilon(u)+\sin(2\pi t).
\]

**2. Exact Fourier frequencies.** Iterating the response equation backwards gives the uniformly convergent series
\[
 h_\varepsilon(u)=\sum_{n=1}^{\infty}r^{n-1}\sin(2\pi\langle v_n,u\rangle),
 \quad v_n=A^{-Tn}(1,0)^T=(F_{2n-1},-F_{2n})^T,
\]
where \(F_0=0,F_1=1\) are Fibonacci numbers. The identity follows from \(A^{-T}=\begin{psmallmatrix}1&-1\\-1&2\end{psmallmatrix}\) and the Fibonacci recurrence. Distinct \(v_n\) are neither equal nor opposite. The eigenvalues of \(A\) are \(\lambda\) and \(\lambda^{-1}\); hence there exist constants \(0<c<C<\infty\), independent of \(n\), with \(c\lambda^n\le |v_n|\le C\lambda^n\).

**3. Sharp regularity, including the boundary.** Since each \(\pm v_n\) carries Fourier coefficient of modulus \(r^{n-1}/2\), Parseval yields
\[
\|h_\varepsilon\|_{H^s}^2
=\frac12\sum_{n\ge1}r^{2n-2}(1+4\pi^2|v_n|^2)^s.
\]
For \(s\ge0\), this converges exactly when \(r\lambda^s<1\), and diverges at equality. For an integer \(m\ge0\) satisfying \(r\lambda^m<1\), termwise differentiation up to order \(m\) is uniformly absolutely convergent, giving \(C^m\). Conversely, if \(h_\varepsilon\in C^m\) with \(m\ge1\), the Riemann–Lebesgue lemma applied to \(\partial_t^m h_\varepsilon\) requires its Fourier coefficients at \(v_n\) to tend to zero. Their absolute values are
\[
\frac{(2\pi F_{2n-1})^m r^{n-1}}2,
\]
which **do not tend to zero** when \(r\lambda^m\ge1\), including equality. For \(m=0\), the graph response is continuous and \(r<1\), consistent with the criterion. Solving \(r\lambda^m<1\) for \(\varepsilon\) gives the stated \(\varepsilon_m\). The identity \((\lambda-1)/(\lambda+1)=1/\sqrt5\) gives the first derivative threshold.

**4. Exact sharp gradient.** In the differentiable region \(r\lambda<1\), the derivative series converges uniformly and
\[
\partial_s h_\varepsilon(u)
=-2\pi\sum_{n\ge1}r^{n-1}F_{2n}\cos(2\pi\langle v_n,u\rangle).
\]
Every term has the same sign at \(u=0\); the triangle inequality is therefore attained there. By the even-Fibonacci generating function,
\[
\sum_{n\ge1}F_{2n}r^{n-1}=\frac1{1-3r+r^2},
\]
which proves the exact sup norm. Substitution of \(r=(1-\varepsilon)/(1+\varepsilon)\) gives the positive denominator \((5\varepsilon^2-1)/(1+\varepsilon)^2\) and its critical divergence.

## Verification
A standalone script, `verify_response.py`, checks the integer cat-map inverse, every displayed Fibonacci wavevector identity for the first nineteen modes, the exact generating-function and threshold identities, noncollision of the first thirty-five Fourier frequencies, and finite Fourier-covariance sums. It also numerically compares first-order response with the full nonlinear graph transform at three parameters and small forcing; observed discrepancies are below \(2.2\times10^{-13}\) for the given test states. The analytical contraction, Fourier and Riemann–Lebesgue arguments — not finite sampling — establish the infinite-range statements.

## Relationship to prior work
Chigarev, Kazakov and Pikovsky introduced the precise cat-driven Möbius map and noted that invariant attractor and repeller graphs are expected to be smooth for stronger Möbius contraction and rough for weaker contraction; their studied transition and heterodimensional dynamics do not state this exact first-order response threshold or norm. Hadjiloucas, Nicol and Walkden developed general invariant-graph regularity/rigidity results over hyperbolic systems; the present argument uses the classical lacunary Fourier mechanism but specializes it to yield a sharp **model-specific** response threshold and gradient coefficient. Generalized synchronization theory also offers qualitative smoothness bounds; those general ideas are not claimed as new. This theorem is not a classification of identity resonances or periodic fibers.

## Limitations
The sharp \(C^m\) and \(H^s\) thresholds are for **the derivative at zero forcing**, not a universal regularity classification of every nonzero-forcing invariant graph. The result does not classify global attractor collision, heterodimensional orbits or nonsmall forcing. General regularity theory could imply parts of the qualitative threshold; independently equivalent computations in unindexed literature have not been excluded. No independent mathematical audit has been performed.

## References
1. V. Chigarev, A. Kazakov and A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1 (first posted 2023-05-29), subsequently *Chaos* 33, 063113 (2023), doi:10.1063/5.0144672. Defining map and its invariant-graph motivation.
2. D. Hadjiloucas, M. J. Nicol and C. P. Walkden, *Regularity of invariant graphs over hyperbolic systems*, *Ergodic Theory and Dynamical Systems* 22 (2002), 469–482, doi:10.1017/S0143385702000226. General structural context.
3. B. R. Hunt, E. Ott and J. A. Yorke, *Differentiable generalized synchronization of chaos*, *Physical Review E* 55 (1997), 4029–4034, doi:10.1103/PhysRevE.55.4029. General synchronization smoothness context; only abstract available in the present literature comparison.
