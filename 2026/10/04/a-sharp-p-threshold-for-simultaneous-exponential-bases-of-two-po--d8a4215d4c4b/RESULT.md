# A sharp \(p\)-threshold for simultaneous exponential bases of two-point subsets
## Finding
Let \(G\) be a finite abelian group and let
\[
E_j=\{x_j,y_j\},\qquad d_j=y_j-x_j\ne0,
\]
for \(1\le j\le m\). Write
\[
d_j^\perp=\{\psi\in\widehat G:\psi(d_j)=1\}.
\]
Then the family \(E_1,\ldots,E_m\) has a simultaneous exponential Riesz basis if and only if
\[
\widehat G\ne\bigcup_{j=1}^m d_j^\perp.
\]
Equivalently, a character \(\psi\) outside this union gives the simultaneous basis \(\{1,\psi\}\).

If \(p\) is the least prime divisor of \(|G|\), every family of at most \(p\) two-point subsets has a simultaneous basis. The bound is sharp uniformly in \(p\): for every prime \(p\), there are \(p+1\) two-point subsets of \(\mathbb Z_p^2\) with no simultaneous basis.

Thus, for every finite abelian group, every pair of two-point subsets has a simultaneous exponential Riesz basis. This settles the cardinality-two case of Question 1.8 of Ferguson--Mayeli--Sothanaphan.

## Assumptions and scope
A simultaneous basis is understood in the finite-dimensional sense of Ferguson--Mayeli--Sothanaphan: the same subset \(B\subseteq\widehat G\), with \(|B|=|E_j|\), restricts to a basis on every \(E_j\). For two-point sets, invertibility of the corresponding \(2\times2\) Fourier restriction matrix is equivalent to the Riesz-basis property.

The threshold statement assumes \(G\) is nontrivial, which is automatic when a two-point subset exists. The result concerns only families whose members have cardinality two; it does not resolve Question 1.8 for larger equal cardinalities.

## Proof
Take two distinct characters \(\chi_0,\chi_1\in\widehat G\), and put
\[
\psi=\chi_1\chi_0^{-1}.
\]
For \(E_j=\{x_j,y_j\}\), the restriction matrix has determinant
\[
\begin{aligned}
\Delta_j
&=\chi_0(x_j)\chi_1(y_j)-\chi_1(x_j)\chi_0(y_j)\\
&=\chi_0(x_j)\chi_0(y_j)\psi(x_j)\bigl(\psi(d_j)-1\bigr).
\end{aligned}
\]
All prefactors are nonzero, so \(\Delta_j\ne0\) exactly when \(\psi(d_j)\ne1\), or equivalently \(\psi\notin d_j^\perp\). Therefore \(\{\chi_0,\chi_1\}\) is a simultaneous basis precisely when its quotient character \(\psi\) lies outside every \(d_j^\perp\). Conversely, any such \(\psi\) yields the simultaneous basis \(\{1,\psi\}\). This proves the exact characterization.

Now let \(N=|G|\), and let \(p\) be the least prime divisor of \(N\). For nonzero \(d_j\), the order \(o(d_j)\) is a nontrivial divisor of \(N\), hence \(o(d_j)\ge p\). Evaluation at \(d_j\) is a homomorphism from \(\widehat G\) onto the character group of \(\langle d_j\rangle\), so
\[
|d_j^\perp|=\frac{N}{o(d_j)}\le\frac{N}{p}.
\]
Every annihilator contains the trivial character. Hence for \(m\le p\),
\[
\left|\bigcup_{j=1}^m d_j^\perp\right|
\le 1+\sum_{j=1}^m\bigl(|d_j^\perp|-1\bigr)
\le 1+m\left(\frac{N}{p}-1\right)
\le N-p+1<N.
\]
The union cannot cover \(\widehat G\), so the exact characterization supplies a simultaneous basis.

For sharpness, take \(G=\mathbb Z_p^2\). Choose one nonzero vector \(d_j\) from each of the \(p+1\) one-dimensional subspaces of \(G\), and set \(E_j=\{0,d_j\}\). Each \(d_j^\perp\) is a one-dimensional subspace of the two-dimensional dual vector space \(\widehat G\cong\mathbb Z_p^2\). Distinct directions give distinct annihilator lines, so these \(p+1\) lines are all the one-dimensional subspaces of \(\widehat G\), whose union is the whole dual group. The characterization therefore rules out a simultaneous basis. This proves sharpness.

## Verification
The accompanying `verify.py` exhaustively checks the determinant criterion for every two-point subset of several small finite abelian groups, checks every pair of two-point subsets in those groups, and verifies the sharp \(p+1\)-direction obstruction for \(p=2,3,5,7\). It prints `VERIFY_OK`.

These finite computations are only sanity checks. The universal statements follow from the determinant factorization, the annihilator-size identity, and the elementary union estimate in the proof.

## Relationship to prior work
Ferguson, Mayeli, and Sothanaphan define simultaneous bases for families of equal-size subsets and ask whether every pair of equal-size subsets of a finite abelian group has a simultaneous exponential Riesz basis. Their paper states that the pair question is unresolved. It also gives three two-point subsets of \(\mathbb Z_2^2\) with no simultaneous basis and, more generally, \(p+1\) one-dimensional subgroups of \(\mathbb Z_p^2\), each of size \(p\), with no simultaneous basis. The present result identifies the exact obstruction for arbitrary two-point subsets, proves a sharp universal family-size threshold, and produces the corresponding \(p+1\) obstruction using two-point subsets for every prime \(p\).

Classical work of Bhaskara Rao and Reid studies when abelian groups can be covered by proper subgroups and determines minimal covering numbers. That covering theory is directly relevant after the determinant reduction above, but the checked source does not formulate the simultaneous Fourier-basis characterization or the two-point resolution of the Riesz-basis question.

## Limitations
No claim is made for subsets of cardinality three or larger, nor for quantitative conditioning of the simultaneous basis. The originality check covered the source paper's full simultaneous-basis section, exact-phrase and parameter searches, classical subgroup-covering literature, and semantic published-finding corpus searches. Literature using different terminology may still contain an equivalent observation; failed searches are not treated as proof of absolute novelty.

## References
1. S. Ferguson, A. Mayeli, and N. Sothanaphan, "Riesz bases of exponentials and multi-tiling in finite abelian groups," arXiv:1904.04487, first posted 9 April 2019; primary MSC 43A70, 43A40.
2. K. P. S. Bhaskara Rao and J. D. Reid, "Abelian Groups that are unions of proper subgroups," *Bulletin of the Australian Mathematical Society* 45 (1992), 1--7. DOI: 10.1017/S0004972700036959.
