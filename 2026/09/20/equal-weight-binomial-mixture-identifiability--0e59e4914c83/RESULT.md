# Exact identifiability threshold for equal-weight binomial mixtures with known anchors

## Statement

Let
\[
G=\frac1K\sum_{i=1}^K \delta_{p_i},
\qquad 0\le p_i\le 1,
\]
where the \(K\) support points are distinct. Conditional on \(P\sim G\), observe
\[
X\mid P\sim \operatorname{Bin}(N,P).
\]
Thus the marginal law of \(X\) is an equal-weight mixture of \(K\) binomial distributions with the same trial count \(N\).

Suppose \(r\) distinct support locations
\[
A=\{a_1,\ldots,a_r\}\subset[0,1]
\]
are known in advance to belong to \(\operatorname{supp}(G)\), while the remaining \(M=K-r\) support locations are unknown. The weights remain fixed at \(1/K\).

### Theorem — exact threshold

If \(M=0\), the mixing distribution is already known from the anchors.

If \(M\ge 1\), the class is globally identifiable from the marginal law of \(X\) if and only if
\[
\boxed{N\ge M=K-r.}
\]

Equivalently, in the unanchored case \(r=0\), an equal-weight \(K\)-component binomial mixture is identifiable already at
\[
\boxed{N\ge K,}
\]
rather than the classical unrestricted-mixture threshold \(N\ge 2K-1\).

The lower bound is global and sharp: for every fixed anchor set \(A\) with \(r<K\), there are two distinct equal-weight \(K\)-atomic mixing distributions containing all anchors that induce exactly the same binomial-mixture law whenever \(N\le K-r-1\).

## Why the binomial law is a truncated moment sequence

Write
\[
m_j(G)=\int_0^1 p^j\,dG(p).
\]
For \(1\le j\le N\),
\[
\mathbb E[(X)_j]=(N)_j\,m_j(G),
\]
where \((x)_j=x(x-1)\cdots(x-j+1)\). Hence the law of \(X\) determines
\[
m_1(G),\ldots,m_N(G).
\]

Conversely each binomial-mixture probability
\[
\Pr(X=x)=\binom Nx\int_0^1p^x(1-p)^{N-x}\,dG(p)
\]
is the integral of a polynomial of degree at most \(N\). Therefore two mixing distributions induce the same law of \(X\) exactly when their raw moments agree through degree \(N\).

This turns the question into a finite moment-identification problem.

## Proof of sufficiency

Let the unknown support points be
\[
u_1,\ldots,u_M.
\]
Because every component has known weight \(1/K\),
\[
K\,m_j(G)-\sum_{a\in A}a^j
   =\sum_{i=1}^M u_i^j
   =:s_j.
\]

If \(N\ge M\), the data therefore determine the first \(M\) power sums
\[
s_1,\ldots,s_M
\]
of the unknown support points.

Let \(e_j\) denote the \(j\)-th elementary symmetric polynomial in
\(u_1,\ldots,u_M\), with \(e_0=1\). Newton's identities give recursively
\[
j e_j=\sum_{\ell=1}^j(-1)^{\ell-1}e_{j-\ell}s_\ell,
\qquad j=1,\ldots,M.
\]
Thus \(e_1,\ldots,e_M\) are uniquely determined.

Consequently the monic polynomial
\[
Q(t)=\prod_{i=1}^M(t-u_i)
=t^M-e_1t^{M-1}+e_2t^{M-2}-\cdots+(-1)^M e_M
\]
is uniquely determined. Its multiset of roots is exactly the unknown support.
Since the support points are distinct, this determines \(G\) uniquely.

Hence \(N\ge K-r\) is sufficient.

## Proof of sharpness

Assume \(M=K-r\ge1\). Because the anchor set is finite, choose an open interval
\[
I\subset(0,1)
\]
that contains no anchor. Pick \(M\) distinct points
\[
u_1,\ldots,u_M\in I
\]
and form
\[
Q(t)=\prod_{i=1}^M(t-u_i).
\]

All roots are simple and lie in the interior of \(I\). Therefore, for sufficiently small nonzero real \(\varepsilon\), the perturbed polynomial
\[
Q_\varepsilon(t)=Q(t)+\varepsilon
\]
still has \(M\) distinct real roots
\[
v_1,\ldots,v_M\in I.
\]
The two root multisets are different because \(Q_\varepsilon\ne Q\).

Only the constant coefficient changed. Hence the elementary symmetric functions
\[
e_1,\ldots,e_{M-1}
\]
of \(\{u_i\}\) and \(\{v_i\}\) are identical. Newton's identities then imply
\[
\sum_{i=1}^M u_i^j
=
\sum_{i=1}^M v_i^j,
\qquad j=1,\ldots,M-1.
\]

Define
\[
G_u=\frac1K\left(\sum_{a\in A}\delta_a+\sum_{i=1}^M\delta_{u_i}\right),
\qquad
G_v=\frac1K\left(\sum_{a\in A}\delta_a+\sum_{i=1}^M\delta_{v_i}\right).
\]
They are distinct equal-weight \(K\)-atomic probability measures, both contain every prescribed anchor, and satisfy
\[
m_j(G_u)=m_j(G_v),\qquad j=0,1,\ldots,M-1.
\]
Therefore they induce the same mixture of \(\operatorname{Bin}(N,p)\) laws for every
\[
N\le M-1=K-r-1.
\]

