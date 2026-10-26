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

# Verification of the rank-four pentagon-blow-up census

The mathematical reduction uses the four-move part-preserving Ehrenfeucht–Fraïssé strategy. The finite exhaustive phase covers all \(4^5=1024\) positive clone-size vectors with coordinates in \(\{1,2,3,4\}\); each extension orbit is either a repeated selected vertex or an unused vertex in one part. The exact recursive game signature is therefore calculated without pruning admissible move types.

The independently coded labelled-graph oracle visits every vertex, without quotienting clones, for all \(3^5=243\) graphs having sizes in \(\{1,2,3\}^5\). The classification agrees on all \(29403\) distinct pairs. The independent oracle has the same standard logical semantics but a different state space from the quotient implementation.

Recorded commands, from the directory containing the attached files:

```text
python verify_c5.py
```

The command writes `c5_class_table.csv`, containing \(1024\) data records plus one CSV header. The accompanying `verify_c5_output.txt` records `VERIFY_OK`, `CAP3_STABILITY_OK`, and `ORACLE_OK` together with the class representatives. The critical numerical claims are exactly \(33\) rank-four types, optimal minimum representative order \(15\), and one class attaining that minimum order.

The machine check is complete on the clipped finite domain. The mathematical argument lifting that certificate to arbitrary finite clone sizes is the four-pebble strategy recorded in the proof. Neither code execution nor a finite census alone would prove the infinite claim in the absence of that reduction.

Independent external validation has not been performed.
