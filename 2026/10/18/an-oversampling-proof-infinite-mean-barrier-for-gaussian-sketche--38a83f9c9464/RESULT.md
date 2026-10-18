# An oversampling-proof infinite-mean barrier for Gaussian-sketched Krylov Galerkin projections

## Finding

**Theorem (universal finite-sketch moment barrier and minimal-residual contrast).** Let \(A\in\mathbb R^{d\times d}\) be symmetric positive definite, let \(r\in\mathbb R^d\) be a unit vector, and let the Krylov grade of \((A,r)\) exceed \(k\ge1\). Let \(V_k\) be the \(d\times k\) orthonormal Lanczos basis of \(\mathcal K_k(A,r)\), with first column \(r\). For **every finite integer** \(s\ge k\), draw \(S\in\mathbb R^{s\times d}\) with independent standard Gaussian entries, independently of \(A,r\). Let \(x_*=A^{-1}r\), and define the two sketched approximants

\[
 x_F\in\mathcal K_k(A,r),\quad (SV_k)^\top S(r-Ax_F)=0,
\qquad
 x_M=\mathop{\mathrm{argmin}}_{x\in\mathcal K_k(A,r)}\|S(r-Ax)\|_2.
\]

Both are uniquely defined with probability one. Write \(\nu=s-k+1\) and \(E_F=\|x_*-x_F\|_A\), \(E_M=\|x_*-x_M\|_A\), where \(\|y\|_A=\sqrt{y^\top Ay}\). Then

\[
 \mathbb E E_F^p<\infty\quad\Longleftrightarrow\quad 0<p<1,
 \qquad
 \mathbb E E_M^p<\infty\quad\Longleftrightarrow\quad 0<p<\nu.
\]

Moreover, the exact positive Galerkin tail constant exists:

\[
 \lim_{T\to\infty}T\,\mathbb P(E_F>T)
 = 2|\gamma|\int_{\{g:w^\top g<0\}}
 \sqrt{g^\top H^{-1}g}\,\phi_k(g)\,f_\nu(-w^\top g)\,dg
 \in (0,\infty),
\]

where \(H=V_k^\top AV_k\), \(\beta>0\) is the next Lanczos subdiagonal, \(\gamma=\beta\,e_k^\top H^{-1}e_1\ne0\), \(w=\beta H^{-1}e_k\), \(\phi_k\) is the standard \(k\)-variate Gaussian density, and \(f_\nu(t)=2^{1-\nu/2}t^{\nu-1}e^{-t^2/2}/\Gamma(\nu/2)\) for \(t>0\) is the chi density with \(\nu\) degrees of freedom. In contrast, \(\mathbb P(E_M>T)\) has exact polynomial order \(T^{-\nu}\). Thus arbitrary finite Gaussian oversampling never gives the unsafeguarded sketched Galerkin approximation a finite mean absolute energy error, whereas sketched minimal residual has finite second moment whenever \(s\ge k+2\).

## Assumptions and scope

The sketch is Gaussian, drawn once and reused for the two projections; the assertions are unconditional over that sketch. The problem is exact-arithmetic, real symmetric positive definite, and the Krylov subspace is **not yet invariant under** \(A\) (its grade exceeds \(k\)). In particular \(r\notin A\mathcal K_k(A,r)\). The approximation space itself is fixed independently of \(S\); the result is not a statement about adaptively sketched basis generation, finite-precision safeguards, or later iterations of a stochastic algorithm. Any common nonzero scaling of \(S\) gives the same iterates. For a terminated Lanczos process with grade at most \(k\), the exact solution already belongs to the space and both methods instead recover it almost surely.

## Proof

**1. Lanczos reduction.** The three-term recurrence at the final basis vector gives

\[
 AV_k=V_kH+\beta v_{k+1}e_k^\top,
 \qquad H=V_k^\top AV_k>0,\quad\beta>0,
\]

with \(v_{k+1}\) a unit vector orthogonal to the columns of \(V_k\). Every subdiagonal of the real symmetric tridiagonal matrix \(H\) is strictly positive. Consequently \(e_k^\top H^{-1}e_1\ne0\): its numerator as a cofactor is the signed product of the first \(k-1\) Lanczos subdiagonals (the empty product is \(1\) when \(k=1\)), whereas \(\det H>0\).

