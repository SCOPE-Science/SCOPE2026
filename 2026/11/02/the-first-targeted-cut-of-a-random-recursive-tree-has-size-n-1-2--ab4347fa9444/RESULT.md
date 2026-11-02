# The first targeted cut of a random recursive tree has size \(n^{1/(2\log 2)+o_{\mathbb P}(1)}\)

## Finding
Let \(T_n\) be the uniform recursive tree with root \(1\), constructed by attaching each new vertex \(j\) independently to a uniformly chosen earlier vertex. Let \(V_n\) be **any** vertex whose number of children is maximal, with an arbitrary measurable rule for resolving ties. Let \(S_n\) count \(V_n\) and all its descendants (the whole fringe subtree deleted at the first step of degree-targeted cutting). Then
\[
 \frac{\log S_n}{\log n}\xrightarrow{\mathbb P}\frac{1}{2\log 2}.
\]
Equivalently, for every fixed \(\varepsilon>0\), \(\mathbb P(n^{1/(2\log 2)-\varepsilon}\le S_n\le n^{1/(2\log 2)+\varepsilon})\to1\). The conclusion holds simultaneously for every choice among tied maximum-child-count vertices.

## Assumptions and scope
The model is the uniform recursive rooted tree on labels \(\{1,\ldots,n\}\), not the uniform Cayley tree. Degrees count children, rather than undirected neighbors; these are the degrees used for targeted cutting in the motivating work. Let \(D_j\) be the number of children of vertex \(j\), \(S_j\) its fringe-subtree size, and \(\Delta_n=\max_jD_j\). The cut size means the removed fringe subtree *including its root*, not the number of edges removed, the number of repeated cuts, or the remaining root component.

Put \(c=1/\log2\), \(\mu=1-1/(2\log2)\), and \(a=1-\mu=c/2\). The only external probabilistic inputs are the established almost-sure localization of *all* maximum-child-count vertices at labels \(n^{\mu+o(1)}\), and the classical limit \(\Delta_n/\log n\to c\) in probability. References below identify these precise inputs.

## Proof
**1. Exact degree–fringe conditional law.** Fix \(j\ge2\). When a later vertex enters the descendant subtree of \(j\), its parent, conditional on that entry, is uniform among the vertices currently belonging to that subtree. The probability of a later entry depends only on its current size, not on its internal edges. Thus conditioning on the eventual size \(S_j=s\) leaves the internal parent choices distributed as a fresh uniform recursive tree of size \(s\). In particular,
\[
D_j\mid(S_j=s)\ \overset d=\sum_{r=1}^{s-1}B_r,
\qquad B_r\text{ independent},\quad \mathbb P(B_r=1)=1/r.
\]
For every \(t\ge0\), since \(1+x\le e^x\),
\[
\mathbb E[e^{tD_j}\mid S_j=s]
=\prod_{r=1}^{s-1}\left(1+\frac{e^t-1}{r}\right)
\le\exp((e^t-1)H_{s-1}). \tag{1}
\]
The empty product for \(s=1\) equals one. Independently, the subtree-size process is a two-color Pólya urn, initially with one marked and \(j-1\) unmarked vertices. Its beta-binomial tail is exactly
\[
\mathbb P(S_j\ge s)
=\prod_{r=0}^{s-2}\frac{n-j-r}{n-1-r},\qquad 1\le s\le n-j+1,
\tag{2}
\]
with tail zero above the maximum size. Therefore
\[
\mathbb P(S_j\ge s)\le
\exp\left(-\frac{(j-1)(s-1)}{n-1}\right). \tag{3}
\]

**2. Exclude oversized fringes uniformly over candidate maximizers.** Fix sufficiently small \(\varepsilon>0\). Choose \(0<\delta<\varepsilon\). By the cited maximum-degree location theorem, with probability tending to one every maximizer has label at least \(n^{\mu-\delta}\). Applying (3) and the union bound to every such label, with \(u=\lceil n^{a+\varepsilon}\rceil\), gives
\[
\mathbb P\big(\exists j\ge n^{\mu-\delta}:S_j\ge u\big)
\le n\exp(-\tfrac14 n^{\varepsilon-\delta})\longrightarrow0.
\]
(The bound is trivial when \(u>n-j+1\).)

