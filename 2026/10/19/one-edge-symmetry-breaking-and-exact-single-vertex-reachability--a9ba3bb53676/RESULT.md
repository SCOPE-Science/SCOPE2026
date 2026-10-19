# One-edge symmetry breaking and exact single-vertex reachability ranks on Boolean cubes

## Finding

Let \(d\ge2\), let \(Q_d\) be the graph with vertices \(\{0,1\}^d\) and edges joining Hamming-distance-one vertices, and give every edge conductance one except the edge between \((0,0^m)\) and \((1,0^m)\), which has conductance \(c>0\); here \(m=d-1\). Write \(L_d(c)\) for its positive combinatorial weighted Laplacian. For a vertex \(u\), define its one-input reachable dimension by
\[
R_d(c;u)=\operatorname{rank}[e_u,L_d(c)e_u,\ldots,L_d(c)^{2^d-1}e_u].
\]
The sign in the dynamics \(\dot z=-L_d(c)z+e_u v\) does not change this rank.

**Theorem.** Write \(u=(t,x)\) with \(t\in\{0,1\}\), \(x\in\{0,1\}^m\), and \(j=|x|\). If \(c=1\), then \(R_d(1;u)=d+1\) for every vertex. If \(c\ne1\), form the real symmetric tridiagonal matrix of size \(m+1\)
\[
J_m(c)_{rr}=\begin{cases}m+2c,&r=0,\\m+2,&1\le r\le m,\end{cases}\qquad
J_m(c)_{r,r+1}=J_m(c)_{r+1,r}=-\sqrt{(r+1)(m-r)}.
\]
For \(1\le j\le m-1\) let \(G_{m,j}(c)=J_m(c)[0:j,0:j]\) and \(F_{m,j}=J_m(c)[j+1:m+1,j+1:m+1]\), using half-open index ranges. Put
\[
\nu_{m,j}(c)=\deg\gcd_{\mathbb R[z]}\bigl(\det(zI-G_{m,j}(c)),\det(zI-F_{m,j})\bigr).
\]
For the endpoint shells \(j\in\{0,m\}\), define \(\nu_{m,j}(c)=0\). Then, for every \(c>0\) with \(c\ne1\),
\[
\boxed{R_d(c;u)=2d-\nu_{m,j}(c).}
\]
Thus \(2d\) is a universal one-vertex reachable-dimension ceiling, attained at both endpoints of the exceptional edge and at both vertices with \(x=1^m\), for **every** nonunit positive defect conductance. For each fixed interior shell \(j\), all positive conductances outside \(c=1\) and at most \(m-j\) further exceptional values have \(\nu_{m,j}(c)=0\). Consequently every vertex generically has reachable dimension exactly \(2d\), while the ambient system has dimension \(2^d\). In particular a single edge modification changes the rank seen from its endpoints from \(d+1\) to \(2d\), but does not provide full single-input controllability when \(d\ge3\).

Exceptional nonunit parameters first occur in dimension four. At \(d=4\), take \(|x|=1\). The two distinct positive values
\[
\boxed{c=1-\frac{\sqrt3}{2}\quad\text{and}\quad c=1+\frac{\sqrt3}{2}}
\]
each yield rank seven rather than the generic rank eight. All vertices of \(Q_2\) and \(Q_3\) have the full rank \(2d\) for every positive nonunit \(c\).

## Assumptions and scope

All statements quantify over integers \(d\ge2\), real conductances \(c>0\), and every vertex \(u\). Edge weights refer to an undirected combinatorial Laplacian, with no normalized-degree convention. The control input is the canonical basis vector at a single vertex, with no distributed input. The graph is the exact \(d\)-cube with precisely one exceptional edge. The rank concerns the controllable **subspace dimension**, not the minimum number of simultaneous actuators for full controllability, and is invariant under replacing \(L\) by \(-L\). The parameter \(c=1\) is explicitly separate and is not obtained by substituting into the nonunit formula.

## Proof

**1. Separate the defect direction.** Identify \(\mathbb R^{2^d}=\mathbb R^{2^m}\otimes\mathbb R^2\), with the last factor indexing the distinguished bit. In the orthonormal basis \(f_+=(1,1)/\sqrt2\), \(f_-=(1,-1)/\sqrt2\), the Laplacian is the direct sum
\[
L_d(c)\simeq L(Q_m)\ \oplus\ H_m(c),\qquad
H_m(c)=L(Q_m)+2I+2(c-1)e_0e_0^{\mathsf T},
\]
where \(e_0\) denotes the all-zero vertex of \(Q_m\). The vector \(e_{(t,x)}\) has nonzero components proportional to \(e_x\) in both summands; the sign in the second summand does not affect spectral support.

