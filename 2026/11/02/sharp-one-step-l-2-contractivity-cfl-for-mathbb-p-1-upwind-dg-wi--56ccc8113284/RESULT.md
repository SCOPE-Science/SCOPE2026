# Sharp one-step \(L^2\) contractivity CFL for \(\mathbb P^1\) upwind DG with SSPRK3

## Finding

For the standard, unmodified degree-one upwind discontinuous Galerkin discretization of one-dimensional constant-speed transport on a uniform periodic mesh, followed by the classical three-stage third-order strong-stability-preserving Runge–Kutta method, **every step is nonexpansive in the exact physical \(L^2\) norm for every periodic grid and every initial datum if and only if**
\[
  0\le \nu\le \nu_\star,\qquad
  18\nu_\star^4-9\nu_\star^3+3\nu_\star^2+5\nu_\star-1=0,
  \qquad \nu_\star=0.186457280370046\ldots.
\]
The indicated quartic has exactly one positive real zero. At every larger positive Courant number there exists a periodic grid and real initial data for which one time step strictly increases the \(L^2\) norm. The initial failure arises from arbitrarily small nonzero Fourier angles immediately above the threshold; it is not an alternating-grid-mode obstruction.

## Assumptions and scope

Let \(u_t+a u_x=0\) with constant \(a>0\) on a one-dimensional periodic interval partitioned into \(N\ge1\) equal cells of width \(h\). Represent each element's polynomial in the reference coordinate \(\xi\in[-1,1]\) as \(u_j(\xi)=m_j+b_j\xi\). Use exact spatial integration, upwind numerical flux at interfaces, and no filtering, limiting, or modification of the stage operators. The physical squared norm is
\[
 \|u\|_{L^2}^2=h\sum_{j=0}^{N-1}\left(m_j^2+\frac13 b_j^2\right).
\]
The time discretization is SSPRK(3,3), whose stability polynomial on any linear autonomous system is \(r(w)=1+w+w^2/2+w^3/6\). Write \(\nu=a\Delta t/h\). Nonexpansiveness means \(\|u^{n+1}\|_{L^2}\le\|u^n\|_{L^2}\) for all real initial states on every periodic uniform grid, including the constant mode. It is not a claim of cellwise entropy decay or nonexpansiveness for every fixed mesh at every larger Courant number.

## Proof

**1. Exact Fourier symbol.** The weak element equations with upwind flux, on the Fourier ansatz \((m_j,b_j)=z^{-j}(m,b)\), \(|z|=1\), give the dimensionless semidiscrete symbol
\[
 L(z)=\begin{pmatrix}z-1&z-1\\3(1-z)&-3(1+z)\end{pmatrix}.
\]
The Fourier energy weight is \(W=\operatorname{diag}(1,1/3)\). Set
\[
 R_\nu(z)=I+\nu L(z)+\tfrac12\nu^2L(z)^2+\tfrac16\nu^3L(z)^3,
 \qquad D_\nu(z)=W-R_\nu(z)^*WR_\nu(z).
\]
Discrete Parseval reduces the assertion, uniformly over periodic grid sizes, to positive semidefiniteness of \(D_\nu(z)\) for all \(|z|=1\). Conversely, a strictly negative quadratic form at any Fourier angle persists at nearby roots of unity and yields real unstable data (take a real or imaginary part of a growing Fourier state).

**2. Exact two-by-two energy certificates.** Write \(c=\cos\theta\), \(z=e^{i\theta}\) and \(t=1-c\in[0,2]\). Direct polynomial multiplication gives
\[
 (D_\nu)_{11}=2\nu t\,Q(\nu,t),\qquad
 \det D_\nu=-\frac49\nu^4t^2F(\nu,c),
\]
where
\[
\begin{aligned}
9Q(s,t)={}&9-54s+18st+216s^2-162s^2t+24s^2t^2\\
&-567s^3+510s^3t-96s^3t^2+972s^4-702s^4t+120s^4t^2\\
&-972s^5+540s^5t-64s^5t^2,
\end{aligned}
\]
and
\[
\begin{aligned}
F(s,c)&=\frac{1+c}{2}F_+(s)+\frac{1-c}{2}F_-(s),\\
F_+(s)&=3(6s^2-3s+1)(18s^4-9s^3+3s^2+5s-1),\\
F_-(s)&=-(12s^3-6s^2-s-1)(36s^5-18s^4-3s^3+s^2+3s-3).
\end{aligned}
\]
These are polynomial identities rather than approximations. `VERIFY.py` checks them by exact rational interpolation with proven degree bounds.

**3. Certified positivity below the threshold.** On \(0\le s\le1/5\), \(0\le t\le2\), put \(u=5s\), \(v=t/2\). Express \(Q(s,t)\) in the tensor Bernstein basis of bidegree \((5,2)\) on \([0,1]^2\). Its eighteen coefficients, indexed by increasing first-coordinate degree, are exactly

| First index | Second index 0 | Second index 1 | Second index 2 |
|---|---:|---:|---:|
| 0 | \(1\) | \(1\) | \(1\) |
| 1 | \(19/25\) | \(21/25\) | \(23/25\) |
| 2 | \(77/125\) | \(88/125\) | \(313/375\) |
| 3 | \(647/1250\) | \(2201/3750\) | \(2813/3750\) |
| 4 | \(1403/3125\) | \(37/75\) | \(2107/3125\) |
| 5 | \(1232/3125\) | \(3956/9375\) | \(17192/28125\) |

Since all Bernstein basis functions are nonnegative and sum to one, \(Q(s,t)\ge1232/3125>0\) throughout the box.

