# Scientific review

## Correctness — PASS

The domain consists of all integer alphabet sizes \(k\ge2\), all three ordered two-digit words, and Lebesgue initial data. The exact identity \(S_{3m}=k^{-3m-1}u^\top(A_1A_2A_3)^m u\) follows from digit counting. The cubic product has rank two. Its trace and second elementary symmetric coefficient are proved by a matrix expansion and an exterior-square contraction, fixing both the sign and cyclic wraparound term. The positive spectral root governs survival; a nontrivial Jordan block accounts for the exceptional binary polynomial prefactor. The strict ordering is verified by evaluating neighboring quadratics at each other's leading root. The displayed minimal-order counterexample follows from exact two-by-two multiplication. The included integer-arithmetic checker returned `VERIFY_OK` for exhaustive alphabets \(k=2,3,4,5\); it corroborates but does not replace the symbolic proof.

## Originality — PASS, with residual risk

The most relevant full texts inspected were Livorati et al., arXiv:1312.7030v2 (moving/breathing intervals, Ulam computations and overlap approximations), and Cheriyath–Agarwal, arXiv:1905.11767v5 (fixed simultaneous unions of forbidden cylinders, not a periodically varying single cylinder). Standard transfer matrices and static Markov-hole spectral arguments are prior techniques, not claimed novelties. Existing exact two-stage and randomized switching results do not state or imply the four-class three-stage spectrum or the minimal order-only escape-rate transition. Statement-level overlap searches found no direct match. Residual risks include an equivalent older periodic matrix-product formulation not captured by the reviewed sources; absence of a search match is not a proof of absolute novelty.

## Mathematical value — PASS

The natural question is whether the ordering of equal-exposure moving Markov holes changes eventual escape, not merely survival at one finite horizon. Two time slots cannot produce a rate difference by permuting the same holes, whereas three slots can. The theorem classifies *every* three-slot protocol into four exact, strictly ordered dynamical rate classes for every alphabet size, counts their multiplicities, and identifies a qualitative Jordan-prefactor boundary. The explicit binary example isolates temporal ordering while keeping each hole and its frequency fixed. The result is not an arbitrary parameter slice or a numerical improvement.

## Limits

No claim is made about higher-word cylinders, nonuniform measures, continuously moving non-Markov holes, or independent novelty certification. The finite checker establishes only its stated test instances.

Self-review: passed. Independent audit: not yet performed.
