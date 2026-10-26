# Complete two-eigenvalue Jordan spectra of quartic-root triangular matrices

## Finding
Let \(q\) be any prime power and \(n\geq1\). Consider the upper-triangular matrices \(A\in T_n(\mathbb F_q)\) annihilated by the split repeated-root polynomial \(p(t)=t^2(t-1)^2\), equivalently satisfying \(A^2(A-I)^2=0\). Every such matrix has only Jordan blocks of sizes one or two, with eigenvalues zero and one. The following recurrence gives the exact multiplicity of **every** possible paired Jordan partition, uniformly in the field characteristic.

For integers \(m,r\geq0\), define \(f_{0,0}(q)=1\), put \(f_{m,r}(q)=0\) whenever \(r<0\) or \(r>\lfloor m/2\rfloor\), and recursively set
\[
f_{m,r}(q)=q^r f_{m-1,r}(q)+\bigl(q^{m-r}-q^{r-1}\bigr)f_{m-1,r-1}(q)\quad(m\geq1),
\]
where the second term is taken as zero for \(r=0\). Let \(a\) be the dimension of the generalized one-eigenspace, \(i\) the number of size-two Jordan blocks at eigenvalue one, and \(j\) the number at eigenvalue zero. For exactly the ranges
\[
0\leq a\leq n,\qquad0\leq i\leq\lfloor a/2\rfloor,\qquad0\leq j\leq\lfloor(n-a)/2\rfloor,
\]
the number of such matrices is
\[
\boxed{\mathcal N_{n,q}(a,i,j)=\binom na q^{a(n-a)}f_{a,i}(q)f_{n-a,j}(q).}
\]
All these multiplicities are strictly positive. The complete three-parameter Jordan enumerator is therefore
\[
\mathcal J_n(q;U,V,W)=\sum_{a=0}^{n}\binom na q^{a(n-a)}U^a F_a(q,V)F_{n-a}(q,W),
\qquad F_m(q,Z)=\sum_{r=0}^{\lfloor m/2\rfloor}f_{m,r}(q)Z^r.
\]
Specializing all three markers to one gives the complete number of solutions of the quartic matrix equation.

## Assumptions and scope
The algebra \(T_n(\mathbb F_q)\) contains all (not necessarily invertible) upper-triangular \(n\times n\) matrices. Matrices and Jordan forms are over the indicated finite field; zero and one are distinct in every characteristic. A block of size two at eigenvalue \(\lambda\) is \(\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}\). The empty-index base case \(m=0\) is only used in the recurrence. The formula does not include matrices with Jordan blocks of size at least three or eigenvalues other than zero and one.

## Proof
**1. Canonical split square-zero decomposition.** In the polynomial quotient \(\mathbb F_q[t]/(t^2(t-1)^2)\), the polynomial \(e(t)=3t^2-2t^3\) is congruent to zero modulo \(t^2\) and to one modulo \((t-1)^2\). These congruences hold in every characteristic. The Chinese-remainder theorem gives \(e(t)^2\equiv e(t)\) modulo \(p(t)\), and \((t-e(t))^2\equiv0\) modulo \(p(t)\). Consequently, any solution \(A\) has the commuting decomposition
\[
A=E+N,\quad E=e(A),\quad E^2=E,\quad N^2=0,\quad EN=NE.
\]
Conversely, for any such commuting pair, the two invariant summands \(\ker E\) and \(\operatorname{im}E\) carry \(A=N\) and \(A=I+N\), respectively, and so \(p(A)=0\). The decomposition is unique: on those two summands, \(e(E+N)\) is respectively zero and identity because \(e(t)\) has the specified congruences modulo the corresponding squared linear factors.

**2. Counting the idempotent fibers.** Fix a binary diagonal vector \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_n)\), with exactly \(a\) entries equal to one, and let \(D=\operatorname{diag}(\varepsilon)\). Every triangular idempotent \(E\) with that diagonal is conjugate to \(D\) by a unitriangular matrix. Indeed, the matrix \(g=ED+(I-E)(I-D)\) has diagonal one, hence is invertible and unitriangular, and satisfies \(Eg=gD\). The group of unitriangular matrices has \(q^{\binom n2}\) elements. A unitriangular matrix commutes with \(D\) precisely when its \((u,v)\) entry vanishes for every pair of distinct diagonal colors. Exactly \(a(n-a)\) upper-triangular positions join unlike colors, irrespective of their order. Thus the conjugacy orbit, which is exactly this diagonal fiber, has size \(q^{a(n-a)}\).

