# Exact two-round matching-averaging spectrum and logarithmic rank loss

## Finding

Consider two independent synchronous rounds in which the \(2m\) agents are independently paired uniformly at random, and both agents of every pair replace their current values by their arithmetic mean. Fix the first matching \(A\) by relabeling, let \(B\) be uniform among all perfect matchings, and write \(T=P_AP_B\) for the product of the two averaging projections. The conclusions hold for every integer \(m\geq1\), followed by the asymptotic regime \(m\to\infty\).

Superpose the matchings and write \(\ell_1,\ldots,\ell_K\) for the numbers of first-matching pairs in its alternating-cycle components. Thus \(\sum_a\ell_a=m\), with a coincident pair counted as a component of size one, and a doubled pair of cross-edges as a component of size two. The complete list of \(2m\) singular values of \(T\), including multiplicities, is

\[
\{0\}^{m}\ \mathbin{\uplus}\
\mathop{\biguplus}_{a=1}^{K}
\bigl\{\lvert\cos(\pi j/\ell_a)\rvert:0\leq j<\ell_a\bigr\}.
\]

In particular, if \(Z_m=\#\{a:2\mid\ell_a\}\), then

\[
\operatorname{rank}(T)=m-Z_m,
\qquad
\operatorname{rank}(T\vert_{\mathbf 1^\perp})=m-1-Z_m.
\]

The exact probability-generating function of the **additional** rank loss is

\[
\mathbb E[s^{Z_m}]=
\frac{[z^m](1-z)^{-(1+s)/4}(1+z)^{(1-s)/4}}
{[z^m](1-z)^{-1/2}}.
\]

As \(m\to\infty\),

\[
\frac{Z_m-\tfrac14\log m}{\sqrt{\tfrac14\log m}}
\ \Longrightarrow\ N(0,1),
\qquad
\Pr(Z_m=0)\sim
\frac{2^{1/4}\sqrt\pi}{\Gamma(1/4)}m^{-1/4}.
\]

The leading constant in the zero-excess probability is approximately \(0.5813683170\). There is also a sharp spectral-measure description: let

\[
\rho_m=\frac1m\sum_{a=1}^{K}\sum_{j=0}^{\ell_a-1}
\delta_{\lvert\cos(\pi j/\ell_a)\rvert},
\qquad
\rho(dx)=\frac{2\,\mathbf1_{(0,1)}(x)}{\pi\sqrt{1-x^2}}\,dx.
\]

For every realized matching pair,

\[
W_1(\rho_m,\rho)\leq\frac{\pi K}{2m},
\qquad
\mathbb E W_1(\rho_m,\rho)
\leq\frac{\pi}{2m}\sum_{j=0}^{m-1}\frac1{2j+1}
=O\bigl((\log m)/m\bigr).
\]

Hence the empirical distribution of all \(2m\) singular values of \(T\) converges in expected \(W_1\) to \(\tfrac12\delta_0+\tfrac12\rho\).

## Assumptions and scope

Every matching is a partition of the labeled set \(\{1,\ldots,2m\}\) into \(m\) unordered pairs, sampled uniformly from the \((2m-1)!!\) possibilities, independently between rounds. The averaging projection \(P_A\) is the real symmetric matrix with a \(2\times2\) block of four entries equal to \(1/2\) for every pair of \(A\), and zero otherwise. A fixed first matching is sufficient because the law is invariant under relabeling. Singular values are counted with their full multiplicities. The rank on \(\mathbf1^\perp\) concerns the invariant zero-sum subspace, not any nonlinear consensus metric. The reference measure \(\rho\) is the law of \(\lvert\cos(\pi U)\rvert\) for uniform \(U\in[0,1]\).

## Proof

**Step 1: spectral reduction to alternating cycles.** For any matching \(A\), let \(E_A\) be the \(2m\times m\) matrix whose columns are the normalized vectors \((e_u+e_v)/\sqrt2\) for the pairs \(\{u,v\}\in A\). Then \(E_A^TE_A=I_m\) and \(P_A=E_AE_A^T\); similarly for \(B\). Consequently

\[
T=E_A C E_B^T,\qquad C=E_A^TE_B,
\]

and, because both outside factors are isometries, the singular values of \(T\) comprise the \(m\) singular values of \(C\) and another \(m\) zeros. The entry of \(C\) for two pairs is one half the number of agents common to them. Contract each pair of \(A\) into one vertex. The pairs of \(B\) give a degree-two multigraph, permitting loops and double edges, so every connected component is a cycle. After independent row and column relabelings in a component of length \(\ell\), its block of \(C\) is \((I_\ell+S_\ell)/2\), where \(S_\ell\) is the cyclic shift. The Fourier eigenvalues are \((1+e^{2\pi i j/\ell})/2\), and their absolute values are \(\lvert\cos(\pi j/\ell)\rvert\). The value zero occurs exactly once for each even \(\ell\). This proves the full singular spectrum and the first rank equality. Both projections fix \(\mathbf1\), which spans one singular-value-one direction; its restriction to the orthogonal complement therefore has rank exactly one lower.

**Step 2: exact cycle law.** For \(\ell\) specified contracted vertices, the number of ways to join their \(2\ell\) labeled agents into one alternating connected component is \(2^{\ell-1}(\ell-1)!\). This can be seen by choosing an unoriented cyclic order and the two incident half-edges at each contracted vertex; the cases \(\ell=1,2\) yield respectively one loop and two cross-matchings. It follows from the labeled exponential formula that the weighted component-count generating function is

\[
\exp\left(\sum_{\ell\geq1}
\frac{2^{\ell-1}(\ell-1)!}{\ell!}z^\ell\right)
=\exp\left(\frac12\sum_{\ell\geq1}\frac{z^\ell}{\ell}\right)
=(1-z)^{-1/2}.
\]

After conditioning on the total number \(m\) of contracted vertices, the component sizes therefore have the Ewens partition law with parameter \(1/2\). Weighting precisely even component lengths by \(s\) yields

\[
\exp\left(\frac12\sum_{\ell\ \mathrm{odd}}\frac{z^\ell}{\ell}
+\frac{s}{2}\sum_{\ell\ \mathrm{even}}\frac{z^\ell}{\ell}\right)
=(1-z)^{-(1+s)/4}(1+z)^{(1-s)/4},
\]

and dividing its coefficient by the unweighted coefficient proves the exact generating function.

**Step 3: sharp rank-loss fluctuations and rare event.** Singularity analysis of the last generating function gives, uniformly for complex \(s\) in a small neighborhood of \(0\) or \(1\),

\[
\mathbb E[s^{Z_m}]
=\frac{2^{(1-s)/4}\Gamma(1/2)}{\Gamma((1+s)/4)}
 m^{(s-1)/4}(1+o(1)).
\]

Indeed, at \(z=1\) the first factor has algebraic exponent \((1+s)/4\) and the second tends to \(2^{(1-s)/4}\). The possible \(z=-1\) contribution is lower by a factor of order \(m^{-1/2}\) in these neighborhoods, so it does not alter the displayed leading term. With \(s=e^t\) near one, the logarithm of the moment-generating function is \(\tfrac14(e^t-1)\log m+O(1)\), with a locally analytic \(O(1)\) term. Evaluating at \(t=iu/\sqrt{(\log m)/4}\), centering by \((\log m)/4\), and expanding \(e^t\) gives characteristic functions converging to \(e^{-u^2/2}\). Lévy's continuity theorem proves the central limit theorem. Setting \(s=0\) in the same coefficient asymptotic gives the claimed positive constant and exponent for \(\Pr(Z_m=0)\). These conclusions are statements about the random excess rank deficiency, not about repeated applications of the same fixed pair of matchings.

**Step 4: limiting spectrum with a quantitative bound.** On each component, couple the uniform discrete grid measure on \(\{j/\ell:0\leq j<\ell\}\) to continuous uniform measure on \([0,1]\) by sampling within each interval \([j/\ell,(j+1)/\ell]\). The function \(u\mapsto\lvert\cos\pi u\rvert\) is \(\pi\)-Lipschitz, so the coupling cost on that component is at most \(\pi/(2\ell)\). Weighting by its fraction \(\ell/m\) of all contracted vertices and summing proves \(W_1(\rho_m,\rho)\leq\pi K/(2m)\). For Ewens parameter \(1/2\), differentiating the partition normalizer gives

\[
\mathbb EK=\sum_{j=0}^{m-1}\frac{1/2}{j+1/2}
=\sum_{j=0}^{m-1}\frac1{2j+1}.
\]

The expected Wasserstein bound and the full-spectrum limit follow at once. The density of the limiting continuous measure is the elementary push-forward of uniform measure by \(u\mapsto\lvert\cos\pi u\rvert\).

## Verification

The supplied standalone program `verify_two_round_matching.py` exhaustively enumerates all \((2m-1)!!\) second matchings for every \(1\leq m\leq6\), independently constructs the \(2m\times2m\) averaging products and computes their numerical singular values, and compares them against the exact component formula and predicted rank. It also checks exact rational coefficient distributions against exhaustive frequencies, and independently verifies the cycle-index recurrence through \(m=11\). It passed 124,975 assertions across 11,464 exhaustively examined perfect matchings. Use `python verify_two_round_matching.py` in an environment with NumPy. The asymptotic central limit theorem, rare-event constant, and Wasserstein bound are proved above, not certified by finite computations.

## Relationship to prior work

Chiclana's 2026 work introduces and analyzes the same synchronous random-group averaging model and proves Poisson occupancy and quantitative consensus estimates, including first- and second-moment identities. It does not state a full two-round singular-value decomposition or the additional rank-loss law. Lugo's 2009 study gives the foundational alternating-matching cycle structure and equivalent even-cycle permutation enumeration; that matching enumeration is prior work and is not presented as new here. The new synthesis assigns an exact spectrum to every matching component, derives the rank-loss distribution and its sharp zero-defect asymptotic, and gives an explicit expected spectral-measure convergence rate for two synchronous averaging rounds. General results on random products of consensus matrices concern different long-time quantities and do not, in the inspected statements, directly identify this finite-round spectrum.

## Limitations

The model is restricted to complete uniform random perfect matchings of even-sized populations, arithmetic pair averaging, and exactly two rounds. It does not establish comparable rank-loss distributions for larger groups, weighted updates, nonuniform matchings, or three or more rounds. The historical priority of the combined spectral/rank statement is not independently certified; a previously unnoticed implication of general results on random two-regular graphs or products of projections remains possible. The finite verifier uses floating-point singular values to test identities exhaustively at small sizes; it is supplementary to the analytical proof.

## References

- Rafael Chiclana, *Poisson occupancy of paths on permuted regular graphs*, arXiv:2610.14724v1 (first public October 10, 2026), https://arxiv.org/abs/2610.14724 . See the synchronous opinion-averaging model and Section 8.1.
- Michael Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604 (2009), https://arxiv.org/abs/0911.3604 . See Section 8, particularly Propositions 8.1 and 8.2.
- Dragana Bajović, João Xavier, José M. F. Moura, and Bruno Sinopoli, *Consensus and products of random stochastic matrices: Exact rate for convergence in probability*, arXiv:1202.6389 (2012), https://arxiv.org/abs/1202.6389 .
- Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapters VI and IX, for algebraic-singularity coefficient transfer and quasi-power techniques.
