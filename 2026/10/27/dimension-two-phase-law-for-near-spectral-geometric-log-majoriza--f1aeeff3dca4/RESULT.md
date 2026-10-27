# Dimension-two phase law for near spectral geometric log-majorization

## Finding

Let \(A,B\) be arbitrary complex Hermitian positive-definite \(2\times2\) matrices. Write \(X\sharp Y\) for their ordinary geometric mean, and set
\[
M=A^{-1}\sharp B,\qquad
N=A^{-1}\star B=A^{-1/2}(B^{1/2}AB^{1/2})^{1/2}A^{-1/2},
\]
where \(\star\) denotes the unweighted near-geometric mean. Compare the weighted spectral and near spectral curves
\[
P_t=A\natural_tB=M^t A M^t,
\qquad Q_t=A\widetilde{\natural}_tB=N^t A N^t
\quad (0\le t\le1).
\]
Then **Conjecture 5.6 of Ibrahim and Huang holds for every pair of positive-definite matrices in dimension two**:
\[
\boxed{Q_t\prec_{\log}P_t\quad (0<t<\tfrac12),\qquad
P_t\prec_{\log}Q_t\quad (\tfrac12<t\le1).}
\]
For \(AB\ne BA\), both comparisons are **strict in their sole nontrivial log-majorization inequality**, throughout the indicated open parameter ranges. At \(t=0\) and \(t=1/2\), the two spectra agree for every input pair; if \(AB=BA\), the matrices coincide for every \(t\in[0,1]\).

For positive-definite \(2\times2\) matrices \(X,Y\), the relation \(X\prec_{\log}Y\) means \(\lambda_{\max}(X)\le\lambda_{\max}(Y)\) and \(\det X=\det Y\). The theorem supplies an exact trace-difference formula below, which controls the strictness.

## Assumptions and scope

All matrices are finite \(2\times2\), Hermitian and strictly positive-definite over \(\mathbb C\); no commuting assumption, eigenvalue multiplicity restriction, or small-parameter hypothesis is imposed. All fractional powers are the positive functional-calculus powers. The parameter lies in \([0,1]\). The two curves scale alike under independently positive rescalings of \(A\) and \(B\), so the proof may normalize \(\det A=\det B=1\); the conclusion then holds before normalization. There is no assertion in dimension three or higher.

## Proof

**1. Reduction and square-root normal forms.** Both curves satisfy
\[
P_t(aA,bB)=a^{1-t}b^tP_t(A,B),\qquad
Q_t(aA,bB)=a^{1-t}b^tQ_t(A,B)\qquad(a,b>0).
\]
Thus replace each input by its positive determinant-one normalization. The positive \(2\times2\) square-root identity, valid whenever \(\det X=1\), is
\[
X^{1/2}=\frac{I+X}{\sqrt{2+\operatorname{tr}X}}.
\]
This follows from Cayley–Hamilton and positivity. Put
\[
C=B^{1/2},\qquad
D=A^{-1/2}CAC A^{-1/2},\qquad
K=\sqrt{2+\operatorname{tr}(AB)}.
\]
The matrices \(A^{1/2}BA^{1/2}\) and \(CAC\) have determinant one and trace \(\operatorname{tr}(AB)\). Applying the square-root identity in the definitions gives the exact formulas
\[
M=\frac{A^{-1}+B}{K},\qquad
N=\frac{A^{-1}+D}{K}.
\]
Since \(\det D=1\) and \(\operatorname{tr}(AD)=\operatorname{tr}(AB)\), Cayley–Hamilton yields
\[
\det M=\det N=1,\qquad
\operatorname{tr}(AM)=\operatorname{tr}(AN)=K.
\tag{1}
\]
The determinants of \(P_t\) and \(Q_t\) also equal one under this normalization.

**2. A strictly positive commutator-energy defect.** For arbitrary finite-dimensional positive-definite \(A\), Hermitian \(C\), and \(D=A^{-1/2}CAC A^{-1/2}\), diagonalize \(A\) unitarily with eigenvalues \(a_i>0\). Then
\[
\begin{aligned}
\operatorname{tr}D-\operatorname{tr}(C^2)
&=\sum_{i<j}\frac{(a_i-a_j)^2}{a_i a_j}|C_{ij}|^2\\
&=\frac12\left\|A^{-1/2}[A,C]A^{-1/2}\right\|_{\mathrm F}^{2}\ge0.
\end{aligned}
\tag{2}
\]
The equality condition is exactly \([A,C]=0\). Taking \(C=B^{1/2}\), this is equivalent to \([A,B]=0\). Therefore
\[
\operatorname{tr}N-\operatorname{tr}M
=\frac{\operatorname{tr}D-\operatorname{tr}B}{K}\ge0,
\tag{3}
\]
strictly whenever \(AB\ne BA\). This step is exact, not a perturbative approximation.

