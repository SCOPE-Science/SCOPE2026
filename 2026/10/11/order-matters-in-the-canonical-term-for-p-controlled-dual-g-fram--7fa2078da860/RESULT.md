# Order matters in the canonical term for P-controlled dual g-frames
## Finding
Let \(\mathcal H\) be a Hilbert space, let \(\Lambda=\{\Lambda_j\}_{j\in J}\) be a g-frame with ordinary frame operator \(S_\Lambda\), and let \(P\in\mathcal{GL}^+(\mathcal H)\). For the \((P,P)\)-controlled g-frame, write
\[
T_{P\Lambda P}=P T_\Lambda,\qquad S_{P\Lambda P}=P S_\Lambda P.
\]
A \(P\)-controlled dual \(\Gamma\) is defined by
\[
\sum_{j\in J}P\Lambda_j^*\Gamma_j=I_{\mathcal H}.
\]
Theorem 4.3 of Liu--Fu--Tian (2023) places the factor \(P\) on the right of \(S_{P\Lambda P}^{-1}\), namely it uses \(\Lambda_jS_{P\Lambda P}^{-1}P\). That formula is false in general.

The exact parameterization is
\[
\Gamma_j f=(Tf)_j+\Lambda_j P S_{P\Lambda P}^{-1}f,
\qquad T_{P\Lambda P}T=0,
\]
where \(T:\mathcal H\to\bigoplus_{j\in J}\mathcal V_j\) is bounded. The published canonical term \(\Lambda_jS_{P\Lambda P}^{-1}P\) works exactly when
\[
P S_\Lambda=S_\Lambda P.
\]

## Assumptions and scope
The result concerns the literal definition of a \(P\)-controlled dual in Liu--Fu--Tian: \(\Gamma\) is a g-Bessel family satisfying \(\sum_jP\Lambda_j^*\Gamma_j=I\). No commutation between \(P\) and \(S_\Lambda\) is assumed in that definition or in Theorem 4.3. The statement applies to real or complex Hilbert spaces; the explicit counterexample is real and therefore also complex by scalar extension.

## Proof
Because the \((P,P)\)-controlled synthesis operator is \(T_{P\Lambda P}=PT_\Lambda\), its frame operator is
\[
S_{P\Lambda P}=T_{P\Lambda P}T_{P\Lambda P}^*=P S_\Lambda P.
\]
Hence the canonical bounded right inverse of \(T_{P\Lambda P}\) is
\[
R_0=T_{P\Lambda P}^*S_{P\Lambda P}^{-1}
   =T_\Lambda^*P S_{P\Lambda P}^{-1}.
\]
Every bounded right inverse of a surjective bounded operator \(A\) is \(A^*(AA^*)^{-1}+T\) with \(AT=0\). Applying this to \(A=T_{P\Lambda P}\) gives
\[
T_\Gamma^*=T_\Lambda^*P S_{P\Lambda P}^{-1}+T,
\qquad T_{P\Lambda P}T=0,
\]
which is equivalent coordinatewise to the corrected formula in the finding. Conversely, that formula gives
\[
T_{P\Lambda P}T_\Gamma^*
 =T_{P\Lambda P}T+S_{P\Lambda P}S_{P\Lambda P}^{-1}=I,
\]
so it is exactly the family of all \(P\)-controlled duals.

For the published canonical term, set \(T=0\) in its formula. Its reconstruction operator is
\[
P S_\Lambda S_{P\Lambda P}^{-1}P
 =P S_\Lambda P^{-1}S_\Lambda^{-1},
\]
because \(S_{P\Lambda P}^{-1}=P^{-1}S_\Lambda^{-1}P^{-1}\). This equals \(I\) if and only if \(P S_\Lambda P^{-1}=S_\Lambda\), equivalently \(P S_\Lambda=S_\Lambda P\). Thus commutation is the exact boundary for the published order.

