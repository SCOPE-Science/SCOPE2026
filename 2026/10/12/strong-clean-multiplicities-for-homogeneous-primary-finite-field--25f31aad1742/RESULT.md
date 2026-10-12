# Strong-clean multiplicities for homogeneous primary finite-field matrices
## Finding
Let \(A\in M_n(\mathbb F_q)\), and for each monic irreducible \(f\in\mathbb F_q[t]\) let \(V_f\) be the \(f\)-primary summand of the \(\mathbb F_q[t]\)-module on which \(t\) acts by \(A\). Assume that every nonzero \(V_f\) is homogeneous: \(V_f\cong(\mathbb F_q[t]/(f^{m_f}))^{k_f}\) for integers \(m_f,k_f\ge1\). Put \(Q_f=q^{\deg f}\), and define
\[
H_{m,k}(Q)=\sum_{r=0}^{k}{k\brack r}_Q\,Q^{(2m-1)r(k-r)}.
\]
Then the exact number \(s(A)\) of strongly clean decompositions \(A=E+U\), with \(E^2=E\), \(U\in GL_n(\mathbb F_q)\), and \(EU=UE\), is
\[
s(A)=\prod_{f\notin\{t,t-1\}}H_{m_f,k_f}(Q_f).
\]
The \(t\)-primary summand forces \(E=I\), and the \(t-1\)-primary summand forces \(E=0\). In particular, this replaces the semisimple exponent \(r(k-r)\) by the exact nilpotent-thickness exponent \((2m-1)r(k-r)\). Moreover, without any homogeneity assumption, an arbitrary matrix over \(\mathbb F_q\) has a unique strongly clean decomposition if and only if \(A-A^2\) is nilpotent.

## Assumptions and scope
For each monic irreducible \(f\), the primary module is
\[
V_f=\ker f(A)^N
\]
for any sufficiently large \(N\). The homogeneity hypothesis means that all elementary divisors belonging to the same \(f\) have one common exponent \(m_f\); equivalently, \(V_f\) is a free module of rank \(k_f\) over the finite chain ring
\[
R_f=\mathbb F_q[t]/(f^{m_f}).
\]
No homogeneity is assumed for the final unique-decomposition criterion.

The theorem counts decompositions of a fixed matrix, not similarity classes of matrices. It concerns strong cleanness, so the idempotent and unit are required to commute.

## Proof
A strongly clean decomposition is determined by its idempotent, because \(U=A-E\). The commutation condition \(EU=UE\) is equivalent to \(EA=AE\). Hence \(s(A)\) is the number of idempotents in the centralizer of \(A\) for which \(A-E\) is invertible.

The canonical primary decomposition
\[
V=\bigoplus_f V_f
\]
is preserved by every endomorphism commuting with \(A\). Thus a commuting idempotent is a tuple \((E_f)_f\), and invertibility of \(A-E\) is checked independently on the primary summands. For an idempotent \(E_f\),
\[
V_f=\operatorname{im}E_f\oplus\ker E_f,
\]
and these two summands are \(A\)-invariant. On \(\ker E_f\), \(A-E_f=A\); on \(\operatorname{im}E_f\), \(A-E_f=A-I\).

If \(f=t\), then \(A\) is nilpotent on \(V_f\), so \(A\) cannot be invertible on a nonzero kernel. Therefore \(E_f=I\). If \(f=t-1\), then \(A-I\) is nilpotent, so invertibility forces \(\operatorname{im}E_f=0\), hence \(E_f=0\). For every other irreducible \(f\), both \(t\) and \(t-1\) are units modulo \(f^{m_f}\); consequently both \(A\) and \(A-I\) are invertible on every \(A\)-invariant direct summand of \(V_f\). Thus every idempotent in \(\operatorname{End}_{\mathbb F_q[t]}(V_f)\) is admissible.

