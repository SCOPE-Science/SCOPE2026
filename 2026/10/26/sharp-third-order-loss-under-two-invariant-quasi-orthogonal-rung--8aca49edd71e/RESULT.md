# Sharp third-order loss under two-invariant quasi-orthogonal Runge–Kutta projection

## Finding
For two uncoupled planar oscillators of distinct nonzero frequencies, the frozen-gradient, stage-derivative-subspace quasi-orthogonal projection of classical three-stage Kutta Runge–Kutta conserves each oscillator's quadratic energy exactly, but generically destroys the integrator's third order. A local invariant-preserving correction of order \(h^3\) is **unavoidable** within the stage-derivative affine space and is sharply attained by the near-predictor quasi-orthogonal branch. Its accumulated error on fixed nonzero intervals is exactly of order \(h^2\), with an explicit positive asymptotic constant.

Write \(x_j=\omega_j^2\), \(E_j=\|u_j\|_2^2\) and \(S=x_1E_1+x_2E_2\). The sharp leading local correction norm is
\[
\mathcal C=\frac{|x_2-x_1|}{24}\sqrt{\frac{x_1E_1x_2E_2}{S}}>0.
\]
For an initial state \(q_0\) and any fixed \(T>0\), the repeatedly projected step, using the near-predictor branch, satisfies
\[
\lim_{n\to\infty}\frac{\|q_n-e^{TK}q_0\|_2}{(T/n)^2}=T\mathcal C.
\]
For frequencies \(1,2\) and unit modal norms, \(\mathcal C=1/(4\sqrt5)\).

## Assumptions and scope
Let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\), \(K=\operatorname{diag}(\omega_1J,\omega_2J)\), \(\omega_j>0\), \(\omega_1\ne\omega_2\). The ODE is \(\dot q=Kq\), \(q=(u_1,u_2)\in\mathbb R^4\), with \(E_j>0\). The two independently conserved energies are \(I_j(q)=\|u_j\|_2^2/2\). Arithmetic and gradients are exact. We use the classical Kutta three-stage order-three tableau, with derivative stages
\[
 k_1=Kq,\quad k_2=Kq+\frac h2K^2q,\quad k_3=Kq+hK^2q+h^2K^3q,
\]
and predictor \(q_{\mathrm{RK}}=q+hKq+h^2K^2q/2+h^3K^3q/6\). For every \(h>0\), \(\operatorname{span}\{k_1,k_2,k_3\}=\operatorname{span}\{Kq,K^2q,K^3q\}=:S(q)\), a three-dimensional space. The corrected value belongs to \(q_{\mathrm{RK}}+S(q)\), preserves both \(I_j\), and the correction is confined to the span of the two **orthogonal projections to** \(S(q)\) **of** \(\nabla I_j(q_{\mathrm{RK}})\), frozen at the predictor. We distinguish its branch continuous after the rescaling below from unrelated nonlinear roots. The projected-gradient directions are independent for each sufficiently small positive \(h\), but become nearly dependent as \(h\to0\).

## Proof
**Polynomial reduction.** Set \(W=[Kq,K^2q,K^3q]\), \(G=W^{\mathsf T}W\). Distinct positive frequencies and active modes imply \(G\succ0\): if a combination of those three columns vanishes, its modewise tangential and radial components force first the even coefficient to vanish and then the odd polynomial to vanish at two distinct \(x_j\). Each corrected point has unique coefficients
\[
 q^+=q+A Kq+B K^2q+C K^3q.
\]
On the mode with squared frequency \(x\), this is the vector \((1-Bx)u+(A-Cx)Ku\). Both quadratic invariants hold precisely when
\[
 Q(x_j)=0,\qquad Q(x)=(A^2-2B)+(B^2-2AC)x+C^2x^2.
\]
Since \(x_1\ne x_2\), this is equivalent to the two exact identities
\[
 A^2-2B=C^2x_1x_2,\qquad B^2-2AC=-C^2(x_1+x_2).
\]
**Sharp local barrier.** The predictor has \((A_0,B_0,C_0)=(h,h^2/2,h^3/6)\). If an energy-preserving correction is \(O(h^3)\), invertibility of \(W\) on its column space gives \((A-A_0,B-B_0,C-C_0)=O(h^3)\). Expanding the difference \(Q(x_2)-Q(x_1)\) then forces \(C/h^3\to1/8\). The first constraint implies \(B=h^2/2+h(A-h)+o(h^4)\). Thus, after passage to a subsequence when necessary, every candidate with finite rescaled leading displacement lies on
\[
 \frac{q^+-q_{\mathrm{RK}}}{h^3}\longrightarrow aKq-\frac1{24}K^3q.
\]
The least norm on this affine line is reached at
\[
 a_*=-\frac{x_1^2E_1+x_2^2E_2}{24S},
\]
and equals \(\mathcal C\). A smaller \(o(h^3)\) correction is impossible. This barrier concerns **all** energy-preserving points in the stage-derivative affine space, not only the quasi-orthogonal choice.

