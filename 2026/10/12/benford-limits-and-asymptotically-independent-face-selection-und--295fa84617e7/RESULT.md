# Benford limits and asymptotically independent face selection under heterogeneous box fragmentation

## Finding

Fix an integer \(m\ge1\), an integer \(1\le d\le m\), and a real base \(B>1\). For each coordinate \(1\le i\le m\), let \((P_{i,t})_{t\ge1}\) be an independent identically distributed sequence taking values in \((0,1)\), and assume all the coordinate sequences are mutually independent. **The distribution may depend on the coordinate.** Suppose the logarithmic increments \(Y_{i,t}=\log_B P_{i,t}\) have a common finite mean \(\mu\), common finite variance \(\sigma^2>0\), and satisfy, for every nonzero integer \(k\),
\[
\bigl|\mathbb E\exp(2\pi\mathrm{i} kY_{i,1})\bigr|<1\qquad (1\le i\le m).
\]
In particular, this last condition holds if every \(P_{i,1}\) has an atomless distribution, including the continuous cuts in the motivating model.

Choose arbitrary deterministic \(c_i>0\). At time \(n\), put \(S_{i,n}=c_i\prod_{t=1}^nP_{i,t}\). Let \(I_{n,d}\) be the indices of the \(d\) longest \(S_{i,n}\), breaking ties by increasing index. Let
\[
M_{n,d}=\prod_{i\in I_{n,d}}S_{i,n},\qquad
V_{n,d}=2^{m-d}\sum_{I\subseteq\{1,\dots,m\}:\,|I|=d}\prod_{i\in I}S_{i,n}.
\]
Write \(\{x\}\) for the fractional part of a real number. If \(J_d\) is uniform on the \(\binom md\) subsets of size \(d\), and \(U\) is uniform on the circle \(\mathbb R/\mathbb Z\) independently of \(J_d\), then
\[
\boxed{\bigl(I_{n,d},\{\log_B M_{n,d}\},\{\log_B V_{n,d}\}\bigr)\ \Longrightarrow\ \bigl(J_d,U,\{U+(m-d)\log_B2\}\bigr).}
\]
Thus both maximal \(d\)-face product and total \(d\)-frame volume converge to **strong Benford behavior**, and the maximizing set of coordinates tends to a uniform set, independently of the limiting leading digits. The two limiting digit variables are *not* claimed independent: the second is the specified deterministic rotation of the first.

## Assumptions and scope

The integers \(m,d\), the base \(B\), coordinate cut laws, and initial dimensions are fixed as \(n\to\infty\). Cuts are independent over all coordinate–time pairs, with stationarity in each coordinate but not necessarily across coordinates. Only second logarithmic moments, equal first two logarithmic moments across coordinates, and nonresonance at integer frequencies are assumed; no density, smoothness, third moment, or higher moment hypothesis is used. The circle means \(\mathbb R/\mathbb Z\), so braces are interpreted modulo one. A random positive variable is strongly Benford in base \(B\) if its base-\(B\) logarithm converges modulo one to Haar-uniform measure. The formula includes \(d=m\), where there is exactly one product, and \(m=1\).

**Concrete nonsmooth heterogeneous example.** Take \(B=10\), \(m=2\), and two different centered increment laws with the same mean and variance: \(Y_{1,1}=-4+W\), with \(W\) equal to \(1/\sqrt2\) or \(-1/\sqrt2\), each with probability one half; and \(Y_{2,1}=-4+Z\), with \(Z\) equal to \(-\sqrt2,0,\sqrt2\) with probabilities \(1/8,3/4,1/8\). Both have mean \(-4\), variance \(1/2\), negative support, and no nonzero integer-frequency resonance because \(\sqrt2\) is irrational. Setting \(P_{i,t}=10^{Y_{i,t}}\) (with independent copies) gives discrete, genuinely non-identical cut laws excluded by the smooth globally iid hypotheses of the 2025 theorem.

## Proof

