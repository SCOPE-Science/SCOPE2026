# Sharp holding transitions in fastest mixing on clique-layer products

## Finding

Let \(H\) be a finite, simple, connected, \(d\)-regular graph with at least two vertices, both vertex-transitive and edge-transitive. For every integer \(s\ge2\), consider the Cartesian product \(G=H\square K_s\). Define the positive nonzero spectral endpoints of the combinatorial Laplacian of \(H\) by
\[
\alpha=\lambda_2(L_H)>0,\qquad \beta=\lambda_{\max}(L_H),\qquad
M=\max\left\{\beta+2\alpha,\ 2d+\frac{2\alpha(s-1)}s\right\}.
\]
Among **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices supported on the edges and diagonal of \(G\), the exact minimum of the second-largest eigenvalue modulus is
\[
\boxed{\mu_*(G)=1-\frac{2\alpha}{M}.}
\]
One global minimizer, unique among transition matrices constant on the two natural edge orbits, puts probability
\[
\boxed{x_* = \frac2M\quad\text{on each }H\text{-edge},\qquad
 y_* = \frac{2\alpha}{sM}\quad\text{on each }K_s\text{-fiber edge}.}
\]
Its diagonal holding probability is
\[
 h_*=1-\frac{2d+2\alpha(s-1)/s}{M}.
\]
This number is **strictly positive** exactly when \(\beta+2\alpha/s>2d\); it vanishes when \(\beta+2\alpha/s\le2d\). Uniqueness of arbitrary nonsymmetric-orbit optimizers is **not** asserted.

For the Johnson base \(H=J(n,2)\), with \(n\ge4\) and adjacency defined by one-element intersection of distinct two-subsets, the exact specialization is
\[
\alpha=n,\quad \beta=2n-2,\quad d=2n-4,\quad
M=\max\left\{4n-2,\ 6n-8-\frac{2n}s\right\}.
\]
In particular its invariant fastest chain holds with positive probability if and only if \(s(n-3)<n\): for \(n=4\) exactly \(s=2,3\); for \(n=5\) exactly \(s=2\); for \(n\ge6\) none. At equality \(s(n-3)=n\) the holding probability is zero. The SLEM remains constant as \(s\) varies while the first expression for \(M\) dominates and increases strictly with \(s\) thereafter.

## Assumptions and scope

A permitted transition matrix \(P\) is real, symmetric, nonnegative entrywise, has every row sum one, and has \(P_{uv}=0\) for distinct nonadjacent vertices. Diagonal holding is allowed and not prescribed. The objective is \(\mu(P)=\max\{|\lambda|: \lambda\in\sigma(P),\ \lambda\ne1\text{ in the constant-mode listing}\}\), equivalently \(\|P-\mathbf1\mathbf1^{\mathsf T}/|V(G)|\|_2\); this definition remains valid with repeated eigenvalue one. The graph \(H\) has unit unweighted edges and both vertex and edge transitivity. No claim is made for general nontransitive bases, continuous-time mixing, nonreversible chains, or mixing-time cutoffs.

## Proof

**1. Unrestricted optimization reduces to two variables.** The SLEM is the operator norm \(\|P-\mathbf1\mathbf1^{\mathsf T}/|V(G)|\|_2\), hence a convex function of \(P\). Averaging an arbitrary optimum over the product of the automorphism group of \(H\) and the full symmetric group acting on each fiber coordinate cannot increase SLEM and preserves stochasticity and support. Vertex transitivity, edge transitivity, and the transitive action of \(S_s\) on unordered fiber pairs leave two edge orbits: original \(H\)-edges in each layer and edges inside each \(K_s\) fiber. Thus an optimum exists in the form
\[
P(x,y)=I-x(L_H\otimes I_s)-y(I_{|V(H)|}\otimes L_{K_s}),\qquad
 x,y\ge0,\quad dx+(s-1)y\le1.
\]
Here the last inequality exactly enforces nonnegative diagonal entries.

**2. Exact spectral reduction.** The clique Laplacian has eigenvalues \(0\) (once) and \(s\) (multiplicity \(s-1\)). The product Laplacians commute, so every nonconstant eigenvalue of \(P(x,y)\) is one of \(1-x\lambda\) for \(\lambda\in\sigma(L_H)\setminus\{0\}\), \(1-sy\), or \(1-x\lambda-sy\) for positive \(\lambda\in\sigma(L_H)\). Since \(x,y\ge0\), the largest nonconstant eigenvalue is \(\max\{1-\alpha x,1-sy\}\), and the smallest is \(1-\beta x-sy\). Consequently
\[
\mu(x,y)=\max\{1-\alpha x,\ 1-sy,\ \beta x+sy-1\}.
\]
No other spectral mode can dominate because the spectrum lies between the displayed endpoints.

