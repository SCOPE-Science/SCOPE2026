# Logarithmic nuclearity threshold for critical Dirichlet Rhaly operators

## Finding

Put \(\mathcal D_* = \{f(z)=\sum_{n\ge0}f_nz^n:\sum_{n\ge0}(n+1)|f_n|^2<\infty\}\), equipped with the indicated coefficient norm. For each real \(b\), let
\[
 \eta_n(b)=\frac{1}{(n+1)[\log(n+2)]^b},\qquad
 (R_bf)_n=\eta_n(b)\sum_{k=0}^n f_k.
\]
Then the following classification is exact:

1. \(R_b\) is bounded on \(\mathcal D_*\) exactly when \(b\ge1\), and compact exactly when \(b>1\).
2. For every \(1<p<\infty\), \(R_b\in\mathcal S_p(\mathcal D_*)\) exactly when \(b>1\).
3. The **trace-class boundary** is \(R_b\in\mathcal S_1(\mathcal D_*)\) exactly when \(b>2\).
4. For every \(0<p<1\) and every real \(b\), \(R_b\notin\mathcal S_p(\mathcal D_*)\).

For \(b>1\), let \(P_J\) project onto monomials of degree \(n<2^J-1\). Then the exact order of divergence of the nuclear norms of finite sections is
\[
 \|P_JR_bP_J\|_{\mathcal S_1}\asymp_b
 \begin{cases}
 J^{2-b},&1<b<2,\\
 \log(J+1),&b=2,
 \end{cases}\qquad(J\to\infty),
\]
whereas at \(b>2\) they converge to \(\|R_b\|_{\mathcal S_1}<\infty\). In terms of cutoff dimension, these are respectively powers of \(\log N\) and \(\log\log N\). Constants implicit in \(\asymp_b\) depend only on \(b\). These finite-section asymptotics, together with the trace-class and subunit quasi-Schatten endpoints, are the principal contribution.

## Assumptions and scope

The coefficient norm on \(\mathcal D_*\) is equivalent to the classical analytic Dirichlet norm; the two are related by a bounded invertible diagonal isomorphism, so membership in a Schatten ideal is equivalent for the two presentations. All operators and Schatten classes are complex Hilbert-space operators. \(\mathcal S_p\) means the usual Schatten class for any \(p>0\), including a quasi-ideal when \(0<p<1\). The logarithm is natural. The finite sections are the indicated orthogonal compressions in the chosen coefficient model.

Under the orthonormal map \(f\mapsto (\sqrt{n+1}\,f_n)\), the matrix is
\[
 A_b(n,k)=r_n c_k\,\mathbf1_{k\le n},\quad
 r_n=\frac1{\sqrt{n+1}[\log(n+2)]^b},\quad
 c_k=\frac1{\sqrt{k+1}}.
\]
The relevant critical input-factor exponent is \(c_k\asymp(k+1)^{-1/2}\), rather than the constant input factor of an ordinary Rhaly matrix on \(\ell^2\).

## Proof

**1. Boundedness and compactness.** For a positive factorable triangular matrix the discrete two-weight Hardy criterion (Theorem A in Bellavita–Dellepiane–Stylogiannis, 2026, citing Bennett and Grosse-Erdmann) identifies boundedness with finiteness of
\[
 \sup_{m\ge0}\rho_m,
 \qquad \rho_m^2=\left(\sum_{n\ge m}r_n^2\right)
 \left(\sum_{k\le m}c_k^2\right),
\]
and compactness with \(\rho_m\to0\). For \(b\le1/2\), the first tail is infinite. For \(b>1/2\), integral comparison gives
\[
 \sum_{n\ge m}r_n^2\asymp_b[\log(m+2)]^{1-2b},\qquad
 \sum_{k\le m}c_k^2\asymp\log(m+2),
\]
so \(\rho_m\asymp_b[\log(m+2)]^{1-b}\) for large \(m\). This yields precisely the first assertion.

