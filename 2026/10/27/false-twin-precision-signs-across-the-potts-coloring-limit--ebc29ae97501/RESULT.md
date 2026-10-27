# False-twin precision signs across the Potts coloring limit

## Finding
Let \(G=(V,E)\) be a finite simple graph with distinct nonadjacent vertices \(u,v\) having the same open neighborhood \(N\). Choose a coloring \(\sigma:V\to\{1,\ldots,q\}\) with probability proportional to \(w^{m(\sigma)}\), where \(m(\sigma)\) is its number of monochromatic edges. Put \(X_x=\mathbf 1\{\sigma(x)=1\}\), \(\Sigma=\operatorname{Cov}((X_x)_{x\in V})\), and \(Q=\Sigma^{-1}\).

For \(q\ge3\) and \(0<w<\infty\), the matrix \(\Sigma\) is positive definite and
\[
Q_{uv}\le0,\qquad Q_{uv}<0\ \Longleftrightarrow\ |N|\ge2\ \text{and}\ w\ne1.
\]
In particular, the precision entry vanishes for every positive \(w\) when \(|N|\le1\), and at \(w=1\) for every graph.

At \(w=0\), assume \(q\ge\max\{3,\chi(G)+1\}\), and sample a uniform proper \(q\)-coloring. Then \(\Sigma\) is positive definite and \(Q_{uv}\le0\). If \(N\) is a clique, then \(Q_{uv}=0\). Conversely, whenever \(q\ge\max\{3,|V|\}\),
\[
Q_{uv}=0\ \Longleftrightarrow\ N\ \text{is a clique},
\qquad Q_{uv}<0\ \Longleftrightarrow\ N\ \text{is not a clique}.
\]
Thus when two false twins have a common neighboring clique of size at least two and \(q\ge |V|\), the precision entry is zero for proper colorings, but strictly negative for every \(0<w<\infty\) with \(w\ne1\). This is a sharp zero-temperature versus positive-temperature sparsity distinction.

## Assumptions and scope
A *false-twin pair* comprises nonadjacent distinct vertices with identical open neighborhoods. The graph is finite and simple. The Potts weight is \(w^{m(\sigma)}\), with the convention \(0^0=1\). For \(w=0\), only proper colorings receive positive weight. At positive \(w\), no graph-coloring feasibility condition is needed. \(Q_{uv}\) is the off-diagonal entry of the **full** inverse covariance matrix of one fixed color's indicator at **every** vertex. It is not the inverse of a two-by-two marginal covariance, nor the usual Potts interaction matrix.

## Proof
**1. Positive definiteness.** For \(w>0\), each of the \(q^{|V|}\) colorings has positive probability. Since \(q\ge3\), every binary indicator vector occurs with positive probability: choose color \(1\) at the specified vertices and color \(2\) elsewhere. In particular, the all-zero vector and each coordinate vector occur, so the covariance is positive definite.

For \(w=0\), \(q-1\ge\chi(G)\) permits a proper coloring entirely in colors \(2,\ldots,q\). Recolor any single vertex with color \(1\), obtaining a proper coloring whose binary indicator is a coordinate vector. The same affine-support argument gives positive definiteness.

**2. Exact residual-variance identity.** Let \(H=(\sigma(x))_{x\notin\{u,v\}}\), \(Z=(X_x)_{x\notin\{u,v\}}\), and \(p(H)=\mathbb P(X_u=1\mid H)=\mathbb P(X_v=1\mid H)\). Conditional on \(H\), the colors of \(u\) and \(v\) are independent and identically distributed, because they are nonadjacent and have the same neighbor multiset. Consequently, \(X_u,X_v\) are conditionally independent Bernoulli variables with success probability \(p(H)\).

Denote by \(\widehat p(Z)\) the orthogonal projection of \(p(H)\) onto the affine span of \(1\) and the coordinates of \(Z\) in \(L^2\), and set
\[
S=\mathbb E[p(H)(1-p(H))],\qquad R=\mathbb E[(p(H)-\widehat p(Z))^2].
\]
These satisfy \(R\ge0\) and \(S>0\). For positive \(w\), every conditional color has strictly positive probability, so \(0<p(H)<1\). In the proper-coloring case, take a proper coloring of the full graph using at most \(q-1\) colors, relabeled into \(2,\ldots,q\). Its restriction to \(H\) uses at most \(q-2\) distinct colors on \(N\), since \(u\) must have a color absent from \(N\). Thus at least two colors remain available at \(u,v\) on an event of positive probability, again giving \(S>0\).

Write \(C=\operatorname{Cov}(Z)\), which is invertible by step 1, and \(a=\operatorname{Cov}(Z,p(H))\). The covariance blocks at \(u,v\) have diagonal \(S+\operatorname{Var}(p)\), off-diagonal \(\operatorname{Var}(p)\), and identical cross-covariance vectors \(a\). Since \(R=\operatorname{Var}(p)-a^{\mathsf T}C^{-1}a\), the Schur complement of \(C\) is
\[
\begin{pmatrix}S+R&R\\R&S+R\end{pmatrix}.
\]
Inverting this two-by-two block yields the *exact formula*
\[
\boxed{\displaystyle Q_{uv}=-\frac{R}{S(S+2R)}.}
\]
Hence \(Q_{uv}\le0\), and it is zero precisely when \(p(H)\) is an affine function of \(Z\) almost surely.

