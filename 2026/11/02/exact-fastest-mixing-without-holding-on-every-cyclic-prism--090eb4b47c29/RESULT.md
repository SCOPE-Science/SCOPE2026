# Exact fastest mixing without holding on every cyclic prism

## Finding

Let \(n\ge3\) and let \(C_n\square K_2\) be the two-layer cyclic prism with \(2n\) vertices. Among **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices whose diagonal is zero and whose nonzero off-diagonal entries are restricted to edges of this prism, minimize the second-largest eigenvalue modulus \(\mu(P)=\|P-J/(2n)\|_2\), where \(J\) is the all-ones matrix. Then
\[
\boxed{\mu_*^{\mathrm{no\ hold}}(n)=\begin{cases}1,&n\text{ even},\\(4-\varepsilon_n)/(4+\varepsilon_n),&n\text{ odd},\end{cases}\qquad \varepsilon_n=2-2\cos(\pi/n).}
\]
For odd \(n\), the unique minimizer within the rotation-, reflection-, and layer-swap-invariant family assigns probability \(q_n=2/(4+\varepsilon_n)\) to **each** of the two cycle neighbors, probability \(p_n=\varepsilon_n/(4+\varepsilon_n)\) to the rung neighbor, and zero holding probability. In particular \(\mu_*<1\) for odd \(n\), whereas on even prisms no loopless symmetric walk mixes, regardless of edge probabilities. For odd \(n\to\infty\),
\[
1-\mu_*^{\mathrm{no\ hold}}(n)=\frac{\pi^2}{2n^2}+O(n^{-4}).
\]
This spectral gap is asymptotically one quarter of the unrestricted-with-holding optimum on the same graph. No global uniqueness is asserted outside the invariant class.

## Assumptions and scope

The graph has vertex set \(\mathbb Z/n\mathbb Z\times\{0,1\}\). The only permitted off-diagonal transitions connect consecutive vertices in a layer or corresponding vertices across layers; transition matrices are symmetric and stochastic, and **all** diagonal entries must vanish. Individual permitted edge transition probabilities may vary freely and may be zero. We use the asymptotic \(L^2\) convergence factor \(\mu\), not finite-time total variation mixing time. A walk on an even prism necessarily has period two, and the displayed value \(1\) includes disconnected feasible matrices.

## Proof

**Symmetry reduction over all edge weights.** Averaging an arbitrary feasible symmetric stochastic matrix over cyclic rotations, dihedral reflections, and layer exchange preserves stochasticity, nonnegativity, support, and the *zero diagonal*. Since \(\mu(P)=\|P-J/(2n)\|_2\) is convex and invariant under these permutations, averaging cannot increase \(\mu\). Thus a globally optimal value is attained in the two-parameter-invariant family. Write \(q\) for either individual rim-edge probability and \(p\) for each rung-edge probability. The zero-holding constraint forces \(2q+p=1\), or \(0\le q\le1/2\), \(p=1-2q\).

**Exact spectrum.** Let \(\lambda_k=2-2\cos(2\pi k/n)\) be the cycle Laplacian eigenvalues. The two layer-symmetry branches of the transition matrix have eigenvalues
\[
\theta_k^+=1-q\lambda_k,\qquad \theta_k^-=-1+q(4-\lambda_k),\qquad 0\le k<n.
\]
The constant symmetric-layer mode \(\theta_0^+=1\) is the stationary eigenvalue and is omitted from \(\mu\). The formula includes multiplicities and the degenerate endpoints.

**Even cycles.** When \(n\) is even, the prism is bipartite. For the sign vector \(s\) taking values \(\pm1\) on the two bipartition classes, zero diagonal and cross-class-only transitions give \(Ps=-s\) for every admissible stochastic matrix. Therefore \(\mu(P)=1\) always, and the even assertion follows.

