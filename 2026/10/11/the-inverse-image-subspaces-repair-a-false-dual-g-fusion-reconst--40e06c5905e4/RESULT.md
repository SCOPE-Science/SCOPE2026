# The inverse-image subspaces repair a false dual \(g\)-fusion reconstruction

## Finding
Theorem 3.8 of Ghosh--Samanta, *Stability of dual \(g\)-fusion frames in Hilbert spaces*, asserts that its constructed \(g\)-fusion frame on image subspaces \(T W_j\) is an exact dual. The two claimed reconstruction identities fail already for two nonorthogonal lines.

The correction does not require changing the coefficient operators. It replaces the support \(T W_j\) by the *inverse weighted frame-operator image* \(U W_j\), where \(U=T^*S_\Gamma^{-1}T\). This gives both exact reconstruction identities and quantitative frame bounds under all the original uniform invertibility hypotheses.

For any normalized finite Riesz basis, the paper's uncorrected reconstruction operator is exactly the *original frame operator*, not the identity. Its worst-case operator-norm reconstruction error is the norm of the Gram matrix minus the identity.

## Assumptions and scope
Let \(H\) and \(H_j\) be complex Hilbert spaces, and \(J\) a finite or countable index set. Assume \(\Lambda=\{(W_j,\Lambda_j,v_j)\}_{j\in J}\) is a \(g\)-fusion frame, with positive weights \(v_j\), closed subspaces \(W_j\subset H\), bounded maps \(\Lambda_j:H\to H_j\), and bounds \(0<A\le B<\infty\):
\[
A\|f\|^2\le\sum_jv_j^2\|\Lambda_jP_{W_j}f\|^2\le B\|f\|^2\quad(f\in H).
\]
Let \(T\in\mathrm{GL}(H)\) and \(T_j\in\mathrm{GL}(H_j)\), with constants \(0<m\le M<\infty\) such that
\[
\frac1{\|T_j^{-1}\|}\ge m,\qquad \|T_j\|\le M\qquad (j\in J).
\]
The paper also requires commutation with an operator \(K\) when considering \(K\)-frames; here its theorem assumes an ordinary \(g\)-fusion frame, corresponding to \(K=I\), so that condition is automatic.

Define the weighted positive operator
\[
C=\sum_jv_j^2P_{W_j}\Lambda_j^*T_j^*T_j\Lambda_jP_{W_j}.
\]
The bounds on the original family and on the \(T_j\) imply
\[
m^2AI\le C\le M^2BI.
\]
Thus \(C\) and \(U=C^{-1}\) are bounded, positive, self-adjoint, and invertible.

## Proof
**The source operator is the inverse of \(C\).** The paper defines the auxiliary \(g\)-fusion frame \(\Gamma\) with support \(T W_j\) and operators \(\Gamma_j=T_j\Lambda_jP_{W_j}T^*\). The standard identity
\[
P_{W_j}T^*P_{TW_j}=P_{W_j}T^*
\]
shows that its frame operator is
\[
S_\Gamma=TCT^*.
\]
Consequently the paper's own definition gives
\[
U=T^*S_\Gamma^{-1}T=C^{-1}.
\]
Set \(L_j=T_j^*T_j\) and \(\Delta_j=L_j\Lambda_jP_{W_j}U\), just as in the source.

**Correct image subspaces.** Because \(U\) is positive and invertible, \(\widehat W_j=U W_j\) is closed. The orthogonal-projection identity with the operator \(U=U^*\) gives
\[
P_{W_j}UP_{UW_j}=P_{W_j}U.
\]
Therefore
\[
\Delta_jP_{UW_j}=L_j\Lambda_jP_{W_j}UP_{UW_j}=\Delta_j.
\]
The uniform bounds for \(T_j\) yield \(m^2\|y\|\le\|L_jy\|\le M^2\|y\|\), so
\[
m^4A\|Uf\|^2\le\sum_jv_j^2\|\Delta_jP_{UW_j}f\|^2\le M^4B\|Uf\|^2.
\]
Using \(\|Uf\|\ge\|f\|/\|U^{-1}\|=\|f\|/\|C\|\) and \(\|Uf\|\le\|U\|\|f\|\) gives the claimed positive frame bounds.

**Both dual identities.** By the definition of \(C\),
\[
\begin{aligned}
\sum_jv_j^2P_{W_j}\Lambda_j^*\Delta_jP_{UW_j}
&=\sum_jv_j^2P_{W_j}\Lambda_j^*L_j\Lambda_jP_{W_j}U\\
&=CU=I.
\end{aligned}
\]
Taking adjoints gives the second identity
\[
\sum_jv_j^2P_{UW_j}\Delta_j^*\Lambda_jP_{W_j}=I.
\]
For countable \(J\), both mixed series converge unconditionally on each vector because both analysis families are Bessel and the mixed synthesis is the product of their bounded analysis and synthesis operators.

