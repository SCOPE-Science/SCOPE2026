# Sharp two-sided overlap stability for rank-one max-phase Schatten quasi-norms

## Finding

**Theorem (exact rank-one envelope and sharp stability).** Let \(H\) be any complex Hilbert space with \(\dim H\ge2\). For arbitrary \(0<p<1\), positive numbers \(a,b\), and unit vectors \(u,v,x,y\in H\), write
\[
A=a\,uv^*,\qquad B=b\,xy^*,\qquad
Q=|\langle u,x\rangle|^2+|\langle v,y\rangle|^2\in[0,2].
\]
Here \(uv^*\) sends \(h\) to \(u\langle v,h\rangle\). Define the max-phase moment
\[
M_p(A,B)=\max\{\|A+B\|_p^p,\|A-B\|_p^p\}.
\]
Then the **optimal dimension-independent upper envelope at prescribed \(a,b,Q\)** is
\[
M_p(A,B)\le F_{p,a,b}(Q)
=\left(\frac{a+b+\sqrt{(a-b)^2+2abQ}}2\right)^p
+\left(\frac{a+b-\sqrt{(a-b)^2+2abQ}}2\right)^p.
\]
Every \(Q\in[0,2]\) admits equality already on \(\mathbb C^2\): choose rank-one orthogonal projections \(P_u,P_x\) with \(|\langle u,x\rangle|^2=Q/2\), and take \(A=aP_u\), \(B=bP_x\).

Writing \(G_{p,a,b}(Q)=a^p+b^p-F_{p,a,b}(Q)\), the function \(G\) is continuous on \([0,2]\), strictly increasing and strictly convex on \((0,2)\), and \(G(0)=0\). Consequently every rank-one pair satisfies the **sharp quantitative two-sided orthogonality law**
\[
\boxed{a^p+b^p-M_p(A,B)\ge K_p(a,b)
\bigl(|\langle u,x\rangle|^2+|\langle v,y\rangle|^2\bigr),}
\]
where
\[
K_p(a,b)=
\begin{cases}
\displaystyle\frac{pab}{2}\frac{a^{p-1}-b^{p-1}}{b-a},&a\ne b,\\
\displaystyle\frac{p(1-p)}2a^p,&a=b.
\end{cases}
\]
This positive coefficient cannot be increased, even if the space is restricted to \(\mathbb C^2\). An exact stronger version is the nonlinear lower bound \(a^p+b^p-M_p(A,B)\ge G_{p,a,b}(Q)\), with optimality at each \(Q\). In particular, if the max-phase defect is at most \(\varepsilon\), then
\[
Q\le\min\{2,\varepsilon/K_p(a,b)\};
\]
whenever \(0\le\varepsilon\le G_{p,a,b}(2)\), the sharper conclusion is \(Q\le G_{p,a,b}^{-1}(\varepsilon)\). For equally normalized rank-one operators this reads \(Q\le 2\varepsilon/[p(1-p)]\).

## Assumptions and scope

The operators have **rank exactly one** and **positive singular amplitudes** \(a,b\). The ambient Hilbert space can be infinite dimensional: all relevant action lies in two-dimensional left and right subspaces. Complex phases are arbitrary; the max is taken over the two signs, not all complex phases. The statement does **not** assert a stability inequality for higher-rank operators, nor a stability theorem for arbitrary approximately isometric maps. The quantity \(Q\) measures both left and right support overlaps; for rank one it also equals \((\|A^*B\|_1^2+\|AB^*\|_1^2)/(a^2b^2)\).

## Proof

**Step 1: exact two-singular-value invariants.** Put \(c=|\langle u,x\rangle|\), \(d=|\langle v,y\rangle|\), and \(t=cd\). Directly computing the trace and determinant of the nonzero two-by-two corner of \((A\pm B)^*(A\pm B)\) shows that its two (possibly zero) eigenvalues have
\[
s_\pm=a^2+b^2\pm2ab\,\Re\bigl(\langle u,x\rangle\langle y,v\rangle\bigr),\qquad
P=a^2b^2(1-c^2)(1-d^2).
\]
The determinant identity follows either from a two-by-two representation on the spans of the left and right vectors, or from the exterior-power identity \(\|\wedge^2(A\pm B)\|^2=a^2b^2(1-c^2)(1-d^2)\). The latter is valid also when either overlap is one, by continuity. Set \(r=p/2\in(0,1)\), and for \(s\ge2\sqrt P\) put
\[
\Psi_r(s,P)=\left(\frac{s+\sqrt{s^2-4P}}2\right)^r
+\left(\frac{s-\sqrt{s^2-4P}}2\right)^r.
\]
It follows exactly that \(M_p(A,B)=\Psi_r(a^2+b^2+2ab|\Re\langle u,x\rangle\langle y,v\rangle|,P)\).

**Step 2: joint monotonicity and constrained maximization.** Let \(\lambda_1\ge\lambda_2\ge0\) be the roots of \(z^2-sz+P=0\). For \(\lambda_1>\lambda_2>0\), elementary differentiation gives
\[
\frac{\partial\Psi_r}{\partial s}
=r\frac{\lambda_1^r-\lambda_2^r}{\lambda_1-\lambda_2}>0,
\qquad
\frac{\partial\Psi_r}{\partial P}
=r\frac{\lambda_2^{r-1}-\lambda_1^{r-1}}{\lambda_1-\lambda_2}>0.
\]
The monotonicity extends to repeated and zero roots by continuity. Since \(|\Re\langle u,x\rangle\langle y,v\rangle|\le t\), and \(P=a^2b^2(1-Q+t^2)\), both arguments of \(\Psi_r\) are bounded by those obtained with \(t=Q/2\), using \(2cd\le c^2+d^2=Q\). The resulting maximal invariants are exactly those of \(aP_u+bP_x\) with \(|\langle u,x\rangle|^2=Q/2\); the two positive eigenvalues of this latter matrix equal
\[
\lambda_\pm(Q)=\frac{a+b\pm\sqrt{(a-b)^2+2abQ}}2.
\]
This proves the sharp envelope for every feasible \(Q\), including endpoints by continuity.

