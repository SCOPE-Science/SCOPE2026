# The \(1\)-eigenspace is the exact obstruction in a dual \(g\)-frame criterion
## Finding
Let \(\Lambda=(\Lambda_i)_{i\in I}\) be a \(g\)-frame on a Hilbert space \(H\), with frame operator \(S=T_\Lambda T_\Lambda^*\). Fix a dual \(g\)-frame \(\Omega\), and let \(\Gamma\) be a \(g\)-Bessel family. Define the duality defect
\[
X:=T_\Lambda T_{\Gamma-\Omega}^*=\sum_{i\in I}\Lambda_i^*(\Gamma_i-\Omega_i).
\]
Then \(\Gamma\) is a dual of \(\Lambda\) if and only if \(X=0\). The orthogonality condition in Theorem 3.1 of Rajeswari and George (2022) is instead equivalent to
\[
(I-S^{-1})X=0,
\]
so it detects duality only modulo
\[
E_1:=\ker(S-I).
\]
Equivalently, the published condition says exactly that \(R(X)\subseteq E_1\). Therefore its converse is valid for every \(g\)-Bessel \(\Gamma\) if and only if \(E_1=\{0\}\), that is, if and only if \(1\) is not an eigenvalue of \(S\).

The converse fails even for a two-dimensional non-Parseval ordinary frame. On \(H=\mathbb C^2\), let
\[
\Lambda_1(x_1,x_2)=x_1,\qquad \Lambda_2(x_1,x_2)=\sqrt2\,x_2.
\]
Then \(S=\operatorname{diag}(1,2)\), and the canonical dual is
\[
\Omega_1(x_1,x_2)=x_1,\qquad \Omega_2(x_1,x_2)=x_2/\sqrt2.
\]
Take
\[
\Gamma_1(x_1,x_2)=2x_1,\qquad \Gamma_2(x_1,x_2)=x_2/\sqrt2.
\]
The family \(\Gamma\) is itself a \(g\)-frame, with bounds \(1/2\) and \(4\). Moreover,
\[
\Lambda_1-\Lambda_1S^{-1}=0,\qquad
\Lambda_2-\Lambda_2S^{-1}=(x_1,x_2)\mapsto x_2/\sqrt2,
\]
while \(\Gamma_1-\Omega_1=(x_1,x_2)\mapsto x_1\) and \(\Gamma_2-\Omega_2=0\). Hence the two difference families are orthogonal in the paper's sense. Nevertheless,
\[
\sum_i\Lambda_i^*\Gamma_i=\operatorname{diag}(2,1)\ne I,
\]
so \(\Gamma\) is not a dual of \(\Lambda\).

## Assumptions and scope
The statement uses the standard \(g\)-frame conventions in the cited paper: \(T_\Lambda\) denotes synthesis, \(T_\Lambda^*\) analysis, and duality means \(T_\Lambda T_\Gamma^*=I\). Orthogonality of two \(g\)-Bessel families means that the mixed synthesis-analysis operator is zero. No finite-dimensional assumption is needed for the structural characterization; finite dimension is used only for the explicit counterexample.

The exact boundary is point spectrum, not full spectrum. If \(1\) lies in the continuous spectrum of \(S\) but is not an eigenvalue, then \(I-S^{-1}\) need not be boundedly invertible, yet it is injective, which is already enough for the orthogonality condition to force \(X=0\).

## Proof
Because \(\Omega\) is a dual,
\[
T_\Lambda T_\Omega^*=I.
\]
Therefore
\[
T_\Lambda T_\Gamma^*-I
=T_\Lambda(T_\Gamma^*-T_\Omega^*)
=X,
\]
and \(\Gamma\) is a dual exactly when \(X=0\).

Let \(D_i=\Gamma_i-\Omega_i\). Since \(S\) is positive and invertible,
\[
(\Lambda_i-\Lambda_iS^{-1})^*
=(I-S^{-1})\Lambda_i^*.
\]
Consequently the paper's orthogonality condition is
\[
0=\sum_i(\Lambda_i-\Lambda_iS^{-1})^*D_i
=(I-S^{-1})\sum_i\Lambda_i^*D_i
=(I-S^{-1})X.
\]
Also
\[
\ker(I-S^{-1})=\ker(S-I)=E_1,
\]
so the condition is equivalent to \(R(X)\subseteq E_1\). If \(E_1=\{0\}\), this implies \(X=0\), hence duality.