**2. The spectral-support rank principle.** For any real symmetric matrix \(A\), the rank of \([v,Av,\ldots,A^{N-1}v]\) equals the number of its **distinct** eigenvalues whose orthogonal spectral projector does not annihilate \(v\). This follows by expanding the powers in the orthogonal eigenspaces and using Vandermonde independence of distinct eigenvalues. For \(L(Q_m)\), normalized Walsh characters indexed by \(S\subseteq[m]\) have eigenvalues \(2|S|\). At every vertex \(x\), the projection onto the \(2k\)-eigenspace has squared norm \(\binom{m}{k}/2^m>0\); hence the first summand always contributes exactly the \(m+1\) spectral values \(0,2,\ldots,2m\).

**3. The radial and nonradial defect spectra.** Let \(f_r\) be the normalized indicator of the vertices \(x\in Q_m\) with Hamming weight \(r\), for \(r=0,\ldots,m\). Their span \(\mathcal R\) is invariant under \(L(Q_m)\) and \(e_0e_0^{\mathsf T}\), and the restriction of \(H_m(c)\) to it is exactly \(J_m(c)\) above. The matrix is an irreducible real symmetric Jacobi matrix, so its \(m+1\) eigenvalues are all simple and all its eigenvectors have nonzero first and last coordinates. The orthogonal complement \(\mathcal R^\perp\) is invariant, and its eigenvalues are \(2(k+1)\) with multiplicity \(\binom{m}{k}-1\), for \(1\le k\le m-1\). Indeed the rank-one change annihilates this complement and in each Walsh \(2k\)-eigenspace exactly one dimension has nonzero overlap with \(e_0\). Every one of these nonradial shifted eigenvalues already belongs to the list \(0,2,\ldots,2m\) from step 2.

For \(c\ne1\), the eigenvalues of \(J_m(c)\) lie outside this list. To see this, the unperturbed radial \(J_m(1)\) has simple eigenvalues \(2,4,\ldots,2(m+1)\), and its endpoint \(f_0\) overlaps every eigenvector. The matrix determinant lemma, evaluated polynomially at each of these levels, shows \(\det(zI-J_m(c))\ne0\) at every such \(z\) when \(c-1\ne0\): the coefficient of \(2(c-1)\) is the nonzero endpoint cofactor. Also \(H_m(c)>0\) since \(L(Q_m)\succeq0\) and \(2I+2(c-1)e_0e_0^{\mathsf T}\) is positive definite for \(c>0\); thus no eigenvalue is zero. The radial defect eigenvalues therefore contribute spectral values disjoint from both the first summand and the nonradial shifted spectrum.

**4. Exactly which radial modes are seen at a vertex.** Every radial eigenvector is constant on each Hamming-weight shell. Its overlap with \(e_x\), for \(|x|=j\), vanishes precisely when its \(j\)-th Jacobi coordinate is zero. When \(j=0\) or \(j=m\), irreducibility of \(J_m(c)\) forbids a zero, and all \(m+1\) radial values contribute. If \(1\le j\le m-1\), a Jacobi eigenvector with coordinate \(j\) zero restricts to nonzero eigenvectors on **both** adjacent left and right principal blocks of \(J_m(c)\), with the same eigenvalue. Conversely, eigenvectors of the two blocks for a common eigenvalue can be rescaled so their two nearest-neighbor terms cancel in Jacobi row \(j\); their concatenation with a zero \(j\)-coordinate is an eigenvector of the full matrix. Nonvanishing of the boundary coordinates of block eigenvectors guarantees this construction. Since each block has simple spectrum, the number of lost radial eigenvalues is exactly \(\nu_{m,j}(c)\), the degree of the greatest common divisor of their two characteristic polynomials. Adding the \(m+1\) always-visible first-summand levels gives \(m+1+(m+1-\nu)=2d-\nu\).