Let \(p(s)=18s^4-9s^3+3s^2+5s-1\). Its derivative is \(p'(s)=5+s(72s^2-27s+6)>0\) for \(s\ge0\), since the quadratic in parentheses is strictly positive. Thus \(p\) has exactly one positive zero, and \(0<\nu_\star<1/5\). Moreover \(6s^2-3s+1>0\), so \(F_+(s)\le0\) for \(0\le s\le\nu_\star\).

For \(0<s\le1/5\), the two factors \(12s^3-6s^2-s-1\) and \(36s^5-18s^4-3s^3+s^2+3s-3\) are both negative: respectively they are bounded above by \(12/125-1<0\) and \(36/3125+1/25+3/5-3<0\). Consequently \(F_-(s)<0\). Because \(F\) is a convex combination of \(F_+\) and \(F_-\), \(F(s,c)\le0\) for all \(c\in[-1,1]\) and \(0<s\le\nu_\star\). The two identities give \((D_\nu)_{11}>0\) and \(\det D_\nu\ge0\) for every nonzero Fourier angle, hence the Hermitian \(2\times2\) matrix \(D_\nu\) is positive semidefinite.

At the zero angle \(z=1\), the matrix \(R_\nu(1)=\operatorname{diag}(1,r(-6\nu))\). For \(0<\nu\le1/5\), \(r(-6\nu)=1-6\nu+18\nu^2-36\nu^3\) decreases strictly from \(1\) to \(29/125>0\), because its derivative is \(-6(1-6\nu+18\nu^2)<0\); hence this mode is also nonexpansive. At \(\nu=0\) the step is the identity. This establishes the entire closed interval.

**4. Sharpness.** For \(s>\nu_\star\), \(F_+(s)>0\). By continuity, \(F(s,\cos\theta)>0\) for all sufficiently small nonzero \(\theta\). The determinant is then negative, so \(D_s(e^{i\theta})\) has a negative eigenvalue; the one-step map increases energy along its eigenvector. Arbitrarily large periodic grids contain an angle in this open interval. Fourier conjugate pairing (or taking real/imaginary parts) supplies a real initial state with strict energy growth. More precisely, at the low-frequency end,
\[
 \det D_s(e^{i\theta})=-\frac{s^4}{9}F_+(s)\,\theta^4+O_s(\theta^6),
\]
which quantifies the long-wave onset. This proves the if-and-only-if statement, including the endpoint.

## Verification

The standalone standard-library Python file `VERIFY.py` constructs the exact rational Runge–Kutta symbol, checks both energy identities at a mathematically sufficient tensor set of 169 rational interpolation nodes, obtains all eighteen Bernstein coefficients by exact basis transformation, verifies their positivity and the quartic-root bracket, and checks supporting sign inequalities. It reports `VERIFY_OK 562 threshold_interval=(0.186457,0.186458) min_Bernstein 1232/3125`. The interpolation proof uses degree at most twelve in the Courant variable and Laurent degree at most six in the Fourier variable; thirteen distinct exact nodes in each suffice for an identity. Running `python VERIFY.py` requires no third-party packages. Numerical simulations alone are not used to infer uniform stability.

## Relationship to prior work

Liu, Jiang and Zhang (2026) analyze compact high-order explicit DG schemes and fully discrete entropy stability. Their paper includes a nonlinear Burgers counterexample showing that third-order SSP time integration does not guarantee contraction of a selected nonlinear entropy for arbitrarily small Courant numbers. It does not establish the exact uniform quadratic-energy threshold above for the unmodified linear-advection \(\mathbb P^1\) spatial symbol. Sun and Shu (2019) prove general strong-stability results and obstructions for explicit Runge–Kutta discretizations of seminegative operators, but not this exact spatially specialized algebraic boundary. Zhang and Shu (2010) analyze third-order RKDG \(L^2\) stability under a sufficiently small generic CFL restriction; an equivalent sharp specialized constant could exist in material beyond the available abstract and remains a priority risk. Wei and Shu (2025) analyze fully discrete *cellwise* entropy inequalities for a distinct family of third-order explicit Runge–Kutta methods, rather than this global norm calculation.

## Limitations

The exact constant is for linear constant-speed advection, a uniform periodic mesh, degree-one polynomials, exact integration, standard SSPRK(3,3), and the unmodified upwind DG generator. It need not apply to nonuniform meshes, higher polynomial degree, other fluxes or time integrators, or nonlinear convex entropies. The theorem does not assert spectral instability or global solution blowup at every Courant number above its threshold; it asserts failure of the **one-step prefactor-one physical \(L^2\) nonexpansion guarantee** on a sufficiently large periodic grid. The proof is analytical and has not undergone independent external audit; historical priority in older specialized RKDG analyses remains to be resolved.

## References

1. Liu, Jiang and Zhang, *High-Order Fully Discrete Entropy-Stable DG Methods with Compact Explicit Single-Step Time Discretizations* (first public 2026-10-21), https://arxiv.org/abs/2610.30535.
2. Sun and Shu, *Strong Stability of Explicit Runge–Kutta Time Discretizations*, https://arxiv.org/abs/1811.10680.
3. Zhang and Shu, *Stability Analysis and A Priori Error Estimates of the Third Order Explicit Runge–Kutta Discontinuous Galerkin Method for Scalar Conservation Laws*, SIAM Journal on Numerical Analysis (2010), https://doi.org/10.1137/090771363.
4. Wei and Shu, *Fully-discrete cell entropy inequality of third-order explicit Runge–Kutta discontinuous Galerkin method for nonlinear conservation laws* (2025), https://bpb-us-w2.wpmucdn.com/sites.brown.edu/dist/0/348/files/2025/09/Fully-discrete-cell-entropy-inequality-of-third-order.pdf.
