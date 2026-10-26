# Sharp quasi-Schatten norms of the minimal row–column Schur projection

## Finding

Let \(H=\ell_2(\mathbb N_0)\), let \(P\) be the orthogonal projection onto its first coordinate, and define the Schur projection
\[
\mathcal M(X)=PX+XP-PXP.
\]
Thus \(\mathcal M\) retains the first row and first column of a matrix and sets every other entry to zero. For every \(0<p\le1\), its *exact* quasi-Schatten multiplier norm is
\[
\boxed{\quad
\|\mathcal M:\mathcal S_p(H)\to\mathcal S_p(H)\|
=\max_{0\le u\le1}\left\{
\left(\frac{\sqrt{u(4-3u)}+u}{2}\right)^p+
\left(\frac{\sqrt{u(4-3u)}-u}{2}\right)^p
\right\}^{1/p}.\quad}
\]
The maximum has a unique parameter \(u_p\). More explicitly, set
\[
F_p(k)=\frac{2k}{1+3k^2}
\bigl[(1+k)^p+(1-k)^p\bigr]^{1/p},\qquad 0\le k\le1.
\]
For \(0<p<1\), \(F_p\) has a unique maximizer \(k_p\in(0,1/\sqrt3)\), characterized by
\[
\frac{1-3k_p^2}{k_p(1+3k_p^2)}+
\frac{(1+k_p)^{p-1}-(1-k_p)^{p-1}}
{(1+k_p)^p+(1-k_p)^p}=0,
\qquad u_p=\frac{4k_p^2}{1+3k_p^2}.
\]
For \(p=1\), \(k_1=1/\sqrt3\) and \(u_1=2/3\). Every sharp constant is attained by the positive rank-one projection \(X_p=x_p x_p^*\), with \(x_p=\sqrt{u_p}\,e_0+\sqrt{1-u_p}\,e_1\). In particular,
\[
\|\mathcal M\|_{\mathcal S_1\to\mathcal S_1}=\frac2{\sqrt3},
\qquad
u_{1/2}=\frac{7-\sqrt{13}}6,
\]
and the corresponding sharp norm is
\[
\|\mathcal M\|_{\mathcal S_{1/2}\to\mathcal S_{1/2}}
=\sqrt{u_{1/2}(4-3u_{1/2})}+2\sqrt{u_{1/2}(1-u_{1/2})}
=2.1327104114\ldots.
\]
The constant is independent of the ambient Hilbert-space dimension provided it is at least two, and the same formula holds for rectangular matrices with one designated row and one designated column.

## Assumptions and scope

We use the usual singular-value quasi-norm \(\|X\|_p=(\sum_j s_j(X)^p)^{1/p}\) on the complex Schatten ideal \(\mathcal S_p\), \(0<p\le1\). Operator norm of a linear map between these quasi-normed spaces is its best multiplicative constant. The operator \(\mathcal M\) is an idempotent Schur multiplier, not a positive map on operators. The distinguished row and column intersect at one entry; the overlap is retained once. The proof applies equally to finite dimensions at least two and to rectangular matrix spaces.

## Proof

**1. Reduction to rank one.** For \(0<p\le1\), the Schatten quasi-triangle inequality gives
\(\|U+V\|_p^p\le\|U\|_p^p+\|V\|_p^p\). Write any \(X\in\mathcal S_p\) by its singular-value expansion \(X=\sum_j s_jx_jy_j^*\). If \(C\) is the supremum of \(\|\mathcal M(xy^*)\|_p\) over unit vectors \(x,y\), then
\[
\|\mathcal M(X)\|_p^p\le\sum_j s_j^p\|\mathcal M(x_jy_j^*)\|_p^p
\le C^p\|X\|_p^p.
\]
Finite sums converge in \(\mathcal S_p\), while the reverse bound follows by testing rank-one operators. Hence the rank-one supremum equals the full multiplier norm.

**2. The two-parameter singular spectrum.** Write \(s=|\langle x,e_0\rangle|^2\) and \(t=|\langle y,e_0\rangle|^2\). Unitary changes of basis within \(e_0^\perp\), and diagonal phases, reduce \(\mathcal M(xy^*)\) to the real nonnegative \(2\times2\) block
\[
B_{s,t}=\begin{pmatrix}\sqrt{st}&\sqrt{s(1-t)}\\
\sqrt{(1-s)t}&0\end{pmatrix}.
\]
Its singular values \(a\ge b\ge0\) obey
\[
a^2+b^2=s+t-st,\qquad ab=\sqrt{st(1-s)(1-t)}.
\]

**3. Strict symmetrization.** Fix \(S=s+t\) and put \(Q=st\), so \(a^2+b^2=S-Q\) and \(ab=D=\sqrt{Q(1-S+Q)}\). Increasing \(Q\) on its feasible interval decreases \(a\), since the sum of squared singular values decreases while their product increases. At the same time it *strictly increases* the sum \(a+b=\sqrt{S-Q+2D}\). Indeed, with \(A=Q\), \(B=1-S+Q\),
\[
\frac{d}{dQ}(S-Q+2D)=-1+\frac{A+B}{\sqrt{AB}}\ge1
\]
in the interior (endpoints follow by continuity). Thus, as \(Q\) increases, \(a\) decreases while \(b\) increases and \(a+b\) strictly increases. For \(0<p\le1\), the inequality \(a^{p-1}\le b^{p-1}\) gives
\[
\frac{d}{dQ}(a^p+b^p)
=p b^{p-1}(a'+b')+p(a^{p-1}-b^{p-1})a'>0.
\]
By \(st\le(s+t)^2/4\), each fixed \(S\) is therefore maximized uniquely at \(s=t=S/2\). No phase restriction was used, so this rules out asymmetric rank-one extremizers.

