# Finite-horizon reachability design on weighted stars: the quadratic departure from Laguerre allocation

## Finding
Fix an integer \(m\ge2\) and a conductance budget \(B>0\). Let \(z_1<\cdots<z_m\) be the positive zeros of the ordinary generalized Laguerre polynomial \(L_m^{(1)}\), and put \(n=m+1\) and
\[
w_i^0=\frac{Bz_i}{m(m+1)},\qquad
\delta_i=\frac{3B}{2m(4n^2-1)}\,w_i^0\left(w_i^0-\frac{2B}{n}\right).
\]
There exists \(T_0=T_0(m,B)>0\) such that, for each \(0<T<T_0\), the **global** maximizers of the finite-time hub-actuated controllability-Gramian determinant on a weighted \(m\)-leaf star are exactly the \(m!\) permutations of a single strictly increasing, positive weight vector \(w(T)\). It satisfies
\[
\boxed{\quad w_i(T)=w_i^0+\delta_i T^2+O_{m,B}(T^3),\qquad i=1,\ldots,m.\quad}
\]
The first-order design drift vanishes, but the displayed second-order vector is nonzero for \(m\ge2\). In particular, at two leaves and unit budget, the increasing weights are
\[
\boxed{\quad w_1(T)=\frac{3-\sqrt3}{6}-\frac{\sqrt3}{840}T^2+O(T^3),\qquad
w_2(T)=\frac{3+\sqrt3}{6}+\frac{\sqrt3}{840}T^2+O(T^3).\quad}
\]
This theorem describes the continuous-time, **positive finite** horizon. The exact Laguerre optimizer of the shortest-horizon discrete-time reachability problem is a distinct, previously determined fact; the explicit nonzero continuous-time displacement is the assertion here.

## Assumptions and scope
The star has one hub indexed \(0\) and leaves \(1,\ldots,m\), with undirected spoke conductances \(w_i\ge0\) and \(\sum_i w_i=B\). Its weighted combinatorial Laplacian is \(L(w)\). For scalar hub input \(e_0u(t)\), dynamics are \(\dot x=-L(w)x+e_0u(t)\), and the finite-horizon reachability Gramian is
\[
W_T(w)=\int_0^T e^{-tL(w)}e_0e_0^{\mathsf T}e^{-tL(w)}\,dt.
\]
The optimization is over the **entire** closed conductance simplex; no distinctness assumption, preassigned leaf ordering or equal weights is imposed on competitors. Objective is \(\det W_T(w)\), proportional to the squared volume of the unit-input-energy reachable ellipsoid. Bounds and expansions are for fixed \(m,B\) as \(T\downarrow0\). Existence of \(T_0\) is proved, but no explicit largest \(T_0\) or all-horizon classification is asserted.

## Proof
**1. Exact star factorization.** Write \(A=-L(w)\), \(K=[e_0,Ae_0,\ldots,A^me_0]\), and \(b=e_0\). The leaf components of \(A^kb\), for \(k\ge1\), have the form \(w_iP_{k-1}(w_i)\). Indeed the leaf recursion is \(v_{k+1}(i)=w_i h_k-w_iv_k(i)\), where \(h_k\) is the hub component; therefore \(P_{k-1}\) has degree \(k-1\) and leading coefficient \((-1)^{k-1}\). Expanding \(\det K\) along its first column gives the Vandermonde identity
\[
(\det K)^2=\prod_{i=1}^m w_i^2\prod_{1\le i<j\le m}(w_j-w_i)^2.\tag{1}
\]
It follows that the pair \((A,b)\) is controllable exactly for positive pairwise distinct weights.

Let \(C(w)\) be the companion matrix of the characteristic polynomial of \(A\), chosen so that \(AK=KC\) and \(b=Ke_1\). The Cayley–Hamilton identity gives these equalities even when \(K\) is singular. Consequently
\[
W_T=K\,H_T(C)\,K^{\mathsf T},\qquad
H_T(C)=\int_0^T e^{tC}e_1e_1^{\mathsf T}e^{tC^{\mathsf T}}dt.\tag{2}
\]
The \(j\)-th component of \(e^{tC}e_1\) begins with \(t^{j-1}/(j-1)!\). Factoring \(T^{j-1}\) out of row and column \(j\), and \(T\) out of the integral, proves that \(T^{-n^2}\det H_T(C)\) extends jointly real-analytically in \(T\) and the coefficients of \(C\), **including coincident and zero weights**. Its value at \(T=0\) is the positive scaled-Hilbert determinant
\[
h_n=\det\left[\frac1{(i-1)!(j-1)!(i+j-1)}\right]_{i,j=1}^n>0.\tag{3}
\]
Thus \(\det W_T=T^{n^2}h_n(\det K)^2F_n(T,w)\), where \(F_n\) is positive, jointly analytic on a neighborhood of the compact budget simplex and \(F_n(0,w)=1\). This uniform factorization controls competitors approaching uncontrollable boundaries.

