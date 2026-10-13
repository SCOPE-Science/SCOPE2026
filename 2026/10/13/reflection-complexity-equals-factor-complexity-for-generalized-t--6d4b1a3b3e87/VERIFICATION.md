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
# Verification

Run `python3 verify.py` beside `certificate.json`.

The verifier checks the exact first-difference identity on \(900000\) index/modulus instances for \(3\le\ell\le20\), and checks the local length-\(4\) reversal obstruction on \(899946\) instances.

It separately enumerates \(285452\) observed factors from long prefixes for \(3\le\ell\le9\) and lengths through \(48\), confirming that reversible length-\(3\) factors are palindromes and that no observed factor of length at least \(4\) has an observed reversal.

For \(\ell=4\), the first factor/reflection-complexity pairs at lengths \(1,\ldots,6\) are
\[
(4,4),(16,10),(28,28),(44,44),(56,56),(72,72).
\]

These computations stress-test the proof. The theorem for every modulus and every length follows from the symbolic argument in `RESULT.md`, not from finite extrapolation.

Independent audit has not been performed.
