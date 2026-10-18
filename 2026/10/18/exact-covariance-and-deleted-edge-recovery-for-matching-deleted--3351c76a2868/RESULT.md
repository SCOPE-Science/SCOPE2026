# Exact covariance and deleted-edge recovery for matching-deleted complete-graph Lipschitz balls

## Finding

Let \(N\ge3\), and let \(M\) be any nonempty matching of \(m\) edges on \(N\) labeled vertices, with \(1\le m\le\lfloor N/2\rfloor\). Equip the graph obtained from \(K_N\) by deleting \(M\) with its unit-edge shortest-path metric, and put \(H=\{z\in\mathbb R^N:\sum_i z_i=0\}\). Write \(X\) for a uniformly distributed potential in the unit ball of the real Lipschitz dual, modulo constant functions, and choose the centered representative \(Z=X-\overline X\mathbf1\in H\).

Set \(s=N-2m\), \(T=N(N-1)+2m\), \(P=I-\mathbf1\mathbf1^{\mathsf T}/N\), and \(E\) equal to the diagonal indicator matrix of all endpoints of edges in \(M\). Define the orthogonal projector
\[
U=\frac12\sum_{\{a,b\}\in M}(e_a-e_b)(e_a-e_b)^{\mathsf T}.
\]
With the rational coefficients
\[
A=\frac{(N-1)(N^2+3N+2m+2)}{12(N+1)T},\quad
B=\frac{N^2+3N+4}{N(N+1)T},\quad
C=\frac{N-1}{6(N+1)T},
\]
the **full centered covariance operator**, not merely its trace, is
\[
\boxed{\operatorname{Cov}(Z)=AP+BU-CPEP.}
\]
On \(H\), its distinct invariant-component eigenvalues and multiplicities are:

| Component | Eigenvalue | Multiplicity |
| --- | --- | --- |
| Antisymmetric matched pairs | \(A+B-C\) | \(m\) |
| Matched-pair constants of total sum zero | \(A-C\) | \(m-1\), if \(m\ge2\) |
| Unmatched zero-sum fluctuations | \(A\) | \(s-1\), if \(s\ge2\) |
| Matched-versus-unmatched contrast | \(A-sC/N\) | \(1\), if \(s\ge1\) |

Absent components have multiplicity zero. The largest eigenvalue is always \(A+B-C\), strictly separated from every other existing eigenvalue. Its spectral projector is exactly \(U\). Hence the covariance of the uniform Lipschitz potentials uniquely recovers the entire **labeled deleted matching**: \(U_{ab}=-1/2\) precisely on each missing unordered pair, and the remaining off-diagonal entries of \(U\) vanish. Its rank recovers \(m\). In particular, this reconstruction does not require access to the original graph or its individual distances after the covariance has been computed in the canonical labeled Euclidean coordinates.

## Assumptions and scope

All spaces are real. Each existing graph edge has length one; omitted pairs have shortest-path distance two. As \(N\ge3\), the graph is connected. The unit Lipschitz ball is the set of potential functions satisfying \(|x_i-x_j|\le1\) on all existing edges, taken modulo additive constants. A fixed-vertex anchoring and the centered realization yield equivalent uniform probability measures, because they are related by an invertible linear map with constant Jacobian. The covariance formula and graph recovery use the canonical Euclidean scalar product and **given vertex labels** on \(H\), not an arbitrary unknown linear coordinate change.

The anchored-coordinate volume, which is supporting rather than separately claimed new, is \(T/(N-1)=N+2m/(N-1)\). No claim is made for unrelated metrics or for nonmatching deleted edge sets.

## Proof

**1. Exact dissection.** Fix an anchor vertex and first consider the ordinary equilateral stratum \(\max_i x_i-\min_i x_i\le1\). Almost everywhere there is a unique index attaining the minimum. Translating that minimum to zero yields, in each minimum-index chart, \(N-1\) unrestricted independent coordinates in \([0,1]\), and the transformation between that chart and anchored coordinates has absolute determinant one. Thus the stratum has volume \(N\). In its uniform distribution, the minimizer is uniform in \(\{1,\ldots,N\}\), and conditional on it the other coordinates are independent uniform \([0,1]\).

If the range \(r>1\), then its maximizing and minimizing vertices must form a deleted edge: every other pair is constrained to differ by at most one. Conversely, for any ordered orientation of any one of the \(m\) omitted pairs, fix minimum zero, maximum \(r=2-L\), and choose all other \(N-2\) coordinates freely in \([r-1,1]=[1-L,1]\), with \(0<L<1\). Every graph-edge constraint is then satisfied (the remaining coordinates themselves have spread \(L<1\)). The anchored-coordinate Jacobian is one. Its elementary volume density is \(L^{N-2}\,dL\). All \(2m\) oriented charts are disjoint except on boundaries and contribute \(2m/(N-1)\) in total. Therefore the exceptional stratum has probability \(2m/T\). Conditionally on this stratum, the oriented deleted edge is uniform, \(L\) has density \((N-1)L^{N-2}\) on \((0,1)\), and the other vertices are independent uniform on \([1-L,1]\).

