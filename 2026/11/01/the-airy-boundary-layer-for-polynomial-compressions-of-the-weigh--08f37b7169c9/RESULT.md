# The Airy boundary layer for polynomial compressions of the weighted Bergman shift

## Finding

For every fixed \(\alpha>-1\), put \(p=\alpha+1>0\). Let \(\mathcal P_N\) consist of the polynomials of degree at most \(N\) in the normalized analytic weighted Bergman space \(A^2_\alpha(\mathbb D)\). Write \(S_N\) for the orthogonal compression of multiplication by \(z\) to \(\mathcal P_N\), and \(r_N=w(S_N)\) for its numerical radius. If \(a_1=2.338107410459767\ldots\) is the smallest positive number satisfying \(\operatorname{Ai}(-a_1)=0\), then

\[
\boxed{r_N=1-\frac{p}{2N}-\frac{a_1p^{2/3}}{2N^{4/3}}+o_p(N^{-4/3})}\qquad(N\to\infty).
\]

There is also a universal limit for the normalized maximizing polynomial. Express its positive Perron coefficient vector in the normalized monomial basis as \((u^{(N)}_0,\ldots,u^{(N)}_N)\), with \(\sum|u^{(N)}_n|^2=1\). Put \(h_N=N^{-2/3}\), and define the step function

\[
\Phi_N(x)=h_N^{-1/2}u^{(N)}_{N-\lfloor x/h_N\rfloor}
\]

for \(0\le x<(N+1)h_N\), extended by zero elsewhere. Then \(\Phi_N\to\Phi_p\) strongly in \(L^2(0,\infty)\), where

\[
\boxed{\Phi_p(x)=\frac{p^{1/6}}{|\operatorname{Ai}'(-a_1)|}\operatorname{Ai}(p^{1/3}x-a_1),\quad x\ge0.}
\]

The numerical range of \(S_N\) is the closed disk centered at zero with radius \(r_N\). This exact finite-dimensional circularity is the reason the largest Jacobi eigenvalue gives the numerical radius, not just a lower bound.

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The weighted measure is \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha dA(z)/\pi\), with \(dA\) ordinary planar Lebesgue area. All asymptotics are for \(N\to\infty\) with **one fixed** \(\alpha>-1\). No uniformity as \(\alpha\downarrow-1\) is claimed. The scalar \(w(T)=\sup_{\|f\|=1}|\langle Tf,f\rangle|\) is the numerical radius, not spectral radius or operator norm.

Normalized monomials are
\[
e_n(z)=\sqrt{\frac{\Gamma(n+\alpha+2)}{n!\,\Gamma(\alpha+2)}}z^n,\qquad
S_Ne_n=\sqrt{\frac{n+1}{n+p+1}}e_{n+1}\quad(0\le n<N),\qquad S_Ne_N=0.
\]

For the Hardy limiting case \(p=0\), outside the theorem, all weights are one and the *different* exact behavior is \(r_N=\cos(\pi/(N+2))=1-\pi^2/(2N^2)+O(N^{-3})\). This comparison explains the singular change of scale at the boundary of the weighted Bergman family.

## Proof

**1. Monomial reduction and numerical-radius identity.** The beta integral gives
\[
\|z^n\|^2=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)},\qquad
b_n:=\sqrt{\frac{n+1}{n+p+1}}>0.
\]
Thus \(S_N\) is the nilpotent shift with weights \(b_n\). Rotation of the monomial basis unitarily intertwines \(S_N\) with every unimodular multiple of itself. Convexity of its numerical range makes that range a centered closed disk. Its radius is the maximum of \(\operatorname{Re}\langle S_N f,f\rangle\), hence the largest eigenvalue of the symmetric tridiagonal matrix
\[
J_N=\frac12(S_N+S_N^*),\qquad (J_N)_{n,n+1}=b_n/2,\quad 0\le n<N.
\]
Since all edge weights are positive, its top eigenvalue is simple and a top eigenvector can be chosen strictly positive (Perron–Frobenius, after adding the identity).

