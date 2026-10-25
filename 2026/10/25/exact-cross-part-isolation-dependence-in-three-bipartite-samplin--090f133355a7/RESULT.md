# Exact cross-part isolation dependence in three bipartite sampling ensembles

## Finding
Let \(a,b\ge2\) and let \(G_{a,b,m}\) be the uniformly selected \(m\)-edge simple subgraph of \(K_{a,b}\), with \(0\le m\le ab\). Denote by \(I_L\) and \(I_R\) its numbers of isolated left and right vertices. For all integers \(0\le r\le a\), \(0\le s\le b\),
\[
\mathbb E[(I_L)_{\underline r}(I_R)_{\underline s}]
=(a)_{\underline r}(b)_{\underline s}
\frac{\binom{(a-r)(b-s)}m}{\binom{ab}m}.
\tag{1}
\]
Here \((z)_{\underline k}\) is the falling factorial, and \(\binom uv=0\) when \(v>u\ge0\). For \(1\le r<a\) and \(1\le s<b\), if the two individual factorial moments are nonzero and \(m\ge2\), then
\[
\mathbb E[(I_L)_{\underline r}(I_R)_{\underline s}]
<\mathbb E[(I_L)_{\underline r}]\,\mathbb E[(I_R)_{\underline s}].
\tag{2}
\]
In particular, \(\operatorname{Cov}(I_L,I_R)<0\) exactly when
\[
2\le m\le \min\{(a-1)b,a(b-1)\};
\tag{3}
\]
it is zero otherwise. For the balanced sparse regime \(a=b=n\) and \(m/n\to c\in(0,\infty)\),
\[
\operatorname{Cov}(I_L,I_R)\longrightarrow-\frac{c^2}{2}e^{-2c}.
\tag{4}
\]
The sign contrasts with two other natural ensembles. If \(m\) edges are independently sampled **with** replacement from the \(ab\) possibilities, the left and right isolation counts are independent. If each possible edge is instead included independently with probability \(p\in(0,1)\), then
\[
\operatorname{Cov}(I_L,I_R)=ab\,p(1-p)^{a+b-1}>0.
\tag{5}
\]
The assertion is factorial-moment negative dependence **across** the two parts; it does not claim full negative association of the two count vectors or negative quadrant dependence.

## Assumptions and scope
The vertex bipartition is labeled and fixed. The fixed-edge model chooses one of \(\binom{ab}m\) *distinct-edge sets* uniformly, not \(m\) draws with replacement. Variables \(I_L\) and \(I_R\) include isolated vertices even when \(m=0\). The strict assertion (2) assumes both separate factorial moments positive; cases with an impossible isolated subset yield equality at zero. All graph sizes in (1)--(3) are finite; (4) is an asymptotic statement with \(c\) fixed and positive.

## Proof
Fix \(r\) specified left vertices and \(s\) specified right vertices. Their isolation excludes the \(rb+as-rs\) edges incident to either set, leaving \((a-r)(b-s)\) allowable edges. Uniform selection of \(m\) distinct edges gives probability \(\binom{(a-r)(b-s)}m/\binom{ab}m\). Sum over ordered \(r\)-tuples and \(s\)-tuples to obtain (1).

Write \(N=ab\), \(u=rb\), \(v=as\), and \(w=rs\). The probabilities that the specified left set, right set, and both sets are isolated are respectively
\[
P_L=\frac{\binom{N-u}m}{\binom Nm},\qquad
P_R=\frac{\binom{N-v}m}{\binom Nm},\qquad
P_{LR}=\frac{\binom{N-u-v+w}m}{\binom Nm}.
\]
When \(m\le N-u-v+w\), their exact ratio factorizes as
\[
\frac{P_{LR}}{P_LP_R}=
\prod_{j=0}^{m-1}
\left(1-\frac{rsj}{(N-rb-j)(N-as-j)}\right).
\tag{6}
\]
Indeed, each factor follows from the algebraic identity
\[
(N-u-v+w-j)(N-j)=(N-u-j)(N-v-j)-rsj,
\]
which uses \(uv=rsN\). Every factor in (6) is positive and at most one, and the factor at \(j=1\) is strictly smaller than one when \(m\ge2\). If \(m>N-u-v+w\) but the two marginal isolation events remain possible, \(P_{LR}=0<P_LP_R\). If either marginal event is impossible, its joint event is also impossible. These cases prove (2), with equality when \(m\in\{0,1\}\). Taking \(r=s=1\) and multiplying by \(ab\) establishes (3).

