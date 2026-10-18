# Scientific review

## Correctness — PASS

The claim is precisely restricted to nonempty subsets of eight binary words of length three. Every one of the 255 input sets is covered. A complete independent enumeration of all binary superstrings of lengths three through ten proves optimal lengths, since a ten-character binary de Bruijn linearization covers every input. All legal ordered greedy tie choices are visited by a finite recurrence whose number of active strings strictly decreases. There are 7405 distinct reachable canonical states. Exact rational maximization yields \(10/7\), four equality cases, and the size-conditioned spectrum. An independent Hamiltonian-path dynamic program checks all 255 optimum values. The explicit witness and its legal merge trace are available in RESULT.md. The checker was run successfully from the included package.

## Originality — PASS within checked literature

The closest 2026 primary result establishes \(\rho_3=9/5\) over unrestricted alphabets, which does not imply the sharper fixed-binary value nor classify the four extremizers; the 2024 strengthening and compression papers study different, broader inequalities. Actual published-record and published research-index searches for binary three-letter words, greedy superstring, worst tie-breaking, exact ratios, and the specific numerical value found no direct match. The full text of arXiv:2608.20018 could not be retrieved; its appendices could contain a covering fixed-binary calculation. This is an acknowledged, unresolved source risk, not proof of uniqueness.

## Value — PASS

The result fixes both alphabet size and input length at their first nontrivial binary regime, a canonical finite restriction of the 2026 exact length-three greedy-ratio problem. In contrast to the unrestricted \(9/5\) result, the exact binary maximum is \(10/7\). The complete size-refined profile and unique symmetry orbit of extremizers identify which instances cause poor tie-breaking, giving exact small-alphabet benchmarks. This is a full classification of a motivated natural domain, not a lone unmotivated test or parameter change.

## Residual limitations

The finite result does not extend to arbitrary alphabet sizes or lengths. The central 2026 preprint was inspected only through its abstract and technical secondary description because full-text access failed; possible hidden prior coverage is explicitly recorded. Independent scientific audit has not yet occurred.

Self-review: passed. Independent audit: not yet performed.
