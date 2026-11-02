# Connected-motif Palm cancellation and sharp tree-shape covariance phases

## Finding

Let \(G\sim G(n,p)\), with independent edges, \(0<p<1\), and \(n\ge\max\{h,f\}\). Fix connected simple graphs \(H\) and \(F\), with \(h=|V(H)|\ge2\), \(f=|V(F)|\ge2\), and \(e=|E(F)|\ge1\). Let \(C_H\) be the number of connected components isomorphic to \(H\). Count copies of \(F\) either non-induced or induced, declaring the convention in advance; denote the corresponding random count by \(X_F\), and denote by \(t_F(H)\) the number of such copies within \(H\). Put
\[
 b_F=\frac{f!}{|\operatorname{Aut}(F)|},\quad
 Q_F(n,h)=b_F\left[\binom nf-\binom{n-h}f\right],\quad
 s=\begin{cases}0&\text{non-induced},\\ \binom f2-e&\text{induced}.\end{cases}
\]
Here \(\binom af=0\) when \(a<f\). Then the exact identity is
\[
\boxed{\operatorname{Cov}(C_H,X_F)=\mathbb E[C_H]\left[t_F(H)-Q_F(n,h)p^e(1-p)^s\right].}\tag{1}
\]
It includes the exact component expectation
\[
\mathbb E[C_H]=\binom nh\frac{h!}{|\operatorname{Aut}(H)|}
 p^{|E(H)|}(1-p)^{\binom h2-|E(H)|+h(n-h)}>0.\tag{2}
\]
Thus \(Q_F(n,h)>0\) and the sign depends only on the local motif count \(t_F(H)\), the sizes \(n,h,f\), and the motif edge/nonedge count, not on further graph structure.

The complete sign classification is as follows. If \(t_F(H)=0\), the covariance is strictly negative for all \(0<p<1\). If \(t_F(H)>0\), put \(r=t_F(H)/Q_F(n,h)\), so \(0<r\le1\). In the non-induced convention (and for an induced clique), the covariance has one strict positive-to-negative switch at \(p=r^{1/e}\) if \(r<1\), and is strictly positive throughout \(0<p<1\) if \(r=1\). For an induced nonclique, \(s>0\), put \(p_0=e/(e+s)\) and \(M=(e/(e+s))^e(s/(e+s))^s\). If \(0<r<M\), there are exactly two roots \(p_-<p_0<p_+\), with signs positive, negative, positive on the three successive intervals. If \(r=M\), the covariance is nonnegative and vanishes only at \(p_0\). If \(r>M\), it is strictly positive everywhere.

The result has a sharp shape-dependent specialization. For any tree \(H\) on \(h\ge4\) vertices, let \(F\) be the three-vertex path, and define
\[
 W(H)=\sum_{v\in V(H)}\binom{d_H(v)}2,\qquad
 Q=3\left[\binom n3-\binom{n-h}3\right].
\]
For the **non-induced** path count the unique covariance-zero threshold is \(p_c(H)=\sqrt{W(H)/Q}\), and among all \(h\)-vertex trees the sharp envelope is
\[
\boxed{\sqrt{\frac{h-2}{Q}}\ \le\ p_c(H)\ \le\ \sqrt{\frac{\binom{h-1}2}{Q}}.}\tag{3}
\]
The first equality holds only for the path and the second only for the star (up to isomorphism). As \(n\to\infty\) for fixed \(h\), \(np_c(H)\to\sqrt{2W(H)/(3h)}\). For the **induced** three-vertex path, the covariance changes sign twice for every \(n\ge h+1\): the negative-density interval is widest for the path component and narrowest for the star component; the roots are the two solutions of \(p^2(1-p)=W(H)/Q\).

For example, at \(n=5\) and \(p=7/25\), the covariance of the non-induced path motif count with the number of four-vertex path components is negative, whereas its covariance with the number of four-vertex star components is positive. At \(n=5\), the induced-path negative intervals are approximately \((0.31108,0.92149)\) for path components and \((0.41261,0.86695)\) for star components.

