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

The universal argument is analytic. The bundled exact-rational checker verifies representative sharp constructions without replacing the proof.

- For the source ratio \((L,U)=(4,1)\), it verifies \(L>2U\) and the formula \(2+\lfloor U/(L-U)\rfloor=2\).
- For \((L,U)=(7/4,1)\), it verifies a sharp threefold-overlap construction.
- For \((L,U)=(3/2,1)\), it verifies a sharp fourfold-overlap construction.
- For \(L=U=1\), it verifies arbitrary requested finite overlap multiplicity, illustrating the absence of a universal bound.
- At \(L=2U\), it verifies a legal two-repair example with \(p_2=v_1\), certifying sharpness of the strict separation threshold.

All arithmetic in these checks is exact rational arithmetic. The script does not enumerate all repair systems, and no finite test is used as evidence for the universal theorem.
