# Fifth-harmonic interpolation and single-point repair on simplex triangle-centroid orbits

## Finding
Let \(m\geq7\) be an integer and let \(V=\{x\in\mathbb R^m:\sum_i x_i=0\}\), of dimension \(m-1\). For every three-element subset \(S\subset\{1,\ldots,m\}\), put
\[
 x_S=\frac{\mathbf1_S-(3/m)\mathbf1}{\sqrt{3(m-3)/m}}\in S(V).
\]
These are the normalized centroids of the triangular faces of a regular \((m-1)\)-simplex. Let \(E_m\) evaluate **homogeneous complex spherical harmonics of degree five** on \(S(V)\) at all \(\binom m3\) points \(x_S\).

**Theorem.** For every integer \(m\geq7\), the evaluation \(E_m:\mathcal H_5(V)\to\mathbb C^{\binom m3}\) is surjective if and only if \(m\ne27\). At \(m=27\), the rank is \(2924\), and its image consists **exactly** of those data \((y_S)\) with \(\sum_{|S|=3}y_S=0\). All \(2925\) evaluations have exactly one linear relation, their sum. If any one centroid sample is removed and replaced by **any** of the \(27\) original simplex vertices (normalized in \(V\)), the resulting \(2925\)-node evaluation is surjective. This is a single-site repair of the otherwise unavoidable missing mean mode.

At the exceptional order, the unit-diagonal zonal Gram matrix \(K=(P_5(\langle x_S,x_T\rangle))\) has the exact eigenvalues
\[
0^{[1]},\quad (855/256)^{[26]},\quad (455/256)^{[324]},\quad (225/256)^{[2574]}.
\]
Brackets indicate multiplicities. Thus its Moore–Penrose inverse is explicit from the four orthogonal Johnson eigenspace projectors, and every permissible data vector has a minimum-\(L^2\)-norm harmonic interpolant.

## Assumptions and scope
The sphere \(S(V)\) is the unit sphere in the real inner-product space \(V\). Harmonics are complex-valued restrictions of homogeneous degree-five polynomials annihilated by the Laplacian on \(V\). Spherical \(L^2\) uses probability surface measure. The simplex has \(m\) vertices; a triangular face has three vertices. The points \(x_S\) are distinct for \(m\ge7\). Only degree five, complete triangular-face centroid orbits, and the specifically stated one-vertex replacement are claimed. The excluded case \(m=6\) is antipodal: degree-five evaluation has rank ten, not twenty.

Let \(\mathcal U_i\), \(0\leq i\leq3\), be the standard orthogonal Johnson-scheme components of complex functions on three-element subsets of an \(m\)-set: \(\mathcal U_0\) is constant, \(\mathcal U_1\) consists of point-incidence contrasts, \(\mathcal U_2\) is the new pair-incidence component, and \(\mathcal U_3\) is their orthogonal complement. Their dimensions are \(\binom mi-\binom m{i-1}\), with \(\binom m{-1}=0\). Let \(Q_i\) denote their orthogonal projections.

## Proof
**1. Harmonic Gram kernel.** For three-subsets \(S,T\), with \(r=|S\cap T|\), direct normalization gives
\[
\langle x_S,x_T\rangle=\frac{mr-9}{3(m-3)}=:t_r.
\]
The probability-normalized spherical harmonic addition formula in dimension \(m-1\) gives the unit-diagonal Gram kernel
\[
P_5(t)=\frac{t\big((m+3)(m+5)t^4-10(m+3)t^2+15\big)}{m(m-2)}.
\]
If \(D_m=\dim\mathcal H_5(V)=\binom{m+3}{5}-\binom{m+1}{3}\), then the actual evaluation Gramian for the probability-normalized domain inner product is \(E_mE_m^*=D_mK\). Hence \(K\) and \(E_m\) have the same rank.

