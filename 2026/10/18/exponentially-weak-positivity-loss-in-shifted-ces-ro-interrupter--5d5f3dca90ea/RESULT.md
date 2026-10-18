# Exponentially weak positivity loss in shifted Cesàro interrupters

## Finding
For each \(0<\varepsilon<1\), consider the order-one generalized Cesàro operator \(M_{-\varepsilon}\) on \(\ell^2(\mathbb N_0)\), with matrix
\[
 (M_{-\varepsilon})_{nj}=
 \begin{cases}(n+1-\varepsilon)^{-1},&0\le j\le n,\\0,&j>n.\end{cases}
\]
Let the finite-support right inverse and bounded auxiliary operator be defined by
\[
 L_{-\varepsilon}e_j=(j+1-\varepsilon)(e_j-e_{j+1}),
 \qquad B_{-\varepsilon}\big|_{c_{00}}=M_{-\varepsilon}^*L_{-\varepsilon}.
\]
Put \(b=2-\varepsilon\), \(r_n=(n+b)^{-1}\), \(r=(r_n)_{n\ge0}\), and \(R=\operatorname{diag}(r_n)\). Then the bounded compact auxiliary defect has the exact identity
\[
 D_\varepsilon:=I-B_{-\varepsilon}^*B_{-\varepsilon}
 =R-\varepsilon rr^*.
\]
It has **exactly one negative eigenvalue**, simple, equal to \(-\delta_\varepsilon\), where \(\delta_\varepsilon>0\) is uniquely determined by the digamma equation
\[
 \boxed{\ \varepsilon\bigl[\psi(2-\varepsilon+\delta_\varepsilon^{-1})
              -\psi(2-\varepsilon)\bigr]=1.\ }
\]
As the hyponormality threshold is approached from below, its magnitude obeys the **beyond-all-powers** law
\[
 \boxed{\ \delta_\varepsilon
 =\exp\left(-\frac1\varepsilon-\psi(2-\varepsilon)\right)(1+o(1)),
 \qquad \lim_{\varepsilon\downarrow0}e^{1/\varepsilon}\delta_\varepsilon
 =e^{\gamma_{\mathrm E}-1}.\ }
\]
Here \(\psi\) is the digamma function and \(\gamma_{\mathrm E}\) is Euler's constant.

The unique nonnegative unit eigenvector is
\[
 u_n^{(\varepsilon)}=\frac{c_\varepsilon}{1+\delta_\varepsilon(n+2-\varepsilon)},
 \qquad c_\varepsilon^{-2}
 =\sum_{n\ge0}\frac1{(1+\delta_\varepsilon(n+2-\varepsilon))^2}.
\]
Its mass localizes at the exponentially large coordinate scale. More precisely,
\[
 \frac{c_\varepsilon^2}{\delta_\varepsilon}\longrightarrow1,
 \qquad
 \sum_{n\ge0}|u_n^{(\varepsilon)}|^2
 \delta_{\,\delta_\varepsilon(n+2-\varepsilon)}
 \ \Longrightarrow\ \frac{\mathbf1_{[0,\infty)}(t)}{(1+t)^2}\,dt
 \quad(\varepsilon\downarrow0).
\]
The symbol \(\delta_t\) in the measure convergence denotes a Dirac point mass, not the spectral quantity \(\delta_\varepsilon\).

There is also an **exact finite-detection horizon**. Let \(P_N\) project onto \(e_0,\ldots,e_{N-1}\), and let \(N_*(\varepsilon)\) be the first positive integer for which \(P_ND_\varepsilon P_N\), acting on \(P_N\ell^2\), has a negative eigenvalue. Then
\[
 \boxed{\ N_*(\varepsilon)=\min\bigl\{N\ge1:
 \varepsilon[\psi(N+2-\varepsilon)-\psi(2-\varepsilon)]>1\bigr\},\quad
 \lim_{\varepsilon\downarrow0}e^{-1/\varepsilon}N_*(\varepsilon)=e^{1-\gamma_{\mathrm E}},\quad
 N_*(\varepsilon)\delta_\varepsilon\to1.\ }
\]
All smaller initial-coordinate compressions are nonnegative (possibly singular). Finally, the **actual self-commutator** \(M_{-\varepsilon}^*M_{-\varepsilon}-M_{-\varepsilon}M_{-\varepsilon}^*\) has exactly one negative eigenvalue. No assertion is made that its negative eigenvalue has magnitude \(\delta_\varepsilon\).

## Assumptions and scope
All operators act on the complex Hilbert space \(\ell^2(\mathbb N_0)\). The parameter satisfies \(0<\varepsilon<1\) without any asymptotic assumption unless the limit \(\varepsilon\downarrow0\) is explicitly stated. The operator \(L_{-\varepsilon}\) is defined **only on finitely supported vectors**; it is not assumed bounded. The auxiliary operator \(B_{-\varepsilon}\) is defined first by \(M_{-\varepsilon}^*L_{-\varepsilon}\) on that domain and then extended boundedly. Compactness and the negative eigenvalue concern \(D_\varepsilon\); the last inertia assertion concerns the distinct original self-commutator.

