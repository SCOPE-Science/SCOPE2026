# A global-coherence barrier and an extra Krylov step for sketched block kernel preconditioning

## Finding

Consider the sketched block-Jacobi inverse preconditioner defined in equation (12)–(13) of Vitale et al., *BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning* (arXiv:2610.13382v1). For a positive equicorrelation kernel, **every partition into at least two equal blocks leaves the spectral condition number of the kernel-ridge normal matrix exactly unchanged**. When the blocks contain at least two coordinates, the preconditioner additionally creates a third distinct spectral value and, for generic data, increases exact-arithmetic conjugate-gradient termination from two iterations to three.

The statement is quantified over all integers \(n\ge m\ge2\), all integers \(s\ge1\) with \(s\mid m\) and \(q=m/s\ge2\), every correlation \(0<\rho<1\), and every ridge parameter \(\lambda>0\). It includes the genuinely Nyström-restricted case \(m<n\), not only full kernel ridge regression.

Let \(\delta=1-\rho\) and \(K_n=\delta I_n+\rho\mathbf 1_n\mathbf 1_n^{\mathsf T}\). Choose any \(m\) kernel centers (reordering them as the first \(m\)); write \(C=K_n[:,1{:}m]\) and \(K_m=K_n[1{:}m,1{:}m]\). Set
\[
H=C^{\mathsf T}C+\lambda nK_m.
\]
For each of the \(q\) disjoint blocks of size \(s\), form
\[
T_j=\frac{nq}{s}K_s^2+\lambda nqK_s,
\qquad K_s=\delta I_s+\rho\mathbf1_s\mathbf1_s^{\mathsf T},
\qquad P=\operatorname{diag}(T_1,\ldots,T_q).
\]
The algorithm applies the inverse preconditioner \(P^{-1}\). Define the four positive scalars
\[
\begin{aligned}
h_0&=\delta(\delta+\lambda n),\\
h_1&=h_0+m\rho(2\delta+n(\rho+\lambda)),\\
t_0&=\frac{nq}{s}\delta(\delta+\lambda s),\\
t_1&=\frac{nq}{s}(\delta+s\rho)(\delta+s\rho+\lambda s).
\end{aligned}
\]
If \(s\ge2\), the complete spectrum of \(P^{-1/2}HP^{-1/2}\) is
\[
\boxed{
\left\{\frac{h_0}{t_1}\ (q-1\text{ times}),\quad
\frac{h_0}{t_0}\ (m-q\text{ times}),\quad
\frac{h_1}{t_1}\ (1\text{ time})\right\},
}
\]
with strictly increasing displayed values. If \(s=1\), the absent middle family is omitted. In both cases,
\[
\boxed{\kappa_2(P^{-1/2}HP^{-1/2})=\frac{h_1}{h_0}=\kappa_2(H).}
\]
Indeed, \(h_1/h_0\) is a lower bound for **every** positive-definite block-diagonal preconditioner having the same equal-block partition (not only this particular formula). The bare optimal-block-scaling observation is not claimed as independent new theory; the algorithm-specific spectral identity and its Krylov consequence are the assessed finding.

For \(s\ge2\) and \(q\ge2\), ordinary CG on \(Hx=b\) terminates in at most two exact iterations, while this particular preconditioned CG requires exactly three for every right-hand side with nonzero components in each of its three invariant eigenspaces. Such right-hand sides arise from actual response vectors because \(C\) has full column rank. When \(s=1\), the preconditioner is a scalar multiple of the identity and retains two spectral values. In the separate full-block case \(m=n=s\), the block approximation is exactly \(H\), giving one-step preconditioned CG; splitting into \(q\ge2\) blocks loses that perfect conditioning.

## Assumptions and scope

The kernel matrix is real symmetric positive definite with unit diagonal and constant off-diagonal correlation \(0<\rho<1\). This is not an artificial indefinite matrix: Gaussian radial-basis kernels applied to vertices of a regular simplex produce exactly this matrix for a suitable bandwidth. All formulas refer to the normal matrix of Nyström kernel ridge regression and the precise sketched block construction in arXiv:2610.13382v1, with exact block solves and exact arithmetic. The number of centers is \(m\), the number of observations is \(n\), and each block has size \(s\). A 'condition number' means the ratio of the largest to smallest eigenvalues of the symmetric preconditioned SPD operator; it is **not** the Euclidean condition number of the nonsymmetric left-product \(P^{-1}H\) in an unrelated norm.

