# Exact Hilbert–Schmidt coefficients and the two-dimensional logarithmic anomaly for multivariate Rhaly operators

## Finding

For every fixed integer \(d\ge1\), every coordinate \(1\le j\le d\), and every complex sequence \(a=(a_N)_{N\ge0}\), the homogeneous Rhaly expression on the Drury–Arveson space has a Hilbert–Schmidt extension exactly when
\[
  \sum_{N=0}^\infty A_d(N)|a_N|^2<\infty,
\]
where
\[
 A_d(N)=\begin{cases}
 N+1,&d=1,\\[2pt]
 (N+1)H_{N+1},&d=2,\\[2pt]
 \dfrac{N+1}{d-2}\left(\binom{N+d-1}{d-2}-1\right),&d\ge3,
 \end{cases}
 \qquad H_m=\sum_{k=1}^m\frac1k.
\]
Its squared Hilbert–Schmidt norm equals this series exactly. In fact, the coefficient-to-operator map is an isometric linear embedding of the weighted coefficient space into the Hilbert–Schmidt ideal, and different homogeneous output rows are Hilbert–Schmidt orthogonal.

A sharp endpoint consequence is that for \(a_N=(N+1)^{-s}[\log(e+N)]^{-\gamma}\), with real \(s,\gamma\), the Hilbert–Schmidt condition is:

- \(d=1\): \(s>1\), or \(s=1\) and \(\gamma>\tfrac12\);
- \(d=2\): \(s>1\), or \(s=1\) and \(\gamma>1\);
- \(d\ge3\): \(s>\tfrac d2\), or \(s=\tfrac d2\) and \(\gamma>\tfrac12\).

At the critical pure-power exponent (\(\gamma=0\)), the squared Hilbert–Schmidt norm of the output-degree-\(K\) truncation is asymptotic to \(\log K\) for \(d=1\), to \(\tfrac12(\log K)^2\) for \(d=2\), and to \(\log K/((d-2)(d-2)!)\) for \(d\ge3\). The extra logarithm in precisely two variables is an exact dimensional anomaly.

## Assumptions and scope

Let \(H_d^2\) be the complex Drury–Arveson Hilbert space of holomorphic functions on the complex unit ball with reproducing kernel \((1-\langle z,w\rangle)^{-1}\). Its monomials are orthogonal and
\[\|z^\alpha\|^2=\frac{\alpha!}{|\alpha|!}.\]
For the orthogonal homogeneous expansion \(f=\sum_{m\ge0}f_m\), define the finite-output-degree operator
\[
 R_{j,a}^{[K]}f=\sum_{N=0}^K a_N\sum_{m=0}^N z_j^{N-m}f_m.
\]
This bounded finite-rank operator is defined for every complex coefficient sequence and every \(K\ge0\). By a Hilbert–Schmidt extension of the formal infinite expression we mean a bounded operator whose output coefficients agree with this formula on all polynomials (and therefore on the monomial basis). The definition is the homogeneous formulation of the Rhaly tuple, with no assumption that the formal infinite sum is initially bounded. All dimensions \(d\) are fixed finite positive integers; the statement does not assert a dimension-uniform result or any \(\mathcal S_p\) characterization for \(p\ne2\).

## Proof

Write \(w_\alpha=\alpha!/|\alpha|!\) and let \(e_\alpha=z^\alpha/\sqrt{w_\alpha}\) be the normalized monomial basis. Fix the output degree \(N\), an input multi-index \(\alpha\) of total degree \(m\le N\), and put \(r=m-\alpha_j\), the degree carried by the other \(d-1\) coordinates. There is exactly one output multi-index \(\beta=\alpha+(N-m)e_j\). The squared modulus of the resulting normalized matrix coefficient is
\[
 |a_N|^2\frac{w_\beta}{w_\alpha}
 =|a_N|^2\frac{\binom mr}{\binom Nr}.
\]
For \(d\ge2\), the number of choices of the other coordinates having total degree \(r\) equals \(\binom{r+d-2}{d-2}\). For fixed \(N,r\), summing over the possible input degrees \(r\le m\le N\) and using the hockey-stick identity gives
\[
 \sum_{m=r}^N\frac{\binom mr}{\binom Nr}
 =\frac{\binom{N+1}{r+1}}{\binom Nr}
 =\frac{N+1}{r+1}.
\]
The full squared matrix-coefficient sum for output degree \(N\), divided by \(|a_N|^2\), is therefore
\[
 A_d(N)=(N+1)\sum_{r=0}^N\frac{1}{r+1}\binom{r+d-2}{d-2}\qquad(d\ge2).
\]
For \(d=2\) this is \((N+1)H_{N+1}\). For \(d\ge3\), the elementary identity
\[
 \frac1{r+1}\binom{r+d-2}{d-2}
 =\frac1{d-2}\binom{r+d-2}{d-3}
\]
and a second hockey-stick sum give
\[
 A_d(N)=\frac{N+1}{d-2}\left(\binom{N+d-1}{d-2}-1\right).
\]
When \(d=1\), only one input monomial appears in each degree \(0,\ldots,N\), giving \(A_1(N)=N+1\).

