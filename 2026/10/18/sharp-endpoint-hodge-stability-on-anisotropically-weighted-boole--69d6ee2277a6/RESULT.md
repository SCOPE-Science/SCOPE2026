# Sharp endpoint Hodge stability on anisotropically weighted Boolean cubes

## Finding

Let \(d\ge2\). On the graph with vertex set \(V=\{0,1\}^d\), each edge in coordinate direction \(i\) has conductance \(c_i>0\), constant across all edges in that direction. Each undirected edge has the fixed orientation from bit \(0\) to bit \(1\). Write \(B\) for the edge-by-vertex signed incidence matrix with \((Bf)(i,x)=f(x+e_i)-f(x)\) for \(x_i=0\), and \(D\) for the diagonal matrix of edge conductances. On Euclidean energy-normalized edge data consider the orthogonal projector
\[
P=D^{1/2}B(B^{\mathsf T}DB)^+B^{\mathsf T}D^{1/2},
\]
where \((\cdot)^+\) denotes the Moore--Penrose inverse. Its **sharp maximum-norm amplification** is
\[
\boxed{\|P\|_{\ell^\infty(E)\to\ell^\infty(E)}
=1+\max_{1\le i\le d}\sum_{j\ne i}\frac{\sqrt{c_ic_j}}{c_i+c_j}.}
\tag{1}
\]

Indeed, **every row** with output edge in direction \(i\) has absolute row mass exactly \(1\) on the input edges of direction \(i\), and \(\sqrt{c_ic_j}/(c_i+c_j)\) on edges of each distinct direction \(j\). Entries within one direction are strictly positive. For two different directions \(i\) and \(j\), if the output edge has tail \(z_i=0\) and the input edge has tail \(x_j=0\), the matrix entry has sign \((-1)^{z_j+x_i}\). All entries are nonzero, so these signs specify explicit extremizing bounded input patterns.

For every \(c_i>0\),
\[
1<\|P\|_{\infty\to\infty}\le\frac{d+1}{2}.
\]
Equality at the upper bound holds **if and only if** \(c_1=\cdots=c_d\). The complete range of values over positive conductance vectors, with dimension fixed, is
\[
\boxed{\{\|P_c\|_{\infty\to\infty}:c_i>0\}=(1,(d+1)/2].}
\tag{2}
\]
The infimum \(1\) is not attained. For example, the family \(c_i=R^{2(i-1)}\), \(R\ge1\), traverses the full interval from its upper endpoint toward the lower endpoint as \(R\to\infty\).

## Assumptions and scope

The hypercube has all \(2^d\) vertices and \(d2^{d-1}\) edges. Conductances need only be positive, not integral or comparable, but are assumed constant on each coordinate direction. The operator is the **orthogonal projection on the edge Hilbert space** \(\ell^2(E)\), in conductance-normalized coordinates \(D^{1/2}Bf\); only its induced coordinatewise \(\ell^\infty\) norm is being measured. Without energy normalization the non-Hilbert endpoint norm is a different quantity. The formula does not assert sharp norms for general weighted graphs or edgewise-varying conductances. All assertions hold for real and complex edge inputs, since \(P\) has real coefficients and the maximum absolute row sum characterizes both norms.

## Proof

**1. Walsh diagonalization.** For \(S\subseteq[d]\), set \(\chi_S(v)=(-1)^{\sum_{k\in S}v_k}\). The weighted graph Laplacian \(L=B^{\mathsf T}DB\) satisfies
\[
L\chi_S=2\Big(\sum_{k\in S}c_k\Big)\chi_S.
\]
On an edge \((i,x)\) with \(x_i=0\),
\[
(D^{1/2}B\chi_S)(i,x)=-2\sqrt{c_i}\,\chi_S(x)\,\mathbf 1_{i\in S}.
\]
The \(2^d\) Walsh characters are orthogonal and have squared norm \(2^d\). Therefore, for output edge \((i,z)\) and input edge \((j,x)\),
\[
P_{(i,z),(j,x)}=2^{1-d}\sqrt{c_ic_j}
\sum_{S\supseteq\{i,j\}}
\frac{\chi_S(z)\chi_S(x)}{\sum_{k\in S}c_k}.
\tag{3}
\]
The set \(\{i,j\}\) contains just one element when \(i=j\). The empty character does not contribute.

**2. Integral representation and sign rigidity.** Insert the elementary identity \(1/a=\int_0^\infty e^{-at}\,dt\), valid because every denominator in (3) is positive, and sum over the free Walsh coordinates. If \(i=j\), then \(x_i=z_i=0\) and
\[
P_{(i,z),(i,x)}=2^{1-d}c_i\int_0^\infty e^{-tc_i}
\prod_{k\ne i}\bigl(1+(-1)^{z_k+x_k}e^{-tc_k}\bigr)\,dt.
\tag{4}
\]
Every factor is positive when \(t>0\), so every entry in (4) is strictly positive. If \(i\ne j\), then \(z_i=x_j=0\) and
\[
P_{(i,z),(j,x)}=2^{1-d}\sqrt{c_ic_j}\,(-1)^{z_j+x_i}
\int_0^\infty e^{-t(c_i+c_j)}
\prod_{k\notin\{i,j\}}\bigl(1+(-1)^{z_k+x_k}e^{-tc_k}\bigr)\,dt.
\tag{5}
\]
Again the integral is strictly positive, proving the asserted two-bit signs and nonvanishing.