**2. Universal quadratic Gramian coefficient.** For every cyclic real symmetric matrix \(A\) in dimension \(n\ge2\) and cyclic vector \(b\), direct determinant expansion gives
\[
\log\!\left(\frac{\det W_T(A,b)}{h_nT^{n^2}(\det K)^2}\right)
=T\operatorname{tr}A+\frac{nT^2}{2(4n^2-1)}\operatorname{tr}(A^2)+O(T^3).\tag{4}
\]
Here \(W_T(A,b)=\int_0^T e^{tA}bb^{\mathsf T}e^{tA^{\mathsf T}}dt\). For completeness, diagonalize \(A\) with eigenvalues \(\lambda_1,\ldots,\lambda_n\) and nonzero input coordinates. By the Gram determinant integration identity, its determinant is proportional to the integral of \(\det[e^{T\lambda_i u_j}]^2\) on \([0,1]^n\). Let \(s_1\), \(s_2\), \(s_{11}\) denote the Schur polynomials for partitions \((1),(2),(1,1)\). The elementary exponential alternant expansion through degree two is
\[
\frac{\det[e^{T\lambda_i u_j}]}{T^{n(n-1)/2}\Delta(\lambda)\Delta(u)/\prod_{k=0}^{n-1}k!}
=1+\frac{T}{n}s_1(\lambda)s_1(u)
+T^2\left[\frac{s_2(\lambda)s_2(u)}{n(n+1)}+\frac{s_{11}(\lambda)s_{11}(u)}{n(n-1)}\right]+O(T^3).\tag{5}
\]
Normalize the measure proportional to \(\Delta(u)^2\,du\) on \([0,1]^n\) to probability. Its three moments needed in (5) are
\[
\mathbb E\sum u_j=\frac n2,\quad
\mathbb E\left(\sum u_j\right)^2=\frac{n^2}{4}+\frac{n^2}{4(4n^2-1)},\quad
\mathbb E\sum u_j^2=\frac{n(3n^2-1)}{2(4n^2-1)}.\tag{6}
\]
For a direct derivation of (6), use the orthonormal shifted Legendre polynomials for the unit weight on \([0,1]\). Multiplication by \(u\) has diagonal \(1/2\) and off-diagonal \(a_j=j/(2\sqrt{4j^2-1})\). The rank-\(n\) Christoffel–Darboux projection then gives \(\mathbb E\sum u_j=n/2\), variance \(a_n^2\), and \(\mathbb E\sum u_j^2=\sum_{j=0}^{n-1}(1/4+a_j^2+a_{j+1}^2)\); the last sum telescopes to (6). Inserting \(s_2=(s_1^2+\sum u_i^2)/2\) and \(s_{11}=(s_1^2-\sum u_i^2)/2\) into the square of (5), and subtracting half the square of the linear coefficient when taking the logarithm, cancels \((\operatorname{tr}A)^2\) and gives precisely (4). A polynomial-continuation argument covers repeated eigenvalues when the normalized determinant is expressed by the companion representation (2). All remainders, including their first two weight derivatives near the positive distinct optimum, are uniform because of joint analyticity.

For the star, \(\operatorname{tr}A=-2B\) and \(\operatorname{tr}(A^2)=B^2+3\sum_iw_i^2\). Equation (4) therefore becomes
\[
\log F_n(T,w)=-2BT+\frac{n(B^2+3\sum_iw_i^2)}{2(4n^2-1)}T^2+O_{m,B}(T^3).\tag{7}
\]

