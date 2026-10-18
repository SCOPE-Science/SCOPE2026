# Three spatial phases of quasi-stationary laws for power-tail Farey maps

## Finding

For each fixed \(\theta>0\), the canonical absolutely continuous conditionally invariant probability of the \(\alpha\)-Farey map with tail lengths \(t_j=j^{-\theta}\) and absorbing hole \([0,n^{-\theta}]\) has an explicit finite-dimensional cell law. As the hole shrinks, that law undergoes exactly three different spatial scaling regimes, including a logarithmically uniform critical phase.

Let \(J_n\) denote the index of the partition interval containing a point sampled from this probability, and let \(X_n\) be the point itself. Then:

1. If \(\theta>1\), the law of \(J_n\) converges **in total variation** to the distribution \(\Pr(J=j)=j^{-\theta}/\zeta(\theta)\). Equivalently the spatial probabilities converge in total variation to the normalized finite absolutely continuous invariant measure of the closed map.
2. If \(\theta=1\), then \(\log J_n/\log n\) converges to the uniform law on \([0,1]\), with Kolmogorov error \(O(1/\log n)\). The same is true of \(-\log X_n/\log n\).
3. If \(0<\theta<1\), then \(J_n/n\) converges to a continuous law on \((0,1)\) with density
\[
f_\theta(u)=\theta c_\theta\int_u^1 v^{-1-\theta}\exp\bigl(c_\theta(v-u)\bigr)\,dv, \qquad 0<u<1,
\]
where \(c_\theta>0\) is the unique solution of
\[
\theta\int_0^1 v^{-1-\theta}(\exp(c_\theta v)-1)\,dv=1.
\]
Consequently \(n^\theta X_n\) converges weakly to \(U_\theta^{-\theta}\), where \(U_\theta\) has density \(f_\theta\).

At \(\theta\le1\), the *unscaled* quasi-stationary probabilities concentrate at zero. At \(\theta>1\), they instead approach a nondegenerate stationary probability. The spectral escape-rate constants alone do not describe these three spatial limits.

## Assumptions and scope

Fix \(\theta>0\) and integer \(n\ge2\). Define \(t_j=j^{-\theta}\) for \(j\ge1\), \(a_j=t_j-t_{j+1}>0\), and the half-open cells \(A_j=(t_{j+1},t_j]\). On \((0,1]\) define the piecewise-affine map
\[
F_\theta(x)=\begin{cases}
(1-x)/a_1,&x\in A_1,\\
(a_{j-1}/a_j)(x-t_{j+1})+t_j,&x\in A_j,\ j\ge2.
\end{cases}
\]
Set \(F_\theta(0)=0\). The set \(H_n=[0,t_n]\) is absorbing; the surviving cells are \(A_1,\ldots,A_{n-1}\). Endpoint conventions have no effect on absolutely continuous distributions.

The **canonical quasi-stationary probability** \(\mu_n\) means the unique normalized positive Perron eigen-density of the *open* transfer operator restricted to functions constant on these surviving cells. It is also the limit of normalized forward iterates of an initially positive cell-constant density because the associated finite Markov matrix is primitive. This qualification excludes unrelated noncanonical conditionally invariant measures. The distribution \(J_n\) is \(\mu_n(A_j)\) and \(X_n\sim\mu_n\). All statements hold for each fixed \(\theta\) as \(n\to\infty\), not uniformly when \(\theta\) varies with \(n\).

## Proof

**1. Exact eigenvector.** On cell indices, the one-step open mass matrix has transitions \(K_{1j}=a_j\) for \(1\le j<n\), \(K_{j,j-1}=1\) for \(2\le j<n\), and no other nonzero entries. The first row sums to \(1-t_n\), whereas the other rows sum to one. This is the exact pushforward of cell-constant densities because the map carries \(A_1\) affinely over \([0,1]\) and each \(A_j\), \(j\ge2\), affinely onto \(A_{j-1}\). Perron–Frobenius gives a simple leading eigenvalue \(\lambda_n\in(0,1)\). With \(z_n=1/\lambda_n>1\), the characteristic root identity is
\[
\sum_{k=1}^{n-1}a_k z_n^k=1. \tag{1}
\]
The corresponding normalized left eigenvector \(\pi_{n,j}=\mu_n(A_j)\) is
\[
\pi_{n,j}=\pi_{n,1}\sum_{k=j}^{n-1}a_k z_n^{k-j+1},\qquad
\pi_{n,1}=n^\theta(1-\lambda_n). \tag{2}
\]
The backward recursion \(\lambda_n\pi_{n,j}=a_j\pi_{n,1}+\pi_{n,j+1}\) gives the first equality (with the final term absent for \(j=n-1\)); the loss of probability through \(H_n\), equal to \(t_n\pi_{n,1}\), gives the second. Equation (1) also verifies normalization of (2).

