# Independent Audit — 2026/09/10/021

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `da03010b6123a123338452ee432ca27658a8451d`  
**Disposition:** **PASSED**

## Correctness

The identity is correct. Recomputing the double Schubert polynomial from divided differences, setting y=1, reflecting variables, and evaluating the five Lascoux atoms gives exact cancellation R_2143-(L_4343+L_4442-L_4344-2L_4443+L_4444)=0. The lowest degree is 14 and the graded signs +,-,+ agree with the stated convention.

## Originality

Setiabrata–St. Dizier prove the reflected graded Lascoux positivity statement for vexillary (2143-avoiding) permutations and formulate the all-permutation extension as a conjecture. The permutation 2143 is the minimal non-vexillary case and lies outside their theorem. No expansion for 2143 appears in the inspected source, so this exact coefficient list is a genuine boundary-case verification rather than a covered instance.

## Scientific value

As the smallest case beyond the proven vexillary domain, the expansion is a useful exact test of the all-permutation conjecture and a compact regression/induction datum. It does not prove the broader single-2143-cell or all-permutation conjecture, but the base case is scientifically meaningful.

## Limitations

- Only w=2143 is proved; no larger pattern class follows.
- Machine algebra is used for the explicit basis expansion, though the identity is exact and independently replayable.

## Evidence

- [Setiabrata–St. Dizier, Double orthodontia formulas and Lascoux positivity](https://arxiv.org/abs/2410.08038): Theorem covers vexillary/2143-avoiding cases; the general statement is a conjecture. The inspected text contains no explicit 2143 expansion.
- [Orelowitz–Yu, Lascoux expansion of the product of a Lascoux and a stable Grothendieck polynomial](https://arxiv.org/abs/2312.01647): Related Lascoux expansion theory but not the reflected-Schubert coefficient list audited here.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `da03010b6123a123338452ee432ca27658a8451d`; no repository writes were made by this audit.