**2. Atomic logarithmic slabs.** Set
\[
 I_j=\{n:2^j\le n+1<2^{j+1}\},\quad N_j=|I_j|=2^j\quad(j\ge0).
\]
Decompose \(A_b=D+B\), with \(D\) block diagonal over \(I_j\) and \(B\) the strictly lower block-triangular part. On \(I_j\), write
\[
 D_j=\operatorname{diag}(r_n)_{n\in I_j}\,T_{N_j}\,
 \operatorname{diag}(c_k)_{k\in I_j},
\]
where \(T_N\) is the \(N\times N\) lower triangular matrix with every entry on or below the diagonal equal to one. The diagonal factors have minimum and maximum moduli within fixed \(b\)-dependent factors of \(2^{-j/2}(j+1)^{-b}\) and \(2^{-j/2}\), respectively. Applying both upper and lower singular-number inequalities for invertible diagonal factors gives, uniformly for \(1\le m\le N_j\),
\[
 s_m(D_j)\asymp_b2^{-j}(j+1)^{-b}s_m(T_{N_j}).
\]
An exact finite-matrix identity is
\[
 s_m(T_N)=\left[2\sin\!\left(\frac{(2m-1)\pi}{4N+2}\right)\right]^{-1},\qquad1\le m\le N.
\]
Indeed, \(T_N^{-1}\) is the first-difference bidiagonal matrix; the characteristic equation of \((T_N^{-1})^*T_N^{-1}\) gives those eigenvalues. Hence
\[
 \sum_{m=1}^N s_m(T_N)^p\asymp_p
 \begin{cases}N^p,&p>1,\\N\log(N+1),&p=1,\\N,&0<p<1.\end{cases}
\]
It follows that, for all sufficiently large \(j\),
\[
 \|D_j\|_{\mathcal S_p}^p\asymp_{b,p}
 \begin{cases}(j+1)^{-bp},&p>1,\\(j+1)^{1-b},&p=1,\\2^{j(1-p)}(j+1)^{-bp},&0<p<1.\end{cases}
\]
For the middle case \(\|D_j\|_{\mathcal S_1}\) is understood rather than its first power.

**3. The cross-slab part is trace class whenever \(b>1\).** For \(i<j\), the entire \(I_j\times I_i\) rectangle lies below the original diagonal. The corresponding matrix is rank one, equal to \(r|_{I_j}(c|_{I_i})^*\). Unit vectors proportional to these restrictions reduce \(B\), up to zero summands, to the strictly lower triangular matrix
\[
 \widetilde B(j,i)=u_jv_i\mathbf1_{i<j},\qquad
 u_j=\|r|_{I_j}\|_2\asymp_b(j+1)^{-b},\quad
 v_i=\|c|_{I_i}\|_2\asymp1.
\]
Split the block indices \(j\) into dyadic groups \(G_h=\{j:2^h\le j<2^{h+1}\}\), keeping \(j=0\) separately. Inside \(G_h\), the strictly triangular matrix has trace norm at most
\[
 C_b2^{-hb}\|T_{2^h}\|_{\mathcal S_1}
 \le C_b(h+1)2^{h(1-b)}.
\]
For each output group \(G_h\), its part receiving input from all earlier groups is rank one, with trace norm at most \(C_b2^{h(1-b)}\). Both bounds are summable in \(h\) if \(b>1\). Therefore \(B\in\mathcal S_1\). This explicitly separates the cross-slab contribution from the local triangular singular-value mass.

**4. Ideal membership and the sharp nuclear cutoff.** If \(b>1\), Step 3 shows \(B\in\mathcal S_1\subset\mathcal S_p\) for \(p>1\), while Step 2 shows \(D=\bigoplus_jD_j\in\mathcal S_p\) since \(\sum_j(j+1)^{-bp}<\infty\). For \(p=1\), the block-pinching contraction on trace class gives \(\sum_j\|D_j\|_{\mathcal S_1}\le\|A_b\|_{\mathcal S_1}\). Conversely the decomposition and Step 3 give \(\|A_b\|_{\mathcal S_1}\le\sum_j\|D_j\|_{\mathcal S_1}+\|B\|_{\mathcal S_1}\) whenever the series converges. Step 2 proves that this occurs exactly for \(b>2\).

