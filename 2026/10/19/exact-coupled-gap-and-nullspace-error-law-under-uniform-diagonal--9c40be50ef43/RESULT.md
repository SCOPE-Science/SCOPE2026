# Exact coupled gap and nullspace-error law under uniform diagonal splitting

## Finding
Let \(L=\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&0\end{pmatrix}\) be the edge-plus-isolate graph Laplacian, set \(A=L/\sqrt2\in\mathbb R^{3\times3}\), and let \(U,V,W\) be independent uniform random variables on \([0,1]\). Define
\[
B_\varepsilon=A^{\mathsf T}A+\varepsilon\operatorname{diag}(U,V,W),\qquad 0<\varepsilon<2.
\]
Write \(\lambda_1\le\lambda_2\le\lambda_3\) for the eigenvalues, \(G_\varepsilon=\lambda_2-\lambda_1\), and let \(Q_\varepsilon\) be any orthonormal basis for the invariant subspace of the two smallest eigenvalues. Define the **squared original-system nullspace residual**
\[
R_\varepsilon=\|A Q_\varepsilon\|_2^2.
\]
With \(T=|U-V|\) and
\[
s_\varepsilon(t)=\frac{\sqrt{1+\varepsilon^2t^2/4}-1}{\varepsilon},\quad
r_\varepsilon(t)=1-\frac1{\sqrt{1+\varepsilon^2t^2/4}},\quad
q_\varepsilon(t)=\frac14+\frac{(1-t)^2}{12}+s_\varepsilon(t)^2,
\]
the following statements hold **for every** \(0<\varepsilon<2\):

1. The exact joint description is
   \[
   R_\varepsilon=r_\varepsilon(T),\qquad
   G_\varepsilon=\varepsilon\left|W-\frac{U+V}{2}+s_\varepsilon(T)\right|,
   \qquad \mathbb E[G_\varepsilon\mid T=t]=\varepsilon q_\varepsilon(t).
   \]
   The density of \(T\) is \(2(1-t)\) on \((0,1)\). Since \(r_\varepsilon\) is strictly increasing, the conditional gap profile given the exact squared nullspace residual is also \(\varepsilon q_\varepsilon(t)\), with \(t=r_\varepsilon^{-1}(R_\varepsilon)\).
2. The conditional gap profile \(q_\varepsilon\) is strictly convex, decreases at zero, increases at one, and has **exactly one minimum** at an interior \(t_\varepsilon\in(0,1)\), characterized by
   \[
   \frac{1-t_\varepsilon}{6}=2s_\varepsilon(t_\varepsilon)s_\varepsilon'(t_\varepsilon).
   \]
   Hence the expected eigenvalue separation conditioned on increasing nullspace contamination is not monotone.
3. Despite that conditional reversal, gap and squared nullspace residual satisfy the **strict global association law**
   \[
   \boxed{\operatorname{Cov}(G_\varepsilon,R_\varepsilon)<0.}
   \]
4. In the weak-perturbation limit the association has an **exact nonzero universal correlation**:
   \[
   \operatorname{Cov}(G_\varepsilon,R_\varepsilon)
     =-\frac{\varepsilon^3}{1920}+O(\varepsilon^5),\qquad
   \boxed{\lim_{\varepsilon\downarrow0}\operatorname{Corr}(G_\varepsilon,R_\varepsilon)=-\frac3{\sqrt{805}}.}
   \]
   The weak-noise mean laws are \(\mathbb E G_\varepsilon=7\varepsilon/24+O(\varepsilon^3)\) and \(\mathbb E R_\varepsilon=\varepsilon^2/48+O(\varepsilon^4)\).

## Assumptions and scope
The matrix \(A\) is a square Gram factor of the Laplacian of the smallest graph with an edge and an isolated vertex; in particular, \(A^{\mathsf T}A=L\) and \(A\) has a two-dimensional nullspace with a non-coordinate direction. This square formulation satisfies the motivating solver's \(m\ge n\) convention. All random diagonal entries are independent continuous uniforms. The amplitude satisfies \(0<\varepsilon<\sigma_{\min,+}(A)^2=2\), so the two perturbed zero-eigenvalue branches remain the two smallest eigenvalues. All statements concern **exact eigenvectors of the perturbed matrix**, not errors from a finite-iteration Lanczos implementation. The squared residual is an operator-norm square; here its nonzero singular value also equals its Frobenius norm.

