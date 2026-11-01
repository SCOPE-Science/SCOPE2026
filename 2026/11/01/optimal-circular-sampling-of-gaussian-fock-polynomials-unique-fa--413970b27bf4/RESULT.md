# Optimal circular sampling of Gaussian Fock polynomials: unique factorial radius and exponential conditioning

## Finding
For every integer \(n\ge1\), the unique best-conditioned set of exactly \(N=n+1\) normalized Gaussian-Fock polynomial evaluations constrained to a *single centered circle*, with arbitrary positive weights of fixed total mass, is the equally weighted regular \(N\)-gon at one explicitly determined radius. Writing
\[
 x_n=(n!)^{1/n},\qquad M_n=\max_{0\le k\le n}\frac{x_n^k}{k!},
\]
the sharp spectral condition number is
\[
 \boxed{\inf_{R,\,\theta,\,a}\kappa(S)=\sqrt{M_n}.}
\]
The only attaining configurations, up to rotation and permutation, have
\[
 \boxed{\pi R^2=x_n,\quad a_j=1,\quad \theta_j=\theta_0+\frac{2\pi j}{n+1}.}
\]
In particular, the least possible condition number grows exponentially with the precise coefficient
\[
 \boxed{\kappa_{\min,n}=e^{1/4}(2\pi n)^{(e^{-1}-1)/4}\exp\!\left(\frac{n}{2e}\right)(1+o(1)).}
\]

## Assumptions and scope
Use the analytic Fock Hilbert space \(\mathcal F^2\) with
\[
 \|f\|^2=\int_{\mathbb C}|f(z)|^2e^{-\pi|z|^2}\,dA(z),
\qquad e_k(z)=\frac{\pi^{k/2}z^k}{\sqrt{k!}}.
\]
Let \(\mathcal P_n=\operatorname{span}\{e_0,\ldots,e_n}\) and let the truncated kernel diagonal be \(K_n(R)=\sum_{k=0}^n(\pi R^2)^k/k!\). Choose a radius \(R>0\), pairwise distinct phases \(\theta_0,\ldots,\theta_n\) modulo \(2\pi\), and weights \(a_j>0\) summing to \(N=n+1\). Define the square sampling operator by
\[
 (Sf)_j=\sqrt{\frac{a_j}{K_n(R)}}\,f(Re^{i\theta_j}),\qquad 0\le j\le n.
\]
The condition number is \(\kappa(S)=s_1(S)/s_N(S)\). The positivity/distinctness assumptions make \(S\) invertible. Common scaling of weights would leave \(\kappa\) unchanged; the mass convention fixes the normalization. We do **not** allow varying radii by node, adding more points, or non-point-evaluation measurements.

## Proof
**Diagonal lower bound.** Put \(x=\pi R^2\) and \(w_k(x)=x^k/k!\). In the orthonormal monomial basis,
\[
 S_{jk}=\sqrt{\frac{a_j}{K_n(R)}}\sqrt{w_k(x)}e^{ik\theta_j}.
\]
Consequently every diagonal Gram entry is independent of angles and weight allocation:
\[
 (S^*S)_{kk}=\frac{N w_k(x)}{K_n(R)}.
\]
The largest eigenvalue of a positive matrix dominates its largest diagonal entry; the least eigenvalue is bounded above by its smallest diagonal entry. Thus
\[
 \kappa(S)^2\ge h_n(x):=\frac{\max_{0\le k\le n}w_k(x)}{\min_{0\le k\le n}w_k(x)}.
\]
For a regular \(N\)-gon with \(a_j=1\), all off-diagonal Gram entries vanish by finite Fourier orthogonality (degrees \(0\) through \(N-1\)). Equality holds in the lower bound at **every** fixed \(x>0\).

**Unique radius.** The ratio \(w_k(x)/w_{k-1}(x)=x/k\) decreases with \(k\), so \(w_k(x)\) is log-concave and its minimum over the finite index interval is at an endpoint:
\[
 \min_k w_k(x)=\min\{1,x^n/n!}.
\]
There is one balancing point \(x_n=(n!)^{1/n}\). For \(0<x<x_n\),
\[
 h_n(x)=\max_{0\le k<n}\frac{n!}{k!}x^{k-n},
\]
a maximum of finitely many strictly decreasing functions, hence strictly decreasing. For \(x>x_n\),
\[
 h_n(x)=\max_{1\le k\le n}\frac{x^k}{k!},
\]
a maximum of finitely many strictly increasing functions. The global optimum is therefore attained at the **unique** radius \(\pi R^2=x_n\), with value \(h_n(x_n)=M_n\), because \(w_0(x_n)=w_n(x_n)=1\) and every intermediate weight is at least one.