The operator \(R_{j,a}^{[K]}\) has output in the orthogonal direct sum of degrees at most \(K\). Summing squared matrix coefficients over the monomial basis and applying the just-derived identity proves
\[
 \|R_{j,a}^{[K]}\|_{\mathcal S_2}^2
 =\sum_{N=0}^K A_d(N)|a_N|^2.
\]
The degree-\(N\) pieces have pairwise orthogonal Hilbert–Schmidt inner products, because they have disjoint output-degree ranges. Thus the sequence of finite-row operators is Cauchy in \(\mathcal S_2\) precisely when the displayed infinite series converges; its limit has the required monomial coefficients. Conversely, the squared entries of any Hilbert–Schmidt operator agreeing with the formal expression on polynomials include exactly these nonnegative terms, so their total must be finite. This proves both necessity and sufficiency, uniqueness of the extension, exact norm equality, and the isometric embedding assertion. Symmetry of the monomial basis under coordinate permutations proves independence from \(j\).

The coefficients obey
\[
 A_1(N)\sim N,\qquad A_2(N)\sim N\log N,\qquad
 A_d(N)\sim\frac{N^{d-1}}{(d-2)(d-2)!}\quad(d\ge3).
\]
Substitution into the exact series and the integral test give all stated power–logarithm thresholds, including equality at the critical powers. For \(d=2\) at \(a_N=(N+1)^{-1}\), there is also the exact finite identity
\[
 \|R_{j,a}^{[K]}\|_{\mathcal S_2}^2
 =\sum_{k=1}^{K+1}\frac{H_k}{k}
 =\frac12\left(H_{K+1}^2+\sum_{k=1}^{K+1}\frac1{k^2}\right),
\]
obtained by symmetrizing the finite double harmonic sum. It yields the coefficient \(\tfrac12\) of the squared logarithm. For \(d\ge3\), the coefficient of the critical \(1/N\) summand is \(1/((d-2)(d-2)!)\), yielding the remaining critical limits.

## Verification

Run `python3 CHECKER.py` using the supplied standalone file. The actual run passed 577 exact-arithmetic assertions. These independently enumerate normalized monomial matrix entries in dimensions \(1\) through \(7\) and low output degrees, check coordinate symmetry and the closed combinatorial formulas, and test the two-variable harmonic-sum identity and the three-variable critical identity. Those finite checks serve as error detection; the infinite-dimensional and asymptotic claims follow from the analytic proof above, not from numerical extrapolation.

## Relationship to prior work

Pilla introduced the homogeneous Rhaly tuple on the Drury–Arveson space, studying operator boundedness, compactness and spectral properties. The present statement uses its homogeneous action but determines the entire Hilbert–Schmidt coefficient space and sharp critical logarithmic structure. Pilla's related coordinate Cesàro work concerns norms and spectral properties, not this ideal-norm identity. Bellavita, Dellepiane and Stylogiannis establish Schatten criteria for one-variable weighted Hardy and factorable Rhaly operators; those results do not themselves give the multivariable homogeneous-degree Hilbert–Schmidt coefficient \(A_d(N)\), its exceptional two-dimensional harmonic factor, or the exact critical truncation growth established here. The one-dimensional Rhaly Hilbert–Schmidt sum is classical and not asserted to be new. Available source comparisons do not establish definitive priority over all historical formulations.

## Limitations

The result addresses only the homogeneous Rhaly formula specified above on finite-dimensional Drury–Arveson spaces, and only the Hilbert–Schmidt ideal. It says nothing about non-Hilbert–Schmidt bounded extensions or the singular-value distribution in other ideals. The arXiv and literature searches were bounded; an older theorem on multivariate weighted triangular matrices or tensor decompositions might imply these formulas indirectly. The mathematical argument has not received independent validation.

## References

1. Michael R. Pilla, “Rhaly-Type Operators in Several Complex Variables,” arXiv:2606.25885v1 (first submitted 2026-06-24), https://arxiv.org/abs/2606.25885.
2. Michael R. Pilla, “Cesàro-Type Operators Acting on the Drury–Arveson Space,” arXiv:2606.24710v1 (2026), https://arxiv.org/abs/2606.24710.
3. G. Bellavita, V. Dellepiane, and N. Stylogiannis, “Rhaly operators on weighted Hardy spaces and factorable matrices,” arXiv:2606.15875v1 (2026), https://arxiv.org/abs/2606.15875.
4. G. Bellavita, V. Dellepiane, and N. Stylogiannis, “Boundedness, compactness and Schatten class for Rhaly matrices,” *Journal of the London Mathematical Society* (2025), DOI 10.1112/jlms.70304.
