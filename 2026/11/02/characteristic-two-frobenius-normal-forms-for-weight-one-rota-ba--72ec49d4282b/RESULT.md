# Characteristic-two Frobenius normal forms for weight-one Rota–Baxter operators on chain evolution algebras

## Finding
Let \(K\) be any field of characteristic \(2\), let \(n\ge2\), and let \(E_n(K)\) be the evolution algebra with basis \(e_1,\ldots,e_n\) and multiplication \(e_i e_j=0\) when \(i\ne j\), \(e_i^2=e_{i+1}\) for \(1\le i<n\), and \(e_n^2=0\). A weight-one Rota–Baxter operator is a linear map \(R:E_n(K)\to E_n(K)\) satisfying
\[
R(x)R(y)=R(R(x)y+xR(y)+xy)\qquad(x,y\in E_n(K)).
\]

**Complete normal form.** Every such operator is uniquely specified by \(v=R(e_1)=\sum_{s=1}^{n}b_s e_s\). Put \(a=b_1\) and \(d=b_n\). The possible coefficient vectors are **exactly** the following two disjoint classes.

1. **Terminal-support class:** \(b_2=\cdots=b_{n-1}=0\), with \(a,d\in K\) arbitrary.
2. **Sparse Frobenius class:** choose a unique \(k\in\{2,\ldots,n-1\}\), a scalar \(x\in K^\times\), \(a\in\{0,1\}\), and \(d\in K\). For \(2\le j\le n-1\), prescribe
\[
b_j=\begin{cases}
x^{\,\sum_{h=0}^{r-1}2^{h(k-1)}}&\text{if }j=1+r(k-1)\text{ for some integer }r\ge1,\\
0&\text{otherwise}.
\end{cases}
\]
Here \(b_n=d\) is always free, regardless of its residue class. In particular, \(k\) is the first index between \(2\) and \(n-1\) at which the coefficient is nonzero.

For either class, all remaining images are forced by
\[
R(e_i)=\sum_{s=1}^{n-i+1}b_s^{\,2^{i-1}}e_{s+i-1}\qquad(1\le i\le n).
\]
This classification is valid over arbitrary (including infinite and imperfect) characteristic-two fields.

**Finite-field census.** When \(K=\mathbb F_q\), where \(q\) is a power of \(2\), the number of weight-one operators is
\[
|\mathrm{RB}_1(E_n(\mathbb F_q))|=q^2+2(n-2)q(q-1)=(2n-3)q^2-(2n-4)q.
\]
Their ranks as \(\mathbb F_q\)-linear maps have the *exact* distribution
\[
\#\{R:\operatorname{rank}R=r\}=\begin{cases}
1,&r=0,\\
q-1,&r=1,\\
q(q-1),&2\le r\le n-1,\\
(n-1)q(q-1),&r=n.
\end{cases}
\]
For \(n=2\) the intermediate-rank interval is empty. Thus, for fixed \(q\), the entire operator count grows only linearly with \(n\), even though \(\dim\operatorname{End}_K(E_n)=n^2\).

## Assumptions and scope
The defining product is not associative in general. The Rota–Baxter identity is tested using the displayed nonassociative multiplication, not ordinary matrix multiplication. All exponents in the normal form are nonnegative integers and field powers, not matrix powers. No hypothesis of algebraic closure or perfection is required. The finite census requires a finite field of characteristic two. The classification concerns weight exactly \(1\), and the unperturbed chain with the specific nonzero superdiagonal products \(e_i^2=e_{i+1}\).

## Proof
**1. Frobenius recursion.** In characteristic two, taking \(x=y=e_i\) in the defining identity cancels the two mixed summands and gives \(R(e_i)^2=R(e_{i+1})\) for \(i<n\), and \(R(e_n)^2=0\). Let \(Q(z)=z^2\). In this evolution algebra,
\[
Q\Bigl(\sum_{s=1}^n c_s e_s\Bigr)=\sum_{s=1}^{n-1}c_s^2e_{s+1}.
\]
Induction gives \(R(e_i)=Q^{i-1}(v)\) and the displayed image formula. In particular all images are upper triangular in the ordered basis, and \(R(e_n)\) is a multiple of \(e_n\), so its square vanishes.

**2. Exact cross-equations.** For \(1\le i<j\le n\), we have \(e_i e_j=0\) and \(e_iR(e_j)=0\), while
\[
R(e_i)e_j=b_{j-i+1}^{\,2^{i-1}}e_{j+1}
\]
when \(j<n\) (and zero when \(j=n\)). Equating the coefficient of \(e_{m+1}\), for \(j\le m<n\), in the Rota–Baxter identity yields
\[
b_{m-i+1}^{\,2^{i-1}}b_{m-j+1}^{\,2^{j-1}}
=b_{j-i+1}^{\,2^{i-1}}b_{m-j+1}^{\,2^j}.
\]
The Frobenius map is injective over every field of characteristic two. Writing \(s=j-i+1\) and \(t=m-j+1\), these equalities are therefore equivalent to
\[
\boxed{b_{s+t-1}b_t^{\,2^{s-1}}=b_s b_t^{\,2^s}}\tag{*}
\]
for all integers \(s\ge2\), \(t\ge1\), \(s+t-1\le n-1\). Every instance of (*) is already obtained by choosing \(i=1,j=s,m=s+t-1\), and all other cross-identities are its Frobenius powers. Equations with \(j=n\) are automatic. Therefore the diagonal recursion together with (*) is **necessary and sufficient** for a weight-one Rota–Baxter operator.

**3. Solve (*).** If \(b_2=\cdots=b_{n-1}=0\), every instance of (*) vanishes, giving the terminal-support class and showing that \(a\) and \(d\) are unconstrained.

