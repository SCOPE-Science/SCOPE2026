# An exponential gap between minimum-eigenvalue and determinant designs for circular Fock sampling

## Finding

For every integer \(m\geq 1\), put \(n=m+1\),
\[
F_m(t)=\sum_{k=0}^{m}\frac{t^k}{k!},\qquad
T_m=(m!)^{1/m},\qquad
\mu_m(t)=\frac{\sum_{k=0}^{m}k t^k/k!}{F_m(t)}.
\]
In the \(n\)-dimensional Gaussian Fock polynomial space, consider all square, normalized point-evaluation designs with \(n\) distinct points lying on **one circle of freely chosen radius**. Define the squared condition number as the ratio of the largest to smallest eigenvalues of the frame Gram operator, and define the determinant criterion as the determinant of that same normalized Gram operator.

**Theorem (two incompatible optimal radii).** Every design maximizing the least frame eigenvalue, and every design minimizing the squared condition number, consists of the vertices of a regular \(n\)-gon (up to rotation), at the unique radius
\[
\boxed{\rho_{\mathrm E}=\sqrt{T_m/\pi}}.
\]
The sharp least frame eigenvalue and squared condition number are respectively
\[
\boxed{A_m^*=\frac{n}{F_m(T_m)},\qquad
\kappa_m^{2,*}=\max_{0\leq k\leq m}\frac{T_m^k}{k!}.}
\]
Every determinant-maximizing design is likewise a rotated regular \(n\)-gon, but at the unique radius
\[
\boxed{\rho_{\mathrm D}=\sqrt{S_m/\pi},\qquad \mu_m(S_m)=m/2.}
\]
For \(m=1,2\), \(S_m=T_m\). For **every \(m\geq3\)** one has \(S_m>T_m\): the determinant optimizer is strictly worse in minimum eigenvalue and conditioning than the minimum-eigenvalue optimizer. More sharply,
\[
S_m=\frac m2+\frac{\sqrt m}{2\sqrt{2\pi}}
\left(\frac{\sqrt e}{2}\right)^m(1+o(1)),
\quad T_m\sim\frac m e,
\]
and, if \(\kappa_{m,\mathrm D}\) denotes the singular-value condition number at the determinant optimum,
\[
\boxed{\frac{\kappa_{m,\mathrm D}^{2}}{\kappa_m^{2,*}}
\sim \frac{2^{(1-1/e)/2}}{\sqrt e}\,(\pi m)^{-1/(2e)}
\exp\!\left[\left(\frac12-\frac1e\right)m\right].}
\]
In particular, maximizing the normalized sampling determinant causes an **exponentially growing relative squared-conditioning loss** within this single-circle design class.

## Assumptions and scope

The Fock norm is
\[
\|f\|^2=\int_{\mathbb C}|f(z)|^2e^{-\pi|z|^2}\,dA(z).
\]
Let \(\mathcal P_m\) be the polynomials of degree at most \(m\), with orthonormal basis \(e_k(z)=(\pi^k/k!)^{1/2}z^k\). Its reproducing kernel is \(K_m(z,w)=\sum_{k=0}^m(\pi z\overline w)^k/k!\). Choose \(\lambda_j=\rho e^{i\theta_j}\) with \(\rho>0\) and distinct angles modulo \(2\pi\), for \(0\leq j\leq m\). The finite-section-kernel-normalized evaluation operator is
\[
\mathcal T_\Lambda f=\left(\frac{f(\lambda_j)}{\sqrt{K_m(\lambda_j,\lambda_j)}}\right)_{j=0}^{m},
\quad G_\Lambda=\mathcal T_\Lambda^*\mathcal T_\Lambda.
\]
Every \(G_\Lambda\) is positive definite by polynomial interpolation. The **least eigenvalue** means \(\lambda_{\min}(G_\Lambda)\), and \(\kappa^2=\lambda_{\max}(G_\Lambda)/\lambda_{\min}(G_\Lambda)\); the determinant objective is \(\det G_\Lambda\). No free sampling weights or second radial layer are allowed. Normalization uses the **truncated** kernel \(K_m\), not the full Fock kernel.

## Proof

