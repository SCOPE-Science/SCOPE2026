# The first mixed-degree mod-two closed-neighborhood homology in a categorical complete-graph product family

## Finding

For the finite family \(X_n=\mathcal N[K_3\times K_n]\) with \(2\le n\le6\), where \(\times\) denotes the **categorical** graph product, the full positive-degree reduced homology over \(\mathbf F_2\) has the following ranks:

| \(n\) | Nonzero \(\widetilde\beta_k(X_n;\mathbf F_2)\) |
| --- | --- |
| \(2\) | \(\widetilde\beta_1=1\) |
| \(3\) | \(\widetilde\beta_2=14\) |
| \(4\) | \(\widetilde\beta_3=25\) |
| \(5\) | \(\widetilde\beta_4=44\) |
| \(6\) | \(\widetilde\beta_4=47\), \(\widetilde\beta_5=36\) |

All omitted reduced mod-two Betti numbers vanish. In particular, \(n=6\) is the **first** parameter \(n\ge2\) through which this family is indexed that supports homology in two different positive degrees, and the transition occurs in two adjacent degrees. This is a finite, exact cutoff statement, not an infinite-parameter classification.

## Assumptions and scope

The graph \(G_n\) has vertices \((i,j)\) for \(i\in\{0,1,2\}\) and \(j\in\{0,\ldots,n-1\}\). Its distinct vertices \((i,j)\) and \((a,b)\) are adjacent precisely when \(i\ne a\) **and** \(j\ne b\). The closed ball at \((i,j)\) is
\[
B_{i,j}=\{(i,j)\}\cup\{(a,b):a\ne i,\ b\ne j\}.
\]
The complex \(X_n\) contains exactly those nonempty subsets of \(V(G_n)\) lying in at least one such \(B_{i,j}\). Each ball has exactly \(2n-1\) vertices and gives a maximal simplex (for these \(n\)). Homology here is simplicial homology over \(\mathbf F_2\), and the reductions use the standard augmentation in degree zero.

## Proof

For every integer \(n\) with \(2\le n\le6\), generate the \(3n\) vertex masks of closed neighborhoods using the displayed formula. For each mask enumerate **every nonempty submask**, deduplicate to obtain the full simplex set \(F_k\) in each dimension \(k\), and construct the simplicial mod-two boundary \(\partial_k\) whose column for a simplex \(\sigma\) consists exactly of its codimension-one faces. The identity \(\partial_{k-1}\partial_k=0\) follows from the standard pairwise cancellation of deleted vertex pairs over \(\mathbf F_2\). Exact binary elimination provides the rank \(r_k=\operatorname{{rank}}_{{\mathbf F_2}}(\partial_k)\). Therefore
\[
\beta_k=|F_k|-r_k-r_{{k+1}} \quad (k\ge1), \qquad
\beta_0=|F_0|-r_1.
\]

The complete face counts \((|F_0|,\ldots,|F_d|)\) and corresponding boundary ranks \((r_0,\ldots,r_d)\), with \(r_0=0\), are:

| \(n\) | Face-count vector | Boundary-rank vector |
| --- | --- | --- |
| \(2\) | \((6,12,6)\) | \((0,5,6)\) |
| \(3\) | \((9,36,78,45,9)\) | \((0,8,28,36,9)\) |
| \(4\) | \((12,66,216,366,252,84,12)\) | \((0,11,55,161,180,72,12)\) |
| \(5\) | \((15,105,450,1155,1650,1230,540,135,15)\) | \((0,14,91,359,796,810,420,120,15)\) |
| \(6\) | \((18,153,810,2700,5598,7026,5580,2925,990,198,18)\) | \((0,17,136,674,2026,3525,3465,2115,810,180,18)\) |

The rank identity yields the asserted reduced Betti numbers in every degree. As a consistency check, the alternating face-count sum for \(n=6\) is \(12\), agreeing with \(1+47-36=12\). The ranks and face counts are supplied by two separate algorithms using, respectively, tuple sets and integer bit masks; neither uses random or partial sampling. The exact programs are included in `verify_closed_neighborhood.py`.

## Verification

Run `python3 verify_closed_neighborhood.py`. For each \(n\in\{2,3,4,5,6\}\), it enumerates all faces of all \(3n\) closed balls and computes the complete mod-two chain ranks by two independently implemented representations and elimination routines. Hard-coded vectors are checked by assertions in both routes, and Euler characteristics are cross-checked. The run passes only if every asserted value is reproduced. All computations are finite and self-contained; no external packages or data are required.

## Relationship to prior work

Matsushita's *Closed neighborhood complexes of graphs* [1] defines this invariant, relates it to independence complexes, and determines the closed-neighborhood complex of the **Cartesian** rook graph \(K_m\square K_n\) (Example 3.5). That result is for \(\mathcal N[K_m\square K_n]\), not \(\mathcal N[K_m\times K_n]\). Because complementation exchanges these two graph products, confusing the two would invalidate a novelty claim. The 2023 work of Antolín Camarena and Carnero Bravo [2] determines the independence complex of \(K_2\times K_m\times K_n\), which yields the known Cartesian case via [1], but does not give the listed finite ranks for the categorical input here. The present claim is specifically the first observed mixed-degree mod-two cutoff in the closed-neighborhood complexes of \(K_3\times K_n\) at \(n=6\).

## Limitations

Only the parameters \(2\le n\le6\) and coefficient field \(\mathbf F_2\) are proved. The calculation neither determines integral torsion nor proves a wedge-of-spheres homotopy decomposition, and it makes no claim about \(n\ge7\). The exhaustive computation is a proof of the stated finite cases only. A broader unavailable or unlocated formula may imply these values; the literature comparison is not a claim of exhaustive novelty.

## References

[1] Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, initial public submission 2025-11-16, sections 1.1–1.2 and Example 3.5, https://arxiv.org/html/2511.12608v2.

[2] Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, initial public submission 2023-07-23, section 4, https://arxiv.org/html/2307.12401v2.
