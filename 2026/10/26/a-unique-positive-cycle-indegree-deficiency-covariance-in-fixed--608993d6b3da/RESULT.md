# A unique positive cycle–indegree-deficiency covariance in fixed-outdegree digraphs

## Finding
For every integer \(n\ge3\), construct a loop-free random digraph by allowing each labeled vertex to choose, independently of all other vertices, exactly \(k\) distinct out-neighbors uniformly from the other \(n-1\) vertices. Let \(Z\) be the number of vertices having indegree zero. Let \(C_\ell\) be the number of directed simple cycles of length \(\ell\), counted up to cyclic rotation, for each \(2\le\ell\le n\). Write
\[
p=\frac{k}{n-1},\quad q=1-p,\quad A=\frac{n-1}{n-2},\quad (n)_\ell=\frac{n!}{(n-\ell)!}.
\]
For \(1\le k\le n-2\), the exact finite-sample covariance is
\[
\boxed{\operatorname{Cov}(Z,C_\ell)=\frac{(n)_\ell}{\ell}p^\ell q^{n-1}\left[(n-\ell)A^\ell-n\right].}
\]
Its sign is strictly **positive if \(\ell=2\)** and strictly **negative for every \(3\le\ell\le n\)**. For \(k=n-1\), all these covariances are zero, because \(Z=0\) deterministically.

In the comparison loop-free directed Erdős–Rényi model, with every ordered arc independently present with probability \(p\), the covariance is
\[
\boxed{\operatorname{Cov}_{\mathrm{ind}}(Z,C_\ell)=-(n)_\ell p^\ell(1-p)^{n-1}<0\qquad(0<p<1).}
\]
Consequently, the reciprocal-pair statistic \(C_2\) has **opposite covariance signs** with \(Z\) under fixed and independent outdegree sampling, even when the expected outdegrees agree. The positive covariance in the fixed-outdegree model comes from a small but exact cancellation between cycle vertices that cannot have indegree zero and outside vertices that become more likely to have indegree zero.

For each *fixed* positive integer \(k\) and cycle length \(\ell\) as \(n\to\infty\), the finite formula further yields
\[
\begin{aligned}
\lim_{n\to\infty}n\operatorname{Cov}(Z,C_2)&=\frac{k^2e^{-k}}2,\\
\lim_{n\to\infty}n^2\operatorname{Cov}(Z,C_3)&=-\frac{2k^3e^{-k}}3,\\
\lim_{n\to\infty}n\operatorname{Cov}(Z,C_\ell)&=-\frac{(\ell-3)k^\ell e^{-k}}2\quad\text{for each fixed }\ell\ge4.
\end{aligned}
\]
The extra order of cancellation for directed triangles is a second distinction within the cycle spectrum.

## Assumptions and scope
The digraph has distinct labeled vertices; self-loops and parallel arcs are forbidden. Different vertices choose their outgoing neighbor sets independently, but outgoing arcs sharing a source are sampled without replacement and hence dependent. A directed \(2\)-cycle consists of the two opposite arcs between a vertex pair. A simple directed \(\ell\)-cycle requires \(\ell\) distinct vertices and contains one directed arc from each; cyclic rotations identify the same cycle, but reversal is a different cycle whenever \(\ell\ge3\). The theorem concerns ordinary integer \(n\ge3\), \(1\le k\le n-1\), \(2\le\ell\le n\). No asymptotic assumption is needed for the finite identity. The displayed limits require \(k\) and \(\ell\) fixed independently of \(n\).

## Proof
Fix \(1\le k\le n-2\), so \(p,q>0\). For each vertex \(v\), let \(I_v\) be the indicator of indegree zero. Every other source avoids \(v\) with probability \(q\), independently across sources; therefore
\[
\mathbb{P}(I_v=1)=q^{n-1},\qquad \mathbb E Z=nq^{n-1}.
\]
Fix a directed simple cycle \(\gamma\) on a specified \(\ell\)-tuple of distinct vertices, and let \(J_\gamma\) indicate its presence. Its required outgoing arcs use distinct sources, hence
\[
\mathbb P(J_\gamma=1)=p^\ell.
\]
If \(v\) lies on the cycle, \(I_vJ_\gamma=0\), because \(v\) receives an arc from its predecessor. If \(v\) lies outside the cycle, every one of its \(n-1-\ell\) noncycle potential incoming sources still avoids \(v\) with probability \(q\). At each of the \(\ell\) cycle sources, conditioning on selection of the prescribed successor leaves a uniform \((k-1)\)-subset of the remaining \(n-2\) possible targets. The probability of avoiding \(v\) is exactly
\[
\frac{\binom{n-3}{k-1}}{\binom{n-2}{k-1}}=\frac{n-k-1}{n-2}=qA.
\]
The independent outgoing choices across sources therefore give
\[
\mathbb P(I_v=1\mid J_\gamma=1)=q^{n-1}A^\ell
\qquad (v\notin\gamma).
\]
Consequently,
\[
\mathbb E[Z\mid J_\gamma=1]=(n-\ell)q^{n-1}A^\ell,
\]
and the elementary indicator identity \(\operatorname{Cov}(Z,J_\gamma)=\mathbb P(J_\gamma=1)(\mathbb E[Z\mid J_\gamma=1]-\mathbb EZ)\) yields
\[
\operatorname{Cov}(Z,J_\gamma)=p^\ell q^{n-1}\big[(n-\ell)A^\ell-n\big].
\]
There are exactly \((n)_\ell/\ell\) labeled directed simple cycles, since choosing an ordered \(\ell\)-tuple counts each cyclic rotation \(\ell\) times. Summation over these indicators proves the covariance identity without any assumption of independence among different cycles.

