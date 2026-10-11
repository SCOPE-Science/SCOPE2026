# Complete first-coordinate Fourier spectrum on finite-field rank-one matrices

## Finding

Let \(q\) be a prime power and \(m,n\ge2\). For the nonzero rank-one matrices \(X\subseteq M_{m\times n}(\mathbb F_q)\), the first-coordinate Fourier band is
\[
\Omega=\{0\}\cup\{aE_{ij}:a\in\mathbb F_q^\times,\ 1\le i\le m,\ 1\le j\le n\}.
\]
Its normalized restriction Gram matrix has the following complete spectrum. Set
\[
 z=q-1,\qquad t=\frac{zq^{m+n-2}}{(q^m-1)(q^n-1)},\qquad
 c_1=1-qt,\qquad c_2=1-(q+1)t,\qquad T=zmn,
\]
\[
 B=qt+zt(m+n-1)+c_2T,
 \qquad \lambda_\pm=\frac{1+B\pm\sqrt{(1-B)^2+4c_1^2T}}2.
\]
Here \([k]\) denotes multiplicity \(k\), and equal numerical eigenvalues have their multiplicities added:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\lambda_+&1\\
\lambda_-&1\\
qt&mn(q-2)\\
(1+zn)t&m-1\\
(1+zm)t&n-1\\
t&(m-1)(n-1).
\end{array}
\]
Every listed eigenvalue with positive multiplicity is strictly positive. Thus the restricted characters are linearly independent on the rank-one set, for every field size and both matrix dimensions.

The maximum fraction of ambient Fourier energy that this band can place on \(X\) is precisely
\[
 \frac{|X|}{q^{mn}}\max\{\lambda_+,(1+zn)t,(1+zm)t\},\qquad
 |X|=\frac{(q^m-1)(q^n-1)}{q-1}.
\]
The squared condition number of the normalized restriction matrix is exactly
\[
 \kappa^2=\frac{\max\{\lambda_+,(1+zn)t,(1+zm)t\}}{\min\{\lambda_-,t\}}.
\]
In square dimensions \(m=n=d\), for each fixed \(q\),
\[
 \lambda_+\sim \frac{q-1}{q^2}d^2,\qquad
 \lambda_-\sim\frac{2(q-1)}d,\qquad
 \kappa^2\sim\frac{d^3}{2q^2}\quad(d\longrightarrow\infty).
\]

## Assumptions and scope

Fix an arbitrary nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\) and define \(\chi_A(Y)=\psi(\operatorname{tr}(A^\mathsf T Y))\) on the additive group \(V=M_{m\times n}(\mathbb F_q)\). Put \(G_{A,C}=|X|^{-1}\sum_{Y\in X}\overline{\chi_A(Y)}\chi_C(Y)\) for \(A,C\in\Omega\). The ambient norm is the normalized counting \(L^2\)-norm on \(V\), while restriction to \(X\) uses normalized counting measure on \(X\). The spectral coefficient coordinates use the orthonormal ambient characters, not their non-orthogonal restrictions. Both row and column dimensions are at least two; the set contains matrices of **rank exactly one**, not rank at most one. No parity restriction is imposed on \(q\).

## Proof

**1. Fourier transform of the rank-one shell.** Every nonzero rank-one matrix is \(uv^\mathsf T\) with nonzero \(u\in\mathbb F_q^m\), \(v\in\mathbb F_q^n\), modulo exactly \(q-1\) common scalar choices. If \(A\) has rank \(r\), summing first over \(v\) and then over \(u\) gives
\[
 \sum_{Y\in X}\chi_A(Y)
 =\frac{q^{m+n-r}-q^m-q^n+1}{q-1}.
\]
Indeed, among \(u\ne0\), precisely \(q^{m-r}-1\) satisfy \(A^\mathsf T u=0\). For each such \(u\), the sum over \(v\ne0\) is \(q^n-1\); for every other \(u\), it equals \(-1\). Division by \(q-1\) gives the formula. This is the classical rank-one character sum in the bilinear-forms association scheme (Delsarte, Appendix equation A7), also proved here directly.

