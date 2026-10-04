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
The exact arithmetic verification is supplied in `verify.py`.

It checks that the printed first branch holds for every positive \(n<12\) to which that branch applies, then fails at \(n=12\). It separately checks that the printed second branch holds at every positive multiple of \(8\) below \(24\), then fails at \(n=24\).

The proof that \(p-1\mid\lambda(m)\) whenever a prime \(p\mid m\) is not inferred from this finite check. It follows symbolically from the standard prime-power least-common-multiple formula and is the implication used in the published Lemma 3.