## Proof
**Diagonalization and joint law.** In the orthonormal basis \(e_+=(1,1,0)/\sqrt2\), \(e_-=(1,-1,0)/\sqrt2\), and \(e_3=(0,0,1)\), the matrix \(B_\varepsilon\) consists of an isolated eigenvalue \(\varepsilon W\) and the block
\[
\begin{pmatrix}\varepsilon M&\varepsilon(U-V)/2\\
\varepsilon(U-V)/2&2+\varepsilon M\end{pmatrix},
\qquad M=(U+V)/2.
\]
Its two eigenvalues are \(1+\varepsilon M\pm\sqrt{1+\varepsilon^2T^2/4}\). The smaller equals \(\varepsilon(M-s_\varepsilon(T))\), while the larger is at least \(2\), and the other two eigenvalues lie in \([0,\varepsilon]\). Consequently \(G_\varepsilon=\varepsilon|W-M+s_\varepsilon(T)|\). The squared sine of the angle between the smaller block eigenvector and \(e_+\) is \([1-(1+\varepsilon^2T^2/4)^{-1/2}]/2\). The isolated \(e_3\) is in \(\ker A\), while \(\|Ae_-\|_2^2=2\); this gives \(R_\varepsilon=r_\varepsilon(T)\).

**Conditional expectation.** The folded uniform difference \(T\) has density \(2(1-t)\). Conditional on \(T=t\), its midpoint \(M\) is uniform on \([t/2,1-t/2]\) and is independent of \(W\). Since
\(0\le s_\varepsilon(t)<t/2\) for \(t>0\), the shifted midpoint \(C=M-s_\varepsilon(t)\) lies in \([0,1]\). For every \(c\in[0,1]\),
\[
\mathbb E_W|W-c|=\frac14+(c-\tfrac12)^2.
\]
Taking the conditional expectation over \(M\), whose variance is \((1-t)^2/12\), proves the displayed formula for \(q_\varepsilon(t)\).

