# A singular covariance transition for cycle counts in Ewens derangements

## Finding

Let \(\theta>0\), let \(n\ge r+s\), and fix distinct integers \(2\le r<s\). Choose a permutation of \(\{1,\ldots,n\}\) without fixed points with probability proportional to \(\theta^{K}\), where \(K\) is its number of cycles. Let \(C_r,C_s\) count its cycles of the indicated lengths. Define
\[
Z_m(\theta)=[z^m]\exp\!\left(\theta\sum_{j\ge2}\frac{z^j}{j}\right),\quad m\ge0.
\]
Then \(Z_0=1\), \(Z_1=0\), and \(Z_m>0\) for \(m\ge2\). The mixed covariance is
\[
\operatorname{Cov}(C_r,C_s)=\frac{\theta^2}{rs}\frac{Z_n Z_{n-r-s}-Z_{n-r}Z_{n-s}}{Z_n^2}. \tag{1}
\]
The following **qualitative and quantitative dependence transition** holds for every fixed pair of distinct lengths.

1. **Uniform derangements:** when \(\theta=1\), for every finite \(n\ge r+s\),
\[
\operatorname{sgn}\operatorname{Cov}(C_r,C_s)=(-1)^{n-r-s}.
\tag{2}
\]
There is no zero-covariance case. As \(u=n-r-s\to\infty\),
\[
\operatorname{Cov}(C_r,C_s)
=\frac{(-1)^u e}{rs(u+1)!}\left(1+O_{r,s}(u^{-1})\right).
\tag{3}
\]
2. **Nonunit Ewens weights:** if \(\theta\ne1\), as \(n\to\infty\) with \(\theta,r,s\) fixed,
\[
\operatorname{Cov}(C_r,C_s)
=\frac{\theta^2(1-\theta)}{n^2}+O_{\theta,r,s}(n^{-3}).
\tag{4}
\]
Consequently all such covariances are eventually positive when \(0<\theta<1\), and eventually negative when \(\theta>1\). Their leading coefficient is independent of the two cycle lengths, in contrast with the exceptional factorially small, parity-alternating case \(\theta=1\).

## Assumptions and scope

The sampling law is the Ewens cycle-weight measure **conditioned to have no one-cycles**. Each derangement \(\pi\) of size \(n\) has probability \(\theta^{K(\pi)}/(n!Z_n(\theta))\). The lengths \(r,s\) are distinct and fixed when asymptotic notation is used; all finite-size assertions concern \(n\ge r+s\) and \(r,s\ge2\). The covariance of a cycle count with itself is a variance and is not covered by (2)–(4). At \(n-r-s=1\), two such cycles cannot coexist, explaining one of the negative cases. The limit in (4) is pointwise in \(\theta\), not uniform as \(\theta\to1\).

## Proof

**Exact identity.** The exponential formula for weighted permutations gives the displayed definition of \(Z_m\). Marking one \(r\)-cycle and then separately one \(s\)-cycle gives the factorial-moment identities
\[
\mathbb E C_r=\frac{\theta}{r}\frac{Z_{n-r}}{Z_n},\quad
\mathbb E C_s=\frac{\theta}{s}\frac{Z_{n-s}}{Z_n},\quad
\mathbb E(C_r C_s)=\frac{\theta^2}{rs}\frac{Z_{n-r-s}}{Z_n}.
\]
Their difference proves (1). Differentiating the generating function also gives the independent recurrence
\[
Z_0=1,\quad Z_1=0,\quad (m+1)Z_{m+1}=mZ_m+\theta Z_{m-1}\quad(m\ge1).
\tag{5}
\]

**Strict finite parity law.** At \(\theta=1\), put \(d_m=Z_m(1)=\sum_{j=0}^m(-1)^j/j!\). In particular \(d_0=1\), \(d_1=0\), and \(1/3\le d_m\le1/2\) for all \(m\ge2\). Set \(u=n-r-s\); the numerator determining the sign in (1) becomes
\[
B_u=d_{u+r+s}d_u-d_{u+r}d_{u+s}.
\]
For \(u=0\), \(B_0\ge1/3-1/4>0\); for \(u=1\), \(B_1=-d_{r+1}d_{s+1}<0\). For \(u\ge2\), introduce \(w_k=d_{k+s}/d_k\). By the strictly decreasing alternating factorial terms,
\[
\operatorname{sgn}(w_k-1)=(-1)^{k+1},\qquad
\left|d_{k+s}-d_k\right|=\sum_{j=1}^{s}\frac{(-1)^{j-1}}{(k+j)!}.
\]
Writing \(a_k=|w_k-1|\), the alternating-series bounds and the bounds on \(d_k\) yield
\[
a_k\ge 2\left(\frac1{(k+1)!}-\frac1{(k+2)!}\right)
=\frac{2(k+1)}{(k+2)!},\qquad
 a_{k+1}\le\frac3{(k+2)!}.
\]
Therefore \(a_{k+1}<a_k\) for all \(k\ge2\), regardless of \(s\). The sequence \(w_k\) oscillates about one with strictly decreasing deviations. It follows for every \(r\ge1\) that \(w_{u+r}>w_u\) when \(u\) is even and \(w_{u+r}<w_u\) when \(u\) is odd. Since
\[
B_u=d_{u+r}d_u(w_{u+r}-w_u),
\]
this proves (2), including its strictness and all boundary cases.

