# Independent Audit — 2026/09/10/033

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `285b1708cd8af9b669a470353b5e146859b6bf46`
- Disposition: **PASSED**

## Correctness

**PASS** — Independent direct pattern-matching enumeration reproduces U=394, C1=C2=393 at n=6; U=1806, C1=1781, C2=1785 at n=7; and U=8558, C1=8224, C2=8308 at n=8. The two stated length-7 witnesses were independently checked to be separable and to lie on opposite sides. The n=7 difference census 21 versus 25 also reproduces. These finite certificates alone prove non-Wilf-equivalence and that n=7 is the first separating index.

## Originality

**PASS** — Exact-basis searches and exact count/witness searches found no indexed source stating this constrained separable-cell split or its 1781/1785 counts. The nearby Albert–Atkinson–Vatter theorem is a general structural result and does not supply this cell verdict. No database/table match was located for the exact two bases.

## Scientific value

**PASS** — A first-separation certificate for a concrete Wilf cell is a reusable classification datum: it settles equivalence without relying on asymptotic inference, supplies explicit two-sided witnesses, and gives independently reproducible initial enumerations. The n=10..12 extension is secondary to the decisive n=7 certificate.

## Limitations

- This run independently recomputed the decisive range only through n=8; the deposited n=9..12 sequence was not re-executed here.
- No growth-rate separation follows from the finite census.
- Originality search cannot logically exclude an unindexed thesis or private table; no exact indexed prior was found.

## Sources

- Subclasses of the Separable Permutations: https://arxiv.org/abs/1007.1014 — Nearby structural literature; does not state the exact cell split.
- PermPAL: https://permpal.com/ — Pattern-avoidance database checked for exact-basis coverage; no exact matching entry surfaced in this run.

This audit is independent of the record's pre-existing AUDIT.json. GitHub was read only as evidence; no repository mutation was performed in this audit chat.
