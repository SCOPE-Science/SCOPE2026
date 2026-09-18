# All-order fixed-DCT rank-one factorization of the AR(1) Karhunen–Loève transform

## Result

Let
\[
R_N(\rho)=[\rho^{|i-j|}]_{i,j=0}^{N-1},\qquad 0<\rho<1,
\]
and let
\[
T_N(\rho)=(1-\rho^2)R_N(\rho)^{-1}
\]
be its normalized inverse covariance. Thus \(T_N(\rho)\) is tridiagonal with endpoint diagonal entries \(1\), interior diagonal entries \(1+\rho^2\), and off-diagonal entries \(-\rho\).

Write \(C_N^{\mathrm{II}}\) for the orthonormal DCT-II,
\[
[C_N^{\mathrm{II}}]_{n,k}
=\sqrt{\frac2N}\,\beta_n
\cos\!\frac{\pi n(2k+1)}{2N},
\qquad
\beta_0=2^{-1/2},\quad \beta_n=1\ (n>0).
\]
Define
\[
\ell_n=2-2\cos\frac{n\pi}{N},\qquad
 d_n=(1-\rho)^2+\rho\ell_n,
\]
\[
q_n=\sqrt{\frac2N}\,\beta_n\cos\frac{n\pi}{2N},
\qquad \sigma=\rho(1-\rho).
\]
Then for every integer \(N\ge2\),
\[
\boxed{
C_N^{\mathrm{II}}T_N(\rho)(C_N^{\mathrm{II}})^T
=
D+\sigma\bigl(qq^T+(Sq)(Sq)^T\bigr),
}
\]
where \(D=\operatorname{diag}(d_0,\ldots,d_{N-1})\) and
\(S=\operatorname{diag}(1,-1,1,-1,\ldots)\).
Equivalently, entrywise,
\[
G_{ij}=d_i\delta_{ij}
+\sigma q_iq_j\bigl(1+(-1)^{i+j}\bigr).
\]
Hence opposite-parity DCT modes do not couple at all. After grouping even and odd DCT indices, \(G\) is the direct sum of two diagonal-plus-rank-one matrices,
\[
\boxed{
G_{\rm even}=D_{\rm even}+2\sigma q_{\rm even}q_{\rm even}^T,
\qquad
G_{\rm odd}=D_{\rm odd}+2\sigma q_{\rm odd}q_{\rm odd}^T.
}
\]
If \(Q_{\rm even}\) and \(Q_{\rm odd}\) are their orthogonal eigenvector matrices, with rows ordered by increasing generator eigenvalue, and \(\widetilde Q_N\) embeds these two matrices on the even and odd DCT coordinates, then
\[
\boxed{
W_N(\rho)=\widetilde Q_N(\rho) C_N^{\mathrm{II}}
}
\]
is the exact AR(1) KLT, up to the usual eigenvector row signs. The corrected eigenvalues alternate in parity, so the natural DCT index order already gives decreasing covariance-eigenvalue order.

Each parity correction is a classical secular eigenproblem. If \(I\) is one parity class and \(\nu\) is an eigenvalue of
\(D_I+2\sigma q_Iq_I^T\), then
\[
1+2\sigma\sum_{j\in I}\frac{q_j^2}{d_j-\nu}=0,
\qquad
v_j\propto\frac{q_j}{d_j-\nu}.
\]
Because \(d_j\) is strictly increasing within each parity class and every relevant \(q_j\ne0\), the roots strictly interlace the poles. Thus the correction matrices are Cauchy-structured in exactly the same sense as the even-order corrections previously identified in arXiv:2609.20221.

## Odd-order corollary: fixed DCT-VI and DCT-VIII cores

For \(N=2M+1\), fold the input into
\[
u_k=\frac{x_k+x_{N-1-k}}{\sqrt2}\quad(0\le k<M),
\qquad u_M=x_M,
\]
\[
v_k=\frac{x_k-x_{N-1-k}}{\sqrt2}\quad(0\le k<M).
\]
Let \(B_N\) denote this orthogonal folding map and \(P_N\) interleave the symmetric and antisymmetric outputs. The odd-length DCT-II parity identity is
\[
C_N^{\mathrm{II}}
=
P_N\bigl(C_{M+1}^{\mathrm{VI}}\oplus C_M^{\mathrm{VIII}}\bigr)B_N,
\]
where \(C_M^{\mathrm{VIII}}\) is, up to the standard sign/reversal convention, the DST-VII branch used in the classical odd DCT-II splitting.

Consequently the exact odd-order AR(1) KLT has the nonrecursive factorization
\[
\boxed{
W_N(\rho)=
P_N\Bigl[
\bigl(Q_s C_{M+1}^{\mathrm{VI}}\bigr)
\oplus
\bigl(Q_a C_M^{\mathrm{VIII}}\bigr)
\Bigr]B_N,
}
\]
where both \(Q_s\) and \(Q_a\) diagonalize explicit diagonal-plus-rank-one matrices. In particular, the odd case does not require a residual-KLT recursion or a separate arrowhead diagonalization.

An equivalent generator-domain statement makes the structure especially transparent. Let \(T_s(\rho)\) and \(T_a(\rho)\) be the symmetric and antisymmetric blocks after folding, and let \(e_0\) denote the outer boundary coordinate. Then
\[
\boxed{
T_x(\rho)
=\rho T_x(1)+(1-\rho)^2I+\rho(1-\rho)e_0e_0^T,
\qquad x\in\{s,a\}.
}
\]
For odd \(N\), \(T_s(1)\) is diagonalized by DCT-VI and \(T_a(1)\) by DCT-VIII. This is the direct odd analogue of the DCT-II/DCT-IV rank-one construction for even order.