**2. Exact nonnegative edge-energy decomposition.** Set \(b_{-1}=b_N=0\), \(V_{N,n}=1-(b_{n-1}+b_n)/2\), and \(\mu_N=1-b_{N-1}\). For every vector \(u=(u_0,\ldots,u_N)\), direct expansion and summation of the mixed terms give
\[
\begin{aligned}
\langle (I-J_N)u,u\rangle-\mu_N\|u\|^2
={}&\frac12\sum_{n=0}^{N-1}b_n|u_{n+1}-u_n|^2\\
&+\sum_{n=0}^N(V_{N,n}-\mu_N)|u_n|^2.
\end{aligned}
\tag{1}
\]
The sequence \(b_n\) is strictly increasing. Consequently each term on the right is nonnegative; in particular the last-index boundary barrier is
\[
V_{N,N}-\mu_N=\frac{b_{N-1}}2,
\]
whereas, for \(1\le j\le N-1\), the interior term is
\[
V_{N,N-j}-\mu_N=b_{N-1}-\tfrac12(b_{N-j-1}+b_{N-j}).
\tag{2}
\]
At \(j=N\), the same expression holds with \(b_{-1}=0\). Extend \(b_n\) to \(b(t)=\sqrt{(t+1)/(t+p+1)}\) on \(t\ge0\). Its derivative
\[
b'(t)=\frac{p}{2\sqrt{t+1}(t+p+1)^{3/2}}
\]
is positive and bounded below on \([0,N]\) by \(c_pN^{-2}\) for all \(N\ge2\), for some \(c_p>0\). The boundary value \(V_{N,0}-\mu_N=b_{N-1}-b_0/2\) is bounded away from zero for all large \(N\). It follows, for a (possibly smaller) \(c_p>0\), that
\[
V_{N,N-j}-\mu_N\ge c_p\frac j{N^2},\qquad 1\le j\le N.
\tag{3}
\]
Moreover, for each fixed \(R>0\), uniformly for \(1\le j\le RN^{2/3}\), Taylor expansion about \(N\) gives
\[
N^{4/3}(V_{N,N-j}-\mu_N)=\frac p2 jN^{-2/3}+o_{p,R}(1).
\tag{4}
\]
The baseline has \(\mu_N=\frac p{2N}+O_p(N^{-2})\).

