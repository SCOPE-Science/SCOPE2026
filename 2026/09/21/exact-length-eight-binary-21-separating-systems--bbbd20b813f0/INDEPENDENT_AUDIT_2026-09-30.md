# Independent audit — 2026-09-30

**Record:** `2026/09/21/exact-length-eight-binary-21-separating-systems--bbbd20b813f0`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `3642eb4f1282d4f940e961a7884c5965107c510e`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The equivalence between binary 2-frameproof codes, (2,1)-separating systems, and general-position sets in Q8 was checked directly from the coordinatewise descendant/geodesic-subcube condition. The minimum-distance reductions d≠1 and d≤4 for an 11-word hypothetical code are valid. The C++ verifier was inspected rather than trusted as a black box. It enumerates every feasible orbit of a canonical third word for d=2,3,4, uses graph coloring only as a valid clique upper bound, and separately enforces the full three-word separating constraint at each branch. Its logged maxima are all at most 10 and the explicit 10-word witness is exhaustively checked.

## Originality

**PASS (literature-bounded).** The August 2026 general-position survey still lists exact hypercube values only through Q7, while the 2023 Korže–Vesel paper gives Q8 only a lower bound 10. That very recent status source strongly supports novelty of the matching upper bound. Priority remains stated to the checked literature rather than as an exhaustive global nonexistence claim.

## Scientific value

**PASS.** Determining gp(Q8)=10 closes the first dimension immediately beyond the previously exact range and simultaneously settles the binary length-eight (2,1)-separating / 2-frameproof parameter.

## Literature and evidence

- Chandran, Klavžar and Tuite, The General Position Problem: A Survey (v5, 2026): https://arxiv.org/abs/2501.19385
- Korže and Vesel, General Position Sets in Two Families of Cartesian Product Graphs: https://doi.org/10.1007/s00009-023-02416-z

## Limitations

- The upper bound is a finite exact computer-assisted verification after symmetry reduction, not a parameter-uniform proof.
- No claim is made for Q9 or larger hypercubes.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
