# Scientific assessment

## Correctness — PASS

The necessity construction has exactly four candidates and nonempty ballots of size at most two; the least winning score is \(\lfloor2(n-\lceil n/3\rceil)/3\rfloor\), which exceeds the losing candidate's score in exactly the stated negative population region. The positive direction uses a maximum-coverage selection among welfare maximizers and forces the only possible non-improving exchange into an equality case, where a second exchange increases coverage. Both boundary assertions have independent counting proofs. The standalone finite-domain verifier reproduced the claimed threshold in 850,550 enumerated anonymous approval profiles and the constructed examples through 100 voters. These finite tests do not substitute for the all-population proof.

## Originality — PASS, with documented residual priority risk

The closest established result is Elkind et al., *The Price of Justified Representation*, arXiv:2112.05994: the full manuscript treats welfare optimization constrained by JR, asymptotic welfare losses, algorithms and selected general constructions, not the exact sparse-ballot, three-seat, population-dependent compatibility threshold. Becker, Greger and Peters, arXiv:2609.11912, show that a core committee always exists, but do not require that it also maximize approval count. The original JR existence paper likewise does not impose welfare optimality. Targeted searches of mathematical records, primary texts and available previous research claims found no implication equivalent to the complete phase criterion. Index incompleteness and unrecognized formulations of the sparse-ballot case remain priority risks; a failed search is not a uniqueness proof.

## Value — PASS

The result gives a natural exact zero-price-of-JR phase law in a highly constrained voting environment; it identifies the first failure, an unusual return of compatibility at populations ten and eleven, complete all-size obstructions thereafter by residue, and minimal committee and ballot-size dimensions. The sharp boundary is not a mechanical restatement of general welfare-approximation bounds and is relevant to design of limited-approval elections.

## Scientific limitations

Only binary approval valuations, a three-seat committee and at most two approvals per voter are covered by the main equivalence. The boundary assertions separately concern two seats and singleton ballots; no general welfare-loss magnitude is asserted. The proof is mathematical, not a formal machine certification. The finite verifier's test domain is explicitly bounded.

Self-review: passed. Independent audit: not yet performed.
