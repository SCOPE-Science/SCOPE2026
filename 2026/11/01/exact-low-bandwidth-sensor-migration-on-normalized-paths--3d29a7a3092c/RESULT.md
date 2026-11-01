# Exact low-bandwidth sensor migration on normalized paths

## Finding

For each path on \(n\ge3\) vertices, one spatial sensor observes a graph signal at successive times. The optimal sensor for **determinant-based reconstruction of the first few low-frequency modes** changes sharply with the number of vertices. The following theorem gives all optimal sensors for the first two, three, or four modes, including every exceptional tie, and a general sufficient size threshold for any number of modes.

Let \(2\le m\le n\), and let \(C_j\) be the \(m\times m\) observation matrix defined below. Maximizing \(\det(C_j^*C_j)\) over vertices \(j\in\{0,\ldots,n-1\}\) gives exactly these sets:

| Low-frequency modes \(m\) | Path order \(n\) | All maximizing vertices (zero-based) |
|---|---|---|
| \(2\) | \(3\) | \(\{0,2\}\) |
| \(2\) | \(4\) | \(\{0,1,2,3\}\) |
| \(2\) | \(n\ge5\) | \(\{1,n-2\}\) |
| \(3\) | \(3\le n\le6\) | \(\{0,n-1\}\) |
| \(3\) | \(n\ge7\) | \(\{1,n-2\}\) |
| \(4\) | \(n=4\) | \(\{0,1,2,3\}\) |
| \(4\) | \(n=7\) | \(\{0,2,4,6\}\) |
| \(4\) | \(n=9\) | \(\{0,1,3,5,7,8\}\) |
| \(4\) | \(n\in\{5,6,8\}\) | \(\{0,n-1\}\) |
| \(4\) | \(n\ge10\) | \(\{1,n-2\}\) |

Furthermore, **for every integer \(m\ge2\) and \(n\ge\lceil3m^{3/2}\rceil\), the only maximizing vertices are \(1\) and \(n-2\)**.

Every assertion is independent of the particular spectral evolution: the same optimizers hold for \(T=h(B)\) whenever the values of \(h\) on the selected \(m\) eigenvalues are pairwise distinct. In particular they apply to heat evolution \(T=\exp[-\tau(I-B)]\) for every \(\tau>0\), as well as to \(T=B\). The result concerns the volume/determinant (\(D\)-optimal) objective, not necessarily the smallest singular value or the spectral condition number.

## Assumptions and scope

Let \(P_n\) be the unweighted path with vertex set \(\{0,1,\ldots,n-1\}\), adjacency matrix \(A\), degree matrix \(D\), and symmetric normalized adjacency \(B=D^{-1/2}AD^{-1/2}\). Write \(d_0=d_{n-1}=1\) and \(d_j=2\) for interior vertices. Its orthonormal eigenvectors \(v_k\) and simple eigenvalues \(\lambda_k\), indexed in descending order, are

\[
\lambda_k=\cos\left(\frac{k\pi}{n-1}\right),\qquad
v_k(j)=\frac{\sqrt{d_j}\cos\left(\frac{kj\pi}{n-1}\right)}{c_k},
\]

where \(c_k=\sqrt{2(n-1)}\) for \(k\in\{0,n-1\}\), and \(c_k=\sqrt{n-1}\) otherwise. We select the low-pass space \(E_m=\operatorname{span}\{v_0,\ldots,v_{m-1}\}\).

Choose any complex-valued function \(h\) on the spectrum with pairwise distinct \(\alpha_k=h(\lambda_k)\) for \(0\le k<m\). The evolution \(T=h(B)\) is diagonal in this orthonormal basis. For a sensor at vertex \(j\), sample \(T^t f(j)\) at \(t=0,1,\ldots,m-1\). In the coefficients of \(f\in E_m\), the observation matrix is

\[
C_j=\big(v_k(j)\alpha_k^t\big)_{0\le t,k<m}.
\]

For isotropic equal-variance independent sensor noise, the determinant of \(C_j^*C_j\) is proportional to the inverse generalized variance of the recovered spectral coefficients; maximizing it is the \(D\)-optimal sensor criterion. The signal, noise and sampling assumptions are part of the statement, not claims about other observation models.

## Proof

**1. Determinant reduction.** The measurement matrix factors as a Vandermonde matrix in the distinct \(\alpha_k\) times the diagonal matrix of \(v_k(j)\). Its squared determinant is

\[
\det(C_j^*C_j)=\left|\prod_{0\le a<b<m}(\alpha_b-\alpha_a)\right|^2
\prod_{k=0}^{m-1}|v_k(j)|^2.
\]

