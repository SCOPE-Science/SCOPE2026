# Optimal resetting to an unknown target on vertex-transitive networks

## Finding

Let \(G\) be a finite, connected, undirected, loopless vertex-transitive graph on \(n\geq3\) vertices, and let \(P\) be its simple-random-walk transition matrix. A searcher is initially placed according to a probability vector \(\rho\); at each discrete time step it makes a \(P\)-move with probability \(1-\gamma\), or relocates to a fresh independent \(\rho\)-sample with probability \(\gamma\). The target is chosen uniformly and independently once, is fixed thereafter, and is detected also at time zero.

For every \(0<\gamma<1\), the unique relocation distribution minimizing both the mean first-hitting time averaged over uniformly chosen targets **and** the worst-target mean first-hitting time is the uniform distribution \(u\). More precisely, writing \(z=1-\gamma\), \(Q=(I-zP)^{-1}\), \(c=Q_{jj}\) (independent of \(j\)), \(R_j=(\rho Q)_j\), and \(\mu=1/(n\gamma)\), the target-specific mean and exact mean regret are

\[
 H_j(\rho,\gamma)=\frac1\gamma\left(\frac{c}{R_j}-1\right),
 \qquad
 \frac1n\sum_j H_j(\rho,\gamma)-\frac1n\sum_j H_j(u,\gamma)
 =c\gamma n\sum_j\frac{(R_j-\mu)^2}{R_j}.
\]

The regret is strictly positive for every nonuniform \(\rho\). If \(1=\lambda_1>\lambda_2\geq\cdots\geq\lambda_n\geq-1\) are the eigenvalues of \(P\), the optimal mean at fixed \(\gamma\) is

\[
 F(z)=\sum_{k=2}^{n}\frac{1}{1-z\lambda_k}.
\]

The stationary-distribution-weighted Kemeny functional of the reset chain is, in contrast, independent of \(\rho\) (its spectrum is invariant under the relocation law). Uniform-prior hitting-time optimization detects a law dependence that the Kemeny functional does not.

This is strictly convex on \([0,1]\) and its unique minimizing \(z\) lies in \((0,1)\) exactly when

\[
 \sum_{k=2}^{n}\frac{\lambda_k}{(1-\lambda_k)^2}>0;
\]

otherwise the minimum is at \(z=1\) (no resets). The endpoint \(z=0\) (always reset) is never optimal. At the interior optimum \(z_*\), the unique scalar equation is \(\sum_{k=2}^{n}\lambda_k/(1-z_*\lambda_k)^2=0\).

For the nearest-neighbor cycle \(C_n\), the displayed strict inequality holds **if and only if** \(n\geq5\). Hence cycles with \(n=3,4\) are optimized by no resetting; all \(C_n\) with \(n\geq5\) have a unique joint optimum of a uniform relocation distribution and a positive resetting probability. For \(C_5\), exactly

\[
 \gamma_*=5-2\sqrt5,\qquad F(1-\gamma_*)=2+\frac4{\sqrt5}.
\]

Furthermore, as \(n\to\infty\) through integer cycle sizes, \(\gamma_*=1-1/n+O(n^{-2})\), and the jointly minimized mean is \(n-1-1/(2n)+O(n^{-2})\).

## Assumptions and scope

Every step, including a relocation step, consumes one time unit. No physical move occurs on the same step as relocation. The initial distribution and all relocation draws share the same arbitrary law \(\rho\), including possible zero weights. An initial position equal to the target gives hitting time zero. The uniformly sampled target is independent of all walker and relocation randomness and is not resampled. The average objective is the arithmetic mean of target-specific expected times; it is **not** the stationary-distribution-weighted Kemeny average for a nonuniform relocation law. All expectations under \(0<\gamma<1\) are finite because the graph is connected.

At \(\gamma=0\), relocation never occurs and every initial \(\rho\) yields the same uniform-target average \(F(1)\), by the Kemeny constant identity. At \(\gamma=1\), a relocation law omitting a target may have infinite mean for that target; uniform relocation yields \(F(0)=n-1\). Thus distribution uniqueness is asserted for strictly positive, strictly subunit resetting probabilities, with the corresponding qualification at the no-reset boundary.

## Proof

**1. Resolvent and renewal.** For the walk without resets, let \(T_j\) be its first visit to \(j\), allowing \(T_j=0\). The strong Markov property at \(T_j\) gives, for \(0<z<1\),

