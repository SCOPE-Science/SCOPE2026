# Universal unipotent omission for w=[x,y]^2 z^3 on PSL(2,q), q = 3 mod 4, is false (counterexample at q=11)

## Context
Word maps on finite simple groups are studied in the Borel / Larsen–Shalev / Liebeck–O'Brien–Shalev–Tiep surjectivity and Waring program. Mixed commutator-power words such as w(x,y,z)=[x,y]^2 z^3 sit at the open boundary where character-sum and algebro-geometric fibre-count methods meet. The admitted target claim was a universal non-surjectivity statement: for every prime power q = 3 mod 4 with q >= 11, the map w on G_q = PSL(2,q) misses the nontrivial unipotent class U_q.

## Definitions
- q = 11 (prime power, 11 = 3 mod 4, 11 >= 11, hence in the claimed family).
- G_q = PSL(2,q) = SL(2,q)/{+/-I}; identify M ~ -M.
- [x,y] = x y x^{-1} y^{-1}; w(x,y,z) = [x,y]^2 z^3.
- U_q = image in G_q of the SL(2,q)-class of U = [[1,1],[0,1]] (trace 2, nontrivial, not +/-I).
- |w^{-1}(g)| = number of triples in G_q^3 mapping to g.

## Result
The universal claim is FALSE. For q = 11, the unipotent element u (image of U) lies in the image of w. Explicit SL(2,11) lifts:

- X = [[4,0],[6,3]], det = 12 = 1 mod 11,
- Y = [[2,10],[10,1]], det = 2-100 = 2-1 = 1 mod 11,
- Z = [[2,10],[3,10]], det = 20-30 = 9-8 = 1 mod 11,

satisfy [X,Y] = [[10,5],[0,10]], [X,Y]^2 = [[1,1],[0,1]] = U, Z^3 = [[10,0],[0,10]] = -I, hence w(X,Y,Z) = U(-I) = -U ~ U in PSL(2,11). Therefore |w^{-1}(u)| >= 1, contradicting "|w^{-1}(g)| = 0 for every g in U_q for all q = 3 mod 4, q >= 11".

## Proof / evidence
Exact 2x2 matrix arithmetic mod 11 (proof by witness, not statistical evidence):
X^{-1} = [[3,0],[5,4]], Y^{-1} = [[1,1],[1,2]]; direct multiplication gives [X,Y] = X Y X^{-1} Y^{-1} = [[-1,-6],[0,-1]] = [[10,5],[0,10]]; squaring gives U; cubing Z gives -I; product gives -U, identified with U in PSL. All steps replayed by output/artifacts/verify_counterexample.py (stdlib only), printing VERIFY_OK. Auditor independently re-executed the script and a manual cross-check; all equalities hold. One q in the family suffices to refute a universal statement.

## Limitations
Disproves only the universal claim as stated. Does not decide full surjectivity of w on PSL(2,11), fibre behaviour for larger q = 3 mod 4 (19, 23, ...), nor any equidistribution or character-bound statement. Possible splitting of unipotents in PSL(2,q) is irrelevant here because the witness hits the topic-defined representative U_q exactly.

## Reproducibility
Run from the lane directory: python3 output/artifacts/verify_counterexample.py (pure stdlib, deterministic, prints VERIFY_OK with all intermediate matrices).

## References
- Target and admission context: inputs/topic.json (Borel / Larsen–Shalev / Liebeck–O'Brien–Shalev–Tiep program; Bandman–Garion x^a y^b and Engel PSL(2,q) results as nearest different-word prior work).
- Nearest prior results checked and distinguished: Biswas–Saha arXiv:2012.01408 (different 2-variable words); Larsen–Shalev–Tiep probabilistic Waring (product-of-images, not single-word fibre); Bandman–Garion–Grunewald Engel words on PSL(2,q); Liebeck–O'Brien–Shalev–Tiep arXiv:1505.00718 (x^N y^N-type, large groups); Bandman et al. survey on equations in simple matrix groups.