## Proof

**Step 1: exact normal matrix.** Let \(E\) consist of the first \(m\) columns of \(I_n\). Since \(C=\delta E+\rho\mathbf1_n\mathbf1_m^{\mathsf T}\), direct multiplication gives
\[
C^{\mathsf T}C=\delta^2 I_m+(2\delta\rho+n\rho^2)\mathbf1_m\mathbf1_m^{\mathsf T}.
\]
Adding \(\lambda nK_m\) yields
\[
H=h_0I_m+\rho(2\delta+n(\rho+\lambda))\mathbf1_m\mathbf1_m^{\mathsf T}.
\]
The constant-vector eigenvalue is \(h_1\); its orthogonal complement has eigenvalue \(h_0\). These are distinct because \(\rho>0\).

**Step 2: three orthogonal eigenspaces.** Within a block, \(K_s\) acts by \(\delta\) on vectors with zero coordinate sum and by \(\delta+s\rho\) on the all-ones vector. Accordingly, \(T_j\) acts by \(t_0\) and \(t_1\) on these two subspaces. Decompose \(\mathbb R^m\) orthogonally as: (a) zero-sum vectors within each block, of total dimension \(m-q\); (b) vectors constant within each block but with total sum zero, of dimension \(q-1\); and (c) the span of \(\mathbf1_m\). On (a) the pair \((H,P)\) has generalized eigenvalue \(h_0/t_0\); on (b), \(h_0/t_1\); on (c), \(h_1/t_1\). These subspaces exhaust the domain, proving the spectrum and multiplicities.

**Step 3: strict ordering.** As \(\rho>0\), clearly \(t_1>t_0\), hence \(h_0/t_1<h_0/t_0\). It remains to show \(h_1/h_0>t_1/t_0\). After subtracting one from each ratio and cancelling \(\rho/\delta>0\), this becomes
\[
\frac{m(2\delta+n(\rho+\lambda))}{\delta+\lambda n}>
\frac{s(2\delta+s(\rho+\lambda))}{\delta+\lambda s}.
\]
Because \(m=qs\ge2s\), it suffices to replace \(m\) on the left by \(2s\). Multiplication by the positive denominators then reduces the difference to
\[
\begin{aligned}
&2(2\delta+n(\rho+\lambda))(\delta+\lambda s)
 -(2\delta+s(\rho+\lambda))(\delta+\lambda n)\\
&\quad=2\delta^2+3s\delta(\rho+\lambda)
 +2s^2\lambda(\rho+\lambda)
 +(n-2s)\bigl[s\lambda(\rho+\lambda)+2\delta\rho\bigr]>0.
\end{aligned}
\]
All summands are nonnegative, and the first is positive, as \(n\ge m\ge2s\). Thus the displayed three eigenvalues are strictly ordered when \(s\ge2\). Their maximum/minimum ratio is \((h_1/t_1)/(h_0/t_1)=h_1/h_0\). For \(s=1\), \(t_1\) is common to both eigenspaces and the same condition-number identity holds.

**Step 4: block-local impossibility.** Take any real SPD block-diagonal \(Q\) with the same \(q\ge2\) equal blocks, without assuming its blocks are equal. Put \(u=\mathbf1_m\), let \(\zeta=\exp(2\pi i/q)\), and let the entries of \(v\) on block \(j\) all equal \(\zeta^j\). The root-of-unity sum vanishes, so \(Hu=h_1u\) and \(Hv=h_0v\), whereas \(\|u\|_2^2=\|v\|_2^2=m\). Critically, because \(Q\) is block diagonal and all block phases have modulus one,
\[
u^{\mathsf T}Qu=v^*Qv>0.
\]
The generalized Rayleigh quotient on \(u\) is \(h_1m/(u^{\mathsf T}Qu)\), and on \(v\) it is \(h_0m/(v^*Qv)\). The spectral extremes of \(Q^{-1/2}HQ^{-1/2}\) bracket these two quotients, so its condition number is at least \(h_1/h_0\). Complex test vectors are legitimate for the complexification of a real SPD generalized eigenproblem, with the same extreme eigenvalues. Equality is attainable by \(Q=I_m\), as well as by the specified block approximation. This proves a structural global-coherence obstruction without any claim that it is new independent of the classical optimal block-scaling literature.

