# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/08/003`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `82e7203f0c4500b31b350eaf2fc9e06a99f4fdbd`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

A complete Betti-table census for Artinian monomial ideals in four variables with Hilbert function (1,4,10,5), including the 1752 cubic-generated slice and all 15504 ideals with generators through degree 4.

## Correctness — PASSED

Independent monomial enumeration reproduced the cubic-slice h4 distribution 1752/2124/468/24. A separate Koszul/Tor computation reproduced exactly 10 Betti tables on the 1752 terminating cubic-generated ideals with the stated frequencies, 80 S4-orbits and no Borel-fixed cases. Extending to all C(20,5)=15504 monomial ideals in the stated Hilbert stratum reproduced exactly 48 Betti tables and the archived frequency multiset. Euler checks and rational/modular rank checks agreed.

## Originality — PASSED

Pardue/Bigatti-Hulett type results determine extremal lex Betti data, and the literature discusses the general fixed-Hilbert-function realizability problem, but the audit did not locate a complete table-by-table census for this Hilbert function or its 15504 monomial ideals. The fixed-Hilbert-function census is therefore original relative to the checked sources; no novelty is attributed to Koszul homology itself.

## Scientific value — PASSED

The record closes a concrete realizability stratum with exact frequencies, witnesses, symmetry orbits and a larger full-stratum extension. It is a reusable test case for syzygy/Betti software and for conjectures about integral Betti tables at fixed Hilbert function, giving scientific value beyond a single computation.

## Search and independent checks

Independent checks:

- independent monomial survivor enumeration
- independent Koszul/Tor Betti computation and Euler identities
- S4 orbit and Borel-fixed recount
- full 15504-ideal extension

Literature/search queries:
- `Hilbert function 1 4 10 5 monomial Betti tables`
- `fixed Hilbert function Betti table census four variables`
- `Pardue Betti numbers Hilbert function monomial ideals`

Sources:
- https://doi.org/10.1215/ijm/1255985937
- https://doi.org/10.1216/jca-2009-1-1-159

## Final disposition

**PASSED.** The record remains accepted on all three audited axes.
