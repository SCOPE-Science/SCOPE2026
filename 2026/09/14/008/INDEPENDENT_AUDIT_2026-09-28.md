    # Independent audit — 2026/09/14/008

    **Audit date:** 2026-09-28 (UTC)  
    **Repository:** `SCOPE-Science/SCOPE2026`  
    **Assigned source tree:** `21282ae2efbca8fe26999dabed9c9061cd6934e9`  
    **Audited current source tree:** `21282ae2efbca8fe26999dabed9c9061cd6934e9`  
    **Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
    **Disposition:** repaired

    The current `main` tree for this record matches the assignment tree SHA.

    ## Correctness

    **PASSED** — PASS AFTER REPAIR. Independent reconstruction gives 20 edges and exactly 16 minimal covers in orbit types (3,3,1)^5,(3,5,0)^5,(4,2,1)^5,(5,0,1). The fractional-cover LP has optimum 29/19 at (3^5,2^5,4)/19. I enumerated all 3,656 half-integral edge covers, obtaining exactly 474 D5-orbits; the worst dual ratio is 29/38 at x=(1/2,...,1/2). I also independently enumerated 594 nonbipartite induced vertex sets and found no disjoint pair, confirming odd-cycle packing number 1. Together with standard half-integral b-matching structure, this validates the 1/2 rounding gap and rho=38/29. Reproducibility paths are repaired.

    ## Originality

    **PASSED** — SUPPORTED, NARROW. Bocci et al. give the squarefree-monomial LP framework and Gu–Hà–O'Rourke–Skelton give exact formulas for unicyclic graphs. The Grötzsch graph is not unicyclic, and the checked sources do not state the numerical pair 29/19 and 38/29 for M4. The elementary I^(2r-1) containment is not treated as original; retained originality is the exact M4 invariant computation.

    ## Scientific value

    **PASSED** — SUBSTANTIVE EXACT BENCHMARK. M4 is the canonical triangle-free 4-chromatic Mycielski graph. Exact symbolic-power invariants for its edge ideal, with independently checkable LP and odd-cycle-packing certificates, provide a useful non-perfect, non-unicyclic test case.

    ## Independent checks

    - rebuilt M4 and all 16 minimal covers
- solved the fractional cover LP at 29/19
- enumerated 3,656 half-integral edge covers and 474 D5 orbits, with worst dual value 29/38
- enumerated 594 nonbipartite induced sets and verified no disjoint pair
- verified actual committed artifacts live under artifacts/ and artifacts/probe/
- confirmed current and assigned tree SHAs agree

    ## Limitations

    - The universal saturated-cover containment lemma is not claimed as novel.
- The audit independently checked the core invariants, not every ancillary alpha-table entry in the original package.
- Targeted literature comparison cannot prove exhaustive priority.
- Open-access sources were sufficient; Oxford Download was not needed.

    ## Evidence and references

    - https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/008
- https://arxiv.org/abs/1508.00477
- https://arxiv.org/abs/1805.03428

    This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
