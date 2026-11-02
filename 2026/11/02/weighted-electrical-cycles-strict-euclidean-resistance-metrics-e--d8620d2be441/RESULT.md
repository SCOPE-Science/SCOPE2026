# Weighted electrical cycles: strict Euclidean resistance metrics, exact simplex spectra, and a sharp continuum boundary

## Finding

**Theorem.** Let \(n\ge3\), and give the \(n\) edges of a cycle arbitrary positive electrical resistances \(r_0,\ldots,r_{n-1}\). Let \(R(v,w)\) be effective resistance between vertices, regarded as a distance, **not** its square root. Then:

1. \((V,R)\) has **strict \(2\)-negative type**. Thus its \(n\) vertices are isometric to an affinely independent Euclidean \((n-1)\)-simplex, and the minimum possible Euclidean embedding dimension of \(R\) is exactly \(n-1\), for every choice of positive edge resistances.
2. Set \(L=\sum_i r_i\). The circle \(\mathbb R/L\mathbb Z\), endowed with the resistance metric
   \[
   \rho_L(s,t)=\frac{\delta(L-\delta)}{L},\qquad \delta=(s-t)\bmod L\in[0,L),
   \]
   has **strict \(2\)-negative type on each nontrivial finite configuration** and supremal \(p\)-negative type exactly \(2\). An explicit universal isometric Hilbert embedding is given below. The weighted-cycle theorem is the restriction to its vertex positions.
3. For the unit-resistance cycle on \(n\) vertices, write \(s_j=\sin(\pi j/n)\), \(1\le j\le n-1\). The centered Euclidean Gram matrix \(B=-\tfrac12 J[R(i,j)^2]J\), where \(J=I-\mathbf1\mathbf1^{\mathsf T}/n\), has Fourier eigenvalues
   \[
   b_j=\frac{3-2s_j^2}{4n s_j^4}>0
   \]
   on the nonconstant characters, and its zero eigenvalue is simple. Its pseudodeterminant is exactly
   \[
   \det{}' B=\frac{2^{n-1}\bigl(T_n(2)-(-1)^n\bigr)}{3n^{n+3}},
   \]
   with \(T_n\) the first-kind Chebyshev polynomial. Hence the squared Euclidean \((n-1)\)-simplex volume is
   \[
   \operatorname{Vol}_{n-1}^2
   =\frac{2^{n-1}\bigl(T_n(2)-(-1)^n\bigr)}{3n^{n+2}((n-1)!)^2}.
   \]
4. Let \(\wp_n\) denote the supremal \(p\)-negative type of the unit-resistance \(n\)-cycle endowed with \(R\). Then \(\wp_3=+\infty\), whereas for every \(n\ge4\)
   \[
   2<\wp_n\le\frac{2\log2}{\log\bigl(2(n-2)/(n-1)\bigr)}.
   \]
   Consequently \(\lim_{n\to\infty}\wp_n=2\). In particular every **finite** weighted electrical cycle has some strict negative type above \(2\), while the full resistance circle does not admit any exponent above \(2\).

The limit statement does **not** claim monotonicity of \(\wp_n\) or an exact formula for its finite-\(n\) value. The bound is an explicit, generally nonoptimal, three-vertex obstruction.

## Assumptions and scope

Each edge is a resistor of positive real resistance, so conductance is its reciprocal. Effective resistance is the voltage drop needed for unit current between endpoints. All distances here use effective resistance itself, not graph shortest-path distance and not \(\sqrt R\). For a real symmetric zero-diagonal distance matrix \(d\), strict \(p\)-negative type means
\[
\sum_{i,j=1}^{m} a_i a_j d(x_i,x_j)^p<0
\quad\text{for every distinct }x_i\text{ and real }a\ne0\text{ with }\sum_i a_i=0.
\]
The supremal exponent is the supremum of those \(p\ge0\) for which the inequality with \(\le0\) holds for all finite subsets. The Euclidean Gram matrix \(B\) above uses squared **Euclidean** distances \(R^2\). The circle is a continuous metric space; the embedding dimension assertion pertains to finite vertex sets.

## Proof