**1. A diagonal constraint for arbitrary angular nodes.** Write \(t=\pi\rho^2\), \(a_k=t^k/k!\), \(F=F_m(t)\). In the orthonormal basis,
\[
(G_\Lambda)_{k\ell}
=\frac{\sqrt{a_ka_\ell}}F\sum_{j=0}^{m}e^{i(k-\ell)\theta_j}.
\]
Consequently the diagonal is \(d_k=na_k/F\), independently of the angles. The Rayleigh principle gives
\[
\lambda_{\min}(G_\Lambda)\leq\min_kd_k,\quad
\lambda_{\max}(G_\Lambda)\geq\max_kd_k,\quad
\kappa(G_\Lambda)^2\geq\frac{\max_ka_k}{\min_ka_k}.
\]
Hadamard's determinant inequality gives \(\det G_\Lambda\leq\prod_kd_k\). At a rotated regular \(n\)-gon, the angular sums at every nonzero difference \(|k-\ell|<n\) vanish, so all three bounds are attained simultaneously at that fixed \(t\).

Equality in the determinant bound forces all off-diagonal entries to vanish. In particular, \(\sum_j e^{i\ell\theta_j}=0\) for \(1\leq\ell\leq m\). Newton's identities imply that the monic polynomial whose roots are \(e^{i\theta_j}\) has the form \(z^n-c\), where \(|c|=1\); hence the nodes form a rotated regular \(n\)-gon. The same rigidity applies whenever a least-diagonal coordinate realizes the least eigenvalue: the corresponding standard basis vector is a minimum-eigenvalue eigenvector, forcing its whole off-diagonal row to vanish; at an endpoint coordinate, this supplies all nonzero angular power sums.

**2. The least-eigenvalue and condition optima.** The sequence \(a_k\) is strictly log-concave in \(k\), so its minimum occurs at an endpoint. Since \(a_0=1\) and \(a_m=t^m/m!\),
\[
\min_ka_k=\min\{1,t^m/m!\}.
\]
The endpoints agree exactly when \(t=T_m=(m!)^{1/m}\). For \(t<T_m\), the upper bound on the least eigenvalue is \(n a_m/F\), strictly increasing because its logarithmic derivative is \((m-\mu_m(t))/t>0\). For \(t>T_m\), the upper bound is \(n/F\), strictly decreasing. Thus the sharp maximum is \(n/F_m(T_m)\), realized only by a regular polygon at \(t=T_m\).

Also, \(\max_k a_k\) is the upper envelope of monomials \(t^k/k!\). For \(t<T_m\), the ratio \(\max_k a_k/a_m\) strictly decreases: each relevant term has logarithmic derivative \((k-m)/t<0\), except \(k=m\), which cannot be the maximum for \(m\geq2\) at the optimum range. For \(t>T_m\), \(\max_k a_k/a_0\) strictly increases: each nonconstant term does so, and the maximum is nonconstant. The elementary \(m=1\) case has the same unique minimum at \(t=1\). This proves the unique global condition optimum at \(T_m\) and its displayed value; regular-polygon rigidity follows from the endpoint minimum-eigenvector argument above.

