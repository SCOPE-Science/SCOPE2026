# Bridge-conditioned vertex degrees in two-community random spanning trees

## Finding

**Theorem.** Fix integers \(m,n\ge2\). Partition the vertices of a complete graph into labeled communities \(A\) and \(B\) of sizes \(m\) and \(n\). Give each within-community edge conductance \(\alpha>0\) and each cross-community edge conductance \(\beta>0\). Sample a spanning tree \(T\) with probability proportional to the product of its edge conductances. Mark any fixed \(v\in A\), set \(D=\deg_T(v)\), and let \(K\) be the total number of cross-community edges of \(T\).

The complete joint weighted generating polynomial is
\[
Z(w,z)=\sum_T \alpha^{m+n-1-K(T)}\beta^{K(T)}w^{D(T)}z^{K(T)}
=\beta zw\,[\alpha(m-1+w)+\beta nz]^{m-1}
[\alpha n+\beta z(m-1+w)]^{n-1}.
\]
In particular, \(\mathbb E[w^Dz^K]=Z(w,z)/Z(1,1)\), with
\[
Z(1,1)=\beta(\alpha m+\beta n)^{m-1}(\alpha n+\beta m)^{n-1}.
\]
Consequently, \(K\) is distributed as one plus a sum of independent binomials:
\[
K\ \overset{\mathrm d}=\ 1+\operatorname{Bin}\!\left(m-1,\frac{\beta n}{\alpha m+\beta n}\right)
+\operatorname{Bin}\!\left(n-1,\frac{\beta m}{\alpha n+\beta m}\right).
\]
Likewise, \(D\) has the distribution of one plus independent binomials with respective parameters \((m-1,\alpha/(\alpha m+\beta n))\) and \((n-1,\beta/(\alpha n+\beta m))\).

More sharply, write \(r_k=\mathbb E[D\mid K=k]\) for every integer \(1\le k\le m+n-1\); all these events have positive probability. The conditional means do not depend on \(\alpha\) or \(\beta\). When \(m=n\), they are all exactly \(2-1/m\). When \(m\ne n\), the sequence \((r_1,\ldots,r_{m+n-1})\) is **neither nondecreasing nor nonincreasing**, for every choice of positive conductances. Explicitly, with
\[
S=\frac{(m-1)n}{m}+\frac{(n-1)m}{n}>0,
\]
one has
\[
r_1=2-\frac1m,\qquad
r_2-r_1=\frac{(m-n)(mn-m-n)}{m^2nS},\qquad
r_{m+n-1}=1+\frac{n-1}{m}.
\]
The initial step and total endpoint displacement therefore have opposite strict signs whenever the sizes differ.

Finally, the unconditional covariance is
\[
\operatorname{Cov}(D,K)=\alpha\beta n\left[
\frac{n-1}{(\alpha n+\beta m)^2}
-\frac{m-1}{(\alpha m+\beta n)^2}\right].
\]
For \(m\ne n\), define the explicit threshold
\[
q_* =\frac{\sqrt{(m-1)(n-1)}-1}{m+n-1+\sqrt{(m-1)(n-1)}}\in(0,1/3).
\]
Writing \(q=\beta/\alpha\), the covariance is negative, zero, or positive according as \((n-m)(q-q_*)\) is negative, zero, or positive. Thus a unique conductance ratio reverses the correlation sign, despite the conductance-independent, nonmonotone conditional regression. When \(m=n\), covariance is zero for every positive ratio, although \(D\) and \(K\) are not independent.

## Assumptions and scope

All graphs here are finite, undirected, complete and vertex-labeled. The sizes satisfy \(m,n\ge2\) and the two conductances are strictly positive. Every spanning tree carries its product-conductance Gibbs weight. The marked vertex is fixed in \(A\); no randomness is introduced in its selection. \(K\) counts edges across the prescribed partition, not edges on a minimum cut of the sampled tree. The conclusions are exact for all specified finite orders and weights.

## Proof

**1. Bivariate tree enumerator.** Introduce formal markers \(w,z\) by multiplying each edge incident to \(v\) by \(w\), and each cross-community edge by \(z\), counting an edge incident to \(v\) and crossing communities with both markers. By the weighted Matrix–Tree Theorem, the resulting enumerator is the determinant of the Laplacian minor obtained by removing \(v\).

Among the remaining vertices, the \(m-1\) vertices of \(A\) have diagonal/off-diagonal block \(U I_{m-1}-\alpha J_{m-1}\), where \(U=\alpha(m-1+w)+\beta nz\). The \(n\) vertices of \(B\) have block \(V I_n-\alpha J_n\), where \(V=\alpha n+\beta z(m-1+w)\). The off-diagonal blocks are \(-\beta z J\). On vectors summing to zero within \(A\setminus\{v\}\), the minor acts by \(U\), with multiplicity \(m-2\); on the zero-sum subspace within \(B\), it acts by \(V\), with multiplicity \(n-1\). On block-constant vectors its matrix is
\[
\begin{pmatrix}
\alpha w+\beta nz&-\beta nz\\
-\beta z(m-1)&\beta z(m-1+w)
\end{pmatrix},
\]
whose determinant simplifies to \(\beta zwU\). Multiplying the factors gives \(Z(w,z)=\beta zwU^{m-1}V^{n-1}\). This computation holds as a polynomial identity, including for marker value zero. Setting either marker to one and normalizing yields both independent-binomial marginals.

