# Exact finite variance of the fourth moment of a random unimodular polynomial
## Finding
Let \(n\ge 2\), let \(a_0,\ldots,a_{n-1}\) be independent Haar-uniform random variables on the unit circle, and put
\[
P_n(z)=\sum_{j=0}^{n-1}a_jz^j,\qquad
X_n=\|P_n\|_{L^4(\mathbb T)}^4,
\]
where Haar measure on \(\mathbb T\) is normalized to have total mass \(1\). Then
\[
\mathbb E X_n=2n^2-n
\]
and the variance is exactly
\[
\operatorname{Var}(X_n)=
\begin{cases}
\dfrac{2n(n-2)(4n-7)}{3},& n\text{ even},\\[6pt]
\dfrac{2(n-1)(4n^2-11n+3)}{3},& n\text{ odd}.
\end{cases}
\]
In particular,
\[
\operatorname{Var}(X_n)=\frac{8}{3}n^3+O(n^2),
\]
so the coefficient of variation of \(X_n\) is asymptotic to \(\sqrt{2/(3n)}\).

## Assumptions and scope
For \(1\le k<n\), define the aperiodic autocorrelation
\[
C_k=\sum_{j=0}^{n-1-k}a_{j+k}\overline{a_j}
\]
and the base energy
\[
E_n=\sum_{k=1}^{n-1}|C_k|^2.
\]
Parseval gives the exact identity
\[
X_n=n^2+2E_n.
\]
The result concerns independent continuous phases. It does not assert the same variance for binary, finite-alphabet, periodic, or dependent coefficient ensembles.

## Proof
Expand
\[
E_n=\sum_{k=1}^{n-1}\sum_{i,j=0}^{n-1-k}
a_{i+k}\overline{a_i}\,\overline{a_{j+k}}a_j.
\]
The terms with \(i=j\) are identically \(1\), and there are
\[
\sum_{k=1}^{n-1}(n-k)=\frac{n(n-1)}2
\]
of them. Every term with \(i\ne j\) is a nontrivial character of the torus of coefficient phases and hence has mean \(0\). Therefore
\[
\mathbb E E_n=\frac{n(n-1)}2
\]
and \(\mathbb E X_n=2n^2-n\).

It remains to count equal nontrivial characters. For \(i<j\), write \(d=j-i>0\). The corresponding character is
\[
\chi_{i;d,k}
=
a_{i+k}a_{i+d}\overline{a_i a_{i+d+k}},
\qquad i+d+k\le n-1.
\]
Its two negative exponent locations are the endpoints \(i\) and \(i+d+k\), while its positive exponent multiset is \(\{i+d,i+k\}\). Consequently another triple gives the same character exactly when it has the same left endpoint and interchanges \(d\) and \(k\). Thus the multiplicity is \(1\) when \(d=k\) and \(2\) when \(d\ne k\). The characters arising from \(i>j\) are the conjugates of those with \(i<j\), and no nontrivial character equals its conjugate.

Let \(T\) be the number of nonconstant ordered summands. Then
\[
T=\sum_{k=1}^{n-1}(n-k)(n-k-1)
=\frac{n(n-1)(n-2)}3.
\]
Let \(N_1\) be the number of distinct nontrivial characters of multiplicity \(1\). The condition \(d=k\), including the conjugate characters, gives
\[
N_1=
2\sum_{\substack{d\ge1\\2d\le n-1}}(n-2d)
=
\begin{cases}
\dfrac{n(n-2)}2,&n\text{ even},\\[6pt]
\dfrac{(n-1)^2}2,&n\text{ odd}.
\end{cases}
\]
If \(N_2\) is the number of distinct nontrivial characters of multiplicity \(2\), then \(T=N_1+2N_2\). Orthogonality of Haar characters gives
\[
\operatorname{Var}(E_n)=N_1+4N_2=2T-N_1.
\]
Hence
\[
\operatorname{Var}(E_n)=
\begin{cases}
\dfrac{n(n-2)(4n-7)}6,&n\text{ even},\\[6pt]
\dfrac{(n-1)(4n^2-11n+3)}6,&n\text{ odd}.
\end{cases}
\]
Finally \(X_n=n^2+2E_n\), so \(\operatorname{Var}(X_n)=4\operatorname{Var}(E_n)\), proving the stated formula.

## Verification
The accompanying verifier independently enumerates every character exponent vector occurring in the expansion of \(E_n\) for \(2\le n\le40\). It checks the constant-term count, verifies that every nonconstant character has multiplicity \(1\) or \(2\), and compares the exact sum of squared multiplicities with the two parity formulas. These finite checks corroborate the proof; the theorem for all \(n\ge2\) rests on the character classification and counting argument above.

## Relationship to prior work
Schmidt's work on unimodular polynomials records the exact Parseval connection between fourth norms and squared aperiodic autocorrelations and studies deterministic extremal growth. Choi and Mossinghoff study averages and moments for random unimodular polynomials; their moment theorem implies that the variance of the normalized fourth norm tends to zero, while their discussion records the classical mean \(\mathbb E X_n=2n^2-n\). The present formula resolves the finite-\(n\) variance exactly, including a parity correction, and therefore gives the explicit concentration scale hidden by the asymptotic variance statement.

Searches across fourth-norm, autocorrelation-energy, random-phase, and finite-variance formulations found no statement implying this exact parity formula. The closest indexed results concern deterministic phase optimization, different random polynomial ensembles, or asymptotic concentration rather than the finite Haar-phase variance.

## Limitations
The argument uses independence and Haar-uniformity essentially through character orthogonality. It does not provide higher cumulants, a central limit theorem, or tail bounds. An older equivalent formula may exist in random-polynomial, coding, or radar literature under different notation; the closest directly inspected average-norm source gives asymptotic moment concentration rather than this finite formula.

## References
1. Kai-Uwe Schmidt, “On a problem due to Littlewood concerning polynomials with unimodular coefficients,” arXiv:1302.2766; Journal of Fourier Analysis and Applications 19 (2013). Primary MSC 42A05 and 11B83.
2. Kwok-Kwong Stephen Choi and Michael J. Mossinghoff, “Average Mahler's measure and \(L^p\) norms of unimodular polynomials,” Pacific Journal of Mathematics 252 (2011), DOI 10.2140/pjm.2011.252.31.