\[
 Q_{ij}=\mathbb E_i[z^{T_j}]Q_{jj}.
\]

Vertex transitivity makes \(Q_{jj}=c\) for all \(j\). Averaging the identity against \(\rho\), the success probability in one attempt before the next geometric reset is \(a_j=R_j/c\). A reset occurs at a geometric step and consumes that step; the expected duration of an attempt ending either on success or at that reset is \((1-a_j)/\gamma\). Restarting independently from the same law \(\rho\) gives

\[
 H_j=\frac{1-a_j}{\gamma a_j}=\frac1\gamma\left(\frac c{R_j}-1\right).
\]

The formula agrees directly with the backward equations for the transition matrix \((1-\gamma)P+\gamma\mathbf1\rho\), with the target made absorbing. In particular, relocation onto the target counts as an immediate hit at the end of that relocation step.

**2. Exact optimality of the relocation law.** As \(P\) is stochastic, \(Q\mathbf1=\gamma^{-1}\mathbf1\), so \(\sum_j R_j=\gamma^{-1}=n\mu\). By the harmonic-arithmetic mean inequality, \(\sum_jR_j^{-1}\geq n/\mu\), with equality only when all \(R_j=\mu\). Since \(Q\) is invertible, \(\rho Q=\mu\mathbf1^{\mathsf T}\) implies \(\rho=u\). Expanding \((R_j-\mu)^2/R_j\) yields the exact regret identity in the finding, not merely a bound. Similarly, \(\min_jR_j\leq\mu\), so \(\max_jH_j\geq(c/\mu-1)/\gamma\), with strict inequality unless \(\rho=u\). Thus uniform relocation uniquely minimizes both objectives for every fixed \(0<\gamma<1\).

**3. Spectral optimal rate.** Uniform relocation gives \(R_j=\mu\), whence \(H_j=nc-1/\gamma\) for every target. Because \(nc=\operatorname{tr}Q\) and \(P\) is symmetric, the trivial eigenvalue \(\lambda_1=1\) contributes exactly \(1/\gamma\); cancellation yields \(F(z)\). Every denominator is positive on \([0,1]\), since the connected chain has only one eigenvalue equal to one. Differentiating,

\[
 F'(z)=\sum_{k=2}^{n}\frac{\lambda_k}{(1-z\lambda_k)^2},\qquad
 F''(z)=2\sum_{k=2}^{n}\frac{\lambda_k^2}{(1-z\lambda_k)^3}>0.
\]

Looplessness gives \(\operatorname{tr}P=0\), hence \(F'(0)=\sum_{k=2}^{n}\lambda_k=-1\). Strict convexity and the sign of \(F'(1)\) establish the asserted exhaustive boundary/interior dichotomy and unique root. The reset chain has nontrivial eigenvalues \(z\lambda_2,\ldots,z\lambda_n\) for every \(\rho\), by the rank-one update \(zP+\gamma\mathbf1\rho\); its stationary-weighted Kemeny sum is therefore independent of the reset law, unlike the uniform-prior objective. Because uniform relocation is optimal separately at each positive rate, this also solves the joint law-and-rate optimization. The \(\gamma=0\) boundary has the same objective \(F(1)\) for any initial law by standard mean hitting-time identities for uniform stationary target sampling.

**4. Exact cycle threshold.** On \(C_n\), \(\lambda_k=\cos(2\pi k/n)\) for \(k=1,\ldots,n-1\), excluding the constant mode. The elementary sums

\[
 \sum_{k=1}^{n-1}\csc^2\!\left(\frac{\pi k}{n}\right)=\frac{n^2-1}{3},
 \qquad
 \sum_{k=1}^{n-1}\csc^4\!\left(\frac{\pi k}{n}\right)=\frac{n^4+10n^2-11}{45}
\]