The Vandermonde factor is positive and independent of \(j\). The constants \(c_k\) in the eigenvector formula are likewise independent of \(j\). Hence, **without omitted normalization factors**, the exact vertex-to-endpoint ratio is

\[
\boxed{
\frac{\det(C_j^*C_j)}{\det(C_0^*C_0)}
=d_j^m\prod_{k=1}^{m-1}
\cos^2\left(\frac{kj\pi}{n-1}\right).}
\tag{1}
\]

This remains valid when \(m=n\), since the extra normalization at \(k=n-1\) cancels in the ratio. Both endpoints have ratio one, and reflection \(j\mapsto n-1-j\) preserves the ratio. On the first half of the path put \(\theta_j=\pi j/(n-1)\) and

\[
P_m(\theta)=\prod_{k=1}^{m-1}|\cos(k\theta)|.
\]

Then each interior vertex has square-root ratio \(2^{m/2}P_m(\theta_j)\).

**2. Two modes.** The interior square-root ratio is \(2\cos\theta_j\) on \(0<\theta_j\le\pi/2\), strictly decreasing with \(j\). The first neighbor beats an endpoint precisely when \(2\cos(\pi/(n-1))>1\), which holds for \(n\ge5\), is an equality for \(n=4\), and is false for \(n=3\). This gives the complete two-mode classification.

**3. Three modes.** Write \(t=\cos\theta\in[0,1]\). Then

\[
P_3(\theta)=t|2t^2-1|.
\]

On \(0\le t\le1/\sqrt2\) its maximum is \(2/(3\sqrt6)\), attained at \(t=1/\sqrt6\). On \(1/\sqrt2\le t\le1\) it is strictly increasing. If \(n\ge7\), the first interior point satisfies \(t_1\ge\sqrt3/2\), so

\[
P_3(\theta_1)\ge\frac{\sqrt3}{4}>
\frac{2}{3\sqrt6},\qquad
2^{3/2}P_3(\theta_1)>1.
\]

It therefore strictly beats all other interior vertices and both endpoints. For \(3\le n\le6\), direct exact values at the finitely many admissible angles give \(P_3(\theta_j)\le1/4\) for every interior \(j\), so \(2^{3/2}P_3(\theta_j)\le1/\sqrt2<1\). Thus the two endpoints are the only optima.

**4. Four modes.** With \(y=\cos^2\theta\), the interior product becomes

\[
P_4(\theta)=F(y),\qquad
F(y)=y|(2y-1)(4y-3)|.
\]

On \(3/4\le y\le1\), \(F\) is strictly increasing. On \(0\le y\le3/4\), elementary differentiation of the two cubic pieces gives the sharp upper bound

\[
F(y)\le c_*:=\frac{10+7\sqrt7}{108}<\frac{21}{64}.
\tag{2}
\]

If \(n\ge10\), \(y_1=\cos^2(\pi/(n-1))\ge\cos^2(\pi/9)>7/8\). The final strict inequality follows from

\[
\cos(2\pi/9)\ge1-\tfrac12(2\pi/9)^2>61/81>3/4,
\]

using \(\pi^2<10\). Consequently

\[
F(y_1)>F(7/8)=21/64>c_*.
\]

Every subsequent vertex on the first half has \(y_j<y_1\): if \(y_j\ge3/4\), monotonicity of \(F\) makes it strictly worse; if \(y_j\le3/4\), (2) makes it strictly worse. And \(4F(y_1)>1\), so the first neighbor beats both endpoints.

For the remaining orders \(4\le n\le9\), the exact internal-angle check is short. At \(n=4\), the two internal angles have \(y=1/4\) and \(F=1/4\). At \(n=5\), all internal \(F\)-values vanish. At \(n=6\), their possible values are \((\sqrt5-1)/16\) and \((\sqrt5+1)/16\), both smaller than \(1/4\). At \(n=7\), only the internal points \(j=2,4\) have \(F=1/4\). At \(n=9\), exactly \(j=1,3,5,7\) have \(F=1/4\), using \(\cos^2(\pi/8)=(2+\sqrt2)/4\) and \(\cos^2(3\pi/8)=(2-\sqrt2)/4\). Finally, at \(n=8\), consider the three internal points on the first half: their squared cosines lie respectively in \((3/4,\cos^2(\pi/8))\), \((1/4,1/2)\), and \((0,\cos^2(3\pi/8))\). On each interval, the corresponding cubic piece is monotone towards an endpoint at which \(F=1/4\), so each has \(F<1/4\). An internal point matches an endpoint exactly when \(4F=1\), which completes the four-mode table.