**2. Finite-measure regime.** For \(\theta>1\), set \(S_n=\sum_{k=1}^{n-1}k a_k=\sum_{j=1}^n j^{-\theta}-n^{1-\theta}\). Thus \(S_n\to\zeta(\theta)\). From \(z_n^k\ge1+k(z_n-1)\), (1) implies \(z_n-1\le n^{-\theta}/S_n\), and hence \(n\log z_n\to0\). The mean value theorem in (1) gives \(z_n-1\sim n^{-\theta}/\zeta(\theta)\), so \(\pi_{n,1}\to1/\zeta(\theta)\). For fixed \(j\), (2) then gives \(\pi_{n,j}\to t_j/\zeta(\theta)\). Since the limiting masses sum to one, Scheffé's lemma on the countable state space implies total-variation convergence. Within each cell both measures are uniform, so total variation also holds for the spatial probabilities.

**3. Critical regime.** Let \(\theta=1\) and \(L_n=\sum_{k=1}^{n-1}k a_k=H_n^{\mathrm{harm}}-1\), where \(H_n^{\mathrm{harm}}=\sum_{k=1}^{n}1/k\). The preceding root bound gives \(n\log z_n\le1/L_n\), hence \(1\le z_n^{k-j+1}\le\exp(1/L_n)\) for every term of (2). Since \(\sum_{k=j}^{n-1}a_k=1/j-1/n\), the normalized vector \(\pi_n\) differs in total variation by \(O(1/L_n)\) from the explicit harmonic proxy
\[
q_{n,j}=\frac{1/j-1/n}{H_n^{\mathrm{harm}}-1},\qquad 1\le j<n.\tag{3}
\]
Indeed every unnormalized weight differs from its proxy by a factor in \([1,\exp(1/L_n)]\), and so does the normalization. For \(0\le s\le1\), let \(m=\min(n-1,\lfloor n^s\rfloor)\). Then
\[
\sum_{j=1}^m q_{n,j}=\frac{H_m^{\mathrm{harm}}-m/n}{H_n^{\mathrm{harm}}-1}
=s+O(1/\log n)
\]
uniformly in \(s\). This proves the Kolmogorov estimate for \(\log J_n/\log n\). If \(X_n\in A_{J_n}\), then \(1/(J_n+1)<X_n\le1/J_n\), so the difference of \(-\log X_n/\log n\) and \(\log J_n/\log n\) is at most \(\log2/\log n\). The same weak limit and Kolmogorov rate follow.

**4. Infinite-measure regime.** For \(0<\theta<1\), write \(c_n=n\log z_n\). The root identity becomes exactly
\[
1=n^\theta\sum_{k=1}^{n-1} a_k\bigl(\exp(c_n k/n)-1\bigr).\tag{4}
\]
For every fixed \(c\ge0\), the right side with \(c_n\) replaced by \(c\) converges to \(\theta\int_0^1 v^{-1-\theta}(\exp(cv)-1)\,dv\), by a Riemann sum with an integrable majorant of order \(v^{-\theta}\) near zero. The limiting function is continuous, strictly increasing from zero to infinity, so (4) and monotonicity yield \(c_n\to c_\theta\), with \(c_\theta\) defined in the finding. Equation (2) gives \(\pi_{n,1}\sim c_\theta n^{\theta-1}\). For any fixed \(u\in(0,1)\) and \(j/n\to u\), a uniform Riemann-sum calculation over \([u,1]\) yields
\[
n\pi_{n,j}\longrightarrow\theta c_\theta\int_u^1v^{-1-\theta}e^{c_\theta(v-u)}\,dv=f_\theta(u).\tag{5}
\]
No probability mass disappears at zero: by (2), \(z_n^n\) bounded, and telescoping of \(a_k\),
\[
\pi_{n,j}\le C_\theta n^{\theta-1}j^{-\theta},\quad
\sum_{j\le\delta n}\pi_{n,j}\le C'_\theta\delta^{1-\theta}\quad (\delta>0)
\]
for sufficiently large \(n\). Summing (5) away from zero and using this estimate proves weak convergence on \((0,1)\). Direct Tonelli integration checks that the stated density has total mass
\[
\int_0^1 f_\theta(u)du=\theta\int_0^1v^{-1-\theta}(e^{c_\theta v}-1)dv=1.
\]
Finally, the deterministic interval bounds \((n/(J_n+1))^\theta<n^\theta X_n\le(n/J_n)^\theta\) and the limit's lack of an atom at zero imply \(n^\theta X_n\Rightarrow U_\theta^{-\theta}\) by Slutsky and continuous mapping.

