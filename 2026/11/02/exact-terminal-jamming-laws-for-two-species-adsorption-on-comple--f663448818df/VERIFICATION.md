---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

Run `python3 check_jamming.py` with a standard Python 3 interpreter. The script uses only `fractions`, `functools`, and `math` from the standard library. It independently computes absorption probabilities for each allowed state of the continuous-time process by enumerating all successful vertex/species transitions with exact rational rates. It compares this recursion with the theorem's closed formula for every unordered multipartite part-size partition with total order from \(2\) to \(8\), for \(p\in\{1/4,1/3,1/2,2/3,3/4\}\). The same script checks the separate symmetric binomial identity for every \(1\le n\le150\).

Observed result: `PASS: 290 exact Markov-chain distributions, 1169 assertions; n=1..150 binomial identities`.

For the exact theorem, the indispensable argument is the competition between the first successfully proposed outside species and first opposite-species attempt at a still-vacant vertex of the initial part. The finite binomial sums follow by integrating exponential clocks. The infinite-size mixture uses weak convergence of these clocks and bounded convergence; its validity is not inferred from numerical limits. The \(3/(8n)\) correction is established by the exact centered-binomial identity and the bounded fourth-moment remainder, not the finite numerical tests.

No independent mathematical validation or exhaustive historical-priority determination has been performed.
