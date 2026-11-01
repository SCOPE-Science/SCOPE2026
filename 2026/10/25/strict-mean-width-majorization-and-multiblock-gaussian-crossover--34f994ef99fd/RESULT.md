# Strict mean-width majorization and multiblock Gaussian crossover for multipartite stable-set polytopes

## Finding
Let \(r\geq3\), let \(\mathbf n=(n_1,\ldots,n_r)\) be positive integers, and put \(N=\sum_i n_i\). Let \(P_{\mathbf n}\subset\mathbb R^N\) be the stable-set polytope of the complete multipartite graph \(K_{n_1,\ldots,n_r}\), in its standard coordinate embedding. If \(Z_{ij}\) are independent standard normals and \(S_i=\sum_{j=1}^{n_i}(Z_{ij})_+\), then its Euclidean mean width is exactly
\[
w(P_{\mathbf n})=\frac{2\,\mathbb E\max_{1\le i\le r}S_i}{\sqrt2\,\Gamma((N+1)/2)/\Gamma(N/2)}.
\]
At fixed \(N,r\), every outward unit transfer between two blocks, from a smaller block of size at least two to an at-least-as-large block, **strictly increases** the width. Thus the unique minimizing profile up to permutation has entries differing by at most one; the unique maximizing profile up to permutation is \((N-r+1,1,\ldots,1)\).

Write \(\mu=1/\sqrt{2\pi}\), \(\sigma^2=1/2-1/(2\pi)\). For fixed \(r\), if \((n_i-N/r)/\sqrt N\to c_i\) as \(N\to\infty\), with \(\sum_i c_i=0\), then
\[
w(P_{\mathbf n})=\frac{2\mu}{r}\sqrt N+F_r(\mathbf c)+o(1),\qquad
F_r(\mathbf c)=2\mathbb E\max_i\left(\mu c_i+\frac\sigma{\sqrt r}G_i\right),
\]
where the \(G_i\) are independent standard normals. The function \(F_r\) is strictly convex on the zero-sum subspace, symmetric, and uniquely minimized at \(\mathbf c=0\). For three balanced blocks, \(F_3(0,0,0)=\sigma\sqrt{3/\pi}\). More generally, if \(n_i/N\to\alpha_i\geq0\), \(\sum_i\alpha_i=1\), then
\[
\frac{w(P_{\mathbf n})}{\sqrt N}\longrightarrow 2\mu\max_i\alpha_i.
\]
Consequently the maximum/minimum width ratio over all positive \(r\)-block profiles of total size \(N\) tends to \(r\).

## Assumptions and normalization
All assertions use the standard unweighted stable-set polytope
\[
P_{\mathbf n}=\operatorname{conv}\bigcup_{i=1}^r\{(0,\ldots,0,x,0,\ldots,0):x\in[0,1]^{n_i}\},
\]
in the canonical orthogonal decomposition of \(\mathbb R^N\). Its Euclidean mean width is \(\int_{S^{N-1}}(h_P(u)+h_P(-u))\,d\omega(u)\) with \(\omega\) normalized spherical measure. The asymptotics require fixed \(r\), not growing numbers of classes. Equality statements are up to permutation of parts. The already-studied two-block case is excluded from novelty scope. All displayed expectations are finite.

## Proof
**1. Gaussian support formula.** Every stable set lies inside one independent vertex class. Hence for any \(g\in\mathbb R^N\) the support function is
\[
h_{P_{\mathbf n}}(g)=\max_i\sum_j(g_{ij})_+.
\]
For a standard Gaussian vector \(g=RU\), \(U\) is uniform on the sphere, independent of \(R=\|g\|\), and \(\mathbb ER=\sqrt2\Gamma((N+1)/2)/\Gamma(N/2)\). By homogeneity and central symmetry of Gaussian measure, the mean width equals \(2\mathbb Eh_P(g)/\mathbb ER\), proving the formula.

**2. Strict transfer lemma in the domain actually needed.** Let \(Y\ge0\) be integrable with both \(\Pr(Y=0)>0\) and \(\Pr(Y>0)>0\). For independent copies let \(S_m\) be the sum of \(m\) copies. Let \(C\ge0\) be **integrable**, independent of all those copies, and satisfy **\(\Pr(C=0)>0\)**. If \(p\ge q\ge2\), then
\[
\mathbb E\max(S_{p+1},S_{q-1},C)>\mathbb E\max(S_p,S_q,C),
\]
where each displayed family of sums consists of independent sums with the indicated lengths. The condition on \(C\) is essential to this general lemma: it cannot be omitted for arbitrary \(Y,C\).

