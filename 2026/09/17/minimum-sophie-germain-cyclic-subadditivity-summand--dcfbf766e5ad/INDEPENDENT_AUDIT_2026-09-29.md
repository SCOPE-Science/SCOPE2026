# Independent audit — 2026-09-29

**Record:** `2026/09/17/minimum-sophie-germain-cyclic-subadditivity-summand--dcfbf766e5ad`  
**Audited source tree:** `ca7595171fbbb8a73f0f9eccb89becbbd64d116f`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** PASSED

## Correctness

PASS. For cyclic r>2, evenness is impossible because phi(r) is even, and a square factor p^2|r would force p|gcd(r,phi(r)); hence a Sophie Germain cyclic a>2 is odd and both a and 2a+1 are squarefree. Modulo 18 this excludes the odd residues 9 (9|a) and 13 (9|2a+1), leaving {1,3,5,7,11,15,17}. I independently recomputed the maximum occupancy of these residues in windows of lengths 1 through 21, the exact initial values C_sigma(m) through 21, and the witness window (87088,87109]. The tables agree with the record: M(m)<=C_sigma(m) for every m<=20, while C_sigma(21)=8 and the length-21 witness contains exactly nine Sophie Germain cyclic integers. Direct totient/gcd checks verified all nine witness integers and their transforms 2a+1. Therefore no counterexample can have smaller summand <=20 and (21,87088) proves sharpness.

## Originality

PASS, qualified. Ibarra's July 2026 counterexample uses smaller summand 31, and current searches for the exact witness 87088, the value 21, and the mod-18 packing argument found no prior or subsequent source stating the sharp minimum. Cohen's original conjecture and OEIS provide the underlying sequence but not this extremal window theorem. The priority claim is necessarily qualified because the topic is recent and the sharpening is elementary once the residue obstruction is noticed.

## Scientific value

PASS. The result turns an existence counterexample into an exact extremal statement: it proves a global lower bound for every possible counterexample and supplies a sharp witness. The short congruence-packing proof is reusable and materially sharpens the previously published m=31 example.

## Evidence and literature

- https://arxiv.org/abs/2508.08335 — J. E. Cohen, Conjectures about Primes and Cyclic Numbers; source of the Sophie Germain cyclic counting-function conjecture.
- https://arxiv.org/abs/2607.09793 — J. A. Ibarra, A counterexample to a subadditivity conjecture of Cohen for Sophie Germain cyclic numbers; gives the earlier counterexample (m,n)=(31,3928).
- https://oeis.org/A397387 — OEIS sequence of Sophie Germain cyclic numbers; background/checking source.

## Limitations

- The theorem minimizes the smaller summand under 1<=m<=n; it does not minimize n, m+n, or another size functional.
- The originality search cannot exclude an unindexed contemporaneous note; no such overlap was located through 2026-09-29.

## Audit conclusion

All three audit axes pass. No substantive research-file correction is required. This audit changes only the independent-audit verification channel and does not alter Lean or expert-attestation channels.
