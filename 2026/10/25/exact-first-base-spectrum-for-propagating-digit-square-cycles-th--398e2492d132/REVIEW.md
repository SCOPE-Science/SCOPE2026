# Review of the first-base spectrum for propagating digit-square cycles

## Correctness

PASS. Every propagating cycle lies in the eligible two-digit graph. Exhaustive graph traversal by two independently implemented methods and direct witnesses prove the nineteen minimal first bases. The C++17 verifier was compiled and run successfully with exact arithmetic and no extrapolation.

## Originality

PASS relative to inspected primary literature, relevant records and accessible preceding claims. Lorenzini et al., *Integer Dynamics*, Remark 2.13, asserts a nonsharp-in-form existence bound through length twenty, without giving this minimal-base spectrum or proving the common cutoff sharp. Their length-seven first-base example is already known and is not claimed as an independent discovery. Other data and unindexed tables remain an originality risk.

## Mathematical value

PASS. The full first-occurrence invariant over the source-motivated range \(2\le\ell\le20\) and the exact sharp uniform cutoff of \(1230\) address a specific computational gap in the source and show a strongly nonmonotone dependence on cycle length. The claim is finite and does not infer general growth laws.

## Limitations

Cycles with more than two digits, with a zero trailing digit, or lengths beyond twenty are not covered. Any unpublished source computation may contain the same table. No independent external verification is claimed.

Self-review: passed. Independent audit: not yet performed.
