# Universal single-circle conditioning obstruction for weighted Bergman polynomial sampling

## Finding

Fix \(\alpha>-1\) and an integer \(N\ge2\). In the weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\) let \(\mathcal P_N\) denote the polynomials of degree at most \(N\). For a radius \(0<r<1\) and any nonzero finite positive Borel measure \(\nu\) on the circle, let
\[
 Q_{r,\nu}(p)=\int_0^{2\pi}|p(re^{i\theta})|^2\,d\nu(\theta).
\]
Write \(\mathscr K(r,\nu)\) for the ratio of its optimal upper and lower squared-norm bounds on \(\mathcal P_N\), with value \(+\infty\) if the lower bound vanishes. Set
\[
 w_k=\frac{(\alpha+2)_k}{k!},\qquad t_N=w_N^{-1/N},\qquad
 K_{\alpha,N}=\max_{0\le k\le N}w_k\,w_N^{-k/N}.
\]
Then the **global optimum over every radius and every positive angular sampling design**, including continuous angular observation and arbitrary numbers and weights of nodes, is
\[
 \boxed{\inf_{0<r<1,\,\nu>0}\mathscr K(r,\nu)=K_{\alpha,N}>1.}
\]
Equality occurs **if and only if** \(r^2=t_N\) and the first \(N\) nonconstant angular Fourier moments vanish:
\[
 \int e^{im\theta}\,d\nu(\theta)=0,\qquad m=1,\ldots,N.
\]
In particular, among all designs with exactly \(N+1\) distinct nodes and strictly positive weights, equality holds precisely for equally weighted vertices of a regular \((N+1)\)-gon, up to rotation and relabeling.

As \(N\to\infty\), with \(\alpha>-1\) fixed, the optimal squared condition number grows as
\[
 \boxed{K_{\alpha,N}\sim
 \frac{1}{\Gamma(\alpha+2)}
 \left(\frac{1}{e}\right)^{\alpha+1}
 \left(\frac{N}{\log N}\right)^{\alpha+1}.}
\]
The uniquely optimal radius obeys
\[
 r_N=\sqrt{t_N}=1-\frac{(\alpha+1)\log N}{2N}+O_\alpha(N^{-1}).
\]
Thus no sequence of measurements confined to one radius can form uniformly conditioned sampling frames for all increasing Bergman polynomial spaces, irrespective of angular oversampling.

## Assumptions and scope

Use the probability-normalized area measure
\[
 d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,\frac{dA(z)}\pi,
\qquad \alpha>-1,
\]
so the orthonormal polynomial basis is \(e_k(z)=\sqrt{w_k}z^k\), for \(0\le k\le N\). The measure \(\nu\) can be discrete or continuous, and its positive total mass does not affect \(\mathscr K\). A discrete design with fewer than \(N+1\) support points is singular and has infinite condition number. The theorem concerns **one common centered circle** and does not constrain or classify observations at multiple radii.

## Proof

**1. Universal diagonal obstruction.** Normalize \(\nu\) to a probability measure and put \(t=r^2\). In the orthonormal basis above, its positive semidefinite sampling Gram matrix is
\[
 G_{k\ell}=\sqrt{w_kw_\ell}\,r^{k+\ell}
 \int e^{i(k-\ell)\theta}\,d\nu(\theta).
\]
Its diagonal is \(d_k=w_kt^k\). The Rayleigh variational principle gives
\[
 \lambda_{\min}(G)\le\min_k d_k,
 \qquad \lambda_{\max}(G)\ge\max_k d_k,
\]
so \(\mathscr K(r,\nu)\ge D(t):=\max_k d_k/\min_k d_k\), including singular designs.

**2. Unique optimal radius.** For \(\alpha>-1\),
\[
 \frac{w_{k+1}}{w_k}=1+\frac{\alpha+1}{k+1}
\]
is strictly decreasing. Hence \(k\mapsto\log d_k\) is strictly concave and its minimum on \(\{0,\ldots,N\}\) lies at an endpoint. Since \(w_0=1\) and \(w_N>1\), the equality of endpoint diagonals is attained at the unique \(t_N=w_N^{-1/N}\in(0,1)\). For \(t<t_N\), \(d_N<d_0\) and
\[
 D(t)=\max_{0\le k<N}\frac{w_k}{w_N}t^{k-N},
\]
which is strictly decreasing as \(t\) increases (each nonconstant term has a strictly negative power, and the maximizing term cannot be \(k=N\) since \(D(t)>1\)). For \(t>t_N\), \(d_0<d_N\) and
\[
 D(t)=\max_{1\le k\le N}w_kt^k,
\]
strictly increasing. Hence \(\min_{0<t<1}D(t)=D(t_N)=K_{\alpha,N}\) and the optimal radius is unique. Strict concavity puts \(d_k>1\) for each interior \(k\), so \(K_{\alpha,N}>1\).