**(a) Electrical reduction.** Choose an orientation and put vertex \(i\) at the circle coordinate \(t_i=r_0+\cdots+r_{i-1}\) modulo \(L\), with \(t_0=0\). Between two vertices, the two disjoint series arcs have resistances \(\delta\) and \(L-\delta\). Their parallel equivalent is \(\delta(L-\delta)/L\). This also proves that arbitrary positive cycle resistances are restrictions of one common circle metric.

**(b) Exact Fourier kernel.** For \(u\in[0,1]\), let \(h(u)=u^2(1-u)^2\), periodically extended. Its constant Fourier coefficient is \(1/30\), and for every integer \(m\ne0\) four integrations by parts give
\[
\int_0^1 h(u)\cos(2\pi m u)\,du=-\frac{3}{2\pi^4m^4}.
\]
Here the endpoint values and first derivatives vanish, while \(h^{(3)}(0)=-12\), \(h^{(3)}(1)=12\) and \(h^{(4)}=24\). Absolute convergence and \(h(0)=0\) yield the identity
\[
\rho_L(s,t)^2
=\frac{3L^2}{\pi^4}\sum_{m=1}^{\infty}
\frac{1-\cos(2\pi m(s-t)/L)}{m^4}.
\tag{1}
\]
Consequently
\[
\Phi_L(t)=L\sqrt{\frac{3}{2\pi^4}}
\Bigl(\frac{\cos(2\pi mt/L)}{m^2},\frac{\sin(2\pi mt/L)}{m^2}\Bigr)_{m\ge1}\in\ell^2(\mathbb N;\mathbb R^2)
\]
satisfies \(\|\Phi_L(s)-\Phi_L(t)\|_2=\rho_L(s,t)\) for all \(s,t\). This is an embedding of the resistance distance itself.

**(c) Strictness and dimension.** For distinct circle points \(t_1,\dots,t_m\) and real coefficients of zero sum, (1) gives
\[
\sum_{i,j}a_i a_j\rho_L(t_i,t_j)^2
=-\frac{3L^2}{\pi^4}\sum_{k\ge1}
\frac{\bigl|\sum_i a_i e^{2\pi\mathrm ikt_i/L}\bigr|^2}{k^4}.
\tag{2}
\]
If equality held, the moments for \(k=1,\dots,m-1\) would vanish, and the zeroth moment vanishes by assumption. Writing \(z_i=e^{2\pi\mathrm it_i/L}\), these \(m\) equations form an invertible Vandermonde system \((z_i^k)_{0\le k<m}\), because the points are distinct. Hence every \(a_i=0\). This proves strictness. Standard centered-Gram reconstruction, or (2), then shows that every \(m\)-point restriction has Euclidean affine rank \(m-1\), not a smaller rank.

