# Exact clean-decomposition multiplicities for \(2\times2\) finite-field matrices
## Finding
For every prime power \(q\) and \(A\in M_2(\mathbb F_q)\), define \(c(A)\) to be the number of clean decompositions \(A=E+U\) with \(E^2=E\) and \(U\in GL_2(\mathbb F_q)\). Equivalently, \(c(A)\) is the number of idempotents \(E\) for which \(A-E\) is invertible.

If \(A=\lambda I\), then
\[
c(A)=\begin{cases}
1,&\lambda\in\{0,1\},\\
q^2+q+2,&\lambda\notin\{0,1\}.
\end{cases}
\]

Now suppose \(A\) is non-scalar. Let \(e(A)\in\{0,1,2\}\) denote the number of \(\mathbb F_q\)-rational eigenlines of \(A\). Define
\[
\epsilon(A)=\mathbf 1_{\det A=0\ \mathrm{or}\ \det(A-I)=0},\qquad
u_0(A)=\mathbf 1_{\det A\ne0},\qquad
u_1(A)=\mathbf 1_{\det(A-I)\ne0}.
\]
Then
\[
c(A)=q^2-1+e(A)-q\epsilon(A)+u_0(A)+u_1(A).
\]
Equivalently,
\[
c(A)=\begin{cases}
q^2+1+e(A),&0,1\text{ are both not eigenvalues},\\
q^2-q+e(A),&\text{exactly one of }0,1\text{ is an eigenvalue},\\
q^2-q+1,&0\text{ and }1\text{ are both eigenvalues}.
\end{cases}
\]

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\), so \(q\) may be any prime power. The decomposition is ordinary clean decomposition: no commutativity condition between \(E\) and \(U\) is imposed. The result is specific to \(2\times2\) full matrix algebras.

## Proof
There are exactly two idempotents of ranks \(0\) and \(2\), namely \(0\) and \(I\). The rank-one idempotents are in bijection with ordered pairs \((L,K)\) of distinct projective lines in \(\mathbb F_q^2\): \(E\) is the projection onto \(L\) along \(K\). Hence there are \((q+1)q\) rank-one idempotents.

For a rank-one idempotent \(E\), \(\operatorname{tr}E=1\) and \(\det E=0\). Writing \(s=\operatorname{tr}A\) and \(d=\det A\), the two-dimensional determinant identity gives
\[
\det(A-E)=d-s+\operatorname{tr}(AE).
\]
Thus \(A-E\) is singular exactly when
\[
\operatorname{tr}(AE)=s-d=:c.
\]
Fix \(L=\langle u\rangle\). For the projection onto \(L\) along a complementary line \(K\), \(\operatorname{tr}(AE)\) is the coefficient of \(u\) in the decomposition of \(Au\) relative to \(L\oplus K\). Therefore the number of bad choices of \(K\) for this fixed \(L\) is: \(q\) if \((A-cI)L=0\); \(0\) if \(L\) is an eigenline with eigenvalue different from \(c\); and \(1\) otherwise, namely \(K=(A-cI)L\).

For non-scalar \(A\), an eigenvalue has exactly one eigenline. Also, with \(\chi_A(t)=t^2-st+d\),
\[
\chi_A(c)=d(d-s+1)=\det A\,\det(A-I).
\]
Hence \(c\) is an eigenvalue exactly when \(\det A=0\) or \(\det(A-I)=0\). The number of bad rank-one idempotents is consequently
\[
(q+1-e(A))+q\epsilon(A).
\]
Subtracting this from \(q(q+1)\), then adding the rank-zero idempotent exactly when \(A\) is invertible and the rank-two idempotent exactly when \(A-I\) is invertible, yields the stated formula.

If \(A=\lambda I\), every rank-one idempotent splits the space into eigenvalues \(\lambda-1\) and \(\lambda\) for \(A-E\). Thus all rank-one idempotents work exactly when \(\lambda\notin\{0,1\}\). The two scalar boundary cases each have only one clean idempotent, while outside the boundary both \(0\) and \(I\) also work, giving \(q(q+1)+2\).

## Verification
The bundled `verify_clean_m2.py` independently enumerates all matrices and all idempotents over the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), compares the direct decomposition count with the formula for every matrix, checks that the number of idempotents is \(q(q+1)+2\), and returns `VERIFY_OK`. These finite checks corroborate but do not replace the uniform proof above.

## Relationship to prior work
Lee and Zhou introduced the clean index \(\operatorname{in}(R)=\sup_a |\mathcal E(a)|\), where \(\mathcal E(a)\) is exactly the set of clean idempotents of \(a\). Their work is ring-wide and organizes small clean-index values; it does not give the elementwise \(2\times2\) finite-field profile above. Chen's full-text paper develops criteria for clean matrices and explicitly illustrates construction of clean decompositions, but the inspected theorem and examples are qualitative rather than an exact count by similarity type. A later dissertation reports clean-index calculations for matrix rings over \(\mathbb Z/n\mathbb Z\); its abstract therefore makes it a close comparison for the maximum of \(c(A)\), but the available abstract does not state an elementwise formula or cover arbitrary extension fields \(\mathbb F_q\).

## Limitations
The result does not address \(M_n(\mathbb F_q)\) for \(n>2\). The full text of the 2018 dissertation was not accessible in this check, so an elementwise formula hidden there remains a residual originality risk; the abstract only claims ring-level index calculations for matrix rings over \(\mathbb Z/n\mathbb Z\). The 2004 paper on clean matrices was also available only through metadata/abstract in this check. No claim of independent validation is made.

## References
1. T.-K. Lee and Y. Zhou, *Clean Index of Rings*, Communications in Algebra 40 (2012), 807–822, DOI 10.1080/00927872.2010.538781.
2. H. Chen, *Clean matrices over commutative rings*, Czechoslovak Mathematical Journal 59 (2009), 145–158, DML-CZ identifier 140469.
3. B. L. Schoonmaker, *Clean Indices of Common Rings*, PhD dissertation, Brigham Young University (2018), ScholarsArchive 7027.
