# Parity-sharp path-energy amplification under coordinate sorting

## Finding
For every integer \(N\ge2\), let \(S_N:\mathbb R^N\to\mathbb R^N\) arrange the coordinates increasingly. Define the homogeneous path energy
\[
\mathcal E_N(x)=\sum_{j=1}^{N-1}(x_{j+1}-x_j)^2,
\]
and the sharp **two-point** amplification constant
\[
K_N=\sup_{\mathcal E_N(x-y)>0}\left(\frac{\mathcal E_N(S_Nx-S_Ny)}{\mathcal E_N(x-y)}\right)^{1/2}.
\]
Then
\[
K_N\le \cot\left(\frac{\pi}{2N}\right),
\]
with equality **if and only if \(N\) is even**. If \(N\ge3\) is odd, the following fully explicit strict enclosure holds:
\[
\cot\left(\frac{\pi}{2N}\right)\sqrt{1-\frac{\pi^2}{2N^2}}
\ \le K_N <\ \cot\left(\frac{\pi}{2N}\right).
\]
In particular, \(K_N\sim 2N/\pi\), for both parities. In contrast, every individual vector satisfies \(\mathcal E_N(S_Nx)\le\mathcal E_N(x)\). Thus individual energy monotonicity does not control the stability of differences.

## Assumptions and scope
Vectors are real, vertices \(1,\ldots,N\) are in the fixed unweighted path order, and the energy is the squared discrete first-difference seminorm. Additive constants are factored out; all linear operators are evaluated on \(\mathbb R^N/\operatorname{span}\{\mathbf1\}\). Sorting is nondecreasing, with ties harmless by continuity. Every amplification is measured between **two inputs**; the one-point energy estimate is a different assertion. The right-hand lower bound for odd \(N\) is positive, since \(N\ge3\).

## Proof
**1. The nonlinear modulus equals the largest permutation modulus.** On every open chamber with strictly ordered input coordinates, \(S_N\) is a fixed permutation matrix \(P\). Each such chamber is nonempty. For any two vectors, partition the segment connecting them at finitely many coordinate-crossing parameters; along each subsegment the derivative of sorting is one of these permutation matrices. The triangle inequality for the quotient energy norm yields
\[
K_N\le\max_{P\in\mathfrak S_N}\sup_{\mathcal E_N(z)>0}
\left(\frac{\mathcal E_N(Pz)}{\mathcal E_N(z)}\right)^{1/2}.
\]
Conversely, for each permutation \(P\), choose an interior point of the corresponding ordering chamber and sufficiently small perturbations with arbitrary direction \(z\). Sorting acts exactly as \(P\) on their difference, giving the reverse inequality. The maximum is attained because the number of permutations is finite and the quotient unit sphere is compact.

**2. The universal spectral ceiling.** The path Laplacian \(L_N\) is the matrix satisfying \(\mathcal E_N(z)=z^\top L_Nz\). Its eigenvalues are
\[
\lambda_k=4\sin^2\left(\frac{k\pi}{2N}\right),\quad k=0,1,\ldots,N-1.
\]
For every mean-zero \(z\), and every permutation \(P\),
\[
\mathcal E_N(Pz)\le\lambda_{N-1}\|z\|_2^2,
\qquad \mathcal E_N(z)\ge\lambda_1\|z\|_2^2.
\]
Because \(\lambda_1=4\sin^2(\pi/(2N))\) and \(\lambda_{N-1}=4\cos^2(\pi/(2N))\), the asserted ceiling follows. Both extremal nonconstant eigenspaces are one-dimensional. A convenient equal-norm eigenvector pair is
\[
u_j=\cos\left(\frac{(j-1/2)\pi}{N}\right),\qquad
v_j=(-1)^{j-1}\sin\left(\frac{(j-1/2)\pi}{N}\right),\qquad j=1,\ldots,N.
\]
Both have zero sum and squared Euclidean norm \(N/2\). Equality in both Rayleigh bounds requires an extremal input proportional to \(u\), with a coordinate permutation proportional to \(v\).

**3. Parity classifies exact spectral saturation.** For even \(N\), the coordinate multisets of \(u\) and \(v\) coincide. To see this, use the identity \(\sin\alpha=\cos(\pi/2-\alpha)\) and pair indices \(j\) with \(N+1-j\); their signs are opposite when \(N\) is even. Consequently some permutation \(P\) satisfies \(Pu=v\). The corresponding Rayleigh quotient achieves \(\lambda_{N-1}/\lambda_1\), and hence the global two-point constant attains the ceiling. For odd \(N\), \(u\) has exactly one zero coordinate (its middle coordinate), while \(v\) has none. Thus neither \(u\) nor its negative can be permuted to \(v\). Because the eigenspaces and the finite permutation family exhaust all equality cases, the inequality is strict.

