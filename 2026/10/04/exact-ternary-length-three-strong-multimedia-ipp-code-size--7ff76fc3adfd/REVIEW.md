# Review

## Correctness
PASS. The published length-three bound gives at most \(12\) codewords at alphabet size \(3\). The proof then reduces the SMIPPC definition to an exact local uniqueness condition inside each pair descendant box. The bundled standard-library verifier generates every minimal forbidden configuration from that definition, directly verifies the explicit \(11\)-word code, and exhausts the three symmetry-normalized possibilities for a hypothetical \(12\)-word code. No branch reaches size \(12\).

## Originality
PASS. The 2014 archive source proves only the upper bound \(12\) in the ternary case and constructs optimal codes for alphabet sizes congruent to \(0,1,2,5\) modulo \(6\). The complete 2024 follow-up still concludes with optimal constructions only for alphabet sizes not congruent to \(3\) or \(4\) modulo \(6\). Exact-parameter, expanded-name, parent-set, and nearby traceability-code searches found no statement implying the exact value \(11\). A residual risk remains that an unindexed small-parameter computation exists elsewhere.

## Value
PASS. Alphabet size \(3\) is the smallest case in an omitted congruence class of the published optimal-construction program. Showing that the general upper bound drops by one here settles a natural first boundary case for a fingerprinting-code notion designed for efficient colluder tracing.

## Closest literature and limitations
The closest archive source is arXiv:1411.6841v1, which defines the object, proves the general upper bound, and gives constructions in four congruence classes. The 2024 Designs, Codes and Cryptography paper revisits precisely the same length-three problem and still excludes alphabet sizes congruent to \(3\) or \(4\) modulo \(6\) from its optimal-construction theorem. The present result is only for the ternary case and does not classify all extremizers or settle larger omitted alphabets.

Same-model review: passed. Independent audit: not yet performed.