**3. Strictness at positive temperature.** Put \(d=|N|\). For \(w>0\), conditional on \(H\), let \(k_c(H)\) be the number of vertices of \(N\) colored \(c\). Then
\[
p(H)=\frac{w^{k_1(H)}}{\sum_{c=1}^{q}w^{k_c(H)}}.
\]
If \(d=0\), this is the constant \(1/q\). If \(d=1\), it takes only two values, according to whether that neighbor has color \(1\), and therefore is affine in its indicator coordinate. At \(w=1\), it is also constant.

Suppose \(d\ge2\) and \(w>0\), \(w\ne1\). Compare two positive-probability assignments \(H\): all vertices outside \(\{u,v\}\) colored \(2\), and the same assignment except that one vertex of \(N\) has color \(3\). Both have \(Z=0\), while their conditional probabilities are respectively
\[
\frac1{w^d+q-1},\qquad\frac1{w^{d-1}+w+q-2}.
\]
The denominators differ by \((w-1)(w^{d-1}-1)\ne0\). Thus \(p(H)\) cannot be a function of \(Z\), much less an affine one; \(R>0\), proving strict negativity.

**4. Zero-temperature structure.** On each positive-probability conditioning assignment \(H\), let \(K(H)\) be the set of colors occurring on \(N\). The proper-coloring conditional probability is
\[
p(H)=\begin{cases}0,&1\in K(H),\\[2pt]1/(q-|K(H)|),&1\notin K(H).\end{cases}
\]
If \(N\) is a clique of size \(d\), all its colors are distinct, so \(|K(H)|=d\) on support. Consequently
\[
p(H)=\frac{1-\sum_{x\in N}X_x}{q-d},
\]
an affine function of \(Z\). Here \(q-d\ge2\), because \(\chi(G)\ge d+1\) and \(q\ge\chi(G)+1\). Thus \(R=0\).

If \(N\) is not a clique, choose nonadjacent distinct \(a,b\in N\). Under \(q\ge|V|\), the following two proper assignments on \(V\setminus\{u,v\}\) both have positive probability after summing over possible colors at \(u,v\): first give all remaining vertices pairwise distinct colors from \(2,\ldots,q\); second give \(a,b\) the same color \(2\) and give every other remaining vertex its own distinct color from \(3,\ldots,q\). Their indicator vectors \(Z\) both vanish. However the numbers of different colors on \(N\) are respectively \(d\) and \(d-1\). Therefore \(p(H)\) takes the two distinct values \(1/(q-d)\) and \(1/(q-d+1)\) at the same \(Z\). It follows that \(R>0\), proving strict negativity. The case \(d=0\) or \(d=1\) is a clique by convention and was already covered. \(\square\)

## Verification
The standalone standard-library script `verify_potts_twins.py` enumerates complete colorings with exact rational Potts weights, computes the full covariance matrix by direct moments, inverts it using exact Gaussian elimination, separately computes the residual-variance formula, and compares the two expressions as well as their sign conditions. Its completed execution reports `EXACT_POTTS_CHECK_OK graph_palette_temperature_cases 588`. The cases include every false-twin graph on three to five labeled vertices with selected color counts and temperatures, plus selected six-vertex instances. These finite calculations check boundary and algebraic cases but do not replace the proof for arbitrary graphs.

## Relationship to prior work
The antiferromagnetic Potts literature studies proper-coloring limits and mixing, including Bencs–Berrekkal–Regts (2023) and Chen–Liu–Mani–Moitra (2023). Spectral-independence research, including Chen–Galanis–Štefankovič–Vigoda (2020), examines conditional influences relevant to mixing; these influence matrices are distinct from the full inverse covariance of a single color's indicator field. A related exact cycle-coloring precision analysis concerns one highly symmetric graph family. The theorem here makes an all-graph statement for false twins, gives the precise residual-variance identity, and classifies when graph-neighborhood structure causes a precision zero at positive versus zero temperature. Existing general Schur-complement and conditional-independence identities are ingredients, not claimed as new.

## Limitations
The theorem requires an identical common neighbor set and nonadjacent false twins, a homogeneous single interaction parameter, a common color palette, and the indicator of one fixed color. At zero temperature the *if and only if* clique classification is proved under \(q\ge|V|\); for the smaller admissible range \(\chi(G)+1\le q<|V|\), the conclusion is only \(Q_{uv}\le0\), with the clique sufficient condition. Nothing is asserted for \(q=2\) or singular low-palette proper-coloring measures. Zero precision is a statement about linear partial correlation; it is not in general interchangeable with nonlinear conditional independence. No historical uniqueness or independent validation is claimed.

## References
- F. Bencs, K. Berrekkal and G. Regts, *Near optimal bounds for weak and strong spatial mixing for the anti-ferromagnetic Potts model on trees*, arXiv:2310.04338, first posted October 6, 2023. https://arxiv.org/abs/2310.04338
- Z. Chen, K. Liu, N. Mani and A. Moitra, *Strong spatial mixing for colorings on trees and its algorithmic applications*, arXiv:2304.01954, first posted April 4, 2023. https://arxiv.org/abs/2304.01954
- Z. Chen, A. Galanis, D. Štefankovič and E. Vigoda, *Rapid Mixing for Colorings via Spectral Independence*, arXiv:2007.08058, first posted July 16, 2020. https://arxiv.org/abs/2007.08058