Set \(U=SV_k\in\mathbb R^{s\times k}\), \(h=Sv_{k+1}\in\mathbb R^s\). They are independent matrices/vectors of independent standard Gaussians. Because \(s\ge k\), \(U\) has full column rank almost surely. Define

\[
 z=(U^\top U)^{-1}U^\top h,
 \qquad H_S=H+\beta z e_k^\top.
\]

The sketched Galerkin equation reduces exactly to \(H_S y=e_1\) with \(x_F=V_ky\). As shown below, \(H_S\) is invertible almost surely.

**2. Spherical Student law.** Conditioning on \(U\), \(z\) is Gaussian with covariance \((U^\top U)^{-1}\). The Gram matrix is Wishart with \(s\) degrees of freedom. Integrating its density with the conditional Gaussian density and using the rank-one determinant identity gives

\[
 f_z(z)=\frac{\Gamma((s+1)/2)}{\pi^{k/2}\Gamma((s-k+1)/2)}
 (1+\|z\|_2^2)^{-(s+1)/2}.
\]

Equivalently, in distribution,

\[
 z=G/R,\quad G\sim N_k(0,I),\quad R\sim\chi_{\nu},
 \qquad\nu=s-k+1,
\]

where \(G\) and \(R\) are independent. The law has full positive density on \(\mathbb R^k\). Thus the determinant identity

\[
 \det H_S=\det H\,(1+\beta e_k^\top H^{-1}z)
\]

shows that \(H_S\) is singular with probability zero, but its determinant can lie arbitrarily close to zero with positive probability.

**3. A universal simple pole.** Put \(a=H^{-1}e_1\), \(w=\beta H^{-1}e_k\), and \(\gamma=\beta e_k^\top a\ne0\). Sherman–Morrison yields the **exact** coefficient formula

\[
 y=a-\frac{\gamma H^{-1}z}{1+w^\top z}
   =a-\frac{\gamma H^{-1}G}{R+w^\top G}.
\]

Writing \(L=R+w^\top G\) and \(v=x_*-V_ka\), the energy error satisfies

\[
 E_F=\left\|v+\gamma V_kH^{-1}G/L\right\|_A,
 \qquad \|V_kH^{-1}G\|_A=\sqrt{G^\top H^{-1}G}.
\]

Conditional on \(G=g\), the variable \(L\) is a translate of the independent chi variable \(R\), so its density at zero is \(f_\nu(-w^\top g)\) on the half-space \(w^\top g<0\) and zero otherwise. Integration over a shrinking interval about this simple pole gives the stated tail constant. More explicitly, on fixing \(g\) in the strict half-space, the large-error event is asymptotically \(|L|<|\gamma|\sqrt{g^\top H^{-1}g}/T\), of width \(2|\gamma|\sqrt{g^\top H^{-1}g}/T\). Integration over \(g\) is justified by Gaussian decay, the chi density's exponential decay and at most polynomial growth, splitting away a Gaussian-small large-\(\|g\|\) region; these bounds also control the fixed vector \(v\). The integral is finite, since \(f_\nu(t)\) is bounded by a polynomial times a Gaussian, and strictly positive because \(w\ne0\), \(\gamma\ne0\), and the half-space has positive Gaussian measure.

The \(1/T\) tail implies \(\mathbb E E_F^p=\infty\) for all \(p\ge1\) by the layer-cake identity. For \(0<p<1\), the conditional Gaussian/chi representation makes \(\mathbb E \|G\|^p/|R+w^\top G|^p<\infty\): locally around the simple pole, \(|L|^{-p}\) is integrable; away from it, Gaussian and chi tails make the remaining integral finite. The triangle inequality then gives finite \(\mathbb E E_F^p\).

**4. The minimal-residual contrast.** Let \(B=AV_k\) (full column rank) and let \(P_B\) be its Euclidean orthogonal projector. Since the Lanczos grade exceeds \(k\), \(\delta=\|(I-P_B)r\|_2>0\); otherwise \(A^{-1}r\in\mathcal K_k(A,r)\) and the process has terminated. Put \(y_0=(B^\top B)^{-1}B^\top r\), and write the thin QR factorization \(B=QR_B\). The Gaussian sketch makes \(SQ\) independent of \(S(I-P_B)r/\delta\). The sketched least-squares normal equations therefore give