**3. Upper bound by smooth Airy trial functions.** Put \(h=N^{-2/3}\). For a real \(\varphi\in C_c^\infty((0,\infty))\) of unit \(L^2\) norm, define \(u_{N-j}=\sqrt h\,\varphi(jh)\) and normalize the discrete vector. Its support is away from both endpoints for sufficiently large \(N\). The right side of (1), multiplied by \(h^{-2}=N^{4/3}\), converges, by (4) and elementary Riemann-sum estimates, to
\[
\mathfrak q_p[\varphi]=\frac12\int_0^\infty\bigl(|\varphi'(x)|^2+p x|\varphi(x)|^2\bigr)\,dx.
\]
The Rayleigh principle therefore shows
\[
\limsup_{N\to\infty}N^{4/3}\bigl(1-r_N-\mu_N\bigr)
\le\inf_{\varphi\in C_c^\infty((0,\infty)),\,\|\varphi\|_2=1}\mathfrak q_p[\varphi].
\tag{5}
\]

**4. Lower bound, tightness and the Dirichlet boundary.** Choose the positive unit top eigenvector \(u^{(N)}\). By (5), its scaled energy in (1) is uniformly bounded. Coercivity (3) implies, for each \(R>0\),
\[
\sum_{j\ge RN^{2/3}}|u^{(N)}_{N-j}|^2\le\frac{C_p}{R},
\tag{6}
\]
so the mass is tight at the scale \(j\asymp N^{2/3}\). Also (1) implies \(u^{(N)}_N=O_p(h)\), hence \(h^{-1/2}u^{(N)}_N\to0\), which enforces a Dirichlet condition at the limiting origin.

Let \(a_j=h^{-1/2}u^{(N)}_{N-j}\) for \(0\le j\le N\). Linearly interpolate the values \(a_j\) on mesh \(jh\), then join \(a_N\) to zero over the next mesh cell and extend by zero. Since \(\min_n b_n=b_0>0\), the difference term in (1) gives a global bound \(\int|\varphi_N'|^2\le C_p\). The fixed positive last-physical-index barrier \(V_{N,0}-\mu_N\ge c_p\) controls the final interpolation cell. The interpolation differs in \(L^2\) norm by \(O_p(h)\) from the exact normalized step profile, and (6) gives uniform tightness. Therefore a subsequence converges weakly in \(H^1_{\mathrm{loc}}\) and strongly in \(L^2(0,\infty)\) to a unit vector \(\varphi\), with \(\varphi(0)=0\).

On any compact interval, \(b_{N-j}\to1\) uniformly, while the rescaled potential converges by (4). Weak lower semicontinuity on each compact interval and then monotone enlargement of the interval yield
\[
\liminf_{N\to\infty}N^{4/3}(1-r_N-\mu_N)\ge\mathfrak q_p[\varphi].
\tag{7}
\]
Taking the infimum over Dirichlet unit vectors of finite form energy matches (5) by the form-core property of \(C_c^\infty((0,\infty))\). This proves convergence of the rescaled smallest energy to the exact ground energy of \(\tfrac12(-\partial_x^2+p x)\) on the half-line with Dirichlet boundary.

**5. Exact Airy constant and eigenfunction.** The decaying solutions of \(-\varphi''+p x\varphi=2E\varphi\) are scalar multiples of \(\operatorname{Ai}(p^{1/3}x-2Ep^{-2/3})\). The first Dirichlet eigenvalue is \(E_p=\tfrac12a_1p^{2/3}\), with a simple, positive ground state. The classical identity \(\int_{-a_1}^\infty\operatorname{Ai}(y)^2dy=\operatorname{Ai}'(-a_1)^2\) fixes its normalized amplitude as stated. The variational limit and \(\mu_N=p/(2N)+O_p(N^{-2})\) yield the boxed numerical-radius expansion.

Every convergent subsequence of the positive discrete eigenvector profiles has the same positive normalized Airy ground-state limit; compactness from (6) and the derivative estimates then gives convergence of the full family. Equivalently, a near-optimal polynomial places its squared monomial mass within degree distance \(O(N^{2/3})\) of the top permitted degree, with the explicit Airy distribution.

## Verification

The standalone file `check.py` directly constructs the symmetric Jacobi finite sections and tests the exact weighted-moment ratios, the identity (1) at numerical Perron vectors, numerical eigenvalue scaling, positivity, the eigenvector Airy profile, and the exact Hardy-endpoint formula. Run it using `python check.py` after installing the packages in `requirements.txt`. The checks include multiple fixed weights and degrees through \(4096\), and pass **1922 finite assertions**. The checker does not establish limits; the proof above provides the infinite-dimensional compactness and lower-bound arguments.

## Relationship to prior work

Simanek's 2020 preprint and the subsequent Le–Simanek paper supply the weighted Bergman shift and block-Jacobi operator context, but their principal theorems are hyponormality criteria for infinite Toeplitz operators with added radial symbols. Gorkin and Partington (2019) calculate numerical radii of restricted shifts in Hardy model spaces associated with inner functions; finite Hardy shifts correspond to the distinct \(p=0\) regime. Lukic (2017) treats spectral-density and subordinate-solution behavior for infinite eventually monotone Jacobi matrices; its results do not directly give a moving finite-truncation top eigenvalue or the normalized eigenvector profile here. Sen and collaborators (2025) analyze numerical ranges of full weighted Bergman Toeplitz and composition operators, rather than degree-truncated shifts. Related Airy-edge asymptotics for geometrically damped periodic weighted shifts concern different coefficients and an infinite-operator parameter limit. These observations establish a precise technical distinction, not an absolute guarantee of historical novelty.

## Limitations

The result is an asymptotic for each fixed \(\alpha>-1\), not a uniform two-parameter theorem. There is no explicit error rate beyond the \(o_p(N^{-4/3})\) remainder, nor a characterization of all higher eigenvalues. The approximate Airy profile involves exact spectral data; noisy numerical computation is not a certified spectral enclosure. General Jacobi finite-section turning-point theorems might encompass this family and remain a historical-priority risk. An independent mathematical audit has not been performed.

## References

1. B. Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Space*, arXiv:2001.07823v1, first posted 2020-01-22. https://arxiv.org/abs/2001.07823
2. T. Le and B. Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2003.07330v1, first posted 2020-03-16. https://arxiv.org/abs/2003.07330
3. P. Gorkin and J. R. Partington, *Norms of Truncated Toeplitz Operators and Numerical Radii of Restricted Shifts*, Computational Methods and Function Theory 19 (2019), 487–508; accepted manuscript https://eprints.whiterose.ac.uk/id/eprint/146209/
4. M. Lukic, *Spectral edge behavior for eventually monotone Jacobi and Verblunsky coefficients*, arXiv:1705.09461v1, first posted 2017-05-26. https://arxiv.org/abs/1705.09461
5. A. Sen, S. Halder, R. Birbonshi and K. Paul, *Numerical range of Toeplitz and Composition operators on weighted Bergman spaces*, arXiv:2502.02833v1, first posted 2025-02-05. https://arxiv.org/abs/2502.02833