**5. Exceptional sets are finite.** For a fixed interior \(j\), the right block \(F_{m,j}\) has exactly \(m-j\) distinct, \(c\)-independent eigenvalues. For any fixed candidate \(\lambda\) from this set, \(\det(\lambda I-G_{m,j}(c))\) is affine in \(c\). It cannot be identically zero: its coefficient and constant term cannot both vanish, by strict interlacing of the two consecutive endpoint principal minors of an irreducible Jacobi matrix. Thus each right-block eigenvalue accounts for at most one exceptional conductance. The number of positive exceptional nonunit conductances is at most \(m-j\). When \(c=1\), the two summands have overlapping spectra \(0,2,\ldots,2m\) and \(2,4,\ldots,2m+2\), and their union has \(m+2=d+1\) values. Every value is seen from each vertex, so this is the uniform-case rank.

**6. The first exceptional example.** For \(d=3\), the only interior index is \(m=2,j=1\). The right block has eigenvalue \(4\), and the left block has eigenvalue \(2+2c\), so their only collision is \(c=1\). For \(d=4\), \(m=3,j=1\), the right block is the symmetric \(2\times2\) matrix with diagonal \(5\) and off-diagonal \(-\sqrt3\); its eigenvalues are \(5\pm\sqrt3\). The left block has eigenvalue \(3+2c\), so the two positive nonunit collisions occur at the displayed values. They are mutually exclusive; hence \(\nu=1\), giving rank seven. There are no interior indices for \(d=2\).

## Verification

The accompanying standard-library script `verify_one_defect_cube.py` reconstructs the full weighted cube Laplacian, computes its Krylov rank over two finite fields for every shell representative and both endpoints of the distinguished bit, for \(2\le d\le6\) and six exact rational conductances, and independently predicts the answer using exact principal-block characteristic-polynomial gcds. It also verifies exact \(\mathbb Q(\sqrt3)\) Jacobi eigenvector identities for the exceptional four-cube cases. Run `python3 verify_one_defect_cube.py`; the actual completed run printed `VERIFY_OK 489 exact arithmetic checks`. Modular checks are corroborative for the tested instances only; the arbitrary-dimensional and arbitrary-real-conductance statements are established by the preceding proof.

## Relationship to prior work

Notarstefano and Parlangeli (first public arXiv posting 2012-03-01) study controllability and observability through reductions and symmetries of Cartesian-product grids; their constructions concern unperturbed grid Laplacians. Yuan et al. (2013) relate control requirements on undirected weighted networks to eigenspace multiplicity through the PBH framework. Chapman, Nabi-Abdolyousefi and Mesbahi (2014) establish control criteria for genuine Cartesian-product networks. Zhang, Cao and Camlibel (2014) give topological upper and lower bounds for controllable-subspace dimension via equitable and distance partitions, not the full conductance-dependent equality or resonances. Those frameworks motivate but do not give the exact cyclic support of a hypercube **after one edge ceases to have the Cartesian-product conductance**. Here the new assertion is the all-vertex, all-positive-conductance reachable-rank formula, including the sharp \(2d\) ceiling and Jacobi-minor exceptional values, rather than the general PBH criterion or the elementary Walsh spectrum. The rank-one perturbation technique is standard background, not claimed as new.

## Limitations

The theorem is restricted to one defective edge on a Boolean hypercube, a canonical single-vertex actuator, undirected positive conductances, and exact linear dynamics. It does not assert full controllability in dimensions \(d\ge3\), multi-input optimality, control energy, or robustness of numerical rank under floating-point error. Some special positive nonunit edge weights can lower the rank from its generic value at interior shells. The comparison with broader indexed or unindexed single-defect graph-controllability literature may be incomplete, and the result has not undergone independent mathematical audit.

## References

1. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129v1 (first submitted 2012-03-01), later IEEE Transactions on Automatic Control 58 (2013), 1719–1731. https://arxiv.org/abs/1203.0129
2. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications 4 (2013), 2447. https://doi.org/10.1038/ncomms3447
3. A. Chapman, M. Nabi-Abdolyousefi and M. Mesbahi, *Controllability and observability of network-of-networks via Cartesian products*, IEEE Transactions on Automatic Control 59 (2014), 2668–2679. https://doi.org/10.1109/TAC.2014.2328757
4. S. Zhang, M. Cao and M. K. Camlibel, *Upper and lower bounds for controllable subspaces of networks of diffusively coupled agents*, IEEE Transactions on Automatic Control 59 (2014), 745–750. https://doi.org/10.1109/TAC.2013.2275666
5. A. C. M. Ran and M. Wojtylak, *Eigenvalues of rank one perturbations of unstructured matrices*, Linear Algebra and its Applications 437 (2012), 589–600. https://doi.org/10.1016/j.laa.2012.02.027
