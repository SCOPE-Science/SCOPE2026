# Exact non-Gaussian fixed-cylinder pair-collision law for full shifts

## Finding
Fix integers \(q\ge2\) and \(k\ge1\). For a uniform Bernoulli symbolic orbit, equality of two length-\(k\) cylinders has an **exact finite-sample expectation** and a **non-Gaussian, explicitly diagonalized order-\(N\) fluctuation**. With \(U_N\) as below,
\[
\mathbb E U_N=\binom N2 q^{-k},
\qquad
\frac{U_N-\mathbb E U_N}{N}\ \xrightarrow{\mathrm d}\
\frac{1}{2q^k}\left[k\sum_{a=1}^{q-1}(Z_{0,a}^2-1)+\sum_{d=1}^{k-1}(k-d)\sum_{a=1}^{(q-1)^2q^{d-1}}(Z_{d,a}^2-1)\right].
\]
All the displayed \(Z_{d,a}\) are independent standard Gaussians. In particular,
\[
\operatorname{Var}(U_N)=\frac{(q+1)q^k-(q+1)-2k(q-1)}{2(q-1)q^{2k}}N^2+O_{q,k}(N).
\]
The asymptotic covariance matrix of the vector of centered \(k\)-word counts normalized by \(\sqrt N\) has eigenvalue \(k/q^k\) with multiplicity \(q-1\), eigenvalue \((k-d)/q^k\) with multiplicity \((q-1)^2q^{d-1}\) for \(1\le d<k\), and eigenvalue \(0\) with multiplicity \(q^{k-1}\). These are all \(q^k\) eigenvalues, counted with multiplicity. The limit is not Gaussian: its third cumulant is positive.

## Assumptions and scope
Let \((\xi_i)_{i\ge0}\) be independent uniformly distributed letters from \(\{0,\ldots,q-1\}\). Define the sliding \(k\)-block \(W_i=(\xi_i,\ldots,\xi_{i+k-1})\) and the *unordered collision count*
\[
U_N=\#\{(i,j):0\le i<j<N,\ W_i=W_j\}.
\]
The symbolic full shift \(\sigma\) sends \((\xi_i)\) to \((\xi_{i+1})\). In the symbolic ultrametric \(d(x,y)=q^{-L(x,y)}\), where \(L\) is the length of the common initial word, the equality \(W_i=W_j\) is exactly the fixed-resolution relation \(d(\sigma^i x,\sigma^j x)\le q^{-k}\), with the conventional boundary defined by the length-\(k\) cylinder relation. The theorem holds for every *fixed* pair \((q,k)\), as \(N\to\infty\); it is not a joint limit with \(k\to\infty\).

## Proof
Choose a real-valued orthonormal basis \(\phi_0=1,\phi_1,\ldots,\phi_{q-1}\) of functions on the single-symbol space under normalized counting measure. Every nonconstant basis function has zero mean. For each multiindex \(a=(a_0,\ldots,a_{k-1})\), set \(\Phi_a(w)=\prod_{j=0}^{k-1}\phi_{a_j}(w_j)\), and let \(S_{a,N}=\sum_{i=0}^{N-1}\Phi_a(W_i)\). Orthonormal completeness gives, pointwise,
\[
\mathbf1_{u=v}=q^{-k}\sum_a\Phi_a(u)\Phi_a(v),
\qquad
U_N=\frac{1}{2q^k}\sum_a S_{a,N}^{2}-\frac N2.
\]
The all-zero multiindex contributes \(N^2\). If \(a\ne0\), then \(\mathbb E\Phi_a(W_i)=0\), \(\mathbb E\Phi_a(W_i)^2=1\), and \(\mathbb E[\Phi_a(W_i)\Phi_a(W_j)]=0\) for \(i\ne j\). For the last statement, when the decorated nonzero supports are shifted by a nonzero displacement, they cannot coincide as nonempty finite decorated sets; an endpoint unique to one product supplies a centered independent factor. Thus \(\mathbb E S_{a,N}^2=N\). The exact expectation formula follows because there are \(q^k-1\) nonconstant multiindices.

Every nonzero multiindex has a unique *anchored decorated support pattern*: translate its leftmost nonzero position to coordinate \(0\), and call the distance to its rightmost nonzero position \(d\). There are \(q-1\) anchored patterns with \(d=0\), and \((q-1)^2q^{d-1}\) patterns with each \(1\le d<k\). For a fixed anchored pattern of span \(d\), there are \(k-d\) distinct placements in a \(k\)-word. Every placement produces the same stationary product process shifted by at most \(k\) time steps. Its sum \(S_{a,N}\) therefore differs from the anchored sum by at most \(2k\max|\Phi_a|\), uniformly in \(N\).

