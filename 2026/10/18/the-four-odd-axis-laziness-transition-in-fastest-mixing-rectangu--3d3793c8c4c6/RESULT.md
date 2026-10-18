# The four-odd-axis laziness transition in fastest-mixing rectangular tori

## Finding

Let \(d\ge 2\) and let \(n_1,\ldots,n_d\ge3\) be arbitrary integers. On the Cartesian product of simple cycles \(G=\square_{i=1}^d C_{n_i}\), optimize the second-largest eigenvalue modulus (SLEM) over **all** real symmetric entrywise-nonnegative row-stochastic matrices whose off-diagonal support is contained in graph edges; self-loops are permitted. The optimization places no a priori equality constraint on different edges.

Set
\[
\delta_i=2-2\cos(2\pi/n_i),\qquad
\Delta_i=2-2\cos(2\pi\lfloor n_i/2\rfloor/n_i),
\]
\[
S=\sum_{i=1}^d\delta_i^{-1},\quad
R=\sum_{i=1}^d\frac{\Delta_i}{\delta_i},\quad
t_* =\min\left\{\frac1{2S},\frac2{1+R}\right\}.
\]
The **globally minimum** SLEM is \(\mu_*=1-t_*\). It is attained by assigning the same probability \(w_i=t_*/\delta_i\) to each of the two nearest-neighbor moves in coordinate direction \(i\), and holding probability \(h_*=1-2t_*S\) at every vertex. This is the unique optimizer in the class of direction-invariant kernels; uniqueness among every unrestricted, possibly spatially varying kernel is *not* asserted.

The holding probability exhibits an exact combinatorial transition. Let \(o\) be the number of odd side lengths among the \(n_i\). Then
\[
h_*=0\quad\Longleftrightarrow\quad
 o\ge4\ \text{or}\ \bigl(o=3\text{ and all three odd lengths equal }3\bigr).
\]
Thus, for example, a six-factor torus with odd lengths \(3,5,7\) and three even lengths has positive optimal holding, while a four-factor torus with odd lengths \(3,5,7,9\) has zero optimal holding. No restriction is imposed on the even side lengths.

If the dimension \(d\ge2\) and \(n_2,\ldots,n_d\) are fixed while \(n_1=N\to\infty\), then
\[
1-\mu_* = \frac{2\pi^2}{N^2}+O(N^{-4}),\qquad
w_1=\frac12+O(N^{-2}),\qquad
w_i=\frac{2\pi^2}{\delta_i N^2}+O(N^{-4})\quad(i\ge2).
\]
Among kernels forced to use a single common edge probability in every direction, the best SLEM has gap \(1-\mu_{\mathrm{common}}=2\pi^2/(dN^2)+O(N^{-4})\). Hence the ratio of the optimal spectral gap to that restricted spectral gap tends to exactly \(d\).

## Assumptions and scope

The cycles are simple undirected graphs on at least three vertices. The Cartesian product has vertex set \(\prod_i\mathbb Z/n_i\mathbb Z\). Each vertex has exactly \(2d\) distinct neighbors, namely one step in either direction along each coordinate. Matrices are real, symmetric, nonnegative, stochastic, and may have diagonal holding mass; the edge-transition probabilities may initially vary independently across space. The objective is \(\mu(P)=\lVert P-\mathbf{1}\mathbf{1}^\top/|V|\rVert_2\), not total-variation mixing time, resistance, or a nonreversible mixing criterion.

All formulas hold for every integer dimension and every list of allowed cycle lengths, including repeated or mixed odd/even lengths. The asymptotic keeps \(d\) and the shorter side lengths fixed. The uniqueness statement is confined to direction-invariant kernels.

## Proof

**1. Symmetrization from unrestricted kernels.** Let \(J=\mathbf{1}\mathbf{1}^\top/|V|\). Since the operator norm is convex and \(J\) is invariant under vertex permutations, \(\mu(P)=\|P-J\|_2\) is convex and invariant under graph automorphisms. Average any feasible kernel over coordinate translations and independent reflections. This preserves feasibility and does not increase \(\mu\). Translations make holding probabilities independent of position; reflection in each coordinate identifies its two directed nearest-neighbor edges. Thus a global optimum exists in the direction-invariant family
\[
P(w)=I-\sum_{i=1}^d w_iL_i,\qquad w_i\ge0,\quad 2\sum_i w_i\le1,
\]
where \(L_i\) is the cycle Laplacian acting in coordinate \(i\).

**2. Exact spectral reduction.** Fourier characters indexed by \(k_i\in\{0,\ldots,n_i-1\}\) diagonalize every \(L_i\). Their eigenvalues in \(P(w)\) are
\[
1-\sum_{i=1}^d w_i\left[2-2\cos(2\pi k_i/n_i)\right].
\]
The largest eigenvalue other than the constant mode is \(1-t\), with \(t=\min_i w_i\delta_i\); it is attained by activating a first nonzero frequency in a coordinate attaining the minimum. The least eigenvalue is \(1-\sum_i w_i\Delta_i\), attained by maximizing the Laplacian frequency independently in every coordinate. Therefore, exactly,
\[
\mu(P(w))=\max\left\{1-t,\ \sum_iw_i\Delta_i-1\right\}.
\]

