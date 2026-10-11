# The canonical \(K\)-\(g\)-fusion dual formula fails without \(S_\Lambda\)-invariance of \(R(K)\)

## Finding
The canonical-dual construction in Theorem 3.3 of Sadri--Ahmadi--Rahimi is false for a general closed-range operator \(K\). The same formula appears as Theorem 8 in the later journal version.

Put
\[
R=R(K),\qquad
C=S_\Lambda|_R:R\longrightarrow S_\Lambda(R).
\]
The source proves that \(C\) is a homeomorphism and then starts its canonical-dual proof with
\[
Kf=S_\Lambda(C^{-1})^*Kf.
\]
That equality does not follow from
\[
C^{-1}C=I_R.
\]
The adjoint reverses the two Hilbert spaces: the automatic identity is
\[
C^*(C^{-1})^*=I_R,
\]
where
\[
C^*=P_RS_\Lambda|_{S_\Lambda(R)}.
\]
Thus a projection onto \(R\) is missing unless \(R\) is invariant under \(S_\Lambda\).

In fact, the source's first reconstruction equality is valid for every \(f\) exactly when
\[
S_\Lambda R(K)\subseteq R(K).
\]

## Assumptions and scope
Let \(H\) be a Hilbert space, \(K\in\mathcal B(H)\) have closed range, and let \(\Lambda\) be a \(K\)-\(g\)-fusion frame with positive self-adjoint frame operator \(S_\Lambda\). The source's lower bound implies that
\[
C=S_\Lambda|_{R(K)}:R(K)\to S_\Lambda(R(K))
\]
is bounded below and hence is a bounded bijection onto its range with bounded inverse.

The counterexample below is finite-dimensional, has a single closed fusion subspace, and all operators have closed range. Therefore no convergence, domain, or closed-image issue can account for the failure.

The structural equivalence established here concerns the proof's core operator identity. In the general infinite-dimensional formula, the source also writes images of closed subspaces under bounded operators; separate closedness assumptions may be needed to ensure that all proposed fusion subspaces are closed.

## Proof
Take
\[
H=\mathbb C^2,\qquad
K=P_{\operatorname{span}\{e_1\}}.
\]
Use one index with
\[
W_1=H,\qquad v_1=1,\qquad H_1=H,
\]
and define
\[
\Lambda_1=
\begin{pmatrix}
\sqrt2&1/\sqrt2\\
0&\sqrt{3/2}
\end{pmatrix}.
\]
Then
\[
S_\Lambda=\Lambda_1^*\Lambda_1
=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
\]
The eigenvalues of \(S_\Lambda\) are \(1\) and \(3\). Hence, for every \(f\in H\),
\[
\|K^*f\|^2
\le
\|f\|^2
\le
\langle S_\Lambda f,f\rangle
\le
3\|f\|^2.
\]
Thus the family is a \(K\)-\(g\)-fusion frame with admissible bounds \(A=1\) and \(B=3\).

Let
\[
R=R(K)=\operatorname{span}\{e_1\}.
\]
Then
\[
S_\Lambda e_1=2e_1+e_2,
\]
so
\[
S_\Lambda(R)=\operatorname{span}\{2e_1+e_2\}.
\]
For
\[
C=S_\Lambda|_R:R\to S_\Lambda(R),
\]
the normalized vector
\[
q=\frac{2e_1+e_2}{\sqrt5}
\]
satisfies
\[
Ce_1=\sqrt5\,q,\qquad C^{-1}q=\frac1{\sqrt5}e_1.
\]
Taking the adjoint between the two one-dimensional Hilbert spaces gives
\[
(C^{-1})^*e_1=\frac1{\sqrt5}q
=\frac{2e_1+e_2}{5}.
\]
Therefore
\[
S_\Lambda(C^{-1})^*e_1
=
e_1+\frac45e_2
\ne e_1=Ke_1.
\]

For the source's proposed dual, the single fusion subspace is
\[
\widetilde W_1
=
K^*C^{-1}P_{S_\Lambda(R)}H
=
R,
\]
and the single analysis operator is
\[
\widetilde\Lambda_1
=
\Lambda_1P_{S_\Lambda(R)}(C^{-1})^*K
=
\Lambda_1(C^{-1})^*K.
\]
Hence at \(e_1\) the defining dual reconstruction equals
\[
\Lambda_1^*\widetilde\Lambda_1P_{\widetilde W_1}e_1
=
S_\Lambda(C^{-1})^*e_1
=
e_1+\frac45e_2,
\]
which is not \(Ke_1\). This disproves the theorem.

