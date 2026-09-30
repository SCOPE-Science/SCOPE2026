# Independent audit — 2026-09-29
- Source: `2026/09/12/057`
- Assigned/current tree SHA: `53b48bb1723e008796e3bfde0415e22974a25944`
- Audited repository commit: `eff2c6312cec5b0dee5115e5f42211a853092dfb`
- Disposition: **repaired**

## Three-axis assessment

### Correctness

**PASSED** — PASSED AFTER REPAIR. The exact helper-function census is correct: for ML-DSA-44 and each nonzero |z|≤78, exactly 44|z| residues r change HighBits under r→r+z; the union over all allowed nonzero shifts is 44 disjoint 156-point boundary neighborhoods (6864 residues), totaling 271128 flipping (r,z) pairs, and UseHint reconstructs every such one-step high-bit change. The original headline “ω=80 is exactly tight” was too strong because its 1024 arbitrary (r,z) coefficient pairs are not shown to arise from a valid ML-DSA key/message/signing execution.

### Originality

**PASSED** — SUPPORTED NARROWLY AFTER REPAIR. FIPS 204 and the Dilithium literature define Decompose/MakeHint/UseHint and the ω cap, but the audit located no prior source tabulating this exact ML-DSA-44 per-coefficient boundary census (44|z|, 6864 residues, 271128 pairs). The repaired record claims only that helper-level combinatorics, not signature-level tightness.

### Scientific value

**PASSED** — The repaired result is a precise boundary-test invariant for implementations of the most error-prone rounding/hint helpers. It gives closed-form counts and an exhaustive oracle for edge-case testing while explicitly separating helper-function attainability from the much stronger question of whether an honest/valid signature can realize hint weight 80.

## Independent checks

- current main record tree exactly equals the assigned source-tree SHA
- reviewed census_script.py and independently checked the boundary-count formula 44|z|
- checked 2×44×sum_{z=1}^{78} z = 271128 and 44×156 = 6864
- reviewed witness_script.py and confirmed it constructs arbitrary coefficient pairs, not an ML-DSA Sign execution
- compared the construction with FIPS 204 signing, where h=MakeHint(-c t0, w-c s2+c t0) and z/signature components are algebraically and hash-coupled

## Limitations

- The repaired claim is only about coefficientwise Decompose/HighBits/MakeHint/UseHint behavior under arbitrary shifts |z|≤78.
- It does not prove that hint weight 80 occurs for any valid ML-DSA-44 signature; signing couples coefficients through A, secret polynomials, the challenge c, rejection sampling, and the Fiat–Shamir hash.
- The synthetic 80/81 coefficient vectors remain useful helper tests but must not be described as valid signatures or signing transcripts.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/057
- https://csrc.nist.gov/pubs/fips/204/final
- https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf
- https://pq-crystals.org/dilithium/data/dilithium-specification-round3-20210208.pdf