**3. A two-eigenvalue power identity.** Since \(M,N\) are determinant-one positive-definite \(2\times2\) matrices, let
\[
\operatorname{tr}M=2\cosh u,\qquad
\operatorname{tr}N=2\cosh v,
\qquad 0\le u\le v,
\]
with \(u<v\) if and only if the input matrices do not commute. Define for every real \(p\), \(w>0\),
\[
F_p(w)=\frac{\sinh(pw)}{\sinh w},\qquad F_p(0)=p.
\]
The two eigenvalues of each determinant-one matrix \(T\) are \(e^{w}\) and \(e^{-w}\); interpolation at these two points gives
\[
T^x=F_{1-x}(w)I+F_x(w)T
\qquad (x\in\mathbb R).
\tag{4}
\]
In conjunction with (1), formula (4) yields a complete trace representation:
\[
\boxed{\begin{aligned}
\operatorname{tr}Q_t-\operatorname{tr}P_t
={}&\operatorname{tr}(A)[F_{1-2t}(v)-F_{1-2t}(u)]\\
&+K[F_{2t}(v)-F_{2t}(u)].
\end{aligned}}
\tag{5}
\]

**4. Exact sign and equality.** The function \(F_p\) is strictly decreasing on \([0,\infty)\) when \(0<p<1\), constant when \(p=0\) or \(p=1\), and strictly increasing when \(p>1\). Moreover, \(F_{-p}=-F_p\). To verify these signs for \(p>0\), differentiate the logarithm for \(w>0\):
\[
\frac{d}{dw}\log F_p(w)=\frac{(pw)\coth(pw)-w\coth w}{w}.
\]
The function \(s\mapsto s\coth s\) is strictly increasing for \(s>0\), because \(\sinh(s)\cosh(s)>s\). Continuity covers \(w=0\).

If \(0<t<1/2\), both \(F_{1-2t}\) and \(F_{2t}\) strictly decrease, so (5) is nonpositive, and strictly negative if \(u<v\). If \(1/2<t\le1\), \(F_{1-2t}=-F_{2t-1}\) and \(F_{2t}\) both strictly increase, making (5) nonnegative, strictly positive for \(u<v\). At \(t=0\) and \(t=1/2\), equation (5) vanishes. Finally, the two curves have the same determinant, so comparison of their traces is equivalent to comparison of their larger eigenvalues and hence to log-majorization in dimension two. This proves all assertions. \(\square\)

## Verification

Run the included dependency-free verifier from this directory:

```sh
python3 check_near_spectral.py
```

It reports `PASS: 896 exact rational identities and inequalities`. The tests cover the exact commutator identity in matrix dimensions two through four, determinant-one normal forms for rational positive \(2\times2\) examples, the midpoint trace constraint, and the endpoint strictness formula. Each assertion uses rational arithmetic. These finite checks verify algebraic normalizations but do **not** prove the universal real-parameter or complex-matrix inequalities; those follow analytically from Steps 1–4.

## Relationship to prior work

Ibrahim and Huang, *Order relations for the near geometric and near spectral geometric curves* (arXiv:2610.23736v1, first posted 16 October 2026), introduce \(Q_t\), prove endpoint log-majorization in Theorem 4.3 and midpoint isospectrality in Theorem 4.4, and give a dimension-two formula in Proposition 4.13. Their Conjecture 5.6 asks precisely for the two opposite parameter-range log-majorizations. Neither that proposition nor their conditional results supply the full sign and strictness statement proved here.

Franco, Gan and Kim, *Near-geometric mean of positive definite operators* (2025), introduce the near-geometric mean and compare it with earlier means, but the accessible abstract and preview do not establish a near-spectral-versus-spectral **curve** ordering. The full article could not be inspected, so independent priority checking remains appropriate.

Gan and Kim, *Revisit on spectral geometric mean* (2022), study the ordinary spectral mean and its geodesic properties, without the later near-spectral curve. Their *Weak log-majorization between the geometric and Wasserstein means* (2023) compares the spectral mean against metric and Wasserstein means, rather than comparing \(P_t\) and \(Q_t\). The relevant primary sections of both arXiv papers were inspected.

## Limitations

Only complex Hermitian positive-definite \(2\times2\) matrices are covered. The paper's conjecture in all dimensions remains unresolved by this argument. The result establishes spectral log-majorization, not a Löwner-order comparison. An older equivalent statement could exist under alternative terminology, and a plausible earlier near-geometric reference was not fully accessible; no independent historical-priority audit is claimed. Finite exact tests are not substituted for the proof.

## References

1. M. A. Ibrahim and H. Huang, *Order relations for the near geometric and near spectral geometric curves*, arXiv:2610.23736v1 (16 October 2026), https://arxiv.org/html/2610.23736v1 (particularly Theorems 4.2–4.4, Proposition 4.13 and Conjecture 5.6).
2. J. A. Franco, L. Gan and S. Kim, *Near-geometric mean of positive definite operators*, Positivity **29** (2025), article 54, https://doi.org/10.1007/s11117-025-01147-7 (accessible abstract/preview only).
3. L. Gan and S. Kim, *Revisit on spectral geometric mean*, arXiv:2208.12407v1 (2022), https://arxiv.org/html/2208.12407v1.
4. L. Gan and S. Kim, *Weak log-majorization between the geometric and Wasserstein means*, arXiv:2301.07934v4 (2023), https://arxiv.org/html/2301.07934v4.
