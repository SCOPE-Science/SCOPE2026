# A one-switch law for degree-class–motif covariance, with induced-path reentrance

## Finding

Let \(G\sim G(n,p)\) be the independent-edge random graph, with integer \(n\ge2\) and \(0<p<1\). Let \(N_k\) denote the number of vertices of degree exactly \(k\), for \(0\le k\le n-1\). Fix any simple graph \(H\) with \(h\le n\) vertices and at least one edge. Let \(X_H\) count injective vertex maps of \(H\) into \(G\) preserving every edge of \(H\), without imposing nonedge conditions. Write \(d_v\) for the degree of a vertex \(v\) in \(H\), \(e=|E(H)|\), \(N=n-1\), and \(b_k=\binom Nk p^k(1-p)^{N-k}\). For the falling factorial \((x)_r=x(x-1)\cdots(x-r+1)\), with \((x)_0=1\), the exact covariance is

\[
\operatorname{Cov}(N_k,X_H)
=(n)_h p^e b_k\left[\sum_{v\in V(H)}\frac{(k)_{d_v}}{(N)_{d_v}p^{d_v}}-h\right].
\]

Put \(\delta_+(H)=\min\{d_v:d_v>0\}\). For \(0\le k<N\), the covariance is **strictly negative at every** \(0<p<1\) when \(k<\delta_+(H)\). For \(\delta_+(H)\le k<N\), it is strictly positive below one threshold \(p_*(n,k,H)\in(0,1)\), zero at that threshold and strictly negative above it. The threshold is the unique solution of

\[
\sum_{v:d_v>0}\frac{(k)_{d_v}}{(N)_{d_v}p^{d_v}}=|\{v:d_v>0\}|.
\]

For \(k=N\), the covariance is strictly positive throughout \(0<p<1\). Thus all non-induced motif counts obey a universal **at-most-one-switch law**, with no assumption that \(H\) is connected or regular. In particular, when every nonisolated vertex of \(H\) has the same degree \(d\), the unique threshold for \(d\le k<N\) is

\[
p_*(n,k,H)=\left(\frac{(k)_d}{(n-1)_d}\right)^{1/d}.
\]

The non-induced qualification is essential. Let \(P_3\) be the three-vertex path, let \(X^{\mathrm{ind}}_{P_3}\) count injective maps whose three images induce **exactly** the two path edges, and take \(k=1\). For every \(n\ge3\),

\[
\operatorname{Cov}(N_1,X^{\mathrm{ind}}_{P_3})
=(n)_3p^2(1-p)^{n-2}\bigl[2-3(n-1)p(1-p)\bigr].
\]

For \(n=3\), this covariance is positive at every \(0<p<1\). For every \(n\ge4\), it has **two** distinct zeros

\[
p_\pm(n)=\frac{1\pm\sqrt{1-8/[3(n-1)]}}2,
\]

and the signs, from smaller to larger \(p\), are strictly positive, strictly negative, strictly positive. The smallest possible example occurs at \(n=4\), with zeros \(1/3\) and \(2/3\). For the same path counted as a non-induced motif,

\[
\operatorname{Cov}(N_1,X_{P_3})=(n)_3p^2(1-p)^{n-2}\,[2-3(n-1)p],
\]

so there is instead just one zero, \(2/[3(n-1)]\). These formulas use the injective-map convention; dividing either path count by the order-two automorphism factor scales covariance but does not change any sign.

## Assumptions and scope

Every edge among \(n\) labeled vertices is present independently with the same parameter \(p\in(0,1)\). A non-induced copy requires only the edges of the pattern; extra edges are allowed. An induced copy additionally requires its internal nonedges to be absent. The pattern \(H\) may have isolated vertices but must contain an edge. Degrees \(k\) range from \(0\) to \(n-1\). All displayed formulas concern exact finite-sample covariances, not limits or asymptotic substitutions. The two-switch example uses \(P_3\), the undirected path with exactly two edges.

## Proof

**Step 1: condition on a fixed non-induced embedding.** Let \(\phi:V(H)\hookrightarrow[n]\) be injective and \(A_\phi\) the event that its \(e\) prescribed edges exist. Independent edges give \(\Pr(A_\phi)=p^e\). At an image vertex \(\phi(v)\), precisely \(d_v\) incident edges have been fixed present, while the remaining \(N-d_v\) incident edges remain independently Bernoulli with parameter \(p\). Consequently,

\[
\Pr(\deg_G(\phi(v))=k\mid A_\phi)
=\binom{N-d_v}{k-d_v}p^{k-d_v}(1-p)^{N-k}.
\]

The binomial coefficient is zero if its lower index is inadmissible. Every vertex outside the image has its degree distribution unchanged, since the prescribed edges have both endpoints inside the image. Since \(\mathbb E N_k=nb_k\), summing the image contributions gives

\[
\operatorname{Cov}(N_k,\mathbf1_{A_\phi})
=p^e\sum_{v\in V(H)}
\left[\binom{N-d_v}{k-d_v}p^{k-d_v}(1-p)^{N-k}-b_k\right].
\]

There are exactly \((n)_h\) injective maps. By covariance linearity, multiplying and using