Conjugating \(N\) by \(g\) preserves its rank, its square-zero property and commutation with \(E\). The matrices \(N\) commuting with \(D\) have no entries between unlike-color indices. On the two ordered index sets, their nonzero parts form independent strictly upper-triangular square-zero matrices of dimensions \(a\) and \(n-a\). Their ranks determine the numbers of size-two Jordan blocks of \(A\) at one and zero. Therefore a fixed diagonal coloring contributes \(q^{a(n-a)}f_{a,i}(q)f_{n-a,j}(q)\) matrices of the specified paired Jordan type. There are \(\binom na\) binary diagonals with \(a\) ones.

**3. Square-zero rank recurrence.** Let \(f_{m,r}(q)\) count strictly upper-triangular square-zero matrices of size \(m\) and rank \(r\). Such a matrix has the unique block form
\[
X=\begin{pmatrix}B&v\\0&0\end{pmatrix},\quad B^2=0,\quad Bv=0,
\]
with \(B\) of size \(m-1\). If \(\operatorname{rank}B=r\), exactly \(q^r\) choices \(v\in\operatorname{im}B\) preserve the rank. If \(\operatorname{rank}B=r-1\), exactly \(q^{m-r}-q^{r-1}\) vectors in \(\ker B\setminus\operatorname{im}B\) increase the rank to \(r\). Since \(B^2=0\) implies \(\operatorname{im}B\subseteq\ker B\), these cases are disjoint and exhaustive. This proves the stated recurrence, including the zero-rank boundary. Induction also proves positivity for every admissible rank: take disjoint adjacent size-two Jordan blocks with nonzero superdiagonal entries, realizing each \(r\leq\lfloor m/2\rfloor\).

Multiplying the three independent factors in step 2 and summing over the diagonal choices completes the enumerator proof. No computational enumeration is used in this argument.

## Verification
The accompanying standalone script `verify_squarezero_semisimple.py` constructs the quartic polynomial and its canonical idempotent over prime fields and over \(\mathbb F_4\), computes the two component ranks directly, and compares the exhaustive three-index histograms against the recurrence. It checks sizes \(n\leq5\) over \(\mathbb F_2\), \(n\leq3\) over \(\mathbb F_3\) and \(\mathbb F_4\), and \(n\leq2\) over \(\mathbb F_5\). For instance, the total solution counts are \(60\) at \((n,q)=(3,2)\), \(824\) at \((4,2)\), \(20224\) at \((5,2)\), \(192\) at \((3,3)\), and \(440\) at \((3,4)\). Further integer-recurrence cross-checks cover \(n\leq24\) and seven numerical field-size parameters. All tests are finite checks; the preceding proof establishes the infinite-family claim.

## Relationship to prior work
Ekhad and Zeilberger (1995), building on Kirillov and Melnikov, enumerate strictly upper-triangular square-zero matrices and supply the underlying rank recurrence. Yip (2018) derives rank- and Jordan-refined counts for nilpotent upper-triangular matrices, hence supplies information about the **single-eigenvalue** factors. Gargate and Gargate (2020) enumerate triangular solutions of separable quadratic and higher potent equations, addressing **distinct-root, semisimple** behavior. The present formula counts the full **mixed two-eigenvalue Jordan spectrum with repeated roots** by a canonical polynomial idempotent and an explicit unitriangular orbit-fiber decomposition. The known one-eigenvalue counts and distinct-root counts are not asserted as new. Broader formulas elsewhere might imply the same mixed spectrum; such historical priority has not been exhaustively resolved.

## Limitations
Only the split quartic polynomial with roots zero and one, both of multiplicity two, is treated; the argument does not classify arbitrary repeated-root polynomials or arbitrary triangular conjugacy orbits. The formula is a finite-field point-count and Jordan-type classification, not a description of scheme-theoretic nilpotents or an independent review. Historical priority remains a limitation.

## References
- Shalosh B. Ekhad and Doron Zeilberger, *An Explicit Formula for the Number of Solutions of X^2=0 in Triangular Matrices over a Finite Field*, arXiv:math/9512224v1 (19 December 1995), https://arxiv.org/abs/math/9512224.
- Martha Yip, *Rook Placements and Jordan Forms of Upper-Triangular Nilpotent Matrices*, Electronic Journal of Combinatorics 25(1) (2018), P1.68, DOI:10.37236/6888, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i1p68.
- Ivan Gargate and Michael Gargate, *How to construct a upper triangular matrix that satisfy the quadratic polynomial equation with different roots*, arXiv:2008.11272v1 (2020), https://arxiv.org/abs/2008.11272.
- Ivan Gargate and Michael Gargate, *(k+1)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243v1 (2020), https://arxiv.org/abs/2009.04243.