**Step 3: exact modulus, monotonicity, and curvature.** For \(0<p<1\), the elementary Stieltjes formula is
\[
z^p=\frac{\sin(\pi p)}\pi\int_0^\infty\frac{z}{z+s}s^{p-1}\,ds\quad(z\ge0).
\]
Set \(S=a+b\), \(D(Q)=ab(1-Q/2)\) and \(C_p=\sin(\pi p)/\pi\). Since \(\lambda_++\lambda_-=S\) and \(\lambda_+\lambda_-=D\), adding the two Stieltjes integrands yields
\[
F_{p,a,b}(Q)=C_p\int_0^\infty s^{p-1}
\frac{sS+2D(Q)}{s^2+sS+D(Q)}\,ds.
\]
For \(0<Q<2\), differentiation under the integral is legitimate (uniformly on compact interior subintervals). Its first derivative is
\[
F'(Q)=-\frac{C_pab}{2}\int_0^\infty s^{p-1}
\frac{s(2s+S)}{(s^2+sS+D(Q))^2}\,ds<0,
\]
and its second derivative is
\[
F''(Q)=-\frac{C_p(ab)^2}{2}\int_0^\infty s^{p-1}
\frac{s(2s+S)}{(s^2+sS+D(Q))^3}\,ds<0.
\]
Thus \(G=a^p+b^p-F\) is strictly increasing and strictly convex. At \(Q=0\) the unordered pair of eigenvalues is \(\{a,b\}\), and direct differentiation of the square-root expression gives \(-F'(0)=K_p(a,b)\) for \(a\ne b\). When \(a=b\), use \(F(Q)=a^p[(1+\sqrt{Q/2})^p+(1-\sqrt{Q/2})^p]\) to obtain \(-F'(0)=p(1-p)a^p/2\). Convexity gives \(G(Q)\ge G'(0)Q=K_p(a,b)Q\). Every coefficient is optimal: the projection family from Step 2 has defect exactly \(G(Q)=K_p(a,b)Q+o(Q)\) as \(Q\downarrow0\). The inverse-modulus bound follows from strict monotonicity of \(G\). This concludes the proof.

## Verification

The accompanying standard-library program `checks/verify.py` directly constructs complex two-by-two rank-one examples, evaluates their two singular values using the trace/determinant of the Gram matrix, and checks the sharp envelope and tangent inequality over a fixed reproducible grid; it separately checks attaining projection pairs and the small-overlap slope for equal and unequal amplitudes. The program is a finite numerical diagnostic, **not** a proof of the all-parameter theorem; Steps 1–3 are analytic.

## Relationship to prior work

Zhang and Liu, *On Surjective Max-Phase Isometries of Schatten p-Classes (0<p<1)*, arXiv:2610.13271, published October 9, 2026, Lemmas 2.1, 2.6, and 2.7 and Theorem 1.1, establish qualitative two-sided support rigidity and the rank-one two-singular-value max-phase formula for normalized partial isometries. The present theorem uses that structure **without claiming the rank-one spectral computation itself as new**, and asks a different, quantitative variational question: at specified (possibly unequal) amplitudes and specified **combined left/right squared overlap**, what is the exact maximal max-phase moment and the best global stability coefficient? The equality-at-zero result of Zhang–Liu does not state an envelope, strict convexity, an optimal coefficient, or a quantitative near-equality estimate.

Huang and Zhu, *Tingley's Problem for Schatten p-Classes, 0<p≠2<∞*, arXiv:2607.11244, first posted July 13, 2026, Lemmas 3.3–3.4, also obtain qualitative phase recovery via the two-singular-value trace/determinant data. Their conclusion does not compare all pairs with a fixed sum of squared left and right overlaps or optimize over unequal amplitudes. General sharp Schatten inequalities for larger exponents, such as Qiu's arXiv:2608.17565, address a different range and functional. Results on Schatten-four support rigidity likewise concern a different exponent and angle functional.

## Limitations

The result concerns **rank-one operators only** and proves neither stability of arbitrary nonlinear maps nor high-rank support estimates. Its exact profile is a constrained optimization of previously known rank-one spectral identities; priority risk remains that a broad unlocated matrix-concavity or stability result might already imply this optimized profile. No independent mathematical audit has been performed. At very small \(p\), finite-precision singular-value routines must explicitly exclude numerical null singular values; the provided two-by-two checker uses both eigenvalues of the exact rank-two corner.

## References

1. Wenwen Zhang and Qi Liu, *On Surjective Max-Phase Isometries of Schatten p-Classes (0<p<1)*, arXiv:2610.13271, first posted 2026-10-09. https://arxiv.org/abs/2610.13271
2. Jinghao Huang and Yunpeng Zhu, *Tingley's Problem for Schatten p-Classes, 0<p≠2<∞*, arXiv:2607.11244, first posted 2026-07-13. https://arxiv.org/pdf/2607.11244
3. Hongsen Qiu, *Sharp Quasi-Reverse Minkowski Inequality for Schatten Norms*, arXiv:2608.17565, first posted 2026-08-18. https://arxiv.org/abs/2608.17565
