# Sharp third-step channel frontier and false breakdown in inverse-leading extended Krylov bases

## Finding

At the third basis vector of two inverse-leading extended Krylov procedures, the mixed-channel (MCIL) and split-channel (SCIL) candidates obey an exact scalar residual identity even for **nonsymmetric** invertible matrices. This gives a complete, sharp classification of their local orthogonalization conditioning, identifies a premature mixed-channel breakdown that is not exhaustion of the extended Krylov space, and gives a well-conditioned three-dimensional symmetric indefinite witness.

Let \(A\in\mathbb R^{n\times n}\), \(n\ge3\), be invertible, and let \(v\in\mathbb R^n\) satisfy \(\|v\|_2=1\). Set
\[
\alpha=v^\top A^{-1}v,\qquad
\beta=\|A^{-1}v-\alpha v\|_2>0,\qquad
v_2=\frac{A^{-1}v-\alpha v}{\beta},
\]
\[
Q=I-vv^\top-v_2v_2^\top,\qquad
m_1=v^\top Av,\qquad m_2=\|Av\|_2^2.
\]
Assume \(QAv\ne0\) so that the split-channel procedure can extend the two-dimensional space. For the third candidates \(w_{\rm S}=Av\) and \(w_{\rm M}=Av_2\), define \(\rho_{\rm S}=\|Qw_{\rm S}\|_2/\|w_{\rm S}\|_2\) and \(\rho_{\rm M}=\|Qw_{\rm M}\|_2/\|w_{\rm M}\|_2\), including zero residual ratios for breakdown.

**Exact third-step law:**
\[
Qw_{\rm M}=-\frac{\alpha}{\beta}Qw_{\rm S},\qquad
\gamma_3:=\frac{\rho_{\rm M}}{\rho_{\rm S}}
=\frac{|\alpha|\sqrt{m_2}}{\sqrt{1-2\alpha m_1+\alpha^2m_2}}.
\]
The denominator is strictly positive. Consequently,
\[
\gamma_3<1\quad\Longleftrightarrow\quad2\alpha m_1<1,
\qquad
\gamma_3=1\quad\Longleftrightarrow\quad2\alpha m_1=1,
\qquad
\gamma_3>1\quad\Longleftrightarrow\quad2\alpha m_1>1.
\]
In particular, \(\rho_{\rm M}=0\) exactly when \(\alpha=0\), despite the positive split-channel third residual. This is an algorithmic **false breakdown**, not an intrinsic rank exhaustion of \(\operatorname{span}\{v,A^{-1}v,Av\}\).

There is an exact symmetric indefinite witness with spectral condition number \(5/2\):
\[
A=\operatorname{diag}(-6/5,2,3),\qquad b=(1,1,1)^\top,\qquad v=b/\sqrt3.
\]
For this instance, \(\alpha=0\), \(\beta^2=19/54\), and
\[
\det[b,A^{-1}b,Ab]=28/15\ne0,\qquad
\|QAv\|_2^2=1568/4275,\qquad
\rho_{\rm S}^2=1568/20577.
\]
Thus the SCIL method finds an independent third basis vector, but the MCIL method breaks down at its third orthogonalization. Dimension three is minimal for a **premature third-vector** breakdown because fewer than three independent basis vectors cannot exist in lower dimension.

On the *same* matrix, the starting vectors \(b=(1,1,2)^\top\) and \(b=(1,2,2)^\top\) (normalized before use) give \(\alpha m_1=16/45\) and \(\alpha m_1=47/81\), respectively, and have nonzero split-channel third residuals. Hence both strict conditioning orderings occur for one fixed, well-conditioned symmetric indefinite matrix.

The phenomenon is not isolated: for \(A_t=\operatorname{diag}(-6/5+t,2,3)\) and \(v=(1,1,1)^\top/\sqrt3\), the split residual is nonzero for sufficiently small \(|t|\), and
\[
\alpha(t)=-\frac{25t}{18(6-5t)},\qquad
\lim_{t\to0}\frac{\gamma_3(t)}{|t|}=\frac{95}{108\sqrt3}.
\]
Arbitrarily severe **relative** third-step orthogonalization conditioning is therefore possible with matrices whose singular-value condition numbers remain bounded near \(5/2\).

## Assumptions and scope

The conclusions are for exact Euclidean inner products and exact matrix-vector operations. The general formulas require an invertible **real** matrix, a unit initial vector, \(\beta>0\), and \(QAv\ne0\). In the limiting case \(\alpha=0\), \(\gamma_3=0\) is defined through the residual ratios, although no third mixed-channel basis vector can be normalized. The nonsymmetric generalization concerns the third-vector candidate identity only; it does not claim comparable behavior at all later steps.

The phrase 'false breakdown' means only that the chosen recurrence fails even though the next extended Krylov direction exists, not that a floating-point implementation must stop rather than use a look-ahead or switch channel. The instability ratio is a *local* cancellation indicator, not a deterministic bound on the accumulated loss of orthogonality or on downstream matrix-function error.

## Proof

**Step 1 (candidate identity).** Since \(\beta v_2=A^{-1}v-\alpha v\), multiplication by \(A\) gives the **exact** relation
\[
\beta Av_2=v-\alpha Av.
\]
Because \(Qv=0\), applying \(Q\) gives \(QAv_2=-(\alpha/\beta)QAv\). In particular, \(QAv_2=0\) if and only if \(\alpha=0\), given \(QAv\ne0\). No symmetry is used.