**Odd cycles: global lower bound.** Suppose \(n\) is odd and put \(\Lambda=2+2\cos(\pi/n)\), so \(4-\Lambda=\varepsilon_n\). The antisymmetric zero-frequency and top-frequency modes give the lower bound
\[
\mu(P)\ge\max\{|4q-1|,\ 1-q\varepsilon_n\}\quad(0\le q\le1/2).
\]
(The second mode is negative because \(q\varepsilon_n<1\).) The two functions attain their smallest maximum uniquely at \(q_*=2/(4+\varepsilon_n)\), where \(4q_*-1=1-q_*\varepsilon_n=(4-\varepsilon_n)/(4+\varepsilon_n)\). This gives the universal lower bound within the invariant family, hence also for the unrestricted problem by the symmetry argument.

**Attainment against every other Fourier mode.** Set \(\delta=2-2\cos(2\pi/n)\). For odd \(n\ge3\) the positive nonconstant cycle eigenvalues lie in \([\delta,\Lambda]\), with \(\varepsilon_n\le\delta\le4\) and \(\varepsilon_n\le\Lambda\le4\). At \(q=q_*\), the symmetric branch \(1-q_*\lambda\) is decreasing, so its modulus over this interval is bounded by the absolute values at \(\delta\) and \(\Lambda\). The four inequalities \(\varepsilon_n\le\delta,\Lambda\le4\) imply
\[
-\mu_*\le1-q_*\Lambda\le1-q_*\delta\le\mu_*.
\]
The antisymmetric branch \(-1+q_*(4-\lambda)\) is also decreasing; its extreme values are exactly \(+\mu_*\) at \(\lambda=0\) and \(-\mu_*\) at \(\lambda=\Lambda\). Thus all other nonstationary eigenvalues have modulus at most \(\mu_*\), establishing attainment and uniqueness among invariant matrices.

**Asymptotic comparison.** Taylor expansion gives \(\varepsilon_n=\pi^2n^{-2}+O(n^{-4})\) and the displayed loopless gap. For the unrestricted problem with holding, the known all-prism optimum \(\mu_n=\Delta/(\Delta+2\delta)\), where \(\Delta=2[1-\cos(2\pi\lfloor n/2\rfloor/n)]\), has gap \(2\pi^2n^{-2}+O(n^{-4})\). Hence the ratio of the loopless gap to the unrestricted gap tends to \(1/4\).

## Verification

Run `python3 verify_loopless.py` with Python 3 standard library. It evaluates the entire Fourier spectrum at the proposed optimal probabilities for odd \(3\le n\le99\), verifies the spectral-bound identities, checks the bipartite \(-1\) eigenvalue for even \(n\le100\), and independently compares the claimed formula against one-dimensional interval-search values. The verifier is numerical corroboration; the preceding exact inequalities prove the theorem for every \(n\).

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduced the general fastest-mixing symmetric Markov-chain optimization, while Boyd, Diaconis, Parrilo and Xiao's complete 2007 preprint gives the permutation-averaging reduction and Cartesian-product spectral machinery. Their formulations **allow holding probabilities**, whereas this result imposes the structurally different zero-diagonal condition. An earlier exact optimum for cyclic prisms **with holding permitted** does not determine the optimum without holding: in the latter problem even prisms are necessarily periodic, and the odd-prism extremum has a different active spectral pair and a fourfold smaller asymptotic gap. No full-prism loopless formula was identified in the inspected primary sources or queried research records, but equivalent unindexed historical results remain possible.

## Limitations

The model is restricted to symmetric row-stochastic transitions, a uniform stationary distribution, and undirected cyclic prisms. Directed transitions, holding at even one vertex, arbitrary prescribed stationary distributions, and exact finite-time mixing measures are outside scope. Global optimal **value**, not global uniqueness of the matrix, is proved. The spectral certificate is analytic; finite numeric checks do not certify the infinite family. Independent mathematical audit has not been performed.

## References

- S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://doi.org/10.1137/S0036144503423264
- S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first public version 2007-09-06. https://arxiv.org/abs/0709.0955
