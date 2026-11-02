# Scientific review

## Correctness — PASS
For each of the 256 three-block Boolean predicates, the suffix/parity transducer gives the binary pattern-counting sequence, Moore refinement gives its intrinsic minimal DFAO, and exhaustive incoming-label profile reachability gives the shortest inhomogeneous path or proves none exists. The shortest path lengths are 2 for masks 0, 68, 136, 204; 3 for masks 85, 170; 4 for mask 255; and nonexistent for the other 249 masks. By Allouche–Yao's normalization, the resulting opacity values are 1, 1/2, 1/4 and 0. Direct numeral-output comparisons are corroborative; the finite-state graph argument is what supports the infinite statement. The identity u_F(1ab)=1_{1ab in F} and the analogous identity for u_F(10ab) recover all eight mask bits, establishing distinctness.

## Originality — PASS, with priority limitations
The foundational Allouche–Yao theorems give a general procedure for any automatic sequence, not a table of all 256 predicates. Earlier all-one-pattern sequences and ordinary Rudin–Shapiro-related work study smaller families or different invariants. XOR combinations are not classified merely by knowing the individual-pattern opacity values, because the intrinsic quotient can change. The complete exceptional-mask set and numerical census were not located as previously published results in the inspected literature, though an unindexed or unpublished exact census is possible.

## Value — PASS
This is a natural exact classification of all binary three-block local parity predicates, distinguishing 249 transparent and seven nontransparent cases. The explicit exceptions demonstrate the nonadditive behavior of opacity under XOR and provide a finite reference case for future analyses of larger windows.

## Scope
The proof and verification apply exactly to ordinary binary representations, normalized prefix-metric opacity and the 256 length-three predicates; they do not establish any classification at longer window lengths. Formal proof-assistant verification and external expert attestation are not asserted.

## References
J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences. The general case*, arXiv:2404.13601, published in *Acta Informatica* 63:7 (2026). R. J. Hendel, *Runs, Squares, Palindromes, and Unbordered Factors of a Family of Binary Pattern Sequences with the All-One Pattern*, arXiv:2505.20547.