## Assumptions and scope

All graphs are finite, undirected, loopless, simple. An \(H\)-component means a maximal connected component with vertex-induced graph isomorphic to \(H\); it is counted once, not once per automorphism. An \(F\)-copy is an unlabeled edge-preserving embedding modulo automorphisms, counted once for each distinct edge-set image; in the induced version its vertex set must induce exactly that image. Since \(F\) is connected and has at least two vertices, it has no isolated vertices, so this convention is unambiguous. Both \(H\) and \(F\) are fixed before choosing \(n,p\). No independence of component count and motif count is asserted at a covariance-zero value.

## Proof

For each \(h\)-subset \(A\subseteq[n]\), write \(J_A\) for the event that \(A\) is the vertex set of a connected component isomorphic to \(H\). Then \(C_H=\sum_{|A|=h}\mathbf1_{J_A}\). On \(J_A\), every cross-edge between \(A\) and its complement is absent, the induced graph on \(A\) is isomorphic to \(H\), and every edge within the complement retains its independent Bernoulli \(p\) law.

Partition all potential copies of connected \(F\) into those wholly inside \(A\), wholly outside \(A\), and using vertices of both. On \(J_A\), the first class contributes exactly \(t_F(H)\) (isomorphism invariance). The second class remains independent, with conditional mean \(b_F\binom{n-h}f p^e(1-p)^s\). Every potential copy in the third class contains at least one crossing edge because \(F\) is connected, so it contributes zero under \(J_A\), in either motif convention. Hence
\[
 \mathbb E[X_F\mid J_A]=t_F(H)+b_F\binom{n-h}f p^e(1-p)^s.
\]
Unconditionally, \(\mathbb E[X_F]=b_F\binom nf p^e(1-p)^s\). Subtracting these expectations, multiplying by \(\Pr(J_A)\), and summing over \(A\) proves (1). On each \(A\), there are \(h!/|\operatorname{Aut}(H)|\) possible induced labeled graphs isomorphic to \(H\); each has probability \(p^{|E(H)|}(1-p)^{\binom h2-|E(H)|+h(n-h)}\) of forming a component. Summing proves (2).

Since any \(F\)-copy inside \(H\) is one of the \(Q_F(n,h)\) potential copies intersecting \(A\), \(0\le t_F(H)\le Q_F(n,h)\), and \(Q_F(n,h)>0\). For \(s=0\), \(p\mapsto p^e\) increases strictly on \((0,1)\), yielding the one-switch classification. For \(s>0\), logarithmic differentiation gives
\[
 \frac{d}{dp}\log(p^e(1-p)^s)=\frac ep-\frac{s}{1-p},
\]
so the density factor increases strictly up to \(p_0=e/(e+s)\), decreases strictly afterwards, and has the stated maximum \(M\). Its comparison to \(r\) proves all zero, one-tangency and two-switch cases, including boundary cases.

For a tree \(H\), each unordered pair of incident edges determines a unique (induced and non-induced) three-vertex path; hence \(t_F(H)=W(H)\). On each three-element vertex set there are three possible non-induced path embeddings, proving the stated formula for \(Q\). Write \(x_v=d_H(v)-1\ge0\). Then \(\sum_v x_v=h-2\), and \(W(H)=\sum_v\binom{x_v+1}2\). Moving one unit of positive excess from a smaller to a larger coordinate strictly increases this sum. The minimum over tree degree sequences occurs at \(h-2\) coordinates equal to one and two equal to zero, corresponding uniquely to a path; the maximum occurs at a single coordinate \(h-2\), corresponding uniquely to a star. This proves (3) and both equality classifications. Moreover, \(Q\sim(3h/2)n^2\), giving the sparse-scale limit.

