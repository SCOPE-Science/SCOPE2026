# Exact Hilbert distortion and dimension transition for snowflaked clique bouquets

## Finding
For integers \(k\ge 2\) and \(m_1,\ldots,m_k\ge 1\), let \(G\) be the unweighted graph made by identifying a single hub across \(k\) cliques of respective orders \(m_i+1\). There are \(N=\sum_i m_i\) non-hub vertices. For \(0\le\alpha\le1\), equip its vertices with the snowflake \(d_\alpha=d_G^\alpha\), taking \(d_0(x,y)=1\) for distinct vertices. Put
\[
 r=2^{2\alpha},\qquad b_i=\frac{r-1+1/m_i}{2},\qquad
 S=\sum_{i=1}^k\frac1{b_i},\qquad R^2=\frac r2-\frac1S.
\]
Then the least bi-Lipschitz distortion into an arbitrary real Hilbert space is
\[
 \boxed{c_2(V(G),d_\alpha)=\max\{1,\sqrt{R^2}\}.}
\]
The function \(R^2\) increases strictly with \(\alpha\). There is a unique \(\alpha_*\in(0,1]\) with \(R^2(\alpha_*)=1\), and \(\alpha_*=1\) holds exactly for \(k=2\) and \(m_1=m_2=1\). Thus the snowflake isometrically embeds in Hilbert space exactly when \(0\le\alpha\le\alpha_*\). All optimally normalized embeddings are congruent (up to a Euclidean isometry). Their affine dimension is exactly \(N\) for \(\alpha<\alpha_*\) and exactly \(N-1\) for \(\alpha\ge\alpha_*\).

For balanced bouquets \(m_1=\cdots=m_k=m\), the formulas become
\[
 c_2^2=\max\left\{1,\frac{(k-1)2^{2\alpha}+1-1/m}{2k}\right\},
 \qquad \alpha_* =\frac12\log_2\frac{2k-1+1/m}{k-1}.
\]
In particular, the ordinary unweighted graph metric (\(\alpha=1\)) satisfies
\[
 c_2(V(G),d_G)^2=2-\left(2\sum_{i=1}^k\frac{m_i}{3m_i+1}\right)^{-1}.
\]
The friendship graph with \(k\) triangles is the case \(m_i=2\), yielding \(c_2^2=2-7/(4k)\).

## Assumptions and scope
All graphs are finite, simple and unweighted, and all Hilbert spaces are real with unrestricted dimension. For distinct non-hub vertices the graph metric is \(1\) within one clique and \(2\) across different cliques; each hub–leaf distance is \(1\). Raising these distances to \(\alpha\in[0,1]\) gives within-block and hub distances \(1\), cross-block distance \(t=2^\alpha\). This is a metric since \(1\le t\le2\). For an embedding \(f\), its distortion is the least \(C\ge1\) for which some \(s>0\) satisfies \(s d_\alpha(x,y)\le\|f(x)-f(y)\|\le sC d_\alpha(x,y)\) for every pair; an embedding is *noncontractingly normalized* after scaling to \(s=1\).

## Proof
**1. Exact weighted variance lower bound.** Let \(a_i=(m_i-1)/(2m_i)\), so \(a_i+b_i=r/2\), and define strictly positive weights \(p_i=b_i^{-1}/S\), \(w_{ia}=p_i/m_i\) on the \(N\) non-hub vertices \((i,a)\). For a noncontractingly normalized embedding put the hub at \(0\) and write its leaf vectors as \(x_{ia}\). The weighted Hilbert variance identity is
\[
 \sum_{u<v}w_uw_v\|x_u-x_v\|^2
 =\sum_u w_u\|x_u\|^2-\left\|\sum_u w_ux_u\right\|^2.
\]
All hub–leaf distances are at most \(C\), while all distinct within-block distances are at least \(1\) and all cross-block distances are at least \(t\). Consequently,
\[
 C^2\ge\sum_i a_ip_i^2+r\sum_{i<j}p_ip_j
 =\frac r2-\sum_i b_ip_i^2
 =\frac r2-\frac1S=R^2.
\]
Also \(C\ge1\), proving the universal lower bound.

**2. Explicit Hilbert realization.** Choose pairwise orthogonal vectors \(u_i\) with \(\|u_i\|^2=b_i\). For each \(i\), in a subspace orthogonal to all the \(u_j\) and all other block subspaces, take a centered regular simplex \(v_{ia}\), \(1\le a\le m_i\), with \(\|v_{ia}-v_{ib}\|^2=1\) for \(a\ne b\) and \(\|v_{ia}\|^2=a_i\). If \(m_i=1\), use \(v_{i1}=0\). Put \(y_{ia}=u_i+v_{ia}\). Its pairwise squared distances are \(1\) within a block and \(r\) between blocks, because \(a_i+b_i=r/2\). Let \(c=\sum_i p_i u_i\). Since \(p_ib_i=1/S\), we have \(\|c\|^2=1/S\) and
\[
 \|y_{ia}-c\|^2=a_i+b_i-2/S+1/S=R^2
\]
for every leaf. When \(R^2\ge1\), place the hub at \(c\): this attains distortion \(\sqrt{R^2}\). When \(R^2<1\), place the hub at \(c+z\), where \(z\) is perpendicular to every leaf subspace and \(\|z\|^2=1-R^2\): every pairwise metric distance is then attained exactly, so distortion is \(1\). In both regimes the lower bound is sharp.

