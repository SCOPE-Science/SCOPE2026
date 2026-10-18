# Scientific review

## Correctness — PASS

For finite nonempty triangle-free \(H\) with connected \(I=\operatorname{Ind}(H)\), and \(m\ge2\), triangles of \(K_m\vee H\) are exactly triangles within hubs, one hub plus an edge of \(H\), or two hubs plus one vertex of \(H\). Therefore the equality \(\operatorname{CF}_3(K_m\vee H)=\Delta_R\cup_I(D_m*I)\cup\bigcup_{i<j}[u_i,u_j]\) is exhaustive. Cofibration and an equivariant contraction of the full simplex give \(A\simeq D_{m+1}*I\); connectedness of \(I\) makes \(A\) simply connected. Attaching one-cell edges contributes one free circle apiece. The relative homology long exact sequence identifies the integral \(H_1\) edge-permutation module as \(\bigwedge^2\mathbb Z^m\), while the join-chain tensor and \(\widetilde H_0(D_{m+1})\) give the higher integral modules. The proof covers every specified graph and integer without using a finite-experiment extrapolation.

A reproducible standalone script independently generates graph triangles and all legal faces, checks mod-two homology, and evaluates signed Lefschetz numbers for six tests. These finite checks agree with the formulas; they do not prove the general theorem.

## Originality — PASS, subject to bibliographic uncertainty

The motivating primary source (Ghosh–Selvaraja, arXiv:2602.09623, February 10, 2026) was compared at the level of its theorems and constructions. Its localized clique attachments and shellability criteria do not assert the current global clique-join homotopy or integral representation formulas; induced nonchordal cycles in the specialized family also evade its chordal hypotheses. The nearest mathematical-record results on neighborhood complexes of clique joins concern a different simplicial functor; cycle matching-complex character results can supply the known input \(\operatorname{Ind}(C_n)\) but do not compute the three-clique-free complex of the clique join. Searches for triangle-free/clique-free complexes, equivalent joins and suspension or exterior-square formulas identified no statement implying the theorem. There may be unindexed equivalent results, and no claim of literature completeness is made.

## Mathematical value — PASS

The theorem converts an arbitrary connected independence-complex homotopy type into the three-clique-free topology of a whole family of graphs that contain many triangles, while introducing an unexpected universal free fundamental group of rank \(\binom m2\). Its exact *integral equivariant* information detects hub permutations, including endpoint signs on first homology, and preserves torsion in any higher base homology. The cycle family gives natural mixed one- and higher-dimensional homotopy types. These are a structural transfer law and symmetry classification, not only an arbitrary small-graph invariant or a face count.

## Residual limitations

The result is restricted to connected \(\operatorname{Ind}(H)\), graph joins with a clique, and the canonical product symmetry subgroup. The cycle special case uses preexisting independence-complex calculations. A published or unindexed stronger general simplicial gluing theorem may subsume the argument, although the targeted comparisons found none stated for this construction. The finite checker cannot establish integral torsion behavior for all graphs; the proof does.

Self-review: passed. Independent audit: not yet performed.
