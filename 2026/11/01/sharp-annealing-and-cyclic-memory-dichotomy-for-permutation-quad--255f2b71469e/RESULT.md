# Sharp annealing and cyclic-memory dichotomy for permutation quadratic stochastic maps

## Finding
Consider the permutation family of quadratic stochastic maps described below, now with a possibly different mixing coefficient at every iteration. The entire long-time behavior is determined by the scalar quantity \(\sum_{n\geq0}\alpha_n(1-\alpha_n)\), with one precisely characterized finite-time exception.

**Theorem.** Let \(m\geq3\), let \(\pi\) permute \(\{1,\ldots,m-1\}\), and let \((\alpha_n)_{n\geq0}\subset[0,1]\) be arbitrary. Put \((Pz)_k=z_{\pi(k)}\), let \(L\) be the order of \(P\), and set \(\Pi=L^{-1}\sum_{r=0}^{L-1}P^r\). Given any initial probability vector \(x^{(0)}\) with \(0<x_m^{(0)}<1\), define \(z^{(0)}=(x_1^{(0)},\ldots,x_{m-1}^{(0)})/(1-x_m^{(0)})\), \(u=2x_m^{(0)}-1\), and \(D_n=\sum_{j=0}^{n-1}\alpha_j(1-\alpha_j)\).

1. If \(D_n\to\infty\), every such trajectory tends to the permutation-cycle-balanced point \(\big(\Pi z^{(0)}/2,1/2\big)\). If \(P\neq I\), define \(\sigma=\min\{\sin^2(\pi j/\ell):\ell\text{ is a cycle length of }\pi,\ 1\le j<\ell\}>0\). Then the normalized composition satisfies the quantitative estimate
\[
\left\|z^{(n)}-\Pi z^{(0)}\right\|_2\le e^{-2\sigma D_n}\left\|z^{(0)}-\Pi z^{(0)}\right\|_2.
\]
2. If \(D_\infty<\infty\), put \(\delta_j=\min(\alpha_j,1-\alpha_j)\), \(b_j=\mathbf1_{\{\alpha_j<1/2\}}\), and \(B_n=\sum_{j<n}b_j\). The stochastic matrices
\[
Q_n=\prod_{j<n}\left[(1-\delta_j)I+\delta_jP^{1-2b_j}\right]
\]
converge in operator norm to a stochastic matrix \(Q_\infty\). The omega-limit set of the nonlinear trajectory is exactly
\[
\omega(x^{(0)})=\begin{cases}
\{\big(P^{B_\infty}Q_\infty z^{(0)}/2,1/2\big)\},&B_\infty<\infty,\\
\{\big(P^rQ_\infty z^{(0)}/2,1/2\big):0\le r<L\},&B_n\to\infty.
\end{cases}
\]
Repeated elements in the second set are counted only once. Quantitatively,
\[
\left\|z^{(n)}-P^{B_n}Q_\infty z^{(0)}\right\|_2
\le2\left(\sum_{j\ge n}\delta_j\right)\left\|z^{(0)}\right\|_2.
\]
3. Suppose \(P\ne I\). **Every** initial point with \(0<x_m^{(0)}<1\) converges to its cycle-balanced point if and only if either \(D_\infty=\infty\), or \(P^2=I\) and \(\alpha_j=1/2\) for at least one \(j\). In the latter case that single update erases every nontrivial permutation mode. For \(P=I\), every trajectory converges to its cycle-balanced point for any schedule.

**Sharp critical example.** Fix a three-cycle \(\pi\), take \(m=4\), and let \(\alpha_n=(n+4)^{-p}\) for \(p>0\). For \(p\le1\), all interior-mass trajectories converge to the cycle-balanced point. At \(p=1\), each non-cycle-balanced normalized orbit has sharp decay \(\|z^{(n)}-\Pi z^{(0)}\|_2=\Theta(n^{-3/2})\). For \(p>1\), every non-cycle-balanced initial state has an omega-limit set of exactly three distinct points, cyclically permuted by \(P\).

