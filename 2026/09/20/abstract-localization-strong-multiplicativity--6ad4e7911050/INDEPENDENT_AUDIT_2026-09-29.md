# Independent Audit — 2026-09-29

**Record:** `2026/09/20/abstract-localization-strong-multiplicativity--6ad4e7911050`  
**Title:** Abstract localization rings do not characterize strong multiplicativity  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `3bc828fe320769fb0126ef284ab808c0a0dfde40`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. For R=k[x] x C with C=(k[x,x^{-1}])^N, T={1,e} is strongly multiplicative while S={(x,1)^n} is not, since intersection_n (x^n k[x] x C)=0 x C and no element of S lies there. Yet R_T is C and R_S is k[x,x^{-1}] x C, which is abstractly isomorphic to C by shifting the countable product. The spectral distinction is also correct: D(S)=D_{k[x]}(x) disjoint-union Spec(C) is not clopen, while D(e)=Spec(C) is clopen. Requiring the isomorphism R_S -> Re to be under R repairs the issue; directly, e=1 in R_S forces some t in S to annihilate 1-e, and invertibility of every se in Re puts e in every sR, so that t=te belongs to S intersect intersection_s sR.
- **Originality — PASS:** PASS, with source-wording qualification. The current Kim--Koc arXiv abstract states the intended equivalence as 'R_S is the localization at an idempotent' and is still v1. The audited record supplies a concrete separation between that marked localization notion and mere abstract ring isomorphism; targeted searches did not locate this counterexample elsewhere. The arXiv full theorem text was not independently retrievable in this run, so the audit does not overstate the precise wording of Theorem 2.6 beyond the repository evidence and public abstract.
- **Scientific value — PASS:** PASS. The example isolates a real categorical distinction: the abstract isomorphism type of a localization forgets its embedding of the base ring. The correction is concise, reusable, and prevents a false converse if an unmarked ring-isomorphism formulation is used, while leaving the valid map-compatible theorem intact.

## Independent findings
- The non-strong family is witnessed explicitly by the powers of s=(x,1), whose principal ideals have intersection 0 x C.
- The absorbing countable product gives an explicit unital isomorphism k[x,x^{-1}] x C ~= C.
- The two localization spectra embed differently in Spec(R), so an abstract homeomorphism cannot identify D(S) with D(e).
- The map-compatible converse can be proved directly from the universal localization map, without relying on the disputed abstract-isomorphism step.

## Independent checks
- Recomputed both localizations and the intersection of the principal ideals s^nR.
- Checked the coordinate-shift ring isomorphism B x B^N ~= B^N and its unit preservation.
- Checked the clopen/non-clopen spectral embeddings using idempotents of k[x].
- Compared against the current arXiv v1 abstract and searched for an independently published version of the same counterexample.

## Literature evidence
- https://arxiv.org/abs/2609.16741 — Kim--Koc v1; public abstract states equivalence with localization at an idempotent, arbitrary-intersection preservation, and clopen D(S).
- https://arxiv.org/abs/2512.23935 — Superseded predecessor on strongly multiplicative sets, included as historical context.
- https://doi.org/10.1007/s13366-019-00476-5 — Hamed--Malek background on S-prime ideals; not a source for the present abstract-isomorphism separation.

## Limitations
- The arXiv full text for 2609.16741 could not be independently rendered in this run; the public abstract was accessible, while the exact theorem wording is supported by the audited repository record rather than a separately rendered source page.
- The map-compatible formulation is standard localization language; originality is only claimed for the explicit separation/correction.
- The counterexample uses a countably infinite product and does not address Noetherian or finite-product restrictions.

The assigned source tree was unchanged between inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` and audited commit `253a0fe5d0217455660a277f9adb940030e567ad`; the assigned tree SHA therefore remains the exact current tree audited. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC as required by the task-specific audit contract.