**Rigidity of angles and weights.** Suppose \(\kappa(S)^2=M_n\) at the balanced radius. The diagonal Rayleigh quotients for the constant and highest monomials equal \(d=N/K_n(R)\), the smallest diagonal entry. Equality in the eigenvalue-ratio bound forces \(\lambda_{\min}(S^*S)=d\); therefore the constant-monomial unit vector is a least-eigenvalue eigenvector. Its off-diagonal Gram entries must vanish:
\[
 \sum_{j=0}^n a_j e^{i\ell\theta_j}=0
 \quad(1\le\ell\le n).
\]
Define \(U_{jk}=\sqrt{a_j/N}e^{ik\theta_j}\). Vanishing positive and negative Fourier moments and \(\sum a_j=N\) yield \(U^*U=I_N\). Since \(U\) is square, it is unitary. The squared norm of row \(j\) is then \(a_j\), so each \(a_j=1\). Orthogonality of two distinct rows implies
\[
 \sum_{k=0}^n e^{ik(\theta_j-\theta_\ell)}=0\qquad(j\ne\ell).
\]
As the phases are distinct, the geometric-series identity forces every angle difference to be a nonzero multiple of \(2\pi/N\). There are exactly \(N\) nodes, so they comprise one rotated regular \(N\)-gon. Conversely this configuration attains the stated bound. This proves the complete equality characterization, including \(n=1\).

**Sharp growth.** Stirling's expansion gives
\[
 x_n=\frac ne+\frac{\log(2\pi n)}{2e}+O\!\left(\frac{(\log n)^2}{n}\right).
\]
The maximizing index for \(w_k(x_n)\) is a Poisson mode at distance at most one from \(x_n\); the index lies below \(n\). The local Stirling estimate therefore yields
\[
 M_n=\frac{e^{x_n}}{\sqrt{2\pi x_n}}(1+O(n^{-1})).
\]
Taking a square root and substituting the preceding expansion establishes exactly
\[
 \sqrt{M_n}=e^{1/4}(2\pi n)^{(e^{-1}-1)/4}e^{n/(2e)}(1+o(1)).
\]

## Verification
The attached `check_sampling.py` evaluates the exact Gram matrices for regular polygons and random positive-weight angular perturbations, tests the diagonal bound and uniqueness of the optimum on finite grids, and compares logarithmic asymptotics with the explicit formula. The script passed 694 finite assertions using NumPy. These are consistency checks; the proof above establishes the all-degree result. Rerun with `python check_sampling.py` using Python 3 and NumPy.

## Relationship to prior work
Gröchenig and Ortega-Cerdà (2021 preprint; 2022 journal article) introduce precisely the finite Gaussian-Fock sampling normalization and prove in Proposition 6.4 that no \(n+1\)-point families have *uniform* Marcinkiewicz–Zygmund constants. Their conclusion does not give the optimum over circular geometries, its equality cases, or a quantitative sharp exponential rate. Here the class is much more restricted (one common centered radius) but the finite-degree minimax problem is solved exactly, with positive sample weights also optimized. The discrete Fourier orthogonality for a regular polygon is standard and is used rather than claimed as new. General Vandermonde conditioning results concern different norms/weights and do not directly determine the factorial Fock radius or its asymptotics.

## Limitations
The optimum is **not** claimed for all sets of \(n+1\) arbitrary planar nodes or for oversampled frames. The conditioning metric is the ordinary spectral condition number of *normalized point evaluations*. Only positive scalar weights and common-radius configurations are optimized. Established special-function and Fourier facts are not asserted to be novel. Historical priority remains subject to further specialized literature review. Independent mathematical validation has not been performed.

## References
1. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz-Zygmund Inequalities for Polynomials in Fock Space*, arXiv:2109.11825, first posted 24 September 2021; *Mathematische Zeitschrift* 302 (2022), 1409–1428, DOI 10.1007/s00209-022-03087-4. In particular, the monomial and reproducing-kernel formulas in Section 2 and Proposition 6.4.
2. V. Y. Pan, *How Bad Are Vandermonde Matrices?*, arXiv:1504.02118, 2015. General Fourier/Vandermonde conditioning context, not used as a sharp Gaussian-weighted minimax theorem.