**2. Exact Johnson-sector eigenvalues.** Write the four-valued function \(P_5(t_r)\), for \(r=0,1,2,3\), in the Newton basis \(\sum_{j=0}^3a_j\binom rj\). For the matrix with entries \(\binom{|S\cap T|}{j}\), the scalar on \(\mathcal U_i\) is zero for \(j<i\) and equals
\[
\binom{3-i}{j-i}\binom{m-j-i}{3-j}\qquad (j\ge i).
\]
This follows from the ranks of subset-incidence maps, or by directly counting common supersets and restricting to the nested incidence orthogonal differences. Taking the Newton finite differences of the displayed \(P_5(t_r)\) and simplifying yields the complete four-sector spectrum:
\[
\begin{aligned}
\lambda_0={}&\frac{m(m-27)^2(m-6)^2(m-4)(m+3)}{162(m-3)^4(m-2)},\\
\lambda_1={}&\frac{mA(m)}{486(m-3)^5(m-2)},\\
\lambda_2={}&\frac{10m(m-6)(m+3)B(m)}{81(m-3)^5(m-2)},\\
\lambda_3={}&\frac{10m^2(m+3)C(m)}{81(m-3)^5(m-2)},
\end{aligned}
\]
where
\[
\begin{aligned}
A(m)={}&m^7-12m^6+1241m^5-30837m^4+272970m^3\\
&-880875m^2+131220m+2755620,\\
B(m)={}&m^4-27m^3+254m^2-594m-648,\\
C(m)={}&5m^3-47m^2+648.
\end{aligned}
\]
The four eigenvalues respectively have multiplicities \(1\), \(m-1\), \(\binom m2-m\), and \(\binom m3-\binom m2\). These identities are exact polynomial identities, not inferred from sampling finitely many \(m\).

**3. Exhaustive exclusion of other integral singularities.** For an integer \(m\), the values of \(A(m)\) modulo \(13\), as \(m\) runs through residues \(0,\ldots,12\), are
\[
10,3,11,9,12,12,12,10,7,9,6,2,1.
\]
Likewise the values of \(B(m)\) modulo \(7\) are \(3,1,2,6,2,3,4\), and the values of \(C(m)\) modulo \(11\) are \(10,1,5,8,7,10,3,5,2,2,2\). All are nonzero; each list checks **all** residues modulo its modulus. Thus \(\lambda_1,\lambda_2,\lambda_3\) cannot vanish at any integer \(m\ge7\). The factorization of \(\lambda_0\) shows that it vanishes in that domain exactly at \(m=27\). Because \(K\) is a positive semidefinite Gram matrix, all its other eigenvalues are positive. This proves surjectivity except at \(27\), and proves that the nullspace at \(27\) consists precisely of constants.

At \(m=27\) the kernel entries for overlap \(r=0,1,2,3\) simplify to \((-1/512,0,21/512,1)\). The four eigenvalues are exactly those displayed in the theorem and their multiplicities sum to \(2925\). In particular, the only linear dependence among the row functionals is \(\sum_SE_{m,S}=0\). The image is the codimension-one hyperplane \(\sum_Sy_S=0\), and the other \(2924\) row functionals remaining after any single deletion are linearly independent.

**4. Repair by one simplex vertex.** A concrete nonzero degree-five harmonic vanishing at every triangle centroid when \(m=27\) is needed to prove independence of the replacement row. For \(x\in V\), define \(p_j(x)=\sum_{i=1}^m x_i^j\) and \(R(x)=\|x\|^2\). Set
\[
H_m(x)=p_5(x)-\frac{10(m-1)}{m(m+5)}R(x)p_3(x).
\]
The tangent Laplacian \(\Delta_V=\sum_i\partial_i^2-m^{-1}(\sum_i\partial_i)^2\) satisfies \(\Delta_Vp_5=20(m-1)p_3/m\), \(\Delta_Vp_3=0\) on \(V\), and \(\Delta_V(Rp_3)=2(m+5)p_3\). Therefore \(\Delta_VH_m=0\); it is a genuine homogeneous harmonic of degree five.

