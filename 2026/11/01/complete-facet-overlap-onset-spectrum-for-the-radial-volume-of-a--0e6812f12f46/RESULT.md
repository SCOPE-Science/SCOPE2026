# Complete facet-overlap onset spectrum for the radial volume of a regular simplex

## Finding
Let \(d\ge3\) be an integer. Let \(S_d\subset\mathbb R^d\) be a regular Euclidean simplex with centroid at the origin and inradius one; let \(X\) be uniform in its \(d\)-dimensional volume, and put \(R=\|X\|_2\). For each \(1\le k\le d\), define
\[
\rho_{d,k}=\sqrt{\frac{dk}{d-k+1}},\quad a_{d,k}=\frac d{d-k+1},\quad g_{d,k}=\left(\frac{d+1}{d}\right)^{k-1}\frac{d-k+1}{d},\quad p_{d,k}=\frac{d+k}{2}.
\]
The strictly ordered radii \(1=\rho_{d,1}<\cdots<\rho_{d,d}=d\) are precisely the first radii at which a ball about the centroid can meet the simultaneous exterior of any prescribed \(k\) facets. More strongly, the common \(k\)-fold exterior-overlap volume \(C_{d,k}(t)\) is zero for \(t\le\rho_{d,k}\), positive for \(t>\rho_{d,k}\), and satisfies the **sharp onset law**
\[
C_{d,k}(\rho_{d,k}+\varepsilon)
= c_{d,k}\varepsilon^{p_{d,k}}+o(\varepsilon^{p_{d,k}}),\qquad
c_{d,k}=\frac{\pi^{(d-k)/2}(2\rho_{d,k})^{(d+k)/2}}{(2a_{d,k})^k\sqrt{g_{d,k}}\,\Gamma((d+k)/2+1)}.
\]
These coefficients are strictly positive and explicit for **all** \(1\le k\le d\), including the terminal vertex regime.

The exact cumulative distribution of \(R\) is the following finite inclusion-exclusion integral:
\[
\Pr(R\le t)=\frac{\kappa_dt^d+\sum_{k=1}^{d}(-1)^k\binom{d+1}{k}C_{d,k}(t)}{V_d},\qquad t\ge0,
\]
where \(\kappa_m=\pi^{m/2}/\Gamma(m/2+1)\), \(V_d=d^{d/2}(d+1)^{(d+1)/2}/d!\), and the integrals for \(C_{d,k}\) are specified below. In particular the distribution is zero below zero and identically one for \(t\ge d\). The signed new inclusion-exclusion contribution activated at \(\rho_{d,k}\) is exactly \((-1)^k\binom{d+1}{k}c_{d,k}\varepsilon^{p_{d,k}}/V_d+o(\varepsilon^{p_{d,k}})\).

## Assumptions and scope
There are \(d+1\) unit outward facet normals \(u_i\), with \(\langle u_i,u_j\rangle=-1/d\) for \(i\ne j\); the regular simplex is \(S_d=\{x:\langle u_i,x\rangle\le1\ \text{for all }i\}\). The exterior of facet \(i\) means \(\langle u_i,x\rangle>1\), with equality immaterial to volume. For a subset of \(k\) distinct facets, \(C_{d,k}(t)\) denotes the volume of their common exterior inside \(B_t(0)\). It depends on \(k\), not on the subset, by simplex symmetry. The \(d+1\)-fold exterior is empty because \(\sum_i u_i=0\). Define \(v_+^0=\mathbf1_{\{v>0\}}\) when a zero power occurs in an integral.

## Proof
**1. Simplex normalization.** The standard regular-simplex Gram relations give \(\sum_{i=1}^{d+1}u_i=0\), and its opposite vertices are \(-d u_i\). Their mutual distance is \(\sqrt{2d(d+1)}\). Hence \(\operatorname{Vol}(S_d)=V_d\), as displayed, and the maximum vertex radius is \(d\). Convexity of the Euclidean norm gives \(\|x\|\le d\) for all \(x\in S_d\).

**2. Exact prescribed-overlap integral.** For \(1\le k\le d\) form the \(k\times k\) Gram matrix and its inverse:
\[
G_{d,k}=\frac{d+1}{d}I_k-\frac1d\mathbf1\mathbf1^\top,\qquad
G_{d,k}^{-1}=\frac d{d+1}I_k+\frac d{(d+1)(d-k+1)}\mathbf1\mathbf1^\top.
\]
Direct spectral decomposition yields \(\det G_{d,k}=g_{d,k}\) and \(G_{d,k}^{-1}\mathbf1=a_{d,k}\mathbf1\). Define \(q_{d,k}(y)=y^\top G_{d,k}^{-1}y\). The affine coordinate change \(y_i=\langle u_i,x\rangle-1\ge0\), together with orthogonal \(z\in(\operatorname{span}\{u_i\})^\perp\), has volume Jacobian \(g_{d,k}^{-1/2}\) and exact radial identity
\[
\|x\|^2=\rho_{d,k}^2+2a_{d,k}\sum_{i=1}^k y_i+q_{d,k}(y)+\|z\|^2.
\]
Consequently, for every \(t\ge0\),
\[
C_{d,k}(t)=\frac{\kappa_{d-k}}{\sqrt{g_{d,k}}}\int_{[0,\infty)^k}\left(t^2-\rho_{d,k}^2-2a_{d,k}\sum_{i=1}^k y_i-q_{d,k}(y)\right)_+^{(d-k)/2}\,dy.
\]
For \(k=d\), interpret the exponent-zero positive part as the indicator that the parenthesis is positive. This formula uses an ordinary \(k\)-dimensional integral with compact support, and no numerical approximation is needed.

