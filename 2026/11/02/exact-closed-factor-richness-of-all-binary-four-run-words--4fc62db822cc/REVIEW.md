# Scientific review

## Correctness — PASS

The proof classifies closed factors by their one, two, three or four runs, proves that all possibilities have been exhausted, and counts distinct words without duplicate identifications. The maximum and its equality cases follow by a sharp integer-product inequality; the generating function follows by enumerating all same-letter run pairs with a fixed minimum. The extracted standalone checker independently compares two definitions of closedness and the explicit class decomposition for all four-run words of lengths \(4\) through \(16\), checks additional longer samples and the generating-function coefficients. These computations support, but do not replace, the all-length proof. No unstated generic-position or parity assumption is used.

## Originality — PASS (with priority qualification)

The full text of Badkobeh–Fici–Lipták, arXiv:1305.6395, explicitly gives the CR-poor characterization and a four-block construction with a quadratic **lower bound**, rather than the exact four-run factor formula or complete extremizer counts. The relevant sections and statements of Parshina–Puzynina, arXiv:2111.00863, establish an **unrestricted asymptotic maximum** and cite the four-block construction without giving this restricted exact theorem. The closest indexed research claim about exact maxima at lengths \(25\)–\(27\) concerns unrestricted binary words and likewise does not entail an all-length four-run enumeration. Multiple actual literature and mathematical-record searches found no equivalent formula. This is a best-knowledge assessment, not proof that no unindexed prior presentation exists.

## Value — PASS

Four runs are the first binary run class permitting any closed-factor excess above the baseline \(n+1\): every at-most-three-run word is a factor of a bitonic word. The 2013 foundational paper already uses this precise four-block shape to demonstrate quadratic growth, which makes the exact all-length count, the sharp quadratic coefficient \(1/16\), complete equality classification and generating function natural targets rather than arbitrary narrow parameters. They distinguish the four-run class from the unrestricted \(1/6\) leading coefficient, without claiming an unrestricted solution.

## Closest literature and limitations

- Badkobeh, Fici, Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395, full text examined; its stated lower bound and bitonic characterization do not determine the formula proved here.
- Parshina, Puzynina, *Finite and Infinite Closed-Rich Words*, arXiv:2111.00863, relevant primary text and bounds examined; its global asymptotic result is not a four-run exact classification.
- Restricted scope: exactly four runs, positive exponents, binary alphabet, distinct contiguous linear factors, empty factor included. Unindexed results remain a priority risk, and no independent audit was undertaken.

Self-review: passed. Independent audit: not yet performed.
