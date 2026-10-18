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

# Reproduction and limits

Run `python3 verify.py` in the same folder as the accompanying scientific files; it uses Python standard-library integer arithmetic only, no network, and prints `VERIFY_OK` when all checks succeed. The code represents monomials as exponent tuples and truncates products whenever an exponent reaches \(d\). For each selected configuration it independently evaluates \(f^d\) and the proposed coefficient restriction, rather than merely substituting the closed formula.

## Actual saved-check outcomes

Exhaustive generator-image enumeration and invertible leading-matrix combination yielded 24 for \((r,d,q)=(2,2,2)\), 72 for \((2,2,3)\), 2048 for \((2,3,2)\), 25509168 for \((2,3,3)\), and 688128 for \((3,2,2)\). Deterministic sparse substitutions agreed in 12 of 12 sampled assignments for each of \((r,d,p)=(3,6,3),(2,6,3),(3,4,2),(2,6,2)\). The replay ended `VERIFY_OK`.

These tests are finite and do not prove the universal theorem. The universal proof uses the Nakayama argument, the nonzero mixed Frobenius-binomial coefficient, and the coefficient-of-\(t^{m-1}\) rigidity lemma in `RESULT.md`. The geometric conclusions concern the reduced automorphism parameter variety; no group-scheme smoothness assertion is verified.
