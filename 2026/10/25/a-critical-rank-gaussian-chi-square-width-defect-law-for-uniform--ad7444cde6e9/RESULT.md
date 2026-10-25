# A critical-rank Gaussian–chi-square width-defect law for uniform-matroid independence polytopes

## Finding
For every integer \(n\ge2\) and \(1\le k\le n\), let
\[
I_{n,k}=\{x\in[0,1]^n:\textstyle\sum_{i=1}^n x_i\le k\},\qquad C_n=[0,1]^n.
\]
Write \(W_K(u)=h_K(u)+h_K(-u)\) for the length of the orthogonal projection of \(K\) onto a unit direction \(u\), and let \(U_n\) be uniform on the sphere in \(\mathbb R^n\). Let integer ranks \(k_n\) obey
\[
c_n=\frac{k_n-n/2}{\sqrt n}\longrightarrow c\in\mathbb R.
\]
Put \(\mu=\sqrt{2/\pi}\), \(a=\sqrt{2/\pi}\), and for \(z\in\mathbb R\) define
\[
Q_c(z)=\frac1a\left[\left(\frac z2-c\right)_+^2+\left(-\frac z2-c\right)_+^2\right],\qquad t_+=\max(t,0).
\]
If \(Z\sim N(0,1)\) and \(Y\sim N(0,1-3/\pi)\) are independent, then the **joint two-scale geometric limit** is
\[
\boxed{\left(W_{C_n}(U_n)-\mu\sqrt n,\quad \sqrt n\bigl(W_{C_n}(U_n)-W_{I_{n,k_n}}(U_n)\bigr)\right)\Longrightarrow\bigl(Y,Q_c(Z)\bigr).}
\]
The first component is the classical cube-width fluctuation; the new geometric information is the correlated two-sided rank-trimming defect at a finer scale, including its asymptotic independence from the first component. At the critical center \(c=0\), the second limit is exactly \(\chi_1^2/(4a)\). For \(c>0\), this second law acquires an atom at zero of mass \(2\Phi(2c)-1\), whereas for \(c\le0\) it has no atom at zero.

There is also an **exact finite-dimensional equality criterion**. For all admissible \(n,k\),
\[
\Pr\bigl\{W_{I_{n,k}}(U_n)=W_{C_n}(U_n)\bigr\}
=2^{-n}\!\sum_{j=n-k}^{k}\binom nj,
\]
where a sum whose lower index exceeds its upper index is defined to be zero. In the critical scaling this probability tends to \(2\Phi(2c)-1\) for \(c>0\) and to zero for \(c\le0\). In particular, the probability that the cap is *completely invisible to directional width* has a sharp square-root-rank window.

## Assumptions and scope
All widths use the inherited ambient Euclidean metric, not the lattice-affine metric on a lifted generalized permutohedron. Both bodies have full affine dimension for \(1\le k\le n\). The sphere is measured with normalized rotation-invariant surface measure. Convergence is weak convergence of real random vectors; no claim of almost-sure convergence or convergence of moments of the scaled defect is made. The statement covers every sequence of integer ranks with the given finite real limit \(c\), including parity effects absorbed in \(c_n\). Independent Gaussian variables \(Y,Z\) in the limiting statement mean independence of the limiting **two components**, not independence of the finite-dimensional widths.

