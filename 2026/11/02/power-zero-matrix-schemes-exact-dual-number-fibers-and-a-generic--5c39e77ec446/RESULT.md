# Power-zero matrix schemes: exact dual-number fibers and a generic-reducedness divisibility criterion

## Finding
For every field \(k\) and positive integers \(n,m\), equip the matrix-power-zero locus with its *entry-equation scheme structure*
\[
\mathscr N_{n,m}=\operatorname{Spec}k[x_{ij}:1\le i,j\le n]/((X^m)_{ij}:1\le i,j\le n).
\]
For a point \(A\) of Jordan partition \(\lambda=(\lambda_1,\ldots,\lambda_t)\vdash n\), where every \(\lambda_i\le m\), the rank of the differential of the matrix power map is, in every characteristic,
\[
\boxed{R_m(\lambda)=\sum_{i=1}^t\sum_{j=1}^t\max\{0,\lambda_i+\lambda_j-m\}.}
\]
The Zariski tangent dimension at \(A\) is \(n^2-R_m(\lambda)\). In particular, for any prime power \(q\), every lift \(A+\varepsilon B\) in \(M_n(\mathbb F_q[\varepsilon]/(\varepsilon^2))\) satisfies \((A+\varepsilon B)^m=0\) for precisely \(q^{n^2-R_m(\lambda)}\) choices of \(B\).

There is a sharp geometric consequence. Write \(n=am+r\) with \(a\ge0\) and \(0\le r<m\). The underlying reduced variety is irreducible, with dense nilpotent conjugacy orbit of type \((m^a,r)\) (omitting a zero part); its dimension is
\[
\dim(\mathscr N_{n,m})=n^2-(ma^2+2ar+r).
\]
On this orbit the difference between the scheme tangent dimension and the reduced variety dimension is **exactly**
\[
\boxed{\operatorname{excess}=\min\{r,m-r\}.}
\]
Consequently, the entry-equation scheme \(\mathscr N_{n,m}\) is **generically reduced if and only if \(m\) divides \(n\)**. When \(m\nmid n\), it is generically nonreduced; this statement holds in all characteristics.

