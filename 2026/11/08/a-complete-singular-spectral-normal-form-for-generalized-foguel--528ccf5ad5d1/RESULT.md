# A complete singular spectral normal form for generalized Foguel operators

## Finding
Let \(H_1,H_2\) be infinite-dimensional separable complex Hilbert spaces, let \(V_j\in\mathcal B(H_j)\) be isometries, and let \(T\in\mathcal B(H_2,H_1)\). For the generalized Foguel operator
\[
F=\begin{pmatrix}V_1^*&T\\0&V_2\end{pmatrix}
\quad\text{on }H_1\oplus H_2,
\]
put \(E=\ker V_1^*\), \(K=(\ker T)^\perp\subseteq H_2\), \(S=|T|\vert_K\), and
\[
\varphi(s)=\frac{s+\sqrt{s^2+4}}2\quad (s\geq0).
\]
There is an **exact unitary equivalence of positive operators**
\[
\boxed{\displaystyle
|F|\ \simeq\ 0_E\ \oplus\ I_{\ker T^*}\ \oplus\ I_{\ker T}\ \oplus\ \varphi(S)\ \oplus\ \varphi(S)^{-1}.}
\tag{1}
\]
The identity summands act on their indicated Hilbert spaces; the final two summands act on two copies of \(K\). In particular, this representation is independent of \(V_2\) and depends on \(V_1\) only through its defect-space dimension.

The singular eigenvalue multiplicities at the exceptional points are **exactly**
\[
\dim\ker|F|=\dim\ker V_1^*,\qquad
\dim\ker(|F|-I)=\dim\ker T+\dim\ker T^*.
\tag{2}
\]
Every positive singular eigenvalue \(s\) of \(|T|\), with \(s>0\), produces both singular eigenvalues \(\varphi(s)\) and \(\varphi(s)^{-1}\), each with the same multiplicity. Equivalence (1) also identifies the corresponding continuous spectral parts, not just the eigenvalues.

Writing \(\sigma_{\mathrm{ess}}\) for Fredholm essential spectrum, (1) yields the exact **essential singular spectrum**
\[
\begin{split}
\sigma_{\mathrm{ess}}(|F|)
={}&\{\varphi(s),\varphi(s)^{-1}:s\in\sigma_{\mathrm{ess}}(|T|)\}\\
&\cup\begin{cases}\{1\},&T\text{ is not Fredholm},\\\varnothing,&T\text{ is Fredholm},\end{cases}\\
&\cup\begin{cases}\{0\},&\dim E=\infty,\\\varnothing,&\dim E<\infty.\end{cases}
\end{split}
\tag{3}
\]
When \(T\) is Fredholm, the essential singular spectrum has a genuine open gap around \(1\). When \(T\) is bounded below but has infinite-dimensional cokernel, \(1\) may instead be an *isolated essential singular value*, even though \(0\notin\sigma_{\mathrm{ess}}(|T|)\).

Finally, for every \(0<p<\infty\),
\[
\boxed{\quad |F|-I\in S_p\quad\Longleftrightarrow\quad
\dim\ker V_1^*<\infty\ \text{and}\ T\in S_p.\quad}
\tag{4}
\]
If these conditions hold, and \((s_j(T))\) lists the nonzero singular values of compact \(T\), with multiplicity, the exact Schatten-power identity is
\[
\boxed{\displaystyle
\big\||F|-I\big\|_{S_p}^p=\dim\ker V_1^*
+\sum_j\left[(\varphi(s_j(T))-1)^p+
(1-\varphi(s_j(T))^{-1})^p\right].}
\tag{5}
\]
These statements form consequences of the one normal-form theorem (1), rather than independent claims.

## Assumptions and scope
All Hilbert spaces and operators are complex, and all operators are bounded. The isometries need not be surjective and their defects may be infinite-dimensional. The corner \(T\) need not be compact, injective, normal, or Fredholm. The space \(K\) is the closure of \(\operatorname{ran}T^*\); the restriction \(S\) is positive and injective on \(K\), but its inverse need not be bounded. The function \(\varphi\) and its reciprocal are bounded continuous functions on \([0,\|T\|]\). Empty direct summands are omitted. We define \(S_p\) to include the Schatten quasi-ideal for \(0<p<1\), and use the Fredholm (Calkin) essential spectrum, not the Weyl essential spectrum.

