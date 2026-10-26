# Singular spectra and two-number rigidity for Dirichlet–Volterra commutators

## Finding

Let \(\mathcal H^2\) be the Hardy Hilbert space of ordinary Dirichlet series, with orthonormal basis \(e_n(s)=n^{-s}\), \(n\geq1\). For every integer \(c\geq2\), put \(g_c(s)=c^{-s}\) and let
\[
V_cf(s)=-\int_s^{+\infty}f(w)g_c'(w)\,dw,
\]
initially for Dirichlet polynomials. For distinct integers \(a,b\geq2\), write \(C=[V_a,V_b]=V_aV_b-V_bV_a\), \(u=\log a\), \(v=\log b\), \(t=u+v\), and \(K=uv|u-v|\). For every integer \(k\geq1\), the complete decreasing singular-value sequence of \(C^k\) is
\[
s_n(C^k)=\prod_{j=0}^{k-1}\frac{K}{(\log n+(j+1)t)(\log n+jt+u)(\log n+jt+v)},\qquad n\geq1.
\]
In particular,
\[
\|C^k\|=\frac{(K/t^3)^k}{k!\,(u/t)_k\,(v/t)_k},
\qquad s_n(C^k)\sim\frac{K^k}{(\log n)^{3k}}\quad(n\to\infty),
\]
where \((z)_k=z(z+1)\cdots(z+k-1)\). Every \(C^k\) is compact but belongs to no finite Schatten class \(\mathcal S_p\), \(p>0\). Moreover \(C\) is quasinilpotent, with
\[
\|C^k\|\sim\Gamma(u/t)\Gamma(v/t)\,k\,\frac{(K/t^3)^k}{(k!)^3}\quad(k\to\infty).
\]
The two largest singular values of \(C\) uniquely determine the unordered pair \(\{a,b\}\), among all distinct integer pairs at least two. If \(a=b\), the commutator is identically zero.

## Assumptions and scope

The scalar field is complex. The space \(\mathcal H^2\) is the coefficient Hilbert space \(\{\sum_{n\ge1}x_n n^{-s}:\sum|x_n|^2<\infty\}\), so \(\|e_n\|=1\); integrals are taken on rightward horizontal rays where the Dirichlet polynomial converges absolutely. The symbols are precisely individual nonconstant Dirichlet monomials, not arbitrary Dirichlet polynomials. Each \(V_c\) extends uniquely and boundedly from polynomials to \(\mathcal H^2\). Singular values are counted with multiplicity, nonincreasingly, indexed from one. Compact operators are measured against every finite Schatten exponent, including quasi-Banach \(0<p<1\). No assertion is made about commutators of general polynomial symbols or about BMOA/Bergman operator norms.

## Proof

**1. Coefficient formula.** Direct integration yields, for each \(n\ge1\),
\[
V_c e_n=\frac{\log c}{\log(cn)}e_{cn}.
\]
The multiplication of indices \(n\mapsto cn\) is injective and the coefficient is at most one, proving bounded extension. Writing \(L=\log n\), compositions are
\[
V_aV_b e_n=\frac{uv}{(L+v)(L+t)}e_{abn},\qquad
V_bV_a e_n=\frac{uv}{(L+u)(L+t)}e_{abn}.
\]
Subtracting,
\[
Ce_n=\frac{uv(u-v)}{(L+t)(L+u)(L+v)}e_{abn}.
\]
No coprimality of \(a,b\) is needed.

**2. Every power and its singular values.** Set
\[
w_n=\frac{K}{(\log n+t)(\log n+u)(\log n+v)}.
\]
Its sign-adjusted predecessor is the coefficient of \(Ce_n\). For each integer \(k\ge1\), repeatedly multiplying the input index by \(ab\) gives
\[
C^ke_n=\operatorname{sgn}(u-v)^k\,d_n^{(k)}e_{(ab)^kn},\qquad
d_n^{(k)}=\prod_{j=0}^{k-1}w_{(ab)^jn}.
\]
The functions in the denominators are strictly increasing in \(\log n\), and all factors are positive. Hence \(d_1^{(k)}>d_2^{(k)}>\cdots>0\), with limit zero. The output basis vectors indexed by \((ab)^kn\) are orthonormal. Consequently \((C^k)^*C^ke_n=(d_n^{(k)})^2e_n\), so \(s_n(C^k)=d_n^{(k)}\) in exact decreasing order and \(C^k\) is compact.