It remains to identify the exact condition behind the failed first equality. Since \(K:H\to R\) is onto,
\[
S_\Lambda(C^{-1})^*K=K
\]
holds if and only if
\[
S_\Lambda(C^{-1})^*y=y
\quad\text{for every }y\in R.
\]
The map \((C^{-1})^*:R\to S_\Lambda(R)\) is onto. For
\[
z\in S_\Lambda(R)
\]
one has
\[
C^*z=P_RS_\Lambda z.
\]
Putting
\[
y=C^*z
\]
shows that the preceding identity is equivalent to
\[
S_\Lambda z=P_RS_\Lambda z
\quad\text{for every }z\in S_\Lambda(R),
\]
or
\[
S_\Lambda^2(R)\subseteq R.
\]
Because \(S_\Lambda^2\) is self-adjoint, an invariant closed subspace \(R\) reduces \(S_\Lambda^2\). Functional calculus then gives reduction, hence invariance, for
\[
S_\Lambda=(S_\Lambda^2)^{1/2}.
\]
Conversely, if \(R\) is invariant under \(S_\Lambda\), self-adjointness makes \(R\) reducing. The restricted operator \(C\) is then a positive self-adjoint bounded-below operator on \(R\), hence invertible on \(R\), and
\[
(C^{-1})^*=C^{-1}.
\]
Therefore
\[
S_\Lambda(C^{-1})^*y=y
\]
for every \(y\in R\). This proves the equivalence.

## Verification
The public preprint was inspected at Remark 1, Definition 5, and the complete statement and proof of Theorem 3.3. Remark 1 defines the inverse as the inverse of
\[
S_\Lambda:R(K)\to S_\Lambda(R(K)).
\]
Definition 5 requires exact reconstruction of \(Kf\). Theorem 3.3 begins its proof with the invalid substitution of \(S_\Lambda\) for the adjoint of this restricted map.

The 2020 journal version was inspected at the corresponding Definition 5 and Theorem 8. It reproduces the same canonical-dual formula and the same first equality.

The matrix identities in the counterexample were checked exactly:
\[
\Lambda_1^*\Lambda_1=
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\]
whose eigenvalues are \(1\) and \(3\), and the failed reconstruction vector is exactly
\[
e_1+\frac45e_2.
\]

## Relationship to prior work
Huang--Yang's 2020 study of \(K\)-\(g\)-fusion frames cites the 2018 construction paper and develops range and stability properties, but the checked material does not supply this correction to the canonical-dual theorem.

Shamsabadi--Arefijamaal--Sadeghi's 2020 theory of \(K\)-fusion duals uses the correct restricted-adjoint identity
\[
Kf=C^*(C^{-1})^*Kf
=
P_{R(K)}S_W(C^{-1})^*Kf.
\]
The explicit projection \(P_{R(K)}\) is exactly what distinguishes that reconstruction from the failed step in the \(K\)-\(g\)-fusion theorem. Their result concerns \(K\)-fusion frames and a different dual definition, so it does not itself provide the present \(K\)-\(g\)-fusion counterexample or the equivalence with \(S_\Lambda\)-invariance.

The broader \(K\)-\(g\)-frame literature treats duality by synthesis-factorization methods rather than by assuming that a restricted inverse is self-adjoint. Targeted searches by theorem number, source identifier, canonical-dual formula, range-invariance terminology, and correction terminology did not locate an indexed correction of Theorem 3.3 or Theorem 8.

## Limitations
The finding refutes the stated canonical \(K\)-\(g\)-fusion dual theorem and exactly characterizes when its first operator identity is valid.

It does not claim that \(S_\Lambda\)-invariance alone settles every topological detail of the theorem's proposed fusion subspaces in infinite dimension. In particular, images of closed subspaces under bounded operators need not be closed without further hypotheses.

A later or unindexed source may contain the same theorem-specific correction.

## References
1. V. Sadri, R. Ahmadi and A. Rahimi, *Construction of \(k\)-\(g\)-fusion frames and their duals in Hilbert spaces*, arXiv:1806.03595v1, 10 June 2018.
2. R. Ahmadi, G. Rahimlou, V. Sadri and R. Zarghami Farfar, *Constructions of \(K\)-\(g\)-fusion and their dual in Hilbert spaces*, Bulletin of the Transilvania University of Brasov, Series III 13(62) (2020), 17--32, DOI 10.31926/but.mif.2020.12.61.1.2.
3. M. Shamsabadi, A. A. Arefijamaal and G. Sadeghi, *Duals and multipliers of \(K\)-fusion frames*, Journal of Pseudo-Differential Operators and Applications 11 (2020), DOI 10.1007/s11868-020-00352-0.
4. Y. Huang and Y. Yang, *\(K\)-\(g\)-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, 57, DOI 10.1186/s13660-020-02320-0.
