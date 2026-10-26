# Sharp universal coefficient for qubit half-information exclusion

## Finding

Let \(C\) be any finite classical label and let \(\{p_j,\rho_j\}\) be an arbitrary ensemble of qubit states. Write \(\chi(C:Q)=S(\bar\rho)-\sum_jp_jS(\rho_j)\) for its Holevo information. Let \(I(C:X)\) and \(I(C:Z)\) denote the classical mutual informations obtained by measuring each state in two complementary Pauli bases. Define

\[
A(s)=\frac{\operatorname{artanh}\sqrt{s}}{\sqrt{s}},\qquad a_* = \sup_{0<s<1}\left\{\frac{s^2A(s)}{A(s)-1}-2s\right\},\qquad c_* = \frac{1}{1+a_*}.
\]

Then the sharp universal coefficient is \(c_*\): for every such ensemble,

\[
\chi(C:Q)-I(C:X)\ge c_* I(C:Z),
\]

and no coefficient strictly larger than \(c_*\) works for all finite qubit ensembles. The supremum is a positive interior maximum. Numerical maximization places it near \(s=0.4845418\), giving \(c_*\approx0.7906755\); this decimal is illustrative, while the exact claim is the variational formula and proof below. In particular, \(c_*>1/2\), improving the coefficient used in the recent qubit half-information-exclusion proof.

Combining this sharpened ensemble inequality in the two orientations of the standard two-qubit argument gives the corollary

\[
I(A:B)\ge I(X_A:X_B)+I(Z_A:Z_B)+(2c_*-1)I(X_A:Z_B),
\]

for every two-qubit state, where each \(I(\cdot:\cdot)\) on the right is the mutual information of the indicated measurement outcomes. The cross-basis term is available when the \(X\)-on-\(A\), \(Z\)-on-\(B\) outcome table is measured.

## Assumptions and scope

All entropies use base-two logarithms. A qubit state is represented by \(\rho(\mathbf v)=(\mathbf 1+\mathbf v\cdot\boldsymbol\sigma)/2\), with Bloch vector \(\mathbf v=(x,y,z)\) in the closed unit ball. The ensemble is finite, the label probabilities are arbitrary, and conditional states may be pure or mixed. \(X\) and \(Z\) are orthogonal Pauli axes; the result does not assert the same constant for nonorthogonal measurements, arbitrary POVMs, or dimensions above two.

Put \(h(t)=H_2((1+t)/2)\), the even binary entropy function. For an ensemble with average Bloch vector \(\bar{\mathbf v}\), direct entropy expansion gives

\[
\chi-I(C:X)-cI(C:Z)=g_c(\bar{\mathbf v})-\sum_jp_jg_c(\mathbf v_j),\qquad g_c(\mathbf v)=h(\|\mathbf v\|)-h(x)-ch(z).
\]

Consequently, the inequality for every finite ensemble is equivalent to concavity of \(g_c\) on the Bloch ball.

## Proof

Work first in the open unit ball, where the Hessian is smooth. Multiplying its entries by the common positive factor \(\ln 2\) does not affect semidefinite signs. Set \(s=\|\mathbf v\|^2\), \(A=\operatorname{artanh}(\sqrt{s})/\sqrt{s}\), \(B=(1-s)^{-1}\), and \(\mathbf u=\mathbf v/\|\mathbf v\|\). The negative Hessian of the radial entropy \(h(\|\mathbf v\|)\) is

\[
R=A\mathbf 1+(B-A)\mathbf u\mathbf u^{\mathsf T},
\]

which is positive definite. Let \(X_0=x^2\), \(Y=y^2\), \(Z=z^2\), and

\[
\delta(s)=\frac{1-A^{-1}}{s},\qquad \delta(0)=\frac13.
\]

The inverse radial-curvature matrix is \(R^{-1}=A^{-1}\mathbf 1-(1-\delta)\mathbf v\mathbf v^{\mathsf T}\). The remaining coordinate curvatures of \(-\nabla^2g_c\) are \((1-X_0)^{-1}\) in the \(x\)-direction and \(c(1-Z)^{-1}\) in the \(z\)-direction. By the Schur-complement criterion, \(-\nabla^2g_c\succeq0\) is equivalent to positive semidefiniteness of

\[
Q_c=\begin{pmatrix}
\delta(Y+Z)&(1-\delta)xz\\
(1-\delta)xz&(1/c-1)(1-Z)+\delta(X_0+Y)
\end{pmatrix}.
\]

Write \(a=1/c-1\). Its diagonal entries are nonnegative for \(0<c\le1\), and direct expansion gives

\[
\det Q_c=\delta a(Y+Z)(1-Z)+\delta^2Y s-(1-2\delta)X_0Z.
\]

The power series \(A(s)=\sum_{n\ge0}s^n/(2n+1)\), together with \(3^n\ge2n+1\), implies \(A(s)\ge(1-s/3)^{-1}\), hence \(\delta(s)\ge1/3\). When \(Y+Z>0\), the determinant condition is \(a\ge F\), where

\[
F=\frac{(1-2\delta)X_0Z-\delta^2Ys}{\delta(Y+Z)(1-Z)}.
\]

If \(\delta\ge1/2\), then \(F\le0\). If \(\delta<1/2\), then

\[
F\le\frac{1-2\delta}{\delta}\frac{X_0Z}{(Y+Z)(1-Z)}
\le\frac{1-2\delta}{\delta}\frac{X_0}{1-Z}
\le\frac{s(1-2\delta)}{\delta}.
\]

