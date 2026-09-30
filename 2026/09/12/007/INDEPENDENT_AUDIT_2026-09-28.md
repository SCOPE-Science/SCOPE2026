# Independent Audit — 2026/09/12/007

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `fda72bb415af198bd3573173a96a62c9d92ad4a0`  
**Audited current source tree:** `fda72bb415af198bd3573173a96a62c9d92ad4a0`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** repaired

The current `main` record tree matches the assigned tree SHA.

## Correctness

PASS AFTER SUBSTANTIVE COUNTING REPAIR. Exact re-enumeration confirms 18 oriented BG-admissible factor records and the outermost section alpha^2=13/10, but they form 9 unordered decompositions and only six distinct numerical wall loci. The top locus is realized by two unordered decompositions, not uniquely by one. The repaired result/script state the correct multiplicities while preserving the outermost semicircle.

## Originality

SUPPORTED, NARROW. Targeted searches of GM stability/Serre-functor/moduli literature found general constructions but no explicit branch-fixed beta=-3/2 six-locus census or the 13/10 outer envelope. The audit therefore treats the corrected numerical census as a narrow new computation, not as a new general stability theorem.

## Scientific value

MEANINGFUL NUMERICAL BOUND. A complete exact envelope for candidate two-factor walls of a specific branch-fixed class is reusable for later actual-wall and Bridgeland-moduli arguments; correcting decomposition counts does not remove the outermost bound.

## Independent checks

- exact independent 18-record enumeration
- grouping into 9 unordered decompositions and six normalized wall equations
- two distinct top decompositions at alpha^2=13/10
- current main tree equals assigned tree

## Limitations

- The six loci are numerical candidates under stated necessary conditions; actual wall existence is not proved for every locus.
- Picard-rank-one/general special-GM hypotheses remain.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/007
- https://doi.org/10.1002/mana.202200010
- https://doi.org/10.2140/gt.2022.26.3055

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
