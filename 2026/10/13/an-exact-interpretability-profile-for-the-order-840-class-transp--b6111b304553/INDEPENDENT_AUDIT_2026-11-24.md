# Independent mathematical audit

## correctness

PASS

Checked the χ table, overlap rule, integer-chain equations and same-parity distinctness against Iskra §3. Equivalently, after χ(XY) the next letter must start at the partner of Y in its transposition; there are two choices. Each next index is a rational affine function of the original integer index. Its integrality gives one linear congruence; after reducing each, the whole system is solvable iff the residue differences are divisible by the pairwise gcds of the moduli. On a nonempty solution progression, nonidentical affine forms at same-parity positions exclude at most one value per pair, while identical ones preclude exactness. An independent exact implementation, replayed as `python3 /workspace/branches/independent-checks.py 5`, obtained total counts 8,16,32,64,128,256,512, both interpretation counts 8,8,8,6,4,2,0, and precisely LqRpQl and LqPrQl at length six. At length seven integer infeasibility implies exact infeasibility, which is the hypothesis actually used in Theorem 6.4. Direct application of b then a reconstructed all four recorded cycles on distinct integers. Theorem 7.1 gives the reverse divisibility once finiteness holds, so the order is 840. With lengths at most eight, the factors 8, 5 and 7 force three separate lengths and the factor 3 forces a fourth. This is minimality only for individual-cycle certificates under that bound. Read the frozen verification, checker and stored output; this replay did not execute the uploaded checker and makes no Lean or expert-attestation claim.

## originality

PASS

The order, the source theorems, existence of the relevant cycle lengths, and the elementary factor-count argument are not credited as new. The distinct supported content is the exact integer and exact-interpretation census, the concrete terminal words, and the explicit point-cycle data giving a check without RCWA. No examined prior statement supplies or forces those data merely from the already-known order or the aggregate cycle lengths.

## value

PASS

This is the extremal example chosen by the source for the universal bound, not an arbitrary small pair. Its exact depth-six survivors and the obstruction to even integer interpretation at depth seven give a useful benchmark for the interpretation test, stronger than checking the known order. The short explicit cycles furnish a checkable lower-bound certificate without the original RCWA computation. Recomputing order 840, or the elementary minimum of four alone, would not justify acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
