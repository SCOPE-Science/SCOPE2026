# Sharp two-sector numerical-radius sum bound and angular phase transition

## Finding
Let \(H\) be a nonzero complex Hilbert space, and let \(A,B\in\mathcal B(H)\). Suppose
\[
W(A)\subset\Sigma_\alpha,\quad W(B)\subset\Sigma_\beta,\qquad
\Sigma_\theta=\{re^{i\phi}:r>0,\ |\phi|\le\theta\},
\quad 0\le\alpha,\beta<\frac\pi2.
\]
Put \(\delta=\alpha+\beta\) and let \(w(T)=\sup_{\|x\|=1}|\langle Tx,x\rangle|\). Then the optimal universal constant, with no condition on dimension or commutativity, is
\[
\boxed{\quad w(A+B)\ge C(\alpha,\beta)\max\{w(A),w(B)\},\qquad
C(\alpha,\beta)=\begin{cases}
1,&0\le\delta\le\pi/2,\\
\sin\delta,&\pi/2<\delta<\pi.
\end{cases}\quad}
\]
More precisely, for each fixed pair of sector half-angles, no larger constant works for all such operators; dimension one already realizes or approximates the optimum. When the two half-angles coincide at \(\gamma\), exact numerical-radius monotonicity under addition holds for \(\gamma\le\pi/4\). For \(\gamma>\pi/4\) its sharp replacement is the factor \(\sin(2\gamma)\). In finite dimensions the inequality is strict when \(\delta\le\pi/2\), though strictness fails for some infinite-dimensional examples.

## Assumptions and scope
The inner product is any conventional complex Hilbert inner product; the numerical range and numerical radius do not depend on the convention. The sectors are centered on the positive real axis and exclude the origin, while permitting either boundary ray. Thus the real part of each quadratic form is positive on every nonzero vector; no uniform strictly positive lower bound is required. The angles, operator dimensions and norms are otherwise arbitrary. For the sharpness quantifier, for every \((\alpha,\beta)\) in the indicated range, \(C(\alpha,\beta)\) is the infimum of \(w(A+B)/\max\{w(A),w(B)\}\) over all admissible operators and Hilbert spaces.

## Proof
For nonzero complex numbers \(z\in\Sigma_\alpha\) and \(v\in\Sigma_\beta\), their angular separation \(\vartheta\) obeys \(0\le\vartheta\le\delta<\pi\). Write \(r=|v|/|z|\). Then
\[
\frac{|z+v|^2}{|z|^2}=1+r^2+2r\cos\vartheta
\ge 1+r^2+2r\cos\delta.
\]
If \(\delta\le\pi/2\), the rightmost expression is at least \(1\). If \(\delta>\pi/2\), complete the square:
\[
1+r^2+2r\cos\delta=(r+\cos\delta)^2+\sin^2\delta
\ge\sin^2\delta.
\]
Therefore \(|z+v|\ge C(\alpha,\beta)|z|\). Exchanging \(z\) and \(v\) yields the same inequality with \(|v|\), so
\[
|z+v|\ge C(\alpha,\beta)\max\{|z|,|v|\}.
\]
For every unit vector \(x\), apply this scalar lemma with \(z=\langle Ax,x\rangle\) and \(v=\langle Bx,x\rangle\). Taking the supremum over \(x\) gives both \(w(A+B)\ge Cw(A)\) and \(w(A+B)\ge Cw(B)\), hence the displayed theorem. This argument neither assumes nor requires attainment of the numerical radius.

For \(\delta>\pi/2\), take the one-dimensional operators (complex scalars)
\[
A=e^{i\alpha},\qquad B=(-\cos\delta)e^{-i\beta}.
\]
Because \(0<-\cos\delta<1\), both are strictly accretive and \(\max\{w(A),w(B)\}=1\). Their arguments differ by exactly \(\delta\), and completing the same square with \(r=-\cos\delta\) shows \(w(A+B)=\sin\delta\). Thus no larger constant is valid. For \(\delta\le\pi/2\), take the scalars \(A=1\), \(B=\varepsilon>0\). Their ratio is \(1+\varepsilon\to1\), so the factor \(1\) is optimal but not scalar-attained by two nonzero summands.

