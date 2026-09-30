# Independent audit — 2026/09/12/060
Assigned/current tree: `7d8727dea88ad8aa475a3bc3ed13f526f6549509`  
Disposition: **repaired**

## Correctness

The value -7/8 is correct under the standard small-J convention. For beta=4H-2E1-E2-E3 the toric divisor pairings are (2,1,1,2,1,1), so the factorial denominator is 4. Expanding the beta-term of the toric I-function gives (1/4)z^-7-(1/4)S z^-8+..., with S=(7/2)H-(1/2)E1-(3/2)E2-(3/2)E3. Hence the H coefficient at z^-8 is -7/8, which is the coefficient dual to the insertion H in the one-point J-function. The degree-one effective toric classes have a negative toric-divisor pairing, so they contribute at order z^-1 rather than to the z^0 mirror map; no correction changes this coefficient.

## Originality

The method is standard toric mirror symmetry. Focused searches located general toric mirror theorems and descendant frameworks but not this exact class/insertion/value. Search non-detection is not a priority proof; originality is limited to an explicit benchmark computation.

## Scientific value

The exact value is a useful regression datum for toric Gromov-Witten software and hand calculations, but it is not a new mirror theorem or structural result.

## Independent checks

- Recomputed all six divisor pairings, factorial denominator, harmonic sum, effectivity identity, and J/I coefficient.
- Checked that c1=1 toric classes do not contribute a z^0 mirror-map term.

## Limitations

- The record-referenced output/artifacts/mirror_check.py and verify_all.py are absent from the audited Git tree; they were not treated as read or executed.
- The audit verifies the coefficient extraction, not the full published proof of the toric mirror theorem.
- No exhaustive literature search can establish priority for a single numerical invariant.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/12/060
- https://arxiv.org/abs/1310.4163
- https://doi.org/10.2140/gt.2017.21.315
- https://arxiv.org/abs/1612.02402