For finite fields the resulting exact total census is
\[
\boxed{\#\{C\in M_n(\mathbb F_q[\varepsilon]/(\varepsilon^2)):C^m=0\}
=\sum_{\substack{\lambda\vdash n\\\lambda_1\le m}}
\frac{|\operatorname{GL}_n(\mathbb F_q)|\ q^{n^2-R_m(\lambda)}}{q^{\sum_j(\lambda'_j)^2}\prod_{s\ge1}\prod_{h=1}^{b_s(\lambda)}(1-q^{-h})}.}
\]
Here \(b_s(\lambda)\) is the number of parts of size \(s\), and \(\lambda'\) is the conjugate partition. The formula counts labeled matrices, not conjugacy classes.

## Assumptions and scope
The scheme is defined by the \(n^2\) coordinate entries of \(X^m\) alone, **without imposing** the characteristic-polynomial coefficients or passing to the radical ideal. Over an arbitrary field, its reduced geometric points are nilpotent matrices with largest Jordan block at most \(m\); all matrices are understood after a field extension where needed. The rank and generic geometry statements are valid for every field, including all positive characteristics, \(m=1\), and \(m>n\). The arithmetic formula assumes the split dual-number coefficient ring \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\), not an arbitrary length-two local ring.

The finite-field orbit size is
\[
\frac{|\operatorname{GL}_n(\mathbb F_q)|}{|\operatorname{Aut}_{\mathbb F_q[t]}(\oplus_i\mathbb F_q[t]/(t^{\lambda_i}))|},
\quad |\operatorname{Aut}|=q^{\sum_j(\lambda'_j)^2}\prod_{s\ge1}\prod_{h=1}^{b_s(\lambda)}(1-q^{-h}).
\]
The products are finite and yield integers after cancellation, including for \(n=m=1\).

## Proof
**1. Differential and splitting into ordered Jordan-block pairs.** For arbitrary \(A,B\in M_n(k)\), expansion over dual numbers gives
\[
(A+\varepsilon B)^m=A^m+\varepsilon D_m(A)(B),\qquad
D_m(A)(B)=\sum_{j=0}^{m-1}A^jBA^{m-1-j}.
\]
Thus the tangent space at a power-zero matrix is precisely \(\ker D_m(A)\). Since the rank is similarity-invariant, put \(A\) in Jordan form. The matrix space splits into ordered rectangular blocks, one for every ordered pair \((\lambda_i,\lambda_j)\), each preserved by \(D_m(A)\).

**2. Rank on one rectangular block.** Fix block sizes \(1\le b,c\le m\). The commuting left and right Jordan-shift actions on \(M_{b,c}(k)\) identify it, as a module over two commuting variables, with \(k[u,v]/(u^b,v^c)\). This identification follows directly from a corner matrix unit, whose iterated left and right shifts give every matrix unit exactly once. On this module the block differential is multiplication by
\[
h_m(u,v)=\sum_{j=0}^{m-1}u^jv^{m-1-j}.
\]
Because \((u-v)h_m=u^m-v^m=0\) in the quotient, every monomial multiple of total degree \(s\) agrees with \(u^s h_m\). If \(0\le s\le b+c-m-1\), there is an exponent \(j\) with \(s\le j\le b-1\) and \(0\le m-1+s-j\le c-1\); its monomial has coefficient \(1\), so \(u^s h_m\ne0\) in every characteristic. For larger \(s\), all terms have total degree at least \(b+c-1\), so vanish. The surviving products have pairwise distinct total degrees, hence are linearly independent. Their number is \(\max(0,b+c-m)\). Summing ordered blocks proves the rank formula without assuming that \(m\) is invertible in \(k\).

**3. All dual-number fibers.** A lift \(A+\varepsilon B\) is power-zero exactly when \(A^m=0\) and \(B\) belongs to the computed kernel, a vector space of dimension \(n^2-R_m(\lambda)\). Therefore it contains exactly \(q^{n^2-R_m(\lambda)}\) elements. Over \(\mathbb F_q\), nilpotent similarity classes correspond to partitions, and the automorphism order of the direct sum of cyclic \(\mathbb F_q[t]\)-modules is the product stated above. Multiplying each orbit size by its lift-fiber size and summing produces the exact census.

**4. Dense orbit, dimension and reducedness.** The nilpotent Jordan type \(\lambda^*=(m^a,r)\), with zero remainder omitted, dominates every partition of \(n\) with largest part at most \(m\); the usual nilpotent-orbit closure relation therefore says its conjugacy orbit is dense in the power-zero locus. The orbit is smooth in every characteristic because its matrix centralizer is a vector space and its group centralizer is the smooth open subset of units. The centralizer dimension is the sum of squares of the columns of \(\lambda^*\):
\[
C=\sum_j(\lambda_j^{*\prime})^2=ma^2+2ar+r.
\]
The orbit (and hence the reduced variety) has dimension \(n^2-C\). The rank formula at this partition reads
\[
R_m(\lambda^*)=ma^2+2ar+\max\{0,2r-m\},
\]
so \(C-R_m(\lambda^*)=r-\max\{0,2r-m\}=\min\{r,m-r\}\). If this number is positive, the entry-equation scheme has extra infinitesimal directions at every point of the dense smooth reduced orbit and cannot be generically reduced. If it is zero, the tangent dimension equals the reduced orbit dimension; the local ring at a point of that orbit is regular (embedding dimension equals Krull dimension), so the scheme is reduced there. Thus the scheme is generically reduced precisely when \(r=0\), equivalently \(m\mid n\).

## Verification
The standalone file `check_power_lifts.py` constructs matrix products directly over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), checks the rectangular differential rank by modular Gaussian elimination in 612 cases, and exhaustively enumerates every dual-number matrix in the small stated dimensions. Its result is in `check_output.txt` and ends with `ALL_NILPOTENT_MATRIX_POWER_LIFT_CHECKS_OK`. The exhaustive tests include \(n=3,q=2\) and exponents from two through six. A separate check computes the dense-orbit tangent excess at 72 pairs of positive integers. Finite tests corroborate, but do not replace, the symbolic all-field proof.

## Relationship to prior work
Weyman (2000) determined generators for *reduced nilpotent orbit closures* by combining matrix-power equations with characteristic-polynomial invariants. His reduced equation ideal is not the entry-equation scheme studied here; indeed its additional invariants are deliberately not imposed. Prasad, Singla and Spallone (first preprint 2012, Section 6.2, formulas (6.9) and the rectangular-block action) already wrote down exactly the linearized power map and its action on matrix units. Neither the existence of the differential nor the Jordan-block decomposition is claimed as new. The contribution is the closed all-block rank formula, the consequent exact uniform dual-number census and the sharp generically reduced versus generically nonreduced divisibility boundary.

Earlier classifications of all square-zero matrices over length-two chain rings, including a finer Smith-stratified census, already imply the specialization \(m=2\) of the arithmetic count; that specialization is not claimed as independently new. A prior published calculation gives the complete **nilpotency-index distribution** for lifts of one Jordan block. It already covers the one-block special case of the finite arithmetic formula, and that special case is not claimed as an independent contribution. The remaining general count treats all Jordan partitions at exponents at least three; the scheme-theoretic divisibility boundary is additional. Exact priority of these deductions among less accessible historical sources remains unverified.

## Limitations
This theorem counts dual-number matrices satisfying one prescribed power equation, not matrices over all length-two local rings, higher-order lifts or similarity classes over dual numbers. It concerns generic reducedness of the **entry-equation scheme**, not global reducedness and not the reduced orbit-closure ideal with characteristic-polynomial conditions. The rank formula may be extractable from earlier blockwise linearization formulas; the assessed mathematical contribution is their combined general arithmetic and generic-scheme consequences. Historical publication priority is provisional, and independent validation has not occurred.

## References
1. J. Weyman, *Two results on equations of nilpotent orbits*, arXiv:math/0006232v1, first posted 2000-06-30. https://arxiv.org/abs/math/0006232
2. A. Prasad, P. Singla and S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157v1, first posted 2012-12-26; see Sections 6.2–6.3 of the later revised version. https://arxiv.org/abs/1212.6157