## Proof
**1. Exact support functions and the loss.** Let \(G_1,\ldots,G_n\) be independent standard Gaussian variables. Their normalized vector \(G/\|G\|_2\) is uniform on the sphere. The extreme-point description of \(I_{n,k}\) gives
\[
h_{I_{n,k}}(G)=\sum_{j=1}^{\min(k,B)}G_{(j)}^+,
\]
where \(B=\#\{i:G_i>0\}\) and the \(G_{(j)}^+\) are the positive coordinates in decreasing order. The cube support is the sum of all positive coordinates. Hence if \(L_+\) is the sum of the \((B-k)_+\) *smallest* positive coordinates, and \(L_-\) is the sum of the \((n-B-k)_+\) smallest absolute values among negative coordinates, then exactly
\[
W_{C_n}(G/\|G\|_2)-W_{I_{n,k}}(G/\|G\|_2)=\frac{L_++L_-}{\|G\|_2}.\tag{1}
\]
Every nonempty trimming sum is strictly positive almost surely. Therefore equality in (1) holds if and only if \(B\le k\) and \(n-B\le k\). Since \(B\sim\operatorname{Bin}(n,1/2)\), this proves the finite binomial formula without approximation.

**2. A small-order-statistic lemma at the central rank.** Conditional on any sign pattern, the absolute Gaussian coordinates in the two sign groups are independent samples from the half-normal distribution \(F(t)=2\Phi(t)-1\), \(t\ge0\). Its density at the origin is \(a=F'(0)=\sqrt{2/\pi}\), and its inverse satisfies \(F^{-1}(v)=v/a+O(v^2)\) as \(v\downarrow0\). For a half-normal sample of size \(b\), suppose \(b/n\to1/2\) and \(0\le m\le K\sqrt n\), with fixed \(K\). If \(X_{(1)}\le\cdots\le X_{(b)}\) are its order statistics, then
\[
\sup_{0\le m\le K\sqrt n}\left|\sum_{j=1}^{m}X_{(j)}-\frac{m^2}{2ba}\right|\ \xrightarrow{\Pr}\ 0.\tag{2}
\]
To verify (2) directly, transform by \(F\): the ordered uniforms admit the exponential-spacing representation \(V_{(j)}=S_j/S_{b+1}\), with \(S_j=E_1+\cdots+E_j\) for independent unit exponentials \(E_i\). Uniformly for \(j\le K\sqrt n\), Kolmogorov's maximal inequality gives \(\max_{j\le K\sqrt n}|S_j-j|=O_{\Pr}(n^{1/4})\), while \(S_{b+1}/b\to1\) in probability. Consequently
\[
\sup_{m\le K\sqrt n}\left|\sum_{j\le m}V_{(j)}-\frac{m(m+1)}{2b}\right|=o_{\Pr}(1).
\]
Moreover, \(\max_{j\le K\sqrt n}V_{(j)}=O_{\Pr}(n^{-1/2})\), so the aggregate inverse-CDF error is \(O_{\Pr}(\sqrt n\,n^{-1})=o_{\Pr}(1)\). Replacing \(m(m+1)\) by \(m^2\) costs \(O(n^{-1/2})\). This proves (2). The same argument applies conditionally to both sign groups and is uniform when both sizes lie in \([n/3,2n/3]\), an event of probability tending to one.

**3. Trimming limit.** Put \(Z_n=2(B-n/2)/\sqrt n\). The binomial central limit theorem gives \(Z_n\Longrightarrow Z\sim N(0,1)\), and \(B/n\to1/2\) in probability. From the rank assumption, both trimming counts are \(O_{\Pr}(\sqrt n)\). Applying (2) after truncating at an arbitrarily large fixed \(K\) yields
\[
L_++L_-=\frac{(B-k_n)_+^2+(n-B-k_n)_+^2}{na}+o_{\Pr}(1)
=Q_{c_n}(Z_n)+o_{\Pr}(1).\tag{3}
\]
The law of large numbers gives \(\|G\|_2/\sqrt n\to1\) in probability. Combining (1) and (3) therefore proves the second marginal limit \(\sqrt n(W_C-W_I)\Longrightarrow Q_c(Z)\).

**4. Cube fluctuations and asymptotic independence.** The classical cube-width identity is
\[
W_{C_n}(G/\|G\|_2)=\frac{\sum_i|G_i|}{\sqrt{\sum_iG_i^2}}.
\]
A two-variable Taylor expansion at the Gaussian means \(\mathbb E|G_i|=\mu\) and \(\mathbb EG_i^2=1\) gives
\[
W_{C_n}-\mu\sqrt n=\frac1{\sqrt n}\sum_{i=1}^n\left[|G_i|-\mu-\frac\mu2(G_i^2-1)\right]+o_{\Pr}(1).\tag{4}
\]
The bracketed summands are centered and have variance \(1-3/\pi>0\), using \(\mathbb E|G_i|^3=2\mu\). Thus the ordinary central limit theorem gives the first marginal limit \(Y\). For every \(n\), the vector of Gaussian signs is independent of the vector of absolute values; hence \(Z_n\) is independent of the left-hand side of (4) *exactly*. Equation (3) makes the scaled loss a continuous function of \(Z_n\) up to an error tending to zero in probability. The joint central limit theorem and Slutsky's theorem yield the claimed pair \((Y,Q_c(Z))\) with independent components.

**5. The transition and its zero atom.** At \(c=0\), \((z/2)_+^2+(-z/2)_+^2=z^2/4\), giving \(Q_0(Z)=Z^2/(4a)\). If \(c>0\), \(Q_c(Z)=0\) precisely when \(-2c\le Z\le2c\), so its atom has mass \(2\Phi(2c)-1\). For \(c=0\) the sole zero of the continuous variable \(Z\) has probability zero, while for \(c<0\) the two positive-part squares cannot vanish simultaneously. Finally the exact binomial equality probability from step 1 converges to the same atom mass by the central limit theorem, including zero for \(c\le0\). This completes the proof.

## Verification
The accompanying standalone `verify.py` requires Python's standard library only. Run `python3 verify.py`. It enumerates the Boolean vertices for \(1,400\) independent finite support-function comparisons across dimensions \(2\) through \(8\), checks the exact identity (1) and the zero-defect criterion in every case, and performs \(1,080\) seeded Gaussian diagnostics across three sizes and three rank offsets. On the executed checker, the large-size mean absolute errors in approximating the normalized loss by its quadratic conditional-sign formula were \(0.037916\), \(0.001440\), and \(0.186640\) at offsets \(c=0\), \(0.75\), and \(-0.75\), respectively, for dimension \(4,096\). These diagnostics cannot prove weak convergence, which follows from the proof above. The classical cube variance and balanced-limit mean evaluate numerically to \(0.045070341449\) and \(0.313328534329\).

## Relationship to prior work
Ferroni and McGinnis establish the exact indicator-coordinate independence-polytope realization as a special fat prism slice and study lattice-point enumeration, Ehrhart positivity, and related generalized-permutahedron constructions [1]; their inspected full text, especially Section 6.3, contains no random-width or signed Gaussian-order-statistic theorem. Ferroni's earlier paper [2] proves Ehrhart positivity through half-open hypersimplices, not this metric law. Kabluchko, Litvak and Zaporozhets [3] already prove the Gaussian cube-width marginal in (4); that marginal is used as a known baseline, not claimed to be new. The rank-constrained loss is distinct from a hypersimplex's fixed-cardinality width: the independence polytope optimizes over *all* allowed cardinalities and trims only excess positive/negative coordinates.

Existing exact Euclidean radius and John-ellipsoid formulas for the same capped cube [4,5] locate deterministic geometric transitions but imply neither the random directional equality probability nor the finer chi-square/atomic joint width-defect law. A previously available hypersimplex width central limit theorem [6] works at order-one fluctuations and does not determine this smaller-order cap-versus-cube difference. More general one-sided normal-order-statistic facts are tools in step 2; the joint spherical normalization, rank-window comparison and atom law are separate geometric conclusions.

## Limitations
This theorem is specific to equal coordinate capacities, uniform matroids, unit Gaussian/spherical directions, and integer ranks with bounded centered square-root scaling. It does not assert a universal result for unequal prisms, general matroids, fixed-cardinality hypersimplices, non-Gaussian directions, or rank offsets growing faster than \(\sqrt n\). No convergence rate, moment convergence of the scaled defect, or independent validation is claimed. An equivalent two-scale law under truncated-cube or random-cardinality-optimization terminology may exist outside the inspected sources; bibliographic nonmatches alone cannot prove uniqueness.

## References
1. L. Ferroni and D. McGinnis, *Lattice points in slices of prisms*, arXiv:2202.11808v1 (first public 2022-02-23), especially Sections 1.1, 2.1, 6.3; https://arxiv.org/abs/2202.11808.
2. L. Ferroni, *Integer point enumeration on independence polytopes and half-open hypersimplices*, arXiv:2012.04711v1 (first public 2020-12-08), Sections 1–3; https://arxiv.org/html/2012.04711v1.
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v3 (2016), Section 3.3; https://arxiv.org/html/1511.08479v3.
4. *Uniform-matroid independence polytopes have two exact Euclidean radius transitions*, public mathematical record `2026/10/11/SCOPE-uniform-matroid-independence-polytopes-have-two-exact-euclidean--7ec706524f8f`, RESULT.md.
5. *Three-phase John ellipsoid of a capped hypercube*, public mathematical record `2026/10/11/SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127`, RESULT.md.
6. *Nonmonotone Gaussian angular-width fluctuations of hypersimplices*, identified prior research result `fe20d5fa-3db3-4e73-9796-5d8811b471be` (available result claim).