**Exceptional factorial scale.** Taylor's alternating remainder at one gives
\[
d_m-e^{-1}=\frac{(-1)^m}{(m+1)!}\left(1+O(m^{-1})\right).
\]
With fixed \(r,s\ge2\), the other remainder terms in \(B_u\) are of smaller factorial order. Consequently
\[
B_u=\frac{(-1)^u e^{-1}}{(u+1)!}\left(1+O_{r,s}(u^{-1})\right).
\]
As \(d_n\to e^{-1}\), substitution in (1) proves (3).

**Nonunit scale.** The generating function is
\[
\sum_{m\ge0}Z_m(\theta)z^m=e^{-\theta z}(1-z)^{-\theta}.
\]
Expanding the analytic factor around its sole dominant singularity \(z=1\), then applying the gamma-ratio expansion to each singular term, gives an arbitrarily long inverse-power expansion (for fixed \(\theta>0\)); in particular
\[
Z_m(\theta)=\frac{e^{-\theta}}{\Gamma(\theta)}m^{\theta-1}
\left(1+\frac{3\theta(\theta-1)}{2m}+\frac{c_2(\theta)}{m^2}+O_\theta(m^{-3})\right).
\tag{6}
\]
For positive integer \(\theta\), the same expansion follows by separating the finite principal part at \(z=1\) from an entire remainder with factorially small coefficients. In logarithms, the mixed finite difference therefore satisfies
\[
\log\frac{Z_nZ_{n-r-s}}{Z_{n-r}Z_{n-s}}
=-\frac{(\theta-1)rs}{n^2}+O_{\theta,r,s}(n^{-3}).
\]
Also \(Z_{n-r}Z_{n-s}/Z_n^2=1+O_{\theta,r,s}(n^{-1})\). Exponentiating and substituting into (1) proves (4). The coefficient is nonzero precisely when \(\theta\ne1\), completing the eventual sign statements.

## Verification

The standalone Python 3 file `verify.py` uses only the standard library. Running `python3 verify.py` checks the normalizer via an independently expressed coefficient recurrence, enumerates all derangements through eight symbols under three rational Ewens weights, checks the first and mixed cycle-count moments against direct weighted enumeration, and checks all parity signs for \(2\le r<s\le9\) (with \(r\le8\)) and \(0\le n-r-s\le64\). It also checks the nonunit leading asymptotic numerically at \(n=300\) for four rational weights and three pairs of lengths. The observed output was `PASS: 2003 exact integer/rational assertions and asymptotic numerical comparisons`. These finite checks complement, but do not replace, the all-size proof above.

## Relationship to prior work

Betz, Ueltschi and Velenik (2009) studied cycle-weighted random permutations and their normalizing generating functions; the present derangement weight choice specializes their framework to no one-cycles. Da Silva, Jamshidpey and Tavaré (2020) explicitly derived factorial moments and marginal cycle-count laws for Ewens derangements: those published formulas **already entail equation (1)**, so (1) is not claimed as independently novel. The contribution examined here is the **strict all-size sign alternation** at unit weight, its factorial scale, and the explicit nonunit \(n^{-2}\) sign regime with the exceptional singular parameter identified. Neither inspected primary account states those refinements. Their possible implicit derivability from broader asymptotic methods is an acknowledged priority limitation.

## Limitations

The nonunit sign is only eventual and depends on the fixed parameter; no global finite-size sign threshold is asserted for \(\theta\ne1\). Neither estimate is uniform over moving cycle lengths or parameters approaching one with sample size. Strict alternation concerns **covariance**, not association, independence, stochastic monotonicity or any causal relationship. Finite verification cannot establish historical novelty. The mixed-moment formula is previously known, and additional earlier work may imply the refined results; independent priority assessment remains necessary.

## References

- V. Betz, D. Ueltschi and Y. Velenik, *Random permutations with cycle weights*, arXiv:0908.2217v1 (public August 17, 2009), https://arxiv.org/abs/0908.2217; Annals of Applied Probability 21 (2011), 312–331.
- P. H. da Silva, A. Jamshidpey and S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840v1 (public June 8, 2020), https://arxiv.org/abs/2006.04840; see equations (5)–(7) for the published normalization and factorial moments.