\[
 y_M=y_0+\delta R_B^{-1} Z,
 \qquad Z=G'/R',
\]

where \(G'\sim N_k(0,I)\), \(R'\sim\chi_\nu\) independently. The exact \(k\)-variate Student tail law has finite norm moments exactly for \(p<\nu\) and a two-sided norm tail of order \(T^{-\nu}\). Because \(\delta>0\) and \(R_B\) is invertible, and because the \(A\)-norm of \(x_*-V_ky_M\) differs from a fixed affine translation of an invertible image of \(Z\) only by an equivalent finite-dimensional norm, these thresholds and tail orders transfer to \(E_M\). This proves all assertions.

## Verification

The accompanying `check.py` computes both projections directly from finite exact-rational Gaussian-surrogate sketch matrices and checks their defining equations and moment-relevant normalizations. It also independently integrates the exact one-step chi/Student tail formulas using a numerical Student CDF. The verification is a diagnostic on the **formulas**, not a probabilistic proof of their asymptotics. The core universal result is established by the analytic Lanczos/Wishart/pole argument above. Run `python check.py` with the dependencies in `requirements.txt`.

## Relationship to prior work

Balabanov and Nouy's randomized Galerkin theory (2018, arXiv:1803.02602), and Balabanov and Grigori's randomized FOM/GMRES definitions (2021, arXiv:2111.14641, Section 4.3), provide high-probability geometric control and the sketched Galerkin and least-squares formulations. Güttel and Schweitzer (2022, arXiv:2208.11447, Sections 2 and 5) establish sketched FOM interpolation and document Ritz-value instability, while Timsit, Grigori and Balabanov (2023, arXiv:2302.07466, Section 5.1) report spiking errors and near-zero randomized Ritz values. These phenomena motivate, but do not state, an unconditional **all-Krylov-dimensions** infinite-mean law at every finite Gaussian sketch size. Ahfock, Astle and Richardson (2017, arXiv:1706.03665) and Browne and Andrews (2023, arXiv:2306.03593) already establish Gaussian-sketch least-squares Student distributions; that **known** result accounts for the minimal-residual comparison. The added Galerkin assertion instead uses the irreducible Lanczos coupling and an inverse rank-one matrix pole to deduce the universal first-moment failure. The generic Student and matrix-inversion ingredients are classical and are not claimed to be novel individually.

## Limitations

The theorem concerns fixed iteration \(k\) and unconditional sketch randomness, not accuracy conditional on a successful subspace embedding, not median behavior, and not the long-run behavior of practical guarded Krylov solvers. It does not claim that sketched Galerkin typically diverges; its infinite expectation is caused by arbitrarily rare near-singular reduced systems. It does not extend without analysis to discrete or structured sketches, adaptive sketch rejection, exact-arithmetic stopping at the Krylov grade, or non-symmetric/non-positive matrices. The precise leading constant is an integral rather than a simple closed form for general \(k\). Prior general Gaussian least-squares distribution results cover the minimal-residual half of the comparison and supply an ingredient in the Galerkin derivation.

## References

1. O. Balabanov and A. Nouy, *Randomized linear algebra for model reduction. Part I: Galerkin methods and error estimation* (first public 2018-03-07), arXiv:1803.02602, https://arxiv.org/abs/1803.02602.
2. O. Balabanov and L. Grigori, *Randomized block Gram-Schmidt process for the solution of linear systems and eigenvalue problems* (first public 2021-11-29), arXiv:2111.14641, https://arxiv.org/abs/2111.14641.
3. S. Güttel and M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions* (first public 2022-08-24), arXiv:2208.11447, https://arxiv.org/abs/2208.11447.
4. E. Timsit, L. Grigori and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers* (first public 2023-02-15), arXiv:2302.07466, https://arxiv.org/abs/2302.07466.
5. D. Ahfock, W. Astle and S. Richardson, *Statistical properties of sketching algorithms* (first public 2017-06-12), arXiv:1706.03665, https://arxiv.org/abs/1706.03665.
6. R. Browne and J. Andrews, *Statistical inference for sketching algorithms* (first public 2023-06-06), arXiv:2306.03593, https://arxiv.org/abs/2306.03593.
