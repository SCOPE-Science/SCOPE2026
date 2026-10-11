# Coefficient-range projections refute an operator invertibility theorem for generalized frames

## Finding
Theorem 4.2 of Kiran Kumar--Upender Reddy claims that a closed-range operator \(T\) must satisfy \(TT^*\) invertible if \(K\) has dense range, \((\Lambda_j)\) is a \(K\)-\(g\)-frame, and both \((T\Lambda_j)\) and \((T^*\Lambda_j)\) are \(K\)-\(g\)-frames. The claim fails already for a Parseval \(g\)-frame on \(\mathbb R^2\).

Let
\[
H=\mathbb R^2,\qquad K=I,
\]
take every coefficient space to equal \(H\), and define
\[
\Lambda_1(x,y)=(x,0),\qquad
\Lambda_2(x,y)=(y,0),\qquad
\Lambda_j=0\quad(j\ge3).
\]
For every \(f=(x,y)\),
\[
\sum_{j\ge1}\|\Lambda_jf\|^2
=
|x|^2+|y|^2
=
\|f\|^2.
\]
Thus \((\Lambda_j)\) is a Parseval \(K\)-\(g\)-frame.

Now put
\[
T=P_{\operatorname{span}\{e_1\}}
=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
Then \(T\) has closed range and \(T=T^*\). Every \(\Lambda_jf\) belongs to \(\operatorname{span}\{e_1\}\), so
\[
T\Lambda_j=\Lambda_j,
\qquad
T^*\Lambda_j=\Lambda_j.
\]
Consequently both transformed families appearing in Theorem 4.2 are again the same Parseval \(K\)-\(g\)-frame. But
\[
TT^*=T
\]
has nontrivial kernel \(\operatorname{span}\{e_2\}\) and is not invertible.

The failure is not tied to these coordinates. If
\[
M_\Lambda=
\overline{\operatorname{span}}
\left(\bigcup_jR(\Lambda_j)\right)
\]
is a proper closed subspace, then choosing \(T=P_{M_\Lambda}\) leaves all coefficient maps unchanged under both \(T\) and \(T^*\). Hence transformed-frame hypotheses can be completely blind to \(T\) on \(M_\Lambda^\perp\).

## Assumptions and scope
The example removes any type ambiguity in the source notation by taking every target coefficient space equal to \(H\), so each composition \(T\Lambda_j\) is a well-defined operator \(H\to H\).

The example also uses \(K=I\), which has dense range, so no pathology of a nonclosed or non-surjective operator range is involved. The index set may be taken to be \(\mathbb N\), exactly as in the theorem, by setting \(\Lambda_j=0\) for \(j\ge3\).

The structural statement \(M_\Lambda=H\) is asserted only as a necessary visibility condition for a universal invertibility conclusion of this postcomposition type. It is not claimed to be sufficient by itself.

## Proof
For the displayed family,
\[
\|\Lambda_1(x,y)\|^2=|x|^2,\qquad
\|\Lambda_2(x,y)\|^2=|y|^2,
\]
and all later terms vanish. Therefore
\[
\sum_{j\ge1}\|\Lambda_jf\|^2=\|f\|^2=\|K^*f\|^2,
\]
which proves the Parseval \(K\)-\(g\)-frame identity.

Since
\[
R(\Lambda_j)\subseteq\operatorname{span}\{e_1\}=R(T)
\]
for every \(j\),
\[
T\Lambda_j=\Lambda_j.
\]
The projection is self-adjoint, so the same identity holds with \(T^*\). Hence both transformed families satisfy exactly the same Parseval identity.

On the other hand,
\[
TT^*=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\]
so \(TT^*e_2=0\). Thus the conclusion of Theorem 4.2 is false.

More generally, suppose all coefficient ranges lie in a proper closed subspace \(M\). For \(T=P_M\),
\[
T\Lambda_j=\Lambda_j=T^*\Lambda_j
\]
for every \(j\). Therefore no hypothesis expressed only through these postcomposed families can distinguish \(P_M\) from the identity on the coefficient data, although \(P_M\) is globally noninvertible.

A clean sufficient repair is available in the ordinary \(g\)-frame specialization. Let
\[
C_\Lambda f=(\Lambda_jf)_j
\]
be the analysis operator and suppose \(C_\Lambda\) is onto the coefficient direct sum. Because an ordinary \(g\)-frame analysis operator is bounded below, onto-ness makes \(C_\Lambda\) boundedly invertible onto that direct sum. Writing
\[
C_{T\Lambda}=D_TC_\Lambda,
\qquad
C_{T^*\Lambda}=D_{T^*}C_\Lambda,
\]
bounded-below estimates for both transformed families imply that \(D_T\) and \(D_{T^*}\) are bounded below. Testing on vectors supported in a single coefficient coordinate shows that \(T\) and \(T^*\) are both bounded below. Therefore \(T\) has closed range, \(T^*\) has trivial kernel, \(R(T)\) is dense and closed, and \(T\) is invertible.

## Verification
The target theorem and proof were inspected in the full article. The source attempts to extend a vector-frame invertibility result to \(K\)-\(g\)-frames. Its proof moves from lower bounds for postcomposed coefficient maps to injectivity and surjectivity statements about \(T^*T\) and \(TT^*\) on the whole ambient space.

The counterexample shows the missing step exactly: the maps \(\Lambda_j\) can take values in one proper coefficient-range subspace, so the transformed frame inequalities never test \(T\) on its orthogonal complement.

The vector-frame predecessor in Ramu--Johnson has a different mechanism. For transformed vectors \(Tf_i\), the analysis coefficients are
\[
\langle f,Tf_i\rangle=\langle T^*f,f_i\rangle,
\]
so a lower \(K\)-frame inequality can directly detect \(N(T^*)\). Postcomposition \(T\Lambda_j\) does not provide that same ambient-space test.

All computations in the counterexample are exact finite-dimensional identities; no numerical experiment or finite approximation is used to justify an infinite-dimensional statement.

## Relationship to prior work
Ramu--Johnson's vector-frame theorem proves an invertibility conclusion under analogous hypotheses for transformed frame vectors. The present counterexample explains why that result does not automatically extend to operator-valued coefficient maps: a whole proper subspace of the coefficient target can contain every \(R(\Lambda_j)\).

The earlier \(K\)-\(g\)-frame literature establishes the definitions, construction methods, and stability theory used by the target paper, but the checked source descriptions do not supply the missing coefficient-range visibility hypothesis or the projection counterexample above.

Targeted searches for the exact article and theorem, the \(TT^*\)-invertibility conclusion, projection-valued coefficient ranges, and postcomposition by closed-range operators did not locate an indexed correction with the same claim.

## Limitations
The necessary condition
\[
M_\Lambda=H
\]
is not asserted to be sufficient. The onto-analysis repair is stated only for the ordinary \(g\)-frame case \(K=I\), where its proof is immediate from bounded-below analysis operators.

No claim is made about unrelated results in the source. An unindexed erratum, thesis remark, or informal correction may contain the same theorem-specific counterexample.

## References
1. N. Kiran Kumar and G. Upender Reddy, *Operators Preserving K-g- Frames*, Turkish Journal of Computer and Mathematics Education 11(3) (2020), 1462--1468, DOI 10.17762/turcomat.v11i3.12958.
2. G. Ramu and P. Sam Johnson, *Frame operators of K-frames*, SeMA Journal 73 (2016), 171--181, DOI 10.1007/s40324-016-0062-4.
3. D. Hua and Y. Huang, *K-g-Frames and Stability of K-g-Frames in Hilbert Spaces*, Journal of the Korean Mathematical Society 53(6) (2016), 1331--1345, DOI 10.4134/JKMS.j150499.