\[
\frac{\binom{N-d}{k-d}p^{k-d}(1-p)^{N-k}}{b_k}
=\frac{(k)_d}{(N)_dp^d}
\]

proves the first formula. This computation does not assume distinct embedding events are independent.

**Step 2: sharp sign classification.** The positive factor \((n)_h p^e b_k\) never affects the sign. Degrees \(d_v=0\) contribute \(1\) inside the bracket and therefore cancel. Set \(s=|\{v:d_v>0\}|>0\). If \(k<\delta_+(H)\), every \((k)_{d_v}\) with positive \(d_v\) vanishes, and the bracket equals \(-s\). If \(\delta_+(H)\le k<N\), the continuous function

\[
F_k(p)=\sum_{v:d_v>0}\frac{(k)_{d_v}}{(N)_{d_v}}p^{-d_v}-s
\]

is strictly decreasing on \((0,1)\), tends to \(+\infty\) as \(p\downarrow0\), and satisfies \(F_k(1)<0\) because \((k)_d<(N)_d\) for every positive \(d\le N\) when \(k<N\). Hence it has exactly one zero and the claimed strict signs. When \(k=N\), each positive-degree summand is \(p^{-d_v}>1\), making \(F_N(p)>0\). For a common positive degree \(d\) the root equation reduces to \((k)_d/((N)_dp^d)=1\).

**Step 3: induced three-vertex path.** For an injective image of \(P_3\), the event that the induced image has exactly the two path edges has probability \(p^2(1-p)\). Conditional on this event, the two endpoint degrees are \(1+\operatorname{Bin}(n-3,p)\), while the central vertex has degree at least two. Therefore their combined expected contribution to \(N_1\) is \(2(1-p)^{n-3}\); without conditioning, the three vertices contribute \(3(n-1)p(1-p)^{n-2}\). All outside degrees remain unaltered. Multiplication by the event probability and the number \((n)_3\) of injective maps gives exactly

\[
(n)_3 p^2(1-p)^{n-2}[2-3(n-1)p(1-p)].
\]

The quadratic \(p(1-p)\) has maximum \(1/4\) at \(p=1/2\). For \(n=3\), \(3(n-1)/4=3/2<2\), so the bracket is strictly positive. For every \(n\ge4\), \(3(n-1)/4>2\), giving two distinct interior roots and strict sign pattern \(+,-,+\). Their quadratic formula is as displayed. Repeating the conditional calculation while allowing the chord joining the path endpoints yields \(2(1-p)^{n-2}\) in place of \(2(1-p)^{n-3}\), proving the final non-induced identity.

## Verification

The standalone `verify.py` enumerates independent-edge graphs by edge-mask, counts degree-class vertices and injective induced/non-induced pattern embeddings directly, and evaluates every expectation using exact rational probabilities. It compares those raw covariance values against a separately implemented conditioning formula for pattern edge sets corresponding to an edge, a three-vertex path, a triangle, an edge plus an isolated vertex, and a three-vertex empty graph, for vertex counts \(n=3,4,5\), all admissible degrees and five rational values of \(p\). It also checks the exact two-switch and one-switch boundaries for the three-vertex path on four vertices. The executable reports 608 passing exact checks. Enumeration confirms finite cases only; the universal theorem is proved in the preceding paragraphs.

## Relationship to prior work

The underlying independent-edge random graph and the binomial degree marginal are classical. Greenhill, Isaev and McKay study expected subgraph and induced-subgraph counts in a different model with a prescribed degree sequence. Bhattacharya, Chatterjee and Janson study fluctuations of arbitrary subgraph counts in graphon-based random graphs, focusing on asymptotic distributions. Alarfaj, Taylor and Bogachev study pairwise dependence of vertex degrees in independent-edge graphs. These findings do not, in their inspected statements, supply the finite-sample joint covariance between a whole degree *class* and every non-induced pattern, its unique sign-transition classification, or the induced-path two-transition contrast. The formulas here are directly derivable by independent-edge conditioning; they should not be interpreted as claiming this conditioning technique itself is new.

## Limitations

The one-switch law does **not** extend to all induced motifs, as the explicit counterexample demonstrates. The finding does not cover inhomogeneous edge probabilities, random graphs with fixed degree sequences, random regular graphs, dependence measures other than covariance, or conditional concentration inequalities. Exhaustive computation checks small finite instances but cannot establish universal statements. An equivalent or broader earlier mixed-moment identity may exist in classical random-graph literature; historical priority has not been independently certified.

## References

1. C. Greenhill, M. Isaev and B. D. McKay, *Subgraph counts for dense random graphs with specified degrees*, arXiv:1801.09813 (first public version, 30 January 2018). https://arxiv.org/abs/1801.09813
2. B. B. Bhattacharya, A. Chatterjee and S. Janson, *Fluctuations of Subgraph Counts in Graphon Based Random Graphs*, arXiv:2104.07259 (15 April 2021). https://arxiv.org/abs/2104.07259
3. B. Alarfaj, C. Taylor and L. Bogachev, *The joint node degree distribution in the Erdős–Rényi network*, arXiv:2303.05138 (9 March 2023). https://arxiv.org/abs/2303.05138