For a bounded self-adjoint operator, the number of negative eigenvalues counts multiplicity. Convergence of probability measures in the statement is weak convergence against all bounded continuous test functions on \([0,\infty)\). The compression \(P_ND_\varepsilon P_N\) is restricted to the \(N\)-dimensional range of \(P_N\), rather than being considered on all of \(\ell^2\) with an extraneous zero eigenspace.

## Proof
**1. Exact columns and the compact defect.** The Schur test with weights \((n+1)^{-1/2}\) bounds \(M_{-\varepsilon}\): its entries are bounded by \((1-\varepsilon)^{-1}(n+1)^{-1}\), and the weighted row and column sums are uniformly bounded. On the finite-support domain, direct rowwise cancellation gives \(M_{-\varepsilon}L_{-\varepsilon}x=x\). The \(j\)-th column of \(B_0=M_{-\varepsilon}^*L_{-\varepsilon}\) is
\[
 (B_0e_j)_i=\begin{cases}r_j,&0\le i\le j,\\r_j-1,&i=j+1,\\0,&i\ge j+2.\end{cases}
\]
Consequently, for \(i<j\), the column inner product is
\[
 \langle B_0e_i,B_0e_j\rangle
 =[(i+2)r_i-1]r_j=\varepsilon r_ir_j,
\]
and its diagonal is \((i+1)r_i^2+(1-r_i)^2=1-r_i+\varepsilon r_i^2\). The resulting bounded Gram form extends \(B_0\) uniquely to a bounded operator \(B\), and gives
\[
 B^*B=I-R+\varepsilon rr^*,\qquad D_\varepsilon=R-\varepsilon rr^*.
\]
Because \(r_n\to0\) and \(r\in\ell^2\), both \(R\) and \(rr^*\) are compact, hence so is \(D_\varepsilon\). The positive \(R\) has trivial kernel and the rank-one subtraction has negative index at most one.

**2. The exact negative eigenvalue.** A negative eigenvalue \(-\delta\) satisfies
\[
 (R+\delta I)u=\varepsilon\langle u,r\rangle r.
\]
Any nonzero solution must be proportional to \((R+\delta I)^{-1}r\), and the necessary-and-sufficient scalar equation is
\[
 1=\varepsilon\sum_{n=0}^\infty\frac{r_n^2}{r_n+\delta}
 =\varepsilon\sum_{n=0}^\infty
 \left(\frac1{n+b}-\frac1{n+b+\delta^{-1}}\right).
\]
The digamma summation identity turns this into the boxed equation. Its right-hand sum decreases strictly and continuously from \(+\infty\) as \(\delta\downarrow0\) to zero as \(\delta\to\infty\). Thus there is exactly one positive root; its eigenspace is one-dimensional and, by the negative-index bound, there are no other negative eigenvalues. Substitution yields the stated eigenvector.

**3. Exponential law.** The scalar equation implies \(\delta_\varepsilon\to0\) as \(\varepsilon\downarrow0\). Uniformly for \(b\in[1,2]\), the standard digamma asymptotic gives
\[
 \psi(b+\delta^{-1})=\log(\delta^{-1})+O(\delta).
\]
Therefore
\[
 \log(\delta_\varepsilon^{-1})
 =\varepsilon^{-1}+\psi(2-\varepsilon)+O(\delta_\varepsilon).
\]
Exponentiating gives the sharp multiplicative asymptotic; \(\psi(2)=1-\gamma_{\mathrm E}\) gives the limit constant. In particular, \(\delta_\varepsilon\) is smaller than every fixed positive power of \(\varepsilon\).

**4. Universal eigenvector profile.** With \(h=\delta_\varepsilon\), the normalization denominator is a Riemann sum on a mesh of width \(h\):
\[
 h\sum_{n\ge0}[1+h(n+b)]^{-2}\longrightarrow
 \int_0^\infty(1+t)^{-2}dt=1.
\]
Thus \(c_\varepsilon^2/h\to1\). Inserting any bounded continuous test function \(\varphi\) and applying the same Riemann-sum argument (first truncate a tail using integrability, then pass to the limit on a compact interval) gives
\[
 \sum_{n\ge0}|u_n^{(\varepsilon)}|^2\varphi(h(n+b))
 \longrightarrow\int_0^\infty\frac{\varphi(t)}{(1+t)^2}\,dt.
\]

