# Strict mean-width majorization and multiblock Gaussian crossover for multipartite stable-set polytopes

## Finding
For each fixed integer \(r\ge3\), every \(r\)-tuple of positive integers \(\mathbf n=(n_1,\ldots,n_r)\), and \(N=\sum_i n_i\), the standard Euclidean stable-set polytope of the complete multipartite graph \(K_{n_1,\ldots,n_r}\) has the exact mean-width representation
\[
\boxed{w(P_{\mathbf n})=\frac{2\,\mathbb E\max_{1\le i\le r}\sum_{j=1}^{n_i}(Z_{ij})_+}{\sqrt2\,\Gamma((N+1)/2)/\Gamma(N/2)}}.
\]
The \(Z_{ij}\) are independent standard normal variables and \((t)_+=\max(t,0)\). At fixed \(N\) and \(r\), this width is **strictly Schur-convex** in the integer vector of part sizes: every nontrivial transfer of one vertex from a smaller positive part of size at least two into an at-least-as-large part strictly increases the width. Therefore its unique minimizers up to part permutation have part sizes differing by at most one; its unique maximizer up to permutation is \((N-r+1,1,\ldots,1)\).

Put \(\mu=1/\sqrt{2\pi}\) and \(\sigma^2=1/2-1/(2\pi)\). For fixed \(r\ge3\), if \(N\to\infty\) through positive integer profiles and \((n_i-N/r)/\sqrt N\to c_i\) for all \(i\), so \(\sum_i c_i=0\), then
\[
\boxed{w(P_{\mathbf n})=\frac{2\mu}{r}\sqrt N+F_r(\mathbf c)+o(1),\qquad
F_r(\mathbf c)=2\,\mathbb E\max_{1\le i\le r}\left(\mu c_i+\frac{\sigma}{\sqrt r}G_i\right),}
\]
where the \(G_i\) are independent standard normal variables. The function \(F_r\) is symmetric and strictly convex on the zero-sum subspace, hence uniquely minimized at \(\mathbf c=0\). The explicit three-block balanced constant is \(F_3(0,0,0)=\sigma\sqrt{3/\pi}\).

For arbitrary fixed-rank profiles with \(n_i/N\to\alpha_i\ge0\) and \(\sum_i\alpha_i=1\),
\[
\boxed{\frac{w(P_{\mathbf n})}{\sqrt N}\longrightarrow 2\mu\max_i\alpha_i.}
\]
Consequently, the ratio of the maximum to the minimum mean width among all \(r\)-part profiles with total size \(N\) converges to precisely \(r\) as \(N\to\infty\).

## Assumptions and scope
The graph \(G=K_{n_1,\ldots,n_r}\) has \(r\ge3\) nonempty independent vertex classes of sizes \(n_i\ge1\). Write the ambient vector space as the orthogonal sum \(\mathbb R^N=\bigoplus_i\mathbb R^{n_i}\). Its stable-set polytope is
\[
P_{\mathbf n}=\operatorname{conv}\left(\bigcup_{i=1}^r\{(0,\ldots,0,x,0,\ldots,0):x\in[0,1]^{n_i}\}\right).
\]
The Euclidean mean width uses ambient unit-sphere probability measure \(\omega_{N-1}\),
\[
w(K)=\int_{S^{N-1}}\bigl(h_K(u)+h_K(-u)\bigr)\,d\omega_{N-1}(u),\quad h_K(u)=\sup_{x\in K}\langle u,x\rangle.
\]
All dimension-dependent limits hold with the number \(r\) of blocks fixed. Distinct vectors of part sizes are compared at fixed \((N,r)\); equality classifications are up to permutation of blocks. The case \(r=2\) is explicitly not claimed as an original result here because the associated polytope is orthogonally congruent, by reflecting one coordinate block, to the previously analyzed two-level order polytope.

