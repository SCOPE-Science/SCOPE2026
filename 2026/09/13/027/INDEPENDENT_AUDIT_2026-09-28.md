# Independent audit — 2026-09-29
- Source: `2026/09/13/027`
- Assigned/current tree SHA: `1fc2fc8751787bf8bf311031844af479fb9f88f2`
- Audited repository commit: `eff2c6312cec5b0dee5115e5f42211a853092dfb`
- Disposition: **passed**

## Three-axis assessment

### Correctness

**PASSED** — Independent enumeration reproduces 108 candidate normalized base blocks, 224 raw exact-cover families and 7 multiplier classes. Developing each representative with the forced short orbit gives a valid 70-block STS(21), and an independent scan of all 54,264 six-subsets reproduces Pasch counts 63,63,63,42,42,21,0. Classical literature independently confirms that there are seven cyclic STS(21) systems.


### Originality

**PASSED** — The seven cyclic systems themselves are classical, so that classification is not new. Targeted searches through the STS(21) classification/configuration literature did not locate the exact Pasch-count vector or the cyclic-subclass maximum 63. The retained originality is narrowly the exact Pasch census/max over this already-known finite family.


### Scientific value

**PASSED** — Pasch configurations are standard structural invariants in Steiner triple systems, and the exact extremum plus full seven-type distribution is a reusable datum for the classical cyclic STS(21) family. The contribution is finite and computational but scientifically interpretable rather than an arbitrary enumeration.


## Independent checks

- independently regenerated the 108 admissible base triples and solved the exact-cover condition to obtain 224 raw families
- quotiented by units modulo 21 and reproduced seven multiplier classes and their class sizes
- developed every representative to 70 blocks and verified all 210 point pairs occur exactly once
- independently scanned every 6-subset and reproduced Pasch counts 63,63,63,42,42,21,0
- compared with Mathon–Phelps–Rosa, whose 1981 classification explicitly includes the seven cyclic systems
- confirmed the current main record tree matches the assigned source-tree SHA

## Limitations

- The independent rerun establishes the exact census for the seven multiplier representatives; the literature search cannot prove that no obscure older table printed the same Pasch vector.
- The result concerns only cyclic STS(21), not all STS(21).
- Open-access/bibliographic sources were sufficient; Oxford Download was not needed.

## Citations

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/13/027
- https://doi.org/10.1090/S0025-5718-1981-0616374-9
- https://doi.org/10.1002/jcd.21906