**2. Second moments.** Symmetry under \(x\mapsto-x\) makes \(\mathbb E Z=0\). In the equilateral stratum, each coordinate contrast \(e_i-e_j\) has squared expected difference
\[
\frac2N\frac13+\frac{N-2}{N}\frac16=\frac{N+2}{6N},
\]
so permutation symmetry gives its centered covariance \(\lambda_0P\), where \(\lambda_0=(N+2)/(12N)\).

On the exceptional stratum, conditional on oriented pair \((a,b)\) and \(L\), put \(r=2-L\). Up to a common additive constant, the coordinate vector is the signed displacement \(\frac r2(e_a-e_b)\) plus independent mean-zero uniform errors \(\xi_j\) of variance \(L^2/12\) at the remaining vertices. Projection by \(P\), averaging over pair orientations and the \(m\) pairs, and using the orthogonal projector \(U\) give the conditional covariance
\[
\operatorname{Cov}(Z\mid\mathrm{exception})
=\frac{\mathbb E r^2}{2m}U
 +\frac{\mathbb E L^2}{12}\left(P-\frac1mPEP\right).
\]
Elementary beta integration yields
\[
\mathbb E L^2=\frac{N-1}{N+1},\qquad
\mathbb E(2-L)^2=\frac{N^2+3N+4}{N(N+1)}.
\]
Mixing this covariance with \(\lambda_0P\), using probabilities \(2m/T\) and \(1-2m/T\), gives exactly \(AP+BU-CPEP\) with the displayed coefficients. Every formula is exact for all allowed \(N,m\).

**3. Spectrum.** Orthogonally decompose \(H\) into antisymmetric contrasts on each deleted pair (dimension \(m\)), zero-sum fluctuations of the pair means (dimension \(m-1\)), zero-sum fluctuations on unmatched vertices (dimension \(s-1\)), and, when \(s>0\), one matched-versus-unmatched contrast. The first space is the range of \(U\). The operator \(PEP\) has eigenvalues \(1,1,0,s/N\), respectively, on these components. The four displayed covariance eigenvalues follow directly. Moreover,
\[
\frac BC=\frac{6(N^2+3N+4)}{N(N-1)}>1,
\]
so \(A+B-C>A\), while every other existing eigenvalue is at most \(A\). Thus the maximal spectral projector is precisely \(U\). Its off-diagonal entries equal \(-1/2\) on the deleted matched pairs and vanish on all other pairs. This proves exact recovery, including the boundary cases \(m=1\), \(s=0\), or \(s=1\). \(\square\)

## Verification

The accompanying standalone script `check_matching_cov.py` uses exact integer lattice sums in dilates of the anchored integral Lipschitz polytope, **not** the range-stratum probability argument. It obtains leading volume and quadratic-moment coefficients by finite differences of the weighted Ehrhart polynomials and checks the predicted eigenvalues as rational numbers. It passed every configuration \(3\le N\le6\), \(1\le m\le\lfloor N/2\rfloor\): eight configurations in total, including each type of degenerate invariant component. It also checks the anchored volume as a diagnostic. The independent arithmetic calculations are finite consistency checks; the preceding dissection and linear-algebra argument prove the all-dimensional statement.

To reproduce, use `python check_matching_cov.py` with Python's standard library. The file is included with this finding, not referenced from another record.

## Relationship to prior work

Aliaga [1] places the real Lipschitz dual and its finite-metric predual in the functional-analytic setting, and proves extremal-molecule characterizations, not uniform-interior covariance or metric reconstruction from covariance. D'Alì, Delucchi and Michałek [2] identify the dual Lipschitz polytope in the symmetric-edge-polytope program, studying faces, Ehrhart theory and normalized volumes rather than the centered second-moment operator. Alexander, Fradelizi, García-Lirola and Zvavitch [3] examine finite-metric volume products and equilateral examples; their geometric/volume results do not state the present covariance recovery theorem. Previously recorded results on the same broad metric families give their volumes, graph-polytope facets or Hilbert distortion; the \(K_{2,2}\) covariance is also known as an instance of the complete-bipartite calculation, and is included here only as a boundary case of the natural all-parameter statement. None of those facts is claimed separately new.

The distinct claim is the exact \(N,m\)-dependent covariance **and recovery of the missing labeled matching from its leading eigenspace**. Closest scholarly and research-database searches did not locate a stronger theorem that implies this result; undiscovered equivalent presentations remain possible.

## Limitations

The theorem requires deletion of pairwise vertex-disjoint edges and the counting-coordinate inner product on the labeled zero-sum potential space. Recovery from an unlabeled spectrum alone is not claimed. The result has a complete analytic proof and small-dimensional exact-arithmetic corroboration; it has not undergone independent scientific audit. Literature searches do not establish definitive uniqueness of the result across all publications.

## References

[1] Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first submitted February 1, 2021; primary MSC 46B20), https://arxiv.org/abs/2102.01219 .

[2] Alessio D'Alì, Emanuele Delucchi and Mateusz Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, https://arxiv.org/abs/1910.05193 .

[3] Mark Alexander, Matthieu Fradelizi, Luis C. García-Lirola and Artem Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, https://arxiv.org/abs/1911.10642 .