**The unique conditional reversal.** Put \(s=s_\varepsilon\). Direct differentiation gives
\[
s'(t)=\frac{\varepsilon t}{4\sqrt{1+\varepsilon^2t^2/4}},\qquad
s''(t)=\frac{\varepsilon}{4(1+\varepsilon^2t^2/4)^{3/2}}>0.
\]
Thus \(q''(t)=1/6+2(s'(t))^2+2s(t)s''(t)>0\), while \(q'(0)=-1/6\) and \(q'(1)=2s(1)s'(1)>0\). A unique interior minimizer follows, including the stated equation.

**Strict negative covariance at every admissible amplitude.** Set \(F=\mathbb E q_\varepsilon(T)\). Since
\[
s(t)=\frac{\varepsilon t^2}{4(\sqrt{1+\varepsilon^2t^2/4}+1)},\qquad
\mathbb E T^4=\frac1{15},
\]
we have \(s(t)^2\le\varepsilon^2t^4/64\). Consequently
\[
F\le\frac7{24}+\frac{\varepsilon^2}{960}
<\frac{71}{240}<\frac13=q_\varepsilon(0).
\]
Also \(s(t)\ge t^2s(1)\), so
\[
F-q_\varepsilon(1)\ge\frac1{24}-\frac{14}{15}s(1)^2.
\]
For \(0<\varepsilon<2\), \(s(1)^2<(3-2\sqrt2)/4<5/112\), and hence \(F>q_\varepsilon(1)\). Strict convexity therefore implies there is exactly one \(t_0\in(0,1)\) at which \(q_\varepsilon(t_0)=F\), with \(q_\varepsilon(t)>F\) for \(t<t_0\) and \(q_\varepsilon(t)<F\) for \(t>t_0\). As \(r_\varepsilon\) is strictly increasing,
\[
\frac{\operatorname{Cov}(G_\varepsilon,R_\varepsilon)}{\varepsilon}
=\mathbb E[(q_\varepsilon(T)-F)(r_\varepsilon(T)-r_\varepsilon(t_0))]<0,
\]
where strictness follows because \(T\) has a positive density on \((0,1)\).

**Weak-noise constant.** Uniform Taylor expansions on \([0,1]\) yield \(s_\varepsilon(t)=\varepsilon t^2/8+O(\varepsilon^3)\), \(q_\varepsilon(t)=q_0(t)+O(\varepsilon^2)\), and \(r_\varepsilon(t)=\varepsilon^2t^2/8+O(\varepsilon^4)\), with \(q_0(t)=1/4+(1-t)^2/12\). Exact triangular-density integrals give
\[
\mathbb ET^2=\frac16,\quad\mathbb ET^4=\frac1{15},\quad
\mathbb E q_0(T)=\frac7{24},\quad
\operatorname{Cov}(q_0(T),T^2)=-\frac1{240},\quad
\operatorname{Var}(T^2)=\frac7{180}.
\]
At zero noise the scaled gap tends to \(G_0=|W-M|\), with \(\mathbb E G_0^2=1/8\), hence \(\operatorname{Var}(G_0)=23/576\). Therefore
\[
\frac{\operatorname{Cov}(G_\varepsilon,R_\varepsilon)}{\varepsilon^3}
\longrightarrow-\frac1{1920},\qquad
\operatorname{Var}(R_\varepsilon/\varepsilon^2)\longrightarrow\frac7{11520},
\]
and division by the corresponding standard deviations gives \(-3/\sqrt{805}\). The error orders follow from the conditional mean formula and even analytic expansions in \(\varepsilon\).

## Verification
The standalone file `verify.py` reconstructs \(B_\varepsilon\) and its two-dimensional invariant space independently using dense symmetric eigensolvers for one thousand deterministic pseudorandom draws across five amplitudes. It compares actual eigenvalue gaps and original-system nullspace residuals with the joint formulas. It also checks conditional quadrature identities, exact rational moment constants, the limiting correlation, and strictly negative covariances at seven representative positive amplitudes. Reproduced output: `PASS 4038 assertion groups`. The analytic sign theorem and the all-amplitude assertions are proved above; a finite verifier cannot establish them.

## Relationship to prior work
Kressner and Shao, arXiv:2407.04634v1 (5 July 2024), introduce iid uniform diagonal perturbation in randomized small-block Lanczos, prove a probability bound for perturbed zero-eigenvalue separation (Theorem 4), and separately bound the approximate nullspace residual (Theorem 6). Their algorithmic and perturbation results are foundational here, not claimed as new. Meyer, Musco, and Musco, arXiv:2305.02535, establish related gap-dependent Krylov low-rank guarantees, but not this joint graph-model dependence. A separate prior exact study of a diagonally perturbed two-dimensional nullspace derives **marginal first-order level-repulsion laws** and inverse-gap moment cutoffs for general orientations; those marginal statements are expressly excluded from the present novelty claim. Neither marginal gap probabilities nor a separate residual bound determine the signed finite-amplitude gap–residual covariance or the conditional U-shaped joint profile derived above.

## Limitations
The result concerns the minimal nontrivial disconnected graph, not arbitrary matrices or arbitrary graph components. The strict sign is proved for \(0<\varepsilon<2\); no assertion is made for stronger perturbations, alternative diagonal laws, other noise correlations, or finite-precision/finite-iteration Krylov trajectories. The limiting correlation characterizes this model only. Originality remains contingent on broader specialized perturbation literature; numerical reproduction is not independent mathematical validation.

## References
1. Daniel Kressner and Nian Shao, *A randomized small-block Lanczos method for large-scale null space computations*, arXiv:2407.04634v1 (first public version, 5 July 2024), Sections 1–3; https://arxiv.org/html/2407.04634v1 .
2. Raphael A. Meyer, Cameron Musco, and Christopher Musco, *On the Unreasonable Effectiveness of Single Vector Krylov Methods for Low-Rank Approximation*, arXiv:2305.02535 (2023); https://arxiv.org/abs/2305.02535 .
3. G. W. Stewart and J.-G. Sun, *Matrix Perturbation Theory*, Academic Press, 1990 (background on invariant-subspace perturbations).
