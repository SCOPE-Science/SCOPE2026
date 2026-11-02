# A seven-to-eight layer spectral transition in fastest non-holding walks on cyclic clique networks

## Finding

Consider the Cartesian-product graph \(G_{n,m}=C_n\mathbin{\square}K_m\), with \(n\geq3\) cycle positions and \(m\geq2\) vertices at each position. Among **all** symmetric stochastic transition matrices \(P\) supported on graph edges and satisfying \(P_{uu}=0\), the minimum of the second-largest eigenvalue modulus
\[\mu(P)=\max\{\lambda_2(P),-\lambda_{nm}(P)\}\]
has the exact classification below. In particular, no assumption of equal individual edge probabilities is needed to attain the global bound.

Set
\[\alpha_n=2\bigl(1-\cos(2\pi/n)\bigr),\qquad
\beta_n=2\Bigl(1-\cos\bigl(2\pi\lfloor n/2\rfloor/n\bigr)\Bigr),\qquad
\gamma_n=4-\beta_n.\]
A two-class transition matrix assigns probability \(a\) to each of the two cycle neighbors and probability \(b\) to each of the \(m-1\) different clique vertices at the same cycle position; it must satisfy \(2a+(m-1)b=1\).

**Two layers (\(m=2\)).** If \(n\) is even, the optimal value is \(\mu_*=1\), and in fact every feasible transition matrix has \(\mu=1\). If \(n\) is odd, the unique two-class minimizer and its value are
\[a_*={2\over4+\gamma_n},\qquad b_*={\gamma_n\over4+\gamma_n},\qquad
\mu_*={4-\gamma_n\over4+\gamma_n}.\]

**At least three layers (\(m\geq3\)).** Define
\[a_L={m-2\over(m-1)(\alpha_n+\beta_n)-2m},\qquad
a_H={m\over2m+(m-1)\alpha_n},\qquad a_* =\min\{a_L,a_H\}.\]
The minimum and a globally optimal two-class allocation are
\[\boxed{\mu_*=1-\alpha_n a_*,\qquad b_*={1-2a_*\over m-1}.}\]
Both classes have strictly positive transition probabilities. Except at \((n,m)=(3,3)\), this is the **unique two-class minimizer**; uniqueness is not asserted among all unrestricted optimizers. At \((3,3)\), every \(a\in[1/6,1/3]\), with \(b=(1-2a)/2\), is two-class optimal, with \(\mu_*=1/2\).

For even \(n\), always \(a_*=a_L\). For odd \(n\), the binding extremal eigenmode switches precisely when
\[\boxed{m\ \gtreqless\ 4\bigl(1+\cos(\pi/n)\bigr).}\]
Here \(a_L\) wins below the threshold and \(a_H\) wins above it (with equality at the threshold). Consequently, for **every odd \(n\geq5\)**, the switch lies between integer layer counts \(7\) and \(8\): \(m\leq7\) uses \(a_L\), while \(m\geq8\) uses \(a_H\). For \(n=3\), the exact crossover is \(m=6\).

For every fixed \(m\geq3\), the asymptotic spectral gap is
\[1-\mu_*(n,m)={2\pi^2\over n^2}+O_m(n^{-4}).\]
Compared with the uniform, no-holding nearest-neighbor walk (probability \(1/(m+1)\) on each incident edge), the ratio of spectral gaps tends to \((m+1)/2\). This gives a growing fixed-layer speedup as the number of clique layers increases.

## Assumptions and scope

Vertices are pairs \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(1\leq r\leq m\). Distinct pairs are adjacent if their cycle positions agree and their clique coordinates differ, or their clique coordinates agree and their cycle positions are adjacent in \(C_n\). The graph is simple; \(C_3=K_3\) has two distinct cycle neighbors per vertex. A feasible \(P\) is real symmetric, entrywise nonnegative, stochastic (\(P\mathbf1=\mathbf1\)), supported only on graph edges off-diagonal, and has exactly zero diagonal. Zero edge probabilities are permitted. \(\mu(P)\) is computed excluding the single stationary-direction eigenvector, even if eigenvalue one has further multiplicity. The result minimizes this spectral objective; it does not purport to give finite-time total-variation mixing constants or classify every nonsymmetric-in-edges minimizer.

## Proof