For an explicit counterexample take \(\mathcal H=\mathbb C^2\), coefficient spaces \(\mathbb C\),
\[
\Lambda_1(x_1,x_2)=x_1,
\qquad
\Lambda_2(x_1,x_2)=\sqrt2\,x_2,
\]
so \(S_\Lambda=\operatorname{diag}(1,2)\). Let
\[
P=\begin{{pmatrix}}2&1\\1&2\end{{pmatrix}},
\]
which is positive invertible with eigenvalues \(1\) and \(3\). Then
\[
S_{P\Lambda P}=P S_\Lambda P
 =\begin{{pmatrix}}6&6\\6&9\end{{pmatrix}},
\qquad
S_{P\Lambda P}^{-1}P
 =\begin{{pmatrix}}2/3&-1/6\\-1/3&1/3\end{{pmatrix}}.
\]
Thus the published \(T=0\) choice has
\[
\Gamma_1(x_1,x_2)=\frac23x_1-\frac16x_2,
\qquad
\Gamma_2(x_1,x_2)=\sqrt2\left(-\frac13x_1+\frac13x_2\right).
\]
Its mixed reconstruction operator is
\[
\sum_{{j=1}}^2P\Lambda_j^*\Gamma_j
 =P S_\Lambda S_{{P\Lambda P}}^{{-1}}P
 =\begin{{pmatrix}}2/3&1/3\\-2/3&7/6\end{{pmatrix}}
 \ne I.
\]
Therefore it is not a \(P\)-controlled dual, despite satisfying the displayed form in the published theorem with \(T=0\).

## Verification
The counterexample uses only exact \(2\times2\) matrices. Direct multiplication gives \(S_\Lambda=\operatorname{{diag}}(1,2)\), \(S_{{P\Lambda P}}=\begin{{pmatrix}}6&6\\6&9\end{{pmatrix}}\), and the nonidentity mixed operator above. Positivity and invertibility of \(P\) are immediate from its eigenvalues. Since \(P S_\Lambda P\) is positive invertible, \(\Lambda\) satisfies the \((P,P)\)-controlled g-frame hypotheses.

The corrected term can also be checked directly:
\[
P S_{P\Lambda P}^{-1}
=\begin{{pmatrix}}2/3&-1/3\\-1/6&1/3\end{{pmatrix}},
\qquad
P S_\Lambda\bigl(P S_{P\Lambda P}^{-1}\bigr)=I.
\]
No finite experiment is used to infer an infinite statement; the general parameterization is an operator identity.

## Relationship to prior work
Liu, Fu, and Tian define \(P\)-controlled duals by the mixed reconstruction identity and state Theorem 4.3 with the order \(\Lambda_jS_{P\Lambda P}^{-1}P\). Their proof treats the second summand as if it reconstructed the identity, which is exactly the step that fails when \(P\) and \(S_\Lambda\) do not commute.

Forughi, Osgooei, Rahimi, and Javahernia (arXiv:1905.08962v1, 2019) define a canonical controlled g-dual in the equal-control case with the order \(\Lambda_i C S_C^{-1}\), where \(S_C=C^*S_\Lambda C\). For positive \(C=P\), this is the same order as the corrected term \(\Lambda_i P S_{P\Lambda P}^{-1}\), not the order printed in the 2023 theorem. Thus the correction restores the earlier canonical ordering while adding the exact commutation criterion for when the later reversed order happens to work and the full right-inverse parameterization under the later definition.

## Limitations
This finding addresses Theorem 4.3 and the order of the canonical factor under the paper's own definition of \(P\)-controlled dual. It does not audit other equivalence claims in the article. The corrected parameterization is standard right-inverse theory specialized to the controlled synthesis operator. An unindexed erratum, thesis, or informal note could contain the same counterexample or commutation criterion.

## References
1. H.-M. Liu, Y.-L. Fu, Y. Tian, “Controlled g-frames and dual g-frames in Hilbert spaces,” *Journal of Inequalities and Applications* 2023, 64 (2023), doi:10.1186/s13660-023-02972-8. Published 2023-05-02. Primary MSC 42C15.
2. M. Forughi, E. Osgooei, A. Rahimi, M. Javahernia, “An appropriate representation space for controlled G-frames,” arXiv:1905.08962v1 (2019), especially Section 3 and equation (3.2).
