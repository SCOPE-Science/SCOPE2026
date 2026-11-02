# Universal mean-square heating from nondegenerate random steps in Verlet integration

## Finding
Consider the unit-frequency oscillator \(\dot q=p\), \(\dot p=-q\), with Hamiltonian \(\mathcal H(q,p)=(q^2+p^2)/2\). Let \(H_1,H_2,\ldots\) be independent and identically distributed positive step lengths, independent of a deterministic nonzero initial vector \(z_0=(q_0,p_0)^\mathsf T\). Suppose the law of \(H_1\) has compact support inside \((0,2)\). Run velocity Störmer–Verlet at these steps.

**Sharp dichotomy.** If the step distribution is a point mass at \(h\), the whole trajectory is uniformly bounded and preserves a positive quadratic modified energy. If the step distribution is not a point mass, there exist a number \(\lambda>1\) and a positive-definite symmetric matrix \(W\), depending only on the step distribution, such that for every integer \(n\geq0\),
\[
\mathbb E[z_n^\mathsf T Wz_n]=\lambda^n z_0^\mathsf T Wz_0.
\]
Consequently \(\mathbb E\mathcal H(z_n)\) lies between positive constant multiples of \(\lambda^n\) for all \(n\). The number \(\lambda\) is the spectral radius of the exact three-dimensional second-moment operator.

**Exact two-point certificate.** If \(H\) equals \(u\) with probability \(p\in(0,1)\) and equals \(v\) otherwise, where \(0<u,v<2\), the lifted second-moment matrix \(T_{p,u,v}\) specified below satisfies
\[
\det(I_3-T_{p,u,v})=-\frac{p(1-p)}8u^2v^2(u^2-v^2)^2.
\]
In particular, any unequal pair has a real second-moment eigenvalue strictly greater than one; equality of the steps is the only mean-square bounded case in the stable interval.

**Sharp small-randomness rate.** Fix \(0<h<2\), and let \(\xi\) be a bounded real random variable with \(\mathbb E\xi=0\) and \(\operatorname{Var}(\xi)=\sigma^2>0\). For sufficiently small \(\varepsilon>0\), put \(H=h+\varepsilon\xi\). Then
\[
\lambda(h,\varepsilon)=1+\frac{\sigma^2h^4}{2(4-h^2)}\varepsilon^2+O_h(\varepsilon^3).
\]
When the law of \(\xi\) is symmetric, the remainder improves to \(O_h(\varepsilon^4)\). The coefficient is strictly positive for every \(0<h<2\). These are limits at a fixed base step \(h\).

## Assumptions and scope
The map for one velocity-Verlet step of length \(s\in(0,2)\), acting on the column vector \(z=(q,p)^\mathsf T\), is
\[
A(s)=\begin{pmatrix}a_s&s\\-s\kappa_s&a_s\end{pmatrix},\qquad
 a_s=1-s^2/2,\quad\kappa_s=1-s^2/4.
\]
Thus \(z_{n+1}=A(H_{n+1})z_n\). Step draws are independent across iterations and are not chosen adaptively from the state. Time is indexed by the number of steps, not by a fixed deterministic physical duration. The support restriction keeps every deterministic step in the strictly elliptic stability interval and the moments finite. The claim does not require an absolutely continuous step distribution.

For the exact two-point formula, the three second moments are ordered as \((\mathbb E q_n^2,\mathbb E q_np_n,\mathbb E p_n^2)^\mathsf T\). For the small-randomness expansion, \(\xi\) is bounded, its law does not depend on \(\varepsilon\), and \(h\) is fixed as \(\varepsilon\downarrow0\).

## Proof
**1. Each deterministic step is elliptic and has its own quadratic invariant.** Direct multiplication yields \(\det A(s)=1\) and \(\operatorname{tr}A(s)=2-s^2\in(-2,2)\). Therefore \(A(s)\) has no real invariant line. The positive-definite matrices
\[
P_s=\operatorname{diag}(\kappa_s^{-1},1),\qquad
D_s=\operatorname{diag}(\kappa_s,1)
\]
satisfy \(A(s)P_sA(s)^\mathsf T=P_s\) and \(A(s)^\mathsf TD_sA(s)=D_s\). Each of these positive-definite invariant forms is unique up to a positive scalar: conjugating \(A(s)\) by \(P_s^{1/2}\) gives a nontrivial planar rotation, whose invariant symmetric matrices are scalar. Thus a nonzero fixed-step orbit is bounded, and distinct \(s\)'s admit no common positive-definite invariant form of either type.

