# Antiperiodic Brownian geometry of the odd-cycle integrality cap

## Finding
Let \(n\ge5\) be odd. For the cycle with cyclic indices, define the fractional stable-set polytope
\[
F_n=\{x\in\mathbb R^n:x_i\ge0,\ x_i+x_{i+1}\le1\text{ for all }i\},
\]
and the integral stable-set polytope \(S_n=\operatorname{conv}\{\mathbf1_I:I\text{ is a stable set}\}\). Let \(X_n\) be uniformly distributed by \(n\)-dimensional Euclidean volume on \(F_n\), conditional on \(X_n\notin S_n\). Write \(h_n=\tfrac12\mathbf1\), \(Q_n=\|X_n-h_n\|_2^2\), and let \(E_{2k}\) denote the Euler secant numbers, defined by \(\sec t=\sum_{k\ge0}|E_{2k}|t^{2k}/(2k)!\).

**Exact cap and probability.** The set \(F_n\setminus S_n\) is, up to a null boundary, the open simplex with vertices \(h_n\) and the \(n\) incidence vectors of maximum stable sets of the cycle. Its volume is \(1/(2n!)\); therefore
\[
\Pr\{X\notin S_n\mid X\sim\mathrm{Unif}(F_n)\}
 =\frac{1}{n|E_{n-1}|}
 \sim\frac{(\pi/2)^n}{2n!}.
\]

**Conditional shape.** As \(n\to\infty\) through odd integers,
\[
Q_n\ \Longrightarrow\ Q=\int_0^1\left(B(t)-\frac12B(1)\right)^2\,dt,
\]
where \(B\) is standard Brownian motion. The limit has the explicit spectral and Laplace descriptions
\[
Q\ \overset{d}=\sum_{j=0}^{\infty}\frac{Z_{j,1}^2+Z_{j,2}^2}{\pi^2(2j+1)^2},
\qquad \mathbb E e^{-sQ}=\operatorname{sech}\!\sqrt{s/2}\quad(s\ge0),
\]
for independent standard normal variables \(Z_{j,a}\). In particular, \(\mathbb EQ=1/4\), \(\operatorname{Var}(Q)=1/24\), and at finite odd dimension
\[
\mathbb E Q_n=\frac{n}{4(n+2)}.
\]
The event of violating integrality has superfactorially small relative volume, but its volume-uniform conditional Euclidean radius about the fractional vertex remains nondegenerate at scale one.

## Assumptions and scope
All volumes are ordinary coordinate Euclidean volumes in \(\mathbb R^n\). The statements hold for *every odd* \(n\ge5\), with the limit along the odd sequence. The description of \(S_n\) by adding the unique odd-cycle inequality \(\sum_i x_i\le(n-1)/2\) to the edge/nonnegativity relaxation is classical (see References). The conditional variable \(X_n\) is *not* sampled uniformly from the integral polytope and is *not* a random direction. Boundaries have zero \(n\)-volume, so strict or non-strict definitions of the cap give the same probability law.

## Proof
**1. A precise simplex for the missing volume.** Set \(y_i=1-x_i-x_{i+1}\). With \(A=I+P\), where \(P\) is the cyclic coordinate shift, \(y=\mathbf1-Ax\). Since \(n\) is odd, \(\det A=2\), and
\[
\sum_i x_i=\frac{n-\sum_i y_i}{2}.
\]
Thus the violated odd-cycle inequality is equivalent to \(y_i\ge0\) and \(\sum_i y_i<1\). This whole simplex maps into \(F_n\): its \(n+1\) vertices map respectively to \(h_n\) when \(y=0\), and to the distinct maximum-stable-set incidence vectors when \(y=e_j\). In particular, all inverse images are nonnegative, so no missing facet cuts the simplex. The Jacobian is \(1/2\), proving \(\operatorname{vol}(F_n\setminus S_n)=1/(2n!)\).

**2. Exact ambient fractional volume.** Define the integral operator \((Tf)(u)=\int_0^{1-u} f(v)\,dv\) on \(L^2[0,1]\). Iterating its kernel around the cycle gives \(\operatorname{vol}(F_n)=\operatorname{tr}(T^n)\) for \(n\ge3\). Its eigenvectors \(\cos((j+\tfrac12)\pi u)\), \(j\ge0\), have eigenvalues \(2(-1)^j/((2j+1)\pi)\); completeness follows from the regular separated Sturm–Liouville problem with a derivative-zero boundary at \(0\) and a value-zero boundary at \(1\). The trace-class power therefore gives, for odd \(n\),
\[
\operatorname{vol}(F_n)=\left(\frac2\pi\right)^n\sum_{j\ge0}\frac{(-1)^j}{(2j+1)^n}
 =\frac{|E_{n-1}|}{2(n-1)!}.
\]
The last equality is the standard odd-integer Dirichlet beta/secant-number identity. As the beta sum tends to one, division by the cap volume establishes the exact and asymptotic probability claims.

