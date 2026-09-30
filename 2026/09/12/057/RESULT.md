# Exact ML-DSA-44 per-coefficient MakeHint boundary census

## Context

FIPS 204 ML-DSA-44 uses `q=8380417`, `gamma2=(q-1)/88=95232`, `alpha=2*gamma2=190464`, and `beta=tau*eta=78`. The standardized `Decompose`, `HighBits`, `MakeHint`, and `UseHint` helpers implement rounding and one-bit carry correction. This record characterizes their coefficientwise boundary behavior exactly.

## Result

For residues `r in Z_q` and any nonzero integer shift `z` with `|z|<=78`:

1. `Decompose` has 44 high-bit blocks. One block has 190465 residues and the other 43 have 190464 residues.
2. For each fixed `z`, exactly `44*|z|` residues satisfy `HighBits(r) != HighBits(r+z mod q)`, equivalently `MakeHint(z,r)=1`.
3. Across all nonzero `|z|<=78`, the set of residues that can flip is exactly the disjoint union of the 44 intervals `[c_j-77,c_j+78]`, where `c_j=j*alpha+95232`. It contains `44*156=6864` residues.
4. The total number of flipping `(r,z)` pairs over `z=±1,...,±78` is `271128 = 2*44*(1+...+78)`.
5. On every flipping pair in the exhaustive census, `UseHint(1,r)=HighBits(r+z mod q)`; no reconstruction errors occur.

The committed scripts also construct a **synthetic coefficient-level test vector** with 80 flipping coordinates and a variant with 81. This is useful for testing helper and hint-weight boundary handling. It is **not** a proof that a valid ML-DSA-44 signature can attain hint weight 80.

## Proof

Let `H=alpha/2=95232` and `m=(q-1)/alpha=44`. Away from the standardized `q-1` fold, `HighBits` changes only when `r` crosses one of the 44 block tops

`c_j = j*alpha + H`,  `j=0,...,43`.

For a positive shift `z`, exactly `z` residues immediately below each boundary cross it, giving `44 z` flips. For a negative shift, exactly `|z|` residues immediately above each boundary cross in the opposite direction. Since `78 << alpha`, boundary neighborhoods do not overlap. Taking the union over all allowed shifts gives `[c_j-77,c_j+78]` at each boundary, 156 residues per boundary. Summing the fixed-shift counts gives

`2*44*sum_{z=1}^{78} z = 271128`.

The special `q-1` fold is handled by the FIPS 204 `Decompose` rule and is included in the exhaustive script. The resulting `UseHint` direction agrees with the new `HighBits` value on every enumerated flipping pair.

## What this does not show

A valid ML-DSA signature does not permit the 1024 coefficient pairs `(r,z)` to be chosen independently. During signing, the challenge is derived from the commitment, the response and hint inputs are coupled to the secret polynomials, and rejection sampling imposes additional vector constraints. Therefore a coefficientwise construction with 80 `MakeHint` ones does not establish signature-level attainability of `omega=80`. The original tightness claim is withdrawn.

## Reproducibility

- `artifacts/census_script.py` exhaustively enumerates every residue `r` and every nonzero `|z|<=78` and writes `artifacts/census.json`.
- `artifacts/witness_script.py` generates the synthetic 80/81 coefficient-level boundary tests and writes `artifacts/witness.json`.

## References

1. NIST FIPS 204, Module-Lattice-Based Digital Signature Standard (2024).
2. CRYSTALS-Dilithium specification, rounding and hint-correction lemmas.
