# Independent mathematical audit

## correctness

PASS

Reconstructed the repaired proof. Gohn et al. supply the maximum length. Independently, two terms in the same units-digit block force its prefix digit product to be one. A start at residue b−1 would include two final digits b−1 separated by b. At residues 1 through b−2 the first two prefixes must be binary and consecutive, forcing the first to end in 0; either a third prefix would have to be binary despite ending in 2, or the run contains a final digit divisible by ell_b in its first block and final digit ell_b in its second block, forcing ell_b to divide b. Thus the start is b²c. The first full block is equivalent to binary c and L_b|b²c; the last ell_b terms then follow. Valuations at primes dividing b give the trailing zeros; ONLY M_1 has to be coprime to b. Verified each nontrivial Fourier factor bound, including the empty product, the fixed-prefix counts, both strict cutoffs and the endpoint comparison giving Theta bounds. Base 3 gives E_3(m)=2^(m−2) for m≥2 and first start 36 by parity. Replay: repairs/3/RESULT.md. Frozen verify.py was inspected, not executed; no finite test substitutes for the proof.

## originality

PASS

For the repaired claim only: the known boundary theorem and elementary start reformulation are excluded from the originality claim. The inspected sources do not establish the quantitative longest-run census, fixed-prefix distribution, and two explicit global counting constants as a result or corollary. Standard Fourier methods are not claimed as new.

## value

PASS

Counting and locating longest runs is a natural question left by the known length theorem. The modulus and valuation parameters give explicit predictive shell counts; the fair-digit limit and two computable incompatible global power-law constants show a distributional phenomenon not conveyed by the existence or length of runs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