**1. A probabilistic rank gap.** For \(d<m\), write the logarithmic side lengths as
\[
L_{i,n}=\log_B c_i+\sum_{t=1}^nY_{i,t}.
\]
By the independent-coordinate central limit theorem,
\[
\left(\frac{L_{i,n}-n\mu}{\sigma\sqrt n}\right)_{i=1}^m\ \Longrightarrow\ (Z_i)_{i=1}^m,
\]
where the \(Z_i\) are independent standard normal variables. Let \(G_{n,d}\) be the difference between the \(d\)-th and \((d+1)\)-st largest \(L_{i,n}\). The continuous mapping theorem at normal vectors without ties gives
\[
G_{n,d}/(\sigma\sqrt n)\ \Longrightarrow\ \Gamma_d,
\]
where \(\Gamma_d\) is the corresponding normal rank gap and \(\Pr(\Gamma_d>0)=1\). In particular \(G_{n,d}\to\infty\) in probability. Symmetry of the independent Gaussian limit, and the absence of ties therein, also give
\[
\Pr(I_{n,d}=I)\longrightarrow \binom md^{-1}
\]
for every \(d\)-element subset \(I\). Fixed initial dimensions and unequal increment distributions have no effect on these conclusions because their centered Gaussian limits have the same variance.

**2. Split the increments to separate rank and phase.** Put \(r=\lfloor\sqrt n\rfloor\) and \(N=n-r\). Define
\[
A_i=\log_B c_i+\sum_{t=1}^{N}Y_{i,t},\qquad
T_i=\sum_{t=N+1}^{n}Y_{i,t}.
\]
Let \(I^0\) be the size-\(d\) set of the largest \(A_i\), and let \(G^0\) denote the \(d\)-th to \((d+1)\)-st prefix gap. From Step 1 and \(n^{3/8}/\sqrt N\to0\),
\[
\Pr(G^0\le2n^{3/8})\to0.
\]
Independence, the common mean, and Chebyshev's inequality show
\[
\Pr\!\left(\max_i|T_i-r\mu|>n^{3/8}\right)
\le\frac{m\sigma^2 r}{n^{3/4}}=O(n^{-1/4})\to0.
\]
On the complementary event, the perturbations \(T_i-r\mu\) can change any pairwise gap by at most \(2n^{3/8}\); hence the winners cannot change. Consequently
\[
\Pr(I_{n,d}\ne I^0)\to0.
\]

**3. Joint Fourier coefficients.** For every nonzero integer \(k\), set
\[
q_k=\max_{1\le i\le m}\left|\mathbb E e^{2\pi\mathrm{i}kY_{i,1}}\right|<1.
\]
Fix a \(d\)-element set \(I\). Conditional on all prefixes, \(I^0\) is fixed and the suffix increments are independent, so
\[
\left|\mathbb E\left[\boldsymbol1_{\{I^0=I\}}
\exp\!\left(2\pi\mathrm{i}k\sum_{i\in I^0}(A_i+T_i)\right)\right]\right|
\le q_k^{dr}\to0.
\]
Replacing \(I^0\) by \(I_{n,d}\) in the indicator and the exponent changes the expectation by at most \(2\Pr(I_{n,d}\ne I^0)\), because on the agreement event the selected sums agree exactly. Thus the nonzero Fourier coefficients of the joint limiting law of \(I_{n,d}\) and \(\{\log_BM_{n,d}\}\) vanish on every fixed label \(I\). At frequency zero their masses tend to \(\binom md^{-1}\) by Step 1. Fourier uniqueness for probability measures on the circle, separately for each finite label, proves
\[
(I_{n,d},\{\log_BM_{n,d}\})\Longrightarrow(J_d,U),\qquad U\perp J_d.
\]
For \(d=m\) there is just one label and the same conclusion follows immediately from independence and the product of the \(m\) characteristic functions (or the same prefix/suffix argument without needing a rank gap).