For \(y_U=\mathbf1_U-(k/m)\mathbf1\), with \(|U|=k\), direct substitution gives
\[
H_m(y_U)=\frac{k(k-m)(2k-m)\big(12k^2-12km+m^2+5m\big)}{m^3(m+5)}.
\]
At \(m=27\) and \(k=3\), this is zero; homogeneity gives \(H_{27}(x_S)=0\) for all sampled centroids. At \(m=27\), \(k=1\), it equals \(7475/13122\ne0\) before radial normalization, so \(H_{27}\) does not vanish at any normalized simplex vertex. Consequently evaluation at any simplex vertex is not in the span of the triangle-centroid evaluation functionals. Combining it with the \(2924\) independent rows left after removing any one centroid produces \(2925\) independent rows. The repair assertion follows.

**5. Reproducible interpolation.** At \(m=27\), write \(K^+=(256/855)Q_1+(256/455)Q_2+(256/225)Q_3\). For any data vector \(y\) of zero sum, the unique minimum-norm interpolating function in \(\mathcal H_5(V)\) is
\[
h_y(z)=\sum_{S,T}(K^+)_{ST}y_TP_5(\langle z,x_S\rangle),
\qquad
\|h_y\|_{L^2}^2=\frac1{D_{27}}\langle y,K^+y\rangle.
\]
For \(m\ne27\), the same formula with \(K^{-1}\) and arbitrary \(y\) applies. This follows directly from the reproducing-kernel normal equations, including their normalization by \(D_m\).

## Verification
Running `python3 VERIFY.py` (requires Python 3 and SymPy) recomputes \(P_5\) from Gegenbauer polynomials, rederives the four eigenvalues from finite differences and incidence eigenvalues, and checks the displayed factorization as identities in the symbol \(m\). It checks every residue in the three modular exclusions; calculates exact characteristic polynomials of the full centroid Gram matrices for each \(m=6,7,8,9,10,11\); verifies the exceptional kernel and trace at \(m=27\); and recomputes the concrete harmonic's centroid/vertex evaluations. All checks passed. These finite examples are corroboration; the symbolic identities and residue exhaustions provide the general proof.

## Relationship to prior work
Dai and Xu (arXiv:1304.2585, first public posting 2013-04-09) establish the reproducing-kernel and zonal Gegenbauer framework; it does not treat the specified simplex triangle-centroid sample geometry. Khalid, Kennedy and McEwen (arXiv:1403.4661, 2014-03-19) motivate sharp spherical-harmonic sampling but study an iso-latitude scheme on the two-sphere, not these high-dimensional centroid orbits. Burcroff (2017, *Johnson Schemes and Certain Matrices with Integral Eigenvalues*, especially Corollary 7.5) supplies a generic spectral formula for **every** Johnson intersection matrix. That broad algebraic identity is an important computational predecessor: specialized to the present kernel it yields the unreduced eigenvalue expressions. It does not state the degree-five harmonic arithmetic exception, all-integer nonvanishing result, or off-orbit one-vertex repair. The latter uses the additional explicitly harmonic witness \(H_m\). There may be an earlier equivalent instance in association-scheme or spherical-design literature; the novelty assessment is subject to independent review.

## Limitations
The theorem does not assert uniqueness of an interpolating harmonic (the harmonic source space is much larger than the sample space). At \(m=27\), zero-sum data are necessary and sufficient only for the **original** centroid orbit, not for arbitrary perturbations. The replacement claim concerns any single normalized simplex vertex, not arbitrary new points. No conclusions for other degrees, other face sizes, or general weighted sampling arrays are claimed.

## References
1. F. Dai and Y. Xu, *Spherical Harmonics*, arXiv:1304.2585v1 (first posted 2013-04-09), Section 2, reproducing kernels and addition formula. https://arxiv.org/abs/1304.2585
2. Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661v1 (first posted 2014-03-19). https://arxiv.org/abs/1403.4661
3. A. Burcroff, *Johnson Schemes and Certain Matrices with Integral Eigenvalues* (2017), Theorem 1.1 and Corollary 7.5. https://math.uchicago.edu/~may/REU2017/REUPapers/Burcroff.pdf
4. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical Codes and Designs*, Geometriae Dedicata **6** (1977), 363–388, DOI:10.1007/BF03187604 (bibliographic comparison; full text not inspected).