**2. Covariance and unique reversal.** The identity
\[
\operatorname{Cov}(D,K)=
\left.(w\partial_w)(z\partial_z)\log Z(w,z)\right|_{w=z=1}
\]
gives the displayed covariance by differentiating the two logarithmic factors. After setting \(q=\beta/\alpha\) and removing strictly positive factors, its sign equals the sign of
\[
(n-1)(m+nq)^2-(m-1)(n+mq)^2
=(n-m)\big[(m^2+mn+n^2-m-n)q^2+2mnq-(mn-m-n)\big].
\]
For unequal \(m,n\ge2\), \(mn-m-n)>0\). The bracketed quadratic is strictly increasing on \(q>0\), starts negative, and tends to infinity. Thus it has exactly one positive zero. Solving the equivalent equation \(\sqrt{n-1}(m+nq)=\sqrt{m-1}(n+mq)\) yields \(q_*\). Its positivity follows from \(\sqrt{(m-1)(n-1)}>1\); its upper bound follows from \(2\sqrt{(m-1)(n-1)}\le m+n-2\). When \(m=n\), the covariance formula vanishes identically.

**3. Conditional regression.** At fixed \(K=k\), every tree has the same conductance weight \(\alpha^{m+n-1-k}\beta^k\), so the conditional law is independent of both parameters. Write \(c_k=[z^k]Z(1,z)\), and let \(H(z)=\left.\partial_w\log Z(w,z)\right|_{w=1}\). Then
\[
H(z)=1+\frac{(m-1)\alpha}{\alpha m+\beta nz}
+\frac{(n-1)\beta z}{\alpha n+\beta mz},
\qquad
r_k=\frac{[z^k]Z(1,z)H(z)}{c_k}.
\]
In particular \(r_1=H(0)=2-1/m\). To find \(r_2\), since the conditional law is weight-independent, take \(\alpha=\beta=1\). We have \(c_2/c_1=S\) and \(H'(0)=(m-n)(mn-m-n)/(m^2n)\). Coefficient division gives the stated \(r_2-r_1=H'(0)/S\).

The maximal possible value \(K=m+n-1\) forces every tree edge to cross the partition. Such trees are the uniform spanning trees of the complete bipartite graph \(K_{m,n}\), whose weighted Matrix–Tree count (or symmetry plus the tree-degree sum in \(A\)) gives \(r_{m+n-1}=1+(n-1)/m\). Thus the endpoint gap is \((n-m)/m\). Since \(mn-m-n=(m-1)(n-1)-1>0\) for \(m\ne n\), the first increment and endpoint gap have opposite signs, proving failure of monotonicity in either direction. When \(m=n\), the community-switching and within-community vertex permutations act transitively on vertices while preserving \(K\); given \(K=k\), every vertex has expected degree \(2(2m-1)/(2m)=2-1/m\). Nevertheless independence of \(D\) and \(K\) fails: if \(D=2m-1\), the tree is a star centered at \(v\), hence \(K=m\), while the full-support marginal of \(K\) is not concentrated at \(m\).

## Verification

The accompanying standard-library Python checker enumerates Prüfer codes independently of the Laplacian formula and verifies their complete joint degree/bridge-count coefficient tables for multiple \((m,n,\alpha,\beta)\) combinations of up to seven vertices. It separately computes exact Laplacian determinants, factorial-moment covariance, both binomial marginals, all conditional endpoint and first-increment formulas, and balanced/unbalanced sign cases. Running `python verify.py` completed with **250 exact assertions passed**. These computations are finite cross-checks; the Matrix–Tree argument above proves the all-size identities.

## Relationship to prior work

Sanmartín, Schnörr and Hamprecht (2024) develop the weighted spanning-tree Gibbs framework and general node-degree moment and covariance methods, including a node-degree polynomial via the Matrix–Tree Theorem; that general machinery is explicitly prior, not claimed as new. Rapoport (2023) develops edge-indicator and joint local-degree laws for uniform spanning trees on general graphs. The contribution asserted here is the explicit *joint* bridge-count/marked-degree factorization for two uniform-conductance communities and the all-size nonmonotone conditional-regression classification combined with a unique cross-conductance covariance reversal. Standard transfer-current formulas or general Laplacian differentiation alone do not state that classification. A broader formula in prior work may imply it after specialization; historical-priority certainty is not asserted.

## Limitations

The findings concern precisely two communities, equal conductance among all edges of each type, and positive weights. No monotonicity or threshold theorem is claimed for heterogeneous within-community weights, arbitrary partitions into three or more communities, or random minimum spanning trees formed from independent random edge costs. The first two conditional means and endpoints prove nonmonotonicity but **do not** classify the number or locations of internal turning points. A general prior theorem could still imply these exact specializations, and no independent mathematical audit has been performed.

## References

1. E. Fita Sanmartín, C. Schnörr and F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472, first posted 2024-09-20. https://arxiv.org/html/2409.13472v2
2. A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992, first posted 2023-12-22. https://arxiv.org/html/2312.14992v1
3. E. Babson and collaborators, *Models of random spanning trees*, arXiv:2407.20226, first posted 2024-07-29. https://arxiv.org/html/2407.20226v2