Under homogeneity,
\[
\operatorname{End}_{\mathbb F_q[t]}(V_f)\cong M_{k_f}(R_f).
\]
Let \(R=R_f\), let \(Q=Q_f\), let \(m=m_f\), and let \(k=k_f\). Since \(R\) is local, the image and kernel of every idempotent in \(M_k(R)\) are free complementary direct summands. All rank-\(r\) idempotents are conjugate to \(\operatorname{diag}(I_r,0)\), and the stabilizer of this standard idempotent in \(GL_k(R)\) is \(GL_r(R)\times GL_{k-r}(R)\). Therefore their number is
\[
\frac{|GL_k(R)|}{|GL_r(R)|\,|GL_{k-r}(R)|}.
\]
Reduction modulo the maximal ideal gives a surjection \(GL_j(R)\to GL_j(\mathbb F_Q)\) with kernel of size \(Q^{(m-1)j^2}\). Hence
\[
|GL_j(R)|=Q^{(m-1)j^2}|GL_j(\mathbb F_Q)|.
\]
Using
\[
\frac{|GL_k(\mathbb F_Q)|}{|GL_r(\mathbb F_Q)|\,|GL_{k-r}(\mathbb F_Q)|}
={k\brack r}_Q Q^{r(k-r)},
\]
the rank-\(r\) idempotent count becomes
\[
{k\brack r}_Q Q^{(2m-1)r(k-r)}.
\]
Summing over \(r\) and multiplying over the independent neutral primary factors proves the formula.

For the final uniqueness statement, homogeneity is unnecessary. If a neutral primary summand \(V_f\) with \(f\notin\{t,t-1\}\) is nonzero, then choosing \(E_f=0\) or \(E_f=I\) gives two distinct admissible choices, so the strongly clean decomposition is not unique. If only the \(t\)- and \(t-1\)-primary summands occur, the preceding forced-choice argument gives exactly one decomposition. Over a field this condition is equivalent to the minimal polynomial having only powers of \(t\) and \(t-1\) as primary factors, which is equivalent to \(A-A^2\) being nilpotent.

## Verification
The bundled standard-library checker independently tests both the matrix and local-ring steps. It exhaustively enumerates all commuting idempotents for selected matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). The cases include two copies of the irreducible quadratic primary module over \(\mathbb F_2\), mixed \(0\)-, \(1\)-, linear-neutral, and irreducible-quadratic factors over \(\mathbb F_3\), and scalar neutral matrices. It also checks the unique-decomposition criterion for every \(2\times2\) matrix over \(\mathbb F_2\) and \(\mathbb F_3\).

To test the genuinely nonsemisimple exponent directly, the checker enumerates all idempotents in
\[
M_2(\mathbb F_3[u]/(u^2))
\]
and obtains \(110=H_{2,2}(3)\), and all idempotents in
\[
M_2(\mathbb F_2[u]/(u^3))
\]
and obtains \(98=H_{3,2}(2)\). The replay ends with `VERIFY_OK`.

## Relationship to prior work
Fan and Yang study strong cleanness of matrix rings over local rings and related power-series, truncated-polynomial, and trivial-extension constructions. Borooah, Diesl and Dorsey give the broad factorization framework for strongly clean matrix rings and the invariant-summand characterization of strongly clean endomorphisms. These sources address existence rather than the exact number of decompositions of a fixed finite-field matrix. Chen, Gürgün and Kose study ring-wide unique strong cleanness for triangular matrix rings; that setting does not imply the fixed full-matrix multiplicity formula here.

The present result isolates a natural nonsemisimple stratum on which the full multiplicity remains closed-form. The nilpotent thickness \(m\) contributes the factor \(Q^{2(m-1)r(k-r)}\) beyond the residue-field idempotent count, producing the exponent \(2m-1\). The uniqueness corollary needs no homogeneity and gives an elementwise full-matrix criterion.

## Limitations
The explicit product formula assumes that every primary module is homogeneous. When one irreducible factor occurs with several different elementary-divisor exponents, the relevant centralizer is an endomorphism ring of a nonfree finite-length module; counting all of its idempotents requires additional module-type data and is not covered here. The finite computations verify representative cases only; the theorem for all parameters rests on the proof above. An equivalent enumeration could exist under older module-decomposition or centralizer-idempotent terminology not exposed by the searches performed.

## References
1. L. Fan and X. Yang, *On strongly clean matrix rings*, Glasgow Mathematical Journal 48 (2006), DOI: 10.1017/S0017089506003284.
2. G. Borooah, A. J. Diesl and T. J. Dorsey, *Strongly clean matrix rings over commutative local rings*, Journal of Pure and Applied Algebra 212 (2008), DOI: 10.1016/j.jpaa.2007.05.020.
3. H. Chen, O. Gürgün and H. Kose, *Uniquely strongly clean triangular matrices*, Turkish Journal of Mathematics 39 (2015), DOI: 10.3906/mat-1408-13.
