# The polynexus product-count conjecture for consecutive-diagonal rook monoids

## Finding

For each integer \(n\ge 2\), let \(M_n\) be the inverse submonoid of the \(n\)-by-\(n\) rook monoid consisting of the zero matrix and the \(0\)-\(1\) partial permutation matrices whose ones form a single nonempty consecutive block along a single diagonal. Set

\[
\psi(n)=\bigl|\{(X,Y)\in(M_n\setminus\{0\})^2:XY\ne0\}\bigr|.
\]

Then

\[
\boxed{\psi(n)=\frac{(n+1)^7-n^7-(n+1)^3+n^3}{120}.}
\]

This establishes Conjecture 1 of Fikioris and Fikioris, *A subsemigroup of the rook monoid* (arXiv:2111.01863, §7). In particular, their conditional formula for the proportion of nonzero products in the nonzero elements of \(S_n=M_n\setminus\{1\}\) is unconditional, and that proportion tends to \(21/40\) as \(n\to\infty\).

## Assumptions and scope

The theorem concerns **ordered** pairs, including pairs containing the identity, of **nonzero** elements of \(M_n\). Products equal to zero are excluded from \(\psi(n)\). Multiplication is ordinary matrix multiplication; there are no field assumptions, since the matrices have at most one nonzero entry in each row and column. The result holds for every integer \(n\ge2\); the counting expressions also hold for \(n=1\).

A nonzero matrix is uniquely encoded by \((\ell,a,b)\), where \(1\le\ell\le n\) and \(1\le a,b\le n-\ell+1\). Its ones occupy the positions \((a+j,b+j)\) for \(0\le j<\ell\). Its domain interval of row indices is \([a,a+\ell-1]\), and its image interval of column indices is \([b,b+\ell-1]\). Write \(Q_n=|M_n\setminus\{0\}|\).

## Proof

**Step 1: total nonzero elements.** For each block length \(\ell\), the row and column starts are independent and each has \(n-\ell+1\) choices. Hence

\[
Q_n=\sum_{\ell=1}^{n}(n-\ell+1)^2
=\frac{n(n+1)(2n+1)}6.
\]

**Step 2: classify zero products.** Let \(X=(\ell,a,b)\) and \(Y=(k,c,d)\). Matrix multiplication gives \(XY\ne0\) exactly when the column interval \([b,b+\ell-1]\) of \(X\) meets the row interval \([c,c+k-1]\) of \(Y\). Consequently \(XY=0\) exactly when those two integer intervals are disjoint. For fixed positive lengths \(\ell,k\) with \(\ell+k\le n\), disjoint placements have two orders. In either order, distribute the \(n-\ell-k\) unoccupied sites among the left, middle and right gaps, giving \(\binom{n-\ell-k+2}{2}\) possibilities. The number of ordered disjoint placements is therefore

\[
(n-\ell-k+1)(n-\ell-k+2).
\]

For \(\ell+k>n\) no disjoint placements exist. The other starts \(a,d\) are unconstrained and contribute \((n-\ell+1)(n-k+1)\). Thus the number \(Z_n\) of ordered zero-product pairs of nonzero matrices is

\[
Z_n=\sum_{\ell=1}^{n-1}\sum_{k=1}^{n-\ell}
(n-\ell+1)(n-k+1)(n-\ell-k+1)(n-\ell-k+2).
\]

**Step 3: evaluate the double sum.** Group terms by \(s=\ell+k\). Directly summing the first two factors over \(\ell=1,\ldots,s-1\) yields

\[
\sum_{\ell=1}^{s-1}(n-\ell+1)(n-s+\ell+1)
=(s-1)(n+1)(n+1-s)+\frac{(s-1)s(s+1)}6.
\]

Hence

\[
Z_n=\sum_{s=2}^{n}(n-s+1)(n-s+2)
\left((s-1)(n+1)(n+1-s)+\frac{(s-1)s(s+1)}6\right).
\]

