# Cubic zonal interpolation on type-A roots and the unique eleven-vertex orthogonality resonance

## Finding

For every integer \(m\ge4\), put \(V_m=\{z\in\mathbb R^m:\sum_{i=1}^m z_i=0\}\), with its Euclidean metric, and select the \(N=\binom m2\) positive normalized type-\(A_{m-1}\) roots
\[
x_{ij}=(e_i-e_j)/\sqrt2,\qquad 1\le i<j\le m.
\]
Let \(\mathcal H_3(V_m)\) be the complex Hilbert space of degree-three homogeneous harmonic polynomials on \(V_m\), restricted to its unit sphere, with probability surface measure. Let \(E_m h=(h(x_{ij}))_{i<j}\), and set \(G_m=E_m E_m^*\), acting on complex edge data with the ordinary counting inner product.

Let \(B\) be the oriented vertex-edge incidence matrix of the complete graph on \(m\) vertices, with column \(e_i-e_j\) for edge \(i<j\). Define the orthogonal projectors
\[
P_{\mathrm{cut}}=\frac1m B^*B,\qquad P_{\mathrm{cyc}}=I-P_{\mathrm{cut}}.
\]
Then the **complete degree-three sampling spectrum** is
\[
\boxed{G_m=\lambda_{\mathrm{cyc}}P_{\mathrm{cyc}}+\lambda_{\mathrm{cut}}P_{\mathrm{cut}}},
\]
where
\[
\boxed{\lambda_{\mathrm{cyc}}=\frac{(m-1)(m+1)(m+3)}8},
\qquad
\boxed{\lambda_{\mathrm{cut}}=\frac{(m-1)(m-2)(m-3)(m+3)}{48}}.
\]
The two eigenspaces have dimensions \((m-1)(m-2)/2\) and \(m-1\), respectively; coincident eigenvalues are combined at \(m=11\). In particular, **every** complex assignment to the \(N\) chosen roots has a cubic harmonic interpolant. On the full antipodal root system, the attainable data are exactly the odd assignments \(y_{ji}=-y_{ij}\).