## Assumptions and scope
The state space is the **closed** simplex \(\{x\in\mathbb R^m:x_k\ge0,\ \sum_kx_k=1\}\). The updates are, for all \(n\ge0\),
\[
x_k^{(n+1)}=2x_m^{(n)}\big(\alpha_nx_k^{(n)}+(1-\alpha_n)x_{\pi(k)}^{(n)}\big)\quad(1\le k<m),\qquad
x_m^{(n+1)}=(x_m^{(n)})^2+\big(1-x_m^{(n)}\big)^2.
\]
These updates preserve the simplex. The theorem allows zeros among the first \(m-1\) components, but assumes \(0<x_m^{(0)}<1\) so normalization is defined. If \(x_m^{(0)}\in\{0,1\}\), the trajectory reaches the last-coordinate vertex within one update. The omega-limit set means the accumulation set of the sequence, not a periodic orbit of a fixed autonomous map; coefficients may vary forever.

## Proof
**Exact separation.** Let \(s_n=x_m^{(n)}\), \(u_n=2s_n-1\), and \(z^{(n)}=(x_1^{(n)},\ldots,x_{m-1}^{(n)})/(1-s_n)\). Direct substitution gives
\[
u_{n+1}=u_n^2,\qquad u_n=u^{2^n},\qquad
1-s_{n+1}=2s_n(1-s_n),\qquad
z^{(n+1)}=[\alpha_nI+(1-\alpha_n)P]z^{(n)}.
\]
Therefore the **exact finite-time formula** is
\[
x^{(n)}=\left(\frac{1-u^{2^n}}2\prod_{j<n}[\alpha_jI+(1-\alpha_j)P]z^{(0)},\ \frac{1+u^{2^n}}2\right).
\]
The finite product is order-independent because all factors are polynomials in \(P\). Since \(|u|<1\), the scalar coordinate approaches \(1/2\) doubly exponentially.

**Divergent-mixing regime.** Each cycle of length \(\ell\) diagonalizes \(P\) into the Fourier eigenvalues \(\zeta_{\ell,j}=e^{2\pi i j/\ell}\), \(0\le j<\ell\). On this mode the step multiplier is \(\lambda_{n,\ell,j}=\alpha_n+(1-\alpha_n)\zeta_{\ell,j}\), with exact modulus identity
\[
|\lambda_{n,\ell,j}|^2=1-4\alpha_n(1-\alpha_n)\sin^2(\pi j/\ell).
\]
The constant modes \(j=0\) form the range of \(\Pi\) and remain unchanged. For every other mode, \(|\lambda_{n,\ell,j}|\le e^{-2\sin^2(\pi j/\ell)\alpha_n(1-\alpha_n)}\), including any zero multipliers. Orthogonality of Fourier modes and finiteness of the cycle set give the stated operator-norm estimate and convergence when \(D_n\to\infty\).

**Summable-mixing regime.** For \(0\le\delta\le1/2\), \(\delta/2\le\delta(1-\delta)\le\delta\); hence \(D_\infty<\infty\) is equivalent to \(\sum_j\delta_j<\infty\). By direct algebra,
\[
\alpha_jI+(1-\alpha_j)P=P^{b_j}\big[(1-\delta_j)I+\delta_jP^{1-2b_j}\big].
\]
All factors commute. The bracket factors are convex combinations of permutation matrices, have operator \(2\)-norm at most one, and differ from the identity in norm by at most \(2\delta_j\). Their products \(Q_n\) are Cauchy, with \(\|Q_\infty-Q_n\|_2\le2\sum_{j\ge n}\delta_j\). It follows that \(z^{(n)}=P^{B_n}Q_nz^{(0)}\) differs by a vanishing amount from \(P^{B_n}Q_\infty z^{(0)}\). If \(B_n\) eventually stabilizes, the latter converges. Otherwise \(B_n\) increases by zero or one infinitely often, so it takes each residue modulo \(L\) infinitely often, yielding precisely the stated finite accumulation set.

**Sharp universal criterion and exceptional cancellation.** Sufficiency is established above. If \(D_\infty<\infty\) and \(\pi\) has a cycle of length \(\ell\ge3\), the Fourier mode \(j=1\) has no zero step multiplier for any \(\alpha\in[0,1]\); its modulus is bounded below by \(\cos(\pi/\ell)>0\). Since the sum of its squared deficits is finite, the infinite product of its moduli is strictly positive. Taking a probability vector concentrated on one coordinate of that cycle produces a nonzero surviving component orthogonal to \(\Pi\), so universal convergence to \(\Pi z^{(0)}\) is impossible. If all nontrivial cycles have length two, the only nontrivial eigenvalue is \(-1\), with multiplier \(2\alpha_j-1\). A single \(\alpha_j=1/2\) annihilates the entire nonconstant subspace, and \([I+P]/2=\Pi\) when \(P^2=I\). Without such a step, the finite-deficit condition again gives a strictly positive infinite product, and an unbalanced initial vector witnesses failure. The identity permutation is immediate.

