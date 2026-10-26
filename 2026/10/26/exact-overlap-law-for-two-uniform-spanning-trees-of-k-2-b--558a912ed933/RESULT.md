# Exact overlap law for two uniform spanning trees of \(K_{2,b}\)

## Finding
For every integer \(b\ge 2\), draw independently and uniformly two spanning trees \(T,T'\) of the complete bipartite graph \(K_{2,b}\), and put \(X=|E(T)\cap E(T')|\). There exist independent random variables \(Y\sim\operatorname{Bin}(b-2,1/2)\) and \(Z\sim\operatorname{Bernoulli}(1/(2b))\) such that
\[
X\overset{d}{=}2+Y+Z.
\]
In particular, the exact probability generating function is
\[
\mathbb E[z^X]=z^2\left(\frac{1+z}{2}\right)^{b-2}\left(1-\frac1{2b}+\frac{z}{2b}\right).
\]
Its support is exactly \(\{2,3,\ldots,b+1\}\), and
\[
\mathbb EX=\frac{(b+1)^2}{2b},\qquad
\operatorname{Var}(X)=\frac{(b-1)(b^2-b+1)}{4b^2}.
\]
If \(Y\) has the binomial law above, the exact total-variation discrepancy of the translated binomial core is
\[
d_{\rm TV}(\mathcal L(X),\mathcal L(2+Y))
=\frac{1}{2b}\frac{\binom{b-2}{\lfloor(b-2)/2\rfloor}}{2^{b-2}}.
\]

## Assumptions and scope
Both trees are selected independently from all *labeled* spanning trees of \(K_{2,b}\), where the two vertices of one part and the \(b\) vertices of the other part are distinguished. Edges are undirected and simple. The result holds for every integer \(b\ge2\); the random variables on the right-hand side are only a distributional representation, not an identification with a particular chosen edge. For \(b=2\), the binomial \(Y\) has zero trials.

## Proof
Write the vertices in the size-two part as \(u,v\), and the vertices in the other part as \(w_1,\ldots,w_b\). In any spanning tree, each \(w_i\) has degree one or two, since it is adjacent only to \(u,v\). Connectivity forces at least one vertex of degree two: without one, \(u\) and \(v\) lie in different connected components. Two vertices of degree two would form a four-cycle; therefore there is exactly one, called the *bridge spoke* \(R\). Conversely, choosing \(R\in\{1,\ldots,b\}\), including both \(uw_R,vw_R\), and independently choosing precisely one of \(uw_i,vw_i\) for each \(i\ne R\) always produces a spanning tree. This is a bijection from \(b2^{b-1}\) equally weighted choices to all spanning trees, so \(R\) is uniform and the remaining attachment bits are independent unbiased bits.

For two independent trees let their bridge spokes be \(R,R'\). When \(R\ne R'\), the spoke at \(R\) supplies exactly one shared edge, as does that at \(R'\). Each of the \(b-2\) other spokes supplies exactly one shared edge if and only if its two independent fair attachment bits agree, an event of probability \(1/2\); these events are mutually independent. Thus
\[
X\mid(R\ne R')\ \overset d=\ 2+\operatorname{Bin}(b-2,1/2).
\]
When \(R=R'\), the common bridge spoke supplies two shared edges and the remaining \(b-1\) spokes contribute independent fair agreements, giving
\[
X\mid(R=R')\ \overset d=\ 2+\operatorname{Bin}(b-1,1/2).
\]
Since \(\mathbb P(R=R')=1/b\), and \(\operatorname{Bin}(b-1,1/2)\) is the sum of an independent \(\operatorname{Bin}(b-2,1/2)\) and a fair Bernoulli variable, the unconditional mixture is \(2+Y+Z\), with \(\mathbb P(Z=1)=(1/b)(1/2)=1/(2b)\) and \(Y,Z\) independent. This proves the generating function and exact support. The mean and variance follow by adding independent terms.

For the total-variation identity, set \(p=1/(2b)\) and \(q_j=\mathbb P(Y=j)\), with \(q_j=0\) outside \(0\le j\le b-2\). Then for every integer \(j\),
\[
\mathbb P(X=2+j)-(q_j)=p(q_{j-1}-q_j).
\]
Hence \(d_{\rm TV}(\mathcal L(X),\mathcal L(2+Y))=\frac p2\sum_{j\in\mathbb Z}|q_{j-1}-q_j|\). The finite symmetric binomial sequence \((q_j)\) is unimodal, so this sum telescopes to twice its maximal atom. Its maximal atom is \(2^{-(b-2)}\binom{b-2}{\lfloor(b-2)/2\rfloor}\). Substituting yields the claimed formula. The argument also covers the point mass \(b=2\).

## Verification
The standalone `verify.py` enumerates all \(b2^{b-1}\) labeled spanning trees using the bridge-spoke bijection and all ordered pairs for each \(2\le b\le6\). Using exact rational arithmetic, it compares every overlap probability to the claimed distribution and checks the exact mean, variance, and total-variation formula. Its output is supplied as `verification_output.txt`. This finite enumeration is a reproducibility check and **not** the proof for general \(b\), which is given above.

## Relationship to prior work
Bóna and Wagner, *On the intersection of pairs of trees*, arXiv:2501.18570, first circulated 2025-01-30, study common-edge counts of independently uniform spanning trees. The accessible full text (version 1), Section 4 and its conclusion, establishes asymptotic Poisson laws for balanced complete multipartite graphs and mentions an approximate binomial law for \(K_{k,n-k}\) with fixed \(k\). It does not state this exact finite-dimensional factorization for \(k=2\), nor the exact total-variation correction. The previous work's fixed-\(k\) approximation motivates obtaining an exact law in the smallest nontrivial fixed-side case. The related Li–Chen–Yan forest-containing spanning-tree formula gives general forest extension counts, not this closed overlap law without additional enumeration and simplification.

## Limitations
The exact law is specific to a two-vertex part and is not asserted for \(K_{k,b}\) when \(k\ge3\). The accessible full text examined was the 2025 version; the later 2026 revision's abstract was examined, but its full text could not be retrieved. The novelty comparison to that revision and to older specialized literature therefore retains a historical-priority risk.

## References
Bóna, M. and Wagner, S. (with F. Burghart added in later versions), *On the intersection of pairs of trees*, arXiv:2501.18570, first public 2025-01-30. https://arxiv.org/abs/2501.18570

Li, D., Chen, W., and Yan, W., *Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, Journal of Graph Theory **104** (2023), 160–170 (as cited in arXiv:2501.18570, Section 4).
