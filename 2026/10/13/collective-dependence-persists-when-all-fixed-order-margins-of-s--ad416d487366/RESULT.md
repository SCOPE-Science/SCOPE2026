# Collective dependence persists when all fixed-order margins of spherical copulas become independent

## Finding
For each integer \(d\ge 2\), let \(P_{d,p}\) denote the unique positive \(L_p\)-norm spherical copula with uniform coordinate marginals, in the absolutely continuous range \(p>d-1\). Write \(Q_d\) for the product of \(d\) uniform distributions on \([0,1]\), and use natural logarithms. The total correlation has the exact value
\[
I_{d,p}:=D_{\mathrm{KL}}(P_{d,p}\|Q_d)
=-\log\Gamma(\beta)-(d-1)\log\Gamma(1+\alpha)
+t\bigl[\psi(1+\alpha)-\psi(\beta)\bigr],
\qquad \alpha=\frac1p,\quad t=\frac{d-1}{p},\quad \beta=1-t.
\]
Here \(\psi\) is the digamma function. Fix an arbitrary real \(c>1\), and set \(p_d=c(d-1)\). Then
\[
\lim_{d\to\infty}I_{d,p_d}=G(c)
:=-\log\Gamma(1-c^{-1})-c^{-1}\psi(1-c^{-1})>0.
\]
Simultaneously, for every *fixed* integer \(k\ge2\), the distribution \(P_{d,p_d}^{(k)}\) of any \(k\) designated coordinates satisfies
\[
D_{\mathrm{KL}}\bigl(P_{d,p_d}^{(k)}\|Q_k\bigr)
=\frac{\pi^2 k(k-1)}{12p_d^2}+O_k(p_d^{-3}),
\qquad
\|P_{d,p_d}^{(k)}-Q_k\|_{\mathrm{TV}}\longrightarrow0.
\]
Despite this fixed-order asymptotic independence, the full-dimensional dependence remains separated from independence in total variation:
\[
\liminf_{d\to\infty}\|P_{d,p_d}-Q_d\|_{\mathrm{TV}}
\ge 1-2^{-1/c}\left(1+\frac{\log2}{c}\right)>0.
\]
In particular, for \(c=2\), the limiting total correlation is exactly
\[
G(2)=\log(2/\sqrt\pi)+\gamma/2=0.409390070086\ldots\ \text{nats},
\]
while the total-variation lower bound tends to \(0.047828682946\ldots\). Here \(\gamma\) is Euler's constant. The positive profile \(G(c)\) strictly decreases in \(c\), tends to infinity as \(c\downarrow1\), and tends to zero as \(c\to\infty\).

## Assumptions and scope
The positive \(L_p\)-norm spherical copula means the law of a positive-orthant \(L_p\)-spherical random vector with each marginal uniform on \([0,1]\), in the sense of Bernard, Müller and Oesting. For \(d\ge2\) and real \(p>d-1\), its density relative to \(d\)-dimensional Lebesgue measure is
\[
c_{d,p}(x)=\frac{\mathbf 1\{x_i\ge0,\ \sum_{i=1}^d x_i^p<1\}}
{\Gamma(\beta)\,\Gamma(1+\alpha)^{d-1}}
\left(1-\sum_{i=1}^d x_i^p\right)^{-t}.
\]
The symbols \(D_{\mathrm{KL}}\) and \(\|\cdot\|_{\mathrm{TV}}\) denote relative entropy and the supremum-over-events total variation distance, respectively. All asymptotics use real \(p_d=c(d-1)\), with fixed \(c>1\); the order \(k\) of a marginal is held fixed, and \(d\ge k\).

## Proof
**1. Dirichlet reduction.** Under \(P_{d,p}\), change variables to \(Y_i=X_i^p\) and the slack \(W=1-\sum_{i=1}^dY_i\). The Jacobian is \(\alpha^d\prod_{i=1}^dY_i^{\alpha-1}\). The preceding copula density therefore becomes the Dirichlet density with parameter vector
\[
(Y_1,\ldots,Y_d,W)\sim
\operatorname{Dirichlet}(\alpha,\ldots,\alpha,\beta),
\qquad d\alpha+\beta=1+\alpha.
\]
In particular \(W\sim\operatorname{Beta}(\beta,d\alpha)\) and
\[
\mathbb E\log W=\psi(\beta)-\psi(1+\alpha).
\]
The logarithm of the copula density on its support equals
\[
-\log\Gamma(\beta)-(d-1)\log\Gamma(1+\alpha)-t\log W.
\]
Integrating this equality against the copula law proves the exact total-correlation expression; the integral is finite because \(\beta>0\).

**2. Fixed-coordinate laws.** Dirichlet aggregation of the unobserved coordinates and the slack gives, for \(k\le d\),
\[
(Y_1,\ldots,Y_k,1-\sum_{i=1}^kY_i)
\sim\operatorname{Dirichlet}\bigl(\alpha,\ldots,\alpha,1-(k-1)\alpha\bigr).
\]
Consequently the \(k\)-coordinate law is precisely \(P_{k,p}\). Taylor expansion at zero of
\[
\log\Gamma(1+z)=-\gamma z+\frac{\zeta(2)}2z^2+O(z^3),\qquad
\psi(1+z)=-\gamma+\zeta(2)z+O(z^2)
\]
in the exact formula, using \(\zeta(2)=\pi^2/6\), yields
\[
I_{k,p}=\frac{\pi^2 k(k-1)}{12p^2}+O_k(p^{-3}).
\]
Pinsker's inequality implies \(\|P_{k,p}-Q_k\|_{\mathrm{TV}}\le\sqrt{I_{k,p}/2}\); taking \(p=p_d\) proves all fixed-order marginal assertions.