**3. Absolute row masses.** Fix the output edge \((i,z)\). Summing (4) over all \(2^{d-1}\) tails \(x\) with \(x_i=0\) replaces each free factor by \(2\), hence
\[
\sum_{x:x_i=0}|P_{(i,z),(i,x)}|
=c_i\int_0^\infty e^{-tc_i}\,dt=1.
\]
For any \(j\ne i\), summing the absolute value of (5) over all tails \(x\) with \(x_j=0\) removes the parity prefactor and produces the factor \(2^{d-1}\) (one sum over \(x_i\), and \(d-2\) product-factor sums). Consequently
\[
\sum_{x:x_j=0}|P_{(i,z),(j,x)}|
=\sqrt{c_ic_j}\int_0^\infty e^{-t(c_i+c_j)}\,dt
=\frac{\sqrt{c_ic_j}}{c_i+c_j}.
\]
This proves the row-mass assertion exactly, including all dimensions and positive weights. The induced \(\ell^\infty\) norm of a finite matrix is its largest absolute row sum; choosing the signs of input edge data to match a maximizing row gives equality, proving (1).

**4. Sharp universal range.** By the arithmetic--geometric mean inequality, \(\sqrt{c_ic_j}/(c_i+c_j)\le 1/2\), with equality precisely when \(c_i=c_j\). As \(d\ge2\), every row mass is greater than \(1\), while its upper bound is \(1+(d-1)/2\). If one row reaches this upper bound, its conductance agrees with those of every other direction, so **all** weights are equal. Conversely, equal conductances attain the bound.

For \(c_i(R)=R^{2(i-1)}\), \(R\ge1\), the pairwise summand is \(R^{|i-j|}/(1+R^{2|i-j|})\), strictly decreasing for \(R>1\) and tending to zero as \(R\to\infty\). For each \(i\), the sum decreases strictly; the maximum of finitely many such sums is continuous and strictly decreasing. At \(R=1\), its value is \((d-1)/2\); at infinity it is zero. Thus this family realizes exactly every norm in (2), and the infimum cannot be attained by positive weights.

## Verification

The accompanying pure-Python `verify.py` reconstructs weighted Laplacians and their edge projectors **without using the Walsh formula**, by inverting a grounded vertex Laplacian in exact rational arithmetic. Integer square-root conductances make every test entry rational. It checks all directionwise absolute row sums, every entry sign, matrix symmetry and idempotence, in dimensions \(1\) through \(5\) and twelve conductance patterns (including strongly anisotropic ones). Recorded output: **31,006 exact-rational assertions passed**. This is finite corroboration of (3)--(5), not an exhaustive or infinite proof; the general theorem is justified by the analytical steps above. The dimension-one checks test the boundary case only; the main range statement is for \(d\ge2\).

## Relationship to prior work

Graph Hodge least-squares decompositions and their use for rankings are established in Jiang--Lim--Yao--Ye [1]. Transfer-current orthogonal projection representations \(dGd^*\) and weighted electrical networks are classical and appear in Kassel--Wu [2]. Bernardi [3] studies spanning trees and the effect of direction-dependent edge weights on hypercubes. These works supply the underlying decomposition, kernel and product-graph background, but the inspected relevant portions do not state the exact **edgewise absolute row masses**, resulting maximum norm (1), complete anisotropy range (2), or cross-direction sign law.

Related published calculations on Walsh projections in Hamming Lipschitz-free spaces [4] concern **vertex-function spectral projections with a Lipschitz seminorm**, not the \(\ell^2\)-orthogonal Hodge projector on \(\ell^\infty\)-bounded edge vectors. A published cactus transportation-space result [5] concerns **coordinate suppression projections of spanning-tree molecular bases**, not orthogonal gradient projections on a hypercube (which has shared-edge cycles when \(d\ge3\)). The cube-edge fourth-moment result [6] concerns degree-two Rademacher chaos, while a cyclic Riesz-transform result [7] concerns the one-dimensional \(\ell^2\) multiplier \(DL^{-1/2}\), not \(DL^{-1}D^{\mathsf T}\) on cube edge flows. The special case \(d=2\) is a single cycle and is not singled out as independently original; the principal content is the arbitrary anisotropic product family, its pairwise row-mass factorization and global sharp bounds.

## Limitations

The classification assumes conductance homogeneity **within each coordinate direction** and energy-normalized edge data. It does not give the norm of \(D^{-1/2}PD^{1/2}\) or arbitrary perturbations of individual edge conductances. The statement concerns the given orthogonal projector, not the smallest norm among all projections onto the same gradient subspace. The formula is mathematically proved here, but literature priority remains provisional: a semantically equivalent earlier product-graph transfer-current calculation, possibly using an electrical-network or Green-function presentation rather than an explicit norm formula, has not been excluded. No external independent scientific or bibliographic audit has been performed.

## References

1. X. Jiang, L.-H. Lim, Y. Yao and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067v1, first public 2008-11-07, https://arxiv.org/abs/0811.1067.
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946v1, first public 2013-12-10, https://arxiv.org/pdf/1312.2946.
3. O. Bernardi, *On the spanning trees of the hypercube and other products of graphs*, arXiv:1207.0896v1, first public 2012-07-04, https://arxiv.org/pdf/1207.0896.
4. *Coordinate-shadow norm formula for Walsh projections on Hamming Lipschitz-free spaces*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-coordinate-shadow-norm-formula-for-walsh-projections-on-hamming--6d24f15eba8d.
5. *Sharp coordinate-projection norms for edge bases of cactus transportation spaces*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-coordinate-projection-norms-for-edge-bases-of-cactus-trans--b98930fbc1cd.
6. *Sharp fourth moment and Euclidean distortion of the real \(Q_3\) edge Walsh chaos*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-and-euclidean-distortion-of-the-real-q-3-edg--45ae4e57bc26.
7. *Cycle Riesz transforms as parity blocks of doubled cyclic Hilbert transforms*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cycle-riesz-transforms-as-parity-blocks-of-doubled-cyclic-hilber--241f167596e5.