**3. Sharp threshold and coefficient.** Since \(q_{d,k}\) is positive definite and the linear term is nonnegative on the orthant, the integral vanishes when \(t\le\rho_{d,k}\) and is strictly positive when \(t>\rho_{d,k}\). Set \(T=t^2-\rho_{d,k}^2\) and \(y_i=(T/(2a_{d,k}))v_i\). After pulling out \(T^{(d+k)/2}\), the remaining domain and integrand converge to the compact simplex integral
\[
\int_{v_i\ge0,\,\sum v_i\le1}(1-\sum v_i)^{(d-k)/2}\,dv
=\frac{\Gamma((d-k)/2+1)}{\Gamma((d+k)/2+1)}.
\]
The discarded quadratic term is nonnegative; the rescaled integrands are bounded by the last integrable integrand (or by one when \(k=d\)), so dominated convergence applies for every \(1\le k\le d\). Using the definition of \(\kappa_{d-k}\) gives
\[
C_{d,k}(t)\sim\frac{\pi^{(d-k)/2}}{(2a_{d,k})^k\sqrt{g_{d,k}}\Gamma((d+k)/2+1)}T^{(d+k)/2}.
\]
Since \(T\sim2\rho_{d,k}\varepsilon\) when \(t=\rho_{d,k}+\varepsilon\), the announced positive coefficient follows. Finally \(\rho_{d,k}^2=dk/(d-k+1)\) is strictly increasing with \(k\).

**4. Radial distribution.** The complement of the simplex is the union of its \(d+1\) open facet exteriors. Finite inclusion-exclusion inside \(B_t(0)\) gives the exact CDF; the intersection of all \(d+1\) exteriors is impossible, so the sum terminates at \(k=d\). Each term for \(k\) is zero before the corresponding threshold and has the sharp signed onset stated above. This proves all assertions.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and SymPy. It checks the Gram inverse, determinant, nearest-point distance, monotone thresholds in dimensions 2 through 15, and independent elementary circular/spherical cap coefficients; 586 individual checks passed. Exact arithmetic verifies the matrix identities; three small-radius numerical checks corroborate the circle-segment limit. The infinite-dimensional-index statement is proved analytically, not by finite tests.

For \(d=3,k=1\), the three-dimensional spherical-cap identity \(C_{3,1}(t)=\pi(t-1)^2(2t+1)/3\) gives \(c_{3,1}=\pi\), agreeing with the general formula. For \(d=2,k=1\), the circular-segment formula \(t^2\arccos(1/t)-\sqrt{t^2-1}\) gives \(c_{2,1}=4\sqrt2/3\). (The main theorem is stated for \(d\ge3\); these lower-dimensional checks test the general algebra.)

## Relationship to prior work
Dirksen (2015) studied sharp volumes of affine sections of regular simplices; its principal results concern sections of prescribed dimension and distance rather than intersection with concentric Euclidean balls and all exterior-facet overlap onsets. Baci--Kabluchko--Prochno--Sonnleitner--Thäle (2020) studied the Euclidean and other norm distributions of a uniform point in a centered simplex in the **high-dimensional limit**; the present result gives finite-dimensional boundary thresholds and exact gamma coefficients. Arman--Kaire--Prymak (2025) derived one- and two-cap union bounds for spherical caps centered at regular-simplex vertices, noting the first triple-overlap threshold. A separate published calculation extends their formula through triple overlaps with a sharp triple onset; it does not supply all \(k\) **ball-volume** overlap contributions and coefficients, including the final vertex regime. The thresholds can also be derived from standard Gram and face-distance geometry; novelty is not claimed for their values alone.

## Limitations
The asserted formula is a finite integral representation, not an elementary closed-form density for every dimension. No optimization of cap-body covering numbers, generic-simplex extension, or asymptotics as \(d\to\infty\) is claimed. Literature comparisons cannot certify worldwide historical priority; the precise all-depth volume coefficients remain the claim subject to independent scrutiny.

## References
1. H. Dirksen, *Sections of the regular simplex -- Volume formulas and estimates*, arXiv:1509.06408 (first public 21 September 2015), https://arxiv.org/abs/1509.06408.
2. A. Baci, Z. Kabluchko, J. Prochno, M. Sonnleitner, C. Thäle, *Limit theorems for random points in a simplex*, arXiv:2005.04911 (first public 11 May 2020), https://arxiv.org/abs/2005.04911.
3. A. Arman, J. S. Kaire, A. Prymak, *Hadwiger's conjecture for cap bodies*, arXiv:2510.25968 (first public 29 October 2025), https://arxiv.org/abs/2510.25968.
4. *Exact third-order union formula at the first multiple-overlap threshold for simplex-centred spherical caps*, publicly accessible research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-third-order-union-formula-at-the-first-multiple-overlap-th--e4ea7f0caeb7.
