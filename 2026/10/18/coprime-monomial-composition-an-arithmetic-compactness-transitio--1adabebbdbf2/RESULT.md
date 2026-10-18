# Coprime monomial composition: an arithmetic compactness transition and a sharp weak-trace threshold

## Finding

Let \(\alpha>-1\), and let \(\mathcal D_\alpha\) be the complex weighted Dirichlet Hilbert space specified below. For integers \(m,k\ge2\), let \(C_m f=f\circ(z\mapsto z^m)\), and set
\[
K_{m,k}^{(\alpha)}=C_m^*C_k-C_kC_m^*.
\]
Then \(K_{m,k}^{(\alpha)}\) is compact **if and only if** \(\gcd(m,k)=1\). If \(m,k\) are coprime and \(\alpha=0\), the operator vanishes identically. If \(m,k\) are coprime and \(\alpha\ne0\), its singular values obey
\[
\lim_{n\to\infty} n\,s_n(K_{m,k}^{(\alpha)})
=\Lambda_{\alpha;m,k}
:=\frac{|\alpha|(\alpha+1)}{2}\,\frac{(m-1)(k-1)}{mk}
(mk)^{(1-\alpha)/2}>0.
\]
Consequently, in this nonzero compact case, \(K_{m,k}^{(\alpha)}\in\mathcal S_p\) exactly when \(p>1\), for \(0<p<\infty\), and
\[
\sum_{j=1}^{N}s_j(K_{m,k}^{(\alpha)})
=\Lambda_{\alpha;m,k}\log N+O_{\alpha,m,k}(1).
\]
Thus \(|K_{m,k}^{(\alpha)}|\) is Dixmier-measurable, and each normalized Dixmier trace of it equals \(\Lambda_{\alpha;m,k}\).

## Assumptions and scope

The unit disk \(\mathbb D\) carries normalized area measure \(dA=dx\,dy/\pi\). The Hilbert norm is
\[
\|f\|_{\mathcal D_\alpha}^2=|f(0)|^2
+(\alpha+1)\int_{\mathbb D}|f'(z)|^2(1-|z|^2)^\alpha\,dA(z),
\qquad \alpha>-1.
\]
The operators \(C_m,C_k\) act on this same space. Adjoints, compactness and singular values refer to this Hilbert norm; singular values are listed nonincreasingly with multiplicity. The result is for integer monomial degrees at least two, not for arbitrary composition symbols. All complex conjugations implicit in the adjoint are harmless because the coefficient weights are positive real numbers.

## Proof

**1. Orthogonal coefficient normalization and boundedness.** The monomials are orthogonal. For each \(n\ge1\), beta integration gives
\[
w_n:=\|z^n\|_{\mathcal D_\alpha}^2
=(\alpha+1)n^2\int_0^1 u^{n-1}(1-u)^\alpha\,du
=\Gamma(\alpha+2)n^2\frac{\Gamma(n)}{\Gamma(n+\alpha+1)},
\qquad w_0=1.
\]
Writing \(e_n=z^n/\sqrt{w_n}\), we obtain an orthonormal basis. For integer \(r\ge2\),
\[
C_re_0=e_0,\qquad C_re_n=a_r(n)e_{rn},
\quad a_r(n)=\sqrt{\frac{w_{rn}}{w_n}}\quad(n\ge1).
\]
The standard gamma-ratio expansion at positive integers, for fixed \(\alpha\), is
\[
w_n=\Gamma(\alpha+2)n^{1-\alpha}
\left(1-\frac{A_\alpha}{n}+O_\alpha(n^{-2})\right),
\qquad A_\alpha=\frac{\alpha(\alpha+1)}2.
\]
It follows that \(a_r(n)\to r^{(1-\alpha)/2}>0\) and that \(C_r\) is bounded, with \(\sup_{n\ge1}a_r(n)<\infty\).

**2. The arithmetic noncompactness obstruction.** Let \(g=\gcd(m,k)>1\). For each positive integer \(j\) not divisible by \(g\), put \(n_j=(m/g)j\). The index \(n_j\) is not divisible by \(m\), whereas \(kn_j\) is. Thus
\[
C_kC_m^*e_{n_j}=0,
\qquad
C_m^*C_ke_{n_j}
=a_k(n_j)a_m((k/g)j)e_{(k/g)j}.
\]
As \(j\to\infty\) through such integers, the displayed coefficient tends to \((mk)^{(1-\alpha)/2}>0\). The vectors \(e_{n_j}\) are orthonormal and hence weakly null, so their images under \(K_{m,k}^{(\alpha)}\) cannot converge in norm to zero. The operator is not compact.

**3. Exact sparse decomposition in the coprime case.** Suppose \(\gcd(m,k)=1\). For \(n\ge1\), the vector \(C_m^*C_ke_n\) is nonzero only when \(m\mid kn\), equivalently \(m\mid n\); the same divisibility condition holds for \(C_kC_m^*e_n\). Also \(K_{m,k}^{(\alpha)}e_0=0\). Therefore
\[
K_{m,k}^{(\alpha)}e_{mj}=\Delta_j e_{kj},
\qquad K_{m,k}^{(\alpha)}e_n=0\ \text{if }m\nmid n,
\]
where, for all integers \(j\ge1\),
\[
\Delta_j=
\frac{w_{mkj}}{\sqrt{w_{mj}w_{kj}}}
-\frac{\sqrt{w_{mj}w_{kj}}}{w_j}.
\]
Since both index families \(\{mj:j\ge1\}\) and \(\{kj:j\ge1\}\) are pairwise distinct, the nonzero singular-value list of \(K_{m,k}^{(\alpha)}\) is precisely the decreasing rearrangement of \(\{|\Delta_j|:j\ge1\}\), with zero values omitted. This identity gives compactness as soon as \(\Delta_j\to0\).