## Proof
**Exact Gaussian representation.** Each stable set of a complete multipartite graph lies in one vertex class. Linear optimization over the convex hull of its coordinate cubes therefore gives, for every \(g\in\mathbb R^N\),
\[
h_{P_{\mathbf n}}(g)=\max_{1\le i\le r}\sum_{j=1}^{n_i}(g_{ij})_+.
\]
For a standard Gaussian \(g=RU\) with \(U\) uniform on \(S^{N-1}\), radius \(R=\|g\|\) independent of \(U\), and \(\mathbb ER=\sqrt2\Gamma((N+1)/2)/\Gamma(N/2)\), homogeneity gives \(\mathbb Eh_P(g)=\mathbb ER\,\mathbb Eh_P(U)\). Gaussian central symmetry gives \(w(P)=2\mathbb Eh_P(U)\). This proves the displayed exact formula with no asymptotic approximation.

**Strict transfer lemma.** Let \(Y\ge0\) be any random variable with both \(\mathbb P(Y=0)>0\) and \(\mathbb P(Y>0)>0\). For independent identically distributed copies \(Y_{ij}\), write \(S_m=\sum_{j=1}^mY_j\). For any \(p\ge q\ge2\) and any independent \(C\ge0\), the expected maximum of \((S_p,S_q,C)\) strictly increases when \((p,q)\) is replaced by \((p+1,q-1)\), with \(C\) unchanged. Here is a direct coupling and proof, including strictness.

Use independent \(A,B\stackrel d=S_{q-1}\), \(V\stackrel d=S_{p-q+1}\), one \(Y\stackrel d=Y_1\), and \(C\); then before and after the transfer the respective maxima can be coupled as
\[
M_{\mathrm{before}}=\max(A+V,B+Y,C),\qquad
M_{\mathrm{after}}=\max(A+V+Y,B,C).
\]
For fixed \(b,y,c\ge0\), let \(d(a,b;y,c)=\max(a+y,b,c)-\max(a,b+y,c)\). Its derivative with respect to \(a\), wherever it exists, is
\[
\mathbf1_{\{a>\max(b,c)-y\}}-\mathbf1_{\{a>\max(b+y,c)\}}\ge0.
\]
Thus \(d\) is nondecreasing in its first argument. By exchangeability, \(\mathbb E[d(A,B;Y,C)]=0\); since \(V\ge0\), it follows that \(\mathbb E[d(A+V,B;Y,C)]\ge0\). Strictness follows on the positive-probability event \(A=B=C=0\), \(V>0\), \(Y>0\), where \(d(V,0;Y,0)-d(0,0;Y,0)=\min(V,Y)>0\). For the desired \(Y=(Z)_+\), each extra block contributing to \(C\) equals zero with strictly positive probability, so this event applies. All expectations are finite. This proves strict width increase under each outward integer transfer.

**Sharp global extremizers.** Repeatedly transfer one vertex from a part of size at least two to a strictly smaller part when their sizes differ by at least two; reversing this balancing operation strictly reduces width. Every profile reaches one whose entries differ by at most one, establishing the unique minimizing orbit. Conversely, repeatedly transfer one vertex from any non-largest part of size at least two to a largest part; each transfer strictly raises width and reaches \((N-r+1,1,\ldots,1)\), giving the unique maximizing orbit. The degenerate case \(N=r\) has one profile and is included.

**Critical multiblock limit.** Write \(\mu=\mathbb E(Z)_+\), \(\sigma^2=\operatorname{Var}((Z)_+)\). Independently for the \(r\) blocks, the central limit theorem yields jointly
\[
\left(\frac{S_{n_i}-\mu N/r}{\sqrt N}\right)_{i=1}^r\Longrightarrow
\left(\mu c_i+\frac{\sigma}{\sqrt r}G_i\right)_{i=1}^r.
\]
Since \(r\) is fixed, \(\max_i|S_{n_i}-\mu N/r|/\sqrt N\) is uniformly bounded in \(L^2\) for profiles in this critical window, by the independent sum variance identity and the bounded normalized deterministic shifts. Hence expectations of maxima converge. Furthermore \(\mathbb E\|g\|/\sqrt N\to1\), and its relative error is \(O(1/N)\); division of the exact Gaussian width formula proves the \(o(1)\) assertion.

