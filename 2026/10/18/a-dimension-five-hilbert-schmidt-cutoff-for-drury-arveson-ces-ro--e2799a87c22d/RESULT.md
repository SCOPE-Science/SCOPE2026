# A dimension-five Hilbert–Schmidt cutoff for Drury–Arveson Cesàro commutators

## Finding

For every integer \(d\ge 2\) and two distinct coordinate indices \(i,j\), the commutator \(K_{ij}=C_iC_j-C_jC_i\) of the Cesàro-type coordinate operators on the Drury–Arveson space \(\mathcal H_d\) is a nonzero bounded operator and satisfies the sharp dichotomy

\[
K_{ij}\in\mathcal S_2(\mathcal H_d)\quad\Longleftrightarrow\quad 2\le d\le5.
\]

More precisely, with \(m\ge0\), \(k,l\ge0\), and \(r=k+l\), its squared Hilbert–Schmidt norm, interpreted as an extended nonnegative real number, is exactly

\[
\|K_{ij}\|_{\mathcal S_2}^{2}
=\sum_{m=0}^{\infty}\ \sum_{\substack{k,l\ge0\\k\ne l}}
\frac{(k-l)^2}{(m+k+1)^2(m+l+1)^2(m+k+l+1)^2}
\frac{\prod_{s=1}^{d-1}(m+k+l+s)}
{\binom{k+l}{k}\prod_{s=1}^{d-1}(k+l+s)}.
\]

This is an exact dimension cutoff for the *non-adjoint coordinate commutator*, not for an adjoint multiplier commutator or the individual Cesàro operators.

## Assumptions and scope

Let \(d\) be any integer at least two. On the unit ball \(\mathbb B_d\subset\mathbb C^d\), let \(\mathcal H_d\) be the reproducing-kernel Hilbert space with kernel \(k(z,w)=(1-\langle z,w\rangle)^{-1}\). For multiindices \(\alpha\in\mathbb N_0^d\), its monomials are orthogonal, with \(\|z^\alpha\|^2=\alpha!/|\alpha|!\), and \(e_\alpha=(|\alpha|!/\alpha!)^{1/2}z^\alpha\) is an orthonormal basis. Here factorials of multiindices mean products of coordinate factorials.

Define on polynomials, and then extend boundedly,

\[
C_jz^\alpha=\sum_{l=0}^\infty\frac{z^{\alpha+l\mathbf e_j}}{|\alpha|+l+1},\qquad 1\le j\le d.
\]

In particular \(C_j f(z)=\int_0^1 f(tz)/(1-tz_j)\,dt\) holds first for polynomials. We only consider the ordinary commutator \(K_{ij}=C_iC_j-C_jC_i\) of different coordinates \(i\ne j\) and the Hilbert–Schmidt ideal \(\mathcal S_2\); no assertion is made about the complete Schatten scale or compactness in dimensions at least six.

## Proof

**1. Boundedness of the coordinate operators.** Fix a coordinate \(j\) and all other monomial exponents \(\beta\), with \(h=|\beta|\). The corresponding closed orthogonal fiber, spanned by the normalized monomials \(z^\beta z_j^n\), is invariant under \(C_j\). Its matrix, indexed by output \(p\ge n\ge0\), is

\[
(C_j)_{p,n}=\frac1{h+p+1}\sqrt{\frac{(h+n)!\,p!}{n!\,(h+p)!}}
=\frac1{h+p+1}\prod_{s=1}^{h}\left(\frac{n+s}{p+s}\right)^{1/2}
\le\frac1{p+1}.
\]

The classical Cesàro matrix \((\mathbf 1_{p\ge n}/(p+1))\) is bounded on \(\ell^2\) with norm two by Hardy's inequality. Entrywise domination on each nonnegative fiber gives \(\|C_j\|\le2\), uniformly in \(h\). Thus all \(C_j\) and their commutators are bounded.

**2. Exact commutator coefficient.** Write \(m=|\alpha|\). Iterating the defining series and extracting a fixed monomial shows that for distinct \(i,j\)

\[
K_{ij}z^\alpha=
\sum_{k,l\ge0}\left(\frac1{(m+l+1)(m+k+l+1)}-
\frac1{(m+k+1)(m+k+l+1)}\right)
 z^{\alpha+k\mathbf e_i+l\mathbf e_j}
\]

\[
=\sum_{k,l\ge0}
\frac{k-l}{(m+k+1)(m+l+1)(m+k+l+1)}
 z^{\alpha+k\mathbf e_i+l\mathbf e_j}.
\]

These monomials are pairwise orthogonal for fixed \(\alpha\). The squared normalized-monomial coefficient includes the factor

\[
R_\alpha(k,l)=\frac{m!}{(m+k+l)!}
\frac{(\alpha_i+k)!}{\alpha_i!}
\frac{(\alpha_j+l)!}{\alpha_j!}.
\]

**3. Exact degree-summed normalization.** Use \(\sum_{a\ge0}\binom{a+k}{k}t^a=(1-t)^{-(k+1)}\), with \(d-2\) additional unit generating factors, to obtain

\[
\sum_{|\alpha|=m}\binom{\alpha_i+k}{k}\binom{\alpha_j+l}{l}
=\binom{m+k+l+d-1}{m}.
\]