**3. Uniqueness and affine dimension.** For \(R^2>1\), equality in the strictly positive weighted variance estimate forces all hub–leaf squared distances to equal \(R^2\), all within-block distances to equal \(1\), all cross-block distances to equal \(r\), and the weighted leaf barycenter to coincide with the hub. Thus all pairwise Euclidean distances are fixed; any two optimal normalized embeddings are congruent. For \(R^2\le1\), optimal distortion equals \(1\), so all pairwise distances are again fixed and congruence follows.

The leaf configuration always has affine dimension \(N-1\). Indeed, for any nonzero real coefficients \(z_{ia}\) summing to zero, write \(T_i=\sum_a z_{ia}\). Its Euclidean squared norm under the construction is
\[
 \left\|\sum_{i,a}z_{ia}y_{ia}\right\|^2
 =\sum_i b_iT_i^2+\frac12\sum_i\left(\sum_a z_{ia}^2-\frac{T_i^2}{m_i}\right)>0.
\]
Every summand is nonnegative, and equality forces every coefficient to vanish. The weighted circumcenter \(c\) belongs to the affine hull of the leaves. If \(R^2<1\), the hub lies at a nonzero perpendicular displacement from that affine hull, so the full affine dimension is \(N\). If \(R^2\ge1\), the hub lies at \(c\), so it is \(N-1\). The same statements apply to every optimal embedding by congruence.

**4. Sharp snowflake threshold.** The weighted lower-bound expression satisfies
\[
 R^2(r)=\max_{p_i\ge0,\,\sum_i p_i=1}
 \left\{\sum_i a_i p_i^2+r\sum_{i<j}p_ip_j\right\},
\]
by a one-line weighted Cauchy–Schwarz minimization; its unique maximizing weights are \(p_i=b_i^{-1}/S>0\). For \(r_2>r_1\), evaluating the expression at the maximizer for \(r_1\) proves \(R^2(r_2)>R^2(r_1)\), because \(k\ge2\) and all the maximizing weights are positive. At \(r=1\), \(S=2N\), giving \(R^2=(N-1)/(2N)<1\). At \(r=4\), \(S=\sum_i2m_i/(3m_i+1)\ge k/2\ge1\), so \(R^2\ge1\), with equality only for two singleton blocks. Continuity yields one and only one threshold. Substituting equal sizes \(m_i=m\) gives the displayed closed forms.

## Verification
The accompanying standalone Python checker uses only exact rational arithmetic. It checked \(585\) choices of block-size tuple and squared interblock distance, with \(72{,}300\) rational assertions, including explicit Gram identities, full exact matrix ranks, weighted variance identities, all pairwise distance constraints and balanced-threshold algebra. Run `python3 check.py`. All checked instances passed. Finite checks do not establish the theorem for every parameter; the four analytical steps above do.

## Relationship to prior work
Robertson (2023, arXiv:2309.16070v1) develops distorted negative type and proves exact Hilbert distortion for complete bipartite graph metrics and Hamming cubes; those theorems do not state the present clique-bouquet formula, its variable-size harmonic law, or its dimension transition. Lou, Obata and Huang (2020, arXiv:2001.06752v1) explicitly calculate the *quadratic embedding constant* of friendship graphs, which concerns conditional negative definiteness of the unsquared distance matrix, not least bi-Lipschitz distortion of the graph metric or its full snowflake family. Choudhury and Nandi (2023, arXiv:2306.15589v1) and Baskoro and Obata (2023, arXiv:2311.03342v1) likewise study quadratic embedding constants, not this quantitative least-distortion/rigidity classification. Those related results and the standard regular-simplex realization motivate the question but do not by themselves give the stated formula.

## Limitations
The theorem applies only to bouquets with one shared hub, uniformly unit internal and hub-edge lengths, and snowflake exponents \(0\le\alpha\le1\). It makes no claim for arbitrary weighted clique bouquets, multi-hub joins, target spaces other than real Hilbert spaces, or quantitative stability of near-optimal embeddings. Bibliographic priority remains provisional: an equivalent earlier result might be expressed using Euclidean distance matrices or minimum enclosing spheres. Independent audit and independent mathematical validation have not been performed.

## References
1. G. Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space*, arXiv:2309.16070v1, first public 2023-09-27. https://arxiv.org/abs/2309.16070
2. Z. Lou, N. Obata, Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752, first public 2020-01-19. https://arxiv.org/abs/2001.06752
3. P. N. Choudhury, R. Nandi, *Quadratic Embedding Constants of Graphs: Bounds and Distance Spectra*, arXiv:2306.15589, first public 2023-06-27. https://arxiv.org/abs/2306.15589
4. E. T. Baskoro, N. Obata, *A Classification of Graphs through Quadratic Embedding Constants and Clique Graph Insights*, arXiv:2311.03342, first public 2023-11-06. https://arxiv.org/abs/2311.03342