**3. Nonvanishing full-dimensional information.** Write \(t_d=(d-1)/p_d=1/c\) and \(\alpha_d=1/p_d\). In the exact formula, the Taylor identities
\[
(d-1)\log\Gamma(1+\alpha_d)=-\gamma t_d+O(d^{-1}),\qquad
 t_d\psi(1+\alpha_d)=-\gamma t_d+O(d^{-1})
\]
show cancellation of the two linear terms. The remaining terms converge to \(G(c)\). If \(u=1/c\in(0,1)\), differentiation of \(-\log\Gamma(1-u)-u\psi(1-u)\) gives \(u\psi'(1-u)>0\); its value at \(u=0\) is zero. This establishes strict positivity and the monotonicity in \(c\). Gamma and digamma expansions at zero prove \(G(c)\to\infty\) as \(c\downarrow1\) and \(G(c)\to0\) as \(c\to\infty\). The half-integer gamma/digamma identities yield the stated exact constant for \(c=2\).

**4. A full-dimensional distinguishing event.** Define
\[
A_d=\Bigl\{x\in[0,1]^d:\#\{i:x_i^{p_d}>1/2\}\ge2\Bigr\}.
\]
Under \(P_{d,p_d}\), the support constraint \(\sum_iX_i^{p_d}<1\) makes \(P_{d,p_d}(A_d)=0\). Under independent uniform coordinates, the count is binomial with success probability
\[
q_d=1-2^{-1/p_d},\qquad d q_d\longrightarrow\frac{\log2}{c}.
\]
Thus, by the Poisson limit for binomial counts,
\[
Q_d(A_d)=1-(1-q_d)^d-dq_d(1-q_d)^{d-1}
\longrightarrow 1-2^{-1/c}(1+\log2/c)>0.
\]
The definition of total variation now proves the lower bound, completing the finding.

## Verification
The accompanying `verify.py` evaluates the exact gamma/digamma expression at high precision, compares it against an independent one-dimensional beta integral for the logarithmic slack, checks the bivariate reflection-formula identity, and tests the predicted limits and finite-dimensional expansions. These finite diagnostics passed; the quantified infinite-dimensional statements follow from the preceding analytic argument rather than extrapolation of computations. Run with `python verify.py` after installing the ordinary Python package `mpmath`.

## Relationship to prior work
Bernard, Müller and Oesting (2022 preprint; 2024 journal publication) proved existence, uniqueness, radial beta representations, and the density of positive \(L_p\)-spherical copulas for \(p\ge d-1\). Their Corollary 11 gives the density used here and their discussion includes marginal correlations and finite extendibility, but does not state the joint KL information profile or the coexistence of fixed-order asymptotic independence with persistent full-dimensional variation distance. The Dirichlet reduction is a direct rewriting of their density using standard probability calculus; it is not presented as a new distribution family.

Perlman and Wellner (2011) studied the Euclidean circular and spherical cases in low dimensions, not the dimension-growing \(p_d=c(d-1)\) regime. Sundgren (2024) explicitly connected a symmetric Dirichlet family to radial \(L_p\)-copulas, particularly a special \(p=d\) slice; this does not entail the positive finite \(c>1\) information profile, and no corresponding relative-entropy or high-dimensional variation-distance limit was identified in the inspected manuscript. The general identification of copula entropy with mutual information is standard, for example in Ma and Sun (2011); the new comparison concerns the simultaneous high-dimensional limits in this particular spherical family.

## Limitations
The theorem concerns the unique positive-orthant \(L_p\)-spherical copula, with uniform marginals and \(p>d-1\). It does not describe arbitrary spherical or Archimedean copulas. The high-dimensional theorem holds for a fixed scale ratio \(c>1\) rather than all moving parameter sequences. The displayed total-variation constant is an explicit positive lower bound, not a claimed sharp distance. Fixed-order marginal convergence does not imply convergence of the full-dimensional laws, since their dimensions increase.

## References
1. C. Bernard, A. Müller, M. Oesting, *Lp-norm spherical copulas*, arXiv:2206.10180v1 (first publicly posted 2022-06-21); Journal of Multivariate Analysis 201 (2024), 105262, doi:10.1016/j.jmva.2023.105262. Author manuscript: https://cris.vub.be/ws/portalfiles/portal/114137087/95653168.pdf .
2. M. D. Perlman and J. A. Wellner, *Squaring the Circle and Cubing the Sphere: Circular and Spherical Copulas*, Symmetry 3 (2011), 574–599, doi:10.3390/sym3030574. https://pmc.ncbi.nlm.nih.gov/articles/PMC3369321/ .
3. D. Sundgren, *Uniform and radial Dirichlet copulas*, preprint posted 2024-01-16, doi:10.21203/rs.3.rs-3857082/v1. https://assets-eu.researchsquare.com/files/rs-3857082/v1_covered_32b2d2a3-a503-4b64-b2ff-8fe500c8cbb7.pdf .
4. J. Ma and Z. Sun, *Mutual Information Is Copula Entropy*, Tsinghua Science and Technology 16 (2011), 51–54, doi:10.1016/S1007-0214(11)70008-6.
