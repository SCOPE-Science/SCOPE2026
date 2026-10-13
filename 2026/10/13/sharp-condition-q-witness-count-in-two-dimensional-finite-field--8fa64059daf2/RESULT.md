# Sharp condition-(Q) witness count in two-dimensional finite-field matrix rings
## Finding
For every odd prime power \(q\), define
\[
w(A)=\#\{U\in\operatorname{GL}_2(\mathbb F_q):A-U\in\operatorname{GL}_2(\mathbb F_q),\ A-U^{-1}\in\operatorname{GL}_2(\mathbb F_q)\}.
\]
Then
\[
\min_{A\in M_2(\mathbb F_q)}w(A)=q^4-3q^3+5q-1.
\]
Equality holds exactly when the characteristic polynomial of \(A\) is irreducible over \(\mathbb F_q\) and \(\operatorname{tr}A\ne0\). In odd characteristic this is equivalent to
\[
\det A\ne0,\qquad \operatorname{tr}A\ne0,\qquad
(\operatorname{tr}A)^2-4\det A	ext{ is a nonsquare in }\mathbb F_q.
\]
Thus the qualitative condition-(Q) theorem for matrix rings has a sharp uniform witness multiplicity in dimension two, and its worst cases are precisely the nonzero-trace anisotropic similarity classes.

## Assumptions and scope
The field is the finite field \(\mathbb F_q\) with \(q\) an odd prime power. A witness for \(A\) means a unit \(U\) for which both differences \(A-U\) and \(A-U^{-1}\) are units. The claim concerns the minimum over all \(2\times2\) matrices, not the full distribution of \(w(A)\), and it does not assert the analogous minimum in higher dimension or in characteristic two.

## Proof
Write \(G=\operatorname{GL}_2(\mathbb F_q)\), so
\[
|G|=(q^2-1)(q^2-q)=q^4-q^3-q^2+q.
\]
First suppose that \(A\) is invertible and nonscalar. Put \(t=\operatorname{tr}A\), \(d=\det A\), and \(D=t^2-4d\). Every such similarity class has the companion representative
\[
A=\begin{pmatrix}0&-d\\1&t\end{pmatrix}.
\]
For invertible \(A\), the set of units \(U\) for which \(A-U\) is singular has size \(q^3-2q\); inversion gives the same size for the condition that \(A-U^{-1}\) is singular. Hence
\[
w(A)=q^4-3q^3-q^2+5q+I(A),
\]
where \(I(A)\) is the number of units for which both differences are singular.

Let
\[
U=\begin{pmatrix}a&b\\c&e\end{pmatrix},\qquad
\delta=\det U\ne0,\qquad x=a+e.
\]
The two singularity equations are
\[
t a+d c-b=d+\delta,\qquad b-dc+t e=d\delta+1,
\]
so
\[
tx=(d+1)(\delta+1).
\]
When \(t\ne0\), fixing \(\delta\) determines \(x\). Eliminating \(b\) and using \(e=x-a\) leaves a quadratic equation in \(a\) whose discriminant, as a polynomial in \(c\), is
\[
P_\delta(c)=D c^2+(2tx-4(d\delta+1))c+x^2-4\delta.
\]
If \(\chi\) is the quadratic character of \(\mathbb F_q\), with \(\chi(0)=0\), the number of solutions for this fixed \(\delta\) is
\[
N_\delta=q+\sum_{c\in\mathbb F_q}\chi(P_\delta(c)).
\]
The discriminant of \(P_\delta\), now regarded as a quadratic in \(c\), factors as
\[
-\frac{16}{t^2}\bigl(t^2-(d+1)^2\bigr)
\bigl(d(\delta+1)^2-t^2\delta\bigr).
\]
If \(D\) is a nonsquare, the first factor \(t^2-(d+1)^2\) is nonzero, while the second quadratic in \(\delta\) has discriminant \(t^2D\) and therefore no root. Thus every \(P_\delta\) has nonzero discriminant and nonsquare leading coefficient. The standard quadratic-character sum gives
\[
N_\delta=q-\chi(D)=q+1
\]
for every \(\delta\ne0\). Therefore
\[
I(A)=(q-1)(q+1)=q^2-1
\]
and consequently
\[
w(A)=q^4-3q^3+5q-1.
\]

It remains to show that every other similarity type has strictly more witnesses. The same quadratic-character calculation gives the following intersection counts for invertible nonscalar matrices:

