# Transfer-killed 2-torsion at five points on Theta_(2,3,4) is false: both H2 groups are torsion-free (ranks 189 vs 3)

## Context
The admitted target asked whether 2-torsion in H_2 of the ordered configuration space F_5(Theta_(2,3,4)) is killed by passage to the unordered quotient B_5(Theta_(2,3,4)) = F_5/S_5 via the 120-sheeted covering projection p and transfer: i.e., whether H_2(F_5;Z) contains a Z/2 class [w] with p_*([w]) = 0. Unordered configuration spaces are S_n-quotients of ordered ones; torsion can in principle be created or killed by the quotient, and n = 5 with S_5 of order 120 was the designated first test case separating 2- and 3-primary effects on the asymmetric theta graph Theta_(2,3,4).

## Definitions
- Theta_(2,3,4): theta graph with two essential vertices joined by three branches of combinatorial lengths 2, 3, 4. Work uses a homeomorphic subdivision with 4 edges per branch (V = 11, E = 12); configuration spaces depend only on homeomorphism type.
- F_5 = ordered configuration space of 5 distinct points; B_5 = unordered configuration space F_5/S_5; p: F_5 -> B_5 the covering projection.
- Abrams cubical model: a k-cell = k edges + (n-k) vertices with pairwise-disjoint closures, with product sign boundary. Valid when every path between distinct essential vertices has >= n-1 edges and every cycle has >= n+1 edges (Abrams 2000). Here n = 5: branch length 4 >= 4, each cycle 8 >= 6.

## Result
The target claim is FALSE. In fact both sides are torsion-free:

- H_2(B_5(Theta_(2,3,4)); Z) ≅ Z^3,
- H_2(F_5(Theta_(2,3,4)); Z) ≅ Z^189,

so no nonzero 2-torsion class [w] exists upstairs; a fortiori none lies in ker p_*. The transfer composite ker(τ∘p_*) therefore contains no Z/2 from the asserted source. The degree-2 ordered/unordered comparison is a torsion-free correspondence (ranks 189 vs 3), not a torsion-killing.

Integral Betti data: unordered b = (1,3,3); ordered H_1 has dim 70 over F_p for p = 2,3,5 (consistent with b_1^ord = 70), H_2 rank 189.

## Proof / evidence
1. Unordered Abrams complex on the subdivided model: C = (462,1512,1785,920,198,12) with exact d^2 = 0 (d1d2 = d2d3 = d3d4 = d4d5 = 0), independently replayed.
2. Greedy free-face collapse to remaining (202,467,266,0,0,0), machine-verified to be a SUBCOMPLEX (every face of every remaining cell is remaining); hence the collapse sequence is a valid homotopy equivalence and the quotient is a 2-dimensional complex with C_3 = 0 homotopy equivalent to B_5.
3. Unordered ranks: rank(A1) = 201, rank(A2) = 263 over Q and over F_2,F_3,F_5, giving b = (1,3,3). H_2(B_5) = ker(A_2) with no C_3 is a subgroup of a free abelian group, hence FREE of rank 3. No 2-torsion downstairs.
4. Ordered lift: 120 lifts per remaining cell (S_5 acts freely), C^ord = (24240,56040,31920), C_3 = 0. Machine-verified: all faces of all 31920 lifted 2-cells present (lifted subcomplex), and explicit label-ordered sign convention satisfies d_1^ord·d_2^ord = 0 over Z on all 31920 columns. Hence H_2(F_5) = ker(d_2^ord) is FREE abelian — a Z/2 class cannot exist. This falsifies the target structurally, independent of rank computation.
5. Ranks pin the groups: sparse exact row-echelon rank of ordered d_2 (56040×31920, 4 nonzeros/column) = 31731 identically over F_2,F_3,F_5,F_7,F_1000003, so b_2^ord = 31920-31731 = 189 and dim H_2(F_p) = 189 for p = 2,3,5. Ordered d_1 rank 24239 over Q (1-skeleton connected, union-find: 1 component) and over F_2 (graph-incidence left-nullspace + no-loop certificate), giving dim H_1(F_p) = 70. Euler cover check: χ^ord = 24240-56040+31920 = 120 = 120·χ(B_5). ✓
6. Freeness plus five-modulus rank agreement gives H_2(F_5) ≅ Z^189, H_2(B_5) ≅ Z^3. Full rank tables and UCT cross-checks exclude 2/3/5-torsion; freeness as subgroups of free groups excludes all other torsion.

## Limitations
- Depends on Abrams' theorem (subdivision criterion) as a cited result; the criterion is verified numerically, the theorem not re-proved.
- Collapse-matching validity certified by machine-checked free-face/subcomplex verification, not an independent Morse-theoretic proof.
- Explicit generators of Z^189 and the integer matrix of p_*: Z^189 → Z^3 (necessarily a nonzero map between free groups; cokernel not computed) are not claimed.
- Scripts use Python standard library + numpy (dense small cases); large ranks use exact sparse elimination over finite fields (replayable).

## Reproducibility
Scripts in output/artifacts/: verify_theta.py (enumerate cells, d^2=0), full_complex.py (d4,d5), collapse.py (greedy collapse), homology_reduced.py (subcomplex check + reduced homology), wiedemann.py (build sparse ordered d2), verify_upstairs.py (lifted subcomplex + d1d2=0 over Z), rank_wied.py / rank_big.py (exact sparse ranks mod 2,3,5,7,1000003), ordered_d1_fix.py / d1f2.py / h1_ordered.py (ordered d1 analysis), HOMOLOGY.txt (rank log). Audit replayed: cell counts, all d^2=0 identities, subcomplex checks, collapse endpoint, d1d2=0 over Z (31920 cols), ordered d2 rank 31731 over F_2,F_3,F_5,F_7,F_1000003, ordered d1 rank 24239 with connectivity + no loops.

## References
- Abrams, Configuration spaces of braid groups of graphs (2000) — cubical model and subdivision criterion (cited).
- Farley-Sabalka, Discrete Morse theory and graph braid groups — Morse models.
- Wawrykow, Homology generators and relations for ordered star-graph configurations — nearest ordered-generation result (H1 stars only).
- Maciazek-Sawicki, Homology groups for particles on one-connected graphs — tree particle homology.
- Kallel, Configuration Spaces of Points: A User's Guide — survey of models.
- An-Drummond-Cole-Knudsen, Asymptotic homology of graph braid groups — asymptotic Betti theory (does not imply fixed-n ranks).
- Chettih-Lütgehetmann (via Idrissi-Roca background) — ordered torsion-freeness for trees with loops only.