**3. Dirichlet coordinates and a functional limit.** Conditional on the cap, \(y\) is uniform on \(\{y_i\ge0,\sum y_i\le1\}\). Hence \(y_i=H_i/T_n\) with \(H_1,\ldots,H_{n+1}\) independent \(\mathrm{Exp}(1)\) variables and \(T_n=\sum_{j=1}^{n+1}H_j\). Put \(w_i=X_{n,i}-1/2\), and \(v_i=(-1)^i w_i\) for \(1\le i\le n\). The edge equations give
\[
v_{i+1}-v_i=(-1)^i y_i,\qquad v_{n+1}=-v_1,
\qquad
v_i=\frac{1}{T_n}\left(\sum_{j<i}(-1)^j H_j-\frac12\sum_{j=1}^n(-1)^jH_j\right).
\]
The alternating deterministic means of the partial sums are uniformly bounded; the centered independent terms \((-1)^j(H_j-1)\) satisfy the functional triangular-array invariance principle with unit variance and uniform exponential tails. Since \(T_n/n\to1\) in probability, their continuous piecewise-linear interpolation shows
\[
\sqrt n\,v_{\lfloor nt\rfloor+1}\Longrightarrow B(t)-B(1)/2
\]
in the Skorokhod topology (with the endpoint interpreted using \(v_{n+1}\)). The limit is continuous. A Riemann-sum application of the continuous mapping theorem then yields \(Q_n=\sum_{i=1}^n v_i^2\Longrightarrow Q\). No claim of an almost-sure coupling is needed.

**4. Spectral law and exact moment.** The limit process has covariance \(K(s,t)=1/4-|s-t|/2\). Its covariance operator is the inverse of \(-d^2/dt^2\) with antiperiodic boundary conditions \(f(1)=-f(0)\), \(f'(1)=-f'(0)\). Its eigenvalues are \(1/[\pi^2(2j+1)^2]\), each twice, from the sine and cosine frequencies \((2j+1)\pi\). Gaussian orthogonal expansion gives the spectral series; the canonical hyperbolic-cosine product gives \(\mathbb E e^{-sQ}=1/\cosh(\sqrt{s/2})\). The first two cumulants, or the eigenvalue sums, yield \(\mathbb EQ=1/4\) and \(\operatorname{Var}(Q)=1/24\).

For the finite mean, the linear map \(v=By\) has every matrix entry of absolute value \(1/2\), and \(B\mathbf1\) has every coordinate of absolute value \(1/2\). Thus \(\operatorname{tr}(BB^T)=n^2/4\) and \(\|B\mathbf1\|^2=n/4\). The uniform \(n\)-simplex moments satisfy \(\mathbb E(yy^T)=(I+\mathbf1\mathbf1^T)/[(n+1)(n+2)]\), giving \(\mathbb E\|By\|^2=n/[4(n+2)]\).

## Verification
Run `python3 odd_cycle_verification.py` with NumPy installed. That standalone diagnostic verifies the determinant, all transformed simplex vertices and cyclic inverse constraints in dimensions \(5,7,11,19\), checks the Euler secant numbers \(5,61,1385\), and samples Dirichlet caps in dimensions \(5,9,31,101,501\). The computed means approach the exactly proved finite means and the measured Laplace transform approaches \(\operatorname{sech}(1/\sqrt2)\). Finite simulation is *not* used as a proof of the functional limit, volume identity or infinite spectral product; those follow analytically above.

## Relationship to prior work
Kafer, Pashkovich and Sanità study the same graph fractional stable-set relaxation and its circuit structure, rather than its missing-volume Euclidean distribution. Bärmann and Schneider give a complete odd-cycle convex-hull characterization, supplying the odd-cycle inequality but not its relative volume or limiting cap shape. Hamano, Hibi and Ohsugi study fractional-stable-set Ehrhart series and algebraic invariants, not this conditional Euclidean-volume probability law. Published treatments of the minimum sphere and John ellipsoid of the *same odd-cycle fractional polytopes* concern radius extremizers and ellipsoid shape, not uniform conditional cap points. Brownian functional invariance principles, Dirichlet simplexes, and the hyperbolic-cosine product are classical tools and are not separately claimed as new.

## Limitations
The distribution concerns only the nonintegral cap and not the typical (unconditional) uniform point of \(F_n\), not random widths, and not other graph families. The Laplace transform is for the limiting *squared radius*, not the radius itself; it does not furnish finite-dimensional density formulas. Bibliographic searches do not prove uniqueness: terminology from order polytopes, alternating permutations or Brownian quadratic functionals might conceal an equivalent statement. Independent mathematical validation is not yet performed.

## References
1. S. Kafer, K. Pashkovich, L. Sanità, *On the Circuit Diameter of some Combinatorial Polytopes*, arXiv:1709.09642v1, first publicly posted 2017-09-27, Section 5, https://arxiv.org/html/1709.09642v1 ; SIAM J. Discrete Math. 33 (2019), 1–25, https://doi.org/10.1137/17M1152115. Primary MSC 52B05.
2. A. Bärmann and O. Schneider, *Set characterizations and convex extensions for geometric convex-hull proofs*, arXiv:2101.09267, 2021-01-22, Section 3.3 Theorem 5; Math. Program. 195 (2022), 475–515, https://doi.org/10.1007/s10107-021-01705-3.
3. G. Hamano, T. Hibi and H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613, https://arxiv.org/abs/1603.09613.
4. Published geometric comparisons: *Cycle fractional stable-set polytopes have a parity-split minimum sphere* and *An exact John ellipsoid and sharp exponential law for odd-cycle fractional stable-set polytopes*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11 .