**3. Exclude undersized fringes at the required extreme degree.** Write \(\alpha=a-\varepsilon>0\). The Chernoff rate
\[
I(b,\alpha)=b\log(b/\alpha)-b+\alpha
\]
satisfies \(I(c,a)=\mu\), while \(I(c,\alpha)>\mu\) because \(\alpha<a<c\). Hence one can choose \(\delta>0\) with \(\delta<\varepsilon\), and \(\eta>0\), such that \(b=c-\eta>\alpha\) and \(I(b,\alpha)>\mu+2\delta\). For \(s\le n^\alpha\), (1) and \(H_{s-1}\le\log s+1\), using \(t=\log(b/\alpha)>0\), yield uniformly in \(j\ge2\)
\[
\mathbb P(S_j\le n^\alpha,\ D_j\ge b\log n)
\le C_{b,\alpha}\,n^{-I(b,\alpha)}.\tag{4}
\]
Consequently, summing (4) over at most \(\lceil n^{\mu+\delta}\rceil\) labels,
\[
\mathbb P\big(\exists j\le n^{\mu+\delta}: S_j\le n^\alpha,\ D_j\ge b\log n\big)
\le C_{b,\alpha} n^{\mu+\delta-I(b,\alpha)}\longrightarrow0.
\]
The root \(j=1\) has fringe size \(n\), so it causes no violation of this lower bound.

**4. Combine high-probability events.** The cited maximum-degree law implies \(\Delta_n\ge(c-\eta)\log n\) with probability tending to one. The cited label-localization theorem implies *all* vertices attaining \(\Delta_n\) have labels between \(n^{\mu-\delta}\) and \(n^{\mu+\delta}\) with probability tending to one. Steps 2 and 3 then show that every such vertex has \(n^{a-\varepsilon}<S_j<n^{a+\varepsilon}\) simultaneously with probability tending to one. This proves the theorem independently of tie-breaking. Larger choices of \(\varepsilon\) follow from the small-\(\varepsilon\) case.

## Verification
The included standalone `verify.py` enumerates **all** \((n-1)!\) recursive trees for each \(2\le n\le8\), computes every nonroot vertex's degree and fringe size, and compares all 210 possible joint-probability positions against the exact factorization
\[
\mathbb P(S_j=s,D_j=d)
=\left[\mathbb P(S_j\ge s)-\mathbb P(S_j\ge s+1)\right]
\frac{\left[{s-1\atop d}\right]}{(s-1)!},
\]
where the bracket is the unsigned Stirling cycle number. Run `python verify.py` using Python's standard library. The finite checker verifies the exact conditional law and urn tail; it does **not** establish the infinite limit. The proof of the limit is given above using cited established asymptotics and explicit uniform exponential estimates.

## Relationship to prior work
Eslava, López, and Ortiz (2022), *Targeted cutting of random recursive trees*, study maximum-degree-first vertex cuts and explicitly identify even the size of the first cut tree as an open question (Section 4). Their results bound the *number* of cuts; they do not assert the size exponent of the first discarded fringe. The 2024 journal version also says the distribution of the first deleted subtree's size was unknown. Lodewijks (first public 2021), *The location of high-degree vertices in weighted recursive graphs with bounded random weights*, Theorem 2.1 and Remark 2.2, gives localization of every maximum-degree vertex, but **does not** by itself control its descendant count. The new step links that external label theorem to size via the exact conditional degree–fringe law and the sharp Cramér-rate calculation \(I(c,a)=\mu\). Neither the claim nor the leading size exponent is an immediate consequence of location alone, because extreme-degree conditioning biases subtree sizes.

## Limitations
This is a first-order logarithmic size limit in probability, not the exact finite-size law, a scaling-limit distribution, a concentration rate, or a description of later cuts. The proof concerns uniform recursive trees with child-count degree, not weighted recursive trees or undirected maximum degree. It uses established probabilistic input theorems rather than proving those theorems anew. Independent mathematical validation and exhaustive historical-priority determination remain outstanding.

## References
1. L. Eslava, S. I. López, M. L. Ortiz, *Targeted cutting of random recursive trees*, arXiv:2212.00183v1, 30 November 2022, https://arxiv.org/html/2212.00183v1 (see Section 4).
2. B. Lodewijks, *The location of high-degree vertices in weighted recursive graphs with bounded random weights*, arXiv:2110.00522, first posted 1 October 2021, https://arxiv.org/abs/2110.00522 ; *Advances in Applied Probability* 56 (2024), Theorem 2.1 and Remark 2.2, https://www.cambridge.org/core/journals/advances-in-applied-probability/article/location-of-highdegree-vertices-in-weighted-recursive-graphs-with-bounded-random-weights/3D398DDDA00010338C15B9A3F8C6A6FE.
3. L. Devroye and J. Lu, *The strong convergence of maximal degrees in uniform random recursive trees and dags*, *Random Structures & Algorithms* 7 (1995), 1–14. The maximum-degree asymptotic also appears in the introduction of reference 1.
