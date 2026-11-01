# Hyponormality rigidity for affine matrix-valued Fock–Sobolev Toeplitz operators

## Finding
For any integer \(m\geq0\), positive integer \(d\), and matrices \(A,B\in M_d(\mathbb C)\), consider the closure \(T\) of the polynomial-core matrix Toeplitz operator with symbol \(zA+\overline z B\) on the normalized vector-valued Fock–Sobolev space \(\mathbb F^{2,m}(\mathbb C)\otimes\mathbb C^d\). Define
\[
P=A^*A-BB^*,\qquad
G=A^*A-AA^*+B^*B-BB^*,\qquad
K=B^*A-AB^*.
\]
Then **the closed unbounded operator \(T\) is hyponormal if and only if**
\[
\boxed{G=0,\quad K=0,\quad P\succeq0.}
\]
When these conditions hold, the self-commutator quadratic form defined on polynomials has the unique bounded extension
\[
\boxed{C_T=(I+m E_{00})\otimes P,}
\]
where \(E_{00}\) is the projection onto the vacuum monomial. In particular \(\sigma_{\mathrm{ess}}(C_T)=\sigma(P)\), \(\|C_T\|_{\mathrm{ess}}=\|P\|\), and the nonessential vacuum contributions are the eigenvalues of \((m+1)P\) (with coincidences allowed). These are assertions about the **bounded extension of the commutator form**; they are not claims that an unbounded operator product acts on the full Hilbert space.

There are genuinely noncommuting nonnormal examples. Let
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
A=N-3I_2,\qquad B=N^*-2I_2.
\]
Then \(G=K=0\) and \(P=5I_2-N-N^*\) has eigenvalues \(4,6\). Thus \(T\) is strictly hyponormal in the sense of a uniformly positive commutator form, although both coefficient matrices are nonnormal and do not commute.

## Assumptions and scope
The scalar Fock–Sobolev norm and orthonormal monomials are
\[
\|f\|_m^2=\frac1{\pi m!}\int_{\mathbb C}|f(z)|^2|z|^{2m}e^{-|z|^2}\,dA(z),\qquad
e_n(z)=\sqrt{\frac{m!}{(n+m)!}}z^n,\quad n\ge0.
\]
The vector-valued space uses the tensor-product norm. On \(\mathcal D_0\), the finite-support span of \(e_n\otimes v\), set \(T_0=P_mM_{zA+\bar zB}|_{\mathcal D_0}\), where \(P_m\) is the orthogonal projection onto holomorphic vectors. The statement concerns its graph closure \(T=\overline{T_0}\), not an unspecified maximal realization. Hyponormality of a densely defined closed operator means \(\mathcal D(T)\subseteq\mathcal D(T^*)\) and \(\|T^*f\|\le\|Tf\|\) for every \(f\in\mathcal D(T)\). All matrices are finite dimensional; no normality or commutativity assumption is made.

## Proof
**Step 1: explicit creation and annihilation.** Define \(Je_n=\sqrt{n+m+1}\,e_{n+1}\) and \(J^*e_0=0\), \(J^*e_n=\sqrt{n+m}\,e_{n-1}\) for \(n\ge1\). Holomorphic multiplication and projection of antiholomorphic multiplication give \(T_0=J\otimes A+J^*\otimes B\) on \(\mathcal D_0\). This densely defined operator is closable because its formal adjoint \(J^*\otimes A^*+J\otimes B^*\) has the same dense invariant polynomial core in its adjoint domain. For \(f\in\mathcal D_0\), \(T^*f=(J^*\otimes A^*+J\otimes B^*)f\), and polynomial vectors lie in the domains of both products \(T^*T\) and \(TT^*\).

**Step 2: exact quadratic commutator.** Expanding on \(\mathcal D_0\), with \(Q=B^*B-AA^*\), gives
\[
(T^*T-TT^*)|_{\mathcal D_0}
=J^*J\otimes P+JJ^*\otimes Q+J^2\otimes K+(J^*)^2\otimes K^*.
\]
Here \(G=P+Q\). Consequently, the diagonal fiber block at \(n=0\) is \((m+1)P\), while at \(n\ge1\) it is \(P+(n+m)G\). The two-step upper/lower blocks are \(\sqrt{(n+m+1)(n+m+2)}K\) and its adjoint. Observe the two finite-dimensional trace identities \(\operatorname{tr}G=\operatorname{tr}K=0\), which hold for all \(A,B\) by cyclicity.

**Step 3: positivity forces cancellation of the growing terms.** Suppose \(T\) is hyponormal. Its commutator form is then nonnegative on \(\mathcal D_0\). Fix \(\theta\in\mathbb R\) and \(v\in\mathbb C^d\), and for \(N\to\infty\) use the normalized packet
\[
f_N=\ell_N^{-1/2}\sum_{j=0}^{\ell_N-1}e^{ij\theta}e_{N+j}\otimes v,
\qquad \ell_N=\lfloor\sqrt N\rfloor.
\]
The exact blocks from Step 2 and \(\ell_N/N\to0\), \(\ell_N\to\infty\) yield
\[
\lim_{N\to\infty}\frac1N
\langle(T^*T-TT^*)f_N,f_N\rangle
=\langle (G+e^{-2i\theta}K+e^{2i\theta}K^*)v,v\rangle.
\]
Thus the Hermitian matrix \(M(\theta)=G+e^{-2i\theta}K+e^{2i\theta}K^*\) is positive semidefinite for every \(\theta\). Its trace is identically zero, so \(M(\theta)=0\) for every \(\theta\). Taking its constant and second Fourier coefficients forces \(G=0\) and \(K=0\). The residual diagonal form from Step 2 is \((I+mE_{00})\otimes P\). Testing any fiber above the vacuum shows \(P\succeq0\). This proves necessity, including the nontrivial off-diagonal rigidity.

