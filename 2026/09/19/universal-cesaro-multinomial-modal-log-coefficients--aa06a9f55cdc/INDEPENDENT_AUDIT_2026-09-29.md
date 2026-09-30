# Independent audit — 2026-09-29 UTC

Record: `2026/09/19/universal-cesaro-multinomial-modal-log-coefficients--aa06a9f55cdc`  
Assigned and audited source tree: `c368e53cf6782c2d9e707d799689209eff4502a6`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `cbfc40c7b61ee8ee71cb6c0af72abbae3b694f84`  
Disposition: **repaired**

## Correctness

**independently_supported**. The Jefferson/Janson transfer and Bernoulli generating-function calculation are correct. Bounded seat excesses turn Janson's weak random-house-size limit into convergence of every polynomial moment. The one-coordinate Bernoulli expectation reduces to e^w((e^w-1)/w)^(n-2), and Stirling coefficient extraction yields exactly the displayed probability-vector-independent constant. Independent symbolic checks reproduce -13/12, 5/8, -187/360 and 21/40 at n=3.

## Originality

**requires_repository_provenance_repair**. The all-order theorem is already in multinomial-mode-cesaro-universality--a66b1067c370, committed 2026-09-18T20:07:58Z, and the identical Bernoulli--Stirling formula is in multinomial-mode-cesaro-log-coefficients--69879bbdb548, committed 2026-09-19T08:07:59Z. This record first appeared at 20:31:49Z, so it cannot carry a separate originality claim.

## Scientific value

**useful_reproducibility_specialization**. The derivation and bundled verifier are useful, but the scientific contribution is corroborative relative to earlier repository results, one of which is strictly broader.

## Evidence and literature checked

- https://arxiv.org/abs/2609.20229
- https://arxiv.org/abs/1110.6369
- https://github.com/SCOPE-Science/SCOPE2026/commit/db7e5802b48553f80805eb9d24d52aff00815a75
- https://github.com/SCOPE-Science/SCOPE2026/commit/aab2545f5756d22a6a450d89976b12b828003a0c
## Limitations

- Assumes rationally independent fixed probabilities.
- Cesaro rather than pointwise convergence.
- No separate originality claim survives repository chronology.
