# A sharp initial-angle barrier for symmetric extended Krylov blocks

## Finding

The initial batched forward/inverse vectors of a symmetric positive-definite extended Krylov method cannot be made arbitrarily orthogonal when the operator is well-conditioned. For each prescribed spectral condition number \(\kappa>1\), the exact infimum of the magnitude of their projected normalized inner product is
\[
\inf_{A,b}\frac{-\langle PAb,PA^{-1}b\rangle}{\|PAb\|_2\,\|PA^{-1}b\|_2}
=\frac{2\sqrt\kappa}{\kappa+1},\qquad P=I-bb^{\mathsf T}.
\]
The infimum is not attained by any admissible non-eigenvector start; a three-eigenvalue sequence approaches it. The associated minimum possible condition number of a **full-rank, two-column, normalized projected initial block** is the *unattained* value
\[
\inf\operatorname{cond}_2([u,w])=\frac{\sqrt\kappa+1}{\sqrt\kappa-1},
\]
where \(u=PAb/\|PAb\|_2\) and \(w=PA^{-1}b/\|PA^{-1}b\|_2\).
This is a conditioning restriction on an unorthogonalized input block, not on the eventual orthonormal basis or a floating-point error bound.

## Assumptions and scope

Throughout, \(A\in\mathbb R^{n\times n}\) is symmetric positive definite, \(n\ge2\), with extreme eigenvalues \(0<m<M\), and \(\kappa=M/m\). The starting vector \(b\in\mathbb R^n\) satisfies \(\|b\|_2=1\) and is not an eigenvector. Let \(P=I-bb^{\mathsf T}\), \(p=PAb\), and \(q=PA^{-1}b\). Both vectors are nonzero. Write \(u=p/\|p\|_2\), \(w=q/\|q\|_2\), and \(t=-\langle u,w\rangle\). The **active spectral support** is the set of distinct eigenvalues whose spectral projections of \(b\) are nonzero. The first split-channel block in the inverse-leading scheme consists of \(A^{-1}b\) and \(Ab\); the same two vectors arise when their order is reversed.

The claim holds for all such finite-dimensional real matrices and vectors, not only diagonal matrices. A nonsingular projected block requires at least three active spectral values. An eigenvector start is excluded because the projected columns vanish and their normalization is undefined.

## Proof

**1. Exact angular identity and strict Kantorovich comparison.** Define the spectral moments \(\mu=b^{\mathsf T}Ab\) and \(\nu=b^{\mathsf T}A^{-1}b\). Cauchy–Schwarz gives \(\mu\nu>1\) because \(b\) is not an eigenvector. With \(T=A^{-1}\), the identity \(T(Ab-\mu b)=b-\mu Tb\) implies
\[
PTp=-\mu q,\qquad b^{\mathsf T}Tp=1-\mu\nu\ne0.
\]
Consequently, \(\|PTp\|_2<\|Tp\|_2\). Since \(p\perp b\),
\[
0<t=\frac{p^{\mathsf T}Tp}{\|p\|_2\,\|PTp\|_2}
>\frac{p^{\mathsf T}Tp}{\|p\|_2\,\|Tp\|_2}.
\]
To establish the spectral inequality in this last expression without an unproved lemma, set \(a=1/M\), \(c=1/m\) and normalize \(\|p\|_2=1\). For every eigenvalue \(\lambda\in[a,c]\), \(\lambda^2\le(a+c)\lambda-ac\). Thus if \(z=p^{\mathsf T}Tp\), then \(\|Tp\|_2^2\le(a+c)z-ac\). The elementary square inequality
\[
(a+c)z-ac\le\frac{(a+c)^2}{4ac}z^2
\]
follows by expanding \(((a+c)z-2ac)^2\ge0\). Therefore
\[
t>\frac{2\sqrt{ac}}{a+c}=\frac{2\sqrt\kappa}{\kappa+1}.
\]
The inequality is strict even if \(p\) happens to saturate the unconstrained Kantorovich inequality, because \(Tp\) has a nonzero component along \(b\).

**2. Condition number and the third orthogonalized direction.** The Gram matrix of \(C=[u,w]\) is \(C^{\mathsf T}C=\begin{psmallmatrix}1&-t\\-t&1\end{psmallmatrix}\). Its eigenvalues are \(1+t\) and \(1-t\). For \(t<1\),
\[
\operatorname{cond}_2(C)=\sqrt{\frac{1+t}{1-t}}
>\frac{\sqrt\kappa+1}{\sqrt\kappa-1}.
\]
Gram–Schmidt on either normalized column first leaves the fraction \(\sqrt{1-t^2}\) of the other column, and hence
\[
\frac{\|(I-\Pi_{\operatorname{span}\{b,A^{-1}b\}})Ab\|_2}{\|PAb\|_2}
=\sqrt{1-t^2}<\frac{\kappa-1}{\kappa+1}.
\]
Here \(\Pi_V\) denotes the Euclidean orthogonal projector onto \(V\). The analogous ratio with the two channels reversed is identical.

