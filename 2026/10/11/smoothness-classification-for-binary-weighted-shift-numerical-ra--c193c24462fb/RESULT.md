# Smoothness classification for binary weighted-shift numerical-radius norms
## Finding
Let \(a=(a_n)_{n\ge 1}\) be any binary sequence, \(a_n\in\{0,1\}\), and let \(T_a e_n=a_ne_{n+1}\) be its forward weighted shift on complex \(\ell_2(\mathbb N)\). Equip the complex sequence space \(\ell_\infty(\mathbb N)\), regarded as a **real** Banach space, with the norm \(N(a)=w(T_a)\), where \(w\) is the numerical radius. A *run* is a maximal consecutive set of coordinates with value one; an infinite run is allowed. Let \(m\) be the largest finite run length if a largest length exists.

The numerical radius at every binary sequence is
\[
N(a)=\begin{cases}
0,&a=0,\\
\cos\bigl(\pi/(m+2)\bigr),&\text{the maximal run length }m\text{ is finite and positive},\\
1,&\text{the run lengths are unbounded or some run is infinite}.
\end{cases}
\]
Furthermore, **the norm is Fréchet differentiable at a binary sequence if and only if precisely one run has the largest length and that length is finite and positive**. In every other binary case, it is not even Gâteaux differentiable.

When the unique longest run consists of the edges \(r,r+1,\ldots,r+m-1\), define \(\theta=\pi/(m+2)\) and \(u_j=\sqrt{2/(m+2)}\sin(j\theta)\) for \(1\le j\le m+1\). The real Fréchet derivative, on arbitrary bounded **complex** perturbations \(h\), is
\[
DN(a)[h]=\sum_{j=1}^{m}u_ju_{j+1}\operatorname{Re}h_{r+j-1}.
\]
For sufficiently small \(\|h\|_\infty\), the error in the linear approximation is bounded by a constant depending on \(m\) times \(\|h\|_\infty^2\).

## Assumptions and scope
All indices begin at one. We call a binary run maximal with respect to inclusion among adjacent positive-weight edges; it may terminate at the start of the half-line or at a zero. There can be finitely or infinitely many runs and possibly one infinite run. Fréchet and Gâteaux differentiability refer to the **real** underlying vector space of complex \(\ell_\infty\), which is essential because a norm is never complex-Fréchet differentiable as a complex-valued holomorphic map on a complex neighborhood of a nonzero vector. No topology other than the uniform norm is used. The numerical-radius norm is equivalent to the uniform norm, so differentiability is unchanged if uniform-norm convergence describes the perturbations.