**4. Unique one-variable optimizer.** Set \(s=t=u\). The block is symmetric and has singular values
\[
\sigma_\pm(u)=\frac{\sqrt{u(4-3u)}\pm u}{2}.
\]
The stated maximum follows. Substitute \(k=\sqrt{u/(4-3u)}\), equivalently \(u=4k^2/(1+3k^2)\), to obtain \(F_p\). For \(0<p\le1\), logarithmic differentiation yields
\[
\frac{F_p'(k)}{F_p(k)}=
\underbrace{\frac{1-3k^2}{k(1+3k^2)}}_{G(k)}+
\underbrace{\frac{(1+k)^{p-1}-(1-k)^{p-1}}
{(1+k)^p+(1-k)^p}}_{H_p(k)}.
\]
On \(0<k<1/\sqrt3\), \(G\) decreases strictly from \(+\infty\) to zero. For \(p<1\), \(H_p<0\) and \(H_p'<0\): writing \(N=(1+k)^{p-1}-(1-k)^{p-1}<0\) and \(Z=(1+k)^p+(1-k)^p>0\), one has \(N'=(p-1)[(1+k)^{p-2}+(1-k)^{p-2}]<0\), \(Z'=pN\), so \(H_p'=(N'Z-pN^2)/Z^2<0\). Consequently there is exactly one root on that interval. For \(k\ge1/\sqrt3\) both terms are nonpositive and at least one is strictly negative. For \(p=1\), \(H_1=0\), and the unique maximum occurs at \(k=1/\sqrt3\). The endpoints \(k=0\) and \(k=1\) do not maximize. This proves uniqueness and the extremizer construction.

**5. Explicit indices.** At \(p=1\), maximize \(\sqrt{u(4-3u)}\) to get \(u=2/3\) and constant \(2/\sqrt3\). At \(p=1/2\), the objective reduces to \(\sqrt{u(4-3u)}+2\sqrt{u(1-u)}\). Differentiating and squaring the positive terms on the interval \(1/2<u<2/3\) gives \(u(3u^2-7u+3)=0\); uniqueness selects \(u=(7-\sqrt{13})/6\), which gives the displayed exact value.

## Verification

Run `python3 verify_star_schatten.py` from the extracted directory. It independently computes singular values of random complex rank-one masked matrices by Gram matrices, checks the two-variable reduction and symmetry comparison, solves the one-dimensional critical equation by bisection, and checks the two explicit endpoints. The diagnostic finite tests do not certify the infinite-dimensional operator statement; that follows from the quasi-triangle inequality and the singular-value decomposition in Step 1.

## Relationship to prior work

The 2026 classification by McDonald, Sukochev, and Zanin identifies finite unions of rows and columns as the only possible supports of bounded Schur patterns on quasi-Schatten ideals below exponent one; its Lemma 2.1(iv) supplies boundedness for such supports, but does not compute this two-sided mask's sharp constant or optimizer. Aleksandrov and Peller's 2001/2002 Hankel and Toeplitz Schur multiplier study supplies the basic quasi-triangle framework but concerns structured diagonal-constant symbols rather than this row–column cross. Banks and Harcharras' 2004 gap theorem treats idempotent Schur multipliers for \(1<p<\infty\), \(p\ne2\), with a two-by-two three-one mask appearing in its argument; it does not resolve the quasi-Banach exponent interval. The \(p=1\) endpoint is included as a consistency check, not asserted as a new standalone discovery. The main claim is the full sharp \(0<p<1\) profile and rank-one optimizer rigidity.

## Limitations

The result concerns the binary row–column cross mask with one designated row and column. It does not compute constants for several distinguished rows/columns, arbitrary sign choices on the same support, or \(p>1\). The literature comparison establishes best-knowledge priority, not a guarantee that no equivalent older finite-matrix inequality exists. No independent mathematical audit has been performed.

## References

1. E. McDonald, F. Sukochev, and D. Zanin, *Schur bounded patterns, submajorisation and operator Lipschitz functions*, arXiv:2605.07564v2 (first posted 8 May 2026), especially Lemma 2.1(iv) and Theorem 2.3, https://arxiv.org/pdf/2605.07564.
2. A. B. Aleksandrov and V. V. Peller, *Hankel and Toeplitz–Schur multipliers*, arXiv:math/0101264 (first posted 31 January 2001), https://arxiv.org/pdf/math/0101264.
3. W. D. Banks and A. Harcharras, *On the norm of an idempotent Schur multiplier on the Schatten class*, Proceedings of the American Mathematical Society 132 (2004), 2121–2125, DOI:10.1090/S0002-9939-04-07340-X.