**Exact obstruction for Riesz bases.** Let \(d\ge2\) and choose unit vectors \(u_1,\ldots,u_d\) forming a basis of \(\mathbb C^d\). Put \(P_j=u_ju_j^*\), \(F=[u_1\ \cdots\ u_d]\), \(\Lambda_j=P_j\), \(W_j=\operatorname{Ran}P_j\), \(v_j=1\), and \(T=T_j=I\). Then \(S=FF^*=\sum_jP_j\), \(U=S^{-1}\), and \(\Delta_j=P_jS^{-1}\). Since
\[
F^*S^{-1}F=I_d,
\]
its diagonal entries give
\[
P_jS^{-1}P_j=P_j.
\]
The original support in Theorem 3.8 is \(T W_j=W_j\). Thus the source's two reconstruction operators are both
\[
D=\sum_jP_jS^{-1}P_j=\sum_jP_j=S.
\]
Because the polar decomposition of invertible \(F\) makes \(FF^*\) and \(F^*F\) unitarily similar,
\[
\|D-I\|=\|FF^*-I\|=\|F^*F-I\|.
\]
This is zero exactly when the normalized basis is orthonormal. In dimension two, with \(c=|\langle u_1,u_2\rangle|\), the Gram spectrum is \(1-c,1+c\), giving the exact error \(c\).

For a rational two-dimensional witness, take
\[
P_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
P_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Then
\[
S=\begin{pmatrix}3/2&1/2\\1/2&1/2\end{pmatrix},\quad
S^{-1}=\begin{pmatrix}1&-1\\-1&3\end{pmatrix},
\]
and both claimed identities output \(Sf\), not \(f\). On \(e_1\), the source formula yields \((3/2,1/2)\) instead of \((1,0)\).

## Verification
The primary source's journal version and open preprint were read at Theorem 3.5, Remark 3.7, Theorem 3.8, and their operator formulas and proofs, including rendered theorem and proof pages. The journal and preprint state the same two identities with subspaces \(T W_j\). The published proof replaces \(P_{W_j}UP_{TW_j}\) by \(P_{W_j}U\), citing a projection identity whose valid image subspace for the operator \(U\) is instead \(U W_j\).

An exact symbolic matrix check confirms the two-line example and the corrected construction under nonidentity auxiliary transforms; the algebraic proof above is independent of that check. All operator-series claims follow from standard Hilbert-space Bessel bounds, not finite computations.

## Relationship to prior work
Heineken--Morillas establish the canonical dual fusion-frame support \(S^{-1}W_j\) and prove that for a Riesz fusion basis a block-diagonal dual with equally dimensional supports must use these inverse images (Proposition 3.7). This is a strong structural predecessor: it already warns that unchanged nonorthogonal subspaces cannot generally support the desired componentwise duality. It does **not** give the specific failed reconstruction operator in Ghosh--Samanta Theorem 3.8, the exact Gram-error formula for that construction, or the uniform \(T_j\)-weighted correction above.

Ahmadi--Rahimlou--Sadri--Zarghami Farfar formulate canonical \(K\)-\(g\)-fusion duals with inverse-image subspaces and prove reconstruction under the corresponding projections. Their work supplies the correct general projection principle. The new statement isolates its precise failure in a later proposed construction and gives a repair for the later theorem's full family of independently transformed local operators.

## Limitations
This result refutes the exact dual identities claimed on \(T W_j\), **not** the existence of a \(g\)-fusion frame on those subspaces in every case. The two-line witness even leaves that family a valid \(g\)-fusion frame, while disproving duality.

The corrected support \(U W_j\) is sufficient and canonical for the given coefficient maps; it is not asserted to be the unique possible dual support. The stated frame bounds are valid universal estimates, not claimed optimal for arbitrary \(T_j\). The Gram-error classification concerns normalized finite Riesz bases, not arbitrary redundant systems.

The open preprint carries an exact submission date in February 2021; an earlier 2020 journal issue also exists, but a day-specific first-online date for the journal edition was not established. The exact day used for the source date is therefore that of the independently verified public preprint record, not a fabricated journal day.

## References
1. P. Ghosh and T. K. Samanta, *Stability of dual \(g\)-fusion frames in Hilbert spaces*, Methods of Functional Analysis and Topology 26(3) (2020), 227--240, DOI 10.31392/MFAT-npu26_3.2020.04; open manuscript arXiv:2103.02593v1, publicly submitted 17 February 2021.
2. S. B. Heineken and P. M. Morillas, *Properties of finite dual fusion frames*, Linear Algebra and its Applications 476 (2015), 39--57, DOI 10.1016/j.laa.2014.04.008; arXiv:1509.07724.
3. R. Ahmadi, G. Rahimlou, V. Sadri and R. Zarghami Farfar, *Constructions of \(K\)-\(g\)-fusion and their dual in Hilbert spaces*, Bulletin of the Transilvania University of Brașov, Series III 13(62)(1) (2020), 17--32, DOI 10.31926/but.mif.2020.12.61.1.2.