**1. Global reduction without imposing equal edges.** For a symmetric stochastic matrix, \(\mu(P)=\|P-J/(nm)\|_{2}\). This objective is convex and invariant under simultaneous permutation of rows and columns. Average an arbitrary feasible \(P\) over the subgroup \(D_n\times S_m\) acting by cycle symmetries and clique-coordinate permutations. Averaging preserves zero diagonals, nonnegativity, row sums, and edge support, and cannot increase \(\mu\). The subgroup has one orbit of cycle edges and one orbit of within-clique edges. Hence the global infimum equals the minimum among the two-class matrices. This proves existence of a globally optimal two-class matrix, **not** uniqueness over the unrestricted feasible set.

**2. Complete spectrum and exact three-line reduction.** Write \(\delta_k=2(1-\cos(2\pi k/n))\). Diagonalize the cycle adjacency by Fourier modes and the clique adjacency into its constant eigenvector and its \((m-1)\)-dimensional contrast space. The complete spectrum is
\[\{1-a\delta_k:0\leq k<n\}\ \cup\
\{1-mb-a\delta_k:0\leq k<n\}^{[m-1]},\]
where the exponent in brackets indicates multiplicity, not another numerical power. The stationary eigenvalue is the constant/clique-constant mode \(k=0\). The largest remaining eigenvalue is \(\max\{1-\alpha_n a,1-mb\}\); the smallest is \(1-mb-\beta_n a\), since the clique-contrast branch lies below the constant branch. Substituting \(b=(1-2a)/(m-1)\) gives, **for every** \(0\leq a\leq1/2\),
\[\mu(a)=\max\left\{\underbrace{1-\alpha_n a}_{L(a)},\quad
\underbrace{{-1+2ma\over m-1}}_{H(a)},\quad
\underbrace{{1\over m-1}+a\left(\beta_n-{2m\over m-1}\right)}_{U(a)}\right\}.\]
This formula includes all negative eigenvalues through the final term; no numerical spectrum truncation occurs.

**3. Two layers.** For \(m=2\), \(U(a)=1-\gamma_n a\). When \(n\) is even, \(\beta_n=4\) and \(U=1\), which also reflects the graph's bipartiteness: every zero-holding transition matrix has eigenvalue \(-1\). When \(n\) is odd, \(\gamma_n>0\), and \(\alpha_n>\gamma_n\) since \(\cos(2\pi/n)<\cos(\pi/n)\). Therefore \(L\leq U\), and \(\mu(a)=\max\{1-\gamma_n a,4a-1\}\). The decreasing and increasing terms meet exactly at \(a_*=2/(4+\gamma_n)\); this proves the stated formulas and unique two-class minimizer.

**4. At least three layers.** For \(n\geq3\), \(\beta_n\geq3\), while \(2m/(m-1)\leq3\) for \(m\geq3\). Thus \(L\) is strictly decreasing, \(H\) is strictly increasing, and \(U\) is nondecreasing, with \(U\) constant **only** for \((n,m)=(3,3)\). Initially \(L(0)=1\) strictly exceeds \(H(0),U(0)\). The first intersections \(L=U\) and \(L=H\) occur at \(a_L\) and \(a_H\), respectively, by direct algebra. Since \(\alpha_n+\beta_n>4\), both intersections lie in \((0,1/2)\). Consequently the pointwise maximum is minimized at the first intersection \(a_* =\min\{a_L,a_H\}\), except that when \(U\) is constant it may have a flat minimizing interval. At \((3,3)\), direct substitution gives \(\mu(a)=\max\{1-3a,3a-1/2,1/2\}\), so precisely \([1/6,1/3]\) is optimal. In every other case both competing upper lines rise strictly beyond the first intersection, implying uniqueness within the two-class family.

**5. Sharp layer transition.** Cross-multiply the positive denominators: \(a_H\leq a_L\) if and only if \(m(4-\beta_n)\geq2\alpha_n\). For even \(n\), \(\beta_n=4\), so this cannot hold. For odd \(n\), put \(\theta=\pi/n\). Then \(4-\beta_n=2(1-\cos\theta)\), while \(\alpha_n=2(1-\cos2\theta)\). Hence
\[{2\alpha_n\over4-\beta_n}=4(1+\cos\theta).\]
For odd \(n\geq5\), this lies strictly between seven and eight, giving the claimed universal integer transition; for \(n=3\), it equals six. At the crossing both positive- and negative-branch constraints can be active.

