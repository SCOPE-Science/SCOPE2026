# Independent audit — 2026-09-30

**Record:** `2026/09/21/strong-roman-nonstandard-six-sevenths-families--d5c761361fb8`  
**Audited repository:** `SCOPE-Science/SCOPE2026`  
**Audited current commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree SHA:** `aeba101ac5983ab556f87b2dcc5355c4a045f6aa`  
**Disposition:** passed

The assignment snapshot remains current for this record: comparison from the dispatcher's source-tree-checked commit to current `main` showed no changed file under the assigned record path. The dated independent-audit targets were separately verified absent, and the current `VERIFICATION.md` blob guard was verified before staging this change-set.

## Correctness — PASS

PASS. The seven-vertex local lower bound was reconstructed case-by-case. For every support-leaf pair the weight is at least one, with equality only in the (support,leaf)=(0,1) configuration. For the subdivided claw S, root labels >=3 immediately force weight >=6; root label 2 with total weight <6 forces all three supports to be zero, but then the root has three zero neighbours and label 2 cannot defend them; root label <=1 forces each support-leaf pair to have weight at least two. For H=S+ab, the c=3+, c=2, c=1 and c=0 cases likewise force weight >=6; in the c=0 case, if the two triangle-side pairs had weight at most three, one support would be zero with leaf 1 and the only possible label-2 defender on the other support would itself have three zero neighbours, requiring label 3. External neighbours occur only at the root and can only make root-based defence harder. The stated weight-six labelings on S and H are valid, and all base-graph root edges join positive roots, so they remain valid globally. The non-isomorphism argument is also sound: for m>=2 a standard rooted product has exactly 3m degree-two support vertices, whereas each H block reduces that count by two. Independent exhaustive enumeration of the two isolated seven-vertex blocks from the definition returned gamma_StR(S)=gamma_StR(H)=6.

## Originality — PASS

PASS, with a documented historical qualification. Alvarez-Ruiz et al. (2017) explicitly pose the universal 6n/7 question and immediately propose that, if true, equality should occur exactly for connected rooted products with the subdivided-claw block. Mahmoodi--Nazari-Moghaddam--Behmaram (2020) already observe that adding an edge to a standard extremal construction need not increase strong Roman domination, so the general edge-addition phenomenon is prior. However, that source does not give the audited triangularized block lower bound, the exact mixed S/H family, or the degree-sequence obstruction to the proposed classification. The complete 15-page Poureidi--Abd Aziz--Jafari Rad--Kamarulhaili (2022) article was obtained through authorized institutional access after open-access attempts failed; it develops linear algorithms for trees and unicyclic graphs and does not state this equality family or classification counterexample. Targeted searches also did not locate the same mixed-block construction. Thus the precise theorem survives the prior-art comparison.

## Scientific value — PASS

PASS. The result gives infinitely many connected exact 6/7 examples outside a published proposed equality class, with a reusable local block proof and an explicit obstruction to rooted-product isomorphism. It is a meaningful correction/refinement of the structural conjecture even though it does not settle the separate universal upper-bound problem.

## Independent checks

- Reconstructed every local lower-bound case for both seven-vertex blocks, including possible external neighbours at the root.
- Independently brute-forced the strong Roman domination number of the isolated S and H blocks and obtained 6 for each.
- Rechecked the two explicit weight-six labelings and the degree-two count separating mixed constructions from standard rooted products.
- Inspected the complete 2022 tree/unicyclic linear-algorithm paper through authorized institutional access after OA routes failed; no equality-family theorem was found.

## Literature evidence

- https://doi.org/10.1016/j.dam.2016.12.013 — Alvarez-Ruiz et al. (2017), tree 6n/7 theorem and closing universal/equality questions.
- https://doi.org/10.22052/mir.2020.225635.1205 — Mahmoodi, Nazari-Moghaddam and Behmaram (2020), prior edge-addition/unicyclic strong Roman results.
- https://doi.org/10.1007/s40840-022-01301-4 — Poureidi et al. (2022), complete 15-page full text inspected via authorized institutional access; linear algorithms for trees and unicyclic graphs.
- https://doi.org/10.3390/math14091535 — Valenzuela-Tripodoro et al. (2026), later exact/complexity results for specific graph families.

## Access notes

- Oxford job c4c0ad06a1c99bda3ee321e3847a36d5 completed; all 15 pages of the 2022 paper were inspected.

## Limitations

- The theorem refutes the proposed equality classification but does not prove the universal gamma_StR(G)<=6|V|/7 conjecture.
- The 2020 paper contains a related prior edge-addition observation, so novelty is restricted to the exact local mechanism and infinite mixed equality family.
- As with any targeted graph-literature search, an unindexed equivalent construction cannot be absolutely excluded.

No GitHub write was performed by the audit chat. This file is staged only by the guarded `scope-audit-change-set-v1` publication plan.