This proves necessity and the exact threshold.

## Exact example

Take \(K=4\), one known anchor \(A=\{0.9\}\), and compare the two unknown triples
\[
U=\{0.1,0.5,0.6\},\qquad
V=\{0.2,0.3,0.7\}.
\]
They satisfy
\[
\sum_{u\in U}u=\sum_{v\in V}v=1.2
\]
and
\[
\sum_{u\in U}u^2=\sum_{v\in V}v^2=0.62.
\]
Hence the equal-weight four-atom measures on \(A\cup U\) and \(A\cup V\) have the same first two raw moments:
\[
m_1=0.525,\qquad m_2=0.3575.
\]
For \(N=2\) both therefore give exactly
\[
\Pr(X=0)=0.3075,\qquad
\Pr(X=1)=0.335,\qquad
\Pr(X=2)=0.3575.
\]
The supports are different, so \(N=2\) is not enough. The theorem says \(N=3\) is enough, since \(K-r=3\).

## Consequences

### 1. Uniform \(K\)-coin models need only \(K\) grouped Bernoulli observations

The usual \(K\)-coin model draws a latent coin and then observes conditionally iid Bernoulli trials. With arbitrary latent weights, the associated sparse Hausdorff moment problem has the familiar \(2K-1\)-moment identifiability scale. If the latent class is known to be uniform, the theorem gives exact identification from only the first \(K\) moments, equivalently from \(K\) conditionally iid Bernoulli observations in one group.

### 2. Known support locations save one trial each

In the equal-weight model, every known support location removes one unknown root of the support polynomial. The exact trial threshold falls from \(K\) to \(K-r\).

### 3. The gain comes from symmetry, not merely parameter counting

For arbitrary unknown mixture weights, recovering support and weights is a Prony-type problem with roughly twice as many degrees of algebraic freedom. Equal weights collapse the moment equations to ordinary power sums, and Newton's identities recover the support polynomial directly. This is why the unrestricted \(2K-1\) threshold does not remain sharp on the equal-weight submodel.

## Relation to prior literature

Blischke's 1964 analysis of mixtures of binomial distributions states identifiability under the classical condition \(N\ge 2K-1\) for unrestricted component weights. Modern reviews likewise record nonidentifiability below \(2K-1\) for the unrestricted binomial-mixture class.

The sparse Hausdorff moment / \(K\)-coin literature studies recovery of a \(K\)-spike distribution from moments when both spike locations and weights are unknown. Gordon, Mazaheri, Schulman and Rabani (2020) and Fan and Li (2023) give recovery algorithms and stability analyses in that unrestricted-weight setting.

The present result concerns the strictly smaller equal-weight model and gives a different exact global threshold, including the anchored extension and a matching construction below threshold. The proof is elementary once the equal-weight restriction is recognized: factorial moments reduce the binomial observation to power sums, and Newton's identities recover the support polynomial.

## Limitations

- The theorem assumes the number \(K\) of distinct components is known and every mixing weight is exactly \(1/K\).
- It is an exact identifiability result. It does not by itself provide a noise-robust recovery rate; root recovery can be ill-conditioned when support points are close.
- The anchors are exact support locations. Approximate anchor information is not covered.
- The result does not claim that equal-weight restrictions improve identifiability for arbitrary component families; the proof uses the polynomial-moment structure of the binomial family.
- Originality is asserted only to the best of our knowledge. The equal-weight proof is closely connected to classical Newton identities and finite moment theory, so an equivalent formulation may exist outside the mixture-model terminology searched.

## References

1. W. R. Blischke, “Estimating the Parameters of Mixtures of Binomial Distributions,” *Journal of the American Statistical Association* 59 (1964), 510–528. https://doi.org/10.1080/01621459.1964.10482176
2. H. Teicher, “Identifiability of Finite Mixtures,” *Annals of Mathematical Statistics* 34 (1963), 1265–1269. https://doi.org/10.1214/AOMS/1177703862
3. G. J. McLachlan, S. X. Lee, S. I. Rathnayake, “Finite Mixture Models,” *Annual Review of Statistics and Its Application* 6 (2019), 355–378. https://doi.org/10.1146/annurev-statistics-031017-100325
4. S. Gordon, B. Mazaheri, L. J. Schulman, Y. Rabani, “The Sparse Hausdorff Moment Problem, with Application to Topic Models,” arXiv:2007.08101 (2020). https://arxiv.org/abs/2007.08101
5. Z. Fan, J. Li, “Efficient Algorithms for Sparse Moment Problems without Separation,” *Proceedings of COLT 2023*, PMLR 195, 3510–3565. https://proceedings.mlr.press/v195/fan23b.html
6. S. L. Gordon, M. Kant, E. Ma, L. J. Schulman, A. Staicu, “Identifiability of Product of Experts Models,” arXiv:2310.09397 (2023). https://arxiv.org/abs/2310.09397
