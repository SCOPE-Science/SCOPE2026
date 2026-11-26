# Sharp all-timestep fourth-order Gauss positivity cutoff on homogeneous paths

## Finding

Let \(P_n\), \(n\ge2\), be a finite undirected simple path with common edge conductance \(c>0\), with vertices \(0,\ldots,n-1\) in path order. Let \(L\) be its combinatorial weighted Laplacian. The completed two-stage Gauss–Legendre end-step for graph heat flow, equivalently fourth-order \([2/2]\) Padé, is
\[
M(h)=(12I+6hL+h^2L^2)^{-1}(12I-6hL+h^2L^2),\qquad h\ge0.
\]
It is entrywise nonnegative for every finite \(h\ge0\) **if and only if** \(2\le n\le3\); in these orders all entries are strictly positive for \(h>0\). For every \(n\ge4\), the entry between an endpoint and its immediate neighbor is negative for all sufficiently large steps, with the exact leading term
\[
 M(h)_{0,1}=-\frac{2(n-1)(2n-7)}{nch}+O_{n,c}(h^{-2}).
\]
In all orders \(M(h)\) remains symmetric, positive definite, and has row sums one for every finite step. Entrywise nonnegativity and positive definiteness therefore differ even for this homogeneous one-dimensional spatial discretization.

## Proof

Set \(Q(z)=z^2+6z+12\) and \(R(z)=(z^2-6z+12)/Q(z)\). The numerator is \((z-3)^2+3>0\), the denominator is positive on \([0,\infty)\), and \(1-R(z)=12z/Q(z)\). The symmetric positive semidefinite Laplacian has \(L\mathbf1=0\); spectral calculus gives \(M(h)=R(hL)\), eigenvalues in \((0,1]\), and \(M(h)\mathbf1=\mathbf1\). In particular all diagonal entries are positive, and \(M(0)=I\).

**Two and three vertices.** Write \(t=ch\). On two vertices the constant and alternating modes have Laplacian eigenvalues 0 and \(2c\), so the off-diagonal is \((1-R(2t))/2=12t/Q(2t)\). On three vertices the mutually orthogonal vectors \((1,1,1),(1,0,-1),(1,-2,1)\) have eigenvalues \(0,c,3c\). Projecting onto them gives the adjacent off-diagonal \((1-R(3t))/3=12t/Q(3t)\), and the entry between the endpoints is
\[
 \frac13-\frac{R(t)}2+\frac{R(3t)}6=6t\left(\frac{1}{Q(t)}-\frac{1}{Q(3t)}\right).
\]
Both entries are positive for \(t>0\) because \(Q\) increases on \([0,\infty)\).

**Four or more vertices.** For every fixed positive Laplacian eigenvalue \(\lambda\), \(R(h\lambda)=1-12/(h\lambda)+O_\lambda(h^{-2})\). On the zero eigenspace it is identically 1. Thus for the Moore–Penrose inverse \(L^\dagger\),
\[
 M(h)=I-12L^\dagger/h+O_{n,c}(h^{-2}).
\]
The remainder is entrywise for fixed \(n,c\), since the spectrum is finite. To compute its leading coefficient at \((0,1)\), put \(u=L^\dagger e_0\), so \(Lu=e_0-\mathbf1/n\) and \(\sum_j u_j=0\). Summing the first \(i+1\) equations telescopes the conductance differences and gives
\[
 c(u_i-u_{i+1})=(n-1-i)/n,\qquad 0\le i\le n-2.
\]
Each difference \(u_i-u_{i+1}\) occurs \(n-1-i\) times in \(\sum_j(u_0-u_j)=nu_0\). Therefore \(u_0=\sum_{k=1}^{n-1}k^2/(n^2c)=(n-1)(2n-1)/(6nc)\). Subtracting \(u_0-u_1=(n-1)/(nc)\) gives
\[
 (L^\dagger)_{0,1}=u_1=\frac{(n-1)(2n-7)}{6nc}.
\]
For \(n\ge4\) this is strictly positive. The off-diagonal expansion now gives the stated negative sign at all sufficiently large steps and completes the cutoff proof.

## Reproducibility, scope, and prior work

The standard-library `verify.py` solves finite exact rational systems for selected orders and steps and checks the asserted coefficient at \((0,1)\) by a constrained Laplacian solve. The test range is finite and does not establish any of the universal quantifiers; those are proved above. The theorem concerns homogeneous conductances, exact arithmetic, and the completed time step, not positivity of intermediate stages. It does not determine the full set of finite admissible steps above the size cutoff.

The small positive orders are covered by the earlier complete multipartite criterion ([Resultary, 2026-10-13, 690509e7de2b](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-an-exact-positivity-criterion-on-complete-multipartite-diffusion--690509e7de2b/RESULT.md)), and an earlier complete multipartite study reports an exact finite-step threshold on \(P_4\) ([2026-10-25, 3b12f25d4b2d](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-unconditional-fourth-order-gauss-pad-positivity-on-complete-mult--3b12f25d4b2d/RESULT.md)). The contribution here is the all-orders path classification and explicit endpoint-neighbor tail. The cycle cutoff, kernel, and tail are already given in [2026-10-13, 98f4ce42b84c](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-six-cycle-threshold-and-all-size-positivity-dichotomy-for-fourth--98f4ce42b84c/RESULT.md) and are not claimed here. A later [2026-11-08 record, 73910250a06c](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-unconditional-fourth-order-gauss-positivity-on-weighted-paths-a--73910250a06c/RESULT.md) also covers equal weights within an arbitrary-positive-conductance path classification.

Earlier general Padé positivity and counterexample work includes Zappavigna, Colaneri, Kirkland and Shorten, [*On the Preservation of Co-positive Lyapunov Functions under Padé Discretization for Positive Systems*](https://mural.maynoothuniversity.ie/id/eprint/2195/) (2010) and [*Essentially Negative News About Positive Systems*](https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf) (2012). Their general sufficient conditions for Hurwitz-stable Metzler generators do not supply an all-step classification for conservative path Laplacians. These comparisons do not establish historical priority.