**3. Spectral-support rank boundary.** In an eigenbasis, linear dependence of \(b\), \(Ab\), \(A^{-1}b\) forces a quadratic \(\alpha\lambda^2+\beta\lambda+\gamma\) to vanish at every active eigenvalue. Therefore these three vectors are independent exactly when the active spectral support contains at least three distinct values. Two active values give dependent projected columns, so \(t=1\), and one active value gives \(p=q=0\). This establishes all rank boundary cases.

**4. Exact sharpness and nonattainment.** Fix \(r=\sqrt\kappa>1\). On three coordinates take
\[
A_r=\operatorname{diag}(1,r,r^2),\qquad
b_\varepsilon=(\sqrt\varepsilon,\sqrt{1-2\varepsilon},\sqrt\varepsilon)^{\mathsf T},
\quad 0<\varepsilon<1/2.
\]
A direct calculation with \(\mu=\sum_i |b_i|^2\lambda_i\), \(\nu=\sum_i|b_i|^2/\lambda_i\) gives
\[
t_\varepsilon=
\frac{2r+\varepsilon(r-1)^2}{r^2+1-\varepsilon(r-1)^2},
\qquad
t_\varepsilon-\frac{2r}{r^2+1}=
\frac{\varepsilon(r-1)^2(r+1)^2}
{(r^2+1)(r^2+1-\varepsilon(r-1)^2)}>0.
\]
Each such vector has three active spectral values and thus produces a full-rank block. As \(\varepsilon\downarrow0\), \(t_\varepsilon\downarrow2r/(r^2+1)\), the third-direction relative residual approaches \((r^2-1)/(r^2+1)\) and \(\operatorname{cond}_2(C)\) approaches \((r+1)/(r-1)\). Since Step 1 was strict for every non-eigenvector start, none of these limiting constants is achieved. The limiting \(b_0\) is an eigenvector, for which both projected vectors vanish; it is not an admissible optimizer.

## Verification

The accompanying standalone `check_first_block.py` uses symbolic algebra to verify the exact three-mode angle and strict-gap formulas, checks the limit algebraically, compares them with direct numerical projections at six explicit parameter points, and tests the universal inequality and Gram condition bound on randomly generated real SPD diagonal examples. It verifies 324 nondegenerate random full-rank conditioning cases. The proof above, rather than finite sampling, establishes the universal results.

## Relationship to prior work

Lund and Schweitzer (2026) describe first-step inverse-leading split-channel block construction and prove a comparison of mixed- and split-channel *loss of orthogonality* for positive-definite operators at later steps. Their framework motivates the question, but it does not present the exact first projected-block spectral-condition-number frontier, its strict unattainability, or the three-mode sharpness sequence. Classical Kantorovich/Wielandt/Bauer–Householder inequalities already imply the underlying unconstrained spectral cosine bound. That classical ingredient is **not** presented as original. The additional content here is the constrained first-block identity, strict projection gap, exact extremal sequence, and rank-collapse boundary. General block Gram–Schmidt stability analyses bound floating-point orthogonality in terms of input conditioning; they do not themselves provide this particular exact optimization over initial extended-Krylov data.

## Limitations

This is an exact-arithmetic first-block geometric theorem. It does not prove a floating-point roundoff estimate, instability of a completed Krylov solver, an inequality for indefinite or nonsymmetric matrices, or anything about later Krylov blocks. The bound for the block condition number only makes sense when three distinct spectral values are active. Standard Kantorovich theory covers a principal inequality ingredient, so independent historical examination could reveal an equivalent constrained result not identified in the accessible literature.

## References

1. K. Lund and M. Schweitzer, *On the stability of basis construction in extended Krylov subspace methods*, arXiv:2610.21603 (first public 2026-10-15), https://arxiv.org/abs/2610.21603.
2. Z. Yan and S. Wu, *A Bauer–Hausdorff Matrix Inequality*, Abstract and Applied Analysis 2013, Article 894824, https://doi.org/10.1155/2013/894824.
3. E. Carson, K. Lund, and M. Rozložník, *The Stability of Block Variants of Classical Gram–Schmidt*, SIAM J. Matrix Anal. Appl. 42 (2021), 1365–1380, https://doi.org/10.1137/21M1394424.
4. Classical Kantorovich/Wielandt inequality (standard spectral cosine inequality); see the historical discussion and references in Yan–Wu (2013).
