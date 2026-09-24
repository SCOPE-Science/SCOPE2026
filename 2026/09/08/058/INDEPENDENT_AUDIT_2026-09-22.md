# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/058`  
**Audit date (UTC):** 2026-09-24  
**Reviewer:** separate AI audit; not Lean verification or expert attestation.

## Source identity and original claim

The audited source directory has tree SHA `3bbd7c3814f9f0b122335d19a64b559a0b2fa8d8`; audited `RESULT.md` blob `01af71f940091adf269b153a314f6ce59a612025`.

The record combines a complete ordered Kronecker-coefficient atlas through n=10, a seven-point Murnaghan ray through n=12, and an n=10 maximum/argmax certificate.

## Correctness — PASS

I independently generated irreducible symmetric-group character tables by a separate Murnaghan–Nakayama implementation and checked character orthogonality before using them. Exact class-sum inner products were then exhaustively evaluated for every ordered partition triple through n=10.

The independent totals exactly reproduced the record:
nonzero counts `1,4,11,43,143,511,1599,5048,14294,40860` for n=1..10; maxima `1,1,1,1,2,5,9,17,28,117`; the stated argmax multiplicities/families; and the unique n=10 maximizing triple `((4,3,2,1)^3)`. The ray `((n-3,2,1),(n-3,2,1),(n-2,1,1))` gave exactly 4 for every n=6..12. Thus the computational claims pass independently.

## Originality — REPAIR REQUIRED, then PASS for the residual contribution

A targeted search for the n=10 maximum found decisive prior art missed by the record's reference comparison. Jonah Blasiak, *Kronecker coefficients for one hook shape* (arXiv:1209.2018, 2012; SLC 2017), introduction, explicitly says: “the maximum size of a Kronecker coefficient for n=10 is 117.” Therefore the numerical fact `M(10)=117` cannot be presented as an unpublished discovery.

I found no source among the checked stability literature or computational literature that publishes the same complete ordered atlas through n=10 together with the stated ray through n=12 and the unique maximizing triple/certificate. The bounded repair therefore preserves the atlas, ray, and independent argmax certification while explicitly identifying 117 as prior art and removing any novelty implication for that value.

## Scientific value — PASS after repair

The surviving contribution is more than the already-known scalar maximum: it supplies a complete exact small-n coefficient dataset, independently certified zeros/nonzeros and argmax families, an explicit constant Murnaghan ray, and a reproducible certificate for the unique n=10 maximizing triple. These are useful regression/benchmark data for Kronecker-coefficient algorithms and stability experiments. The repair makes the boundary between prior fact and new certification explicit.

## Repair

`RESULT.md` is revised to:
1. cite Blasiak's prior statement `M(10)=117`;
2. stop claiming novelty for that value;
3. phrase the n=10 section as a certification of the known maximum plus a unique argmax witness;
4. retain the independently verified atlas/ray claims and all computational limitations.

No numerical data or theorem statement needed correction.

## Disposition

**REPAIRED / PASSED.** Correctness passes; the original novelty framing had a material prior-art omission, but a bounded wording/reference repair yields a correct, qualified, useful record.

## Access notes

Blasiak's full arXiv HTML was lawfully accessible and the decisive statement appears in the introduction (arXiv:1209.2018, introduction, paragraph reporting the n=10 computer experiment). No Oxford fallback was required.
