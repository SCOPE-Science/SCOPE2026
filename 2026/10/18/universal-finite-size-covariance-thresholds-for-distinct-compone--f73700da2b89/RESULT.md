# Universal finite-size covariance thresholds for distinct component classes in Erdős–Rényi graphs

## Finding

For an Erdős–Rényi graph \(G\sim G(n,p)\), fix two **different** component sizes \(1\le r\ne s\le n\), and any two nonempty prescribed classes of connected graphs on respectively \(r\) and \(s\) vertices. Let \(C_{r,A}\) and \(C_{s,B}\) count components in those classes. If \(r+s\le n\), then

\[
\frac{\mathbb E[C_{r,A}C_{s,B}]}{\mathbb E[C_{r,A}]\,\mathbb E[C_{s,B}]}
=\frac{(n-r)!(n-s)!}{n!(n-r-s)!}(1-p)^{-rs}.
\]

Consequently the covariance has **exactly one sign reversal**, at the explicit finite-size threshold

\[
p_{r,s}(n)=1-\left(\frac{(n-r)!(n-s)!}{n!(n-r-s)!}\right)^{1/(rs)}.
\]

The covariance is negative for \(0<p<p_{r,s}(n)\), zero exactly at the threshold, and positive for \(p_{r,s}(n)<p<1\). The threshold does not depend on either connected-component class. If \(r+s>n\), the covariance is strictly negative for all \(0<p<1\). Every admissible off-diagonal threshold satisfies \(p_{r,s}(n)>1/n\), so the entire off-diagonal covariance matrix has strictly negative entries at the classical critical probability \(p=1/n\). For fixed distinct positive integers \(r,s\),

\[
p_{r,s}(n)=\frac1n+\frac{r+s-2}{2n^2}+O_{r,s}(n^{-3}).
\]

The assertion includes ordinary component-size counts, tree-component counts and any other nonempty connected isomorphism types. It is a finite-size, type-independent sign classification, not a claim of new limiting Gaussian covariance theory.

## Assumptions and scope

The vertex set has size \(n\ge3\); all \(\binom n2\) edges occur independently with the same probability \(p\in(0,1)\). The two component sizes are distinct positive integers. A class \(A\) of connected graphs on \(r\) labeled vertices and class \(B\) on \(s\) labeled vertices are each invariant under vertex relabeling and nonempty. Hence their internal probabilities \(\theta_{r,A}(p)\), \(\theta_{s,B}(p)\) are positive for \(p\in(0,1)\). Singletons constitute their own connected class. The corresponding random variables count maximal connected components (not arbitrary induced connected subgraphs). The \(r+s>n\) case is treated separately from the factorial expression.

## Proof

Put \(q=1-p\). For each \(r\)-subset \(S\), the event that \(S\) induces a connected graph in \(A\) and forms an entire component has probability

\[
\theta_{r,A}(p)q^{r(n-r)}.
\]

Thus \(\mathbb E[C_{r,A}]=\binom nr\theta_{r,A}(p)q^{r(n-r)}>0\); similarly for the \(s\)-class. Since distinct graph components cannot intersect, expanding the mixed product counts only pairs of disjoint subsets \(S,T\). For such disjoint sets, internal edges of \(S\) and \(T\) are independent, and their total required absent external edges number

\[
r(n-r)+s(n-s)-rs.
\]

The subtraction avoids counting the \(rs\) edges between \(S\) and \(T\) twice. Hence for \(r+s\le n\),

\[
\mathbb E[C_{r,A}C_{s,B}]
=\binom nr\binom{n-r}s\theta_{r,A}(p)\theta_{s,B}(p)
q^{r(n-r)+s(n-s)-rs}.
\]

Dividing by the product of means cancels all type-dependent factors and yields the displayed universal ratio. Set

\[
R_{r,s}(n)=\frac{(n-r)!(n-s)!}{n!(n-r-s)!}.
\]

Because \(r,s\ge1\), \(r+s\le n\), and \(r\ne s\), one has \(0<R_{r,s}(n)<1\). The ratio \(R_{r,s}(n)q^{-rs}\) is strictly increasing in \(p\), starts below one at \(p=0\), and diverges as \(p\uparrow1\). Thus it crosses one once, at the stated \(p_{r,s}(n)\). Multiplication by the strictly positive product of the means preserves this sign classification. If \(r+s>n\), the two counts cannot simultaneously be positive, so their covariance equals minus their product of strictly positive means.

