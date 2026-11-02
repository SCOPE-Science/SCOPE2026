# Sharp redundancy penalty and online escape for volume-relaxed planar block projections

## Finding
Let \(M\ge3\), and let \(a_1,\ldots,a_M\) be pairwise nonparallel unit vectors in \(\mathbb R^2\). Consider a consistent system \(Ax=b\) with these row vectors and its unique solution \(x_\star\). Independently at every iteration, choose an unordered two-row block \(S=\{i,j\}\) uniformly among the \(\binom M2\) pairs and use the *population-normalized relaxed uniform* block-Kaczmarz update of [1], with
\[
v_{ij}=\det(A_SA_S^{\mathsf T})=\det(a_i,a_j)^2,
\qquad v_\star=\max_{i<j}v_{ij},\qquad
\omega_{ij}=1+\sqrt{1-v_{ij}/v_\star}.
\]
For any deterministic initial error \(e_0=x_0-x_\star\), the exact mean-square factor is
\[
\mathbb E\|x_k-x_\star\|_2^2=q_M(A)^k\|e_0\|_2^2,
\qquad q_M(A)=1-\frac{\sum_{i<j}v_{ij}}{\binom M2\,v_\star}.
\]
**The new sharp row-count envelope** is
\[
\boxed{0\le q_M(A)<\frac{M-2}{M-1},\qquad
\sup_{A}q_M(A)=\frac{M-2}{M-1}.}
\]
The supremum ranges over all such row configurations and is not attained. In particular the sharp three-row supremum is \(1/2\), and the worst allowable factor tends to one as the number of individually redundant rows grows. By contrast, each ordinary unrelaxed two-row block projection (uniform or volume sampled) solves the same system in one update.

For \(e_0\ne0\), let \(T=\min\{k\ge1:x_k=x_\star\}\). If \(r\) pairs attain \(v_\star\), the population-normalized algorithm has the **exact geometric hitting-time law**
\[
\Pr(T>k)=\left(1-\frac{r}{\binom M2}\right)^k,
\qquad \mathbb E T=\frac{\binom M2}{r}.
\]
The sharp near-extremal configurations below have exactly one maximizing pair, hence expected exact termination after \(\binom M2\) updates, versus one update without relaxation. If instead the normalization is the **running maximum initialized from the first sampled pair and updated before the first step**, as suggested in [1], the first relaxation is exactly one and hence \(T=1\) deterministically. Thus the precomputed and online normalizations need not be algorithmically equivalent, even though both define stable relaxation parameters.

## Assumptions and scope
All vectors are real, unit length, and pairwise nonparallel; thus every two-row block is invertible and \(v_{ij}>0\). The system \(Ax=b\) is exactly consistent, the row-pair samples are independent and uniform with replacement, and all updates use exact arithmetic. The main sharp bound applies to the *fixed global maximum* \(v_\star\), not to a changing empirical maximum. The online statement separately assumes the empirical maximum includes the current sample **before** computing its relaxation. The conventional unrelaxed block uses \(\omega=1\).

## Proof
**1. Exact scalar error recurrence.** Since any \(A_S\in\mathbb R^{2\times2}\) is invertible,
\[
A_S^{\mathsf T}(A_SA_S^{\mathsf T})^{-1}A_S=I_2.
\]
Using \(b_S=A_Sx_\star\), the relaxed update therefore reduces identically to
\[
e_{k+1}=(1-\omega_{ij})e_k=-\sqrt{1-v_{ij}/v_\star}\,e_k.
\]
After squaring and averaging the uniform choice independently of the past, \(\mathbb E[\|e_{k+1}\|^2\mid e_k]=q_M(A)\|e_k\|^2\). Iterating gives the displayed exact mean-square law. Its factor is nonnegative because each \(v_{ij}\le v_\star\).

**2. A sharp Euclidean diameter bound.** Write \(a_i=(\cos\theta_i,\sin\theta_i)\) and embed the row direction as the doubled-angle unit vector \(w_i=(\cos2\theta_i,\sin2\theta_i)\). The identity
\[
\|w_i-w_j\|_2^2=4\sin^2(\theta_i-\theta_j)=4v_{ij}
\]
translates the squared row-pair volumes into squared chord lengths. Choose \(p,q\) with \(v_{pq}=v_\star\), and let \(d^2=\|w_p-w_q\|^2=4v_\star\). The parallelogram identity gives, for every \(k\ne p,q\),
\[
\|w_k-w_p\|^2+\|w_k-w_q\|^2
=2\left\|w_k-\frac{w_p+w_q}{2}\right\|^2+\frac{d^2}{2}
\ge\frac{d^2}{2}.
\]
Keeping the endpoint pair and these \(M-2\) pairs of terms, while discarding only nonnegative remaining terms, yields
\[
\sum_{i<j}\|w_i-w_j\|^2\ge d^2+(M-2)\frac{d^2}{2}=\frac{M}{2}d^2,
\qquad\sum_{i<j}v_{ij}\ge\frac{M}{2}v_\star.
\]
Hence \(q_M(A)\le1-1/(M-1)=(M-2)/(M-1)\). For \(M\ge3\) the inequality is strict: since \(w_p,w_q\) are distinct unit vectors, their midpoint has norm strictly less than one and cannot coincide with any \(w_k\), making the displayed inequality strict for each other row.

