# Noncommuting positive controls can destroy a continuous \(g\)-frame

## Finding
The converse direction of Theorem 2.1 of Rossafi--Nhari--Johnson states that every continuous \(g\)-frame is automatically a \((P,Q)\)-controlled continuous \(g\)-frame for arbitrary
\[
P,Q\in GL^+(H).
\]
This is false when the controls do not commute.

Let the measure space consist of one point of mass \(1\), and take
\[
H=H_{\omega_0}=\mathbb R^2,\qquad
\Lambda_{\omega_0}=I_H.
\]
The resulting family is a Parseval continuous \(g\)-frame.

Choose
\[
P=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
Q=
\begin{pmatrix}
1&19/20\\
19/20&1
\end{pmatrix}.
\]
Both are positive and invertible, but they do not commute. For
\[
f=
\begin{pmatrix}
x\\y
\end{pmatrix},
\]
the controlled energy is
\[
\langle Pf,Qf\rangle
=
2x^2+\frac{57}{20}xy+y^2.
\]
At
\[
f_0=
\begin{pmatrix}
1\\-3/2
\end{pmatrix},
\]
this equals
\[
-\frac1{40}.
\]
Hence no positive lower controlled-frame bound can exist.

The exact repair is operator-theoretic. If \(S_\Lambda\) is the ordinary frame operator, then the mixed controlled energy is
\[
\langle Q S_\Lambda P f,f\rangle.
\]
Therefore an ordinary continuous \(g\)-frame is a \((P,Q)\)-controlled continuous \(g\)-frame exactly when
\[
Q S_\Lambda P\in GL^+(H).
\]
Pairwise commutation of \(P,Q,S_\Lambda\) is a simple sufficient condition, and \(P=Q\) is always safe.

## Assumptions and scope
The construction uses a real two-dimensional Hilbert space. This avoids any issue of complex phases: the controlled energy is an ordinary real quadratic form.

The one-point measure space is a legitimate continuous-\(g\)-frame instance. With \(\Lambda_{\omega_0}=I_H\),
\[
\int_\Omega\|\Lambda_\omega f\|^2\,d\mu(\omega)=\|f\|^2.
\]
Thus the ordinary frame bounds are exactly \(1,1\).

The result concerns the unrestricted two-control equivalence in Theorem 2.1 and its universal-control Corollary 2.2. It does not dispute the standard one-control or equal-control equivalence.

## Proof
The eigenvalues of
\[
P=
\begin{pmatrix}
2&0\\0&1
\end{pmatrix}
\]
are \(2\) and \(1\). The eigenvalues of
\[
Q=
\begin{pmatrix}
1&19/20\\19/20&1
\end{pmatrix}
\]
are
\[
1+\frac{19}{20}=\frac{39}{20},
\qquad
1-\frac{19}{20}=\frac1{20}.
\]
Hence \(P,Q\in GL^+(H)\).

Their products are
\[
PQ=
\begin{pmatrix}
2&19/10\\
19/20&1
\end{pmatrix},
\qquad
QP=
\begin{pmatrix}
2&19/20\\
19/10&1
\end{pmatrix},
\]
so \(PQ\ne QP\).

Because \(\Lambda_{\omega_0}=I_H\), the \((P,Q)\)-controlled energy is
\[
q(f)=\langle Pf,Qf\rangle.
\]
Writing \(f=(x,y)^{\mathsf T}\),
\[
q(f)
=
2x^2+\frac{57}{20}xy+y^2.
\]
For \(f_0=(1,-3/2)^{\mathsf T}\),
\[
q(f_0)
=
2-\frac{171}{40}+\frac94
=
-\frac1{40}.
\]
The lower controlled-frame inequality requires
\[
A\|f\|^2\le q(f)
\]
with \(A>0\), which is impossible at \(f_0\).