follow by comparing the constant and quadratic Laurent coefficients as \(x\to0\) in \(\sum_{k=0}^{n-1}\csc^2(x+\pi k/n)=n^2\csc^2(nx)\). Substitution into \(F'(1)\) gives

\[
 F'(1)=\frac14\sum\csc^4\!\left(\frac{\pi k}{n}\right)
 -\frac12\sum\csc^2\!\left(\frac{\pi k}{n}\right)
 =\frac{(n^2-1)(n^2-19)}{180}.
\]

Its sign is negative for \(n=3,4\) and positive for every \(n\geq5\). For \(C_5\) the nonconstant eigenvalues are \((\sqrt5-1)/4\) and \(-(\sqrt5+1)/4\), both doubled; substituting these into \(F'\) gives its only root in \((0,1)\) as \(z_*=2\sqrt5-4\), with the displayed exact minimum.

**5. Large-cycle asymptotics.** For cycles with \(n\geq5\), \(F'(0)=-1\) and \(F''(0)=n-2\), because \(\operatorname{tr}(P^2)=n/2\). Uniformly for \(0\leq z\leq 2/n\) and large \(n\), bounding the third derivative using \(|\lambda_k|\leq1\) gives

\[
 F'(z)=-1+(n-2)z+O(nz^2),\qquad
 F(z)=(n-1)-z+\frac{n-2}{2}z^2+O(nz^3).
\]

Since \(F'(0)<0<F'(2/n)\) for sufficiently large \(n\), the unique root lies in this interval and satisfies \(z_*=1/n+O(n^{-2})\). Inserting it in the second expansion proves the final asymptotic formulas.

## Verification

Run `python verify.py` with NumPy, SciPy and SymPy. The program (i) solves absorbing-chain linear systems independently of the renewal derivation; (ii) checks the targetwise resolvent formula and exact heterogeneity regret on multiple nonuniform relocation laws and cycles; (iii) independently checks the cycle threshold polynomial and fifth-cycle radical, and (iv) checks the large-cycle asymptotic numerically. These tests are finite consistency checks; the general result for infinitely many graphs and cycle sizes is established by the analytical proof above.

## Relationship to prior work

González, Riascos and Boyer (2021, arXiv:2104.00727) develop multiple-node resetting and global transport formulas, including the uniform Google-like strategy. Riascos, Boyer and Mateos (2021, arXiv:2110.15437) optimize the resetting probability for a fixed starting/reset node and a fixed target, including ring examples. Michelitsch, D'Onofrio, Polito and Riascos (2024, arXiv:2409.08394) develop a broad finite-network renewal/first-hitting framework, including multiple resetting nodes and target sets, and consider the stationary-distribution-weighted Kemeny functional. The resolvent, renewal, spectral trace, Kemeny identities, the spectral formula for the uniform relocation strategy, and the strict convexity/derivative rate criterion are pre-existing results (in particular, the explicit convexity calculation and rate condition appear in arXiv:2409.08394, Eq. (52) and its surrounding discussion). They serve as premises, **not as originality claims**. The specific statement assessed here is the **joint** minimax and uniform-unknown-target mean optimization over arbitrary relocation laws, its exact nonuniformity penalty, and the sharp all-cycle rate threshold. In particular, uniform-target weighting must not be replaced by reset-chain stationary weighting when \(\rho\) is nonuniform.

## Limitations

The graph is finite, undirected, connected, loopless and vertex-transitive; an asymmetric or inhomogeneous network may favor a nonuniform reset law. The time-zero detection convention matters when comparing other first-passage definitions. The result optimizes geometric resetting over independent time-homogeneous relocation draws and does not compare arbitrary renewal clocks, adaptive search, target priors other than uniform, or resetting constrained to a subset of vertices. The asymptotic optimum is for the cycle family only; a general graph-size asymptotic is not asserted. An equivalent formulation in prior graph-search or Kemeny-optimization literature may exist despite the explicit comparisons below.

## References

1. F. H. González, A. P. Riascos and D. Boyer, *Diffusive transport on networks with stochastic resetting to multiple nodes*, arXiv:2104.00727 (first posted 2021-04-01), https://arxiv.org/abs/2104.00727.
2. A. P. Riascos, D. Boyer and J. L. Mateos, *Discrete-time random walks and Lévy flights on arbitrary networks: when resetting becomes advantageous?*, arXiv:2110.15437 (first posted 2021-10-28), https://arxiv.org/abs/2110.15437.
3. T. M. Michelitsch, G. D'Onofrio, F. Polito and A. P. Riascos, *Random walks with stochastic resetting in complex networks: a discrete time approach*, arXiv:2409.08394 (first posted 2024-09-12), https://arxiv.org/abs/2409.08394.
