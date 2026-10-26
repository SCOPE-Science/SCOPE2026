# Integral deletion torsion and unimodular interlacing in balanced multiset incidences

## Finding

Let \(n\geq1\) and \(1\leq r\leq n\). Put \(m=n-r+1\) and let \(M_j\) be the multisets of size \(j\) on an ordered alphabet of \(m\) symbols. Consider the integer matrices with rows \(s\in M_{r-1}\) and columns \(t\in M_r\):

* \(E_{n,r}(s,t)\) is the number of positions in \(t\) whose deletion gives \(s\).
* \(R_{n,r}(s,t)\) equals \(1\) exactly when \(t_i\leq s_i\leq t_{i+1}\) for every \(1\leq i<r\), and is \(0\) otherwise.

The **joint integral incidence theorem** is as follows.

**(a) Unimodular transversal submatrix.** The binary interlacing matrix \(R_{n,r}\) contains a square minor of size \(\binom{n-1}{r-1}\) and determinant \(1\). Hence it is a split surjection of free abelian groups and has full row rank over every field.

**(b) Complete torsion and modular rank of the balanced weighting.** If \(1\leq r<n\), the integral cokernel of \(E_{n,r}\) is
\[
\operatorname{coker}_{\mathbb Z} E_{n,r}
\cong\bigoplus_{j=1}^{r}
(\mathbb Z/j\mathbb Z)^{\binom{n-j-1}{r-j}}.
\]
This direct sum is an integral diagonal decomposition; the listed integers \(j\) are not asserted to be the divisibility-ordered Smith invariant factors. Over a field \(K\) of characteristic \(p>0\),
\[
\operatorname{rank}_{K} E_{n,r}
=\sum_{\substack{1\leq j\leq r\\p\nmid j}}
\binom{n-j-1}{r-j}.
\]
In particular, for \(r<n\), this matrix has full row rank in characteristic \(p\) **if and only if** \(p>r\). In characteristic zero it has full row rank. At the boundary \(r=n\), both matrices consist of a single entry: \(R_{n,n}=[1]\) and \(E_{n,n}=[n]\). Thus the latter has cokernel \(\mathbb Z/n\mathbb Z\) and drops rank exactly in characteristics dividing \(n\).

The juxtaposition is sharp: replacing the integer deletion multiplicities by the distinct binary interlacing relation changes the modular behavior from rank loss in every characteristic \(p\leq r\) (when \(r<n\)) to full rank in every characteristic.

## Assumptions and scope

All matrices use the original integral multiset coordinates, not rationally rescaled bases. The convention \(M_0=\{()\}\) handles \(r=1\). The relation matrix \(R_{n,r}\) is the full *interlacing* relation from the order-preserving-transformation problem; it is not the support matrix \(\mathbf 1_{E_{n,r}>0}\), since interlacing may hold without a single deletion producing the shorter multiset. Row and column order affect the signs of chosen minors but not the stated invariant conclusions.

The cokernel means \(\mathbb Z^{M_{r-1}}/E_{n,r}(\mathbb Z^{M_r})\). For \(\mathbb Z/1\mathbb Z\) the direct-sum component is trivial. The full row rank claim is about the matrix as a linear transformation of the indicated free modules; it does not assert invertibility of a rectangular matrix.

## Proof

**Unimodularity of the interlacing relation.** Suppose first \(r<n\); write the alphabet as \(\{0,\ldots,m-1\}\). Enumerate \(M_{r-1}\) in lexicographically increasing order. For each row \(s=(s_1,\ldots,s_{r-1})\), select the distinct column
\[
t(s)=(s_1,\ldots,s_{r-1},m-1)\in M_r.
\]
The selected columns are distinct. Consider the square submatrix whose column indexed by \(s\) is \(t(s)\). Its diagonal entry is \(1\): for \(i<r-1\), one has \(t(s)_i=s_i\leq s_i\leq s_{i+1}=t(s)_{i+1}\), while for the last index \(s_{r-1}\leq m-1\). If \(R_{n,r}(u,t(s))=1\), then \(u_i\geq t(s)_i=s_i\) for all \(i\), so \(u\) is lexicographically no earlier than \(s\). Thus entries above the diagonal vanish, and the chosen minor is unit lower triangular. It has determinant \(1\). A maximal minor of determinant \(\pm1\) yields a right inverse over \(\mathbb Z\) by adjoining zeros outside these columns. When \(r=n\), there is one column and one row, with entry \(1\); when \(r=1\), the same construction selects the maximum symbol as the single pivot column, and the argument holds vacuously.

**Integral diagonalization of the deletion weighting.** Identify \(\mathbb Z^{M_j}\) with the homogeneous degree-\(j\) part \(P_j\) of the polynomial ring \(P=\mathbb Z[x_0,\ldots,x_{m-1}]\), taking a multiset to the monomial whose variable exponents are its multiplicities. The deletion homomorphism is precisely the degree-lowering derivation
\[
D=\sum_{i=0}^{m-1}\frac{\partial}{\partial x_i}:P_r\longrightarrow P_{r-1},
\]
because differentiating a monomial at the \(i\)-th variable counts the copies of the \(i\)-th alphabet symbol that can be deleted.

