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

# Verification and scope

The accompanying `verify.py` independently generates Fibonacci and Lucas terms modulo \(2^m\) from their initial values and checks both claimed mixed-sumset identities, including every admissible and inadmissible residue, for all \(3\le m\le12\). It also verifies the shift congruences for \(G_t=F_{6t}/8\) and \(J_t=G_t+G_{t+1}\) for 576 parameter instances with \(0\le r\le8\) and \(0\le t<32\).

Observed execution output:

```text
VERIFY_OK modulus_exponents=10 shift_congruences=576 largest_modulus=4096
```

The infinite identities follow from the formal generating-function identity, Vandermonde's formula, the elementary binomial valuation inequality and the residue-lifting induction in `RESULT.md`. The finite script is cross-checking evidence only, not a proof of infinitely many cases. The analysis does not address prime-pair asymptotics, bounded recurrence indices or arbitrary odd summands. Independent audit: not performed.