For distinct anchored decorated patterns \(a,b\), the covariance of their product processes vanishes at every relative shift: independence and orthonormality at every decorated position imply zero unless the *full finite decorated supports* are equal after translation, which their distinct anchoring excludes. The variance at zero lag of each anchored process is one. All these processes are bounded and \((k-1)\)-dependent. The finite-dimensional \(m\)-dependent central limit theorem therefore gives a joint Gaussian limit for the anchored normalized sums \(N^{-1/2}S_{a,N}\), with identity covariance and hence mutually independent standard normal components. Bounded differences between placements and the continuous-mapping theorem for squares now give exactly the asserted centered chi-square weighted law.

For the covariance spectrum, apply the same orthogonal basis change to the \(q^k\)-dimensional histogram vector of word counts, normalized by \(\sqrt N\). For each anchored pattern with \(k-d\) placements, the limiting covariance block is the \((k-d)\)-square all-ones matrix divided by \(q^k\); it has one eigenvalue \((k-d)/q^k\) and \(k-d-1\) zero eigenvalues. The constant pattern contributes one zero. This yields the stated spectrum and exactly \(q^{k-1}\) zeros.

Because the processes are bounded and finitely dependent, every joint fourth cumulant of their sums is \(O_{q,k}(N)\): only connected four-index dependency configurations contribute, and there are \(O_{q,k}(N)\) of them. The quadratic-sum identity then gives
\[
\operatorname{Var}(U_N)=\frac{N^2}{2q^{2k}}\left[(q-1)k^2+(q-1)^2\sum_{d=1}^{k-1}q^{d-1}(k-d)^2\right]+O_{q,k}(N).
\]
An elementary finite geometric-sum evaluation reduces the bracket to \(((q+1)q^k-(q+1)-2k(q-1))/(q-1)\). All weights in the limiting law are positive, so its third cumulant \(8\sum_{a}\lambda_a^3\) is positive; the law cannot be normal.

## Verification
The standalone `checker.py` computes the limiting histogram covariance directly from exact overlap probabilities, as a rational matrix, without using the product-basis derivation. Its exact eigenvalues and variance coefficients agree for \((q,k)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,2)\). A second independent exhaustive check enumerates all finite strings in seven small cases and verifies the exact collision mean. `check_results.txt` records the actual outputs. Both checks are finite sanity tests; the proof above, not the computations, establishes the statements for every \(q,k,N\).

## Relationship to prior work
Baker and Todd (arXiv:2606.17880, first posted 2026-06-16) study almost-sure pair-correlation asymptotics for interval-map orbits at shrinking metric scales under mixing/multifractal hypotheses. The result here instead identifies the *entire non-Gaussian second-order limit* at a fixed symbolic-cylinder resolution for the Bernoulli full shift, with the explicit covariance eigenvalues and their multiplicities. Work on symbolic correlation integrals of ordinal patterns, including Schnurr, Silbernagel and Ruiz Marín (2025), derives general limit distributions via \(U\)-statistics, but does not specify this literal-cylinder full-shift spectral formula in the inspected text. Classical multivariate word-frequency central limit theorems supply a related general setting, whereas the explicit rank deficiency and multiplicity spectrum here arise from an anchored decorated-pattern decomposition.

## Limitations
Only the uniform independent-symbol full shift and fixed finite cylinder length are handled. No assertion is made for nonuniform or dependent digit sources, shrinking target scales, Euclidean-circle distance instead of symbolic ultrametric distance, or a uniform-in-\(k\) asymptotic. The covariance formula's existence may also be obtainable from general word-count central limit theory; the claimed contribution is the fully explicit spectral classification and resulting non-Gaussian collision law, not a new central limit theorem for finite-range dependent sequences. The recent primary preprint's full manuscript could not be retrieved from the accessible routes, so its abstract-level comparison carries residual priority risk.

## References
- S. Baker and M. Todd, *Pair correlation statistics for dynamical systems*, arXiv:2606.17880, first posted 2026-06-16. https://arxiv.org/abs/2606.17880
- A. Schnurr, A. Silbernagel, and M. Ruiz Marín, *Limit theorems for the symbolic correlation integral and the Rényi-2 entropy under short-range dependence*, *Statistics*, published online 2025-09-15, DOI 10.1080/02331888.2025.2552184. https://www.tandfonline.com/doi/full/10.1080/02331888.2025.2552184
- G. Reinert, S. Schbath, and M. S. Waterman, *Probabilistic and statistical properties of words: an overview*, *Journal of Computational Biology* (2000), an overview of word-occurrence limit theory.