## Proof
**1. Reduction to a Jacobi operator.** Define \(J(b)\) on \(\ell_2(\mathbb N)\), for a bounded nonnegative sequence \(b\), to be the real symmetric zero-diagonal tridiagonal operator with neighboring entries \(b_n/2\). For all bounded complex \(z\), gauge transformations along the half-line and the variational characterization give
\[
N(z)=\sup_{\|x\|_2=1}\sum_{n\ge1}|z_n|\,|x_n|\,|x_{n+1}|=\sup\sigma(J(|z|)).
\]
The last equality follows from the Rayleigh variational principle: replacing a real vector by its coordinatewise absolute value never reduces the quadratic form. The equality with the first supremum follows by choosing the phases of consecutive coordinates recursively to align the terms, first for finitely supported vectors and then by approximation. Consequently \(N(z)=\|J(|z|)\|\), since the tridiagonal graph is bipartite and its spectrum is symmetric about zero. The uniform estimate
\[
\|J(|z|)-J(|z'|)\|\le\|z-z'\|_\infty
\]
follows by writing \(J(b)\) as half the sum of a unilateral weighted shift and its adjoint.

**2. Exact binary radius.** Zeros of \(a\) split the tridiagonal matrix into independent path components, with one isolated-vertex component if necessary. A run of \(k\ge1\) one-edges is a path on \(k+1\) vertices. Its top eigenvalue is \(\lambda_k=\cos(\pi/(k+2))\), with normalized positive eigenvector whose \(j\)-th entry is \(\sqrt{2/(k+2)}\sin(j\pi/(k+2))\); this is verified by the sine addition formula and vanishing boundary values. Set \(\lambda_0=0\). Hence the top of the direct-sum spectrum is the supremum of these \(\lambda_k\). The strictly increasing numbers \(\lambda_k\) tend to one. An infinite path has top spectral value one, witnessed by long finite constant blocks. The stated three-case formula follows, including \(a=0\).

**3. Unique finite longest run gives uniform quadratic differentiability.** Assume \(m\ge1\) and exactly one run has length \(m\). Let \(u\) be the normalized positive top eigenvector for that path, extended by zero elsewhere. The top eigenvalue \(\lambda_m\) of \(J(a)\) is simple and isolated: every other path has length at most \(m-1\), and the second-largest eigenvalue of the unique longest path is below \(\lambda_{m-1}\) (when \(m=1\), its other eigenvalue is negative). In particular, the difference between the top of the spectrum and the rest is bounded below by
\[
\delta_m=\cos\bigl(\pi/(m+2)\bigr)-\cos\bigl(\pi/(m+1)\bigr)>0.
\]
For any bounded self-adjoint perturbation \(E\) with \(\|E\|<\delta_m/4\), the Rayleigh quotient, after splitting a unit vector into its \(u\)-component and orthogonal component, yields the *uniform spectral-gap estimate*
\[
0\le\sup\sigma(J(a)+E)-\lambda_m-\langle u,Eu\rangle\le\frac{2}{\delta_m}\|E\|^2.
\]
Indeed, for a unit vector with orthogonal component of norm \(t\), the difference of its Rayleigh quotient from \(\lambda_m+\langle u,Eu\rangle\) is at most \(-\delta_m t^2+2\|E\|t+2\|E\|t^2\). When \(\|E\|<\delta_m/4\), completing the square bounds this by \(2\|E\|^2/\delta_m\). Evaluation at \(u\) gives the lower bound. Taking \(E=J(|a+h|)-J(a)\), we have \(\|E\|\le\|h\|_\infty\). Crucially, although the map \(z\mapsto|z|\) is not differentiable at zero coordinates, the expectation \(\langle u,Eu\rangle\) uses **only** the edges in the single longest run, where the original weight equals one. For \(\|h\|_\infty<1/2\), uniformly on these edges,
\[
|1+h_n|=1+\operatorname{Re}h_n+O(|h_n|^2).
\]
Because the off-diagonal matrix entries are halved, their two contributions in the quadratic form add to \(u_ju_{j+1}\), giving exactly the displayed derivative and the quadratic remainder. This proves real Fréchet differentiability even when the binary weight has infinite support away from the winning run.

**4. Two or more finite longest runs forbid Gâteaux differentiability.** Fix one longest run and perturb all of its \(m\) edges by \(t\in\mathbb R\), leaving every other edge unchanged; call this bounded direction \(h\). For sufficiently small positive \(t\), the modified run has radius \((1+t)\lambda_m\), larger than every unmodified run. For sufficiently small negative \(t\), an unmodified maximal run still has radius \(\lambda_m\), while the chosen run has a smaller radius. Thus
\[
N(a+th)=\begin{cases}\lambda_m(1+t),&0<t<1/2,\\\lambda_m,&-1/2<t<0.\end{cases}
\]
The one-sided directional derivatives disagree, so the Gâteaux derivative does not exist.

**5. Unbounded runs forbid Gâteaux differentiability.** Whenever one-runs have arbitrarily large lengths, one can select two disjoint families of finite contiguous one-blocks, with the lengths unbounded *within each family*. This is immediate by partitioning infinitely many increasingly long finite runs into two subsequences; an infinite run can be split into successively longer disjoint subblocks. Define a bounded real direction \(h\) to be \(+1\) on the first family of selected edges, \(-1\) on the second, and zero elsewhere. For \(|t|<1\), the coordinate bound gives \(N(a+th)\le1+|t|\). In the family whose sign agrees with that of \(t\), arbitrarily long blocks all have weight \(1+|t|\). Their path Rayleigh quotients tend to \(1+|t|\), proving the exact identity \(N(a+th)=1+|t|\). Its two one-sided slopes at zero differ. The zero binary sequence is also non-Gâteaux smooth, since every nonzero norm is nondifferentiable at zero. These alternatives exhaust binary sequences.

## Verification
The spectral and directional calculations are analytic and apply to infinitely many coordinates without finite truncation assumptions. A finite-dimensional cross-check used a 47-edge binary vector with a unique four-edge run and a two-edge competitor, and compared the exact sine-vector derivative with symmetric-matrix eigenvalue calculations for complex perturbations. The observed errors were of quadratic order for perturbation sizes \(10^{-2},10^{-3},10^{-4}\). Duplicating the four-edge maximum produced right directional slope \(\cos(\pi/6)\) and left slope zero, as proved above. Such finite tests are illustrative, not part of the proof.

For symbolic replay, the sine addition identity \(\sin((j-1)\theta)+\sin((j+1)\theta)=2\cos\theta\sin(j\theta)\), together with \(\sum_{j=1}^{m+1}\sin^2(j\theta)=(m+2)/2\), verifies the eigenpair. The spectral-gap Rayleigh estimate and the explicit two-sided perturbations verify the infinite-dimensional differentiability and failure cases respectively.

## Relationship to prior work
Sharif's 2023 study treats the numerical radius of unilateral weighted shifts as an equivalent norm on \(\ell_\infty\), derives links with Banach limits, and records classical variational methods for weighted shifts; it does not give this differentiability classification at binary weights. Roy and Sain's 2021 article investigates numerical-radius smoothness in operator spaces, with finite-dimensional criteria. Martín and collaborators' 2023 article supplies abstract smoothness criteria via numerical ranges. None of these inspected statements singles out the binary cube, characterizes its unique-longest-run phase boundary, or computes the Fréchet derivative for possibly infinite-support binary sequences. The proof uses familiar spectral variational principles but requires identifying both the uniform spectral gap and the failure directions across all infinite-run patterns.

## Limitations
This theorem concerns only the binary, nonnegative coordinate skeleton \(\{0,1\}^{\mathbb N}\) of the numerical-radius norm. Perturbations in the differentiability assertion are nevertheless unrestricted bounded complex sequences. It does not classify smooth points at general weighted sequences, does not address numerical-radius smoothness of the weighted shift under arbitrary **operator** perturbations outside the weighted-shift subspace, and does not establish any novelty claim against inaccessible or unindexed literature. 
## References
- A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876 (first version posted 2023-03-02), https://arxiv.org/abs/2303.00876.
- S. Roy and D. Sain, *Numerical radius and a notion of smoothness in the space of bounded linear operators*, arXiv:2107.03490, https://arxiv.org/abs/2107.03490.
- M. Martín et al., *A numerical range approach to Birkhoff-James orthogonality with applications*, arXiv:2306.02638, https://arxiv.org/abs/2306.02638.