**Step 4: positivity on the closure.** Conversely, assume \(G=K=0\) and \(P\succeq0\). Step 2 gives, on \(\mathcal D_0\),
\[
\|T_0f\|^2-\|T_0^*f\|^2
=\langle((I+mE_{00})\otimes P)f,f\rangle\ge0,
\]
where \(T_0^*f\) denotes the actual densely-defined Hilbert-space adjoint on the polynomial core. For any \(f\in\mathcal D(T)\), choose \(f_k\in\mathcal D_0\) with \(f_k\to f\), \(T_0f_k\to Tf\). Applying the inequality to differences shows \(T^*f_k\) is Cauchy. Since \(T^*\) is closed, \(f\in\mathcal D(T^*)\) and \(\|T^*f\|\le\|Tf\|\). Hence \(T\) is hyponormal.

**Step 5: commutator spectrum and an irreducible interaction.** Step 2 gives the bounded form extension \(C_T=(I+mE_{00})\otimes P\). It differs from \(I\otimes P\) by a rank-at-most-\(d\) operator; every eigenvalue of \(P\) occurs on infinitely many nonvacuum fibers. Hence \(\sigma_{\mathrm{ess}}(C_T)=\sigma(P)\) and \(\|C_T\|_{\mathrm{ess}}=\|P\|\). In the stated \(2\times2\) example, exact matrix multiplication yields \(G=K=0\), \(P=\begin{psmallmatrix}5&-1\\-1&5\end{psmallmatrix}\), and \([A,B]=[N,N^*]\ne0\). This is not a simultaneous scalar diagonalization.

## Verification
The standalone checker `verification/verify_affine_fock.py` constructs finite truncations of the creation and annihilation matrices, compares all interior diagonal and two-step self-commutator blocks with the exact formulas, verifies trace cancellation, and checks the noncommuting example for several Fock–Sobolev indices. It reported **3,789 supplementary finite assertions passed**, using Python with NumPy. The top boundary of a finite truncation is excluded from comparisons, since truncation creates an artificial commutator there. The checker does not establish the asymptotic packet argument or the infinite-dimensional closure-domain assertion; these are proved above.

## Relationship to prior work
Ko, Ji Eun Lee, and Jongrak Lee (2026) analyze scalar polynomial-symbol hyponormal Toeplitz operators on the same Fock–Sobolev spaces, notably scalar two-term harmonic symbols. The new claim classifies **arbitrary noncommuting matrix coefficients** for degree-one holomorphic and antiholomorphic terms and identifies the forced cancellation of the matrix-valued growing commutator terms. Al-Qabani and Abdulsattar (2026) work with matrix-valued symbols on vector-valued doubling Fock spaces but study boundedness, compactness and Fredholm properties rather than this unbounded hyponormality classification. Bala and Pandey (2026), and Abhinand, Curto, and Prasad (2026), treat matrix/block Toeplitz hyponormality on the **Hardy circle**, with bounded symbols and distinct compressed-shift geometry; their conclusions do not imply this weighted oscillator commutator criterion. Related finite-dimensional normality/trace algebra is background; neither the trace identities nor the vacuum normalization alone give the classification without the packet argument.

## Limitations
The theorem is for finite matrix multiplicity, degree-one harmonic symbols, and the graph closure of the polynomial-core realization. It does not classify arbitrary higher-degree or nonharmonic matrix symbols, infinite-dimensional coefficient operators (where a traceless positive matrix argument is unavailable), nor subnormality. The formula for \(C_T\) concerns the bounded extension of the commutator **form**, not an everywhere-defined product of unbounded operators. The novelty comparison is based on accessible primary sources and research records; a classical matrix-oscillator criterion under another name might cover the result. Independent expert validation and publication-priority determination remain unperformed.

## References
1. E. Ko, J. E. Lee and J. Lee, “Hyponormality of Toeplitz Operators on the Fock–Sobolev Spaces,” *Mediterranean Journal of Mathematics* **23**, Article 144 (first publicly published June 9, 2026), https://doi.org/10.1007/s00009-026-03142-y .
2. A. Al-Qabani and S. Abdulsattar, “Block Toeplitz Operators on Vector-Valued Doubling Fock Spaces,” *Al-Nahrain Journal of Science* **29** (2026), https://doi.org/10.22401/ANJS.29.2.14 .
3. N. Bala and P. Pandey, “Hyponormal Toeplitz operators with operator valued normal symbols,” arXiv:2609.30801v1 (September 25, 2026), https://arxiv.org/html/2609.30801v1 .
4. M. Abhinand, R. E. Curto and T. Prasad, “Hyponormal block Toeplitz operators with finite rank self-commutators,” arXiv:2605.02214v1 (May 4, 2026), https://arxiv.org/html/2605.02214v1 .