Otherwise let \(k\in\{2,\ldots,n-1\}\) be the smallest index with \(b_k=x\ne0\). Set \(s=k,t=1\) in (*). Since \(x\ne0\), this implies \(a^{2^{k-1}}=a^{2^k}\); injectivity of iterated Frobenius gives \(a=a^2\), hence \(a\in\{0,1\}\).

Next take \(t=k\) in (*). Dividing by the nonzero scalar \(x^{2^{s-1}}\) gives the *forward recurrence*
\[
b_{s+k-1}=b_s x^{\,2^{s-1}}\qquad(2\le s\le n-k).
\]
The initial values \(b_2=\cdots=b_{k-1}=0\) and \(b_k=x\) determine every \(b_j\) through \(b_{n-1}\) uniquely, yielding zero except when \(j=1+r(k-1)\), with the claimed geometric-sum exponent at those indices. No equation (*) involves \(b_n\), so \(d\) is free.

Conversely, these explicit coefficients satisfy every instance of (*). For \(t=1\), this follows from \(a\in\{0,1\}\). For \(t\ge2\) with \(b_t=0\), both sides are zero. If \(b_t\ne0\), its index is \(t=1+\ell(k-1)\) for some \(\ell\ge1\). If \(b_s=0\), then \(s+t-1\) is also off the permitted residue class, and both sides vanish. If \(b_s\ne0\), write \(s=1+r(k-1)\). The exponents obey
\[
\sum_{h=0}^{r+\ell-1}2^{h(k-1)}
=\sum_{h=0}^{r-1}2^{h(k-1)}+2^{r(k-1)}\sum_{h=0}^{\ell-1}2^{h(k-1)},
\]
which proves (*) upon substituting the explicit powers of \(x\). This proves necessity and sufficiency of both disjoint normal forms.

**4. Finite-field count.** The terminal-support class has \(q^2\) members. For each of the \(n-2\) possible indices \(k\), the sparse class has \(2(q-1)q\) members, and different choices of \(k\) are disjoint. Adding gives the exact cardinality.

**5. Rank distribution.** The image formula is upper triangular, with diagonal entries \(a,a^2,\ldots,a^{2^{n-1}}\). If \(a\ne0\), the operator is invertible; this contributes \(q(q-1)+(n-2)q(q-1)=(n-1)q(q-1)\) operators. If \(a=0\) in the terminal-support class, only \(R(e_1)=d e_n\) can be nonzero, giving one rank-zero operator and \(q-1\) rank-one operators. If \(a=0\) in the sparse class with initial index \(k\), then for \(1\le i\le n-k+1\) the first nonzero coordinate of \(R(e_i)\) occurs at \(e_{i+k-1}\) with coefficient \(x^{2^{i-1}}\ne0\); all images with \(i>n-k+1\) vanish. These leading-coordinate positions are distinct, so the rank is exactly \(n-k+1\). As \(k\) ranges from \(2\) to \(n-1\), every rank \(2,\ldots,n-1\) occurs exactly \(q(q-1)\) times. The theorem follows.

## Verification
The accompanying standalone `verify.py` performs independent direct enumeration of all first-image vectors \(v\in\mathbb F_q^n\) for \(q=2,4,8\) in the indicated small dimensions. For each vector it reconstructs \(R(e_i)\) by squaring in the evolution algebra, checks the original Rota–Baxter identity on every ordered basis pair, and calculates the matrix rank by finite-field elimination. It does not use the sparse normal-form recurrence to decide acceptance or compute rank. The exhaustive tested cases are \(q=2\), \(2\le n\le8\); \(q=4\), \(2\le n\le6\); and \(q=8\), \(2\le n\le5\). The program reports `VERIFY_OK` and matches every predicted rank stratum. These finite tests are not an infinite proof; the preceding algebraic argument establishes the full claim.

## Relationship to prior work
Qaralleh, Mukhamedov, and Khakimov [1] classify weight-zero and weight-one Rota–Baxter operators on maximal-nilindex evolution algebras over real or complex fields. Their Section 3 explicitly restricts the coefficient field to real or complex numbers; their weight-one recurrence involves \(x^2/(2x+1)\). Importantly, their Section 5.4 already discusses sparse off-diagonal patterns in the characteristic-zero setting, so sparsity *by itself* is not claimed as new. The present theorem supplies a self-contained characteristic-two classification, including its finite-field exact multiplicities and full linear-rank frequencies; the existing real/complex results do not apply under the present field hypothesis. The local weight-zero study [2] assumes characteristic zero and is not a weight-one characteristic-two classification. Older general Rota–Baxter studies of associative and semigroup algebras [3] do not cover this nonassociative chain family. No historical-priority claim beyond the comparisons stated is made.

## Limitations
The theorem does not cover arbitrary perturbations of the chain multiplication, coefficient characteristic other than two, or weight zero. Even in characteristic two, it asserts only the classification of rational points over a field, not reducedness or smoothness of the representing operator scheme. An equivalent formulation in older or unindexed literature remains possible. The finite computations do not replace the symbolic proof.

## References
[1] I. Qaralleh, F. Mukhamedov, O. Khakimov, *Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669v1, first posted 2026-01-13. https://arxiv.org/abs/2601.08669 ; full text https://arxiv.org/pdf/2601.08669 .

[2] I. Qaralleh, F. Mukhamedov, O. Khakimov, *Local Rota--Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, arXiv:2606.22623v1, first posted 2026-06-21. https://arxiv.org/abs/2606.22623 .

[3] S. Zheng, L. Guo, M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, Communications in Algebra 47 (2019), 3094–3116, DOI: 10.1080/00927872.2018.1552278. https://pmc.ncbi.nlm.nih.gov/articles/PMC7083595/ .