**2. Positive-definite Perron eigenmatrices.** On real symmetric \(2\times2\) matrices define \(\mathscr L(X)=\mathbb E[A(H)XA(H)^\mathsf T]\) and its trace adjoint \(\mathscr L^*(Y)=\mathbb E[A(H)^\mathsf TYA(H)]\). Both maps preserve the cone of positive-semidefinite matrices. On the compact convex set \(\mathcal K=\{X\succeq0:\operatorname{tr}X=1\}\), the continuous normalization \(X\mapsto\mathscr L(X)/\operatorname{tr}\mathscr L(X)\) has a fixed point by Brouwer's theorem. Invertibility of each \(A(s)\) ensures that the denominator is positive. If this eigenmatrix had rank one, \(\mathscr L(X)\) could have rank one in the same direction only if almost every \(A(s)\) preserved a real line, which is impossible. The eigenmatrix \(X\) is therefore positive definite. The same argument gives a positive-definite eigenmatrix \(W\) for \(\mathscr L^*\).

**3. Every nondegenerate law has strict mean-square amplification.** Each matrix \(A(s)XA(s)^\mathsf T\) has determinant \(\det X\). Strict concavity of \(\log\det\) on the positive-definite cone gives
\[
\log\det\mathscr L(X)\geq\mathbb E\log\det(A(H)XA(H)^\mathsf T)=\log\det X,
\]
with equality only if \(A(H)XA(H)^\mathsf T\) is almost surely constant. If \(\mathscr L(X)=\lambda X\), the left-hand side is \(2\log\lambda+\log\det X\), so \(\lambda\geq1\). Equality would make the common value \(X\), forcing \(X\) to be proportional to \(P_s\) for almost every sampled \(s\). As \(s\mapsto\kappa_s\) is strictly decreasing on \((0,2)\), this forces the distribution to be a point mass. Hence \(\lambda>1\) for every nondegenerate law.

Writing \(\mathscr L^*(W)=\lambda_*W\) and taking the trace pairing with \(X\) shows \(\lambda_*=\lambda\), because \(\operatorname{tr}(WX)>0\). Independence then yields \(\mathbb E[z_n^\mathsf TWz_n]=\lambda^nz_0^\mathsf TWz_0\). Comparison of the two positive quadratic forms gives the stated bounds on physical energy. The same identity bounds powers of \(\mathscr L\) on positive matrices by a multiple of \(\lambda^n\); taking differences of positive matrices extends the bound to all symmetric matrices. Since \(\lambda\) is an eigenvalue, it is the spectral radius.

**4. The exact two-point determinant.** With \(a_s=1-s^2/2\), \(b_s=s\), and \(c_s=-s(1-s^2/4)\), the second-moment lift is
\[
M(s)=\begin{pmatrix}
 a_s^2&2a_sb_s&b_s^2\\
 a_sc_s&a_s^2+b_sc_s&a_sb_s\\
 c_s^2&2a_sc_s&a_s^2
\end{pmatrix}.
\]
For the two-point law, \(T_{p,u,v}=pM(u)+(1-p)M(v)\). Expanding the three-by-three determinant and factoring yields
\[
\det(I_3-T_{p,u,v})=-p(1-p)u^2v^2(u^2-v^2)^2/8.
\]
If \(u\ne v\), this negative determinant means the real cubic \(\det(tI_3-T_{p,u,v})\) changes sign between \(t=1\) and sufficiently large positive \(t\), so it has a real zero above one. The positive-cone argument establishes the global exponential energy conclusion independently of this special calculation.