**3. The determinant optimum.** For regular polygons the exact determinant is
\[
D_m(t)=\frac{n^n t^{nm/2}}{F_m(t)^n\prod_{k=0}^m k!}.
\]
Its logarithmic derivative is \(\frac n t(m/2-\mu_m(t))\). The derivative \(\mu_m'(t)=\operatorname{Var}_{p_t}(k)/t>0\), where \(p_t(k)=a_k/F_m(t)\), and \(\mu_m\) increases continuously from \(0\) to \(m\). Hence exactly one positive \(S_m\) satisfies \(\mu_m(S_m)=m/2\), and it is the unique radius optimum. Hadamard equality gives the complete angular optimizer classification.

**4. Why the two radii separate.** At \(t=T_m\), \(a_0=a_m=1\). For \(m\geq3\) and \(1\leq k<m/2\),
\[
\frac{(m-k)!}{k!}> (m!)^{(m-2k)/m},
\qquad\text{hence}\qquad a_k>a_{m-k}.
\]
To verify the first inequality, pair the factors \(j\) and \(m+1-j\) in \(m!\). Their geometric means \(\sqrt{j(m+1-j)}\) increase strictly toward the center; for odd \(m\), the unpaired central factor is still larger. Removing the \(k\) outer pairs strictly increases the geometric mean of the remaining factors. The displayed inequality is exactly this comparison of the full and middle-block geometric means. Pairing the terms \(k\) and \(m-k\) in the numerator of \(\mu_m(T_m)-m/2\) now gives a strict negative sum. Thus \(\mu_m(T_m)<m/2\), so \(S_m>T_m\). For \(m=1,2\), direct substitution gives equality. Since \(S_m>T_m\) and both least-eigenvalue and condition objectives have unique radial optima, the determinant optimizer sacrifices both objectives strictly.

**5. Sharp large-degree gap.** Stirling's formula yields
\[
T_m=\frac{m}{e}+\frac{\log(2\pi m)}{2e}+o(1).
\]
The identity \(\mu_m(t)=t\bigl(1-(t^m/m!)/F_m(t)\bigr)\) and elementary Poisson large-deviation bounds imply \(S_m/m\to1/2\). At \(t=m/2\), the truncated-Poisson tail above \(m\) is exponentially small, \(\mu_m'(t)=1+o(1)\) uniformly in a shrinking neighborhood, and the mean deficit is
\[
\frac m2-\mu_m(m/2)\sim\frac m2\,e^{-m/2}\frac{(m/2)^m}{m!}
\sim\frac{\sqrt m}{2\sqrt{2\pi}}\left(\frac{\sqrt e}{2}\right)^m.
\]
The mean-value theorem transfers this deficit to \(S_m-m/2\). Finally, for positive \(t\to\infty\) with \(t<m\), the largest term of the exponential series satisfies \(\max_k t^k/k!\sim e^t/\sqrt{2\pi t}\). Thus
\[
\kappa_m^{2,*}\sim\sqrt e\,(2\pi m)^{(1/e-1)/2}e^{m/e},
\quad
\kappa_{m,\mathrm D}^{2}\sim\frac{e^{m/2}}{\sqrt{\pi m}},
\]
whose quotient is the stated exponential-gap asymptotic.

## Verification

A standalone numerical verifier `verify_fock.py` reconstructs the normalized finite-section evaluation matrix and Hermitian Gram operators. It compares their eigenvalues at regular polygons to the exact diagonal spectrum; checks Hadamard, Rayleigh, and uniqueness-radius inequalities at 275 randomly chosen angular configurations; solves the unique determinant-radius equation; and tests the logarithmic gap for degrees up to \(640\). It completed 341 test configurations, with maximum regular-spectrum absolute discrepancy \(3.55\times10^{-15}\). The exact claims for all degrees are proved above; finite floating-point tests are supporting diagnostics only. Reproduce with Python 3.10+, NumPy and SciPy by running `python verify_fock.py`.

## Relationship to prior work

Gröchenig and Ortega-Cerdà (arXiv:2109.11825, submitted 2021-09-24) establish the finite Gaussian-Fock reproducing kernel and the general theory of Marcinkiewicz–Zygmund polynomial sampling and its Gabor interpretation. They do **not** claim the present one-circle radial E-versus-D optimizer classification in the inspected full text. Karvonen, Särkkä, and Tanaka (arXiv:1912.07316) study determinant-driven approximate Fekete designs for general real-kernel interpolation, notably Gaussian real-line kernels, rather than this circular finite Fock problem. Earlier coherent-state circle papers study circular superpositions; their possible relevance to finite-dimensional design criteria is a remaining bibliography risk.

The sharp global angular rigidity, the two different uniquely optimal radii, and the exponential asymptotic tradeoff are the claim here. The Fourier diagonalization and Vandermonde/Newton identities themselves are standard tools, not claimed as new.

## Limitations

The optimizer classification is **only** among exactly \(m+1\) distinct normalized evaluation points on a common circle centered at the origin. It is not a global optimum among unrestricted planar point sets, variable weights, or several circles. The exponential gap concerns the square of the matrix/sampling-operator singular-value condition number, not its unsquared value. The single-circle designs become exponentially ill-conditioned with degree, so the theorem is not a uniform Marcinkiewicz–Zygmund sampling result. The numerical verifier is not an infinite proof, and external independent scientific audit has not been performed. An unindexed equivalent coherent-state conditioning treatment remains possible.

## References

1. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Fock Space*, arXiv:2109.11825 (initial public version 2021-09-24), https://arxiv.org/abs/2109.11825; *Mathematische Zeitschrift* 302 (2022), 1409–1428.
2. T. Karvonen, S. Särkkä and K. Tanaka, *Kernel-based interpolation at approximate Fekete points*, arXiv:1912.07316 (2019-12-16), https://arxiv.org/abs/1912.07316.
3. J. Janszky, P. Domokos and P. Adam, *Coherent states on a circle and quantum interference*, *Physical Review A* 48 (1993), 2213–2219, https://doi.org/10.1103/PhysRevA.48.2213 (abstract accessed; full comparison unresolved).
4. P. Domokos, P. Adam and J. Janszky, *One-dimensional coherent-state representation on a circle in phase space*, *Physical Review A* 50 (1994), 4293–4297, https://doi.org/10.1103/PhysRevA.50.4293 (abstract accessed; full comparison unresolved).