**3. Equality and complete angular rigidity.** At \(t=t_N\), \(d_0=d_N=1\) and \(\max d_k=K_{\alpha,N}\). If \(\mathscr K=K_{\alpha,N}\), the chain \(\lambda_{\min}\le1\), \(\lambda_{\max}\ge K_{\alpha,N}\) forces both equalities. Therefore the Rayleigh quotient of the unit vector \(e_0\) equals the smallest eigenvalue \(1\); in a Hermitian matrix this means \(Ge_0=e_0\). Its off-diagonal entries yield \(\int e^{ik\theta}d\nu=0\) for all \(1\le k\le N\). Conversely, these zero moments make \(G\) exactly diagonal, attaining the bound. This proves necessity and sufficiency for every finite positive Borel angular measure.

If \(\nu=\sum_{j=0}^N a_j\delta_{\theta_j}\) has distinct nodes and \(a_j>0\), normalize \(\sum a_j=1\) and form the square matrix \(F_{jk}=\sqrt{a_j}e^{ik\theta_j}\), \(0\le j,k\le N\). Vanishing moments make \(F^*F=I\), hence \(FF^*=I\). The diagonal gives \(a_j=1/(N+1)\). Distinct-row orthogonality gives \(\sum_{k=0}^{N}e^{ik(\theta_j-\theta_\ell)}=0\); hence every ratio \(e^{i(\theta_j-\theta_\ell)}\) is a nontrivial \((N+1)\)-th root of unity. Thus the points form a rotated regular polygon. The converse is the usual root-of-unity sum.

**4. Sharp growth law.** Put \(a=\alpha+1>0\). Stirling's gamma-ratio formula yields, uniformly as \(k\to\infty\),
\[
 w_k=\frac{k^a}{\Gamma(a+1)}(1+O_a(k^{-1})),
 \quad \log w_N=a\log N-\log\Gamma(a+1)+O_a(N^{-1}).
\]
For \(x=k\log w_N/N\), the dominant profile \(w_kt_N^k\) is proportional to \(k^a e^{-k\log w_N/N}\), maximized when \(k\sim aN/\log w_N\sim N/\log N\). More precisely, the ratio of consecutive terms is
\[
 \frac{w_{k+1}t_N^{k+1}}{w_kt_N^k}
 =t_N\left(1+\frac{a}{k+1}\right),
\]
so the maximizing index equals \(a/(\exp(\log w_N/N)-1)+O(1)\). Evaluating at that index gives
\[
 K_{\alpha,N}=\frac1{\Gamma(a+1)}
 \left(\frac{aN}{e\log w_N}\right)^a(1+o(1))
 \sim\frac1{\Gamma(a+1)}\left(\frac{N}{e\log N}\right)^a.
\]
The last expression equals the coefficient in the finding because \(\log w_N\sim a\log N\). Finally \(r_N=\exp(-\log w_N/(2N))\) gives the claimed boundary scale.

## Verification

The exact Gram diagonal, the two monotonicity regions, and the unitary-design rigidity have been compared numerically on finite polynomial families using the reproducible standard-library program `verify.py`. It checks the normalized moment identities for several values of \(\alpha\), positive weighted polygon samples, and random angular perturbations and nonoptimal radii. These finite checks supplement rather than replace the all-order proof and asymptotic argument above.

## Relationship to prior work

Gröchenig and Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Bergman and Hardy Spaces* (first arXiv version May 28, 2020), establish the Bergman polynomial sampling framework and distinguish disk-wide Bergman sampling from boundary-concentrated Hardy sampling. Their open-access full paper supplies the monomial norms and general necessity of radial distribution, but does not formulate a sharp **finite-degree minimax condition number over all positive one-circle designs**, its complete equal-node rigidity, or the weight-dependent asymptotic coefficient proved here. The standard root-of-unity orthogonality is used as known mathematics, not claimed as novel. A corresponding exact one-radius optimization in Gaussian Fock polynomial spaces uses factorial rather than Bergman binomial moments and has exponential rather than polynomial conditioning growth; it does not imply the Bergman formulas. The result also does not follow from a general sampling-cardinality bound, because it holds even with arbitrary angular oversampling or continuous angular access.

## Limitations

The result is specific to measurements on a single centered circle and polynomial degree \(N\). No bound is claimed for arbitrary multiradius designs. The rate is an asymptotic with \(\alpha\) fixed, not a uniform two-parameter expansion. The theorem concerns spectral condition number, not noise statistics for a specified reconstruction algorithm. The proof is self-contained, but an equivalent presentation in older quadrature or polynomial least-squares literature cannot be excluded by electronic searches alone; mathematical novelty remains subject to external historical assessment.

## References

1. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Bergman and Hardy Spaces*, arXiv:2005.14176 (first posted May 28, 2020), https://arxiv.org/abs/2005.14176 ; open-access journal version, *Journal of Geometric Analysis* **31** (2021), 7595–7619, https://doi.org/10.1007/s12220-020-00599-5 .
2. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Fock Space*, arXiv:2109.11825 (first posted September 24, 2021), https://arxiv.org/abs/2109.11825 .
3. K. Gröchenig, *Sampling, Marcinkiewicz–Zygmund Inequalities, Approximation, and Quadrature Rules*, arXiv:1909.07752 (first posted September 17, 2019), https://arxiv.org/abs/1909.07752 .