Indeed take independent \(A,B\sim S_{q-1}\), \(V\sim S_{p-q+1}\), \(Y\) and \(C\), and couple the two maxima as \(\max(A+V,B+Y,C)\) and \(\max(A+V+Y,B,C)\), respectively. For fixed nonnegative \(b,y,c\), define
\[
d(a,b;y,c)=\max(a+y,b,c)-\max(a,b+y,c).
\]
It is nondecreasing in \(a\): wherever derivatives exist,
\[
\partial_a d=\mathbf1_{\{a>\max(b,c)-y\}}-\mathbf1_{\{a>\max(b+y,c)\}}\ge0.
\]
Exchangeability of \(A,B\) gives \(\mathbb E d(A,B;Y,C)=0\), so \(\mathbb E d(A+V,B;Y,C)\ge0\). Strictness holds on the independent positive-probability event \(A=B=C=0,\ V>0,\ Y>0\), because there \(d(V,0;Y,0)-d(0,0;Y,0)=\min(V,Y)>0\). Thus the expected gain is strictly positive.

For our stable-set application, \(Y=(Z)_+\) has an atom of mass \(1/2\) at zero and is positive with positive probability. For a transfer between two blocks, let \(C\) be the maximum of the independent positive-part Gaussian sums in all **other** classes. These classes have finite positive sizes and their sums simultaneously vanish with positive probability, so \(\Pr(C=0)>0\). The strict lemma applies, including when there are no other classes (then set \(C=0\)). The conclusion is therefore true for every asserted block transfer. Note that the unrestricted claim for arbitrary nonnegative independent \(C\) would be false: for example, if \(Y\) is Bernoulli and \(C\) is a sufficiently large constant, both maxima are identically \(C\); no such constant occurs in our application.

**3. Extremizing finite profiles.** Repeated balancing transfers from a strictly larger part to a smaller part whenever the size gap is at least two decrease width strictly, until every pair differs by at most one. Conversely, moving one unit from any nonlargest part of size at least two into a largest part raises width strictly and ends at \((N-r+1,1,\ldots,1)\). This proves both extremal orbits; when \(N=r\), there is only one possible profile.

**4. Near-balanced limit.** The independent block sums have mean \(\mu n_i\), variance \(\sigma^2n_i\), and finite second moments. The multivariate central limit theorem gives
\[
\left(\frac{S_i-\mu N/r}{\sqrt N}\right)_{i=1}^r\Rightarrow\left(\mu c_i+\frac\sigma{\sqrt r}G_i\right)_{i=1}^r.
\]
Since \(r\) is fixed and the normalized centered shifts are bounded in \(L^2\), maxima are uniformly integrable; their expectations converge. Moreover \(\mathbb ER/\sqrt N=1+O(N^{-1})\). Substitution into the exact width formula gives the stated second-order expansion. For any two different shift vectors modulo common translation, the Gaussian density has full support and with positive probability their maximizing indices differ. At those samples the pointwise affine maximum is strictly below the chord between its endpoint values, proving strict convexity of its expectation modulo the common-translation direction. Symmetry under coordinate permutations and averaging show that its unique zero-sum minimizer is zero. Integrating the maximum of three standard Gaussians gives \(\mathbb E\max(G_1,G_2,G_3)=3/(2\sqrt\pi)\), hence the stated constant.

**5. Macroscopic limit and ratio.** If \(n_i/N\to\alpha_i\), then \(S_i/N\to\mu\alpha_i\) in \(L^2\), with the same conclusion when \(\alpha_i=0\). A fixed finite maximum converges in \(L^1\), and \(\mathbb ER/\sqrt N\to1\). This proves \(w(P_{\mathbf n})/\sqrt N\to2\mu\max_i\alpha_i\). The balanced minimizing profile has \(\max\alpha_i=1/r\) in its limit and the maximizer has \(\max\alpha_i=1\); the extremal ratio is \(r\).

## Verification and boundaries
Independent exact-rational calculations checked 1,260 outward transfers with a Bernoulli positive-part surrogate and exposed the necessity of the additional hypothesis on the independent comparison variable \(C\). Other direct finite support and Gaussian diagnostics in `verify_multipartite.py` remain reproducible and corroborative only. The all-parameter conclusion follows from the foregoing proof. This result neither claims general graph stable-set polytopes, arbitrary coordinate weights, noninteger block sizes, growing \(r\), nor higher intrinsic volumes. Strict Schur-convexity is for positive integer part sizes. The integral Gaussian representation is an exact expectation, not a convergence-rate assertion.

## Relationship to prior work
Aliniaeifard, Benedetti, Bergeron, Li and Saliola, *Stable set polytopes and their 1-skeleta* (arXiv:1804.00360), analyze vertices and graph structure rather than the displayed Euclidean mean-width comparison. Ahmad, Fourier and Joswig, *Order and chain polytopes of maximal ranked posets* (arXiv:2309.01626), study face numbers. Kabluchko, Litvak and Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables* (DOI:10.1007/s10958-017-3492-3), provide Gaussian-width techniques for different polytope families. The two-block folded-normal mean-width problem is earlier and is not asserted as new. A general stochastic-majorization theorem elsewhere could subsume part of the transfer argument; historical priority is best-of-knowledge rather than absolute.
