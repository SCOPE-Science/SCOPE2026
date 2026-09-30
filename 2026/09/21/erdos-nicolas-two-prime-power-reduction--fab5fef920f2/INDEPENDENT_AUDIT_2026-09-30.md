# Independent Audit — Prime-power odd parts in Erdős–Nicolas initial-divisor sums

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `5264804ba43eaa6e43f71b17b33d6d4d6c35b008`  
**Audited current source tree:** `5264804ba43eaa6e43f71b17b33d6d4d6c35b008`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

GitHub was used only as read-only evidence. A repository comparison from the assignment inventory snapshot to the audited current `main` commit found no file changes under this record, so the audited tree equals the assigned source tree. The `INDEPENDENT_AUDIT_2026-09-30.md` and `.json` marker files were absent before this guarded plan was prepared.

## Correctness — PASSED

PASS. The ordered-divisor layer arguments are sound. For b=1, writing the cutoff by the largest included powers in the p^0 and p^1 layers reduces the prefix equation to a divisibility relation and leaves only the Mersenne-perfect family plus (a,p)=(3,3), i.e. 24. For b=2, parity of the nonempty p-adic layer sums forces exactly two layers; their total is <4x with x<p^2, forcing a=1, after which even all divisors below p^2 sum to less than 2p^2. If p>2^a, complete p-adic block ordering and reduction modulo p force p=2^{a+1}-1 and then b=1. For b>=3, the proof that the first binary layer is complete, p divides M=2^{a+1}-1, the last complete layer h satisfies h<=v_p(M)-1, and incomplete binary exponents strictly decrease gives s+1<=a+v; the s<b alternative contradicts size bounds, yielding b odd and b<=a+v-1. Independent brute enumeration for a<=8, p<=200, and b<=5 found no violation of Theorems 1–4.

## Originality — PASSED

PASS, narrowly scoped. Erdős–Nicolas (1975) introduced the partial-divisor-sum phenomenon and lists examples; current OEIS entries record the corresponding sequences and computational material. Targeted searches for 2^a p^b, prime-square odd parts, Mersenne specializations, and synonymous partial-divisor-sum formulations did not locate the submitted exact b=1 classification, b=2 exclusion, large-prime obstruction, or finite-per-a reduction for b>=3. No novelty is assigned to the original Erdős–Nicolas definition, perfect-number facts, or elementary p-adic/base-layer techniques.

## Scientific value — PASSED

PASS. The result isolates 24 as the unique nonperfect b=1 case, completely excludes the prime-square slice, and turns every higher-exponent two-prime-support case into a finite list for fixed a. That is a meaningful structural reduction of a sparse divisor-prefix problem, while the record correctly avoids claiming a complete classification for all b>=3.

## Independent checks

- Re-derived all four structural theorems and checked the strict inequalities used in the layer-size arguments.
- Independently brute-enumerated sorted divisor prefixes for modest ranges a<=8, p<=200, b<=5; all observed hits satisfied the submitted classification/necessary conditions and no b=2 hit occurred.
- Checked the small-a exclusions in Theorem 4 and the p-adic valuation argument for the last complete layer.
- Compared with the open Erdős–Nicolas 1975 source metadata/full-text access point and current sequence descriptions; no two-prime-power classification was located.
- Targeted web searches for equivalent 2^a p^b results found no covering prior statement.
- GitHub compare found no changes under the assigned record path; the dated audit pair is absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem does not eliminate every b>=3 case; it gives a finite candidate set for each fixed a.
- The record's a<=30 exhaustive computation is a bounded corollary and is not used as proof of the structural theorem.
- Poorly indexed older divisor-partition/problem literature remains the principal residual originality risk.

## Evidence and references

- https://doi.org/10.24033/bsmf.1793
- https://www.numdam.org/articles/10.24033/bsmf.1793/
- https://oeis.org/A064510
- https://oeis.org/A194472
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/21/erdos-nicolas-two-prime-power-reduction--fab5fef920f2

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