Multiplication by \(m!k!l!/(m+k+l)!\) yields the exact identity

\[
\sum_{|\alpha|=m}R_\alpha(k,l)
=\frac{\prod_{s=1}^{d-1}(m+k+l+s)}
{\binom{k+l}{k}\prod_{s=1}^{d-1}(k+l+s)}.
\]

Summing squared coefficients over the orthonormal basis (Tonelli's theorem for nonnegative terms) proves the asserted exact series. For the constant monomial, its \(z_i\) coefficient is \(1/4\), so \(K_{ij}\ne0\).

**4. Failure at and above dimension six.** Retain only the nonnegative terms with \((k,l)=(1,0)\). Their degree-\(m\) contribution equals

\[
\frac{\prod_{s=1}^{d-1}(m+1+s)}
{\left(\prod_{s=1}^{d-1}(1+s)\right)(m+1)^2(m+2)^4}
\asymp_d (m+1)^{d-7}.
\]

The resulting series diverges for every integer \(d\ge6\), logarithmically at \(d=6\). Hence the full Hilbert–Schmidt series diverges there.

**5. Hilbert–Schmidt convergence through dimension five.** Let \(r=k+l\ge1\). The elementary inequalities

\[
(m+k+1)(m+l+1)\ge(m+1)(m+r+1),\qquad |k-l|\le r,
\]

\[
\sum_{k=0}^r\binom rk^{-1}\le3,
\qquad
\prod_{s=1}^{d-1}\frac{m+r+s}{r+s}
\le\left(1+\frac m{r+1}\right)^{d-1}
\]

bound the exact squared Hilbert–Schmidt series by

\[
3\sum_{m\ge0}\sum_{r\ge1}
\frac{r^2(1+m/(r+1))^{d-1}}{(m+1)^2(m+r+1)^4}.
\]

On \(r>m+1\), its \(m\)-level contribution is \(O_d((m+1)^{-3})\). On \(1\le r\le m+1\), it is at most

\[
O_d\left((m+1)^{d-7}\sum_{1\le r\le m+1}r^{3-d}\right).
\]

This is \(O((m+1)^{-3})\) at \(d=2,3\), \(O((m+1)^{-3}\log(m+2))\) at \(d=4\), and \(O((m+1)^{-2})\) at \(d=5\). All are summable. Combining with Step 4 proves the claimed if-and-only-if theorem and completes the proof.

## Verification

`verifier.py` uses only Python's standard library and exact rational arithmetic to verify the commutator coefficient identity and the multiindex-summed monomial normalization for dimensions two through five, degrees zero through five, and coordinate increments zero through four (600 cases). It also checks nonzero action on constants and positive witness terms for dimensions through eight. Run `python3 verifier.py` in a directory containing that embedded file; the expected marker is `DRURY_CESARO_COMMUTATOR_EXACT_IDENTITIES_OK cases=600`. These finite checks test critical algebra but do not prove convergence or divergence; Step 4 and Step 5 supply the latter analytically.

## Relationship to prior work

Pilla introduced the noncommuting Cesàro coordinate tuple on \(\mathcal H_d\) in the June 23, 2026 manuscript *Cesàro-Type Operators Acting on the Drury-Arveson Space* (arXiv:2606.24710v1). Pilla's June 24 follow-up *Rhaly-Type Operators in Several Complex Variables* (arXiv:2606.25885v1) discusses their exact norms and related Rhaly operators. The present claim concerns a different invariant: the Hilbert–Schmidt threshold of commutators of two distinct Cesàro coordinates.

Fang and Xia, *Commutators and Localization on the Drury–Arveson Space*, prove Schatten estimates for \([M_f^*,M_{z_i}]\), where \(M_f\) is multiplication by a multiplier. The operators in this theorem instead are the non-multiplier, noncommuting Cesàro components \(C_i,C_j\). The multiplier-commutator statements therefore do not imply this cutoff.

The accessible original abstracts and secondary summaries of the two 2026 preprints do not document this cutoff. Their complete texts were not available for comprehensive overlap inspection, so an equivalent unpublished or uninspected assertion cannot be excluded. This limitation is not treated as proof of novelty.

## Limitations

The theorem is restricted to finite integer dimension \(d\ge2\), distinct coordinate indices and the Hilbert–Schmidt class \(\mathcal S_2\). Failure of Hilbert–Schmidt membership in dimension six and above does not by itself imply noncompactness or exclude membership in larger Schatten ideals. All infinite-dimensional steps are analytical; the finite verifier is corroborative only. Bibliographic originality remains subject to complete-text and independent specialist checking.

## References

1. M. R. Pilla, *Cesàro-Type Operators Acting on the Drury-Arveson Space*, arXiv:2606.24710v1, first posted 2026-06-23.
2. M. R. Pilla, *Rhaly-Type Operators in Several Complex Variables*, arXiv:2606.25885v1, first posted 2026-06-24.
3. Q. Fang and J. Xia, *Commutators and Localization on the Drury–Arveson Space*, author-hosted PDF: https://www.acsu.buffalo.edu/~jxia/Preprints/commutator.pdf.
4. W. Arveson, *p-Summable commutators in dimension d*, Journal of Operator Theory (2005), arXiv:math/0308104.
