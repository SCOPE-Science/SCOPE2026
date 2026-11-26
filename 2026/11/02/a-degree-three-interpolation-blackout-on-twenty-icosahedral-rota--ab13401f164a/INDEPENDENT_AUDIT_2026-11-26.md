# Independent mathematical audit

## correctness

PASS

Unitarity gives the unnormalized character Gram and the claimed (2ℓ+1)/20 multiplier after the two stated normalizations. Independent exact reproduction: `python3 /workspace/review-work/icosahedral_charpoly.py` generates the two 3-cycles per three-element support, assigns five-cycle classes using conjugator parity, generates characters by the rotation-character recurrence, and uses 20 exact power traces, Newton identities and exact root extraction for each characteristic polynomial. This reproduced all the spectra in degrees 0–9. It tested the algebraic Gram, not continuous Wigner matrices. The A5 five-dimensional block is D² restricted to A5; multiplicity by character inner product is (2ℓ+1+3(−1)^ℓ−4c_ℓ)/12, strictly positive for ℓ≥4. Its full sampled image therefore persists. The source's Gershgorin sentence gives a weak inequality at the stated numerical lower bound, so strictness was checked separately, without changing the finding: equality requires saturated row sums, hence ℓ≡1 or 3 mod 5 and c_ℓ=±1. All off-diagonal entries are then nonzero and a real equality eigenvector must have equal nonzero coordinate magnitudes and opposite signs exactly across positive edges. The positive-edge graph would be complete bipartite; it is regular by the class counts and has positive edges, so each part must have size 10. Positive degree is 3+6 times the indicator of a positive order-two value plus 7 times the indicator of a positive order-three value. Degree 10 requires the order-three value to be positive, but (123),(124),(125) form a positive triangle: each pairwise relative product has order three. This rules out equality and gives the stated strict bound.

## originality

PASS

The strongest prior Resultary theorem actually covers rank 16 for the four-dimensional standard S5 block on the same twenty nodes. It does not give the image of the additional three-dimensional constituent of D³ or the full degree-three spectrum, nor full interpolation by the distinct degree-two block and its permanent persistence. The twelve-node fivefold analogue and cumulative SO(3) sampling are distinct. The full exact-degree rank law, its notable loss of rank, and the Gram result remain supported as distinct on the inspected evidence.

## value

PASS

The order-three class is an intrinsic symmetric sampling set, not a selection optimized after computation. The exact rank is the feasibility criterion for interpolating arbitrary data at a single Wigner degree, and the rank drop after full interpolation distinguishes this question from routine nested-band sampling. The low-degree spectra further quantify conditioning, and the branching argument explains why full interpolation then persists indefinitely.

The dated certificate retains the supplied scientific assessment, sources and limitations.