**Step 5: the Krylov-step consequence.** A real SPD matrix with exactly \(d\) distinct eigenvalues is annihilated by a degree-\(d\) residual polynomial, and for a right-hand side projecting nontrivially into every eigenspace no lower degree polynomial with constant coefficient one can annihilate all components. Hence CG from zero takes exactly \(d\) steps for such a right-hand side. Here \(H\) has two distinct eigenvalues, while the split preconditioned operator has three distinct eigenvalues for \(s\ge2\). Since \(K_m\) is nonsingular and occupies the first \(m\) rows of \(C\), the map \(y\mapsto C^{\mathsf T}y\) is surjective, so generic right-hand sides are realized by kernel ridge regression response vectors. When \(s=1\), the inner-block eigenspace is zero-dimensional and no third value occurs. When \(m=n=s\), the single block equals the entire system and \(P=H\).

**Exact representative example.** Take \(n=8\), \(m=4\), \(s=2\), \(\rho=3/5\), and \(\lambda=1/10\). Then \(h_0=12/25\), \(h_1=396/25\), and the preconditioned eigenvalues are \(1/48\) once, \(1/4\) twice, and \(11/16\) once. The unpreconditioned and preconditioned spectral condition numbers are both \(33\). For the right-hand side \(b=(1,2,3,4)^{\mathsf T}\), exact-rational CG stops in two iterations without preconditioning and three iterations with the stated block inverse.

## Verification

Run `python verify.py` in a Python environment with NumPy and SymPy installed. The program reconstructs the full equicorrelation Gram matrix, the actual sketched block matrices, and their symmetric generalized spectra for 1,392 finite parameter combinations, checks one exact-rational four-dimensional spectrum, and performs exact-rational CG on the representative example. It verifies the claimed two-versus-three termination counts. These computations test the formulas but do not replace Steps 1–5, which prove the infinite-parameter statement.

## Relationship to prior work

Vitale et al. (2026, arXiv:2610.13382v1) define the sketched block preconditioner and evaluate large-scale kernel learning empirically; equations (7), (12), and (13), plus Appendices B–C, are the direct method specification. The source does not state the equicorrelation spectral identity or its exact-CG consequence in the inspected full-text sections. Classical optimal block-scaling work by Shapiro (1985), Kolotilina (2002), and Demmel (2023) addresses the general optimization of block-diagonal conditioning and may subsume the *abstract* block-local lower bound in Step 4; novelty is not claimed for that lemma in isolation. Southworth and Olivier (2020) analyze broad two-block preconditioner spectra and Krylov termination, but their stated block operators and hypotheses do not specify this 2026 sketched kernel construction or the all-block-size formulas. The assessed contribution is the exact, algorithm-specific three-value spectral profile, all-parameter condition-number equality, and one-extra-CG-step example on legitimate normalized kernel data. Bibliographic overlap through older general frameworks remains a residual risk.

## Limitations

The calculation applies to exact Gaussian-RBF-realizable equicorrelation matrices, uniform center blocks, the specified positive ridge parameter, and exact linear algebra. It is an obstruction example, **not** a proof that the method is unhelpful on typical heterogeneous kernels or that practical floating-point PCG always uses more iterations. The condition number alone need not predict iteration counts; indeed both systems here have only a few distinct eigenvalues. General block-local optimality is a supporting older-type fact rather than a claim of independent discovery. No claim about statistical test error, memory traffic, or approximation quality is made.

## References

1. G. Vitale, G. Meanti, M. Rando, B. Ayuso de Dios, L. Rosasco, *BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning*, arXiv:2610.13382v1, first submitted 2026-10-09, https://arxiv.org/html/2610.13382.
2. A. Shapiro, *Optimal Block Diagonal \(\ell_2\)-Scaling of Matrices*, SIAM Journal on Numerical Analysis 22 (1985), 81–94, https://doi.org/10.1137/0722005.
3. L. Yu. Kolotilina, *Optimally conditioned block matrices*, Linear Algebra and its Applications 340 (2002), 55–67, https://doi.org/10.1016/S0024-3795(01)00412-8.
4. J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 408–413, https://doi.org/10.1137/22M1504901.
5. B. S. Southworth and S. A. Olivier, *A note on \(2\times2\) block-diagonal preconditioning*, arXiv:2001.00711v1 (2020), https://arxiv.org/abs/2001.00711.
