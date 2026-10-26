# A sharp degree-four subdivision reversal for source–sink covariance in random graph orientations

## Finding
Let \(G=(V,E)\) be any finite simple graph without isolated vertices, and orient all edges independently and uniformly. Write \(X_G\) for its number of sources (vertices with indegree zero) and \(Y_G\) for its number of sinks (vertices with outdegree zero), including orientations containing directed cycles. If \(d_v\) denotes the undirected degree and \(a_v=2^{-d_v}\), then
\[
\operatorname{Cov}(X_G,Y_G)=2\sum_{\{u,v\}\in E}a_ua_v-\sum_{v\in V}a_v^2. \tag{1}
\]
Subdivide one edge \(uv\) once by replacing it with \(u-w-v\), where \(w\) is a new degree-two vertex, and let \(G'\) be the resulting graph. Then
\[
\operatorname{Cov}(X_{G'},Y_{G'})-\operatorname{Cov}(X_G,Y_G)
=\frac{2^{-d_u}+2^{-d_v}}2-2^{1-d_u-d_v}-\frac1{16}. \tag{2}
\]
The change is **negative exactly** when \(d_u=d_v=1\) or when both \(d_u,d_v\ge4\), and is **strictly positive in every other case**. In particular, for an edge in a connected graph with at least three vertices, subdivision increases source–sink covariance precisely when at least one endpoint has degree at most three.

For every finite simple \(r\)-regular graph on \(n\) vertices, where \(r\ge2\), let \(\operatorname{Sub}(G)\) replace every edge by a two-edge path. Then
\[
\operatorname{Cov}(X_G,Y_G)=\frac{n(r-1)}{4^r}>0, \tag{3}
\]
whereas
\[
\operatorname{Cov}(X_{\operatorname{Sub}(G)},Y_{\operatorname{Sub}(G)})
=n\left(\frac r{2^{r+1}}-\frac1{4^r}-\frac r{32}\right). \tag{4}
\]
The latter is positive for \(r=2,3\) and **negative for every \(r\ge4\)**, independently of the connectivity or other structure of the regular graph. The boundary is sharp: at \(r=3\) the value is \(5n/64\), and at \(r=4\) it is \(-n/256\).

## Assumptions and scope
Graphs are finite, undirected, simple and without isolated vertices; they may be disconnected. Every edge is oriented with an independent fair coin, so all \(2^{|E|}\) orientations are equally likely. A source has all incident edges oriented away from it, and a sink has all incident edges oriented towards it. The covariance formula excludes degree-zero vertices, since such vertices are simultaneously sources and sinks but contribute only deterministic constants. They can be deleted before using the formula without changing covariance. Subdivision refers to replacing an edge by two edges through one new degree-two vertex, not adding a parallel edge. In (3)–(4), simple \(r\)-regular graphs exist for all admissible \(n,r\).

## Proof
For each vertex \(v\), let \(S_v\) and \(T_v\) indicate that it is a source or sink, respectively. As \(d_v>0\),
\(\Pr(S_v=1)=\Pr(T_v=1)=a_v\), and \(S_vT_v=0\), hence \(\operatorname{Cov}(S_v,T_v)=-a_v^2\). For distinct nonadjacent vertices the incident edge sets are disjoint and \(S_u,T_v\) are independent. If \(uv\in E\), the shared edge must point from \(u\) to \(v\) for both events. Thus
\(\Pr(S_u=T_v=1)=2a_ua_v\), and \(\operatorname{Cov}(S_u,T_v)=a_ua_v\). Summing all ordered pairs of indicators gives (1), with two ordered terms per undirected edge.

When \(uv\) is subdivided, endpoint degrees and all other old degrees are unchanged. In (1), the removed edge contributes \(2a_ua_v\), the two replacement edges contribute \(2(a_u/4+a_v/4)=(a_u+a_v)/2\), and the new vertex contributes the negative diagonal term \(-1/16\). This proves (2).

For the complete sign classification, use symmetry to assume \(d_u\le d_v\), and set \(b=2^{-d_v}\). If \(d_u=1\), expression (2) is \(3/16-b/2\): it equals \(-1/16\) when \(d_v=1\), and is at least \(1/16\) when \(d_v\ge2\). If \(d_u=2\), it equals \(1/16\) for every \(d_v\ge2\). If \(d_u=3\), it equals \(b/4>0\). Finally, if \(d_u\ge4\), both endpoint weights lie in \((0,1/16]\). Therefore \((a_u+a_v)/2\le1/16\) while \(2a_ua_v>0\), proving strict negativity. This exhausts the integer degree possibilities.

For \(r\)-regular \(G\), there are \(nr/2\) edges, and every endpoint weight is \(2^{-r}\). Formula (1) gives (3). In \(\operatorname{Sub}(G)\), each old vertex has weight \(2^{-r}\), each new degree-two vertex has weight \(1/4\), and the number of new vertices is \(nr/2\). Summing the \(nr\) new edge contributions and all diagonal terms in (1) gives (4). At \(r=2\), expression (4) is \(n/8\), and at \(r=3\) it is \(5n/64\). At \(r=4\) it is \(-n/256\). For every integer \(r\ge5\), \(r/2^{r+1}\le r/64<r/32\), so expression (4) is strictly negative. This completes the proof.

## Verification
The accompanying standard-library Python program `verify.py` independently enumerates all orientations of every isolate-free labeled simple graph on two through four vertices, tests single-edge subdivisions of those graphs, and checks additional paths, stars, cycles and complete graphs. It also exhausts all \(2^{20}=1,048,576\) orientations of the one-subdivision of \(K_5\), independently recovering the covariance \(-5/256\). The verifier passed 574 assertion groups in the recorded run. These finite checks corroborate the analytic proof; they do not establish the theorem for arbitrary graphs.

## Relationship to prior work
Linusson (2009) studies directed *path-reachability* correlation inequalities under fair independent orientations; these are not the simultaneous counts of vertices with indegree zero and outdegree zero. Hwang, Jung, Lee, Oh and Yu (2019) study a sink polynomial over **acyclic** orientations, a different probability space. Yu and Zhu (2025) prove a general polynomial and degree-constraint enumeration identity for all orientations: their framework can encode the source–sink joint distribution, so it is a material priority risk, but their inspected theorems do not give (1)–(4) or the sharp degree-four subdivision sign boundary. Conte, Grossi, Marino and Rizzi (2018) develop constrained source-orientation enumeration algorithms; they do not state the covariance threshold. Counting source-sink-free orientations on chordal graphs (Bezáková and Sun, 2022) is also related; its complete primary text was not accessible during the comparison. The specific covariance-sign reversal should receive independent priority review.

## Limitations
The result is for independent unbiased orientations, not random orientations restricted to be acyclic, and not a random underlying graph. The sign classification concerns **covariance**, not independence or first-order stochastic ordering. The degree-four threshold describes edge subdivision and all-edge subdivision of regular graphs, and does not assert a universal sign classification of covariance for every graph. A general orientation-generating polynomial encodes the relevant moments in principle; no claim is made that their finite computation was previously impossible.

## References
1. S. Linusson, *A note on correlations in randomly oriented graphs*, arXiv:0905.2881, first arXiv version dated 2009-05-18, https://arxiv.org/abs/0905.2881.
2. J. Yu and J.-X. Zhu, *Counting degree-constrained orientations*, arXiv:2504.12693, 2025-04-17, https://arxiv.org/abs/2504.12693.
3. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920, 2019-10-24, https://arxiv.org/abs/1910.10920.
4. A. Conte, R. Grossi, A. Marino and R. Rizzi, *Efficient enumeration of graph orientations with sources*, Discrete Applied Mathematics 246 (2018), 22–37, https://doi.org/10.1016/j.dam.2017.08.002.
5. I. Bezáková and W. Sun, *Counting and Sampling Orientations on Chordal Graphs*, WALCOM 2022, https://doi.org/10.1007/978-3-030-96731-4_29.