**6. Comparison and asymptotics.** As \(n\to\infty\) with fixed \(m\geq3\), \(\alpha_n=4\pi^2/n^2+O(n^{-4})\), \(\beta_n=4+O(n^{-2})\), and both \(a_L,a_H\to1/2\) with \(a_*=1/2+O_m(n^{-2})\). This proves the gap expansion. For the simple walk \(a=b=1/(m+1)\), the cycle-constant family has nontrivial largest eigenvalue \(1-\alpha_n/(m+1)\), which dominates in modulus for all sufficiently large \(n\) at fixed \(m\). Therefore its spectral gap is asymptotic to \(4\pi^2/((m+1)n^2)\), proving the stated improvement ratio.

## Verification

The accompanying `verify_cyclic_layers.py` uses NumPy and SciPy. Run `python verify_cyclic_layers.py` from the package directory. It reproduced **1,716** independent bounded one-variable numerical minimizations against the analytic candidates (all \(3\leq n\leq80\) and \(2\leq m\leq23\)), **48** direct full-matrix eigenvalue comparisons (\(3\leq n\leq10\), \(2\leq m\leq7\)), and **225** feasible asymmetric zero-diagonal perturbations using the nullspace of the vertex-edge incidence constraint. It checks the exact rational special values \((n,m)=(3,6)\) and the full two-class plateau at \((3,3)\). All checks passed in the recorded execution.

These finite calculations corroborate the matrix and branch formulas. The infinite-domain result and unrestricted global optimum follow from the exact Fourier spectrum, convex averaging, and piecewise-affine minimax proof; the experiments alone would not suffice.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) formulate symmetric fastest-mixing Markov chains as convex eigenvalue minimization; the paper explicitly allows self-loops. Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955v1, 2007), especially Sections 2.2 and 3.2, prove graph-automorphism reduction and discuss Cartesian-product Laplacian spectra, including cycles and hypercubes. Those general methods are foundational premises here, **not** new claims. However, the inspected product examples and formulas do not state the zero-holding \(C_n\mathbin{\square}K_m\) classification, the complete low/high mode crossover, or its odd-cycle seven-to-eight boundary.

Reber (2018), Section 4, gives coupling bounds for a prescribed **lazy** random walk on the two-layer prism, not unrestricted fastest no-holding weights. Jafarizadeh's work on clique lifts (original journal work predating its 2025 arXiv upload) uses complete bipartite connections between adjacent lifted cliques; those graphs differ from the **matching** connections between adjacent cliques here. Jafarizadeh (2026) gives general association-scheme/LP design methods and Hamming-scheme examples, but the examined full-text examples do not give this two-parameter zero-holding cycle-by-clique formula. General-purpose LP/SDP solvability is not treated as an explicit evaluation of this parameter family. Literature searches and mathematical research-record comparisons did not identify an equivalent or strictly stronger specific classification. This is a best-knowledge originality assessment, not a proof of global priority.

## Limitations

The theorem is for symmetric stochastic matrices with exactly zero holding probability, uniform stationary distribution, and the specified Cartesian-product graph. It does not cover asymmetric chains, biased stationary laws, arbitrary graph products, or the unconstrained-holding fastest-mixing problem. Only the two-class minimizer is classified uniquely where asserted. The mathematical structure and the exact seven-to-eight transition are established analytically; no independent external mathematical audit has been performed. Earlier specialized literature may contain equivalent results not located in the completed searches. The 2007 preprint has a verifiable arXiv public date of September 6, 2007; an earlier May 2007 technical-report month is known but no exact release day was established for it.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689, DOI:10.1137/S0036144503423264; full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (first submitted 2007-09-06), https://arxiv.org/html/0709.0955v1 .
3. J. M. Reber, *Mixing Times of Random Walks on Various Combinatorial Objects*, July 2018, Section 4, https://marshareb.github.io/files/writeup.pdf .
4. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, arXiv:2501.02421 (upload of earlier journal work), Section 3.1, https://arxiv.org/abs/2501.02421 .
5. S. Jafarizadeh, *Pareto–Optimal Design of Markov Chains on Networks Based on Association Schemes*, IEEE Access **14** (2026), 72346–72376, DOI:10.1109/ACCESS.2026.3680803; author full text: https://www.researchgate.net/publication/404746370_Pareto-Optimal_Design_of_Markov_Chains_on_Networks_Based_on_Association_Schemes .
