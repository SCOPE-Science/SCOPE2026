# Sharp rank-one positivity defect of the three-matrix trace-class mixing operation

## Finding

The symmetric three-matrix mixing map introduced by Jiao, Luo and Wu does not preserve the positive-semidefinite cone, even on strictly positive inputs in dimension two. Its entire rank-one restriction admits a closed spectral formula and a sharp universal scalar-regularization threshold.

For every integer \(d\ge2\), every unit vectors \(u,v\in\mathbb C^d\), and every \(a,b>0\), write \(P_u=uu^*\), \(P_v=vv^*\), \(c=\langle u,v\rangle=u^*v\), \(r=|c|\), and
\[
q=\sqrt{(a-b)^2+4ab(1-r^2)}.
\]
Then the exact identity is
\[
\boxed{\Phi_{\mathrm{mix}}(0,aP_u,bP_v)=
\frac{ab}{a+b+q}\big(c\,uv^*+\overline c\,vu^*\big).}
\]
The at-most-two nonzero eigenvalues, including zero at degenerate endpoints, are
\[
\boxed{\lambda_\pm=\frac{ab\,r(r\pm1)}{a+b+q}.}
\]
Consequently the output is positive semidefinite if and only if \(r\in\{0,1\}\), and is indefinite for every \(0<r<1\). The two-dimensional obstruction is minimal: for scalar inputs the map is the ordinary median and preserves positivity.

For rank-one *orthogonal projections* \(P,Q\) (here orthogonal means \(P=P^*=P^2\), not necessarily mutually orthogonal), the exact worst negative eigenvalue over all \(d\ge2\) and all \(P,Q\) is \(-\kappa_*\), where
\[
\boxed{\kappa_* = \frac{t_*(1-t_*)^2}{2(1+t_*^2)}
 =0.06744224886812294\ldots,\qquad
 t_*^3+t_*^2+3t_*-1=0,\quad 0<t_*<1.}
\]
In particular, for every real \(\lambda\ge0\), **all** triples
\(\lambda I_d,\ \lambda I_d+P,\ \lambda I_d+Q\) have positive-semidefinite mixing output for all rank-one projections \(P,Q\) if and only if \(\lambda\ge\kappa_*\). The scalar bound is independent of dimension and attained already in dimension two, at overlap \(r_*=2t_*/(1+t_*^2)=0.5436890126920764\ldots\). The inputs are strictly positive definite as soon as \(\lambda>0\), so positivity fails even among strictly positive inputs whenever \(0<\lambda<\kappa_*\).

## Assumptions and scope

Work over complex Hermitian \(d\times d\) matrices, including real symmetric matrices as a special case. The absolute value is \(|H|=(H^2)^{1/2}\) for Hermitian \(H\), and \(D^\dagger\) denotes the Moore–Penrose inverse of a positive matrix \(D\). Define
\[
D=|A-B|+|B-C|+|C-A|,\qquad
\Phi_{\mathrm{mix}}(A,B,C)=A+\operatorname{Re}\left[(B-A)D^\dagger|C-A|+(C-A)D^\dagger|B-A|\right],
\]
where \(\operatorname{Re}X=(X+X^*)/2\). These are precisely the conventions of Jiao–Luo–Wu, Section 3, formula (3.2). The projection threshold concerns equal-amplitude orthogonal projections (idempotents of rank one); unequal-amplitude formulas are included separately, without claiming an optimized scalar threshold over all positive amplitudes.

## Proof

**1. Reduction and inversion.** Fix \(0<r<1\). Multiplying \(v\) by a unit-modulus scalar, we may assume \(c=r>0\) without changing \(P_v\); this phase change also leaves the claimed product \(cuv^*\) unchanged. On \(S=\operatorname{span}\{u,v\}\), use the orthonormal coordinates \(u=e_1\), \(v=re_1+se_2\), with \(s=\sqrt{1-r^2}\). Let \(B=aP_u\), \(C=bP_v\), \(H=B-C\) and \(h=a-b\). Then \(\operatorname{tr}H=h\), \(\det H=-ab s^2<0\), and \(H\) has eigenvalues \((h\pm q)/2\), one positive and one negative. Interpolating the absolute-value function on these two eigenvalues gives
\[
|H|=\frac hq H+k I_S,\qquad k=\frac{2ab s^2}{q}>0.
\]
Because \(D=B+C+|H|\), on \(S\) one has
\[
D=kI_S+\left(1+\frac hq\right)B+\left(1-\frac hq\right)C.
\]
The matrix entries and an elementary determinant expansion yield
\[
D_{22}=k+\left(1-\frac hq\right)bs^2,\quad
D_{12}=\left(1-\frac hq\right)brs,\quad
\det D=k(a+b+q).
\]
Thus \(D\) is invertible on \(S\), zero on \(S^\perp\), and
\[
u^*D^\dagger v=\frac{rD_{22}-sD_{12}}{\det D}=\frac{r}{a+b+q}.
\]
Restoring the arbitrary complex phase gives \(u^*D^\dagger v=c/(a+b+q)\).

**2. Formula and eigenvalues.** At \(A=0\), both \(B\) and \(C\) are positive, so their absolute values are themselves. Since \(BD^\dagger C+CD^\dagger B\) is Hermitian,
\[
\Phi_{\mathrm{mix}}(0,B,C)=BD^\dagger C+CD^\dagger B
=\frac{ab}{a+b+q}(cuv^*+\overline c vu^*).
\]
The operator \(cuv^*+\overline c vu^*\), restricted to \(S\), has eigenvalues \(r^2+r\) and \(r^2-r\), directly from its trace \(2r^2\) and determinant \(-r^2(1-r^2)\). It vanishes on \(S^\perp\), proving the spectral statement and the strict indefinite sign for \(0<r<1\).

