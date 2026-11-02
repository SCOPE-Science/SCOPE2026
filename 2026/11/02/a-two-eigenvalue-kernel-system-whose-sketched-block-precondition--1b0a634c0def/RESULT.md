# A two-eigenvalue kernel system whose sketched block preconditioner requires arbitrarily many exact CG steps

## Finding
For every integer \(q\ge2\), an exact full-Nyström kernel-ridge normal equation can have only two eigenvalues, independent of \(q\), while the prescribed equal-block BLOKS preconditioner produces exactly \(q+1\) distinct eigenvalues. There is an explicit common right-hand side for which zero-start conjugate gradients (CG) needs exactly two iterations before preconditioning and exactly \(q+1\) iterations afterward, in exact arithmetic. An isospectral kernel matrix with homogeneous block orientation has only three preconditioned eigenvalues. Thus the blockwise orientation, rather than the original system's condition number or rank-one eigenvalue pattern, controls the exact Krylov polynomial degree.

## Assumptions and scope
Let \(q\) be any integer at least \(2\). Set \(n=m=2q\), block size \(m_0=2\), number of equal contiguous blocks \(q\), and ridge coefficient \(\lambda=1/(2q)\). Choose all \(m\) training points as Nyström landmarks, so \(K_{nm}=K_{mm}=K\) and the normal equation is
\[
H=K^2+\lambda nK=K^2+K.
\]
Define \(S_q=\sum_{r=1}^q r^2\), \(t_j=j/\sqrt{S_q}\), and \(u\in\mathbb R^{2q}\) by \(u_{2j-1}=t_j\), \(u_{2j}=0\). The positive-definite Gram matrix is \(K=I_{2q}+uu^{\mathsf T}\). Any SPD finite Gram matrix is realized by an appropriate finite feature map, so this is a legitimate exact kernel instance. With \(K_j\) the diagonal \(2\times2\) principal kernel block, use the equal-size block-sketch preconditioner from the BLOKS construction [1]:
\[
 B=\operatorname{diag}_{j=1}^q\bigl(q^2K_j^2+qK_j\bigr),\qquad M=B^{-1}.
\]
The source's formula \((nq/m_0)K_j^2+\lambda nqK_j\) reduces exactly to this expression with the parameters above. Conjugate gradients is applied with the SPD preconditioner \(M=B^{-1}\), equivalently to \(C=B^{-1/2}HB^{-1/2}\). Set the linear-system right-hand side \(b=e_1+e_2\) and the initial iterate to zero. All algebra and iteration counts use exact arithmetic and exact termination.

## Proof
**Unpreconditioned spectrum and Krylov grade.** Since \(\|u\|_2=1\), the rank-one projector identity gives \(K^2=I+3uu^{\mathsf T}\) and hence \(H=2I+4uu^{\mathsf T}\). Its eigenvalues are \(6\), once, and \(2\), with multiplicity \(2q-1\). The projection of \(b=e_1+e_2\) onto \(u\) is nonzero because \(t_1>0\), and the projection onto \(u^\perp\) is nonzero because of \(e_2\). The zero-start CG grade is thus exactly \(2\).

**Block factors.** Put \(s_j=t_j^2=j^2/S_q\); the values are positive, strictly increasing and sum to one. For block \(j\),
\[
K_j=\operatorname{diag}(1+s_j,1),\quad
B_j=\operatorname{diag}(\beta_j,\beta_0),\quad
\beta_j=q(1+s_j)[q(1+s_j)+1],\quad
\beta_0=q(q+1).
\]
In the coordinate order that groups odd coordinates first, \(C\) splits as the direct sum of the scalar \(\eta_0=2/\beta_0\) with multiplicity \(q\), and an active \(q\times q\) matrix
\[
C_a=\operatorname{diag}(d_1,\ldots,d_q)+4vv^{\mathsf T},\quad
d_j=2/\beta_j,\quad v_j=t_j/\sqrt{\beta_j}>0.
\]
The \(d_j\)'s are positive and distinct, and all are strictly below \(\eta_0\).

**All active eigenvalues are distinct.** The positive rank-one secular equation is
\[
F(z)=1-4\sum_{j=1}^q\frac{v_j^2}{z-d_j}=0.
\]
Because the \(d_j\)'s are strictly ordered and each \(v_j>0\), standard pole/sign analysis shows one simple root between every consecutive ordered pair of poles and one simple root above the largest pole; there are exactly \(q\) distinct active roots, none at a pole. To exclude coincidence with the inactive eigenvalue, direct substitution and cancellation yield
\[
F(\eta_0)=1-2(q+1)\sum_{j=1}^q\frac{1}{q(2+s_j)+1}.
\]
The function \(x\mapsto[2q+1+qx]^{-1}\) is convex on positive inputs; Jensen's inequality and \(q^{-1}\sum_js_j=1/q\) give
\[
\sum_{j=1}^q\frac1{2q+1+qs_j}\ge\frac{q}{2(q+1)}.
\]
Therefore \(F(\eta_0)\le1-q<0\); in particular \(\eta_0\) is not an active eigenvalue. The preconditioned matrix has exactly \(q+1\) distinct eigenvalues. This is the maximal possible number for this rank-one, two-coordinate-per-block construction, because all even coordinates share one scalar eigenvalue.