**3. Optimality and explicit drift.** In the ordered chamber \(0<w_1<\cdots<w_m\), set
\[
\Phi(w)=\sum_i\log w_i+\sum_{i<j}\log(w_j-w_i).
\]
Its Hessian \(H\) is strictly negative definite. Under the budget constraint \(\sum_iw_i=B\), its unique maximum satisfies
\[
\frac1{w_i}+\sum_{j\ne i}\frac1{w_i-w_j}=\lambda,
\qquad\lambda=\frac{m(m+1)}{2B}.\tag{8}
\]
The Laguerre differential equation \(z p''+(2-z)p'+mp=0\), evaluated at zeros of \(L_m^{(1)}\), yields (8) for \(w=w^0\); strict concavity makes this the unique leading optimum. The standard Laguerre coefficient identities give
\[
\sum_iw_i^0=B,\qquad \sum_i(w_i^0)^2=\frac{2B^2}{n}.\tag{9}
\]
At that point elementary differentiation of (8) gives the two vector identities
\[
H w^0=-\lambda\mathbf1,\qquad
H((w^0)^2)=m\mathbf1-2\lambda w^0.\tag{10}
\]
Componentwise square is understood in the second identity. The analytic implicit-function theorem on the budget hyperplane, applied to \(2\Phi+\log F_n\), gives a smooth local maximizer of the form \(w^0+T^2\delta+O(T^3)\) with no linear term, since the first-order contribution in (7) is weight-independent. The \(T^2\) stationarity equation is
\[
2H\delta+\frac{3n}{4n^2-1}w^0=\mu\mathbf1,\qquad \sum_i\delta_i=0.\tag{11}
\]
Equations (9)–(10) solve (11) uniquely and yield the displayed formula for \(\delta\). It is nonzero because the distinct positive coordinates of \(w^0\) cannot all equal \(2B/n\).

Finally, the compact simplex factorization (1)–(3) implies uniform convergence of \(T^{-n^2}\det W_T\) to \(h_n(\det K)^2\); any global maximizer for small \(T\) lies near a permutation of \(w^0\), not at a collision or zero-conductance boundary. The Hessian of \(\log F_n(T,\cdot)\) is uniformly bounded and tends to zero, whereas the Hessian of \(2\Phi\) is uniformly negative definite in the chamber. Consequently each ordered chamber has exactly one global maximizer for all sufficiently small \(T\), and leaf-permutation symmetry supplies all and only the stated optimizers.

## Verification
The accompanying independent standard-library script `verify.py` uses exact rational arithmetic, expands the Gramian determinants for eight diagonal systems of dimensions two through four to the \(T^{n^2+2}\) coefficient, checks the three predicted coefficients against (4), and reconstructs full star Kalman matrices for fifteen weighted instances with up to five leaves to verify (1). Execution produced `VERIFY_OK 39 exact coefficient/determinant identities across 23 finite test instances`. These computations test finite instances only. The infinite-family statements and uniformity are supplied by the preceding analytic argument, not by the enumeration.

## Relationship to prior work
The star Vandermonde controllability determinant and ordinary Laguerre equilibrium are established background; neither is a new claim here. Lou and Hong (2012) explicitly obtain a star Vandermonde controllability factor. The 2014 Laguerre electrostatic study discusses the classical fixed-mean equilibrium. An earlier finite-step discrete-time star design record gives an **exact Laguerre optimizer** for the shortest full-rank discrete reachability horizon; that discrete determinant factors without a time-dependent correction, so it neither implies nor has the present \(T^2\) continuous-time optimizer drift. Becker et al. (2019) study edge-weight design for Gramian constraints by optimization relaxations, not this explicit short-time star D-optimum. Trélat and Zuazua (2026) give a general determinant term through order \(T\) and a remainder of order \(T^2\), but do not identify the universal quadratic trace term or its induced star-design displacement. The contribution here is the explicit positive-horizon drift and the global uniqueness statement, not the leading formula or generic first-order trace correction.

## Limitations
No claim is made about medium/large horizons, arbitrary tree topologies, asymmetric dynamics, heterogeneous edge prices, or higher-order expansion. The oldest motivating archival controllability source is from 2012; later supporting work is used only to delimit what is already known. The universal quadratic coefficient is derived here using classical determinant and polynomial-ensemble identities; it is not claimed that its ingredients are individually novel. Equivalent design-expansion formulations may exist in incompletely indexed literature. No independent mathematical audit is asserted.

## References
1. Y. Lou and Y. Hong, *Controllability analysis of multi-agent systems with directed and weighted interconnection*, International Journal of Control 85 (2012), 1486–1496, doi:10.1080/00207179.2012.690162. Accessible author full text: https://www.researchgate.net/publication/239787831_Controllability_analysis_of_multi-agent_systems_with_directed_and_weighted_interconnection .
2. L. A. Molano Molano, *An electrostatic model for zeros of classical Laguerre polynomials perturbed by a rational factor*, Mathematical Sciences 8 (2014), doi:10.1007/s40096-014-0120-y. https://link.springer.com/article/10.1007/s40096-014-0120-y .
3. C. O. Becker, S. Pequito, G. J. Pappas and V. M. Preciado, *Network Design for Controllability Metrics* (2019), arXiv:1902.04195. https://arxiv.org/pdf/1902.04195 .
4. E. Trélat and E. Zuazua, *Two-term small-time spectral expansions for controllability Gramians* (2026), arXiv:2609.37077, especially Corollary 2. https://arxiv.org/pdf/2609.37077 .
5. F. Marcellán, A. Martínez-Finkelshtein and P. Martínez-González, *Electrostatic models for zeros of polynomials: old, new, and some open problems* (2005), arXiv:math/0512293. https://arxiv.org/abs/math/0512293 .
