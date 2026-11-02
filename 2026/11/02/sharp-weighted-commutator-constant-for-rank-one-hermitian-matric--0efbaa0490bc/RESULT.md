# Sharp weighted commutator constant for rank-one Hermitian matrices

## Finding
For any positive-definite Hermitian \(A\in M_n(\mathbb C)\), \(n\ge2\), write its two smallest eigenvalues, counted with multiplicity, as \(0<a=\lambda_1\le b=\lambda_2\). Define \(S=a+b\), \(\Delta=b-a\), and \(t_*\in[1/\sqrt2,1)\) as the unique solution of
\[
S(1-2t_*^2)+\Delta t_*^3=0.
\]
For every pair of nonzero Hermitian rank-one matrices \(X,Y\), the following inequality is sharp:
\[
\|XY-YX\|_{\mathrm F}^2\le C_A^{\mathrm H}\|X\|_A^2\|Y\|_A^2,
\qquad
C_A^{\mathrm H}=\frac{8t_*^2(1-t_*^2)}{[a(1+t_*)+b(1-t_*)]^2}
=\frac{2}{ab}(3t_*^2-t_*^4-1).
\]
Exactly the same sharp constant holds for nonzero positive semidefinite rank-one pairs. In both cases, two rank-one orthogonal projections onto suitable unit vectors in the spectral plane for \(a,b\) attain the bound. The normalized constant \(abC_A^{\mathrm H}/2\) is strictly increasing with the ratio \(b/a\), starts at \(1/4\), and tends to \(1\), so that \(C_A^{\mathrm H}\sim 2/(ab)\) as \(b/a\to\infty\) with \(a\) fixed.

## Assumptions and scope
Here \(\|Z\|_{\mathrm F}^2=\operatorname{tr}(Z^*Z)\), \(\|Z\|_A^2=\operatorname{tr}(AZ^*Z)\), and \(A>0\). Matrices \(X,Y\) are complex Hermitian rank one, not arbitrary rank-one matrices. Zero is excluded from the sharp-ratio definition but satisfies the inequality trivially. A nonzero rank-one Hermitian matrix is \(r uu^*\) for real \(r\ne0\) and a unit column \(u\); it is positive semidefinite precisely when \(r>0\). The statement holds uniformly in dimension and eigenvalue multiplicities.

## Proof
**1. Reduction to one real overlap.** The quotient is invariant under separate nonzero real rescalings of \(X,Y\), so set \(X=uu^*\), \(Y=vv^*\), where \(\|u\|=\|v\|=1\). Write \(t=|u^*v|\in[0,1]\). Direct expansion, using \((uu^*)(vv^*)=(u^*v)uv^*\), gives
\[
\|[uu^*,vv^*]\|_{\mathrm F}^2=2t^2(1-t^2),\qquad
\|uu^*\|_A^2=u^*Au,\quad\|vv^*\|_A^2=v^*Av.
\]
Thus the sharp quotient at fixed overlap \(t\) is \(2t^2(1-t^2)/D(t)\), where \(D(t)\) is the smallest product \((u^*Au)(v^*Av)\) among unit vectors having overlap modulus \(t\).

**2. Exact Rayleigh-product denominator.** The relevant previously established Rayleigh-product minimization (Pang, Lemma 3.1, cited below) is
\[
D(t)=\begin{cases}
ab(1-t^2),&0\le t\le \delta,\\
\tfrac14[S-\Delta t]^2,&\delta<t\le1,
\end{cases}
\qquad \delta=\frac{b-a}{b+a}.
\]
For completeness, its decisive inequalities can be reconstructed as follows. If \(t<1\), phase \(v\) so that \(u^*v=t\), and form the orthonormal vectors \(f=(u+v)/\sqrt{2(1+t)}\) and \(g=(u-v)/\sqrt{2(1-t)}\). Compression of \(A\) onto their span has eigenvalues \(\mu_1\ge a\), \(\mu_2\ge b\), by the first two Courant–Fischer bounds. Replacing them in the compression's own eigenbasis by \(a,b\) decreases both Rayleigh quotients and hence their positive product. For the resulting two-eigenvalue compression \(H\), let \(x=f^*Hf\in[a,b]\). Then \(g^*Hg=S-x\), \(|f^*Hg|^2=(x-a)(b-x)\), and
\[
(u^*Hu)(v^*Hv)\ge
\left[x-\tfrac12S(1-t)\right]^2+ab(1-t^2).
\]
Minimizing the square over \(x\in[a,b]\) gives the stated two branches, with the transition at \(t=\delta\). Real spectral-plane choices realize every branch. At \(t=1\), \(u\) and \(v\) are proportional and \(D(1)=a^2\), agreeing with the second formula. If \(a=b\), \(D(t)=a^2\) for all overlaps, including \(t=0\), and two orthogonal \(a\)-eigenvectors are available because the lowest eigenvalue has multiplicity at least two.