Equivalently, the symmetric part of the mixed operator has matrix
\[
\frac{PQ+QP}{2}
=
\begin{pmatrix}
2&57/40\\
57/40&1
\end{pmatrix}.
\]
Its determinant is
\[
2-\left(\frac{57}{40}\right)^2
=
-\frac{49}{1600}<0,
\]
so the quadratic form is indefinite.

For the exact repair, let \(\Lambda\) be an ordinary continuous \(g\)-frame with frame operator \(S_\Lambda\). Its controlled quadratic form is
\[
q_{P,Q}(f)
=
\int_\Omega
\langle\Lambda_\omega Pf,\Lambda_\omega Qf\rangle\,d\mu(\omega)
=
\langle Q S_\Lambda P f,f\rangle.
\]
The two-sided controlled-frame inequality with positive constants is exactly the operator inequality
\[
A I_H\le Q S_\Lambda P\le B I_H.
\]
Such constants exist if and only if
\[
Q S_\Lambda P\in GL^+(H).
\]
If \(P,Q,S_\Lambda\) commute pairwise, then their product is positive invertible and the condition holds.

## Verification
The first public preprint was inspected at Definition 1.4 and Theorem 2.1 together with its complete proof. The final journal version was also inspected at the corresponding definition, theorem, Corollary 2.2, and the displayed controlled frame operator
\[
S_{P\Lambda Q}=Q S_\Lambda P.
\]

The theorem assumes only
\[
P,Q\in GL^+(H).
\]
Its proof uses expressions involving
\[
(PQ)^{1/2}
\]
as though \(PQ\) were positive and later derives the converse estimate by multiplying lower and upper operator bounds for \(P,Q,S_\Lambda\). Neither step is valid for arbitrary noncommuting positive operators.

The final journal version lists primary MSC \(42C15\). The earliest verified public source is arXiv:2210.13211v1, dated 25 September 2022.

All counterexample calculations are exact rational arithmetic. No numerical experiment is used.

## Relationship to prior work
Alizadeh--Abdollahpour's 2019 paper on controlled continuous \(g\)-frames explicitly proves that for positive invertible operators \(T,C\), the product \(TC\) is positive if and only if \(TC=CT\). The same paper proves the ordinary-frame equivalence in the safe equal-control case \((C,C)\). This earlier result identifies precisely why an unrestricted two-control extension cannot be justified merely from positivity of the two controls.

Liu--Fu--Tian's 2023 paper on controlled \(g\)-frames notes the commutation criterion before giving a later two-control equivalence without including commutation in that lemma. The checked statement therefore repeats the same structural issue rather than covering the counterexample or its correction.

Targeted searches by exact title, theorem number, arbitrary positive controls, noncommuting controls, mixed operator positivity, and correction terminology did not locate an indexed erratum or a checked source giving this two-dimensional counterexample or the exact condition
\[
Q S_\Lambda P\in GL^+(H).
\]

## Limitations
The exact characterization above is for a fixed ordinary continuous \(g\)-frame and fixed positive invertible controls.

Pairwise commutation is sufficient but is not claimed necessary; positivity of the specific product
\[
Q S_\Lambda P
\]
is the exact condition.

The result does not classify all subsequent dual-frame statements in the source. Any later result that independently imposes enough positivity or commutation may remain valid.

## References
1. M. Rossafi, F.-D. Nhari and P. S. Johnson, *Controlled continuous \(g\)-frames and their duals in Hilbert spaces*, arXiv:2210.13211v1, 25 September 2022; Palestine Journal of Mathematics 15(1) (2026), 21--31.
2. Y. Alizadeh and M. R. Abdollahpour, *Controlled continuous \(g\)-frames and their multipliers in Hilbert spaces*, Sahand Communications in Mathematical Analysis 15(1) (2019), 37--48.
3. H.-M. Liu, Y.-L. Fu and Y. Tian, *Controlled \(g\)-frames and dual \(g\)-frames in Hilbert spaces*, Journal of Inequalities and Applications 2023, Article 64, DOI 10.1186/s13660-023-02972-8.