## Proof

The full-order identity is entrywise. Let \(L_N=T_N(1)\). Then
\[
\rho L_N+(1-\rho)^2I
\]
has the correct off-diagonals \(-\rho\) and the correct interior diagonals \(1+\rho^2\). At each endpoint its diagonal is
\[
\rho+(1-\rho)^2=1-\rho+\rho^2,
\]
short of the required value \(1\) by exactly \(\rho(1-\rho)\). Therefore
\[
T_N(\rho)
=
\rho L_N+(1-\rho)^2I
+\sigma(e_0e_0^T+e_{N-1}e_{N-1}^T).
\]
The DCT-II diagonalizes the Neumann second-difference matrix \(L_N\), with eigenvalues \(\ell_n\). Moreover
\[
C_N^{\mathrm{II}}e_0=q,
\qquad
C_N^{\mathrm{II}}e_{N-1}=Sq,
\]
because reflection of a DCT-II row multiplies row \(n\) by \((-1)^n\). Conjugating the preceding identity by \(C_N^{\mathrm{II}}\) gives the displayed formula for \(G\). The factor \(1+(-1)^{i+j}\) then proves exact parity separation.

The rank-one secular formulas are standard consequences of
\((D_I-\nu I)v=-2\sigma q_I(q_I^Tv)\). Strict interlacing follows because \(2\sigma>0\), the diagonal entries are distinct, and the components of \(q_I\) are nonzero. Finally, centrosymmetry of the AR(1) generator and the classical phase ordering of its modes imply symmetric/antisymmetric alternation, so interleaving the two internally ordered parity blocks produces the KLT order.

For odd \(N\), conjugating by the sum/difference folding map gives the same boundary-rank-one identity separately on the two parity blocks. At \(\rho=1\), those blocks are precisely the second-difference generators diagonalized by DCT-VI and DCT-VIII, giving the stated corollary.

## Relation to prior work

Reznik's recent arXiv:2609.20221 proves the fixed-core diagonal-plus-rank-one factorization for **even** \(N\): after a butterfly, its two cores are DCT-II and DCT-IV. Its Lemma 4.1 and Theorem 4.2 explicitly assume even order. The same paper derives Cauchy-structured corrections and accuracy-controlled \(O(N\log N)\) application using fast-multipole or hierarchical methods.

Reznik's earlier all-order paper arXiv:2608.06522 treats odd \(N\) differently: the odd factorization uses two copies of a one-sided residual KLT plus an arrowhead stage, and the residual transform recursively reduces through half order. At \(\rho\to1\), that construction reduces to the known DCT-VI/DST-VII parity split. The paper also remarks that the companion conference paper uses a fixed-DCT route, but the companion paper's stated fixed-core theorem and construction are restricted to even \(N\). The result above supplies an explicit all-order identity and, in particular, the missing nonrecursive odd-order rank-one correction formula.

The 2013 DCT-II/DCT-VI/DST-VII relation of Reznik supplies the fixed odd trigonometric parity identities, but not the \(\rho\)-dependent exact AR(1) KLT correction theorem. Torun and Akansu (2013) give explicit AR(1) KLT kernels through the classical frequency/root representation rather than this fixed-DCT rank-one factorization.

The improvement is structural rather than asymptotic: the previous recursive odd algorithm already has \(O(N\log N)\) complexity. The new statement shows that odd lengths admit the same nonrecursive fixed-transform-plus-Cauchy-corrections architecture as even lengths.

## Numerical verification

`artifacts/verify.py` checks the full DCT-basis identity, exact parity decoupling, corrected diagonalization, orthogonality, and the odd DCT-VI/DCT-VIII parity split for multiple dimensions and correlations. The recorded maximum residuals are at ordinary double-precision roundoff scale. The analytic proof above does not depend on these numerical checks.

## Limitations

The result is for real stationary AR(1) covariance matrices with \(0<\rho<1\) and orthogonal KLTs. At \(\rho=0\) the covariance is the identity and the KLT is nonunique; endpoint statements there must be interpreted as limits. At \(\rho\to1\), the correction terms vanish and the factorization tends to the DCT-II.

The exact algebraic factorization does not by itself make dense application of the correction matrices exact in \(O(N\log N)\). Fast-multipole/HSS application is accuracy-controlled to a requested tolerance, while direct dense application remains quadratic. No claim is made here about floating-point backward stability of a particular accelerated implementation, negative \(\rho\), nonstationary autoregressive models, or higher-order AR processes.

Originality is asserted only to the best of our knowledge. The main residual risk is simultaneous or unpublished work prompted by the very recent 2026 preprints, especially because arXiv:2608.06522 describes the companion paper broadly as a nonrecursive fixed-DCT route even though the available companion theorem is explicitly even-order.

## References

1. Y. A. Reznik, *Exact fast factorizations of the AR(1) Karhunen–Loève transform*, arXiv:2609.20221 (2026), https://arxiv.org/abs/2609.20221.
2. Y. A. Reznik, *Direct Factorization of the Karhunen–Loève Transform of AR(1) Sources*, arXiv:2608.06522 (2026), https://arxiv.org/abs/2608.06522.
3. Y. A. Reznik, *Relationship between DCT-II, DCT-VI, and DST-VII transforms*, ICASSP 2013, DOI: 10.1109/ICASSP.2013.6638744.
4. M. U. Torun and A. N. Akansu, *An efficient method to derive explicit KLT kernel for first-order autoregressive discrete process*, IEEE Trans. Signal Process. 61(15), 3944–3953 (2013), DOI: 10.1109/TSP.2013.2265225.