**(d) Exact unit-cycle spectral geometry.** For unit resistances let \(u_k=k(n-k)\), where indices are modulo \(n\), and let \(\Delta f(k)=f(k+1)-2f(k)+f(k-1)\). Direct calculation gives the *cyclic* identities
\[
\Delta u=-2+2n\mathbf1_{\{0\}},\qquad
\Delta(u^2)=-12u+2(n^2+1)-4n\mathbf1_{\{0\}}.
\]
At a nonzero Fourier frequency \(j\), \(\Delta\) has multiplier \(-4s_j^2\), hence
\[
\widehat u(j)=-\frac{n}{2s_j^2},\qquad
\widehat{u^2}(j)=-\frac{n(3-2s_j^2)}{2s_j^4}.
\]
Because \(R(k)=u_k/n\), the nonzero Fourier eigenvalues of its squared-distance matrix are \(-\frac{3-2s_j^2}{2ns_j^4}\). Centering and multiplying by \(-1/2\) proves the displayed \(b_j\). The product formula follows from
\[
\prod_{j=1}^{n-1}\sin^2(\pi j/n)=\frac{n^2}{4^{n-1}},\qquad
\prod_{j=1}^{n-1}(2+\cos(2\pi j/n))
=\frac{T_n(2)-(-1)^n}{3\,2^{n-1}}.
\]
Finally, the Gram determinant of the \(n-1\) edge vectors from a chosen simplex vertex is \(n\det'B\). Dividing by \(((n-1)!)^2\) yields the volume formula.

**(e) Sharp finite-to-continuous boundary.** Strict \(2\)-negative type on any fixed finite set is an open condition in the exponent: the associated quadratic form is uniformly negative on the compact unit sphere of real zero-sum coefficients. Thus each finite weighted cycle has \(\wp>2\). The unit triangle is equilateral, so \(\wp_3=+\infty\). For \(n\ge4\), take three consecutive unit-cycle vertices. Their two short resistance distances are \((n-1)/n\); the long one is \(2(n-2)/n\). If \(R\) has \(p\)-negative type then \(R^{p/2}\) is a Euclidean distance and obeys the triangle inequality, forcing
\[
\left(\frac{2(n-2)}{n-1}\right)^{p/2}\le 2.
\]
This yields the explicit bound in the theorem. It tends to \(2\), proving \(\wp_n\to2\). For any fixed \(p>2\), choose \(n\) sufficiently large so that this three-vertex inequality fails. Since those three positions belong to the continuous circle, the continuum has no \(p>2\) negative type. Equation (2) proves strict \(2\)-negative type on every finite subset, completing the contrast.

## Verification

A standalone standard-library checker, `verify_cycle_resistance.py`, independently inverts grounded conductance Laplacians using exact rational arithmetic for 12 weighted and unweighted cycles, compares every effective resistance with the two-arc formula, and verifies positivity of all leading Euclidean edge-Gram minors. It computes exact Gram determinants for unit cycles of lengths \(3\) through \(9\), comparing them with the Chebyshev expression, and numerically replays the discrete Fourier formula for lengths \(3\) through \(31\). It also checks monotonic convergence of the explicit triangle *upper bounds* at selected sizes. All checks passed. The universal proof is (a)–(e), not numerical extrapolation.

## Relationship to prior work

Klein and Randić introduced the electrical resistance distance and its matrix formulation; Zhang and Yang derived resistance distances and Kirchhoff indices in circulant graphs, including cycles. Jorgensen and Pearse's energy-space embedding identifies \(\sqrt R\) as a Hilbert distance; their Section 5 explicitly distinguishes this from embedding \(R\) itself. Schoenberg's negative-type criterion characterizes Euclidean metrics; Sánchez supplies general finite-metric threshold methods, rather than the evaluated weighted-cycle statement.

The new combined claim is the **strict \(2\)-negative type of \(R\) itself for all positively weighted cycles**, its explicit circle Fourier realization, the full unit-cycle Euclidean simplex spectrum and exact volume, and the strict-continuum-versus-supercritical-finite limit law. The Fourier/Bernoulli identity and the underlying general embedding criterion are classical ingredients, not separately claimed as inventions. A stronger published specialized theorem with the same metric and implications would cover this claim; such coverage was not identified in the inspected sources.

## Limitations

No exact formula is claimed for finite \(\wp_n\) at \(n\ge4\), and the displayed finite upper bound need not be optimal. Neither the weighted-cycle Euclideanity nor the continuum threshold extends automatically to arbitrary graphs: for instance a three-leaf unit star has resistance metric equal to its path metric, and its center-to-leaf distances \(1\) and pairwise leaf distances \(2\) cannot all occur in Euclidean space. The result is about positive edge resistances and their effective-resistance metric, not weighted shortest paths. Although the mathematical argument is self-contained, the possibility of an unindexed equivalent treatment of cyclic resistance metrics or Bernoulli kernels remains a literature-priority limitation.

## References

- D. J. Klein and M. Randić, *Resistance distance*, Journal of Mathematical Chemistry 12 (1993), 81–95. DOI: 10.1007/BF01164627.
- H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330–339. First online September 5, 2006. DOI: 10.1002/qua.21068.
- P. E. T. Jorgensen and E. P. J. Pearse, *A Hilbert space approach to effective resistance metric*, arXiv:0906.2535 (first version June 14, 2009), especially Section 5.
- S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (August 2, 2011).
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536. DOI: 10.1090/S0002-9947-1938-1501980-0.