If \(H\) is finite-dimensional and \(\delta\le\pi/2\), a unit vector \(x\) attaining \(w(A)\) exists. Both quadratic form values are nonzero, and
\[
|\langle(A+B)x,x\rangle|^2
=|\langle Ax,x\rangle|^2+|\langle Bx,x\rangle|^2
+2\operatorname{Re}(\langle Ax,x\rangle\overline{\langle Bx,x\rangle})
>|\langle Ax,x\rangle|^2.
\]
Hence \(w(A+B)>w(A)\), and likewise \(w(A+B)>w(B)\). In infinite dimension the scalar dominance remains valid, but strictness need not: on \(\ell^2(\mathbb N)\), take positive diagonal operators with diagonal values \(A_{nn}=1-1/(n+1)\) and \(B_{nn}=1/[2(n+1)]\). Both quadratic forms are strictly positive, while \(w(A)=w(A+B)=1\).

## Verification
The proof is dimension-free and analytic; the decisive identity is the exact polynomial square completion above, and the extremal dimension-one family saturates it. The accompanying standard-library verifier, `verify_sector_sum.py`, independently checks the square-completion polynomial coefficient by coefficient over the integers and exact rational-arithmetic checks for a nontrivial extremizer. Its finite checks confirm the displayed algebra but are not substituted for the all-operator proof. For example, at \(\alpha=\beta=\pi/3\), the scalar pair \(A=e^{i\pi/3}\) and \(B=\tfrac12 e^{-i\pi/3}\) has \(w(A+B)=\sqrt3/2\) and \(\max\{w(A),w(B)\}=1\).

## Relationship to prior work
Bedrani, Kittaneh and Sababheh (2020), Theorem 3.6, proved \(w(A+B)\ge\cos^2(\gamma)\max\{w(A),w(B)\}\) for two matrices in a common sector of half-angle \(\gamma\). Sheikhhosseini and Khosravi (2026), Theorem 4.10, extend that same factor to their *weighted* numerical radius. The present result determines the exact constant for the **ordinary** numerical radius, also allowing unequal half-angles and arbitrary Hilbert-space dimension. It does **not** assert an improvement for general weighted numerical radii. The 2022 work of Bhunia, Paul and Sen contains other sectorial numerical-radius sum, product and power inequalities; its inspected statements do not contain this sharp reverse-sum constant. The bound here is stronger than \(\cos^2\gamma\) for all \(0<\gamma<\pi/2\), with the exact transition at \(\gamma=\pi/4\). No priority claim beyond the particular inspected sources and targeted searches is made.

## Limitations
This theorem requires the two numerical ranges to lie in right-half-plane sectors centered on the **same** positive real axis; arbitrary rotations of the sectors can invalidate the stated constant. The optimal constant is universal, not a description of the sharper factor for each fixed operator pair. The proof concerns the ordinary numerical radius, not the whole family of weighted numerical radii, nor operator norm. The acute-case optimal factor is an infimum, not attained by finite-dimensional admissible pairs. The derivation uses elementary plane geometry; an independently published equivalent argument not identified by the inspected literature remains possible.

## References
1. Alemeh Sheikhhosseini and Maram Khosravi, *Weighted numerical radii of accretive matrices*, arXiv:2608.08507v1, first public 2026-08-09, Theorem 4.10; https://arxiv.org/abs/2608.08507.
2. M. Bedrani, F. Kittaneh and M. Sababheh, *Numerical radii of accretive matrices*, arXiv:2007.08654v1 (2020), Theorem 3.6; https://arxiv.org/abs/2007.08654.
3. P. Bhunia, K. Paul and A. Sen, *Numerical radius inequalities of sectorial matrices*, arXiv:2208.09816v1 (2022), published in *Annals of Functional Analysis* 14 (2023), Paper 66; https://arxiv.org/abs/2208.09816.
