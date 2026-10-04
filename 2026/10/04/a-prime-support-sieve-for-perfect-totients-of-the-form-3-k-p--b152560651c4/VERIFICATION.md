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

The symbolic proof reduces the theorem to the exact inequality \(F(m)\le2\phi(m)-1\) for even \(m\). That inequality is proved by induction in `RESULT.md`; no finite search is needed for the infinite claim.

The bundled `verify.py` reimplements Euler's totient and the complete totient-orbit sum from integer arithmetic. It checks the orbit inequality for every even \(m\le20000\), then checks every prime \(p\le200000\) and every exponent \(2\le k\le8\). Whenever \(3^k p\) is a perfect totient in that finite domain, it checks the exact cross-multiplied form of the support inequality and the three stated congruence exclusions.

Replay output:

`VERIFY_OK limit=200000 kmax=8 even_checked=10000 target_hits=[(2, 619, 5571, 103), (3, 1733, 46791, 433), (2, 1747, 15723, 97), (3, 5189, 140103, 1297), (2, 49003, 441027, 8167)] sieve_violations=0`

The computation is finite corroboration only. It does not establish the theorem outside its tested bounds, and it does not resolve existence of perfect totients \(3^k p\) for \(k\ge4\).