**4. First-order cancellation and the exact coefficient.** Substitute the expansion of \(w_n\) into the two fractions in \(\Delta_j\). With \(R=(mk)^{(1-\alpha)/2}\), the terms have the respective expansions
\[
\frac{w_{mkj}}{\sqrt{w_{mj}w_{kj}}}
=R\left[1+\frac{A_\alpha}{j}
\left(-\frac1{mk}+\frac1{2m}+\frac1{2k}\right)+O(j^{-2})\right],
\]
\[
\frac{\sqrt{w_{mj}w_{kj}}}{w_j}
=R\left[1+\frac{A_\alpha}{j}
\left(1-\frac1{2m}-\frac1{2k}\right)+O(j^{-2})\right].
\]
Subtracting yields the quantitative cancellation
\[
\Delta_j=-\frac{A_\alpha(m-1)(k-1)}{mk}
(mk)^{(1-\alpha)/2}\frac1j+O_{\alpha,m,k}(j^{-2}).
\]
For \(\alpha\ne0\), the coefficient is nonzero because \(\alpha>-1\) and \(m,k\ge2\). Thus \(|\Delta_j|=\Lambda_{\alpha;m,k}/j+O(j^{-2})\), and rearrangement yields \(n s_n(K_{m,k}^{(\alpha)})\to\Lambda_{\alpha;m,k}\). (For example, this follows by counting entries above a positive threshold, using a two-sided \((\Lambda\pm\varepsilon)/j\) bound outside a finite set.) The same estimate gives membership in \(\mathcal S_p\) exactly when \(p>1\).

**5. Logarithmic partial sums and the classical cancellation point.** Because
\[
\sum_{j\ge1}\left||\Delta_j|-\frac{\Lambda_{\alpha;m,k}}j\right|<\infty,
\]
we can compare the sums of the largest \(N\) terms using the elementary \(\ell^1\)-Lipschitz property of decreasing rearrangement. They differ from \(\Lambda_{\alpha;m,k}\sum_{j=1}^N j^{-1}\) by at most a constant independent of \(N\). The logarithmic coefficient follows, and the normalized Dixmier-trace statement follows from convergence of these logarithmic means. If \(\alpha=0\), then \(w_n=n\) holds exactly; both fractions in \(\Delta_j\) equal \(\sqrt{mk}\), so \(\Delta_j=0\) for every \(j\) and \(K_{m,k}^{(0)}=0\) whenever \(m,k\) are coprime. This completes all cases.

## Verification

The accompanying standalone script `check_monomial_dirichlet.py` checks 900 sparse-column identities for small degrees and several weights, six finite-index first-order asymptotic diagnostics, and three noncoprime noncompactness witnesses. It uses only the Python standard library; run it with `python check_monomial_dirichlet.py` in the same directory. These tests are independent finite diagnostics. The infinite-index expansions, compactness claims, Schatten characterization and Dixmier trace are justified by the analytic proof above, not by numerical extrapolation.

## Relationship to prior work

He, Yan, Zhang and Zhao (2026) study products of linear-fractional composition operators on weighted Dirichlet spaces, including qualitative compactness and Schatten results. Here both symbols have degree at least two, and the object is a **difference** of two generally noncompact products, with arithmetic coprimality controlling cancellation and a quantitative weak-trace endpoint.

Abdollahi and Mehrangiz (2011) and Heller and Pons (2018) study monomial composition and, in particular, **self-commutators**. The present theorem concerns the mixed adjoint commutator associated with two independently chosen monomial degrees and provides an exact singular-value coefficient. Their accessible abstracts do not establish this mixed-degree result; their complete papers were not available for full comparison. Existing general weighted-composition results and related commutator research do not imply the stated coefficient through any established implication inspected here.

## Limitations

The classification is restricted to integer monomials on this normalized weighted Dirichlet Hilbert scale. No claim is made about arbitrary analytic composition symbols, mixed weights, or exact singular-value formulas at finite indices after rearrangement. The leading residue describes only the coprime nonclassical case \(\alpha\ne0\). As a publication-priority limitation, full texts of the directly related 2011 and 2018 monomial papers and certain other sources remained inaccessible; an undiscovered equivalent result cannot be excluded. This limitation does not affect the self-contained proof.

## References

1. He, Yan, Zhang, and Zhao, *Some Properties of Products of Linear Fractional Composition Operators on Weighted Dirichlet Spaces*, arXiv:2609.29897v1 (first posted 2026-09-24), https://arxiv.org/html/2609.29897 . Full-text inspection included the principal statements and proofs on products and Schatten membership.
2. Abdolaziz Abdollahi and S. Mehrangiz, *Self-Commutators of Composition Operators with Monomial Symbols on the Dirichlet Space*, *Abstract and Applied Analysis* (2011), doi:10.1155/2011/618968. Abstract accessible; full text not inspected.
3. Katherine Heller and Matthew A. Pons, *Composition Operators with Monomial Symbol Acting on Weighted Hardy Spaces*, *Mediterranean Journal of Mathematics* (2018), doi:10.1007/s00009-017-1040-5. Abstract and bibliographic material accessible; full text not inspected.
4. He and Zhou, *Spectra of Composition Operators Acting on Weighted Dirichlet Spaces*, *Bulletin of the Belgian Mathematical Society* (2025), doi:10.36045/J.BBMS.240726. Abstract accessible; concerns individual spectra.
