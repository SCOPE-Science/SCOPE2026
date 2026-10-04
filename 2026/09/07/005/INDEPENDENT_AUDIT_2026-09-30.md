# Independent audit — 2026-09-30

## Final claim assessed

The complete nonlinearity histogram of all 1,048,576 seven-variable rotation-symmetric Boolean functions is the stated 33-value distribution, with maximum nonlinearity 56 attained by 11,788 functions; the listed extremal representatives and the stated 11- and 12-class affine-inequivalence lower bounds follow from the enumerated spectra and invariants.

## Correctness — PASS

An independent construction of the 20 rotation orbits reproduced the exact orbit minima. A fresh exhaustive batched integer Walsh-Hadamard enumeration over all 1048576 orbit masks reproduced every histogram cell, including 11788 at nonlinearity 56 and 22344 at 55. Independent Mobius/Walsh checks reproduced the two quoted representative masks, ANF masks, degrees, weights and absolute spectra. Recomputing degree, absolute-Walsh multiset and nonzero autocorrelation maximum for all 34132 functions at nonlinearity 55 or 56 yielded exactly 11 distinct invariant triples for the maximizers and 12 for the next-maximizers, validating the lower bounds on affine classes.

Evidence inspected:
- RESULT.md
- artifacts/generator_rsbf7.c
- artifacts/second_impl_verify.py
- independent exhaustive integer FWHT/Mobius census

Residual risks:
- The affine-class statements are lower bounds only; no exact affine orbit classification is claimed.

## Originality — PASS

Stănică-Maitra 2008 already proves the existence of seven-variable rotation-symmetric functions with nonlinearity 56 and counts 1712 one-resilient examples, so the maximum value 56 by itself is prior art. The inspected prior work does not provide the full 1,048,576-function nonlinearity histogram, the total 11788 maximizer count, the canonical per-nonlinearity representatives, or the 11/12 invariant-class lower bounds. Exact-number and semantic searches found no earlier matching census; Published-record search found this record and related lower-dimensional RSBF censuses only.

Sources inspected:
- Stănică and Maitra, Discrete Applied Mathematics 156 (2008), DOI 10.1016/j.dam.2007.04.029
- Kavut-Maitra-Yucel, ePrint 2006/449 and related RSBF search literature

Residual risks:
- A thesis or supplemental computation could contain an unpublished full seven-variable histogram; priority is asserted only for the complete census components, not for existence of nonlinearity-56 RSBFs.

## Scientific value — PASS

A complete exact census of a natural cryptographic function class is a reusable benchmark: it gives the entire distribution, exact extremal multiplicities, canonical representatives, and invariant-based diversity information. Exhaustive finite work is justified here because the class has a canonical 20-orbit parametrization and the result closes the finite classification rather than reporting a sample.

Context checked:
- RESULT.md
- rotation-symmetric Boolean-function literature

Residual risks:
- The class is restricted to rotation symmetry, and the result does not classify affine orbits exactly.

## Outcome

All three acceptance axes pass for the final claim as stated. Conjectures, heuristic search observations, and explicitly excluded broader regimes remain outside the accepted claim.