**Step 2 (normalizations and sharp frontier).** The identity above yields
\[
\beta^2\|Av_2\|_2^2=\|v-\alpha Av\|_2^2
=1-2\alpha m_1+\alpha^2m_2>0,
\]
because \(Av_2\ne0\) for invertible \(A\). Dividing the residual identity by the two candidate norms gives the formula for \(\gamma_3\). Squaring and subtracting one gives
\[
\gamma_3^2-1=
\frac{2\alpha m_1-1}{1-2\alpha m_1+\alpha^2m_2}.
\]
All denominators are strictly positive and \(\gamma_3\ge0\), establishing all three necessary-and-sufficient comparisons. The \(\alpha=0\) case follows without dividing by \(\alpha\).

**Step 3 (well-conditioned exact witness).** For the displayed diagonal matrix, \(A^{-1}b=(-5/6,1/2,1/3)^\top\) and its components sum to zero, so \(\alpha=0\). Squaring their entries and normalizing by \(\|b\|_2^2=3\) yields \(\beta^2=19/54\). Elementary rational determinant expansion gives \(\det[b,A^{-1}b,Ab]=28/15\), proving that \(QAv\ne0\). Since \(v\) and \(v_2\) are orthonormal, their removal from \(Av\) yields \(\|QAv\|_2^2=1568/4275\). Finally \(\|Av\|_2^2=361/75\), giving \(\rho_{\rm S}^2=1568/20577\). The absolute eigenvalues of \(A\) are \(6/5,2,3\), hence \(\kappa_2(A)=5/2\). By the candidate identity, \(Av_2=v/\beta\) and so the mixed residual vanishes exactly while the split residual does not. For \(n<3\), the dimension bound precludes a distinct third direction, proving minimality.

**Step 4 (two strict sign regimes on one matrix).** For any nonzero \(b\), the normalized starting vector has \(\alpha=(b^\top A^{-1}b)/(b^\top b)\) and \(m_1=(b^\top Ab)/(b^\top b)\). Direct rational substitution for the two stated starting vectors yields \(16/45\) and \(47/81\). The respective determinants \(\det[b,A^{-1}b,Ab]\) are nonzero; thus the split third residual does not vanish, and the strict opposite signs follow from Step 2.

**Step 5 (near-breakdown asymptotic).** Direct evaluation on the perturbed diagonal matrix yields \(\alpha(t)=-25t/[18(6-5t)]\); the determinant from Step 3 is continuous and remains nonzero sufficiently near zero. Therefore the denominator of \(\gamma_3\) tends to one, while \(\sqrt{m_2(t)}\to19/(5\sqrt3)\). The displayed limit follows. Singular values and their ratio vary continuously with \(t\), remaining finite and nonzero near zero.

## Verification

Run `python eksm_step3_check.py` with Python 3, NumPy and SymPy. The included standalone script tests all exact rational identities in Steps 3–5, the determinant assumptions, and the asymptotic coefficient symbolically. It also performs 3,600 seeded **independently projected** third-vector comparisons in three, four, and six dimensions, including definite, indefinite, and nonsymmetric test matrices. Those experiments check the implementation but are not used as proofs of the universal statements.

## Relationship to prior work

Lund and Schweitzer (2026), Algorithms 1–2, distinguish MCIL and SCIL and define the local indicator \(\rho_k\) and ratio \(\gamma_k\). Their Theorem 8 proves a definite-matrix ordering under a no-breakdown hypothesis; Example 10 numerically shows different orderings for a symmetric indefinite eight-dimensional matrix. Their Appendix A, Lemma 16 (particularly its first-cycle recurrence), already relates the corresponding **unnormalized** coefficients, and is the closest known algebraic antecedent. The result here should be read as an explicit third-step *normalized-ratio* classification, including the exact zero coefficient with a still-growing extended Krylov space, a minimal well-conditioned witness and its near-breakdown scaling; no originality is asserted for the basic recurrence itself. The present threshold does not follow from the definite-matrix theorem, and the indefinite numerical examples do not state it.

Druskin and Knizhnerman (1998) introduced economical extended Krylov orthogonalization, while Knizhnerman and Simoncini (2010) studied convergence of matrix-function approximants. Those broader methods are not claimed to be new. Earlier work may implicitly contain the zero-inverse-Rayleigh phenomenon; the closest classic articles' public abstracts, rather than their complete articles, were checked, leaving residual bibliographic uncertainty.

## Limitations

This is a third-vector, exact-arithmetic structural classification only. It neither predicts the ultimate accuracy of a full Krylov computation nor asserts that the local \(\rho\) ratio is an exact floating-point error ratio. Any finite-precision near-zero test requires tolerance selection and may interact with numerical solve accuracy, reorthogonalization, and switching strategies. In exact arithmetic, zero \(\alpha\) makes the MCIL recurrence fail even though SCIL remains valid; modified algorithms might avoid this failure. The 3-by-3 rational example is one explicit witness and does not characterize all indefinite spectra or all higher steps. Restricted-access historical full texts were not independently inspected.

## References

1. K. Lund and M. Schweitzer, *On the stability of basis construction in extended Krylov subspace methods*, arXiv:2610.21603v1, first posted 2026-10-15, https://arxiv.org/html/2610.21603v1 (especially Algorithms 1–2, Theorems 1 and 8, Example 10 and Lemma 16).
2. V. Druskin and L. Knizhnerman, *Extended Krylov Subspaces: Approximation of the Matrix Square Root and Related Functions*, SIAM J. Matrix Anal. Appl. 19 (1998), 755–771, https://doi.org/10.1137/S0895479895292400 (abstract and bibliographic record consulted).
3. L. Knizhnerman and V. Simoncini, *A new investigation of the extended Krylov subspace method for matrix function evaluations*, Numer. Linear Algebra Appl. 17 (2010), 615–638, https://doi.org/10.1002/nla.652 (abstract and bibliographic record consulted).
