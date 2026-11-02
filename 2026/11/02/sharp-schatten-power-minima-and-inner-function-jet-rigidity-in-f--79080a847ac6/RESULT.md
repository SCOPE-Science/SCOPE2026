# Sharp Schatten-power minima and inner-function jet rigidity in finite Hardy model spaces

## Finding
Let \(B(z)=\sum_{j\ge0}b_jz^j\) be a finite Blaschke product of degree \(N\ge1\), with \(b=b_0=B(0)\) and \(0<r=|b|<1\). Let \(K_B=H^2(\mathbb D)\ominus BH^2(\mathbb D)\), and let \(S_B=P_{K_B}M_z|_{K_B}\) be the compressed shift. For every integer \(1\le k\le N\), the exact Hilbert–Schmidt identity is
\[
\operatorname{Tr}|S_B^k|^2=N-k+kr^2+\sum_{j=1}^{k-1}(k-j)|b_j|^2.
\]
For every finite real \(p>0\), simultaneously,
\[
\boxed{\operatorname{Tr}|S_B^k|^p\ge N-k+kr^p.}
\]
Equality for one finite \(p>0\) holds if and only if equality holds for every finite \(p>0\); this is equivalent to \(b_1=\cdots=b_{k-1}=0\). At equality, the singular values of \(S_B^k\) are exactly \(N-k\) copies of \(1\) and \(k\) copies of \(r\). All minimizers admit the complete factorization
\[
\boxed{B(z)=\frac{b+z^kC(z)}{1+\overline b\,z^kC(z)}},
\]
where \(C\) is an arbitrary finite Blaschke product of degree \(N-k\), allowing a unimodular constant when \(N=k\). For \(k=N\), the zeros of each minimizing \(B\) form a regular \(N\)-gon of radius \(r^{1/N}\), with orientation fixed by the unimodular parameter in \(C\).

## Assumptions and scope
The Hardy space \(H^2(\mathbb D)\) has the norm \(\|f\|^2=\sum_{j\ge0}|\widehat f(j)|^2\). The finite Blaschke product may have repeated zeros. Its degree \(N\) is the dimension of \(K_B\). The quantity \(\operatorname{Tr}|T|^p\) is the sum of the \(p\)-th powers of the singular values of a finite-dimensional operator \(T\), and is defined for every real \(p>0\). The value \(b\) is fixed when minimizing over degree-\(N\) products; the minimum depends only on \(r=|b|\). The assertions do not include \(r=0\), \(r=1\), \(k>N\), or the \(p=\infty\) operator norm.

## Proof
**1. The defect vector.** Write \(T=S_B\) and \(v(z)=(B(z)-B(0))/z\). For \(f\in K_B\), the function \(\overline B f\) has only strictly negative Fourier modes; hence \(P_{BH^2}(zf)=B\langle zf,B\rangle=B\langle f,v\rangle\). Since multiplication by \(z\) is an isometry,
\[
I-T^*T=v\otimes v,\qquad \|v\|^2=1-r^2.
\]
Also \(K_B\) is invariant under the Hardy backward shift, so \(T^*=M_z^*|_{K_B}\). Thus \(T^{*\ell}v\) is obtained by removing the first \(\ell\) Taylor coefficients of \(v\), and
\[
\|T^{*\ell}v\|^2=\sum_{j\ge\ell+1}|b_j|^2.
\]

**2. The exact moment defect.** A telescoping operator identity gives
\[
I-(T^k)^*T^k=\sum_{\ell=0}^{k-1}T^{*\ell}(v\otimes v)T^\ell
=\sum_{\ell=0}^{k-1}(T^{*\ell}v)\otimes(T^{*\ell}v).
\]
It has rank at most \(k\), so at least \(N-k\) singular values of \(T^k\) equal \(1\). Taking traces, using \(\sum_{j\ge0}|b_j|^2=\|B\|_{H^2}^2=1\), and rearranging yields
\[
\operatorname{Tr}|T^k|^2=N-\sum_{\ell=0}^{k-1}\sum_{j\ge\ell+1}|b_j|^2
=N-k+kr^2+\sum_{j=1}^{k-1}(k-j)|b_j|^2.
\]
In particular, the excess in the displayed identity is nonnegative and vanishes exactly when \(b_1=\cdots=b_{k-1}=0\), with the condition vacuous for \(k=1\).

