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

# Verification details

Run `python3 verify.py`. The script is self-contained (standard library only), uses exact rational arithmetic for all \(817\) finite comparison states and \(C_{820}\), and computes reduced Farey product prime valuations independently by enumerating coprime numerator–denominator pairs at small primes. This exercises the normalization \(\nu_p(d/a)\), validates the denominator jump \((p-1)\varphi(m)\), and confirms the size of the prime-scale error. The uniform theorem for all \(p>1{,}344{,}800\) follows from the explicit inequality proved in `RESULT.md` and the finite exhaustive rational certificate, rather than treating small-prime examples as proof. These are self-review; independent audit is not performed.