**Actual near-predictor quasi-orthogonal branch.** Set \(A=h+ah^3\), \(B=h^2/2+bh^4\), \(C=ch^3\). For each \(j\),
\[
 \frac{Q(x_j)}{h^4}=2(a-b)+(\tfrac14-2c)x_j+O(h^2).
\]
The two frozen projected gradients in coefficient space are proportional (through the positive weights \(x_jE_j\)) to \(G^{-1}R(x_j,h)^{\mathsf T}\), where
\[
 R(x,h)=(h-h^3x/6,\ -1+h^2x/2,\ -x(h-h^3x/6)).
\]
The two rows are independent for every sufficiently small positive \(h\). Their normalized cross product \(N_h=\bigl(R(x_1,h)\times R(x_2,h)\bigr)/\bigl(h(x_2-x_1)\bigr)\) extends analytically to \(h=0\), with limit \((1,0,0)\). The correction is in the projected-gradient span exactly when
\[
 (a,hb,c-\tfrac16)G N_h=0.
\]
At \(h=0\), the two invariant equations yield \(b=a\), \(c=1/8\); the subspace equation then yields \(a=a_*\). Their Jacobian with respect to \((a,b,c)\) is nonsingular since \(x_1\ne x_2\) and \(G_{11}=S>0\). The implicit function theorem therefore produces a unique nearby smooth solution \((a(h),b(h),c(h))\) for sufficiently small \(h\), giving
\[
 A=h+a_*h^3+o(h^3),\quad B=h^2/2+a_*h^4+o(h^4),\quad C=h^3/8+o(h^3).
\]
This branch attains the sharp local constant \(\mathcal C\). The collapse of the rank-two projected-gradient matrix at \(h=0\) explains why a dimension count alone does not ensure the usual order estimate.

**Global error.** Each corrected step multiplies mode \(j\), interpreted as a complex coordinate, by \(z_j(h)=1-B(h)x_j+i\omega_j(A(h)-C(h)x_j)\), which has unit modulus because the energy constraints hold. The coefficients depend on phase-independent energies, so the identical multiplier repeats each step. Taylor expansion of its principal argument gives
\[
 \arg z_j(h)=\omega_j h+\omega_j(a_*+x_j/24)h^3+o(h^3).
\]
With \(h=T/n\), accumulated phase error on mode \(j\) is \(T\omega_j(a_*+x_j/24)h^2+o(h^2)\). The two orthogonal mode contributions therefore give
\[
 \lim_{n\to\infty}h^{-2}\|q_n-e^{TK}q_0\|_2=T\Bigl(\sum_{j=1}^{2}x_jE_j(a_*+x_j/24)^2\Bigr)^{1/2}=T\mathcal C>0.
\]
The last equality is the weighted-variance identity for two points. The original unprojected RK3 local error is \(O(h^4)\), whereas the sharp projection term is of order \(h^3\).

## Verification
Run `python verification/check.py` with the packages in `verification/requirements.txt`. The checker symbolically verifies the energy polynomial, the Kutta stage combination, and the rational constant in the \(\omega_1=1\), \(\omega_2=2\), \(E_1=E_2=1\) example. It also solves the frozen-gradient projection equations at five decreasing steps and measures both the local \(h^3\) and global \(h^2\) constants. The observed terminal ratios approach \(1/(4\sqrt5)\). Finite diagnostics cannot establish the implicit-function existence, sharp optimality, or limiting orders; those follow from the arguments above.

## Relationship to prior work
Najafian and Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods* (arXiv:2409.18328v1, first posted 2024-09-26), define precisely this projected-gradient correction and provide an order-preservation theorem conditional on a limiting rank hypothesis, while noting a necessary stage-count bound. This example exhibits a singular limiting rank although the stage-count bound holds, and derives an exact rate of order loss and sharp constants not asserted by their general conditional theorem. Biswas and Ketcheson, *Multiple-Relaxation Runge-Kutta Methods for Conservative Dynamical Systems* (arXiv:2302.05235), use an alternative multi-relaxation parameterization and nonsingular rank hypotheses. Calvo and coauthors' *On the Preservation of Invariants by Explicit Runge–Kutta Methods* (DOI:10.1137/04061979X) likewise gives conditional invariant-restoring constructions, not the present singular two-frequency quasi-orthogonal asymptotics.

## Limitations
The result requires two simultaneously active **distinct-frequency** real planar oscillator modes, exactly the three-stage classical Kutta tableau, fixed-step frozen-predictor gradients, exact arithmetic and the near-predictor branch. It does not assert the same loss for other Runge–Kutta methods, differently chosen correction directions, inactive or equal-frequency modes, nonlinear ODEs, variable steps, or global selection among distant nonlinear roots. The best-knowledge literature comparison is not independent validation; specialized equivalent formulations may exist.

## References
1. A. Najafian and P. Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods*, arXiv:2409.18328v1 (2024-09-26), https://arxiv.org/html/2409.18328v1 .
2. S. Biswas and D. I. Ketcheson, *Multiple-Relaxation Runge-Kutta Methods for Conservative Dynamical Systems*, arXiv:2302.05235 (2023), https://arxiv.org/abs/2302.05235 .
3. J. I. Montijano, L. Rández, M. Calvo and others, *On the Preservation of Invariants by Explicit Runge–Kutta Methods*, SIAM Journal on Scientific Computing, DOI:10.1137/04061979X, https://doi.org/10.1137/04061979X .
