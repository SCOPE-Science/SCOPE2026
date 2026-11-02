# Sharp terminal-leaf controllability of perfect binary trees with four-level resonances

## Finding

For every integer \(h\ge1\), let \(T_h\) denote the perfect rooted binary tree having \(2^d\) vertices at each depth \(d\in\{0,1,\ldots,h\}\). Every edge has conductance one. Let \(L_h\) be its combinatorial Laplacian. If independent controls are installed at a subset \(S\) of the \(2^h\) terminal leaves, write \(B_S=[e_s]_{s\in S}\). The exact minimum size of \(S\) for controllability of \(\dot z=-L_hz+B_Su\) is

\[
M_h=\sum_{j=0}^{\lfloor(h-1)/4\rfloor}2^{h-1-4j}+\mathbf1_{\{h\equiv3\pmod4\}}.
\]

In particular \(M_1,M_2,M_3,M_4,M_5,M_6=(1,2,5,8,17,34)\). These are **leaf-only**, independent coordinate actuators; no interior vertex or grouped input is used. The minimum has the sharp limits \(M_h/2^h\to8/15\) and \(M_h/(2^{h+1}-1)\to4/15\). The additional actuator demand beyond the mandatory bottom sibling-pair selection has a four-level recurrence.

## Assumptions and scope

The graph is finite and undirected; its root has degree two, nonroot nonleaf vertices have degree three, leaves have degree one, and edges all have weight one. The height \(h\) is any integer at least one. Each selected leaf receives its own freely varying scalar control. Controllability is exact Kalman controllability over \(\mathbb R\), equivalent for symmetric \(L_h\) to the absence of an eigenvector of \(L_h\) vanishing on every selected leaf. This is a fixed graph problem, not structural controllability under varying edge weights.

## Proof

**1. The full spectrum decomposes into radial Jacobi blocks.** At every internal vertex at depth \(d\), anti-symmetrize radially across its two child subtrees. The associated invariant subspace has dimension \(k=h-d\). In an orthonormal depth basis its Laplacian restriction is the Jacobi matrix with diagonal \((3,3,\ldots,3,1)\) (one entry \(1\) if \(k=1\)) and consecutive off-diagonal entries \(-\sqrt2\). There are \(2^d\) independent copies for each \(d\in\{0,\ldots,h-1\}\). The remaining fully radial root block has size \(h+1\), diagonal \((2,3,\ldots,3,1)\), and the same off-diagonals. These orthogonal invariant subspaces exhaust the vertex space because

\[
(h+1)+\sum_{d=0}^{h-1}2^d(h-d)=2^{h+1}-1.
\]

Define the characteristic polynomials with the leaf end eliminated first:

\[
P_0(\lambda)=1,\quad P_1(\lambda)=\lambda-1,\quad P_k(\lambda)=(\lambda-3)P_{k-1}(\lambda)-2P_{k-2}(\lambda)\ (k\ge2).
\]

The root radial block has polynomial

\[
Q_{h+1}(\lambda)=(\lambda-2)P_h(\lambda)-2P_{h-1}(\lambda).
\]

Thus, up to an irrelevant overall leading sign, the Laplacian characteristic polynomial factors into \(Q_{h+1}\) and, for each \(d\), the factor \(P_{h-d}\) of multiplicity \(2^d\). All eigenvalues within each Jacobi block are simple, as its subdiagonal entries are nonzero.

**2. The exact unit-eigenvalue multiplicity.** At \(\lambda=1\), the recurrence reads \(P_k(1)=-2P_{k-1}(1)-2P_{k-2}(1)\), with \(P_0(1)=1\) and \(P_1(1)=0\). Its next values are \(-2,4,-4,0,8,-16,16,0,\ldots\). The characteristic roots are \(-1\pm i\), so \(P_k(1)=0\) precisely if \(k\equiv1\pmod4\); these roots are simple. Moreover

\[
Q_{h+1}(1)=-P_h(1)-2P_{h-1}(1)=0
\quad\Longleftrightarrow\quad h\equiv3\pmod4.
\]

It follows that the eigenspace \(E_h=\ker(L_h-I)\) has dimension exactly \(M_h\), the formula in the Finding. For any input matrix with only \(q\) coordinate columns, the restriction of its transpose to this \(M_h\)-dimensional eigenspace cannot be injective if \(q<M_h\). The PBH criterion therefore proves \(|S|\ge M_h\) for every controllable leaf set.

**3. One leaf per sibling pair detects every non-unit eigenvalue.** Choose an arbitrary leaf from each of the \(m=2^{h-1}\) sibling pairs, obtaining \(S_0\). Suppose \(L_hv=\lambda v\), \(\lambda\ne1\), and \(v\) is zero on \(S_0\). At a selected leaf \(s\) with parent \(p\), the eigenvector equation is \(v_s-v_p=\lambda v_s\); hence \(v_p=0\). At the other leaf of the pair the same equation then forces its coordinate to vanish, because \(1-\lambda\ne0\). The bottom internal parents consequently vanish together with every leaf. The eigenvector equations at those internal parents force their own parents to vanish; induction toward the root gives \(v=0\). Thus \(S_0\) already observes all eigenspaces other than \(E_h\), without any assumption of simple or disjoint other eigenvalues.