**3. Unique optimal overlap.** On the first branch the quotient is \(2t^2/(ab)\), increasing for \(0\le t\le\delta\). On the second branch it is
\[
R(t)=\frac{8t^2(1-t^2)}{(S-\Delta t)^2}.
\]
For \(\delta<t<1\), differentiation shows that \(R'(t)\) has the sign of
\[
h(t)=S(1-2t^2)+\Delta t^3.
\]
Indeed, \(h'(t)=-t(4S-3\Delta t)<0\) for \(0<t\le1\), while \(h(\delta)=S(1-\delta^2)^2>0\) and \(h(1)=-2a<0\). There is exactly one root \(t_*\in(\delta,1)\), and it is the global maximizer. When \(\Delta=0\), \(\delta=0\) and \(t_*=1/\sqrt2\); if \(\Delta>0\), then \(h(1/\sqrt2)>0\) and \(t_*>1/\sqrt2\). This proves the first formula for \(C_A^{\mathrm H}\) and all endpoint cases.

**4. Attainment and equality.** Choose orthonormal eigenvectors \(e_1,e_2\) for the eigenvalues \(a,b\). Define
\[
 u=\sqrt{\frac{1+t_*}{2}}\,e_1+\sqrt{\frac{1-t_*}{2}}\,e_2,\qquad
 v=\sqrt{\frac{1+t_*}{2}}\,e_1-\sqrt{\frac{1-t_*}{2}}\,e_2.
\]
These unit vectors have \(u^*v=t_*\) and both Rayleigh quotients equal \(\tfrac12[a(1+t_*)+b(1-t_*)]\), the minimizing branch of \(D(t_*)\). The positive rank-one projections \(uu^*,vv^*\) attain equality. If \(a<b\), uniqueness of the optimal overlap, coupled with the interior equality case of the Rayleigh-product lemma, forces this spectral-plane form, up to eigenbasis choices and independent scalar rescaling. If \(a=b\), equality requires both generating vectors to lie in the smallest eigenspace and satisfy \(|u^*v|=1/\sqrt2\); these conditions are sufficient. Hence the constant is attained even under the stricter positivity constraint.

**5. Normalization and anisotropy.** The critical equation gives \(\delta=(2t_*^2-1)/t_*^3\). Substitution and cancellation yield
\[
\frac{ab}{2}C_A^{\mathrm H}=3t_*^2-t_*^4-1.
\]
The function \(\delta(t)=(2t^2-1)/t^3\) increases strictly on \([1/\sqrt2,1)\), because \(\delta'(t)=(3-2t^2)/t^4>0\). Likewise \(3t^2-t^4-1\) increases strictly there. At \(\delta=0\) the normalized constant is \(1/4\); as \(\delta\uparrow1\) it tends to \(1\), proving the claimed exact monotone spectral profile and asymptotic behavior.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It computes every numerator from explicit matrix products and both weighted norms directly, checks the displayed maximizing projections, verifies the root identity, and tests 2,200 pseudorandom complex pairs in each of eight spectra of dimensions two, three, and four. Executing the included checker produced `VERIFY_OK`. Numerical tests do not establish the infinite-domain theorem; the preceding spectral and monotonicity arguments do.

## Relationship to prior work
Mayumi–Kimura–Ohno–Chruściński introduced the weighted Frobenius commutator framework and quantum-state motivation. Fang–Cheng developed its rank-one bounds and optimization question. Pang's October 2026 result determines the different sharp constant for **all** rank-one matrices, and his Lemma 3.1 supplies precisely the fixed-overlap Rayleigh-product denominator used here. That lemma and Pang's unrestricted result are **not new claims**. The present theorem evaluates the genuinely narrower Hermitian/positive rank-one problem: its commutator numerator is forced to \(2t^2(1-t^2)\), rather than Pang's independently optimized unrestricted numerator. In particular, as \(b/a\to\infty\) the Hermitian constant scales as \(2/(ab)\), whereas Pang's unrestricted constant tends to \(1/a^2\) with \(a\) fixed, so the distinction cannot be eliminated by asserting that both constants coincide.

## Limitations
The theorem applies only to pairs of rank-one Hermitian matrices and to positive-definite weights; it is not an inequality for arbitrary-rank Hermitian inputs. The exact Rayleigh-product lemma and the weighted-commutator setup belong to the cited earlier literature. A potentially overlapping earlier positive-operator inequality not identifiable from its accessible abstract remains a historical-priority risk. Numerical experiments are illustrative only, and independent mathematical validation is not claimed.

## References
1. Z. Pang, *A sharp weighted commutator inequality for rank-one matrices*, arXiv:2610.29240v1 (first posted 2026-10-21), especially Lemma 3.1 and Theorem 1.1. https://arxiv.org/html/2610.29240v1
2. A. Mayumi, G. Kimura, H. Ohno, D. Chruściński, *Böttcher–Wenzel inequality for weighted Frobenius norms and its application to quantum physics*, arXiv:2403.04199 (2024), https://arxiv.org/abs/2403.04199; *Linear Algebra and its Applications* 700 (2024), 35–49.
3. W. Fang and C.-M. Cheng, *On some conjectures concerning the Böttcher–Wenzel inequality for weighted Frobenius norms*, *Linear Algebra and its Applications* (2025), DOI:10.1016/j.laa.2025.03.015.