For \(m\geq2\), change generators integrally by
\[
y_0=x_0,\qquad y_i=x_i-x_0\quad(1\leq i<m).
\]
The inverse is \(x_0=y_0\), \(x_i=y_i+y_0\). Hence the homogeneous monomial bases in the \(x\)-coordinates and the \(y\)-coordinates are related in *each degree* by unimodular integer matrices, not merely by rationally invertible matrices. As \(D(y_0)=1\) and \(D(y_i)=0\) for \(i>0\), the same \(D\) is \(\partial/\partial y_0\) in the new coordinates.

Every degree-\(r-1\) monomial uniquely has the form \(y_0^{j-1}v\), where \(1\leq j\leq r\) and \(v\) is a monomial in \(y_1,\ldots,y_{m-1}\) of total degree \(r-j\). Its only incoming monomial under \(D\) is \(y_0^jv\), with coefficient \(j\). The other degree-\(r\) monomials, those with no \(y_0\), map to zero. Thus the whole matrix is equivalent over \(\mathbb Z\) to a rectangular diagonal matrix with the nonzero entry \(j\) repeated
\[
\#\{v: \deg v=r-j\}
=\binom{(m-1)+(r-j)-1}{r-j}
=\binom{n-j-1}{r-j}
\]
times. This establishes the cokernel formula, including the absence of free cokernel summands. Reducing the unimodular change-of-basis matrices modulo any prime preserves their invertibility, and the diagonal entry \(j\) survives exactly when \(p\nmid j\), establishing the rank formula. Each \(j\in\{1,\ldots,r\}\) occurs at least once because \(n>r\); hence precisely the primes at most \(r\) cause rank loss. For \(m=1\), \(P_r\) and \(P_{r-1}\) have basis \(x_0^r\) and \(x_0^{r-1}\) and \(D=[r]=[n]\), proving the boundary statement. This completes both parts.

**Concrete sharp contrast.** For \(n=3,r=2\), in the natural multiset orders,
\[
E_{3,2}=\begin{pmatrix}2&1&0\\0&1&2\end{pmatrix},\qquad
R_{3,2}=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}.
\]
The weighted matrix has rank \(1\) in characteristic two, while the binary interlacing matrix retains rank \(2\), witnessed by a unit determinant minor.

## Verification

The independent direct-construction script `verify.py` enumerates all \((n,r)\) with \(1\leq r\leq n\leq9\), reconstructing the integer matrices from deletion positions and interlacing inequalities, rather than from the claimed diagonal basis. It verifies dimension formulas, all row and column sums, support containment, and the exact lexicographic unit-triangular witness for \(R\). Gaussian elimination modulo \(2,3,5,7\) checks both predicted ranks. For \(n\leq7\), SymPy independently computes the actual Smith normal forms and compares their invariant factors after properly combining the claimed cyclic decomposition into divisibility-ordered invariant factors.

The observed output is `VERIFY_OK cases=45 integer_snf=28 prime_rank_comparisons=180`. This finite test is an independent reproducibility check; the all-parameter result rests on the preceding integer proof.

## Relationship to prior work

Higgins's 2026 study establishes the multiset/interlacing correspondence and proves that the deletion multiplicities have constant row sum \(n\) and column sum \(r\). Its Lemmas 3.3 and 3.5 and Corollary 3.7 give neither an integral cokernel nor a modular-rank classification or a unimodular maximal minor for the binary matrix. The general real-spectral analysis of this same weighted matrix in prior records also does not determine its integer cokernel or ranks after reduction modulo primes: singular values do not determine Smith factors.

The literature on Smith forms of *subset* incidence matrices uses different indexing sets and incidence multiplicities. Cai and Stanley analyze the Young-lattice up-down operator \(DU\) on symmetric functions, not the rectangular degree-lowering map on the full polynomial algebra here. The integer change-of-generators used in this proof is elementary; priority over all possible equivalent classical reformulations is not asserted.

## Limitations

This theorem does not determine Smith forms for arbitrary balanced structure-matrix weightings or for any other order-preserving-transformation incidence beyond the stated multiset deletion construction. The displayed cyclic direct sum is not a sorted Smith diagonal (the corresponding Smith factors require collecting prime powers). The modular-rank conclusion is an arithmetic property of the incidence map, not a new claim about permutation matchings. Older or unindexed literature using the language of homogeneous polynomial differentiation or symmetric powers might imply the integral formula, and an independent historical audit has not been performed.

## References

1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1 (first posted 2026-10-01), especially §3, Lemmas 3.3 and 3.5, Corollary 3.7. https://arxiv.org/html/2610.01912v1
2. T. W. Cai and R. P. Stanley, *The Smith normal form of a matrix associated with Young's lattice*, Proceedings of the American Mathematical Society 143 (2015), 4695–4703; arXiv:1502.00922. https://arxiv.org/abs/1502.00922
3. R. P. Stanley, *Smith Normal Form in Combinatorics*, Journal of Combinatorial Theory, Series A 144 (2016), 476–495; arXiv:1602.00166. https://arxiv.org/abs/1602.00166
