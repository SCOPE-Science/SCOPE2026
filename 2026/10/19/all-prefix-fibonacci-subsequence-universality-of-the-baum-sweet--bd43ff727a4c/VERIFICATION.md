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

# Reproducible checks

Run `python3 bs_universality_verify.py` with Python 3. The program independently computes Baum–Sweet digits from explicit binary zero runs and a parity automaton; verifies these agree below index 65536; checks every prefix length 1–2048; checks selected dyadic cutoffs and boundaries immediately around powers of four up to 65536; verifies every adjacent `11` index below 65536; and verifies the Fibonacci count and arch formula at dyadic prefixes through length 65536. The expected result begins `VERIFY_OK`.

The independently implemented backwards next-occurrence recurrence computes the shortest absent scattered subsequence length, not just the greedy arch count. Both agree with the claimed formula on the tested finite cases. Neither this check nor its log is a proof of the infinite quantified result: that result uses the digit-carry lemma, arch lemma and Fibonacci regular-language count in `RESULT.md`.
