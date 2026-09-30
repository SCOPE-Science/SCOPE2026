# Independent audit — 2026-09-30

**Record:** `2026/09/21/lucas-carmichael-ap-prime-triple-parametrization--0e46ab047f14`  
**Audited source tree:** `8d57819198d842fdf1bd4f324ba3ff11ba290578`  
**Disposition:** passed

## Correctness — PASS

PASS. With h=q+1 and common difference d, direct reduction of p+1|n+1, q+1|n+1, r+1|n+1 gives h-d|d(2d-3), h|d^2, and h+d|d(2d+3). Writing h=gu, d=gv with (u,v)=1, the middle divisibility forces u|g; setting g=uw yields h=u^2w and d=uvw and hence the displayed three linear prime forms. The outer conditions reduce to u-v and u+v dividing 2v^2w-3. Same parity is impossible; opposite parity makes u-v and u+v coprime, so the two conditions combine exactly to u^2-v^2 | 2v^2w-3. The converse reverses the steps and uniqueness follows from reduced h/d=u/v. The fixed-shape residue class exists because gcd(2v^2,u^2-v^2)=1. I also independently enumerated all prime arithmetic-progressions with largest prime <=10000: 59,504 triples, 46 direct Lucas--Carmichael triples, 46 parametrized triples, and zero mismatches; the repository artifact reports a larger independent bounded check with zero mismatches.

## Originality — PASS

PASS, with ordinary recreational-number-theory priority qualification. Wright's open work establishes the definition and infinitude of Lucas--Carmichael numbers, and OEIS records the known (6m-1,12m-1,18m-1) subfamily; the filed result explicitly treats that 2:1 ray as prior. Searches for arithmetic-progression prime-factor classifications, the normalized divisibility u^2-v^2 | 2v^2w-3, and the displayed parametrization did not locate an equivalent theorem. A 2023 Lucas--Carmichael characterization and the 2024 three-prime strong-Lucas-test literature address adjacent questions but do not advertise this AP classification. Older Guy/sequence/recreational sources not fully inspected remain a residual risk, so originality is appropriately stated to the best of knowledge rather than absolutely.

## Scientific value — PASS

PASS. The theorem converts a three-prime Lucas--Carmichael divisibility problem with an arithmetic-progression constraint into a complete primitive-shape parametrization and one explicit congruence ray per shape. It explains a known family as one member of a systematic classification and produces a clean Dickson-conjecture consequence. The exact bounded checks support, rather than replace, a complete elementary proof.

## Independent checks

- Re-derived all three reduced divisibilities from the Lucas--Carmichael condition.
- Reversed the gcd normalization to prove sufficiency and uniqueness.
- Checked the fixed-shape congruence and parity lift.
- Ran an independent prime-AP enumeration through 10000 and compared direct divisibility with the parametrization.

## Literature evidence

- https://arxiv.org/abs/1609.00231 — Wright, open preprint proving infinitude of Lucas--Carmichael numbers and supplying baseline prior theory.
- https://oeis.org/A290810 — OEIS entry for the known (6m-1,12m-1,18m-1) prime triple family, explicitly excluded from the novelty claim.
- https://arxiv.org/abs/2311.08012 — Tamilvanan and Muthukrishnan (2023), a different Lucas--Carmichael characterization by base-p digit sums.
- https://doi.org/10.1007/s10623-023-01347-w — Einsele and Paterson (2024), adjacent three-prime/strong-Lucas-test literature.

## Limitations

- Originality remains qualified against older recreational and poorly indexed number-theory sources not exhaustively inspectable.
- The infinitude per fixed shape is conditional on Dickson's conjecture; no unconditional fixed-shape infinitude is claimed.
- The classification assumes exactly three distinct odd prime factors in arithmetic progression.

No GitHub write was performed by the audit chat. The guarded publication plan stages only this audit evidence and the independent-audit verification channel.