For the induced path convention, \(s=1\) and \(e=2\), so the density factor is \(p^2(1-p)\) with maximum \(4/27\). For \(n\ge h+1\), the largest possible ratio is attained by the star and is bounded by
\[
 \frac{\binom{h-1}2}{Q}\le\frac{h-2}{h(h+1)}\le\frac1{10}<\frac4{27}.
\]
Thus every such tree yields exactly two roots. On the increasing branch of \(p^2(1-p)\), the root grows strictly with \(W(H)\); on the decreasing branch it shrinks strictly. The path and star degree-excess extremes therefore give the widest and narrowest negative intervals, respectively. This finishes the proof.

## Verification

Run `python3 verify_component_motif.py` using only the standard library. It independently exhausts labeled graph states at sizes four and five, computes connected-component isomorphism classes and induced/non-induced motif counts directly, and compares exact rational covariances with (1). It checks 94 complete probability identities with no sampling, including cases where the covariance changes sign between the four-vertex path and star. The complete finite verification is evidence of implementation and boundary checking, not a substitute for the all-size argument above. The strict tree inequalities follow symbolically from the convexity of degree excess and the derivative of \(p^2(1-p)\), not numerical root search.

## Relationship to prior work

Ellis and Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, develop exact and asymptotic overlap formulas for \(\operatorname{Var}(X_H)\), rather than a connected-component count paired with a potentially different connected motif count. Their overlap method and normalization identity are an important conceptual precursor; their primary preprint was inspected through its variance lemma, overlay theorems, tree case, and concluding section.

Ginoza and Mugler, *Network motifs come in sets* (arXiv:0907.4680, first publicly posted 2009-07-27), study correlations among motifs in degree-preserving network-randomization procedures; the sections on methods, motif correlations and discussion use different null models and do not provide (1). Frank's 1979 *Moment Properties of Subgraph Counts in Stochastic Graphs* discusses general motif-count covariances; the available abstract does not establish the component-isolation Palm identity, but its full text was inaccessible, so implicit historical coverage remains a risk.

Previously available fixed-edge results for the isolated-edge/triangle pair, and a general degree-count/motif theorem under independent edges, cover some elementary special cases or different observables. In particular, the \(H=K_2\), \(F=K_3\) instance of (1) is **not claimed as new**. A published formula for covariance between total component count and triangle count under bond percolation treats the sum across all component isomorphism types; it neither resolves individual component types nor implies the induced two-boundary classification or the sharp tree-shape envelope. The contribution assessed here is their unified, all-connected-pattern component-versus-motif classification and its explicit two-switch and tree-shape consequences, not the generic covariance-of-indicators technique.

## Limitations

The exact factorization requires independent edge retention and connected \(F\). For disconnected \(F\), a copy may straddle the component boundary without using a cross-edge, and the proof fails. For degree-constrained or fixed-edge random graphs, the external graph is not independent with unchanged edge probability. The result concerns covariance signs, not independence, concentration rates, or causal influence. The asymptotic threshold applies to fixed motifs, not growing motifs. Earlier implicit overlap identities and an inaccessible 1979 full text remain originality risks; independent audit has not been performed.

## References

1. R. B. Ellis and J. P. Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, preprint dated 2009-09-14, https://math.iit.edu/~rellis/papers/12variance.pdf ; *Discrete Applied Mathematics* 158 (2010), 649–658, DOI 10.1016/j.dam.2009.11.012.
2. R. Ginoza and A. Mugler, *Network motifs come in sets: correlations in the randomization process*, arXiv:0907.4680, initially submitted 2009-07-27, https://arxiv.org/abs/0907.4680 ; *Physical Review E* 82 (2010), 011921.
3. O. Frank, *Moment Properties of Subgraph Counts in Stochastic Graphs*, *Annals of the New York Academy of Sciences* 319 (1979), 207–218, DOI 10.1111/j.1749-6632.1979.tb32791.x (abstract inspected; full text not accessed).