**3. Sharp scalar lower bound and attainment.** Since \(w_i\ge t/\delta_i\), feasibility implies \(0\le t\le(2S)^{-1}\) and \(\sum_iw_i\Delta_i\ge tR\). Every feasible direction-invariant kernel therefore obeys
\[
\mu(P(w))\ge f(t):=\max\{1-t,Rt-1\},\qquad0\le t\le(2S)^{-1}.
\]
This piecewise-linear function decreases up to \(2/(1+R)\) and increases afterwards, so the best lower bound is attained at \(t_*\). Choose \(w_i=t_*/\delta_i\). Its row-sum condition follows from \(t_*\le(2S)^{-1}\). If \(t_*=2/(1+R)\), its two spectral endpoints coincide at \(1-t_*\). If \(t_*=(2S)^{-1}\), then \(R+1\le4S\), so the negative endpoint is no greater in modulus than the positive one. In both cases \(\mu(P(w))=1-t_*\), proving unrestricted global optimality by step 1. In the first regime, equality at the negative endpoint forces every \(w_i=t_*/\delta_i\); in the second regime, the saturated probability budget forces the same equalities. Hence the direction-invariant optimizer is unique.

**4. Exact parity threshold.** Write \(K=4S-R=\sum_i(4-\Delta_i)/\delta_i\). The crossing point is feasible precisely when \(K\le1\), and the constructed holding probability is strictly positive precisely when \(K<1\). If \(n_i\) is even, \(\Delta_i=4\) and its contribution is zero. If \(n_i\) is odd, elementary half-angle identities give
\[
\frac{4-\Delta_i}{\delta_i}=
\frac1{4\cos^2(\pi/(2n_i))}\in(1/4,1/3],
\]
with equality at the upper endpoint only for \(n_i=3\). Four or more odd factors therefore make \(K>1\); at most two give \(K<1\); three give \(K\le1\), with equality only when all three lengths are \(3\). This proves the stated if-and-only-if condition.

**5. Long-thin asymptotics.** For \(N=n_1\to\infty\), the first factor has \(\delta_1=4\pi^2N^{-2}+O(N^{-4})\), \(\Delta_1=4+O(N^{-2})\); all other terms are fixed. Hence \(S=N^2/(4\pi^2)+O(1)\), \(R=N^2/\pi^2+O(1)\), so both candidates defining \(t_*\) equal \(2\pi^2N^{-2}+O(N^{-4})\). This yields the weights and SLEM gap claimed above. If all edges are constrained to share one weight \(\alpha\), their optimal value is attained at
\[
\alpha_{\mathrm{common}}=
\min\left\{\frac1{2d},\frac2{\delta_1+\sum_i\Delta_i}\right\},
\]
for all sufficiently large \(N\), since the smallest nonzero product-Laplacian eigenvalue is then \(\delta_1\). As \(\sum_i\Delta_i\le4d\) and \(\delta_1\to0\), this weight tends to \(1/(2d)\). Its spectral gap is \(2\pi^2/(dN^2)+O(N^{-4})\). Taking the ratio gives \(d\).

## Verification

The standalone `verify.py` script reproduces the formulas using independently enumerated full Fourier-mode spectra on sixteen families, checks the holding transition and its exact algebraic boundary cases, compares the proposed optimum with deterministic random feasible direction-weight allocations, and checks the long-thin asymptotic and common-weight comparison. It uses only the Python standard library; run `python verify.py`. Its successful run returned `verification_pass: 2993 assertions`. The script is finite corroboration, not a proof of the universal quantified theorem. The proof above is analytic and covers all integers \(d\ge2\) and \(n_i\ge3\).

## Relationship to prior work

Boyd, Diaconis, and Xiao formulated symmetric fastest-mixing Markov chains as a convex spectral optimization problem. Boyd, Diaconis, Parrilo, and Xiao (arXiv:0709.0955v1; SIAM J. Optim., 2009) established the automorphism-averaging theorem, exact formulas for edge-transitive graphs, and in section 3.2 the equal-side two-dimensional torus \(C_n\square C_n\). Those facts are background, not claimed as new. In particular, when all cycle factors are identical, their edge-transitive theorem already covers the optimal common weight.

The assessed addition is the explicit **multiple independent edge-orbit** minimax classification for arbitrary rectangular high-dimensional products of possibly unequal cycles, together with the exact parity-count holding criterion and dimension-fold long-thin spectral-gap improvement. The previously published edge-transitive single-weight formula does not by itself settle the unequal-factor optimization because such products generally have distinct directional edge orbits. Published Fourier-product formulas supply the spectrum but not the anisotropic probability allocation or its parity threshold. Another relevant primary source on geometric random graphs and toroidal grids establishes mixing-time scaling for a different neighborhood graph and does not provide the above exact finite-graph classification.

## Limitations

The claim is about symmetric transition matrices and spectral SLEM. It neither optimizes nonreversible kernels nor supplies exact total-variation mixing times. All global claims refer to optimal **value** and existence of the specified direction-invariant optimizer; uniqueness among all spatially varying optimal kernels has not been established. Equal-factor edge-transitive specializations are part of published work and are not presented as novel. Potential overlooked sources addressing non-edge-transitive Cartesian products are a residual originality risk. The asymptotic comparison is with the best uniform **edge-probability** restriction, not with all possible nonreversible strategies or richer moves.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: `10.1137/S0036144503423264` (full text: `https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf`).
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819. First arXiv submission 2007-09-06, `arXiv:0709.0955v1`; DOI: `10.1137/070689413` (full text: `https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf`).
3. S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah, *Mixing Times for Random Walks on Geometric Random Graphs*, full text `https://web.stanford.edu/~balaji/papers/05mixingtimes.pdf`, section 3 (different graph neighborhood and mixing-time bounds).
