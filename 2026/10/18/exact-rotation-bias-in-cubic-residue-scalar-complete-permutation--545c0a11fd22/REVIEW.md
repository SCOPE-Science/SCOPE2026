# Mathematical assessment: exact rotation bias in cubic-residue scalar complete permutations

## Correctness — PASS

For every prime power \(q\equiv1\pmod9\), the proof uses the multiplicative subgroup \(K\) of size \(s=(q-1)/3\) and counts *all* functions \(c:\mu_3\to K\) once. Since \(\mu_3\subset K\), the transformation \(a_u=u^kc(u)\) is a bijection of three coordinate copies of \(K\). The polynomial \(f_c\) always permutes its own fibers, while \(f_c+X\) is a permutation precisely if the nonzero scalars \(1+a_u\) induce a permutation of the three fibers. A direct index calculation identifies three rotation patterns and three transposition patterns. Cubic-character orthogonality gives the exact integer populations \(N_j\), and the known Jacobi absolute-value identity proves their positivity for all allowed sizes. The cubic identity proves \(R_q-T_q=(q-4)|J-2|^2/27>0\); the normalized second-order coefficients are obtained by explicit expansion, not numerical extrapolation. The standalone verifier separately exhausts all multipliers and all field inputs over four finite fields (including \(\mathbb F_{64}\)) and checks character sums in eight fields. No finite test is used as proof of a universal statement.

## Originality — PASS, qualified by inaccessible literature

The recent scalar-fiber theorem of Bouyacoub–El-Baz–Kihel provides the admissible family and a sufficient construction based on constant fiber shifts, but no six-permutation enumerative formula or exact rotation/transposition bias. Fear–Wanless give the general cyclotomic orthomorphism criterion and a count of near-linear orthomorphisms, not the complete coefficient-constrained spectrum. Cubic cyclotomic-number literature explains how the local \(N_j\) can be expressed using Jacobi sums, but does not identify the global three-fiber bias. Searches of accessible mathematical literature and mathematical research records found no statement of the exact identity. **Important unresolved overlap:** Bell (2013) explicitly counts all index-three cyclotomic orthomorphisms for certain prime powers; its abstract was available, but its full text could not be accessed without an unavailable approval step. That broader total-count result does not, from the material accessible, imply the restricted rotation-vs-transposition difference, but an equivalent refinement could be present in the inaccessible paper. This risk should be independently checked before publication.

## Mathematical value — PASS

The source's concrete CPP construction uses only the three constant-shift permutations. The remaining three fiber types are equally natural but receive no numerical or structural comparison there. The result provides a complete finite-field family count and proves a **strict arithmetic symmetry bias** between these types, with an exact nonnegative Eisenstein/Jacobi norm controlling the excess and a universal \(q^2/27\) main scale. This directly answers how numerous genuinely nonconstant fiber actions are within the scalar CPP family; it is not a change of notation or an arbitrary parameter slice. The global normalized \(2/9-5/(3q)\) coefficient is sharper than just a limiting probability.

## Closest sources and limits

1. Bouyacoub, El-Baz, Kihel, arXiv:2603.03368, sections 4–6, publicly posted 2026-03-02: read complete HTML text, especially Theorem 5.1 and Corollary 5.3.
2. Fear and Wanless, *Existence results for cyclotomic orthomorphisms*, arXiv:2101.00859, Section 2 and Theorem 1: read HTML; general fiber criterion and near-linear count.
3. Bell, *Cyclotomic orthomorphisms of finite fields*, Discrete Applied Mathematics 161 (2013), DOI 10.1016/j.dam.2012.08.013: bibliographic metadata and abstract only, relevant full text inaccessible; unresolved possible implicit enumeration overlap.
4. *Ternary cyclotomic numbers and ternary Jacobi sums*, AIMS Mathematics (2024), DOI 10.3934/math.20241292: bibliographic/abstract information; background local character data.

The result does not concern unrestricted index-three cyclotomic coefficients or arbitrary exponents. More comprehensive literature comparison and independent verification remain advisable.

Self-review: passed. Independent audit: not yet performed.