**4. Explicit near-saturation for odd lengths.** Put \(\theta=\pi/(2N)\). In increasing order, the coordinates of \(u\) can be written as \(-\cos\alpha_i\), with \(\alpha_i=(i+1/2)\pi/N\) for \(i=0,\ldots,N-1\). For odd \(N\equiv1\pmod4\), the increasing-order coordinates of \(v\) are \(-\cos\beta_i\), where \(\beta_i=(2\lfloor i/2\rfloor+1)\pi/N\), except that the final \(\beta_{N-1}=\pi\). For odd \(N\equiv3\pmod4\), the corresponding angles are \(\beta_i=2\lceil i/2\rceil\pi/N\). In either case, \(|\alpha_i-\beta_i|=\theta\) for all indices; the cosine function is 1-Lipschitz. Hence an explicit permutation \(P\) matching equal coordinate ranks satisfies
\[
\|Pu-v\|_2^2\le N\theta^2.
\]
Let \(z=Pu\). Since \((\lambda_{N-1}I-L_N)v=0\),
\[
\lambda_{N-1}\frac N2-\mathcal E_N(z)
=(z-v)^\top(\lambda_{N-1}I-L_N)(z-v)
\le\lambda_{N-1}\|z-v\|_2^2
\le\lambda_{N-1}N\theta^2.
\]
Divide by \(\mathcal E_N(u)=\lambda_1N/2\) and take square roots to obtain \(K_N\ge\cot\theta\sqrt{1-2\theta^2}\). The ratio of this lower bound and the spectral ceiling tends to one with error \(O(N^{-2})\); therefore \(K_N\sim2N/\pi\).

**5. Individual energy contracts.** Let \(x_{(1)}\le\cdots\le x_{(N)}\) and \(g_k=x_{(k+1)}-x_{(k)}\ge0\). Every original path edge crossing the sorted-value gap \(k\) has absolute difference at least \(g_k\), and its squared length is at least the sum of the squares of all sorted-value gaps that it crosses. The path visits vertices representing both sides of every gap, so at least one original edge crosses each gap. Summing gives \(\mathcal E_N(x)\ge\sum_{k=1}^{N-1}g_k^2=\mathcal E_N(S_Nx)\). This proof also covers ties.

## Verification
The accompanying `verify.py` checks the exact path eigenvectors and parity multiset identities, enumerates the generalized Rayleigh maxima of **every permutation** for \(2\le N\le7\), checks the strict odd bounds, and samples the one-point inequality through \(N=27\). Its 6,344 successful individual finite checks are corroboration rather than an infinite-dimensional or all-\(N\) proof. Run with `python verify.py` using NumPy and SciPy. The all-\(N\) assertion rests on the five analytic steps above.

## Relationship to prior work
Classical and discrete Pólya–Szegő principles concern \(\mathcal E(Sx)\le\mathcal E(x)\) for one input. Chernozhukov–Fernández-Val–Galichon establish improved rearranged estimates in common \(L^p\) losses relative to monotone targets; their statements do not give a two-input path Dirichlet-energy amplification profile. Steinerberger examines one-input graph rearrangement gradient norms. Gupta's later lattice rearrangement treatment likewise studies one-input energy and ordinary \(L^p\) quantities. In a different geometry, sorting has an exact two-point modulus for finite-star Sobolev norms, but its star Laplacian and inhomogeneous quadratic form do not imply this path parity classification. The present result combines the path's two extremal spectral modes with order-statistic matching, distinguishing saturating even lengths from strictly nonsaturating odd lengths.

## Limitations
The exact value of \(K_N\) for odd \(N\ge3\) is not determined; only a strict spectral ceiling and an explicit asymptotically tight lower bound are proved. The theorem does not cover arbitrary weighted paths, other connected graphs, different gradient exponents, or continuous Sobolev rearrangements. No assertion of external independent audit is made; absence of an indexed equivalent statement is not a proof of global literature novelty.

## References
1. V. Chernozhukov, I. Fernández-Val, A. Galichon, *Improving Point and Interval Estimates of Monotone Functions by Rearrangement*, arXiv:0806.4730v1, first public 29 June 2008; https://arxiv.org/abs/0806.4730 .
2. S. Steinerberger, *Discrete Rearrangements and the Pólya–Szegő Inequality on Graphs*, arXiv:2209.06765, 2022; https://arxiv.org/abs/2209.06765 .
3. S. Gupta, *Discrete Functional Inequalities on Lattice Graphs*, arXiv:2403.10270, 2024; https://arxiv.org/abs/2403.10270 .
4. F. J. Almgren and E. H. Lieb, *Symmetric Decreasing Rearrangement Is Sometimes Continuous*, Journal of the American Mathematical Society 2 (1989), 683–773; https://www.ams.org/journals/jams/1989-02-04/S0894-0347-1989-1002639-8/ .
5. C. Anil, J. Lucas, R. Grosse, *Sorting Out Lipschitz Function Approximation*, Proceedings of Machine Learning Research 97 (2019), 291–301; https://proceedings.mlr.press/v97/anil19a.html .