Dividing by \(|X|\) yields \(c_r=(q^{m+n-r}-q^m-q^n+1)/[(q^m-1)(q^n-1)]\). For \(r=1,2\), these are precisely \(c_1,c_2\) above, because \(c_1-c_2=t\) and \(1-c_1=qt\).

**2. Gram blocks.** The set \(\Omega\) consists of one distinguished zero index and \(mn\) cells, each with \(z=q-1\) labels. Two distinct nonzero frequencies differ by a rank-one matrix precisely when they occupy the same matrix row or column (including the same cell); otherwise the difference has rank two. The distinguished zero index differs by rank one from every nonzero frequency. On nonzero indices, let \(R\) be the \(mn\)-by-\(mn\) matrix whose entry is one when two cells share a row or column, including equality. Let \(J_k\) be the all-ones matrix of order \(k\). Then their Gram block is
\[
 D=(1-c_1)I_T+(c_1-c_2)(R\otimes J_z)+c_2 J_T.
\]
Here \(R=I_m\otimes J_n+J_m\otimes I_n-I_{mn}\).

**3. Orthogonal decomposition and every equality space.** In each cell the label vectors of coordinate sum zero form an eigenspace of dimension \(mn(q-2)\) with eigenvalue \(qt\). The cell-constant vectors identify with \(\mathbb C^m\otimes\mathbb C^n\). The orthogonal row-fluctuation space \(\mathbf1_m^\perp\otimes\operatorname{span}(\mathbf1_n)\) has eigenvalue \((1+zn)t\) and dimension \(m-1\); the column-fluctuation space \(\operatorname{span}(\mathbf1_m)\otimes\mathbf1_n^\perp\) has eigenvalue \((1+zm)t\) and dimension \(n-1\). Their tensor interaction \(\mathbf1_m^\perp\otimes\mathbf1_n^\perp\) has eigenvalue \(t\) and dimension \((m-1)(n-1)\). This follows from the corresponding rook-matrix eigenvalues \(n-1,m-1,-1\).

The remaining two dimensions are the zero-frequency vector \(e_0\) and the normalized constant vector \(u=T^{-1/2}\mathbf1_T\) on nonzero frequencies. In this ordered orthonormal basis the Gram matrix is exactly
\[
 \begin{pmatrix}1&c_1\sqrt T\\c_1\sqrt T&B\end{pmatrix},
\]
with distinct eigenvalues \(\lambda_+\) and \(\lambda_-\). For either \(\lambda\), its eigenspace is the one-dimensional span of
\[
 c_1\sqrt T\,e_0+(\lambda-1)u.
\]
This vector satisfies the first row of the eigenvalue equation automatically and the second by the characteristic equation. If any eigenvalues from different blocks coincide, the corresponding listed orthogonal subspaces are to be combined. The six multiplicities total \(1+T\), so no eigenvalue or equality space is omitted.

**4. Strict positivity and sharp energy bounds.** Positivity of \(t\) makes all nontrivial rook-block eigenvalues positive. To prove \(\lambda_->0\), observe that the displayed two-by-two matrix is the Gram matrix on \(X\) of the functions \(1\) and \(Y/\sqrt T\), where
\[
 Y(M)=\sum_{i,j}\sum_{a\in\mathbb F_q^\times}\chi_{aE_{ij}}(M)
     =T-q\,r(M)s(M),
\]
with \(r(M)\), \(s(M)\) the numbers of nonzero coordinates in any factorization \(M=uv^\mathsf T\). Both support numbers are well-defined under nonzero rescaling. Since \(m,n\ge2\), the product \(r(M)s(M)\) is not constant on rank-one matrices, so the variance is positive and the two-by-two Gram determinant \(\operatorname{Var}_X(Y)/T\) is strictly positive. Its trace is positive; therefore both eigenvalues are positive. Also \(c_1>0\), giving two distinct eigenvalues and the displayed eigenvectors.