If \(0<p<1\), any finite-dimensional compression satisfies \(\|D_j\|_{\mathcal S_p}\le\|A_b\|_{\mathcal S_p}\), but Step 2 gives \(\|D_j\|_{\mathcal S_p}^p\asymp_{b,p}2^{j(1-p)}(j+1)^{-bp}\to\infty\). Therefore no \(\mathcal S_p\)-membership is possible, even in the trace-class regime. If \(b\le1\), noncompactness or unboundedness from Step 1 already excludes all \(\mathcal S_p\).

**5. Truncation growth.** For \(P_J\) as defined, the pinching bound and the triangle inequality, together with the uniform estimate \(\|P_JBP_J\|_{\mathcal S_1}\le\|B\|_{\mathcal S_1}\), yield
\[
 \left|\|P_JA_bP_J\|_{\mathcal S_1}
 -\sum_{j=0}^{J-1}\|D_j\|_{\mathcal S_1}\right|
 \le\|B\|_{\mathcal S_1}.
\]
Use \(\|D_j\|_{\mathcal S_1}\asymp_b(j+1)^{1-b}\) and elementary integral comparison to obtain the displayed growth laws. When \(b>2\), convergence of the finite-section trace norms to the full trace norm follows from trace-class convergence of the orthogonal compressions.

## Verification

The standalone `verify_dirichlet_rhaly.py` checks the finite triangular singular-value identity, the exact Hilbert–Schmidt sum of truncated matrices, and singular-value bounds obtained by multiplying triangular matrices by the actual diagonal factors. It passed 482 finite consistency checks with NumPy. These are supplemental checks only. The infinite criteria and asymptotic orders are proved in Steps 1–5.

## Relationship to prior work

Bellavita, Dellepiane, and Stylogiannis (arXiv:2606.15875v1) establish general factorable-matrix boundedness/compactness and Schatten \(\mathcal S_p\) criteria for \(p>1\); they identify classical Dirichlet weights as critical, explicitly compute the Hilbert–Schmidt distinction, and exclude that critical case from their parameter-uniform theorem. Thus the \(p>1\) assertion here is consistent with and can also be extracted from their general theory. The endpoint \(p=1\), the strict subunit quasi-Schatten obstruction, and finite-section nuclear divergence rates for the stated Dirichlet family are not stated there.

Their earlier arXiv:2503.21930 treats Rhaly matrices on unweighted \(\ell^2\), and Galanopoulos–Girela (DOI:10.1007/s12220-026-02361-9) treat boundedness/compactness on analytic spaces, not the present trace-ideal endpoint. A published result for **unweighted** monotone-modulus Rhaly matrices has a superficially similar \(\log\)-squared nuclearity threshold. That result concerns the constant input factor, whereas the Dirichlet matrix here has a decaying input factor and is not boundedly diagonally similar to the unweighted matrix. The weighted trace-class comparison is therefore not a direct consequence of the unweighted statement; the block decomposition above proves the weighted endpoint independently.

## Limitations

The theorem treats one power-logarithmic coefficient family with real exponent, not arbitrary critical-Dirichlet symbols or arbitrary factorable matrices. The bounds \(\asymp\) do not identify the leading constants in finite-section nuclear growth or individual singular-value asymptotics. Existing general weighted Hardy, factorable-matrix or integral-operator theory could furnish an alternative derivation; publication priority beyond the checked sources is not independently certified.

## References

1. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875v1, first public 2026-06-14, https://arxiv.org/abs/2606.15875.
2. C. Bellavita, E. Dellepiane, G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930, first public 2025-03-27, https://arxiv.org/abs/2503.21930.
3. P. Galanopoulos, D. Girela, *Rhaly Operators Acting on Hardy, Bergman, and Dirichlet Spaces*, J. Geom. Anal. 36 (2026), article 115, https://doi.org/10.1007/s12220-026-02361-9.
4. Classical finite-triangular singular-value formula, verified directly from the bidiagonal inverse in the proof above.
