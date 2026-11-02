# Scientific review: logarithmic spatial correlations in planar critical branching random walks

## Correctness — PASS

The theorem specifies the critical offspring mean and finite positive variance, aperiodic five-point step distribution, unconditional occupation counts, exact ranges of separation, and all normalizations. The ordered-pair genealogy identity follows from independent offspring families and \(\mathbb E[K(K-1)]=\sigma^2\). Its first-generation recurrence and the spatial convolution identity were both checked with exact rational arithmetic. The spatial asymptotics follow from the two-dimensional local central limit theorem, Gaussian bounds, and controlled early/late summation slices; the macroscopic profile is a dominated heat-kernel limit and a Gaussian product identity. The proof distinguishes finite checks from the infinite-generation argument. No higher offspring moment or survival conditioning is tacitly used.

## Originality — PASS, subject to historical-priority limits

The full primary 2026 manuscript by Bai, Chen and Lin (arXiv:2609.15538) addresses one-site local survival and Yaglom laws, not the quantitative two-site occupation-count correlation profile. The 2010 arXiv full text of Lalley and Zheng (arXiv:0707.3829), particularly Section 5.4 Proposition 25 and Section 6, contains the exact diagonal second moment and qualitative clustering, but not the explicit \(1-2\theta\) separation law. The general many-to-two recursion and the continuum macroscopic covariance kernel are well-established conceptual predecessors; neither is advertised here in isolation as novel. The assessed contribution is the matched mesoscopic logarithmic correlation law with exact coefficient and its rigorous connection to the diffusive kernel. General multivariate moment methods may imply an alternate derivation; historical priority remains provisional and requires independent literature verification.

## Mathematical value — PASS

The result gives a precise, natural measure of how much ancestry is shared by occupation counts at distinct sites. The full interval of polynomial separation exponents is classified by a linear correlation profile, with exact decorrelation at the diffusive scale and a matching macroscopic kernel. It sharpens previously qualitative planar clustering statements and provides a benchmark for two-point spatial questions and multi-site conditioning. The theorem does not claim a joint Yaglom law or survival-conditioned correlation.

## Closest literature and limitations

- Bai, Chen and Lin, *Critical branching random walks on \(\mathbb Z^2\): local survival probabilities and Yaglom limit theorems*, arXiv:2609.15538, first public 2026-09-14, https://arxiv.org/abs/2609.15538.
- Lalley and Zheng, *Occupation Statistics of Critical Branching Random Walks in Two or Higher Dimensions*, arXiv:0707.3829, https://arxiv.org/html/0707.3829v3, especially Proposition 25 and Section 6.
- Lalley, *Spatial Epidemics: Critical Behavior in One Dimension*, https://arxiv.org/abs/math/0701698, cited for general moment recursions, not inspected in its entirety.

The proof is for one aperiodic lazy walk and finite-variance reproduction; it provides no convergence rate. Independent verification and exhaustive historical-priority certification have not occurred.

Self-review: passed. Independent audit: not yet performed.