Conversely, suppose \(E_1\ne\{0\}\). Choose a nonzero bounded operator \(X:H\to E_1\). The synthesis operator \(T_\Lambda\) is surjective, and
\[
R_0:=T_\Lambda^*S^{-1}
\]
is a bounded right inverse because \(T_\Lambda R_0=SS^{-1}=I\). Put \(U=R_0X\). Writing \(U\) in coordinate maps gives a \(g\)-Bessel family \(D\) with \(T_D^*=U\). For \(\Gamma=\Omega+D\), one has
\[
T_\Lambda T_{\Gamma-\Omega}^*=T_\Lambda U=X\ne0,
\]
so \(\Gamma\) is not a dual, while \((I-S^{-1})X=0\) because \(R(X)\subseteq E_1\). Thus the printed criterion cannot characterize all duals when \(1\) is an eigenvalue.

The concrete \(\mathbb C^2\) example above verifies this failure with both \(\Lambda\) and \(\Gamma\) genuine \(g\)-frames rather than merely Bessel families.

## Verification
For the counterexample,
\[
\sum_{i=1}^2|\Lambda_i x|^2=|x_1|^2+2|x_2|^2,
\]
so the frame bounds are \(1\) and \(2\), and \(S=\operatorname{diag}(1,2)\). Likewise
\[
\sum_{i=1}^2|\Gamma_i x|^2=4|x_1|^2+\tfrac12|x_2|^2,
\]
so \(\Gamma\) has bounds \(1/2\) and \(4\). All mixed-operator identities reduce to the displayed diagonal matrices, so no numerical approximation is involved.

The primary source was inspected at its definitions of dual and orthogonal \(g\)-frames and at Theorem 3.1 together with its proof. The proof derives the operator equation \((I-S^{-1})X=0\) and then invokes invertibility of \(I-S^{-1}\); that invertibility does not follow for a general \(g\)-frame. The argument above shows that injectivity is the exact requirement for the claimed converse.

## Relationship to prior work
Rajeswari and George state Theorem 3.1 as a necessary-and-sufficient orthogonality characterization of dual \(g\)-frames. Earlier work by Arefijamaal and Ghasemi studies alternate dual characterizations, and Fu and Zhang characterize approximate dual \(g\)-frames directly through mixed analysis-synthesis operators. Those checked formulations do not imply that \(I-S^{-1}\) is injective, and they do not state the \(1\)-eigenspace obstruction above.

A related earlier paper by Rajeswari and George gives a necessary orthogonality relation for alternate duals; the present result identifies why promoting that type of relation to an unrestricted converse loses exactly the component in \(E_1\).

## Limitations
The result corrects the converse mechanism in Theorem 3.1 of the cited 2022 paper. It does not assert that every later theorem in that paper fails, nor does it classify all alternate duals beyond the stated defect equation. The literature search found no indexed erratum or source stating this exact spectral correction, but an unindexed note or thesis could contain an equivalent observation.

## References
1. K. N. Rajeswari and Neelam George, “G-FRAMES AND THEIR STABILITY IN HILBERT SPACE,” South East Asian Journal of Mathematics and Mathematical Sciences 18(2) (2022), 125–134, DOI 10.56827/SEAJMMS.2022.1802.12.
2. A. Arefijamaal and S. Ghasemi, “On characterization and stability of alternate dual of g-frames,” Turkish Journal of Mathematics 37 (2013), 71–79, DOI 10.3906/mat-1107-14.
3. X. Fu and Z. Zhang, “Characterization and stability of approximately dual g-frames in Hilbert spaces,” Mathematical Foundations of Computing 1 (2018), 281–293.
4. A. Najati, M. H. Faroughi, and A. Rahimi, “G-frames and stability of g-frames in Hilbert spaces,” Methods of Functional Analysis and Topology 14 (2008), 271–286.