**4. The sum of faces has the maximal phase.** If \(d<m\), every other \(d\)-element set \(I\ne I_{n,d}\) replaces at least one selected coordinate by a nonselected one, so
\[
\frac{\prod_{i\in I}S_{i,n}}{M_{n,d}}\le B^{-G_{n,d}}.
\]
There are \(\binom md-1\) such sets, whence the deterministic bound
\[
1\le \frac{V_{n,d}}{2^{m-d}M_{n,d}}
\le1+\left(\binom md-1\right)B^{-G_{n,d}}.
\]
Since \(G_{n,d}\to\infty\) in probability, the logarithm of this ratio tends to zero in probability. The continuous mapping theorem on the circle and Slutsky's theorem yield the stated joint limit. For \(d=m\), the identity \(V_{n,m}=M_{n,m}\) completes the proof. \(\square\)

## Verification

The proof has no finite-enumeration hypothesis. The standalone standard-library checker `verify.py` confirms the deterministic inequality in Step 4 for independent exact integer-log configurations, including all rank patterns in the enumerated range, and computes the simple example of a nonresonant logarithmic law versus a resonant one. Run `python3 verify.py` from the extracted package directory. The checker supplies finite cross-checks, **not** a substitute for the central limit theorem, Chebyshev bound, Fourier uniqueness, or infinite-parameter proof above.

## Relationship to prior work

Betti, Durmić, McDonald, Miller and Miller (arXiv:2304.08335v1, 2023-04-17), Definition 1.7 and Conjecture 4.1, proposed strong Benford behavior of the maximal lower-dimensional face product in a linear-fragmentation process with possibly different coordinate cut distributions sharing logarithmic mean and variance; their Theorem 1.9 deduced frame Benfordness conditional on maximal-face Benfordness, and their proof of the maximal-face criterion covered a log-uniform one-dimensional special case. The present proof directly resolves the stated full independent-coordinate common-moment case, and adds a joint limit for the winner labels and both leading-digit variables.

Important subsequent work must not be omitted: Fang and Miller, arXiv:2508.12915v4 (2026 revision of a 2025 preprint), Theorem 5, **already proves all face dimensions** when *every* coordinate-time cut is identically distributed and its logarithm has all centered moments, an admissible characteristic-function expansion, bounded density and bounded density derivative. Their Section 3.1 explicitly identifies non-identically distributed coordinates and relaxed assumptions as extensions. The present claim is not priority over that all-dimensional smooth-iid theorem; it strengthens its assumptions to second moments with possible coordinate heterogeneity and establishes label–phase independence. Other literature on random order-statistic spacings concerns different random quantities and does not imply this joint statement.

## Limitations

The conclusion is distributional convergence of one selected fragment at time \(n\), not an almost-sure pathwise Benford frequency or a rate of equidistribution. Neither growing dimension \(m\), dependence across coordinates or times, unequal logarithmic means/variances, nor infinite logarithmic variance is addressed. The nonresonance condition is sufficient and automatically true for atomless cuts; without it, deterministic lattice increments can retain a fixed nonuniform phase. The uniform label law depends crucially on matching logarithmic first two moments. The strongest earlier all-dimensional theorem predates this work for smoother fully iid cuts; bibliographic novelty is limited to the weaker, heterogeneous hypotheses and joint conclusion. No claim of independent external validation is made.

## References

1. L. Betti, I. Durmić, Z. McDonald, J. B. Miller, S. J. Miller, *Benfordness of Measurements Resulting from Box Fragmentation*, arXiv:2304.08335v1 (first public 2023-04-17), Definition 1.7, Theorem 1.9, Conjecture 4.1. https://arxiv.org/pdf/2304.08335
2. B. Fang, S. J. Miller, *Benford Behavior Resulting From Stick and Box Fragmentation Processes*, arXiv:2508.12915v4 (2026 revision; first public 2025-08-18), Theorem 5, Section 3.1, Appendix C. https://arxiv.org/pdf/2508.12915
3. S. J. Miller and M. J. Nigrini, *Order Statistics and Benford's Law*, International Journal of Mathematics and Mathematical Sciences (2008), DOI:10.1155/2008/382948 (background comparison; spacing statistics rather than evolving face maxima).