- if \(t\ne0\), \(D\) is a nonzero square, and \(t^2\ne(d+1)^2\), then \(I(A)=q^2+1\);
- if \(t\ne0\), \(D\) is a nonzero square, and \(t^2=(d+1)^2\), then \(I(A)=(q-1)(2q-1)\);
- if \(D=0\) and \(d\ne1\), then \(I(A)=q^2\);
- if \(D=0\) and \(d=1\), then \(I(A)=2q^2-3q\);
- if \(t=0\) and \(d\ne-1\), then \(I(A)=q^2+q\);
- if \(t=0\) and \(d=-1\), then \(I(A)=q^3-2q\).

Each is strictly larger than \(q^2-1\). This proves the equality characterization among invertible nonscalar matrices.

For completeness, the remaining ranks are elementary. If \(A=0\), every unit is a witness. If \(A=\lambda I\) with \(\lambda\ne0\), then excluding units having eigenvalue \(\lambda\) or \(\lambda^{-1}\) gives
\[
w(\lambda I)=
\begin{cases}
q^4-2q^3-q^2+3q,&\lambda^2=1,\\
q^4-3q^3+6q,&\lambda^2\ne1.
\end{cases}
\]
If \(A\) has rank one and trace zero, direct reduction to \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\) gives
\[
w(A)=q^4-3q^3+2q^2+q.
\]
If \(A\) has rank one and nonzero trace \(s\), reduction to \(\operatorname{diag}(s,0)\) gives
\[
w(A)=q^4-3q^3+q^2+q+
\begin{cases}
(q-1)(2q-1),&s^2=1,\\
(q-1)^2,&s^2\ne1.
\end{cases}
\]
All these values exceed \(q^4-3q^3+5q-1\) for odd \(q\ge3\). Hence the displayed minimum is global.

## Verification
The bundled `verify.py` uses only the Python standard library. It exhausts every matrix and every unit over \(\mathbb F_3\) and \(\mathbb F_5\), checking both the minimum and the equality characterization. It also checks one companion representative of every nonscalar similarity type together with every scalar type over \(\mathbb F_7\) and \(\mathbb F_{11}\), and separately verifies the rank-one formulas. A successful replay prints `VERIFY_OK`.

The computation is a finite consistency check, not the proof for arbitrary prime powers. The all-parameter statement is supplied by the character-sum argument above, which uses only identities valid in every finite field of odd characteristic.

## Relationship to prior work
Wang and Zhou introduced conditions (O), (P), and (Q) for rings of linear transformations and stated that if the division ring has more than two elements then the endomorphism ring satisfies (Q). Their 2012 correction explicitly notes a gap in an earlier lemma, revises the main theorem, and retains the conclusion that \(\operatorname{End}(V_D)\) satisfies (Q) for \(|D|>2\). The present finding asks a different quantitative question in the first nontrivial finite matrix dimension: how many units witness (Q) for a fixed matrix, and what is the sharp minimum over matrices.

Li, Wang, and Zhou subsequently studied the stronger Goodearl--Menal condition with two independently prescribed ring elements. That work is qualitative and classifies rings having the existence property; it does not give a fixed-matrix witness multiplicity. Later finite-field unit-graph work gives exact adjacency parameters for one difference condition such as \(A-U\) being invertible, but it does not control the inverse-coupled simultaneous condition involving \(A-U^{-1}\). A later study of unit stable range one and the Goodearl--Menal condition for individual \(2\times2\) matrices likewise gives qualitative characterizations rather than this finite-field counting law.

## Limitations
The theorem is restricted to odd characteristic. The characteristic-two geometry differs because the discriminant test and quadratic-character sums used in the proof degenerate. No claim is made for \(M_n(\mathbb F_q)\) with \(n>2\), where the two singularity loci have substantially higher-dimensional intersections. The literature comparison found no covering exact count, but absence from the inspected sources and searches is not a proof that no equivalent formulation exists elsewhere.

## References
1. L. Wang and Y. Zhou, “Decomposing Linear Transformations,” *Bulletin of the Australian Mathematical Society* 83 (2011), 256–261. DOI: 10.1017/S0004972710001711. First published online 14 September 2010.
2. L. Wang and Y. Zhou, “Correction to ‘Decomposing Linear Transformations’,” *Bulletin of the Australian Mathematical Society* 85 (2012), 172–173. DOI: 10.1017/S0004972711002644.
3. C. Li, L. Wang, and Y. Zhou, “On Rings with the Goodearl–Menal Condition,” *Communications in Algebra* 40 (2012), 4679–4692. DOI: 10.1080/00927872.2011.618856.
4. Y. D. Karabulut, “Cayley Digraphs of Matrix Rings over Finite Fields,” arXiv:1710.08872.
5. G. Călugăreanu, “On unit stable range one matrices,” arXiv:2104.03994.
