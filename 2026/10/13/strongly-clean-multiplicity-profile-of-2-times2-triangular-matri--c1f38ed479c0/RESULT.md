# Strongly clean multiplicity profile of \(2\times2\) triangular matrices over finite fields
## Finding
Let \(q\) be a prime power and let \(T_2(\mathbb F_q)\) be the ring of upper triangular \(2\times2\) matrices. For \(A=\begin{pmatrix}a&b\\0&c\end{pmatrix}\), let \(s(A)\) be the number of idempotents \(E\in T_2(\mathbb F_q)\) such that \(AE=EA\) and \(A-E\) is a unit. Define
\[
\mu(A)=\begin{cases}
1,&a\ne c,\\
q,&a=c\text{ and }b=0,\\
0,&a=c\text{ and }b\ne0.
\end{cases}
\]
Then
\[
s(A)=\mathbf 1_{a\ne0,\,c\ne0}+\mathbf 1_{a\ne1,\,c\ne1}+\mu(A)\big(\mathbf 1_{a\ne1,\,c\ne0}+\mathbf 1_{a\ne0,\,c\ne1}\big).
\]
Consequently, if \(q=2\), every element has exactly one strongly clean decomposition. If \(q>2\), the complete multiplicity distribution is
\[
\#\{A:s(A)=1\}=4q,\qquad
\#\{A:s(A)=2\}=(q-2)(5q-1),
\]
\[
\#\{A:s(A)=4\}=q(q-2)(q-3),\qquad
\#\{A:s(A)=2q+2\}=q-2.
\]
Thus an element is uniquely strongly clean exactly when both diagonal entries lie in \(\{0,1\}\), and for \(q>2\) the maximum multiplicity \(2q+2\) is attained exactly by the scalar matrices \(\lambda I\) with \(\lambda\notin\{0,1\}\).

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\), with \(q\) any prime power. The ring is exactly \(T_2(\mathbb F_q)\), the upper triangular \(2	imes2\) matrix ring. A strongly clean decomposition of \(A\) is written \(A=E+U\), where \(E^2=E\), \(U\) is invertible, and \(EU=UE\). Since \(U=A-E\), the commutation condition is equivalent to \(AE=EA\). The theorem counts the idempotent summands, hence the decompositions, exactly.

## Proof
Write
\[
A=egin{pmatrix}a&b\0&c\end{pmatrix},\qquad E=egin{pmatrix}e&x\0&f\end{pmatrix}.
\]
The equation \(E^2=E\) gives \(e,f\in\{0,1\}\) and
\[
(e+f-1)x=0.
\]
Thus there are four diagonal types. For \((e,f)=(0,0)\) and \((1,1)\), idempotency forces \(x=0\), giving respectively \(E=0\) and \(E=I\). These contribute exactly when \(A\) and \(A-I\) are invertible, namely when \(a,c
e0\) and when \(a,c
e1\).

For \((e,f)=(1,0)\), every \(x\in\mathbb F_q\) gives an idempotent. Direct multiplication shows that \(AE=EA\) is equivalent to
\[
(a-c)x=b.
\]
Also \(A-E\) is invertible exactly when \(a
e1\) and \(c
e0\). Hence this diagonal type contributes one solution if \(a
e c\), contributes \(q\) solutions if \(a=c\) and \(b=0\), and contributes none if \(a=c\) and \(b
e0\). This is precisely \(\mu(A)\) times \(\mathbf 1_{a
e1,\,c
e0}\).

For \((e,f)=(0,1)\), the commutation equation is
\[
(a-c)x=-b,
\]
and \(A-E\) is invertible exactly when \(a
e0\) and \(c
e1\). The same solution count \(\mu(A)\) therefore applies. Summing the four disjoint diagonal types gives the displayed formula for \(s(A)\).

For the distribution, first suppose \(q>2\). There are \(4q\) matrices with both diagonal entries in \(\{0,1\}\), and the formula gives \(s(A)=1\) exactly there. If exactly one diagonal entry lies in \(\{0,1\}\), there are \(4q(q-2)\) matrices and \(s(A)=2\). If \(a=c=\lambda
otin\{0,1\}\), then \(b=0\) gives \(s(A)=2q+2\), while \(b
e0\) gives \(s(A)=2\); these contribute \(q-2\) and \((q-2)(q-1)\) matrices, respectively. Finally, if \(a,c
otin\{0,1\}\) and \(a
e c\), then \(s(A)=4\), on \(q(q-2)(q-3)\) matrices. The four multiplicities sum to \(q^3=|T_2(\mathbb F_q)|\). For \(q=2\), every diagonal entry already lies in \(\{0,1\}\), so \(s(A)=1\) for all eight elements.

## Verification
The proof is symbolic and uses only the four possible diagonal types of a triangular idempotent. The packaged `verify.py` independently enumerates every matrix and every idempotent in \(T_2(\mathbb F_q)\) for \(q=2,3,5,7\), checks commutation and invertibility directly, compares every elementwise count with the formula, and checks the stated multiplicity distribution. Finite enumeration is used only as a consistency check; the proof above establishes the result for every prime power.

## Relationship to prior work
Lee and Zhou introduced the clean index \(\sup_A|\{E:E^2=E,\ A-E\in U(R)\}|\), without the commutation restriction, and studied formal triangular matrix rings. Chen--Gürgün--Köse studied uniquely strongly clean triangular matrix rings and proved global criteria; their full preprint develops existence and uniqueness conditions but does not give a finite-field elementwise multiplicity profile. The older strong-cleanness literature for triangular matrix rings establishes existence under broad hypotheses rather than counts of commuting clean idempotents. The present result is therefore a quantitative refinement on the smallest nontrivial finite triangular ring: it gives every fiber size, the exact global distribution, the uniquely strongly clean locus, and the maximal-multiplicity locus.

## Limitations
Only \(2	imes2\) upper triangular matrices are treated. No formula is asserted for \(T_n(\mathbb F_q)\) with \(n\ge3\), where idempotent equations and commutants interact across several off-diagonal coordinates. The exhaustive checker covers four prime fields; it is not an exhaustive test over all prime powers, and the generality in \(q\) comes from the field-independent proof.

## References
T.-K. Lee and Y. Zhou, *Clean Index of Rings*, Communications in Algebra 40 (2012), 807--822, DOI 10.1080/00927872.2010.538781.

H. Chen, O. Gürgün, and H. Köse, *Uniquely Strongly Clean Triangular Matrix Rings*, arXiv:1307.7339.

G. Borooah, A. J. Diesl, and T. J. Dorsey, *Strongly Clean Triangular Matrix Rings over Local Rings*, Journal of Algebra 312 (2007), 773--797.
