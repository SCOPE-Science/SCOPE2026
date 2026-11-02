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

Reproduce using a Python 3 interpreter and the included `verify_f3.py`: `python3 verify_f3.py`. The script uses integer `math.comb` and modular remainder, independently from the Lucas/Kummer proof. Observed output: `VERIFY_OK b_range=1..150 exact_divisibility_tests=4276 higher_depth_witnesses=6`.

For every positive \(b\), the proof reduces all failures to \(3\nmid\binom{(b+3)n}{3n-1}\) with \(3\mid bn+1\), by a free cyclic action and an exact adjacent-binomial identity. Base-three carry counts resolve the complementary case. In the nontrivial residue class, Lucas digit comparison forces \(n\ge(3^s+1)/2\), where \(s=\nu_3(b+2)\), and a digitwise witness attains equality. The program checks finitely many instances, not every integer. Neither external certification nor an independent audit has been performed.
