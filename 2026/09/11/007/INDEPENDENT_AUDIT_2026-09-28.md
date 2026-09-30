# Independent Audit — 2026/09/11/007

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `ef0aad293901dfd103ad04288ddaa8ca8e7ffad2`  
**Audited current source tree:** `ef0aad293901dfd103ad04288ddaa8ca8e7ffad2`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA, so no intervening record change required a stale-source re-audit.

## Correctness

PASS. The archived GAP/CTblLib Frobenius table is internally consistent with the stated positive and zero class triples for L3(8), L3(8).3 and L3(8).6. The decisive extension obstructions are elementary once the recorded subgroup structure is established: in the index-3 normal socle of L3(8):3, elements of orders 2 and 7 map trivially to C3, so every (2,3,7) triple is trapped in the socle; in Aut(L3(8)) the normal index-2 L3(8):3 contains all odd-order elements, and the Frobenius table shows that positive triples use the inner involution class, hence lie in that proper subgroup. For the simple socle, the archived exhaustive positive-class scans report generated subgroup orders 168 or 504 with named proper-maximal containment. These data support the non-generation verdict for the three-group window.

## Originality

SUPPORTED, COMPUTATIONAL-CENSUS SCALE. The simple-group non-Hurwitz context and the group/representation data are standard. The potentially original content is the explicit per-class Frobenius table for the :3 and :6 extensions together with the concrete quotient/maximal-subgroup trapping chain. Targeted literature checks found related Hurwitz-group and socle-PSL(3,q) work but not this exact extension-window table. That search result is only supporting context, not a proof that no earlier computation exists.

## Scientific value

USEFUL FINITE-GROUP DATA. The record closes a small canonical almost-simple window over PSL(3,8) and provides reproducible class-multiplication and subgroup-obstruction data rather than a bare negative verdict. Its scope is necessarily narrow and computational; the value is as an exact census fragment and verification benchmark.

## Independent checks

- current main record tree SHA equals the assigned source-tree SHA
- frobenius_all.log read directly and positive/zero class entries matched the RESULT.md table
- L3(8):3 archived log verifies a normal socle of index 3 with quotient C3
- L3(8):6 archived log verifies a normal L3(8):3 subgroup of index 2 and no outside elements of orders 3 or 7

## Limitations

- This audit read the archived GAP/CTblLib and ATLAS-derived logs but did not independently rebuild all permutation representations in a fresh GAP installation.
- The detailed simple-socle proper-maximal attribution depends on the archived exhaustive scan logs and ATLAS word programs.
- Originality is limited to the explicit extension-window census; the underlying character theory, ATLAS data and quotient arguments are standard.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/11/007
- https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L38/
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/L3%288%29.6.html
- https://doi.org/10.17398/2605-5686.36.1.51

This audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