**3. Optimality.** Fix \(M\), choose distinct bounded real constants \(c_3,\ldots,c_M\), and set
\[
\theta_1=-t,\qquad\theta_2=t,\qquad\theta_j=c_jt^2\quad(3\le j\le M),\qquad t\downarrow0.
\]
For sufficiently small positive \(t\), all rows are pairwise nonparallel and the unique maximal volume is \(v_{12}=\sin^2(2t)\). Relative to this volume, the endpoint-pair ratio tends to one, each of the \(2(M-2)\) endpoint-to-central-pair ratios tends to \(1/4\), and the central-to-central ratios tend to zero. Thus
\[
\frac{\sum_{i<j}v_{ij}}{v_\star}
\longrightarrow1+\frac{2(M-2)}4=\frac M2,
\qquad q_M(A)\longrightarrow1-\frac1{M-1}.
\]
This proves sharpness for each finite \(M\); taking \(M\to\infty\) exhibits arbitrarily slow worst-case mean-square contraction despite every selected block having full column rank.

**4. Exact termination and the online distinction.** A nonmaximizing pair has \(0<v_{ij}<v_\star\), so its scalar error multiplier is nonzero; a maximizing pair has \(\omega_{ij}=1\) and kills the error exactly. Starting from a nonzero error, the first exact solution is therefore attained exactly on the first maximizing-pair draw. Independent uniform draws give the geometric distribution and mean in the finding. The construction in step 3 has a unique maximizer, attaining the largest possible mean termination time \(\binom M2\). Any unrelaxed full-rank block has projector \(I_2\) and solves in one step. Finally, the first online draw has sampled maximum equal to its own strictly positive volume, making \(\omega=1+\sqrt{1-1}=1\); it too solves in one step.

## Verification
Run `python3 verify.py` with Python 3 standard library. The standalone script checks 1,540 exact-rational row configurations, including small-angle sharpness families for \(3\le M\le12\); verifies the doubled-angle chord identity, strict envelope, unique maximizing pairs, and 500 exact rational two-row inverses; and tests the three-row near-supremum. These are supplementary finite checks: the proof's parallelogram inequality and limiting construction establish the universal and sharp claims.

## Relationship to prior work
Entezari, Banerjee and Kalantari [1, Section 3.3, Theorem 2] introduced the precise subset-volume-dependent relaxation \(\omega=1+\sqrt{1-v/v_\star}\) and proved its general expected-progress bound. Specializing their theorem to square full-rank blocks already yields the formula \(q_M=1-\bar v/v_\star\); **that specialization alone is not claimed as new**. The contribution here is the sharp universal *row-count envelope* \((M-2)/(M-1)\), its strictness and explicit nonattained extremizers, and the exact fixed-versus-online termination contrast. Their paper does not state this sharp planar classification. The earlier volume-sampling work [2] concerns unrelaxed blocks; the earlier relaxation work [3] studies generic constant-relaxation projections. The elementary point-set squared-distance identities are standard [4]; their use in the sharp normalized-volume bound does not claim a new standalone Euclidean inequality.

## Limitations
The conclusion is for consistent planar systems with pairwise full-rank two-row blocks and globally normalized relaxation. It makes no speed claim for the authors' larger-dimensional experiments with block size below ambient dimension, noisy or inconsistent equations, inexact projectors, or arbitrary online initialization. The constructed slowdown is a *mean-square* and first-exact-hit phenomenon, not a claim of nonconvergence: for every fixed admissible matrix the error eventually becomes identically zero almost surely. The general mean-square formula and the unrelaxed one-step projection are consequences of known definitions; only the sharp row-count envelope and associated comparison are proposed as additional findings. Historical priority for equivalent formulations is not guaranteed.

## References
[1] A. Entezari, A. Banerjee, L. Kalantari, *Volume Sampling and Spectral Equalization in Randomized Alternating Projections*, arXiv:2610.12346v1, publicly posted 2026-10-08. https://arxiv.org/html/2610.12346v1

[2] A. Entezari, A. Banerjee, L. Kalantari, *Kaczmarz and Gauss-Seidel Algorithms with Volume Sampling*, arXiv:2111.06931v3. https://arxiv.org/html/2111.06931v3

[3] A. Entezari, A. Banerjee, *Global Asymptotic Rates Under Randomization: Gauss-Seidel and Kaczmarz*, arXiv:2503.09469v3. https://arxiv.org/html/2503.09469v3

[4] J. N. Copher, *Sums of Squared Distances between Points on a Unit \(n\)-Sphere*, arXiv:2001.02745. https://arxiv.org/abs/2001.02745