For (4) write \(N=n^2\), \(m=m_n\), and
\[
q_n=\frac{\binom{n^2-n}{m}}{\binom{n^2}m},\qquad
R_n=\prod_{j=0}^{m-1}\left(1-\frac{j}{(n^2-n-j)^2}\right).
\]
For all sufficiently large \(n\), the product is in its positive-denominator range. Since \(m=O(n)\),
\[
\log q_n=-m/n+O(n^{-1}),\qquad
\log R_n=-\frac{m(m-1)}{2n^4}+O(n^{-3}).
\]
Therefore \(q_n\to e^{-c}\), \(n^2(R_n-1)\to-c^2/2\), and
\[
\operatorname{Cov}(I_L,I_R)=n^2q_n^2(R_n-1)\to-\frac{c^2}2e^{-2c}.
\]
For sampling with replacement, every draw is an independent pair of a uniformly chosen left index and an independently chosen right index. The entire left-index sequence is independent of the entire right-index sequence, so their respective isolated counts are independent. In the independent-edge model, one fixed left vertex is isolated with probability \((1-p)^b\), one fixed right vertex with probability \((1-p)^a\), and both with probability \((1-p)^{a+b-1}\); subtracting the product and summing over the \(ab\) vertex pairs proves (5).

## Verification
The standalone `verify.py` uses only the Python standard library. Execute `python verify.py` beside this document. It verifies 58,896 exact-rational general-parameter inequalities and product identities, 1,318 independently enumerated factorial-moment identities over 74,384 binary matrices, and a numerical sparse-limit sequence. The finite calculations are consistency checks, not substitutes for the all-size combinatorial and asymptotic arguments.

## Relationship to prior work
Joag-Dev and Proschan (1983) establish negative association for sampling without replacement, with its stated closure property applying to functions of **disjoint** subsets of coordinates. The forbidden edge families for one left-vertex set and one right-vertex set intersect in \(rs\) edges, so that result alone does not imply (2). Blasiak and Durrett (2004, introduction, pp. 1--3) analyze random Oxford bipartite graphs obtained by **sampling with replacement** and explicitly use independence of row- and column-nonemptiness events. That agrees with the independent-count ensemble here, not with distinct-edge sampling; their subsequent results concern component sizes and connectivity. Saltykov (1995) studies a with-replacement bipartite graph and a Poisson limit for total isolates near connectivity. The exact finite distinct-edge factorial inequality, the three-ensemble sign contrast, and the constant in (4) were not identified in these inspected treatments or the searches recorded in the accompanying review; their absence from a search is not proof of historical uniqueness.

## Limitations
The calculation is specific to complete bipartite edge sets with equal selection probability; it does not extend automatically to irregular host graphs, nonuniform edge weights, or prescribed degrees. The inequality is for factorial moments of counts from opposite parts, not for arbitrary increasing transforms. The sparse-limit constant concerns covariance, not an assertion of asymptotic independence. Historical-priority uncertainty remains, especially for older sources on random rectangular occupancy tables and negative dependence.

## References
- K. Joag-Dev and F. Proschan, *Negative Association of Random Variables with Applications*, Annals of Statistics 11 (1983), 286--295, https://doi.org/10.1214/aos/1176346079.
- J. Blasiak and R. Durrett, *Random Oxford Graphs*, public preprint dated June 2004, https://sites.math.duke.edu/~rtd/RG/rndgr0604.pdf.
- A. I. Saltykov, *The Number of Components in a Random Bipartite Graph*, Discrete Mathematics and Applications 5 (1995), 515--524, https://doi.org/10.1515/DMA.1995.5.6.515.