**3. Every positive singular-value power.** The eigenvalues of \(T\) are the zeros of \(B\), with algebraic multiplicity; hence \(|\det T|=|B(0)|=r\), and \(\prod_{i=1}^{N}s_i(T^k)=r^k\). Choose any \(N-k\) singular values equal to \(1\). Denote the remaining \(k\) positive singular values by \(x_1,\ldots,x_k\). Their product is \(r^k\). For each \(p>0\), arithmetic–geometric mean applied to \(x_i^p\) yields
\[
\sum_{i=1}^k x_i^p\ge k\Big(\prod_{i=1}^k x_i^p\Big)^{1/k}=kr^p,
\]
with equality if and only if all \(x_i=r\). Consequently equality for any \(p\) implies equality for \(p=2\), and Step 2 forces the vanishing-jet condition. Conversely that condition gives equality for \(p=2\); equality in the preceding arithmetic–geometric mean then forces the complete singular-value multiset and equality for all \(p>0\).

**4. Classification by a disk automorphism.** The Frostman shift \(\Phi(z)=(B(z)-b)/(1-\overline b B(z))\) is a finite Blaschke product of degree \(N\). It vanishes to order at least \(k\) at the origin if and only if \(b_1=\cdots=b_{k-1}=0\). Dividing by \(z^k\) leaves a finite Blaschke product \(C\) of degree \(N-k\). Solving \(\Phi=z^kC\) for \(B\) gives the stated formula; conversely every such \(C\) yields an admissible \(B\) with the required jets and degree. When \(N=k\), \(C\) is unimodular and zeros satisfy \(z^N=-b/C\), proving the polygon assertion.

## Verification
The self-contained `CHECK.py` constructs compressed backward shifts from Gram matrices of Szegő kernels at distinct Blaschke zeros. It compares the observed \(k\)-th-power singular-value squares with the exact Taylor-coefficient identity, tests five finite exponents per power, and checks both strict and equality cases, including higher-order jet-flat products and regular polygons. Executing `python CHECK.py` with NumPy installed yielded **338 passing finite identities, lower bounds, and equality tests**. These computations check only the listed finite examples; every universally quantified statement follows from the proof above. No computer-assisted infinite certification is claimed.

## Relationship to prior work
Gorkin and Partington (first public version 2017-11-16) develop the compressed-shift matrix model and numerical-radius calculations, and study norms of truncated Toeplitz operators. Lopatto and Rochberg (2014) establish Schatten membership criteria for various truncated Toeplitz operators, explicitly observing that all operators on finite Blaschke model spaces already belong to every Schatten class. Neither inspected full text formulates the fixed-origin, all-positive-power simultaneous optimization or the exact Taylor-jet excess and complete inner-factorization equality classification here. Câmara, Carteiro and Ross (2024) study operator equivalence under multipliers; this is a distinct relation, not an ordered singular-value optimization. The rank-one defect and arithmetic–geometric-mean inequality are classical tools rather than independent claims. No negative literature search proves worldwide novelty; related older matrix inequalities may imply a portion of the lower bound, while the full equality classification is a narrower Hardy-space statement.

## Limitations
The result is finite-dimensional and assumes nonzero \(B(0)\), a fixed degree and a positive integer power no larger than the degree. The operator-norm limit is not covered: for \(k<N\), many compressed powers attain norm \(1\) regardless of their Taylor jets. The universal norm inequality alone follows readily from defect rank and determinant, so its distinctive content is the exact Taylor coefficient excess and full equality classification. Literature coverage does not eliminate all historical-priority risk. Independent mathematical validation has not been performed.

## References
- P. Gorkin and J. R. Partington, *Norms of truncated Toeplitz operators and numerical radii of restricted shifts*, arXiv:1711.06042, first posted 2017-11-16, https://arxiv.org/abs/1711.06042.
- P. Lopatto and R. Rochberg, *Schatten-class truncated Toeplitz operators*, arXiv:1410.1906, first posted 2014-10-07, https://arxiv.org/abs/1410.1906.
- M. C. Câmara, C. Carteiro and W. T. Ross, *Multipliers and equivalence of functions, spaces, and operators*, *Banach Journal of Mathematical Analysis* 18, article 37 (2024), https://doi.org/10.1007/s43037-024-00349-7.
- K. M. Dyakonov, *Interpolation and duality in spaces of pseudocontinuable functions*, *Mathematische Zeitschrift* 302 (2022), https://doi.org/10.1007/s00209-022-03109-1.
