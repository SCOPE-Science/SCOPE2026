# Sharp entrywise sensitivity of two-by-two positive-semidefinite repair

## Finding
Let \(\mathbb S^2\) denote the real symmetric two-by-two matrices, with Frobenius inner product, and let \(\Pi(A)=A_+\) be nearest-point projection onto the cone \(\mathbb S^2_+\) of positive-semidefinite matrices. Give both input and output the **entrywise maximum norm** \(\|A\|_{\max}=\max_{1\le i,j\le2}|A_{ij}|\), not the Frobenius norm.

**Theorem.** The exact global Lipschitz modulus is
\[
\sup_{A\ne B}\frac{\|\Pi(A)-\Pi(B)\|_{\max}}{\|A-B\|_{\max}}=\frac32.
\]
The displayed supremum is not attained by any two distinct finite matrices. It is approached by explicit strictly indefinite matrices with one negative eigenvalue tending to zero, and their arbitrarily small perturbations. Equivalently, every distinct pair satisfies the **strict** inequality
\[
\|A_+-B_+\|_{\max}<\frac32\|A-B\|_{\max}.
\]
The factor is sharp even if the starting matrix has positive diagonal entries.

## Assumptions and scope
Matrices are real, symmetric, and of order exactly two. The repair \(A_+\) is formed by replacing negative eigenvalues by zero, which is the unique Frobenius-nearest positive-semidefinite matrix. The stability metric is the unweighted largest absolute matrix entry. No statement is made about complex Hermitian matrices, larger matrix orders, weighted entrywise metrics, or nearest-correlation matrices with a prescribed diagonal.

## Proof
**1. Differentiation in the mixed-sign spectral region.** Suppose \(A\) has eigenvalues \(\lambda_+>0>\lambda_-\). Write \(R\) and \(Q\) for the orthogonal spectral projections onto its positive and negative eigenspaces. Define
\[
\kappa=\frac{\lambda_+}{\lambda_+-\lambda_-}\in(0,1).
\]
Differentiating \(A_+=\lambda_+R\) by the two-eigenvalue divided-difference formula gives, for every symmetric \(H\),
\[
D\Pi_A(H)=RHR+\kappa(RHQ+QHR)
=(1-\kappa)RHR+\kappa(H-QHQ).
\]
For clarity, this formula also follows directly by diagonalizing \(A\): a perturbation in the positive eigendirection survives, one in the negative eigendirection vanishes, and each mixed matrix entry is multiplied by the divided difference \(\kappa\). On positive-definite matrices the derivative is the identity; on negative-definite matrices it is zero.

**2. Exact componentwise bounds for the two endpoint operators.** Put \(Q=uu^{\mathsf T}\), with \(u=(p,q)\) and \(p^2+q^2=1\). For the linear operator \(T_1(H)=H-QHQ\), the absolute coefficient sum determining its diagonal \((1,1)\)-output is
\[
F(p,q)=1-p^4+2|p|^3|q|+p^2q^2.
\]
Writing \(t=|p/q|\) (and interpreting \(q=0\) by a limit) yields
\[
F(p,q)=1+\frac{t^2(1-t^2+2t)}{(1+t^2)^2},\qquad
\frac32-F(p,q)=\frac{(t-1)^2(3t^2+2t+1)}{2(1+t^2)^2}\ge0.
\]
The \((2,2)\)-output obeys the same bound by interchanging \(p,q\). The off-diagonal output has absolute coefficient sum \(1+z-2z^2\), where \(z=|pq|\in[0,1/2]\); its maximum is \(9/8\). Consequently \(\|T_1\|_{\max\to\max}=3/2\), with a maximizing diagonal row exactly when \(|p|=|q|\).

For \(T_0(H)=RHR\), put \(r=|p/q|\). Its diagonal row sums, with the other obtained by exchanging coordinates, are
\[
\frac{(1+r)^2}{(1+r^2)^2}\le\frac{3+2\sqrt2}{4}<\frac32.
\]
The maximum follows by differentiating the one-variable rational expression (the only positive critical point is \(r=\sqrt2-1\)). The off-diagonal row sum is \(z(1+2z)\le1\). Thus \(\|T_0\|_{\max\to\max}\le(3+2\sqrt2)/4<3/2\).

Since every mixed-sign derivative is a **strict** convex combination \((1-\kappa)T_0+\kappa T_1\), its norm is strictly less than \(3/2\). The same strict bound holds in the positive- and negative-definite regions.