**3. Sharp minimax lower bounds.** If \(u=\mu(x,y)\), the first two displayed terms require \(x\ge(1-u)/\alpha\) and \(y\ge(1-u)/s\). Substituting into the third gives
\[
 u\ge\frac{\beta}{\beta+2\alpha}
 =1-\frac{2\alpha}{\beta+2\alpha}.
\]
Substituting into the stochastic row-budget inequality gives
\[
 u\ge1-\frac{2\alpha}{2d+2\alpha(s-1)/s}.
\]
Their maximum is exactly \(1-2\alpha/M\). The proposed pair \(x_*=2/M\), \(y_*=2\alpha/(sM)\) is feasible by the definition of \(M\); both slow-mode upper constraints attain \(1-2\alpha/M\), and the last extremal eigenvalue does not exceed this modulus because \(M\ge\beta+2\alpha\). It therefore attains the lower bound.

**4. Uniqueness in the invariant class and the holding frontier.** For an invariant minimizer with objective \(u=1-2\alpha/M\), the slow-mode inequalities force \(x\ge x_*\) and \(y\ge y_*\). If \(M=2d+2\alpha(s-1)/s\), the budget is tight at \((x_*,y_*)\), forbidding either strict increase. If \(M=\beta+2\alpha\), the negative-endpoint constraint is tight, likewise forbidding any strict increase. Hence the invariant optimizer is unique. The formula for \(h_*\) shows \(h_*>0\) exactly when \(\beta+2\alpha/s>2d\).

**5. Johnson specialization.** For \(n\ge4\), \(J(n,2)\) is \(2(n-2)\)-regular. Its combinatorial Laplacian eigenvalues are \(0\), \(n\), and \(2n-2\). The latter follows, for example, by decomposing functions on two-subsets into constant functions, vertex-induced mean-zero functions, and their orthogonal complement, with adjacency eigenvalues \(2(n-2)\), \(n-4\), and \(-2\), respectively. Substitution yields the displayed \(M\). The inequality \(\beta+2\alpha/s>2d\) rearranges without approximation to \(s(n-3)<n\). At fixed \(n\), the second branch of \(M\) increases strictly with \(s\) (viewed as a positive real parameter), establishing the plateau-to-growth transition.

## Verification

The included standalone program `fmmc_clique_layers_verify.py` independently constructs weighted transition matrices and checks full eigenvalue spectra and stochasticity, solves a separate three-variable linear program, tests asymmetric feasible perturbations, and evaluates the Johnson identities in exact rational arithmetic. In one replay it passed 95 full-matrix spectral tests, 126 independent linear programs, 504 asymmetric feasible perturbation comparisons, 91 cycle-parity cross-checks, 20 Johnson spectrum checks, and 90 exact-rational evaluations. The proof, not the finite numerical tests, establishes the stated result for all admissible graphs and integers.

## Relationship to prior work

Boyd, Diaconis and Xiao introduced the symmetric fastest-mixing Markov-chain convex program and symmetry averaging [1]. Boyd, Diaconis, Parrilo and Xiao developed graph-automorphism reductions and Cartesian-product Laplacian spectra, and treated edge-transitive graph families and equal-factor Hamming graphs [2]. The present calculation allows two independently tunable edge orbits on \(H\square K_s\), establishes an explicit all-base minimax formula with a sharp stochastic-row-budget frontier, and resolves the corresponding two-parameter Johnson-product family. Earlier results for zero-diagonal cyclic clique products concern a different feasible class and do not determine the holding-allowed optimum for all vertex-and-edge-transitive bases.

## Limitations

The theorem guarantees a globally optimal orbit-invariant transition matrix, not uniqueness among all unrestricted optimizers. It assumes unweighted, simple, connected, vertex- and edge-transitive base graphs and unconstrained symmetric holding probabilities. Literature searches and inspection of primary sources cannot exclude specialized unindexed equivalent results. Exact SLEM controls the asymptotic eigenvalue contraction, not every finite-time mixing functional.

## References

[1] S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: https://doi.org/10.1137/S0036144503423264 ; openly accessible author copy: https://www-leland.stanford.edu/~boyd/papers/pdf/fmmc.pdf . Published electronically 2004-10-29.

[2] S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819. First arXiv posting 2007-09-06, https://arxiv.org/abs/0709.0955 ; author copy: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf .
