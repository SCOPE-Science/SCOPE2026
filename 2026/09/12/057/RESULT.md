# ML-DSA-44 hint-weight omega=80 is exactly tight: explicit attaining witness and exhaustive per-coefficient census

## Context
FIPS 204 (ML-DSA) standardizes three parameter sets. ML-DSA-44 (NIST level 2, Dilithium2) uses q=8380417, gamma2=(q-1)/88=95232, module ranks k=4, l=4, n=256, tau=39, eta=2, beta=tau*eta=78, and hint-weight bound omega=80. Signing compresses commitments via HighBits/LowBits decomposition with base alpha=2*gamma2=190464 and corrects rounding with MakeHint/UseHint bits. The verifier rejects any signature whose hint weight exceeds omega. FIPS 204 states the cap but does not exhibit a transcript attaining exactly 80 hints with full reconstruction correctness, nor a closed-form exhaustive census of flippable coefficients.

## Definitions
q=8380417, gamma2=95232, alpha=190464, H=alpha/2=95232, m=(q-1)/alpha=44 blocks, beta=78, k*n=1024 coefficients, omega=80. Decompose(r): rp=r mod q; r0=centered (rp mod alpha) in (-alpha/2,alpha/2]; if rp-r0==q-1 then (r1,r0)=(0,r0-1), else r1=(rp-r0)/alpha. HighBits(r)=r1, LowBits(r)=r0. MakeHint(z,r)=0 iff HighBits(r)==HighBits((r+z) mod q), else 1. UseHint(h,r)=r1 if h==0, else (r1+1) mod m if r0>0, (r1-1) mod m otherwise. A pair (r,z) with |z|<=beta is flipping if MakeHint=1. Transcript hint weight is the number of flipping pairs.

## Result
The bound omega=80 is exactly tight in the admitted sense: (a) there exists an explicit realizable 1024-coefficient transcript of pairs (r in Z_q, |z|<=78) whose standardized MakeHint outputs contain exactly 80 hints with zero UseHint reconstruction errors; (b) the verifier's explicit hint-count check rejects every transcript with more than 80 hints (demonstrated on an 81-hint variant). Supporting exact census: block histogram 190465+43x190464 summing to q; 44 block tops c_j=j*alpha+95232 (j=0..43); flippable set of exactly 6864=44*156 values equal to the disjoint union of [c_j-77,c_j+78]; per-shift flip counts exactly 44*|z| (z=+/-1 -> 44, ..., z=+/-78 -> 3432), total 271128 flipping (r,z) pairs; zero UseHint errors over all of them.

## Proof / Evidence
Exhaustive exact census over all r in Z_q and all shifts |z|<=78 with exact integer arithmetic (numpy-vectorized script, ~8 s): Decompose computed for every r with the q-1 fold Decompose(q-1)=(0,-1); block transitions verified at c_j+1; UseHint(1,r) compared against HighBits(r+z) on every flipping pair with 0 errors from 271128 pairs; flippable set identity verified by exact set equality against the union of neighborhoods; per-shift counts verified equal to 44*|z|. Explicit witness (stdlib-only independent scalar re-implementation): 40 pairs (c_j,+1) for j=0..39 and 40 pairs (c_j+1,-1) for j=0..39 each give hint 1 (80 total); 944 interior pairs (j*alpha mod q,+78) each give hint 0 since 78<<95232 stays in-block; all |z|<=78; per-pair UseHint(h,r)==HighBits((r+z) mod q) for all 1024 pairs (0 errors); flipping one further pair (c_41,+1) yields 81 hints and the weight<=80 rule rejects it, mirroring FIPS 204 verification. The auditor independently re-implemented the scalar routines and re-verified all 80 flips, interior non-flips, totals, and interval disjointness (spacing 190464 >> 156), and inspected census.json/witness.json (sums, counts, error lists).

## Limitations
The upper-bound half is the standardized verifier's definitional rejection rule, not a distributional statement about honest signing frequencies. The census covers adversarially realizable single-coefficient shifts within the beta=78 budget; it does not model cross-coefficient correlations of challenge multiples c*s nor signer-induced hint distributions. The witness uses minimal boundary-crossing shifts, not a full Dilithium signing trace. All checks use exact integer arithmetic (no floating point).

## Reproducibility
python3 output/artifacts/census_script.py  # regenerates census.json (~8 s)
python3 output/artifacts/witness_script.py # regenerates witness.json (instant)
Both scripts assert key identities and fail loudly on mismatch. Artifacts preserved: census_script.py, witness_script.py, census.json, witness.json.

## References
1. NIST FIPS 204, Module-Lattice-Based Digital Signature Standard (2024).
2. CRYSTALS-Dilithium reference implementation and specification (pq-crystals/dilithium).
3. lattices.io Dilithium/ML-DSA implementation guide (HighBits/LowBits/hint description).
4. postquantum.wiki ML-DSA entry (parameter sets).
5. IETF draft-connolly-cfrg-ml-dsa-security-considerations-01 (signing/verification context).
