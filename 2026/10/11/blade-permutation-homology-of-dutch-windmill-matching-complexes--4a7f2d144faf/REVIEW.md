# Scientific review

## Correctness — PASS

The result concerns the coordinate-aligned blade-permutation action on the matching complex of n>=2 cycles C_m with m=3k+1 or 3k+2, k>=1, joined at a common vertex. A direct fixed-matching argument gives F(pi)=A^c-2f B A^(c-1), where c and f are the cycle and fixed-blade counts of pi, and A=a_(m-2), B=a_(m-3) for the path recurrence a_0=1, a_1=0, a_r=a_(r-1)-a_(r-2).

For a fixed matching S containing o edge orbits, its contribution to the reduced simplicial Lefschetz number is (-1)^(o-1); the empty simplex contributes -1. Thus the reduced Lefschetz number is -F(pi). Donovan--Scoville Theorem 5.8 supplies the sole nonzero reduced homology degree. Substituting the six-periodic recurrence gives the characters sgn(pi)^k for m=3k+1 and sgn(pi)^k(2f(pi)-1) for m=3k+2. Over Q, these are respectively the sign twist and the sign twist of the direct sum of the trivial representation and two standard modules.

A separate fixed-edge-orbit enumeration checked 70 group elements across seven finite (n,m) combinations, agreeing in every case. This is corroboration; the general result follows from the symbolic orbit count and published homology concentration. The exact seven-entry source Git tree, including both artifact blobs, was reconstructed from object identities.

## Originality — PASS (best-of-knowledge)

Donovan and Scoville already establish the nonequivariant sphere and wedge-of-spheres classification for these graphs (New York Journal of Mathematics 29 (2023), Theorem 5.8). Their proof does not state a character of the blade permutation group; homology rank alone does not determine an S_n representation. Bate--Everitt--Ford--Ramos study complete-hypergraph matching complexes and asymptotic representation stability, Dong--Wachs treat the complete-graph matching complex, and Li proves log-concavity for matching permutation modules on arbitrary graphs. None of these theorems supplies this exact induced homology module.

Related explicit computations for the dihedral matching complex of a single cycle and the symmetric-group action on the ordinary Morse complex of a two-edge-arm tree concern different groups or complexes. Their fixed-orbit methods do not imply the joined-cycle blade formula without the new common-center matching analysis. Equivalent-formulation, broader-coverage, exact-table, and implication checks were separately documented. The identical current research record was excluded as prior-art support.

The author’s 2023 thesis landing page was examined, but its full PDF returned 403; no full-text noncoverage claim is made for that thesis. Unindexed historical equivariant cactus/windmill calculations remain possible. The verdict is best-of-knowledge rather than a historical-priority guarantee.

## Mathematical value — PASS

The blade-permutation S_n action is a canonical symmetry of this infinite graph family. The explicit character determines how every blade permutation acts on the single nonzero reduced rational homology group and exposes a parity-dependent sign twist and two standard-representation summands invisible in the previously known Betti numbers. This is a useful structural refinement for equivariant and quotient constructions. No integral or full-automorphism representation is claimed.

## Sources and boundaries

- Donovan and Scoville, *Star clusters in the matching, Morse, and generalized complex of discrete Morse functions*, New York J. Math. 29 (2023), Theorem 5.8, pp. 1409-1410 (arXiv:2207.13780).
- Bate, Everitt, Ford and Ramos, *Homology of matching complexes and representations of symmetric groups*, Proc. Amer. Math. Soc. (2026), DOI:10.1090/proc/17573.
- Dong and Wachs, *Combinatorial Laplacian of the Matching Complex*, Electron. J. Combin. 9 (2002), #R17.
- Li, *Equivariant log-concavity of graph matchings*, arXiv:2202.08828.

The assessment uses neither a formal proof assistant nor expert attestation.
