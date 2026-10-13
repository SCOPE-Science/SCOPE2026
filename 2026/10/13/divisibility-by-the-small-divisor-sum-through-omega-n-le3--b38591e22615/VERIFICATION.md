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

The symbolic proof in `RESULT.md` is the verification basis. The included `verify.py` is an independent finite regression check: it factors every integer \(2\le n\le300000\), restricts to \(\Omega(n)\le3\), computes the small-divisor sum directly from divisor pairs, and compares the actual divisibility condition with the theorem's classification.

Expected output:

`VERIFY_OK limit=300000 checked=168640 solutions=26009 composite_solutions=6,12,18,28,45,117,475,775,2009,13189,... mismatches=0`

The finite check does not establish behavior beyond its cutoff and is not used to prove any infinite branch.
