# Independent mathematical audit

## correctness

PASS

Independently reconstructed column potentials from the Laplacian. A unit common-edge source is supported on the common antisymmetric mode of eigenvalue T; a private internal source has clique eigenvalue a+2 or b+2. For the mixed source δ_u−δ_x, split off (δ_u−δ_v)/2: the symmetric remainder has potentials c/2 on both common vertices and on W, −c on x and zero on the other vertices of U, where c=1/(a+2). The antisymmetric part adds ±1/(2T) on u,v. Summing absolute drops gives (2a+1)c+(b+1)/T, with diagonal (3c+1/T)/2, plus the swapped column. For each source, the displayed diagonal is strictly between zero and one; replacing Q by I−Q changes the absolute column sum by 1−2Q_ee. This recovers all five columns and both norms by symmetry. Checked the elimination of internal columns, the two factorizations and the common-edge comparison B(a,b)−(3−6/T)=b(a−4)/((a+2)T). In particular the common cycle column wins strictly if both sizes are <4, ties if the larger size is 4 and cannot win once either exceeds 4. At a=2, b≥5 the maxima strictly separate. The positive deficits 3/(a+2)+(a+1)/T and 6/(a+2)+(a+2)/T show strict upper bounds and convergence along (k,k²). The frozen exact-rational checker and expected-output description were inspected, not executed; the unrestricted conclusion follows from the exact calculation.

## originality

PASS

Pass is for the exact two-parameter norm and phase classification under edge gluing, not for projector identities or the general phenomenon of separated cut/cycle maxima. Bounded indexed comparisons yielded close analogues, notably the same-day star-product record and the earlier clique-augmented-biclique result. Their host graphs are genuinely different; inspected primary results also do not cover the exact statement. Priority beyond these sources is not established.

## value

PASS

Identifying two cliques along their smallest nontrivial interface is a natural graph composition, and the norm measures maximal electrical response to an edge load. The exact table shows how the interface alters endpoint amplification, gives distinct thresholds and an infinite strict separation between the maximizing edge types, and determines sharp bounds not inherited from the standalone complete graphs. This supplies an explicit benchmark for composition, beyond another numerical example of opposite maximizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