**5. The optimal initial-coordinate detection size.** On \(P_N\ell^2\), the defect is congruent to
\[
 R_N^{1/2}\bigl(I_N-\varepsilon z_Nz_N^*\bigr)R_N^{1/2},
 \qquad (z_N)_n=\sqrt{r_n},\quad0\le n<N.
\]
Its least inertia is negative exactly when \(\varepsilon\sum_{n<N}r_n>1\), and that sum is \(\varepsilon[\psi(N+b)-\psi(b)]\). Since it increases without bound, the minimum \(N_*\) is finite. At the transition the defining inequalities at \(N_*-1\) and \(N_*\) imply
\[
 \varepsilon^{-1}=\psi(N_*+b)-\psi(b)+O(N_*^{-1}).
\]
Using \(\psi(x)=\log x+O(x^{-1})\) proves
\[
 \log N_*=\varepsilon^{-1}+\psi(b)+o(1).
\]
The displayed threshold asymptotics and \(N_*\delta_\varepsilon\to1\) follow.

**6. Exactly one negative direction for the self-commutator.** A vector orthogonal to all \(L_{-\varepsilon}e_j\) has constant coordinates, so must vanish in \(\ell^2\); hence \(L_{-\varepsilon}(c_{00})\) is dense. On that dense subspace, \(BM_{-\varepsilon}L_{-\varepsilon}x=B x=M_{-\varepsilon}^*L_{-\varepsilon}x\), so boundedness yields \(BM_{-\varepsilon}=M_{-\varepsilon}^*\). Consequently
\[
 M_{-\varepsilon}^*M_{-\varepsilon}-M_{-\varepsilon}M_{-\varepsilon}^*
 =M_{-\varepsilon}^*D_\varepsilon M_{-\varepsilon}.
\]
The rank-one negative-index bound passes under congruence by a bounded operator, so the self-commutator has at most one negative eigenvalue. Since \(M_{-\varepsilon}\) has range containing every finitely supported vector (via its right inverse), its range is dense. A negative test vector for \(D_\varepsilon\) can therefore be approximated in the range; continuity gives a negative test vector for the self-commutator. Compactness follows from compactness of \(D_\varepsilon\). A compact self-adjoint operator with one negative direction has exactly one negative eigenvalue. This completes the proof.

## Verification
The standalone program `verify.py`, run with `python verify.py` after installing the dependency in `requirements.txt`, tests **1,296 exact rational finite-column Gram identities**, independently solves the digamma eigenvalue equation at five negative shifts using 85-digit arithmetic, and computes the **first negative finite compression** by integer bisection (including a horizon exceeding \(10^{21}\)). It also checks the exponential prefactor and eigenvector normalization asymptotically. These numerical checks validate the derived formulas; the infinite-dimensional and asymptotic assertions are proved in the preceding six steps, not by the computation.

## Relationship to prior work
Yicen Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order* (arXiv:2610.00193v1, first posted 18 September 2026), proves the positivity threshold and a general finite-rank auxiliary defect decomposition. In its negative-parameter argument, finite-support vectors establish a negative direction. That work supplies the natural question and a closely related structural identity; the present contribution is the **exact unique negative eigenvalue, its exponentially weak magnitude and prefactor, the rescaled eigenvector law, and the sharp first-detectable compression size** for order one. The qualitative rank-one sign obstruction alone does not give any of these quantitative boundary laws.

Earlier work of Le and Rhaly on coposinormality treats unshifted Cesàro matrices and diagonal interrupters. The related generalized-order sharp weighted self-commutator coefficient theorem gives an unbounded-below Rayleigh quotient for negative shifts, not the finite negative eigenvalue of the compact auxiliary defect or its singular scale. A separate result on a rank-one perturbation of the normal real-variable Cesàro operator concerns a different operator and spectrum. These distinctions are by object and logical implication, not merely by terminology.

## Limitations
The spectral magnitude \(\delta_\varepsilon\) belongs to the auxiliary operator \(I-B^*B\), **not** to the original Cesàro self-commutator. Only the latter's number of negative eigenvalues is determined. The result is for **order one** and \(-1<\alpha<0\); higher orders may have several negative rank-one directions. The weak limit is in the rescaled coordinate \(\delta_\varepsilon(n+2-\varepsilon)\), not in fixed index coordinates. The conclusion that an operator-theory claim is mathematically distinct does not establish bibliographic priority over all possible earlier formulations of general rank-one weak-binding theory.

## References
1. Y. Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1, 18 September 2026; full text: https://arxiv.org/html/2610.00193v1.
2. T. Le and H. C. Rhaly Jr., *Coposinormality of the Cesàro matrices*, Archiv der Mathematik 110 (2018), DOI:10.1007/s00013-017-1128-y.
3. *Finite Gram reduction of sharp Cesàro self-commutator bounds at every order*, publicly available mathematical research record, 11 October 2026.
4. *Real-eigenvalue bifurcations for a rank-one perturbation of the normal Cesàro operator*, publicly available mathematical research record, 11 October 2026.