The last inequality follows from \(X_0\le s-Z\) and \((s-Z)/(1-Z)\le s\). This upper bound is sharp as a supremum at fixed \(s\): take \(Y=0\), \(X_0=s-Z\), and let \(Z\downarrow0\) through positive values. Therefore the supremum of the required value of \(a\) over the Bloch ball is exactly

\[
a_* = \sup_{0<s<1}\frac{s(1-2\delta(s))}{\delta(s)}
=\sup_{0<s<1}\left\{\frac{s^2A(s)}{A(s)-1}-2s\right\}.
\]

For \(a\ge a_*\), the determinant and both diagonal entries of \(Q_c\) are nonnegative, including the limiting \(x\)-axis case \(Y=Z=0\). Thus \(g_c\) is concave in the open ball and, by continuity and radial approximation, on the closed ball. Taking \(a=a_*\), equivalently \(c=c_*\), proves the inequality for every finite ensemble.

Conversely, if \(c>c_*\), then \(a<a_*\). Choose an \(s\) for which \(s(1-2\delta)/\delta>a\), then choose small \(Z>0\), \(Y=0\), and \(X_0=s-Z\). The determinant is negative at this interior point, so \(g_c\) has a negative-curvature direction and is not concave. A sufficiently small symmetric two-state ensemble with Bloch vectors \(\mathbf v\pm\varepsilon\mathbf w\) along that direction violates the inequality. Hence \(c_*\) is optimal.

Finally, \(\delta(s)\to1/3\) and the expression for \(a_*\) tends to zero as \(s\downarrow0\); as \(s\uparrow1\), it tends to \(-1\). It is positive for sufficiently small positive \(s\), and every positive value is less than \(s<1\). Thus \(0<a_*<1\), so \(1/2<c_*<1\).

For the two-qubit corollary, apply the sharpened inequality to Bob's ensemble conditioned on Alice's \(X\) outcome, and then to Alice's ensemble conditioned on Bob's \(Z\) outcome with the axes exchanged. Adding gives

\[
\chi(X_A:B)+\chi(Z_B:A)-I(X_A:X_B)-I(Z_A:Z_B)\ge2c_*I(X_A:Z_B).
\]

Data processing under local dephasing gives \(I(A:B)+I(X_A:Z_B)\ge\chi(X_A:B)+\chi(Z_B:A)\). Combining these inequalities yields the stated strengthened two-qubit bound.

## Verification

The proof is analytic: the ensemble identity reduces the universal statement to concavity, and the Schur-complement determinant controls every interior Bloch vector. The upper bound on the determinant requirement is matched by the explicit limiting family \((X_0,Y,Z)=(s-Z,0,Z)\) as \(Z\downarrow0\); this establishes sharpness of the variational constant rather than relying on finite sampling. The numerical decimal is not used in any proof step. Boundary states are covered by continuity.

## Relationship to prior work

Wang, Wang, and Chen prove the qubit half-information-exclusion inequality with coefficient \(1/2\) as a lemma in their 2026 paper on complementary quantum correlations. Their proof uses the same Bloch-ball entropy and Schur-complement strategy but does not optimize the coefficient in the inspected text. The present result solves that one-dimensional optimization exactly as a supremum and proves its optimality. The resulting cross-basis corollary sharpens their two-qubit correlation accounting when the cross measurement table is available.

Schneeloch, Broadbent, and Howell introduced the complementary-quantum-correlation relation and established several special cases. Iqbal's 2026 paper gives sufficient conditions for CQC and an extension to more mutually unbiased bases. Qian's 2026 counterexample study proves CQC fails in several higher-dimensional settings, records the two-qubit case as valid, and gives a different state-dependent corrected inequality; its correction is not the one-sided coefficient optimization proved here. Hall's information-exclusion principle is related in theme but treats different information quantities. None of the inspected statements supplies the optimal coefficient above. This is a best-knowledge comparison, not a claim that every potentially relevant publication has been ruled out.

## Limitations

The exact constant is expressed as a one-variable supremum; no elementary closed form or proof of uniqueness of the numerical maximizer is claimed. The decimal value is a numerical approximation, not a certified interval. The theorem is limited to finite ensembles of qubit states and complementary Pauli projective measurements. It does not cover nonorthogonal axes, generalized measurements, higher dimensions, or finite-sample experimental corrections. The foundational 2014 CQC paper's full text was not accessible during this check; its available abstract reports special-case CQC results, so this remains a limited literature-access risk.

## References

1. J. Wang, Q. Wang, and K. Chen, “Complementary Quantum Correlations Are Universal for Qubits,” arXiv:2608.04916v1 (first public version 2026-08-05).
2. H. Iqbal, “On the CQC conjecture: a sufficient condition and an extension,” *Quantum Information Processing* 25, 250 (2026), DOI: 10.1007/s11128-026-05258-2.
3. J. Schneeloch, C. J. Broadbent, and J. C. Howell, “Uncertainty Relation for Mutual Information,” *Physical Review A* 90, 062119 (2014), arXiv:1404.6496.
4. M. J. W. Hall, “Information Exclusion Principle for Complementary Observables,” *Physical Review Letters* 74, 3307–3311 (1995), DOI: 10.1103/PhysRevLett.74.3307.
5. L. Qian, “Separable Counterexamples to Complementary Quantum Correlations, and Why Random Search Missed Them,” arXiv:2608.14806v2 (2026-08-19).