## Proof
**Step 1: remove the isometry defects.** Since \(V_1^*V_1=I\) and \(V_2^*V_2=I\),
\[
F^*F=\begin{pmatrix}V_1V_1^*&V_1T\\T^*V_1^*&I+T^*T\end{pmatrix}.
\]
On the input decomposition \(H_1=V_1H_1\oplus E\), identify \(V_1x\) with \(x\). It follows by direct unitary conjugation that
\[
F^*F\simeq G^*G\oplus0_E,\qquad
G=\begin{pmatrix}I_{H_1}&T\\0&I_{H_2}\end{pmatrix},
\]
where \(G^*G=\left(\begin{smallmatrix}I&T\\T^*&I+T^*T\end{smallmatrix}\right)\). Functional calculus for positive square roots yields \(|F|\simeq|G|\oplus0_E\). Notice that \(V_2\) has disappeared *exactly*, without passage to a quotient.

**Step 2: polar splitting.** Let \(L=\overline{\operatorname{ran}T}\). The polar partial isometry of \(T\) restricts to a unitary \(U:K\to L\) with \(T|_K=US\). Under \(H_1=L\oplus\ker T^*\) and \(H_2=K\oplus\ker T\), the positive operator \(G^*G\) is unitarily equivalent to the identity on \(\ker T^*\oplus\ker T\), plus the operator
\[
B(S)=\begin{pmatrix}I_K&S\\S&I_K+S^2\end{pmatrix}
\quad\text{on }K\oplus K.
\]
The spectral parameter \(S\) commutes with all entries of this matrix.

**Step 3: a continuous exact diagonalizer.** Define on \([0,\|T\|]\)
\[
a(s)=\sqrt{\tfrac12\left(1-\frac{s}{\sqrt{s^2+4}}\right)},
\quad b(s)=\sqrt{\tfrac12\left(1+\frac{s}{\sqrt{s^2+4}}\right)}.
\]
Then the matrix \(W(s)=\left(\begin{smallmatrix}a(s)&b(s)\\b(s)&-a(s)\end{smallmatrix}\right)\) is unitary for each \(s\ge0\), including \(s=0\), and direct multiplication gives
\[
W(s)^*\begin{pmatrix}1&s\\s&1+s^2\end{pmatrix}W(s)
=\operatorname{diag}(\varphi(s)^2,\varphi(s)^{-2}).
\]
The same identity holds for the commuting operator entries by continuous functional calculus, so \(|B(S)^{1/2}|\) is unitarily equivalent to \(\varphi(S)\oplus\varphi(S)^{-1}\). Combine with Steps 1–2 to prove (1), including all multiplicities and spectral types.

**Step 4: the exceptional eigenvalues.** On \(K\), \(S\) is injective. Since \(\varphi(s)=1\) only at \(s=0\), the kernels of \(\varphi(S)-I\) and \(\varphi(S)^{-1}-I\) are zero. All remaining unit eigenspaces come precisely from \(\ker T^*\oplus\ker T\). The only zero block is \(0_E\), because \(\varphi(S)\) and its inverse are bounded and boundedly invertible. This proves (2).

**Step 5: essential spectrum, including the missing central point.** The zero summand contributes \(0\) to the Fredholm essential spectrum exactly when \(E\) is infinite-dimensional. For \(\lambda>0\) with \(\lambda\ne1\), the top-left scalar corner in
\[
G^*G-\lambda^2I=
\begin{pmatrix}(1-\lambda^2)I&T\\T^*&T^*T+(1-\lambda^2)I\end{pmatrix}
\]
is invertible. Schur complementation shows that this block operator is Fredholm if and only if
\[
\frac{(1-\lambda^2)^2}{\lambda^2}I-T^*T
\quad\text{is Fredholm}.
\]
The latter condition is equivalent to exclusion of \(|\lambda-\lambda^{-1}|\) from \(\sigma_{\mathrm{ess}}(|T|)\). At \(\lambda=1\), a different exact factorization is required:
\[
G^*G-I=\begin{pmatrix}I&0\\T^*&I\end{pmatrix}
\begin{pmatrix}0&T\\T^*&0\end{pmatrix}.
\]
The first factor is invertible; the second is Fredholm if and only if \(T\) is Fredholm. The nonnegative spectrum of \(|G|\) is bounded away from zero because \(G\) is invertible, and the correspondence between \(G^*G\) and \(|G|\) by square root preserves Fredholmness at positive parameters. These facts establish (3). If \(T\) is Fredholm, the essential spectrum of \(|T|\) is bounded away from zero, which gives a two-sided essential spectral gap about \(1\).

