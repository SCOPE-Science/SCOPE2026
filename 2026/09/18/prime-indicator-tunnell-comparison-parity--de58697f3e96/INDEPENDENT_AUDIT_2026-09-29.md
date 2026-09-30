# Independent Audit — Prime-indicator parity in Tunnell-type comparison progressions

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `f2c8f4ed45dc5aaa10f3d29023a02f81c7665a09`  
**Audited current source tree:** `f2c8f4ed45dc5aaa10f3d29023a02f81c7665a09`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; no repository change was made during the audit.

## Correctness — PASS

PASS. Im–Shin Proposition 7.1 gives the normalized mod-(1+i) comparison for every index in Tables 8–9, while their Lemmas 7.2–7.3 establish odd comparator parity only at prime indices. For Q3=x^2+y^2+z^2, Gauss’s formulas and genus theory give 2^(omega(n)-1) | r3(n)/8 for odd square-free n≡3,5 mod 8, so the normalized value is even for every composite and odd for the source-prime rows. For Q135=x^2+3y^2+5z^2, the sign-orbit reduction r135(n)/4≡A(n)+B(n) mod 2 and the discriminant -12/-60 class analysis give the same prime-indicator parity on exactly the published rows; the 3m branch in the mod-40 row is handled by the stated bijections and the mod-5 condition. An independent signed-square enumeration through 100000 reproduced all 29,548 square-free row checks and the outside-row counterexamples r135(39)/4=3 and r135(111)/4=7. The valuation statement follows because v_(1+i)(2)=2.

## Originality — PASS

PASS, narrowly scoped. The full open Im–Shin preprint was inspected at Proposition 7.1, Lemmas 7.2–7.3, Theorem 7.4, and Tables 8–9. It uses comparator parity only for primes and does not state the prime-indicator law on all odd square-free indices or the resulting one-extra-(1+i) divisibility for composites. The three-square formula, genus theory, and binary-form facts are classical; originality is limited to the uniform row-by-row synthesis and the method-level obstruction it reveals.

## Scientific value — PASS

PASS. The theorem identifies exactly what the source’s first mod-(1+i) comparison can and cannot prove: on the published prime progressions it detects primality among square-free inputs, so the same comparison necessarily loses first-layer nonvanishing on every composite. This is useful negative structure that directs any composite extension toward higher (1+i)-adic information or a different comparator.

## Independent checks

- Read and visually checked the open PDF pages containing Proposition 7.1, Lemmas 7.2–7.3, and Tables 8–9.
- Re-derived the Q3 genus-divisibility argument in both n≡3 and n≡5 mod 8 cases.
- Rechecked the Q135 sign-orbit reduction, discriminant -12/-60 representation counts, and the n=3m exceptional branch.
- Independently enumerated signed representations through 100000 and reproduced exactly 29,548 valid square-free row checks with zero failures.
- Verified the outside-row values at 39 and 111 and the (1+i)-valuation consequence.
- Verified the current main directory tree SHA exactly equals the assigned source tree SHA.

## Limitations

- The parity theorem is confined to the twelve comparison rows of Im–Shin Tables 8 and 9; it is false as a global statement for r135.
- Extra (1+i)-divisibility does not imply Fourier-coefficient vanishing and does not by itself create new composite theta-congruent classifications.
- The source preprint is extremely recent, leaving residual unindexed-priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.19085
- https://doi.org/10.1002/9781118400722
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/prime-indicator-tunnell-comparison-parity--de58697f3e96

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