These steps prove all asserted limits and bounds.

## Verification

`verify.py` uses only Python's standard library. It independently constructs the exact finite-state left Perron vector from the backward recursion and the scalar root, checks the eigenvector and survival identities at 30 combinations of parameters and cutoffs, and checks critical harmonic-proxy bounds at three additional cutoffs. Running the included script produced `VERIFY_OK`. Numerical checks do not establish the all-\(n\) theorem; Steps 1–4 above do.

## Relationship to prior work

Knight and Munday (2014 preprint, 2016 revision) define this exact map and Markov hole. Their characteristic polynomial is equation (12); sections 4.2–4.5 derive the escape-rate scales, including the constant \(c_\theta\) for \(0<\theta<1\). Those formulas and the existence of the finite-dimensional conditional eigen-density are **prior work**. The present contribution concerns the **normalized eigenvector's spatial distribution**, its three scaling phases, an explicit nontrivial subcritical limiting density, and the critical uniform logarithmic law with error bound.

Froyland–Murray–Stancevic (2011) prove convergence of conditional invariant probabilities to the finite ACIM for a related Pomeau–Manneville system; this is stronger general context for the finite-measure behavior but does not provide the specific infinite-measure spatial scaling laws here. Demers–Fernandez (2014) study holes away from the neutral origin and polynomial escape with singular forward limits; the hole placement and conditional object differ. Bonanno–Tikekar (2026), in their Example 3.3, recover escape rates for the same piecewise-linear family using an **induced, survivor-supported Gibbs equilibrium probability**. This is not the uninduced open transfer operator's conditionally invariant probability described by (2), and their conclusions do not state the law of \(J_n\) under (2).

## Limitations

The theorem is for fixed \(\theta>0\), exact power-tail cells, and an absorbing Markov hole of the specified size. It does not extend by assertion to arbitrary intermittent maps, other hole geometries, or a joint limit where \(\theta\) varies with \(n\). The canonical cell-constant conditional law is not claimed to exhaust every possible conditionally invariant measure. The novelty assessment is based on inspected primary literature and research search, not a proof of absolute historical priority; a broader unpublished or unindexed eigenvector theorem could overlap.

## References

- G. Knight and S. Munday, *Escape rate scaling in infinite measure preserving systems*, arXiv:1411.3515v1 (first posted 2014-11-13), revised 2016; https://arxiv.org/abs/1411.3515 ; full text https://arxiv.org/html/1411.3515v2 .
- G. Froyland, R. Murray, and O. Stancevic, *Spectral degeneracy and escape dynamics for intermittent maps with a hole*, arXiv:1012.2149 (2010–2011); https://arxiv.org/html/1012.2149v2 .
- M. F. Demers and B. Fernandez, *Escape Rates and Singular Limiting Distributions for Intermittent Maps with Holes*, arXiv:1410.4995v1 (2014); https://arxiv.org/pdf/1410.4995 .
- C. Bonanno and S. N. Tikekar, *On the escape rate for intermittent maps with holes shrinking around the indifferent fixed point*, arXiv:2601.15908v3 (2026), Example 3.3; https://arxiv.org/html/2601.15908v3 .