For every pair of distinct shift vectors whose difference is not a common constant, Gaussian full support gives positive probability that their maximizing indices differ (choose two coordinates whose relative shifts change and push the others sufficiently negative). Since the pointwise maximum of affine functions is strictly below its chord at points where the endpoint maximizing indices differ, its expectation is strictly convex modulo the common-translation direction. Therefore \(F_r\) is strictly convex on \(\sum_i c_i=0\); permutation symmetry and averaging over all permutations imply its unique minimum is zero. For three independent standard normals, integrating their density gives \(\mathbb E\max(G_1,G_2,G_3)=3/(2\sqrt\pi)\), whence the explicit balanced constant.

**Macroscopic limit and extremal ratio.** If \(n_i/N\to\alpha_i\), then \(S_{n_i}/N\to\mu\alpha_i\) in \(L^2\), even when \(\alpha_i=0\), since \(\operatorname{Var}(S_{n_i})\le\sigma^2N\). With fixed \(r\), the maximum converges in \(L^1\) to \(\mu\max_i\alpha_i\). The Gaussian radius is asymptotic to \(\sqrt N\). This proves \(w(P_{\mathbf n})/\sqrt N\to2\mu\max_i\alpha_i\). The minimizing balanced profile has limit \(\max\alpha_i=1/r\), whereas the maximizing one has limit 1; dividing yields the limiting extremal ratio \(r\). This completes the proof.

## Verification
A standalone Python 3 program, `verify_multipartite.py`, is included. It checks the support formula directly against independently enumerated vertices for profiles with three and four blocks; tests 1,980 strict transfers in an exact rational Bernoulli positive-part surrogate; and compares the Gaussian critical-window formula with 150,000 reproducibly seeded Gaussian samples using independent normal-max quadrature. It also checks the balanced three-block constant. Successful output begins `VERIFY_OK`. These finite tests are corroborations of the proved identities and do not establish the infinite theorem or priority.

## Relationship to prior work
The original stable-set polytope construction and its vertex theory are classical; Aliniaeifard–Benedetti–Bergeron–Li–Saliola [1] analyze its 1-skeleton and diameter rather than Euclidean mean widths. Ahmad–Fourier–Joswig [2] analyze face-number inequalities for order and chain polytopes of maximal ranked posets. The chain polytope of a two-level complete poset is the stable-set polytope of a complete bipartite graph; reflecting one block shows it is congruent to the corresponding two-level **order** polytope. Accordingly the earlier exact bipartite mean-width and folded-normal result is already known and is **not** claimed here. The theorem above instead covers every number \(r\ge3\) of independent classes and its genuinely \(r\)-way Gaussian maximum, strict fixed-\(r\) majorization law and sharp asymptotic extremal ratio.

General Gaussian support-function techniques for regular polytopes appear in [3] but do not imply this multipartite strict comparison. Accessible closely related geometric statements about ellipsoids, minimum enclosing spheres and symmetric-edge polytopes concern different functionals. No exhaustive priority assertion is made.

## Limitations
The theorem is about standard unweighted complete multipartite **stable-set** polytopes, fixed finite number of blocks, and the specified canonical Euclidean embedding; it makes no statement about arbitrary graph stable-set polytopes, general edge-weighted profiles, a growing number of blocks, higher intrinsic volumes or uniqueness of the result throughout inaccessible literature. Its strict Schur-convexity is in positive integer part sizes and does not assert strict convexity of an interpolating width for noninteger sizes. The width limit concerns expectations, not a rate or a functional central limit theorem. External independent mathematical validation has not yet occurred. An older probabilistic reformulation of the width inequality may exist outside the inspected literature.

## References
[1] Farid Aliniaeifard, Carolina Benedetti, Nantel Bergeron, Shu Xiao Li and Franco Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (version 1 submitted April 2, 2018). The accessible revised full PDF (2021, 21 pp.), especially Sections 2–3, Theorem 4 and later sections, concerns 0/1 vertices, edges, and graph diameters, not Euclidean mean width.

[2] Ibrahim Ahmad, Ghislain Fourier and Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626 (version 1 submitted September 4, 2023). The accessible revised full PDF (16 pp.), Definitions 2.2 and 3.1, Theorem 4.1 and Corollary 4.2, concerns face combinatorics and \(f\)-vector inequalities, not mean width.

[3] Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, Journal of Mathematical Sciences 225 (2017), 770–787, DOI:10.1007/s10958-017-3492-3. Relevant background for Gaussian-width formulas of classical regular polytopes, not a multipartite stable-set extremal theorem.