**Critical three-cycle.** For \(\alpha_n=(n+4)^{-p}\), the sum of \(\alpha_n(1-\alpha_n)\) diverges exactly when \(p\le1\). For \(p>1\), \(\sum_n\alpha_n<\infty\), every step is permutation-dominated, and the surviving three-cycle Fourier product is nonzero; every unbalanced probability vector therefore gives three distinct limits. At \(p=1\), the nonconstant Fourier multiplier has
\[
|\lambda_n|^2=1-3\alpha_n(1-\alpha_n)=\frac{n^2+5n+7}{(n+4)^2}.
\]
Consequently \(\log|\lambda_n|=-3/[2(n+4)]+O(n^{-2})\), so \(\prod_{j<n}|\lambda_j|=C n^{-3/2}(1+o(1))\) for some \(C>0\). The two nonconstant modes have equal modulus, giving the stated exact order for every unbalanced initial vector. This establishes the sharp boundary.

## Verification
The accompanying standalone checker (run with `python checker.py`) performs exact-rational direct iterations of the nonlinear update, its normalized linear factorization, and the rotation/near-identity decomposition across dimensions three through six and multiple coefficient schedules. It reports 2,961 matching iterate/factorization identities and checks the special half-mixing projection on two-cycles. The finite tests do not constitute proof of the infinite-time statements; those follow from the spectral infinite-product and telescoping arguments above. The exact modulus polynomial for a three-cycle is \(1-3\alpha(1-\alpha)\).

## Relationship to prior work
Jamilov's 2022 preprint (published in 2023) studies the same quadratic operators for a **fixed** interpolation coefficient and proves the corresponding autonomous limit-set classification. The 2020 permutation-QSO predecessor treats the pure-permutation endpoint. A 2023 article by Jamilov and Khudoyberdiev also concerns fixed-parameter permutation QSOs; its full text was inaccessible for final priority comparison. Jamilov and Mukhitdinov's later paper treats fixed convex combinations and compositions of a different two-dimensional simplex family. General results on mixing and products of inhomogeneous stochastic matrices provide relevant background, but the inspected sources do not state the schedule-dependent necessary-and-sufficient criterion with its one-step involution exception, exact residual cyclic accumulation sets, and sharp three-cycle critical exponent for this nonlinear family.

## Limitations
This concerns deterministic schedules \((\alpha_n)\), not adaptive coefficients depending on the evolving state, and a fixed permutation \(\pi\). It does not assert that a finite omega-limit set is an actual periodic trajectory of the nonautonomous system. The limiting stochastic matrix \(Q_\infty\) is generally given by an infinite product rather than elementary entries. Universal convergence means the prescribed permutation-cycle-balanced state, not convergence to an arbitrary limit (which can happen in the summable regime). The claim has undergone internal mathematical checks only, not independent verification; publication-priority comparison against some inaccessible literature remains open.

## References
- U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, arXiv:2210.05107, first posted October 11, 2022; *Communications in Mathematics* 31 (2023), 31–41. https://arxiv.org/html/2210.05107v2 ; https://doi.org/10.46298/cm.10135 .
- U. U. Jamilov, Kh. O. Khudoyberdiev and M. Ladra, *Quadratic operators corresponding to permutations*, *Stochastic Analysis and Applications* 38 (2020), 929–938. https://doi.org/10.1080/07362994.2020.1747494 .
- U. U. Jamilov and Kh. O. Khudoyberdiev, *On the dynamics of non-Volterra quadratic operators corresponding to permutations*, *Journal of Difference Equations and Applications* 30 (2024), 336–360. https://doi.org/10.1080/10236198.2023.2284827 .
- U. U. Jamilov and R. T. Mukhitdinov, *Dynamics of a Convex Combination and Superposition of Non-Volterra Quadratic Stochastic Operators*, *Journal of Convex Analysis* 32 (2025), 975–988. https://doi.org/10.68381/jca32052 .
- W. Bartoszek and M. Pułka, *On mixing in the class of quadratic stochastic operators*, *Nonlinear Analysis* 86 (2013), 95–113. https://doi.org/10.1016/j.na.2013.03.011 .
- Z. Xia et al., *On Inhomogeneous Infinite Products of Stochastic Matrices and Applications*, arXiv:2401.14612, first posted January 26, 2024. https://arxiv.org/abs/2401.14612 .
