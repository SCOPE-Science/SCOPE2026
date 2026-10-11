# Dimension-monotone pinning of annular long-range segregation interfaces
## Finding
Fix positive boundary values \(M_1,M_2\), radii \(0<R<R_1\), and assume \(R_1+R<R_2\). For each integer \(n\ge2\), let \(r_n(R)\in(R_1,R_2-R)\) denote the unique inner free-boundary radius of the two-species annular long-range segregation limit studied by Chuah; the second free boundary is the concentric sphere of radius \(r_n(R)+R\).

Then the interface location is strictly ordered by dimension:
\[
r_{n+1}(R)<r_n(R)\qquad\text{for every }n\ge2.
\]
More sharply, if \(p=n-2\) and \(\alpha=M_1/M_2\), then
\[
r_n(R)-R_1\sim \frac{\alpha R_1}{p}\left(\frac{R_1}{R_1+R}\right)^p\qquad(n\to\infty).
\]
Consequently
\[
r_n(R)\to R_1,\qquad r_n(R)+R\to R_1+R,
\]
and the distance of the inner interface from the inner boundary is exponentially small in dimension, with the displayed sharp prefactor.

## Assumptions and scope
The parameters \(M_1,M_2,R_1,R_2,R\) are fixed while the integer dimension \(n\) varies. The strict geometric condition \(R_1+R<R_2\) guarantees a nonempty radial gap in which the two free boundaries can lie. The claim concerns the \(\varepsilon\to0^+\) limiting free-boundary configuration of the cited annular model. It does not assert an analogous dimension law for nonradial domains, for other interaction kernels, or for solutions at fixed positive \(\varepsilon\).

## Proof
Put \(p=n-2\) and, for every real \(p\ge0\) and \(x\in(R_1,R_2-R)\), define
\[
H_p(x)=\frac{\displaystyle\int_{R_1}^x s^{-p-1}\,ds}{\displaystyle\int_{x+R}^{R_2}s^{-p-1}\,ds}.
\]
For \(p=0\), this is
\[
H_0(x)=\frac{\log(x/R_1)}{\log(R_2/(x+R))}.
\]
For \(p>0\), integration gives
\[
H_p(x)=\frac{R_1^{-p}-x^{-p}}{(x+R)^{-p}-R_2^{-p}}.
\]
These are exactly the two fixed-dimension free-boundary equations in the source, written in one form: \(r_n(R)\) is the unique solution of
\[
H_{n-2}(r_n(R))=\frac{M_1}{M_2}.
\]

For fixed \(p\), the numerator defining \(H_p(x)\) strictly increases with \(x\), whereas the denominator strictly decreases, so \(H_p\) is strictly increasing in \(x\). For fixed \(x\), differentiate with respect to \(p\). If \(\mathbb E_{L,p}\) and \(\mathbb E_{U,p}\) denote averages with density proportional to \(s^{-p-1}\) on \([R_1,x]\) and \([x+R,R_2]\), respectively, then
\[
\frac{\partial}{\partial p}\log H_p(x)
=\mathbb E_{U,p}[\log s]-\mathbb E_{L,p}[\log s].
\]
Every point of the upper interval is strictly larger than every point of the lower interval because \(R>0\). Therefore the right-hand side is strictly positive. Hence \(H_p(x)\) is strictly increasing in \(p\). If \(p_2>p_1\), then
\[
H_{p_2}(r_{p_1+2}(R))>H_{p_1}(r_{p_1+2}(R))=\frac{M_1}{M_2}.
\]
Since \(H_{p_2}\) is strictly increasing in its spatial argument, its unique level point lies to the left. This proves \(r_{p_2+2}(R)<r_{p_1+2}(R)\), and in particular \(r_{n+1}(R)<r_n(R)\).

For the high-dimensional asymptotic, let \(\delta_p=r_{p+2}(R)-R_1>0\), \(\alpha=M_1/M_2\), and \(q=R_1/(R_1+R)\in(0,1)\). The exact source equation is equivalent to
\[
1-\left(1+\frac{\delta_p}{R_1}\right)^{-p}
=\alpha\left(\frac{R_1}{R_1+R+\delta_p}\right)^p
\left[1-\left(\frac{R_1+R+\delta_p}{R_2}\right)^p\right].
\]
The right-hand side is at most \(\alpha q^p\), so it tends to zero. Thus
\[
p\log\left(1+\frac{\delta_p}{R_1}\right)\to0,
\]
which implies \(p\delta_p/R_1\to0\). Divide the preceding exact identity by \(\alpha q^p\). The factor
\[
\left(\frac{R_1+R}{R_1+R+\delta_p}\right)^p
\]
tends to \(1\) because \(p\delta_p\to0\), while
\[
1-\left(\frac{R_1+R+\delta_p}{R_2}\right)^p\to1
\]
because \(R_1+R<R_2\). Finally,
\[
1-\left(1+\frac{\delta_p}{R_1}\right)^{-p}
\sim \frac{p\delta_p}{R_1}.
\]
Therefore
\[
\frac{p\delta_p}{R_1}\sim\alpha q^p,
\]
which is the claimed sharp asymptotic.

## Verification
The proof uses only the exact implicit interface equations supplied by the primary source, a positive-integral representation, differentiation under finite positive integrals, and elementary asymptotics. The ordering argument is uniform for real \(p\ge0\), so the transition from the logarithmic \(n=2\) formula to the power-law \(n\ge3\) formula is included rather than treated as a separate numerical case. The asymptotic is derived from an exact identity; no finite-dimensional experiment is used to infer the \(n\to\infty\) statement.

## Relationship to prior work
Chuah proves existence and uniqueness of the two concentric free boundaries in the annular problem, gives the explicit equations determining their radius separately for \(n=2\) and \(n\ge3\), studies sensitivity to the geometric and boundary parameters, and proves convergence to the adjacent model as the interaction distance tends to zero. The cross-dimensional order \(r_{n+1}(R)<r_n(R)\) and the sharp \(n\to\infty\) boundary-layer law above are not stated there.

The foundational long-range segregation work of Caffarelli, Patrizi, and Quitalo concerns existence and free-boundary structure for the general model. The higher-dimensional work of Chuah and Torres concerns regular and singular free-boundary geometry rather than an annular dimension sequence. Soave, Tavares, and Zilio study a different variational optimal-partition problem and obtain uniform spatial Lipschitz estimates as its distance parameter tends to zero; that result does not determine this annular interface location or its dependence on ambient dimension.

## Limitations
The result is specific to the rotationally invariant two-species annular limit and keeps \(M_1,M_2,R_1,R_2,R\) fixed while varying \(n\). The sharp asymptotic uses the strict gap \(R_1+R<R_2\). No assertion is made about the degenerate endpoint \(R_1+R=R_2\), nonradial perturbations of the annulus, more than two populations, other nonlocal interaction functionals, or the finite-competition system before the segregation limit.

## References
1. H. Chuah, *On Two Species Long Range Segregation in an Annular Domain*, arXiv:2610.02141v1 (2026).
2. L. A. Caffarelli, S. Patrizi, V. Quitalo, *On a long range segregation model*, J. Eur. Math. Soc. 19 (2017), 3575–3628, DOI: 10.4171/JEMS/747.
3. H. Chuah, M. Torres, *The Free Boundary in a Higher-Dimensional Long-Range Segregation Model*, arXiv:2605.07043v1 (2026).
4. N. Soave, H. Tavares, A. Zilio, *Free boundary problems with long-range interactions: uniform Lipschitz estimates in the radius*, Math. Ann. 386 (2023), 551–585, DOI: 10.1007/s00208-022-02406-8.