For \(f=\sum_{A\in\Omega}b_A\chi_A\), ambient Parseval gives \(\|f\|_{L^2(V)}^2=\sum_A|b_A|^2\), while \(\|f\|_{L^2(X)}^2=b^*Gb\). Thus the sharp normalized concentration ratio is \(\lambda_{\max}(G)\). Multiplication by \(|X|/q^{mn}\) gives the fraction of **ambient total energy** on \(X\). Equality occurs exactly for coefficient vectors in the sum of those explicit eigenspaces whose eigenvalue realizes the maximum. Since \(qt\le(1+zn)t,(1+zm)t\) and \(t\) is no larger than the rook fluctuation eigenvalues, the maximum and minimum simplify to the displayed formulas. The positive definiteness proves exact restricted injectivity.

**5. Dimension-asymptotic conditioning.** For \(m=n=d\) and fixed \(q\), direct substitution shows \(t=(q-1)/q^2+O_q(q^{-d})\), \(c_1=1/q+O_q(q^{-d})\), \(c_2=1/q^2+O_q(q^{-d})\). Hence
\[
 B=\frac{q-1}{q^2}d^2+\frac{2(q-1)^2}{q^2}d+O_q(1),
 \quad B-c_1^2T=\frac{2(q-1)^2}{q^2}d+O_q(1).
\]
The two-by-two spectral root and determinant identities give \(\lambda_+=(q-1)d^2/q^2+O_q(d)\) and \(\lambda_-=(2(q-1)/d)(1+O_q(d^{-1}))\). All other eigenvalues are bounded below by a fixed positive constant or grow only linearly in \(d\). Consequently, for large \(d\), the top and bottom eigenvalues are \(\lambda_+\) and \(\lambda_-\), yielding the claimed cubic squared-conditioning law.

## Verification

Run `python checker.py` with Python 3 and NumPy. The script constructs the rank-one shell independently, computes additive character restriction matrices (including \(\mathbb F_4\) via \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\)), and compares the entire Gram matrix and its eigenvalues with the rational formulas. Twelve cases with fields of orders \(2,3,4,5,7\) and various matrix dimensions passed. Its finite computations supplement, but cannot replace, the unrestricted proof above. Every equality space follows from the given orthogonal block decomposition, not from numerical eigenvector matching.

## Relationship to prior work

Delsarte's bilinear-forms association scheme gives the general rank-one character sum (Appendix A7); it does **not** itself state the eigenvalues of the coordinate-frequency submatrix, the complete orthogonal equality spaces, the sharp band-restriction ratio, or the cubic squared-conditioning asymptotic. Those additional conclusions require analyzing the blown-up rook geometry of the *selected* coordinate characters and the coupled zero-frequency block. Related work on symmetric bilinear schemes (Schmidt) and random recovery of low-rank finite-field matrices (Tan–Balzano–Draper) has different admissible measurement families and statements. This theorem neither improves the general Delsarte character table nor addresses random low-rank recovery guarantees.

## Limitations

The sharp constant concerns the specific complete first-coordinate Fourier band, not arbitrary selected frequencies or arbitrary rank shells. No claim is made about optimal design of the frequency band or about higher Fourier degree. The numerical checker covers only small finite fields; the proof is algebraic and exact for all prime powers. Earlier rank-scheme literature may contain an equivalent specialization or an unrecognized Fourier-frame reformulation. Independent external validation has not been performed.

## References

1. Ph. Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory Series A 25 (1978), 226–241, DOI: 10.1016/0097-3165(78)90015-8; in particular Appendix equation A7.
2. V. Y. F. Tan, L. Balzano, and S. C. Draper, *Rank Minimization over Finite Fields: Fundamental Limits and Coding-Theoretic Interpretations*, arXiv:1104.4302, initially submitted 2011-04-21.
3. K.-U. Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, arXiv:1410.7184, initially submitted 2014-10-27.
4. J. Sheekey, *MRD Codes: Constructions and Connections*, arXiv:1904.05813, initially submitted 2019-04-11 (background only).