**Exact preconditioned CG grade.** The right-hand side in symmetric coordinates is \(B^{-1/2}b\). Its even-coordinate component is nonzero, giving positive projection onto the \(\eta_0\) eigenspace. For every eigenvector \(x\) of \(C_a\) with eigenvalue \(z\), the rank-one equation gives \((z-d_j)x_j=4v_j(v^{\mathsf T}x)\). No nonzero eigenvector can have \(v^{\mathsf T}x=0\), since \(z\) is distinct from all \(d_j\), and hence every \(x_j\ne0\). In particular its first active component is nonzero. The active portion of \(B^{-1/2}b\) is a nonzero multiple of that first coordinate vector, so it has nonzero projection onto each of the \(q\) simple active eigenspaces. Consequently all \(q+1\) spectral factors are present in the minimal polynomial for this right-hand side. Exact PCG terminates first at iteration \(q+1\).

**Isospectral homogeneous comparison.** Now instead choose \(u_{2j-1}=1/\sqrt q\), \(u_{2j}=0\), retaining \(K=I+uu^{\mathsf T}\), blocks, and parameters. Both unpreconditioned \(K\) and \(H\) have exactly the same eigenvalues as above. All active preconditioning factors equal \(\beta_1=(q+1)(q+2)\), while the inactive factor remains \(\beta_0=q(q+1)\). The complete preconditioned spectrum is
\[
\frac{2}{(q+1)(q+2)}\quad(q-1\text{ times}),\qquad
\frac{2}{q(q+1)}\quad(q\text{ times}),\qquad
\frac{6}{(q+1)(q+2)}\quad(1\text{ time}).
\]
For \(q\ge2\), these levels are strictly ordered as written. Their condition number is exactly \(3\). This establishes orientation-dependent spectral complexity at identical original spectra.

## Verification
The standalone file `verify.py` uses exact SymPy rational matrices to check the spectrum and Krylov-rank identities for \(2\le q\le7\), and implements exact-arithmetic (preconditioned and unpreconditioned) CG for \(2\le q\le5\). It checks the Jensen-derived exclusion inequality exactly for these cases and the homogeneous companion eigenvalues. These finite computations are **not** the proof for arbitrary \(q\): the universal theorem follows from the projector, secular equation, Jensen, and Krylov-grade arguments above. Run `python verify.py` with SymPy installed.

## Relationship to prior work
Vitale, Meanti, Rando, Ayuso de Dios, and Rosasco [1] introduce the sketched block preconditioner used *without alteration* in the equal-block full-data specialization here. Their material inspected in Sections 2–4 defines the normal equations, block sketch and PCG method, discusses cost/conditioning, and presents computational tests; it does not state this exact family-dependent Krylov-degree classification. Demmel [2] studies near-optimal conditioning of general block-Jacobi preconditioning; neither its abstract nor the source equations directly imply the Krylov-degree separation here. General rank-one spectral secular identities and Krylov termination theorems are classical ingredients, not claimed as new. This theorem's candidate contribution is their **exact model-specific synthesis** for the published block-sketch prescription, including the two-iteration versus \(q+1\)-iteration right-hand-side separation and the isospectral homogeneous comparison.

## Limitations
This is an exact-arithmetic, full-landmark Nyström benchmark with deliberately heterogeneous block leverage. It does not imply that random sketched subblocks, finite precision, finite residual tolerances, or practical large-data runs exhibit worse wall-clock performance. A preconditioned system can require more exact steps yet converge rapidly to a chosen tolerance. It is not a universal lower bound for all preconditioners or block orders. The motivating preprint's appendices and certain older specialized block-conditioning papers were not fully inspected; unrecognized general coverage remains a historical-priority risk. Independent mathematical audit has not been performed.

## References
1. F. Vitale, G. Meanti, L. Rando, B. Ayuso de Dios, and L. Rosasco, *BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning*, arXiv:2610.13382v1 (first public 2026-10-09), https://arxiv.org/abs/2610.13382 .
2. J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 408–413, DOI:10.1137/22M1504901.
3. L. Yu. Kolotilina, *Optimally conditioned block matrices*, Linear Algebra and its Applications 340 (2002), 55–67, DOI:10.1016/S0024-3795(01)00412-8. (Abstract compared; full paper was not read.)