**3. Norm and asymptotic laws.** Inserting \(n=1\) and factoring \(t\) from each denominator yields
\[
\|C^k\|=\prod_{j=0}^{k-1}\frac{K/t^3}{(j+1)(j+u/t)(j+v/t)}
=\frac{(K/t^3)^k}{k!(u/t)_k(v/t)_k}.
\]
For fixed \(k\), each factor in \(d_n^{(k)}\) is asymptotic to \(K/(\log n)^3\); therefore \(d_n^{(k)}\sim K^k/(\log n)^{3k}\). For all real \(p>0\), the series \(\sum_{n\ge2}(\log n)^{-3kp}\) diverges, so \(C^k\notin\mathcal S_p\). The classical gamma formula \((z)_k=\Gamma(k+z)/\Gamma(z)\), together with \(u/t+v/t=1\), gives
\[
k!(u/t)_k(v/t)_k\sim\frac{(k!)^3}{k\Gamma(u/t)\Gamma(v/t)}.
\]
Thus the stated sharp factorial decay follows. In particular \(\lim_{k\to\infty}\|C^k\|^{1/k}=0\), so the spectral radius and spectrum of \(C\) are zero and \(\{0\}\), respectively (the latter because the spectrum of a bounded operator is nonempty).

**4. Inverse rigidity from two singular values.** The first singular value is
\[
\delta=s_1(C)=\frac{|u-v|}{t}\in(0,1).
\]
Up to interchange, this fixes \(u/t=(1+\delta)/2\) and \(v/t=(1-\delta)/2\). Put \(x=(1+\delta)/2\), \(y=(1-\delta)/2\), and \(L=\log2>0\). The second-to-first ratio satisfies
\[
\frac{s_2(C)}{s_1(C)}=\frac{t}{t+L}\,\frac{xt}{xt+L}\,\frac{yt}{yt+L}.
\]
For fixed \(0<\delta<1\), the right side is a continuous, strictly increasing function of \(t>0\), ranging from zero to one. It therefore uniquely determines \(t\), and then the unordered positive pair \(\{u,v\}=\{xt,yt\}\), hence \(\{a,b\}=\{e^u,e^v\}\). The proof of the whole claim is complete.

## Verification

The standalone standard-library script `verify.py` applies the two original Volterra operators successively to basis vectors, forms the commutator and its powers, and compares with the closed coefficients. It also checks strict decrease of the first 74 singular values, the closed power-norm identity, and reconstruction of the two logarithms from the top two singular values for six distinct integer pairs. At preparation, it passed 5,370 deterministic finite assertions. These finite tests are diagnostic; the preceding proof establishes the infinite-dimensional assertions, exact singular sequences, all Schatten exponents, and uniqueness for all distinct pairs.

## Relationship to prior work

Brevig, Perfekt and Seip (2016, arXiv:1602.04729, Theorem 7.2) show that nonconstant individual Dirichlet-series Volterra operators are outside every finite Schatten class. Their result concerns a **single** Volterra operator and does not give the two-generator commutator's exact singular sequence, power norms, or inverse recovery. Bommier-Hato (2020, arXiv:2004.04087, Theorem 4) proves a corresponding exclusion for weighted Bergman Dirichlet spaces, again for individual operators.

Recent work by Qin, Liu and Huang (2026, arXiv:2610.22136v1) addresses commuting Toeplitz operators on a different holomorphic Hilbert space. It motivates examining quantitative consequences of noncommutativity, but its Fock-space Toeplitz hypotheses do not govern the present Dirichlet–Volterra operators. Tong, Wang and Yuan (2026, arXiv:2610.21873v1) study boundedness and compactness for Dirichlet-series Volterra operators on BMOA and endpoint Bergman spaces, without treating these Hilbert-space commutator spectra. No result in these inspected sources implies the stated full singular and inverse classification; potential prior formulations in operator-weighted-shift literature remain a priority risk.

## Limitations

The theorem applies to the classical coefficient Hilbert space \(\mathcal H^2\) and distinct monomial symbols only. The inverse assertion uses the **singular values of the commutator**, not its ordinary eigenvalues (all of which vanish). It is not a classification of general Dirichlet-polynomial commutators. Novelty is assessed against accessible primary works and mathematical research searches, not guaranteed by negative search results. An independent mathematical audit and independent priority check have not been performed.

## References

1. J. Qin, Y. Liu and S. Huang, *Commuting Toeplitz operators with harmonic symbols on the Fock space*, arXiv:2610.22136v1 (15 October 2026), https://arxiv.org/html/2610.22136v1. Primary MSC 47B35.
2. C. Tong, M. Wang and Z. Yuan, *Volterra operators on the BMOA space of Dirichlet series*, arXiv:2610.21873v1 (15 October 2026), https://arxiv.org/html/2610.21873v1. Primary MSC 30B50; context only.
3. O. F. Brevig, K.-M. Perfekt and K. Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729 (first public 15 February 2016), https://arxiv.org/abs/1602.04729.
4. H. Bommier-Hato, *Volterra operators and Hankel forms on Bergman spaces of Dirichlet series*, arXiv:2004.04087 (2020), https://arxiv.org/abs/2004.04087.