**Step 6: ideals.** Subtract \(I\) from (1). On \(E\) the result is \(-I_E\); on the two kernel identity blocks it is zero; on \(K\oplus K\) it is \((\varphi(S)-I)\oplus(\varphi(S)^{-1}-I)\). For \(0\le s\le\|T\|\), both nonnegative magnitudes are continuous positive multiples of \(s\), with the ratios extending to \(1/2\) at \(s=0\). Therefore Schatten membership on those blocks is exactly that of \(S\), equivalently \(T\), and an infinite-dimensional \(E\) is an obstruction for all finite \(p\). Summing the \(p\)-powers of singular values of the mutually orthogonal blocks yields (4) and (5).

## Verification
The accompanying `check.py` uses independent finite-dimensional spectral calculations for complex rectangular corners of every size up to \(6\times6\) and every possible rank. It compares the singular spectrum of a shear with the reciprocal-branch prediction, verifies the block identity, and checks Schatten-power sums and optional zero-defect summands. Running `python check.py` with NumPy prints `FOGUEL_FULL_MODULUS_FINITE_CHECKS_OK 6858`. The finite checks test formulas, **not** the infinite-dimensional operator theorem or its publication priority; Steps 1–6 supply the infinite-dimensional proof.

For an illustrative essential-spectrum separation, take \(H_1=H_2=\ell_2(\mathbb N\times\mathbb N)\), and let \(T\) be the shift \(T e_{j,k}=e_{j+1,k}\). Then \(|T|=I\) and \(\ker T^*\) is infinite-dimensional. With unitary \(V_1,V_2\), formula (3) gives the three-point set
\[
\sigma_{\mathrm{ess}}(|F|)=
\left\{\frac{\sqrt5-1}{2},\ 1,\ \frac{\sqrt5+1}{2}\right\}.
\]
Thus the middle point is isolated and essential, although the corner's essential singular spectrum is just \(\{1\}\).

## Relationship to prior work
Nag and Golla (2026) study these generalized Foguel operators and determine their norm, reduced minimum modulus, attainment, absolute attainment, Fredholmness, and Moore–Penrose inverse. Those conclusions provide the immediate motivation but do not furnish the exact positive-operator spectral normal form or its multiplicity/Schatten consequences. Garcia (2009) derives the nonexceptional singular spectral mapping for a shift-based Foguel operator, explicitly excluding \(0\) and \(1\); Raghupathi (2012) gives an algebraic spectral-mapping proof for one isometry and a criterion for the spectral value \(1\). Nag and Golla (2025) separately analyze norm-attainment classes for positive two-by-two block operators, including certain Gram-like blocks, but do not give this normal form. The scalar reciprocal functions and certain special-case spectral exclusions therefore belong to established theory. The statement assessed here is the **full unitary spectral decomposition with all exceptional eigenspace multiplicities for two arbitrary isometries**, and its precise essential and ideal consequences. The proof is elementary in its building blocks, so older unlocated unitary-normal-form formulations remain a real priority risk.

## Limitations
No assertion is made about eigenvalues of the generally nonnormal operator \(F\) itself. The full spectrum is that of the positive modulus \(|F|\), not of \(F\). The essential-spectrum formula is the Fredholm convention. Although \(V_2\) drops out of \(|F|\), it still affects the range defect and Fredholm index of \(F\) itself. The study does not treat non-isometric diagonal blocks, Banach-space analogues, or unbounded corners. Numerical tests are finite and cannot establish the infinite theorem. Mathematical priority has not been independently certified.

## References
1. P. Nag and R. Golla, *Norm and Minimum Attainment of Foguel-Type Operators*, arXiv:2610.42102v1, posted 2026-10-30. https://arxiv.org/html/2610.42102v1
2. S. R. Garcia, *The norm and modulus of a Foguel operator*, Indiana Univ. Math. J. 58 (2009), 2305–2316; arXiv:0908.0479. https://arxiv.org/abs/0908.0479
3. M. Raghupathi, *A Note on the Norm and Spectrum of a Foguel Operator*, arXiv:1206.6725v1, posted 2012-06-28. https://arxiv.org/abs/1206.6725
4. P. Nag and R. Golla, *On absolutely norm (minimum) attaining 2 × 2 block operator matrix*, arXiv:2507.11148v1, posted 2025-07-15. https://arxiv.org/abs/2507.11148