**5. General large-path sufficient threshold.** Suppose \(m\ge2\) and \(n\ge\lceil3m^{3/2}\rceil\). Put \(\delta=\pi/(n-1)\). Then \(n-1>(5/2)m^{3/2}\) and

\[
P_m(\delta)=\prod_{k=1}^{m-1}\cos(k\delta)
\ge1-\frac{\delta^2}{2}\sum_{k=1}^{m-1}k^2
>1-\frac{2\pi^2}{75}>
\frac{11}{15}>\frac{1}{\sqrt2}.
\tag{3}
\]

Here all factors are positive, \(\cos u\ge1-u^2/2\), and \(\prod(1-a_k)\ge1-\sum a_k\) for \(0\le a_k\le1\). The sum of squares is less than \(m^3/3\). For \(\delta\le\theta\le\pi/[2(m-1)]\), every cosine is nonnegative and the product decreases strictly. For \(\pi/[2(m-1)]\le\theta\le\pi/2\), let \(k\in\{1,\ldots,m-1\}\) be a nearest integer to \(\pi/(2\theta)\). Then

\[
|\cos(k\theta)|\le\sin(\theta/2)\le1/\sqrt2,
\qquad P_m(\theta)\le1/\sqrt2<P_m(\delta).
\]

Thus vertex \(1\) is the unique maximizer on the open first half and, by reflection, vertex \(n-2\) is the only other interior maximizer. Finally \(2^{m/2}P_m(\delta)>1\), so these two also strictly beat the endpoints. This proves the general threshold.

## Verification

The included standalone `CHECK.py` uses only the Python standard library. It independently forms symmetric normalized path-adjacency matrices, constructs and checks their normalized eigenvectors, iterates the graph operator, computes small determinants by elimination, and compares the direct determinant ratios with (1). It also tests heat-evolution Vandermonde matrices, all path orders up to \(300\) for the complete two-through-four-mode classification, and finite instances of the general \(\lceil3m^{3/2}\rceil\) theorem through \(m=18\). Executing `python CHECK.py` produced `CHECK_OK assertions=5641`.

These computations are reproducibility checks rather than an exhaustive proof for unbounded \(n\) or \(m\); the proof above provides the universal quantifiers. In particular, step 5 is analytical and not inferred from the sampled sizes.

## Relationship to prior work

Marques, Segarra, Leus and Ribeiro (2015/2016) develop single-node graph aggregation sampling, its Vandermonde factorization, and general \(D\)-optimal experiment-design criteria. Their factorization supplies a starting point, not the present exact **all-orders low-pass path sensor classification** or its exceptional ties. Bulai, Cabrelli, Cordero, Molter and Saliani (first public version 2026-09-21) study graph Paley-Wiener dynamical sampling and report numerical investigations of path-graph conditioning and sensor placement; their accessible abstract does not state the classifications above. A separate published note treats the **full-spectrum** path determinant, for which endpoints are optimal. Its full-spectrum theorem does not cover the strict low-pass modes here: the low-pass optimum is instead one step inward for large enough paths. General graph-filter and Vandermonde sampling criteria are not claimed as new.

## Limitations

This result concerns symmetric *normalized* adjacency on an unweighted path, the first \(m\) eigenmodes, exactly \(m\) successive samples from a single fixed vertex, and the determinant objective. It does not optimize the worst singular value, the condition number, or arbitrary multi-vertex sensor sets. The general \(\lceil3m^{3/2}\rceil\) bound is a sufficient—not sharp—threshold for \(m\ge5\). The 2026 motivating article's full PDF was not accessible during the literature comparison; a previously unindexed equivalent characterization remains a priority risk.

## References

1. A. G. Marques, S. Segarra, G. Leus, A. Ribeiro, *Sampling of graph signals with successive local aggregations*, IEEE Transactions on Signal Processing **64** (2016), 1832–1843. DOI: 10.1109/TSP.2015.2507546. Author manuscript: https://www.seas.upenn.edu/~aribeiro/preprints/2015_marques_etal.pdf .
2. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces*, arXiv:2609.25472, first submitted 2026-09-21. https://arxiv.org/abs/2609.25472 .
3. L. Huang, D. Needell, S. Tang, *Robust estimation of smooth graph signals from randomized space–time samples*, Information and Inference **13** (2024), iaae012. DOI: 10.1093/imaiai/iaae012.
4. *Universal endpoint optimality for dynamical sampling on normalized paths* (public mathematical research record, 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f .