The precise squared spectral condition number is
\[
\boxed{\kappa(G_m)=\max\left\{\frac{(m-2)(m-3)}{6(m+1)},\frac{6(m+1)}{(m-2)(m-3)}\right\}\ge1,
\]
with equality **if and only if** \(m=11\). At this unique parameter, the \(55\) cubic zonal harmonics centered at the chosen roots are pairwise orthogonal and have squared norm \(210\). Thus \(G_{11}=210I_{55}\), and the resulting \(55\) normalized functions form an orthonormal system inside the \(210\)-dimensional degree-three harmonic space, not a basis of that whole space.

For any edge data \(y\in\mathbb C^N\), the unique *minimum-\(L^2\)-norm* interpolant and its exact squared norm are
\[
h_y(z)=\sum_{i<j}\left(\frac{(P_{\mathrm{cyc}}y)_{ij}}{\lambda_{\mathrm{cyc}}}+\frac{(P_{\mathrm{cut}}y)_{ij}}{\lambda_{\mathrm{cut}}}\right)Z_m(z,x_{ij}),
\]
\[
\boxed{\|h_y\|_{L^2}^2=\frac{\|P_{\mathrm{cyc}}y\|_2^2}{\lambda_{\mathrm{cyc}}}+\frac{\|P_{\mathrm{cut}}y\|_2^2}{\lambda_{\mathrm{cut}}}},
\]
where the homogeneous cubic zonal kernel is
\[
Z_m(z,x)=\frac{(m-1)(m+3)}6\Big((m+1)\langle z,x\rangle^3-3\langle z,x\rangle\|z\|^2\Big),\quad z\in V_m,\ \|x\|=1.
\]

## Assumptions and scope

The integer condition is \(m\ge4\). Roots are Euclidean-normalized by \(\sqrt2\), the sphere has normalized (probability) surface measure, and the data-space norm is ordinary unnormalized counting \(\ell^2\). The harmonic degree is exactly three, rather than all degrees through three. Complex-valued data are allowed. The full \(m(m-1)\)-point root set is antipodal; only \(\binom m2\) representatives are used to avoid the forced sign redundancy of odd harmonics. The matrix \(G_m\) is the data-space Gram operator, so the interpolation operator's nonzero singular values are \(\sqrt{\lambda_{\mathrm{cyc}}}\) and \(\sqrt{\lambda_{\mathrm{cut}}}\).

## Proof

**1. Reproducing kernel and exact normalization.** The dimension of \(V_m\) is \(d=m-1\). The standard probability-sphere addition theorem for homogeneous degree-three spherical harmonics gives
\[
Z_3^{(d)}(u,v)=\frac{d(d+4)}6\left((d+2)\langle u,v\rangle^3-3\langle u,v\rangle\right)
\]
for unit vectors \(u,v\), with diagonal value \(d(d-1)(d+4)/6=\dim\mathcal H_3(\mathbb R^d)\). Its homogeneous extension is \(Z_m(z,x)\) in the finding. Independently, this extension is harmonic because, for a unit \(x\in V_m\),
\[
\Delta_{V_m}\langle z,x\rangle^3=6\langle z,x\rangle,
\quad
\Delta_{V_m}(\|z\|^2\langle z,x\rangle)=2(d+2)\langle z,x\rangle.
\]
Thus the zonal functions lie in the stated harmonic space, and the addition theorem identifies their inner products as evaluations of \(Z_m\).

**2. Edge geometry gives an incidence Gram.** Two distinct selected roots have inner product \(0\) if their edges are disjoint, or \(\pm1/2\) if their edges share a vertex. The sign agrees with that of the corresponding off-diagonal entry of \(B^*B\). Since the degree-three kernel is odd, its value on disjoint edges is zero, while its value on a shared-vertex pair is \(\pm a_m\), with
\[
a_m=Z_3^{(m-1)}(1/2)=\frac{(m-1)(m+3)(m-11)}{48}.
\]
The diagonal is
\[
k_m=Z_3^{(m-1)}(1)=\frac{(m-1)(m-2)(m+3)}6.
\]
Because \((B^*B)_{ee}=2\), the entire Gram matrix, not merely its diagonal or row sums, is
\[
G_m=(k_m-2a_m)I+a_mB^*B.
\]

**3. The two exact spectral sectors.** Complete-graph incidence satisfies \(BB^*=mI-J\). Hence \(P_{\mathrm{cut}}=B^*B/m\) is an orthogonal projection of rank \(m-1\); its orthogonal complement is the cycle space of dimension \(N-m+1=(m-1)(m-2)/2\). Substituting \(B^*B=mP_{\mathrm{cut}}\) and factoring gives
\[
k_m-2a_m=\frac{(m-1)(m+1)(m+3)}8,
\]
\[
k_m+(m-2)a_m=\frac{(m-1)(m-2)(m-3)(m+3)}{48}.
\]
Both are strictly positive for every \(m\ge4\), proving the spectrum and invertibility of \(G_m\).

**4. Every data vector is interpolated, with sharp minimum energy.** Since \(G_m=E_mE_m^*\) is invertible, \(E_m\) is onto. Its Moore–Penrose right inverse is \(E_m^*G_m^{-1}\). The inverse is the displayed projector sum. The reproducing property gives \(E_m^*w=\sum_{i<j}w_{ij}Z_m(\cdot,x_{ij})\), proving the formula for \(h_y\). It is perpendicular to \(\ker E_m\), hence has the smallest harmonic \(L^2\) norm among all solutions. Moreover
\[
\|h_y\|^2=\langle G_m^{-1}y,E_mE_m^*G_m^{-1}y\rangle
=\langle y,G_m^{-1}y\rangle,
\]
which yields the exact orthogonal decomposition of the norm. The antipodal assertion follows from the odd homogeneity of every cubic harmonic and surjectivity onto one choice per pair.

**5. Unique perfect conditioning.** From the factored eigenvalues,
\[
\frac{\lambda_{\mathrm{cut}}}{\lambda_{\mathrm{cyc}}}=\frac{(m-2)(m-3)}{6(m+1)}.
\]
It equals one precisely when \((m-2)(m-3)=6(m+1)\), equivalently \(m(m-11)=0\); for integers \(m\ge4\), only \(m=11\) qualifies. A positive-definite Gram matrix has condition number at least one, with equality exactly when it is scalar. At \(m=11\), \(a_{11}=0\), \(k_{11}=210\), and therefore \(G_{11}=210I_{55}\). These identities prove the orthogonality, the unique sharp conditioning claim, and the especially simple interpolation formula \(h_y=210^{-1}\sum_{i<j}y_{ij}Z_{11}(\cdot,x_{ij})\).

## Verification

The independent symbolic expression for the degree-three addition kernel and the incidence identity were factored exactly in SymPy. The standalone `checker.py` verifies the polynomial factorizations and the resonance equation symbolically. It then checks exact incidence-projector identities and exact reconstruction and norm identities for \(m=4,\ldots,20,23,29\); for \(m\le14\), it also constructs every Gram entry directly from root inner products and the Gegenbauer cubic and compares the resulting rational matrix entrywise with the incidence formula. It verifies \(G_{11}=210I_{55}\). The script completed \(26775\) checks with no failures. These finite checks corroborate, but do not replace, the all-integer argument in the proof. Reproduce with `python3 checker.py` using Python 3 and SymPy.

## Relationship to prior work

Dai and Xu, *Spherical Harmonics* (first arXiv version, April 9, 2013), establish the probability-normalized addition formula and general zonal interpolation framework used here. Those results supply the kernel but do not compute its edge-incidence spectrum on type-\(A\) roots or the unique eleven-vertex orthogonality parameter. Barg, Glazyrin, Okoudjou, and Yu, *Finite two-distance tight frames* (first arXiv version February 14, 2014), treat two-distance frames and the strongly regular graph connection; their complete-graph example uses projected sums \(e_i+e_j\), not cubic harmonic evaluations at normalized differences \(e_i-e_j\). Bannai, Zhao, Zhu, Zhu, and Zhu, *Half of an antipodal spherical design* (first arXiv version October 29, 2017), study sign selections of root systems and harmonic-index design conditions; its \(A\)-series result is a balancing criterion, not a third-degree sampling-spectrum or conditioning classification.

The classical work of Delsarte, Goethals, and Seidel supplies the general spherical code and design background. An accessible full-text comparison of that older paper could not be completed, so an implicitly equivalent observation in classical spherical design or association-scheme literature remains a residual originality risk. The cut/cycle projector decomposition itself is standard graph linear algebra; the claimed contribution is its precise interaction with the degree-three zonal kernel, complete minimum-energy interpolation, and the unique orthogonality resonance for this natural family.

## Limitations

The theorem concerns only harmonic degree three, exact type-\(A\) root representatives, and probability-normalized spherical harmonics; it makes no claim for arbitrary perturbed nodes or other degrees. The complete harmonic space generally contains a nontrivial kernel of the evaluation map: surjectivity is **not** injectivity. The word “tight” at \(m=11\) refers to orthogonality of the \(55\) zonal functions within their span, not to a basis of the entire \(210\)-dimensional harmonic space. The exact result has not received independent external mathematical validation. Earlier literature could contain an equivalent computation under association-scheme or root-system terminology.

## References

1. F. Dai and Y. Xu, *Spherical Harmonics*, arXiv:1304.2585v1 (2013-04-09), particularly §§2–3. https://arxiv.org/pdf/1304.2585
2. A. Barg, A. Glazyrin, K. A. Okoudjou, and W.-H. Yu, *Finite two-distance tight frames*, arXiv:1402.3521v1 (2014-02-14), especially Proposition 2.2 and Theorem 1.2. https://arxiv.org/pdf/1402.3521
3. E. Bannai, D. Zhao, L. Zhu, Y. Zhu, and Y. Zhu, *Half of an antipodal spherical design*, arXiv:1710.10619v1 (2017-10-29), particularly §§2,4. https://arxiv.org/pdf/1710.10619
4. P. Delsarte, J. M. Goethals, and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388. https://doi.org/10.1007/BF03187604