**5. A perturbative coefficient independent of the noise shape.** For deterministic \(h\), the lift \(M(h)\) has a simple eigenvalue one, since the other eigenvalues of a nontrivial planar rotation's quadratic lift are \(e^{\pm2i\theta_h}\ne1\). Right and left eigenvectors are
\[
r_h=(\kappa_h^{-1},0,1)^\mathsf T,\qquad
\ell_h=(\kappa_h,0,1)^\mathsf T,\qquad
\ell_h^\mathsf Tr_h=2.
\]
The perturbed moment operator is
\[
\mathbb E M(h+\varepsilon\xi)
=M(h)+\frac{\sigma^2\varepsilon^2}{2}M''(h)+O_h(\varepsilon^3).
\]
The polynomial entries of \(M\) give the exact identity \(\ell_h^\mathsf TM''(h)r_h=2h^4/(4-h^2)\). Simple-eigenvalue perturbation consequently gives
\[
\lambda(h,\varepsilon)-1
=\frac{\sigma^2\varepsilon^2}{2}\frac{\ell_h^\mathsf TM''(h)r_h}{\ell_h^\mathsf Tr_h}+O_h(\varepsilon^3)
=\frac{\sigma^2h^4}{2(4-h^2)}\varepsilon^2+O_h(\varepsilon^3).
\]
Symmetric noise eliminates all odd powers of \(\varepsilon\) from the moment operator and its simple eigenvalue, giving the fourth-order remainder. This proves the claims.

## Verification
The standalone standard-library program `verification/verify.py` checks the Verlet quadratic invariants, dual eigenvectors, symbolic perturbation contraction, and the factored two-point determinant with exact rational arithmetic. It also compares seven levels of full two-point sampling-history enumeration against lifted second-moment iteration, and checks the asymptotic coefficient at three base steps with independent numerical eigenvalue estimates. Run from the package root with `python3 verification/verify.py`. The program prints `VERIFY_OK` on success. Finite tests independently check algebra but do not establish the all-distributions or infinite-horizon theorem; those follow from the preceding proof.

## Relationship to prior work
Abdulle and Garegnani's 2018 RTS-RK work introduces randomized time steps and proves symplecticity and conditional finite-time energy control; its Sections 7.1–7.2 explicitly distinguish symplecticity of individual steps from global energy control. Their result imposes shrinking step randomness and a bounded-trajectory hypothesis, so it does not imply or contradict the unconditional fixed-law infinite-iteration mean-square classification here. The core Verlet update is classical and is not claimed as new.

Skeel and Gear (1992) establish an obstruction to a naive symplectic-invariant claim for variable steps, but their available abstract does not determine this random-Verlet second-moment amplification factor. Calvo and Sanz-Serna (1993) analyze deterministic variable-step symplectic schemes and long-time error for Kepler's problem, without a theorem equivalent to the present independent random-step exact covariance law in the inspected material. The general principles of positive-matrix maps, concavity of log determinant, and analytic eigenvalue perturbation are standard; the method-specific universal criterion, exact determinant, and small-noise coefficient constitute the specific result assessed here.

## Limitations
The theorem is about expected squared phase-space norm per **number of independently randomized steps**, not stability almost surely or at a fixed physical final time. No almost-sure Lyapunov exponent is claimed. Positive but extremely small randomness still gives exponential mean-square growth as the number of steps tends to infinity, potentially on an exceptionally long time scale. The small-noise expansion holds with the deterministic base step fixed and is not asserted uniformly as that step tends to zero or two. It concerns the one-degree-of-freedom harmonic oscillator, the velocity-Verlet ordering above, and exact arithmetic. Definitive publication priority remains subject to independent literature verification, especially of older variable-step and random-matrix results.

## References
1. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, first publicly posted 2018-01-04, arXiv:1801.01340; particularly Sections 7.1–7.2 and 9.7. https://arxiv.org/html/1801.01340v4
2. R. D. Skeel and C. W. Gear, *Does variable step size ruin a symplectic integrator?*, Physica D 60 (1992), 311–313. https://doi.org/10.1016/0167-2789(92)90247-K
3. M. P. Calvo and J. M. Sanz-Serna, *The development of variable-step symplectic integrators, with application to the two-body problem*, SIAM J. Sci. Comput. 14 (1993), 936–952. Author-hosted OA text: https://sanzserna.org/wp-content/uploads/1993/01/519_M.-P.-Calvo-JMSS-1.pdf