For the critical inequality, cancel factorials to obtain the exact telescoping product

\[
R_{r,s}(n)^{-1}=
\prod_{i=0}^{r-1}\prod_{j=0}^{s-1}
\frac{n-i-j}{n-i-j-1}.
\]

Every factor is at least \(n/(n-1)\), and at least one is strictly larger because distinct positive \(r,s\) give \(r+s\ge3\). Consequently \(R_{r,s}(n)<(1-1/n)^{rs}\), which implies \(p_{r,s}(n)>1/n\). For fixed \(r,s\), expand \(\log R_{r,s}(n)\) through order \(n^{-2}\) using this product:

\[
\frac1{rs}\log R_{r,s}(n)
=-\frac1n-\frac{r+s-1}{2n^2}+O_{r,s}(n^{-3}).
\]

Exponentiating and subtracting from one gives the stated threshold expansion. At \(p=1/n\) it is smaller than every allowed threshold and the covariance is therefore negative, with the disjointness case also negative. This completes the proof.

## Verification

`verify.py` uses exact rational arithmetic to enumerate every graph on \(3\), \(4\), or \(5\) vertices at edge probabilities \(1/5\), \(1/2\), \(4/5\), and every graph on \(6\) vertices at probabilities \(1/5\), \(1/2\). It compares mixed component-count moments against the exact ratio for all ordered distinct size pairs, for unrestricted connected components, trees and cliques, including mixed choices of component class. It independently checks the telescoping factorization and strict critical bound for every admissible pair with \(3\le n\le29\). Running `python verify.py` yields `VERIFY_OK 6982` (6,982 exact assertions). The universal result is justified by the combinatorial proof rather than these finite tests.

As a small check, at \(n=6\) and sizes \(r=1\), \(s=2\), the threshold is \(1-\sqrt{2/3}\), strictly above \(1/6\). Hence their covariance changes from negative to positive as \(p\) crosses this value, regardless of whether the size-two class is described as connected, tree, or clique (all coincide at size two).

## Relationship to prior work

Exact first moments and same-size factorial moments of tree-component counts, as well as Gaussian asymptotics, are classical; see Bollobás, *Random Graphs*, chapter 5, particularly Section 5.1. Pittel (1990) develops a tree census and asymptotic covariance structure: no novelty is asserted for the existence of asymptotic tree-count correlations or their asymptotic covariance. Ráth (2018) gives a component-size moment-generating formula for a **tagged vertex**; that is not the same as a two-class finite-size covariance sign classification. De Ambroggio and Roberts (2021 preprint) study near-critical unusually large components using ballot methods, not exact cross-size covariance thresholds. The contribution here is the uniform finite-\(n\) threshold for every pair of distinct sizes and every pair of positive-probability internal types, including its strict placement above \(1/n\).

## Limitations

The theorem concerns different sizes only: same-size variances have diagonal counting terms and do not satisfy this formula. It assumes independent edges of common probability and does not address inhomogeneous models or dependent-edge graphs. The old random-graph literature includes more general factorial-moment machinery from which the identity may be derivable; in particular full priority comparison with Pittel (1990) could not be completed, and no claim of independent historical verification is made. The finite checker is not a proof for unbounded \(n\).

## References

1. U. De Ambroggio and M. I. Roberts, *Unusually large components in near-critical Erdős–Rényi graphs via ballot theorems*, arXiv:2101.05358, first posted 13 January 2021. https://arxiv.org/abs/2101.05358
2. B. Ráth, *A moment-generating formula for Erdős–Rényi component sizes*, arXiv:1707.05169 (2017 preprint); *Electronic Communications in Probability* 23 (2018). https://arxiv.org/abs/1707.05169
3. B. Pittel, *On tree census and the giant component in sparse random graphs*, *Random Structures & Algorithms* 1 (1990). https://doi.org/10.1002/rsa.3240010306
4. B. Bollobás, *Random Graphs*, second edition, Cambridge University Press (2001), Chapter 5, Section 5.1. https://doi.org/10.1017/CBO9780511814068
