# Scientific review

## Correctness
PASS. The greedy arch count is the binary subsequence-universality index by the first-complete-arch argument. The six-state potential controls the adjusted prefix length under all admissible transitions; at a Dyck return its value is nonpositive. Explicit full-height mountain witnesses attain both parity cases. The attached independent finite dynamic program and complete small-Dyck census agree with the formula. This is an unbounded symbolic proof, not an inference from finite sampling.

## Originality
PASS, subject to ordinary bibliographic risk. The closest full primary works are Barker et al. (2020), which establishes arch factorization and general universality; Schnoebelen and Veron (2023), which studies arch algorithms and compressed inputs; Mol, Rampersad, and Shallit (2023), which studies bounded Dyck nesting height for repetition avoidance; and Adamson et al. (2023), which studies universal words in regular languages. None of those inspected results supplies the sharp global extremal height/index formula. An earlier general binary transition-edge representation alone does not imply the height-constrained extremal optimization without the potential proof. Equivalent results may exist under different language/path formulations.

## Mathematical value
PASS. Height is the standard Dyck nesting-depth invariant, while the index measures coverage of all scattered binary patterns. The theorem supplies a sharp universal lower bound and an infinite exact extremal classification at every height and index; it quantifies a genuine tradeoff between context-free nesting complexity and scattered-pattern universality, not an arbitrary finite slice or a restatement of greedy-arch computation.

## Scope and limits
The proof is restricted to Dyck words over the fixed binary alphabet. It does not classify all extremizing words or determine the whole joint distribution. The claims have not received independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