To determine its strict sign, put \(f_\ell=(n-\ell)A^\ell\). Direct calculation gives
\[
f_2=n+\frac1{n-2}>n,
\qquad
f_3=n-\frac{2n-3}{(n-2)^3}<n.
\]
For every integer \(2\le\ell<n\),
\[
\frac{f_{\ell+1}}{f_\ell}=\frac{(n-1)(n-\ell-1)}{(n-2)(n-\ell)}<1,
\]
where the strict inequality follows on expanding both sides and using \(\ell>1\). Thus \(f_\ell\) decreases strictly from \(\ell=2\) to \(\ell=n\). In particular, the bracket is positive only for \(\ell=2\), and negative for all longer directed simple cycles. The case \(k=n-1\) is deterministic for \(Z\) and gives zero covariance separately.

For the independent-arc comparison model, every cycle event has probability \(p^\ell\). A vertex on the cycle cannot have indegree zero, whereas for any vertex outside the cycle the incoming arcs are independent of the cycle arcs and indegree zero has probability \((1-p)^{n-1}\). Hence \(\mathbb E[Z\mid J_\gamma=1]=(n-\ell)(1-p)^{n-1}\), and summation over cycles gives the stated negative formula.

Finally, with \(k\) and \(\ell\) fixed, \((n)_\ell p^\ell\to k^\ell\) and \(q^{n-1}\to e^{-k}\). For the sign bracket \(b_\ell=f_\ell-n\), the exact identities are
\[
b_2=\frac1{n-2},\qquad b_3=-\frac{2n-3}{(n-2)^3}.
\]
For fixed \(\ell\ge4\), a finite binomial expansion of \(A^\ell=(1+1/(n-2))^\ell\) gives
\[
b_\ell=\frac{\ell(3-\ell)}{2n}+O(n^{-2}).
\]
Substituting these expansions into the finite identity gives all three limits.

## Verification
The supplied standalone `verify.py` uses only Python's standard library. It independently enumerates all outgoing-neighbor-set choices at \(n=3,4,5\) and at \((n,k)=(6,1)\), comparing exact rational averages and mixed moments with the formula for every available cycle length. It also exhaustively checks the independent-arc identity at \(n=4\) and \(p=1/3\) over all \(2^{12}\) loop-free directed arc sets. To replay, run `python verify.py`. The observed terminal marker is `VERIFY_OK`. These finite tests support the proof but do not establish its unrestricted quantifiers; those follow from the conditional probability computation above.

## Relationship to prior work
Sood and Yağan study finite connectivity probabilities in homogeneous random \(k\)-out graphs, using the same independent-uniform-outgoing-subset construction before discarding orientations [1]. Their work addresses global connectivity, not a mixed moment between directed cycle counts and zero-indegree counts. Their inhomogeneous \(k\)-out work [2] and the related study of Eletreby and Yağan [3] provide further context for the row-independent selection construction and isolated undirected components. The latter works use undirected connectivity notions; an indegree-zero vertex in the directed sampling is not generally an isolated vertex of the symmetrized network. Itzkovitz and collaborators [4] analyze approximate expected subgraph counts in random networks with prescribed degree information; their approximate expectations do not imply the exact cross-moment or its all-length sign classification. Earlier methods for random mappings, configurations, or graph motifs may allow a separate derivation, so priority beyond the inspected sources is not established here.

## Limitations
The theorem does not cover independent choices with replacement, random variable row degrees, prescribed incoming degrees, self-loops, or cycles with repeated vertices. It supplies second-order cross moments, not joint distributions or a central limit theorem. For fixed \(k\) and fixed cycle length the covariance tends to zero, even though its exact sign and leading order are structurally different. The novelty assessment is limited to the cited literature and searches; an unlocated broader identity might subsume this result. No independent audit has been performed.

## References
[1] M. Sood and O. Yağan, *Tight Bounds for the Probability of Connectivity in Random K-out Graphs*, arXiv:2006.10638, initially posted 2020-06-18, https://arxiv.org/abs/2006.10638.

[2] M. Sood and O. Yağan, *On the Strength of Connectivity of Inhomogeneous Random K-out Graphs*, arXiv:1911.05147, initially posted 2019-11-12, https://arxiv.org/abs/1911.05147.

[3] R. Eletreby and O. Yağan, *Connectivity of Inhomogeneous Random K-out Graphs*, arXiv:1810.09921, initially posted 2018-10-23, https://arxiv.org/abs/1810.09921.

[4] S. Itzkovitz, R. Milo, N. Kashtan, G. Ziv and U. Alon, *Subgraphs in random networks*, arXiv:cond-mat/0302375, initially posted 2003-02-19, https://arxiv.org/abs/cond-mat/0302375.