At \(r=0\), the projections have orthogonal ranges and \(BD^\dagger C=0\), giving zero. At \(r=1\), \(P_u=P_v=P\), \(D=(a+b+|a-b|)P\), giving \(\Phi_{\mathrm{mix}}(0,aP,bP)=\min(a,b)P\). Both match the formula by continuity and direct computation. If \(d=1\), order the three scalar inputs as \(A\le B\le C\). Then \(D=2(C-A)\) and the defining expression gives \(\Phi_{\mathrm{mix}}(A,B,C)=A+2(B-A)(C-A)/D=B\) when \(A<C\), with the all-equal case immediate. Thus the scalar operation is the median and preserves positivity.

**3. Sharp scalar threshold.** For \(a=b=1\), the smaller eigenvalue is
\[
\lambda_-(r)=-\frac{r(1-r)}{2(1+\sqrt{1-r^2})}.
\]
Put \(t=r/(1+\sqrt{1-r^2})\in[0,1]\). Then \(r=2t/(1+t^2)\), and the magnitude of the negative eigenvalue becomes
\[
f(t)=\frac{t(1-t)^2}{2(1+t^2)},\qquad
f'(t)=\frac{(t-1)(t^3+t^2+3t-1)}{2(1+t^2)^2}.
\]
The cubic \(g(t)=t^3+t^2+3t-1\) is strictly increasing on \([0,1]\), with \(g(0)<0<g(1)\). Hence \(f\) increases up to its unique interior critical point \(t_*\) and decreases afterward; \(f(0)=f(1)=0\). This proves the global, unique (up to phases and unitary conjugacy) maximum \(\kappa_*=f(t_*)\), attained by rank-one projections with overlap \(r_*\). As a further exact characterization, \(r_*\) is the unique root of \(r^3+r^2+r-1=0\) in \((0,1)\).

**4. Positivity restoration and strict-positive failure.** Because \(D\) depends only on differences, translation covariance holds for every real \(\lambda\):
\[
\Phi_{\mathrm{mix}}(A+\lambda I,B+\lambda I,C+\lambda I)=\Phi_{\mathrm{mix}}(A,B,C)+\lambda I.
\]
Thus the least eigenvalue for \(\Phi_{\mathrm{mix}}(\lambda I,\lambda I+P,\lambda I+Q)\) is at least \(\lambda-\kappa_*\), and equality occurs for the optimizing overlap. This proves both directions of the universal threshold and the strict-positive counterexamples.

**5. Simple exact witness.** In \(d=2\), choose
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
Q=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Here \(|P-Q|=I/\sqrt2\), and direct inversion yields
\[
\Phi_{\mathrm{mix}}(0,P,Q)=\frac{1-1/\sqrt2}{2}
\begin{pmatrix}2&1\\1&0\end{pmatrix},\qquad
\lambda_{\min}=1-\frac{3\sqrt2}{4}<0.
\]
For instance, after shifting all three inputs by \(I/32\), the inputs become strictly positive and the output retains a negative eigenvalue \(33/32-3\sqrt2/4<0\).

## Verification

The standalone `CHECK.py` uses SymPy to verify the exact witness, determinant, derivative and resultant identities, and uses NumPy to test the full rank-one formula and its two eigenvalues on 900 deterministic random nondegenerate complex-phase instances, including unequal amplitudes. Its successful output states 900 numerical tests and the approximate threshold \(0.06744224886812294\). These tests are finite consistency checks only; the universal statements follow from the above proof. To rerun, execute `python CHECK.py` with Python 3, NumPy and SymPy installed.

## Relationship to prior work

Jiao, Luo and Wu (arXiv:2610.21445v1, Section 3) define the same operation and prove permutation symmetry plus trace-norm control, which support a sharp metric-cotype theorem. Their Section 3 does not furnish a rank-one spectrum, classify cone preservation, or optimize positivity regularization. In particular their norm estimate (3.5) concerns the distance to an input and does not imply positivity of the output. Nakagawa's Riemannian median (arXiv:2602.14007v2) is a distinct optimization-defined operation on positive-definite matrices, not the algebraic trace-class mixing formula considered here. The result supplies a sharp cone-geometry boundary for this recently defined operation without challenging its original metric-cotype application.

## Limitations

This is an exact rank-one input-family theorem, not a global characterization of the positivity domain of the mixing map for arbitrary positive matrices, nor a universal optimal regularization threshold across all matrix inputs or arbitrary positive rank-one amplitudes. Numerical checks alone cannot establish any infinite family. Historical priority among wider noncommutative median or Jordan-product formulations is not exhaustively certified; the original source and closely relevant primary work were compared, but an unindexed earlier equivalent formula remains a residual possibility.

## References

1. Y. Jiao, S. Luo and L. Wu, *The Sharp Scale Inequality for the Schatten Trace Class*, arXiv:2610.21445v1, first posted 15 October 2026, Section 3, formula (3.2), Lemma 3.2. https://arxiv.org/html/2610.21445v1
2. Y. Nakagawa, *The Riemannian Median Of Positive-Definite Matrices*, arXiv:2602.14007v2 (27 July 2026), Sections 3–4. https://arxiv.org/html/2602.14007v2
