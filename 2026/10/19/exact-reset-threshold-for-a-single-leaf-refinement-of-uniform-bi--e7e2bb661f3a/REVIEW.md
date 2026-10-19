# Scientific review

## Correctness
**PASS.** For arbitrary \(m\ge2\), the proof fully specifies the prefix code, state space, total transition, and reset-word quantifier. The upper bound is a direct state-image calculation. For the lower bound the completed-codeword length equation \(L+h=mK_h+E_h+f\) gives all \(m\) distinct residues of the long-word count. Its largest residue either forces a normal initial word plus \(m-1\) long ones, or forces an explicit hypothetical word of length \(m^2-1\), which is then contradicted using states \(\varepsilon\), \(0\), and \(1\). The endpoint \(m=2\) is included. Standalone subset-BFS tests for \(2\le m\le9\) corroborate but do not replace the infinite proof.

## Originality
**PASS, subject to historical-priority risk.** Actual equivalence and implication searches compared a single refined leaf against general literal prefix-decoder algorithms, the different first-letter-subtree refinement of Ryzhikov–Szykuła (2018), general upper bounds in Berlinkov–Ferens–Ryzhikov–Szykuła (first public 2021, revised 2026), and contemporary synchronization surveys. None of the inspected full texts establishes this exact family-specific result. The Biskup–Plandowski (2009) abstract discusses long-synchronizing families but its complete constructions could not be inspected: it is a material residual risk, not proof of noncoverage. Search misses alone do not establish novelty, and independent historical-priority verification remains necessary.

## Value
**PASS.** Fixed-length binary codes have a modular decoding obstruction to synchronization. Refining only a single leaf is the smallest possible departure from that structure, and its exact all-depth reset threshold is an intrinsic error-recovery invariant, not an arbitrary finite sample. The proof identifies an explicit resynchronization word and an arithmetic obstruction excluding every shorter word, furnishing a motivated structural model for almost-uniform source codes. This family result does not purport to settle general shortest-reset algorithms.

## Scope and risks
Complete binary prefix codes and literal decoders only; no comparison with the state-minimized recognizer and no generalization to arbitrary modified leaves. The 2009 source was not available in full, and the 2026 survey was accessible only by abstract/preview. Finite checker runs cannot certify the all-parameter theorem independently of the proof.

Self-review: passed. Independent audit: not yet performed.