**4. The unit eigenspace needs exactly the remaining pivots.** At \(\lambda=1\), the leaf equation forces every bottom parent coordinate to be zero. Define the pair-sum map \(\Sigma:E_h\to\mathbb R^m\) by \((\Sigma v)_p=v_{p,L}+v_{p,R}\), where \(p\) ranges over bottom parents. Its kernel consists exactly of the \(m\) independent within-pair antisymmetric leaf differences: certainly those vectors are unit eigenvectors; conversely, if every pair sum vanishes, the equation at each zero bottom parent forces its own parent to be zero, and the same induction propagates zero to all interior coordinates. Therefore

\[
\dim\Sigma(E_h)=\dim E_h-m=M_h-2^{h-1}.
\]

Choose a set \(J\) of precisely \(M_h-m\) sibling pairs such that the coordinate restriction \(\Sigma(E_h)\to\mathbb R^J\) is injective. Such a set exists by row-pivot selection on any basis matrix for \(\Sigma(E_h)\). In each pair of \(J\), select the **other** leaf as an additional actuator, giving \(S=S_0\cup\{\text{opposite leaf in pair }p:p\in J\}\) and \(|S|=M_h\). If a unit eigenvector vanishes on \(S\), its pair sums vanish on \(J\) and therefore on every pair. It lies in \(\ker\Sigma\), but on each bottom pair it also vanishes at the originally selected leaf, forcing both coordinates to vanish. Hence it is zero. This proves observability of \(E_h\) and, by Step 3, every other eigenspace. The symmetric PBH test gives full controllability. Together with Step 2 this establishes the exact minimum for every \(h\ge1\).

**5. Density limit.** Geometric summation gives \(M_h=2^{h-1}(1+1/16+1/16^2+\cdots)\) with an exponentially small truncation error and a bounded optional extra term, hence \(M_h/2^h\to8/15\). Dividing by the total vertex count gives the second limit.

## Verification

The standalone standard-library program `verify_binary_tree.py` builds the exact integer Laplacian, computes its \(\lambda=1\) nullspace and greedy leaf pivots over the prime fields of orders \(1000003\) and \(1000033\), and directly checks full finite-field Kalman ranks at every height \(1\le h\le6\). It also checks that one leaf per pair is insufficient at height three. Both prime runs report `ALL_FINITE_CHECKS_PASSED`, with the predicted minima \(1,2,5,8,17,34\). These finite checks support implementation and arithmetic but do not replace the all-height proof above.

Run: `python3 verify_binary_tree.py`.

## Relationship to prior work

He, Liu and Strang (2000) analyze spectra and eigenvectors of growing regular trees and explicitly identify the recurrent unit eigenvalue and limiting spectral mass for a degree-three-root tree. This anticipates the spectral resonance and is not claimed as new. Their tree has a three-child root, whereas \(T_h\) has a two-child root; their result does not select the minimum number of terminal-only independent control coordinates or prove the pivot construction. Parlangeli and Notarstefano (2011) formulate the same symmetric PBH notion for paths and cycles, not this binary-tree family. Ji, Lin, Lee and collaborators (2010) give general tree controllability tests without the present all-height minimum terminal selection formula.

A particularly close source is Dai (first publicly posted 2021): its Cayley-tree example also solves minimum-leader selection but uses the three-branch-root family of order \(3\cdot2^g-2\), in contrast to the two-branch-root family of order \(2^{h+1}-1\) here. Its general critical-set criteria can help analyze trees but do not directly state or imply without further nontrivial spectral and rank arguments the exact terminal-only four-level formula proved here. Mousavi, Haeri and Mesbahi (2018) treat cographs and sibling partitions; perfect binary trees of height at least two are not cographs because they contain induced four-vertex paths. The main assessed contribution is the **sharp terminal-input minimum and its construction**, not the general PBH criterion or the earlier spectral recurrence.

## Limitations

All edges must have identical unit weight; different weights can split the unit eigenvalue and change the minimum. The selected sites are restricted to leaves, and each has an independent input; a single input driving several leaves is not covered. This proves no result about robust structural controllability or arbitrary non-perfect trees. The exact pivot selection is an algebraic existence-and-construction procedure, not an explicit closed-form address for every extra leaf. Specialist literature on other rooted-tree conventions could contain related formulations; no independent mathematical audit has been performed.

## References

1. X. He, Y. Liu and G. Strang, *Laplacian Eigenvalues of Growing Trees*, manuscript dated April 3, 2000, Sections 3–4. https://math.mit.edu/~gs/papers/mp2.pdf
2. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, September 16, 2011. https://arxiv.org/abs/1109.3556
3. Z. Ji, H. Lin, T. H. Lee et al., *Multi-agent controllability with tree topology*, American Control Conference (2010). https://www3.nd.edu/~hlin1/Papers/2010/ACC10_MAS.pdf
4. L. Dai, *Minimum leader selection for structural controllability of undirected graphs with leader-follower framework*, arXiv:2112.01169v1, December 2, 2021; later IET Control Theory & Applications. https://arxiv.org/abs/2112.01169
5. S. Mousavi, M. Haeri and M. Mesbahi, *Laplacian Dynamics on Cographs: Controllability Analysis through Joins and Unions*, arXiv:1802.03599v2, 2018. https://arxiv.org/abs/1802.03599
