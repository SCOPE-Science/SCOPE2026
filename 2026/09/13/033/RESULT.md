# Exact Fano-restricted Pasch minimum over sigma-invariant STS(21)s

## Context

A Steiner triple system of order 21 (STS(21)) is a set of 70 triples on 21 points with every pair in exactly one triple. A Pasch configuration is 4 blocks on 6 points, pairwise meeting once (the (6,4) quadrilateral). A sub-STS(7) is 7 points carrying exactly 7 blocks, necessarily a Fano plane. This record studies the tricyclic family: designs admitting sigma, a permutation of three disjoint 7-cycles. Mathon, Phelps, and Rosa enumerated the isomorphism types of this family (95 in 1981, corrected to 97 in a 1995 addendum). The admitted target asked for the minimum Pasch count over Fano-containing members with a per-type certificate; the isomorphism-splitting step did not finish, so the completed finding is the labeled-level extremal census under a fixed sigma, which fixes the numerical minimum by isomorphism-invariance.

## Definitions

- Points: 21, labelled as Z7 x {0,1,2}, encoded 0..20 with group = p//7, residue = p%7.
- sigma: (a,i) -> (a+1 mod 7, i); three disjoint 7-cycles.
- STS(21): 70 triples, each pair in exactly one triple.
- Pasch: 4 blocks on 6 points, pairwise meeting once.
- Sub-STS(7) (Fano): 7 points carrying exactly 7 blocks.
- Labeled tricyclic design: STS(21) fixed setwise by the fixed sigma above.

## Result

Over all 135128 sigma-invariant labeled STS(21)s, exactly 61040 contain a sub-STS(7) Fano subplane, and the minimum Pasch count over the Fano-containing labeled designs is exactly 7, attained by 1764 labeled solutions. The overall labeled minimum ignoring the Fano restriction is 0. An explicit 70-block witness (labeled index 10) with Fano point set {0,1,2,3,4,5,6} attains the bound: its 7 sub-blocks on that set are 013, 026, 045, 124, 156, 235, 346 (a Fano plane), and its 7 Pasch configurations are {013,026,124,346}, {013,026,156,235}, {013,045,124,235}, {013,045,156,346}, {026,045,124,156}, {026,045,235,346}, {124,156,235,346}, all lying inside the Fano set. Since Pasch count and Fano-containingness are isomorphism invariants, the numerical value of the type-level minimum is likewise 7.

## Proof / evidence

Labeled enumeration: all C(21,3)=1330 triples fall into 190 sigma-orbits of size 7; all C(21,2)=210 pairs fall into 30 sigma-orbits of size 7; 9 block-orbits are inadmissible (a triple meeting one pair-orbit twice), leaving 181 rows each covering 3 distinct pair-orbit columns. A sigma-invariant STS(21) is an exact cover of the 30 columns by 10 rows; exhaustive Algorithm X returns 135128 solutions. Each expands to 70 blocks (10 orbits x 7) and passes an independent pair-uniqueness check. Counting: pasch_find scans block pairs meeting once and tests the two opposite pairings via the pair-to-third map, asserting the 6-fold multiplicity (raw%6==0 and len==raw//6); fano_find uses triple closure via the pair-to-third map. Both were cross-validated against brute-force 6-subset and 7-subset scans. The exhaustive per-solution census gives [index, pasch, nfano, fanosets] for all 135128: 61040 Fano-containing, minimum 7 attained by 1764. The independent verifier rebuilds every design from the exact-cover row sets and asserts n_fano==61040, min==7, min-all==0. The auditor independently re-verified the witness by brute force, re-checked all 135128 exact covers for distinctness and coverage, and triple-cross-checked 12 random solutions (cached census vs fresh library counts vs brute force: all match).

## Limitations

The 95/97-row per-type attribution table (class sizes summing to 135128 with per-type Pasch/Fano values) was not completed; the backtracking isomorphism split stalled in-session. This record therefore claims only the labeled-level theorem plus the numerical type-level value via invariance, not the full per-type certificate. The topic text cites 95 MPR types while the 1995 addendum corrects the total to 97; the labeled census under fixed sigma is unaffected either way.

## Reproducibility

Rebuild the orbit matrix and enumerate exact covers with output/artifacts/sts_lib.py; recompute with output/artifacts/verify_labeled.py against output/artifacts/witness.json (70-block witness with marked Fano set). Brute-force 6-subset (Pasch) and 7-subset (Fano) scans on the witness give 7 and 1 respectively.

## References

- R. A. Mathon, K. T. Phelps, A. Rosa, A class of Steiner triple systems of order 21 and associated Kirkman systems, Math. Comp. 37 (1981), 209-222; Addendum, Math. Comp. 64 (1995) correcting the tricyclic total from 95 to 97.
- P. Kaski, Isomorph-free exhaustive generation of designs with prescribed automorphism groups, SIAM J. Discrete Math. 19 (2005).
- J. I. Kokkala, P. R. J. Ostergard, Sparse Steiner triple systems of order 21, J. Combin. Des. 29 (2021); Zenodo dataset.
- G. Erskine, T. S. Griggs, Properties of Steiner triple systems of order 21, arXiv:2401.13356 (2024).
- Kaski et al., Steiner triple systems of order 21 with subsystems, arXiv:2104.06825.