The summand is a polynomial of total degree at most five in \(n,s\), so the power-sum identities show that \(Z_n\) is a polynomial in \(n\) of degree at most six. Its values for \(n=1,2,3,4,5,6,7\) are exactly

\[
0,\ 8,\ 78,\ 386,\ 1344,\ 3752,\ 8988.
\]

The degree-six polynomial

\[
\frac{n(n-1)(n+1)(n+2)(19n^2+19n+6)}{360}
\]

has these same seven values. Two polynomials of degree at most six that agree at seven distinct integers are identical; this *proves for every* \(n\ge1\) that

\[
Z_n=\frac{n(n-1)(n+1)(n+2)(19n^2+19n+6)}{360}.
\]

This finite interpolation argument is a symbolic polynomial-identity proof, not an extrapolation from numerical experimentation: the degree bound was established before using the seven values.

**Step 4: subtract.** Every ordered pair of nonzero matrices has either zero or nonzero product. Therefore

\[
\begin{aligned}
\psi(n)&=Q_n^2-Z_n\\
&=\frac{n(n+1)(7n^4+14n^3+21n^2+14n+4)}{120}\\
&=\frac{(n+1)^7-n^7-(n+1)^3+n^3}{120}.
\end{aligned}
\]

This proves the theorem. As a corollary, since \(|S_n|=Q_n\), precisely \(\psi(n)-2Q_n+1\) ordered nonzero-product pairs remain after excluding either occurrence of the identity. Their ratio to \((Q_n-1)^2\) tends to \(21/40\) by the leading coefficients above.

## Verification

The standalone \(\texttt{checker.py}\) enumerates all nonzero partial injection matrices through their interval parameters, directly checks composition on individual mapped indices, and counts nonzero products for \(1\le n\le9\). It independently computes zero products from the length sum and checks the closed identities for \(1\le n\le100\), printing \(\texttt{CHECKER\_OK}\) on success. Run with \(\texttt{python3 checker.py}\); only Python's standard library is used. The mathematical proof does not rely on extrapolating these finite tests.

For example, \(n=2\) has \(Q_2=5\), \(Z_2=8\), and \(\psi(2)=17\). For \(n=3\) the corresponding values are \(14\), \(78\), and \(118\), recovering the examples in the source paper after removing identity pairs.

## Relationship to prior work

Fikioris and Fikioris define the same monoid, derive its product and size formulas, introduce this exact ordered-pair invariant, and explicitly leave the proposed seventh-power expression as Conjecture 1 after checking \(n\le70\) (arXiv:2111.01863, §7). The present argument uses a different interval-disjointness count to evaluate it for all \(n\).

The same authors' later open-access study of the real-parameter extension \(\overline M_n\) develops its inverse-semigroup structure, Green relations and roots, rather than settling that finite product-count conjecture (arXiv:2302.09496; *Semigroup Forum* 107 (2023)). OEIS A083200 records the seventh-order polynexus formula independently of the monoid interpretation; knowing that sequence does not imply equality with the monoid product count.

## Limitations

The argument counts only whether a product is zero, not the sizes of the fibers of individual nonzero products or higher-fold products. It does not address the real-parameter extension. Although relevant primary sources and mathematical-record searches did not locate a published solution of the specific conjecture, independently unindexed or differently titled proofs remain possible. No independent mathematical audit has been performed.

## References

1. G. Fikioris and G. Fikioris, *A subsemigroup of the rook monoid*, arXiv:2111.01863 (first posted 2021-11-02), §7, Conjecture 1; *Semigroup Forum* 105 (2022), 191–216, DOI: 10.1007/s00233-022-10302-5.
2. G. Fikioris and G. Fikioris, *An extension to “A subsemigroup of the rook monoid”*, arXiv:2302.09496 (2023); *Semigroup Forum* 107 (2023), 637–650, DOI: 10.1007/s00233-023-10393-8.
3. OEIS Foundation, Sequence A083200, *Polynexus numbers of order 7*, https://oeis.org/A083200.
