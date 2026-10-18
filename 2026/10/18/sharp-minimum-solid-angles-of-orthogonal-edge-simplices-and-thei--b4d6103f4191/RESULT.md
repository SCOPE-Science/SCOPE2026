# Sharp minimum solid angles of orthogonal-edge simplices and their high-dimensional law

## Finding
For each integer \(d\ge2\), consider a \(d\)-simplex with one vertex having \(d\) mutually orthogonal outgoing edges. Its smallest normalized vertex solid angle is maximized **uniquely**, modulo Euclidean similarity, when these edges have equal lengths. The resulting optimal angle is a non-elementary Dirichlet expectation, with the explicit sharp equivalent
\[
\theta_d\sim\frac{e^{-1}}{\sqrt2}\left(\frac{e}{2\pi d}\right)^{d/2}.
\]
The exact finite-dimensional formula is
\[
\theta_d=\frac{\Gamma(d/2)}{2\pi^{d/2}(d-1)!}\mathbb E\left(1+\sum_{j=1}^{d-1}R_j^2\right)^{-d/2},\qquad R\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
This is the **best possible** dimension-dependent minimum-angle quality threshold within orthogonal-edge simplices.

## Assumptions and scope
Let \(e_1,\ldots,e_d\) be a Euclidean orthonormal basis and \(a_1,\ldots,a_d>0\). Up to a rigid motion and translation, every simplex with a specified orthogonal vertex is
\[
S(a)=\operatorname{conv}\{0,a_1e_1,\ldots,a_de_d\}\subset\mathbb R^d.
\]
For each vertex \(v\), let \(C_v=\{\lambda(x-v):\lambda\ge0,\ x\in S(a)\}\) be its closed tangent cone. Its normalized solid angle is \(\omega_v=\Pr(Z\in C_v)\) for a standard \(d\)-dimensional Gaussian \(Z\). This equals its relative \((d-1)\)-dimensional spherical measure, using the entire unit sphere as denominator. Write \(m(S)=\min_v\omega_v\).

For \(R=(R_1,\ldots,R_d)\sim\operatorname{Dirichlet}(1,\ldots,1)\), the coordinates are nonnegative, sum to one, and have constant density \((d-1)!\) over the \((d-1)\)-simplex. All asymptotics here are for positive integer dimensions \(d\to\infty\), not for fixed dimension with degenerating lengths.

## Proof
**1. The sharp extremizer and equality.** At the right-angle vertex \(0\), the tangent cone is exactly the positive orthant; hence \(\omega_0=2^{-d}\). At vertex \(a_i e_i\), every tangent direction \(z\) satisfies precisely
\[
z_j\ge0\quad(j\ne i),\qquad z_i\le -a_i\sum_{j\ne i}\frac{z_j}{a_j}.
\]
This follows by expressing a point of the cone in the rays \(-a_i e_i\) and \(a_j e_j-a_i e_i\). Choose \(i\) so that \(a_i=\max_j a_j\). Since \(a_i/a_j\ge1\), its cone is contained in the corresponding cone of the equal-edge simplex, described by \(z_j\ge0\) and \(z_i\le-\sum_{j\ne i}z_j\). If at least one leg is smaller, the containment is **strict on a nonempty open set**, so the Gaussian measure decreases strictly. The equal-edge nonright vertex cone is strictly contained in the sign orthant \(z_j\ge0\ (j\ne i), z_i\le0\); its angle \(\theta_d\) is thus smaller than \(2^{-d}\). All the \(d\) nonright vertex cones of the equal-edge simplex are congruent. Therefore
\[
m(S(a))\le\omega_{a_i e_i}\le\theta_d,
\]
with strict inequality for unequal lengths. Equal lengths clearly attain \(m(S)=\theta_d\), proving uniqueness up to similarity.

**2. Exact expectation.** Fix one nonright corner in the equal-edge simplex and write \(Z_i=-s\), \(s\ge0\). Its Gaussian event becomes \(Z_j\ge0\) for all \(j\ne i\) and \(\sum_{j\ne i} Z_j\le s\). Therefore
\[
\theta_d=(2\pi)^{-d/2}\int_0^\infty e^{-s^2/2}\int_{\substack{x_j\ge0\\\sum_{j=1}^{d-1}x_j\le s}}e^{-\frac12\sum_{j=1}^{d-1}x_j^2}\,dx_1\cdots dx_{d-1}\,ds.
\]
For fixed \(s>0\), substitute \(x_j=sR_j\). Under the uniform Dirichlet measure on \(d\) coordinates, the inner simplex integral equals
\[
\frac{s^{d-1}}{(d-1)!}\mathbb E\exp\left(-\frac{s^2}{2}\sum_{j=1}^{d-1}R_j^2\right).
\]
Tonelli's theorem applies because the integrand is nonnegative. Evaluating the gamma integral
\[
\int_0^\infty s^{d-1}e^{-s^2(1+q)/2}ds=2^{d/2-1}\Gamma(d/2)(1+q)^{-d/2}
\]
proves the displayed exact formula, with its full normalization factor \(\Gamma(d/2)/(2\pi^{d/2}(d-1)!)\).

**3. Sharp large-dimension constant.** Couple the Dirichlet variables for all dimensions by taking independent exponential random variables \(E_1,E_2,\ldots\) of mean one and setting \(R_j=E_j/(E_1+\cdots+E_d)\). The strong law of large numbers applied to \(E_j\) and \(E_j^2\) gives
\[
d\sum_{j=1}^{d-1}R_j^2
=\frac{d\sum_{j=1}^{d-1}E_j^2}{(\sum_{j=1}^{d}E_j)^2}\longrightarrow2\qquad\text{almost surely}.
\]
Thus \((1+\sum_{j<d}R_j^2)^{-d/2}\to e^{-1}\) almost surely. The terms all lie in \([0,1]\); dominated convergence shows that the expectation tends to \(e^{-1}\). Stirling's formula gives
\[
\frac{\Gamma(d/2)}{2\pi^{d/2}(d-1)!}
\sim\frac{1}{\sqrt2}\left(\frac{e}{2\pi d}\right)^{d/2},
\]
which proves the sharp equivalent.

**4. Low-dimensional checks.** In dimension two the maximizing simplex is a right isosceles triangle with smallest angle \(\pi/4\) out of \(2\pi\), hence \(\theta_2=1/8\). In dimension three, the three generating rays of a nonright cone have lengths \(1,\sqrt2,\sqrt2\), pairwise scalar products all one, and determinant magnitude one. The classical trihedral-angle formula yields
\[
\theta_3=\frac{\arctan(3-2\sqrt2)}{2\pi}.
\]
These special values are consistency checks, not assumptions.

## Verification
The separately supplied `right_simplex_checker.py` runs two deterministic Dirichlet simplex quadratures for \(d=2,3\), compares them with the independent plane-angle and trihedral-angle formulas, and verifies symbolic first and second Dirichlet moment identities. Reproducible seeded Monte Carlo estimates of the **normalized expectation factor** at dimensions 16, 64, 256 and 1024 agree with convergence toward \(e^{-1}\). All checks passed using Python 3, NumPy, SciPy and SymPy. The all-dimension inequality, uniqueness, exact integral identity and asymptotic are established in the proof, not inferred from the finite checks.

## Relationship to prior work
Karasev, Kynčl, Paták, Patáková and Tancer give a general superexponential upper bound for the smallest simplex solid angle and quote Rogers's asymptotic for the *regular* simplex, but do not identify a sharp optimizer or the Dirichlet constant in the orthogonal-edge family [2]. Akopyan and Karasev prove an upper comparison with the *regular* simplex in dimension three and a local regular-simplex statement in dimension four [3]; neither determines this restricted right-angled family in all dimensions. Licht's new shape-measure manuscript [1] motivates the relevance of minimum solid angle, but only its abstract and bibliographic metadata were accessible for review. Consequently no claim is made about uninspected propositions in that manuscript. The new result concerns unequal orthogonal legs and an exact dimension-dependent asymptotic constant, not the broader conjecture that the regular simplex maximizes the least vertex angle among **all** simplices.

## Limitations
The result concerns simplices **with one orthogonal vertex**, not all simplices or general orthoschemes. It does not solve the global minimum-angle problem for arbitrary simplices in dimensions five and above. The finite calculations supplement but do not prove the limit. The full text of Licht [1] was inaccessible at the time of comparison despite attempts to obtain the preprint and open-access alternatives; possible conceptual overlap with that source and with unindexed classical angular literature remains a priority risk. Independent scientific audit is not claimed.

## References
[1] Martin W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1, first submitted 2026-10-05, https://arxiv.org/abs/2610.05883. Relevant evidence inspected: bibliographic metadata and abstract only.

[2] R. Karasev, J. Kynčl, P. Paták, Z. Patáková, M. Tancer, *Bounds for Pach's selection theorem and for the minimum solid angle in a simplex*, arXiv:1403.8147v4, https://arxiv.org/pdf/1403.8147. Relevant full text inspected: section 2, Theorem 6, Question 7, regular-simplex asymptotics.

[3] A. Akopyan and R. Karasev, *Bounding minimal solid angles of polytopes*, arXiv:1505.05263v2, https://arxiv.org/pdf/1505.05263. Relevant full text inspected: the abstract, introduction, conjectures and dimension-three/four arguments.
