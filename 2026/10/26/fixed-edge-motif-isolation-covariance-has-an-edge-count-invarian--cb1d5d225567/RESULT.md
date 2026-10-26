# Fixed-edge motif–isolation covariance has an edge-count-invariant sign

## Finding
Let \(G\) be uniform among simple graphs with vertex set \([n]\) and exactly \(m\) edges. Let \(I\) count its isolated vertices. For a fixed simple graph \(H\) without isolated vertices, let \(X_H\) count non-induced, unlabelled edge-subgraph copies of \(H\) (different embeddings are identified modulo automorphisms of \(H\)). Write \(k=|V(H)|\), \(e=|E(H)|\), \(N=\binom n2\), and \(B=\binom{n-1}{2}\). For integers \(n>k\ge2\), \(e\ge1\), and \(e\le m\le B\),
\[
\operatorname{Cov}(I,X_H)=\mathbb E[I]\mathbb E[X_H]\left(\frac{n-k}{n}\frac{(N)_{\underline e}}{(B)_{\underline e}}-1\right).
\]
Consequently its sign is independent of \(m\) across the nondegenerate range, and depends only on \(n,k,e\), not the incidence pattern of \(H\). In particular, for \(n\ge5\), isolated-vertex count is strictly positively correlated in the covariance sense with the count of two-edge wedges \(P_3\), but strictly negatively correlated with the count of two-edge matchings \(2K_2\), simultaneously for every \(2\le m\le B\). For \(H=P_3\sqcup K_2\), the covariance is strictly negative for \(6\le n\le10\), and strictly positive for \(n\ge11\), for every \(3\le m\le B\). By contrast, in the independent-edge model \(G(n,p)\), \(0<p<1\), the covariance with every such \(X_H\) is \(-k\mathbb E[I]\mathbb E[X_H]/n<0\).

## Assumptions and scope
All random graphs are labeled on \([n]\). A motif occurrence requires all edges of \(H\), but permits additional edges among its vertices. It is counted once per image edge set, rather than once per injective embedding; the total number of potential copies is \(a_H=(n)_{\underline k}/|\operatorname{Aut}(H)|\). The motif has no isolated vertices so that an isolated host vertex cannot lie in the image of a present copy. The proof and strict sign conclusions assume \(n>k\), \(e\le m\le B\), which give both means strictly positive. Define \((z)_{\underline j}=z(z-1)\cdots(z-j+1)\), with the empty product one. For \(m<e\), the motif count is identically zero; for \(m>B\), the isolated count is zero. Those degenerate cases have zero covariance and are excluded from the stated strict signs.

## Proof
Fix one possible copy of \(H\), and a host vertex \(v\). If \(v\) belongs to the copy, its isolation is incompatible with the copy's occurrence because every vertex of \(H\) has positive degree. If \(v\) does not belong to the copy, all \(e\) required motif edges are among the \(B\) edges avoiding \(v\); hence
\[
\Pr(v\text{ isolated and this copy present})=\frac{\binom{B-e}{m-e}}{\binom Nm}.
\]
There are precisely \(n-k\) eligible host vertices per copy. Therefore
\[
\mathbb E[I X_H]=(n-k)a_H\frac{\binom{B-e}{m-e}}{\binom Nm},\qquad
\mathbb E[I]=n\frac{\binom Bm}{\binom Nm},\qquad
\mathbb E[X_H]=a_H\frac{(m)_{\underline e}}{(N)_{\underline e}}.
\]
The falling-factorial identity
\[
\frac{\binom{B-e}{m-e}}{\binom Bm}=\frac{(m)_{\underline e}}{(B)_{\underline e}}
\]
and cancellation yield the displayed covariance formula. The bracket has no occurrence of \(m\) or motif-specific structure other than \(k,e\).

For \(H=P_3\) and \(H=2K_2\), multiply the bracket by the strictly positive quantity \(n(B)_{\underline2}\). Direct factorization gives respectively
\[
(n-3)(N)_{\underline2}-n(B)_{\underline2}=\frac{n(n-1)(n-2)(n-3)}4>0,
\]
\[
(n-4)(N)_{\underline2}-n(B)_{\underline2}=-n(n-1)(n-2)<0.
\]
For \(H=P_3\sqcup K_2\), the analogous numerator is
\[
(n-5)(N)_{\underline3}-n(B)_{\underline3}=\frac{n(n-1)(n-2)}8\big(n^3-12n^2+15n+20\big).
\]
The cubic takes negative values at each of \(n=6,7\) and is strictly increasing for integer \(n\ge8\), since its derivative is \(3n^2-24n+15>0\) there. It is \(-30\) at \(n=10\) and \(64\) at \(n=11\), giving the asserted sharp crossover.

Finally, in \(G(n,p)\), the absence of edges incident to a vertex outside a chosen copy is independent of all edges required by that copy, while the events are incompatible for a vertex inside the copy. Summing gives \(\mathbb E[I X_H]=(n-k)a_H(1-p)^{n-1}p^e\), whereas \(\mathbb E[I]=n(1-p)^{n-1}\) and \(\mathbb E[X_H]=a_Hp^e\). Subtraction proves \(\operatorname{Cov}(I,X_H)=-k\mathbb E[I]\mathbb E[X_H]/n\).

## Verification
Run the accompanying standalone `verify.py` with Python 3 (standard library only). Its exact-rational enumerator checks every fixed-edge graph in the supported exhaustive cases \(n=5\) for \(P_3\) and \(2K_2\), and \(n=6\) for \(P_3\sqcup K_2\). This covers 32,380 graphs and verifies the covariance and both marginal means; additional exact algebraic assertions cover the sign and factorization cases through \(n=100\). It returns `VERIFY_OK 32380 exhaustively enumerated fixed-edge graphs; 436 exact checks`. The infinite all-parameter theorem is established by the preceding combinatorial proof; exhaustive finite tests are consistency checks only.

## Relationship to prior work
Dembo and Lubetzky, arXiv:1804.11327 (first posted 2018-04-30), develop the fixed-edge \(G(n,m)\) graphon large-deviation principle. Goldschmidt, Griffiths and Scott, arXiv:1902.06830 (first posted 2019-02-18), derive exact expected non-induced subgraph counts and study martingale moderate deviations in \(G(n,m)\); their expected-copy formula supplies standard background but their inspected results do not state the present exact motif–isolation covariance or its edge-count-independent sign and sharp motif comparisons. General conditional-moment identities may make this finding implicit in older literature; historical priority has not been independently settled. The binomial-model contrast is a standard consequence of edge independence and is included for interpretation, not claimed as a new marginal identity.

## Limitations
The exact signs require positive means and the non-induced motif convention. This does not classify induced motif counts, vertex-degree histograms other than isolation, or other conditioning schemes. The claim concerns covariances; positive covariance is not positive association. Standard elementary hypergeometric counting underlies the proof, so the structural sign consequences—not the mere mean formulas—are the distinctive result. Published-work coverage remains subject to historical-priority uncertainty, and no independent audit has been performed.

## References
1. A. Dembo and E. Lubetzky, *A large deviation principle for the Erdős–Rényi uniform random graph*, arXiv:1804.11327 (2018), https://arxiv.org/abs/1804.11327.
2. C. Goldschmidt, S. Griffiths and A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs G(n,m) and G(n,p)*, arXiv:1902.06830 (2019), https://arxiv.org/abs/1902.06830.
