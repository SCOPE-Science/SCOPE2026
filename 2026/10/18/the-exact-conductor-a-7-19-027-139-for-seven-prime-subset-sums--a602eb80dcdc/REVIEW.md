# Review of the exact seven-prime-product conductor

## Correctness

**PASS.** The statement fixes squarefree summands having exactly seven distinct prime factors and forbids reuse. The exhaustive base certificate checks the exact subset-sum recurrence for all sums through \(40{,}000{,}000\); two independently coded enumeration and bitset methods agree that the final missing integer is \(19{,}027{,}139\). The next available coin is \(19{,}114{,}095\), while the represented interval above the claimed gap has length \(20{,}972{,}861\). Replacing the largest prime factor with its successor, using Bertrand's postulate, shows successive permitted products have ratio less than two. Overlapping translations then extend coverage to every larger integer. No statistical inference or unverified finite-to-infinite step is made.

## Originality

**PASS, with residual risk.** The originating Butler–Erdős–Graham paper explicitly asks to determine \(a(k)\) and lists exactly the first six values, ending at \(a(6)=894211\), without the present seventh value. Searches of research records, text-indexed literature, and exact-number aliases did not reveal a prior seventh value or a theorem that implies it. The closest published results on Egyptian fractions concern *reciprocals* or general coverage rather than the exact least integer subset-sum conductor. A potentially overlooked equivalent computation is possible, particularly under alternate terminology for squarefree almost-primes.

## Value

**PASS.** This resolves the next unreported exact value of a natural discrete invariant explicitly posed in the originating article, not an arbitrary finite cutoff. The source identifies the invariant as measuring the initial boundary of large consecutive subset-sum blocks in its Egyptian-fraction construction. The result determines both the last obstruction and the beginning of the infinite no-gap regime for seven-prime products. It does not claim an entire general sequence formula.

## Evidence and limitations

The full primary source was inspected in its exact setup and closing statement of the problem; a later Egyptian-fractions preprint was compared on definitions and scope. The proof relies on two self-contained finite checkers included with this claim, not a record of an incomplete experiment. A self-review has been performed; independent audit is not claimed.

Self-review: passed. Independent audit: not yet performed.
