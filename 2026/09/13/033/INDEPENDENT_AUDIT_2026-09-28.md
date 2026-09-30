# Independent Audit — 2026/09/13/033

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `ff023988648557102d5ac94a878674de3f897cde`  
**Disposition:** **PASSED**

## Correctness

**Verdict:** PASS  
The headline finite census was independently reconstructed from the fixed three-7-cycle action rather than accepted from the record cache. The 1,330 triples split into 190 size-7 sigma-orbits; removing the 9 orbits that repeat a pair-orbit leaves 181 admissible exact-cover rows on 30 pair-orbit columns. An independent exhaustive exact-cover enumeration returned exactly 135,128 labeled systems. Recomputing Pasch counts and sub-STS(7) closure over all solutions gave 61,040 Fano-containing systems, minimum Pasch count 7 on that restricted class, 1,764 labeled attainers, and unrestricted minimum 0. The supplied 70-block witness is a valid STS(21), sigma-closed, contains the stated Fano plane, and has seven Pasches. The numerical type-level minimum follows from isomorphism invariance. A packaging limitation remains: verify_labeled.py expects raw_solutions.json, which is not shipped in the current artifact inventory, so that script is not by itself a one-command reproduction of the exhaustive census.

## Originality

**Verdict:** PASS  
Mathon–Phelps–Rosa classify the tricyclic STS(21) family (95 in 1981, corrected to 97) and study resolvability/invariants, Heinlein–Östergård classify all STS(21)s with sub-STS(7), and Erskine–Griggs survey configuration properties of all STS(21)s with nontrivial automorphism. None of those sources states the joint Fano-containing tricyclic Pasch minimum, the fixed-sigma labeled prevalence 61,040/135,128, or the 1,764 attainers. Exact-number and synonymous Pasch/quadrilateral/Fano searches found no covering prior. The result is therefore not a lookup or a direct specialization of a published theorem.

## Scientific value

**Verdict:** PASS  
The record supplies an exact extremal invariant on a classical catalogued symmetry class, together with prevalence data and an explicit extremal witness. The Fano restriction changes the minimum from 0 to 7, so the result captures a real structural interaction rather than merely reprinting a catalog count. The unfinished per-isomorphism-type attribution is appropriately excluded from the headline.

## Evidence

- [Mathon–Phelps–Rosa, A class of Steiner triple systems of order 21 and associated Kirkman systems](https://doi.org/10.1090/S0025-5718-1981-0616374-9): Classifies the tricyclic STS(21) family and studies resolvability/invariants, but does not state the Fano-restricted Pasch minimum or labeled counts audited here.
- [Heinlein–Östergård, Steiner Triple Systems of Order 21 with Subsystems](https://arxiv.org/abs/2104.06825): Classifies all STS(21)s with sub-STS(7), a much broader universe, without the joint tricyclic/Pasch extremum.
- [Erskine–Griggs, Properties of Steiner triple systems of order 21](https://arxiv.org/abs/2401.13356): Surveys the 62,336,617 symmetric STS(21)s and many configurations; no covering Fano-restricted tricyclic Pasch-minimum theorem was found.

## Independent checks

- Independent exhaustive exact-cover enumeration reproduced 135128 total solutions, 61040 Fano-containing, restricted minimum 7, 1764 attainers, and unrestricted minimum 0.
- Witness block set and fixed-sigma closure were independently checked.
- Current main directory tree SHA exactly equals the assigned tree SHA; no GitHub writes were made.

## Limitations

- The shipped verify_labeled.py expects raw_solutions.json, which is absent from the current artifact inventory; the exhaustive result was therefore independently regenerated rather than reproduced by that script alone.
- The record does not provide the complete 97-type attribution table; only the numerical type-level minimum follows by invariance.

## Repository action

This audit is a guarded change-set only. Source tree `ff023988648557102d5ac94a878674de3f897cde` still matches current `main`; no GitHub write was performed by this audit.