**3. The global inequality and nonattainment.** For distinct \(A,B\), parameterize the segment by \(A_s=A+s(B-A)\), \(0\le s\le1\). The map \(\Pi\) is Frobenius-Lipschitz by nearest-point nonexpansivity, hence absolutely continuous on this finite-dimensional segment. Unless the polynomial \(\det A_s\) vanishes identically, its zeros are finite. At almost every other parameter, \(A_s\) is nonsingular and the derivative bounds from Steps 1–2 apply; the matrix positive-part map is differentiable there. Integrating the derivative gives
\[
\|\Pi(B)-\Pi(A)\|_{\max}
\le\int_0^1\|D\Pi_{A_s}\|_{\max\to\max}\,ds\ \|B-A\|_{\max}
<\frac32\|B-A\|_{\max}.
\]
The last inequality is strict because the integrand is strictly below \(3/2\) almost everywhere. If \(\det A_s\equiv0\), every nonzero \(A_s\) has rank one. To prove that these matrices have a common range, write two nonzero endpoints as \(A=\sigma uu^{\mathsf T}\) and \(B=\tau vv^{\mathsf T}\), where \(\sigma,\tau\in\{-1,1\}\) and the norms of \(u,v\) absorb their nonzero eigenvalue magnitudes. Then \(\det((1-s)A+sB)=s(1-s)\sigma\tau(u_1v_2-u_2v_1)^2\). Identical vanishing forces \(u,v\) to be collinear; if an endpoint is zero the same conclusion about the line is immediate. Thus the entire segment is made of scalar multiples of one fixed rank-one matrix. On such a line positive-part projection is scalar positive-part clipping (possibly after reversing the scalar sign), and is at most one-Lipschitz. The strict inequality therefore holds in this exceptional case too.

**4. Sharpness through a concrete sequence.** Let
\[
Q=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
R=I-Q,\quad
H=\begin{pmatrix}1&-1\\-1&-1\end{pmatrix},\quad
A_\delta=R-\delta Q\quad(0<\delta<1).
\]
Here \(\|H\|_{\max}=1\), the eigenvalues of \(A_\delta\) are \(1\) and \(-\delta\), and \(D\Pi_{A_\delta}(H)_{11}=\frac12+\frac1{1+\delta}\). Therefore
\[
\lim_{\delta\downarrow0}\ \lim_{h\downarrow0}
\frac{\|\Pi(A_\delta+hH)-\Pi(A_\delta)\|_{\max}}{h}
\ge\lim_{\delta\downarrow0}\left(\frac12+\frac1{1+\delta}\right)=\frac32.
\]
Together with Step 3 this proves the sharp supremum and nonattainment. The diagonal entries of \(A_\delta\) are \((1-\delta)/2>0\).

## Verification
The companion `check.py` reproduces the crucial polynomial factorization, tests the projection-Jacobian decomposition with exact fractions for representative rational parameters, verifies strict componentwise bounds there, checks the exact sharpness-direction formula, and tests finite perturbations numerically. Invoke `python3 check.py`. A successful local replay reported 2,711 assertions. Finite parameter testing is **not** offered as proof of the universal norm bound, nonattainment, or quantifier over all matrices; those follow from the algebra and integration arguments above.

## Relationship to prior work
Higham (1988) established Frobenius-nearest positive-semidefinite repair and the spectral positive-part representation. Malick and Sendov (2006) derived the generalized Jacobian of the positive-semidefinite projection; Šilhavý (2015) independently investigated differentiability of metric projection at singular boundary points. Their results cover the basic projection and derivative framework but do not, in the examined material, furnish the sharp cross-norm componentwise factor \(3/2\) or explain why finite pairs cannot attain it. The additional contribution here is the optimized absolute-row-sum calculation, strict mixed-sign bound, and global integration/nonattainment argument.

## Limitations
This is a two-by-two, real-symmetric, unweighted entrywise result. The sharpness is an asymptotic limit of finite perturbations, not an equality case. No analogous constant for matrices of higher order is asserted. The available literature assessment is not an exhaustive historical priority proof; an equivalent calculation may exist under semidefinite metric regularity, Lorentz-cone, or eigenvalue-clipping terminology. The original Higham article was assessed via bibliographic abstract and an author-authored exposition, not its entire publisher text.

## References
1. N. J. Higham, *Computing a nearest symmetric positive semidefinite matrix*, Linear Algebra Appl. 103 (1988), 103–118. DOI: 10.1016/0024-3795(88)90223-6.
2. J. Malick and H. S. Sendov, *Clarke generalized Jacobian of the projection onto the cone of positive semidefinite matrices*, Set-Valued Anal. 14 (2006), 273–293. DOI: 10.1007/s11228-005-0005-1. Open preprint: https://www.stats.uwo.ca/faculty/hssendov/Publications/CGJPCPSDM.pdf.
3. M. Šilhavý, *Differentiability of the metric projection onto a convex set with singular boundary points*, J. Convex Anal. 22 (2015), 969–997. Open article: https://journalofconvexanalysis.com/articles/jca22052/jca22052.pdf?v=2.
